"""
Manages translation of markdown and image files for a project.
"""
from pathlib import Path
import logging
from typing import List, Dict, Any, Tuple, Optional, Set, Callable
from tqdm import tqdm
import re
import json
import os
import asyncio

from ..utils.common.file_utils import (
    read_input_file,
    filter_files,
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
    get_filename_and_extension,
    generate_translated_filename,
    handle_empty_document,
)
from ..utils.common.metadata_utils import calculate_file_hash
from ..llm.markdown_translator import MarkdownTranslator
from ..llm.jupyter_notebook_translator import JupyterNotebookTranslator
from .base_structure import ProjectStructure
from ..config.constants import SUPPORTED_IMAGE_EXTENSIONS
from ..utils.common.task_utils import worker
from ..utils.llm.markdown_utils import compare_line_breaks

logger = logging.getLogger(__name__)


class TranslationManager:
    """Manages translation of markdown and image files for a project.

    Coordinates file discovery, translation tasks, and maintains translation metadata
    to efficiently track and update translations.
    """

    def __init__(
        self,
        project_structure: ProjectStructure,
        image_dir: Path,
        excluded_dirs: List[str],
        supported_image_extensions: List[str],
        supported_notebook_extensions: List[str],
        markdown_translator: MarkdownTranslator,
        image_translator=None,
        notebook_translator=None,
        markdown_only: bool = False,
    ):
        """Initialize translation manager with project configuration.

        Args:
            project_structure: Project structure handler
            image_dir: Directory for translated images
            excluded_dirs: List of directories to exclude from translation
            supported_image_extensions: List of file extensions for images
            supported_notebook_extensions: List of file extensions for notebooks
            markdown_translator: Translator for markdown files
            image_translator: Translator for image files
            notebook_translator: Translator for notebook files
            markdown_only: Whether to translate only markdown files
        """
        self.project_structure = project_structure
        self.root_dir = project_structure.root_dir
        self.translations_dir = project_structure.translations_dir
        self.language_codes = project_structure.language_codes
        self.image_dir = image_dir
        self.excluded_dirs = excluded_dirs
        self.supported_image_extensions = supported_image_extensions
        self.supported_notebook_extensions = supported_notebook_extensions
        self.markdown_translator = markdown_translator
        self.image_translator = image_translator
        self.notebook_translator = notebook_translator
        self.markdown_only = markdown_only
        self.evaluation_results = {}
        self.metadata_cache = {}

    async def translate_markdown_files(
        self,
        files_to_translate: Dict[str, List[Path]],
        delete_existing: bool = False,
        evaluation_mode: bool = False,
        fix_mode: bool = False,
        min_confidence: float = 0.7,
        concurrent_tasks: int = 10,
    ) -> Dict[str, Dict[str, Any]]:
        """
        Translate markdown files to target languages.

        Args:
            files_to_translate: Dictionary mapping language codes to lists of files to translate
            delete_existing: Whether to delete existing translations
            evaluation_mode: Whether to run in evaluation mode (record quality metrics)
            fix_mode: Whether to run in fix mode (only translate low-quality files)
            min_confidence: Minimum confidence threshold for fixing translations
            concurrent_tasks: Maximum number of concurrent translation tasks

        Returns:
            Dictionary containing translation results and statistics
        """
        total_results = {}
        total_files = sum(len(files) for files in files_to_translate.values())
        
        if total_files == 0:
            return {"files_translated": 0, "languages": {}}

        overall_progress = tqdm(total=total_files, desc="Overall Progress", unit="file")

        # Load evaluation results if in fix mode
        if fix_mode:
            self._load_evaluation_results()

        # Setup semaphore to limit concurrent tasks
        semaphore = asyncio.Semaphore(concurrent_tasks)

        # For each language code
        for lang_code, files in files_to_translate.items():
            # Skip if no files to translate
            if not files:
                continue

            # Delete existing translations if requested
            if delete_existing:
                self._delete_existing_translations(lang_code)

            # Create tasks for each file
            tasks = []
            for file_path in files:
                # Skip translation if in fix mode and file doesn't need fixing
                if fix_mode and not self._needs_fixing(file_path, lang_code, min_confidence):
                    overall_progress.update(1)
                    continue

                # Create task for translating file
                task = self._create_translation_task(
                    semaphore, file_path, lang_code, evaluation_mode
                )
                tasks.append(task)

            # Run tasks concurrently
            results = await asyncio.gather(*tasks)

            # Update total results
            language_results = {
                "files_translated": len(results),
                "successful": sum(1 for r in results if r["success"]),
                "failed": sum(1 for r in results if not r["success"]),
            }
            total_results[lang_code] = language_results
            overall_progress.update(len(files))

        # Close progress bar
        overall_progress.close()

        # Summarize results
        total_results["files_translated"] = sum(
            lang_results["files_translated"] for lang_results in total_results.values() if isinstance(lang_results, dict)
        )
        total_results["languages"] = {
            lang: results for lang, results in total_results.items() if isinstance(results, dict)
        }

        return total_results

    async def _create_translation_task(
        self,
        semaphore: asyncio.Semaphore,
        file_path: Path,
        lang_code: str,
        evaluation_mode: bool = False,
    ):
        """
        Create an async task for translating a file.

        Args:
            semaphore: Semaphore to limit concurrent tasks
            file_path: Path to the file to translate
            lang_code: Target language code
            evaluation_mode: Whether to run in evaluation mode

        Returns:
            Task for translating the file
        """
        async def translate_task():
            async with semaphore:
                return await self._translate_markdown_file(
                    file_path, lang_code, evaluation_mode
                )

        return await translate_task()

    async def _translate_markdown_file(
        self, file_path: Path, lang_code: str, evaluation_mode: bool = False
    ) -> Dict[str, Any]:
        """
        Translate a single markdown file.

        Args:
            file_path: Path to the markdown file
            lang_code: Target language code
            evaluation_mode: Whether to run in evaluation mode

        Returns:
            Dictionary containing translation results
        """
        try:
            # Get content of markdown file
            content = read_input_file(file_path)
            if not content or handle_empty_document(content):
                return {"success": True, "skipped": True, "reason": "empty_document"}

            # Get translation path
            translation_path = self.project_structure.get_translation_path(file_path, lang_code)
            translation_dir = translation_path.parent
            translation_dir.mkdir(parents=True, exist_ok=True)

            # Translate content
            translated_content = await self.markdown_translator.translate_markdown(
                content, lang_code, file_path
            )

            # Format translation metadata using project structure
            metadata = {
                "original_file": str(file_path.relative_to(self.root_dir)),
                "language_code": lang_code,
                "hash": calculate_file_hash(content),
                "translated_at": "AUTO-GENERATED - DO NOT EDIT",
                "description": f"Translation of {file_path.name} to {lang_code}",
            }
            
            # Format metadata using project structure
            formatted_metadata = self.project_structure.format_metadata(
                metadata, "markdown"
            )
            
            # Write translated content with metadata
            with open(translation_path, "w", encoding="utf-8") as f:
                f.write(f"{formatted_metadata}\n\n{translated_content}")

            logger.info(f"Translated {file_path} to {lang_code} at {translation_path}")
            return {"success": True, "path": str(translation_path)}

        except Exception as e:
            logger.error(f"Error translating {file_path} to {lang_code}: {str(e)}")
            return {"success": False, "error": str(e), "path": str(file_path)}

    def _delete_existing_translations(self, lang_code: str):
        """
        Delete existing translations for a language.

        Args:
            lang_code: Language code
        """
        # Implementation would delete translations for the specified language

    def _needs_fixing(self, file_path: Path, lang_code: str, min_confidence: float) -> bool:
        """
        Check if a file needs fixing based on evaluation results.

        Args:
            file_path: Path to the file
            lang_code: Language code
            min_confidence: Minimum confidence threshold

        Returns:
            Whether the file needs fixing
        """
        # Implementation would check evaluation results to determine if a file needs fixing

    def _load_evaluation_results(self):
        """
        Load evaluation results from files.
        """
        # Implementation would load evaluation results from files

    # Additional methods for translating images, notebooks, etc. would be implemented here

    def get_outdated_translations(self, source_files: List[Path]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Identify translations that are outdated compared to their source files.

        Args:
            source_files: List of source file paths

        Returns:
            Dictionary mapping language codes to lists of outdated translation information
        """
        outdated = {lang_code: [] for lang_code in self.language_codes}
        
        # Check each source file
        for source_file in source_files:
            source_content = read_input_file(source_file)
            if not source_content:
                continue
                
            source_hash = calculate_file_hash(source_content)
            
            # Check translation for each language
            for lang_code in self.language_codes:
                # Get translation path using project structure
                trans_path = self.project_structure.get_translation_path(source_file, lang_code)
                
                # If translation exists, check if it's outdated
                if trans_path.exists():
                    try:
                        trans_content = read_input_file(trans_path)
                        if not trans_content:
                            outdated[lang_code].append({
                                "source": source_file,
                                "translation": trans_path,
                                "reason": "empty_translation"
                            })
                            continue
                            
                        # Extract hash from metadata
                        hash_match = re.search(r"hash: ([a-f0-9]{32})", trans_content)
                        if hash_match:
                            trans_hash = hash_match.group(1)
                            if trans_hash != source_hash:
                                outdated[lang_code].append({
                                    "source": source_file,
                                    "translation": trans_path,
                                    "reason": "hash_mismatch"
                                })
                        else:
                            # No hash found, consider outdated
                            outdated[lang_code].append({
                                "source": source_file,
                                "translation": trans_path,
                                "reason": "no_hash"
                            })
                    except Exception as e:
                        logger.warning(f"Error checking {trans_path}: {e}")
                else:
                    # Translation doesn't exist
                    outdated[lang_code].append({
                        "source": source_file,
                        "translation": trans_path,
                        "reason": "missing"
                    })
        
        return outdated
