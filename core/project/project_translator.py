"""
Project translator manages overall translation process across multiple file types and languages.
"""
import logging
from pathlib import Path
import asyncio

from ..llm.markdown_translator import MarkdownTranslator
from ..llm.text_translator import TextTranslator
from ..llm.jupyter_notebook_translator import JupyterNotebookTranslator
from ..vision.image_translator import ImageTranslator
from ..config.constants import (
    EXCLUDED_DIRS,
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)

from .directory_manager import DirectoryManager
from .translation_manager import TranslationManager
from .config_loader import ConfigLoader
from .structure_factory import ProjectStructureFactory
from .base_structure import ProjectStructure

logger = logging.getLogger(__name__)


class ProjectTranslator:
    """Manages translation of project content across multiple languages.

    Coordinates translation of markdown documents and images, directory management,
    and tracking of translation status across the project.
    """

    def __init__(self, language_codes, root_dir=".", markdown_only=False, config_path=None):
        """Initialize project translation environment.

        Sets up translators and managers needed for project translation operations.

        Args:
            language_codes: Space-separated list of target language codes or list of codes
            root_dir: Root directory of the project to translate
            markdown_only: Whether to process only markdown files and skip images
            config_path: Path to translation configuration file
        """
        # Process language codes
        self.language_codes = language_codes.split() if isinstance(language_codes, str) else language_codes
        self.root_dir = Path(root_dir).resolve()
        self.markdown_only = markdown_only
        
        # Load configuration
        self.config = ConfigLoader.load_config(config_path)
        
        # Set up paths based on configuration
        translations_path = self.config.get("paths", {}).get("translations", "translations")
        image_path = self.config.get("paths", {}).get("images", "translated_images")
        self.translations_dir = self.root_dir / translations_path
        self.image_dir = self.root_dir / image_path
        
        # Set up project structure
        self.project_structure = ProjectStructureFactory.create_structure(
            self.config, self.root_dir, self.translations_dir, self.language_codes
        )

        # Initialize text translator
        self.text_translator = TextTranslator.create()

        # Initialize image translator if not in markdown-only mode
        if not markdown_only:
            self.image_translator = ImageTranslator.create()
        else:
            self.image_translator = None

        # Initialize notebook translator
        self.notebook_translator = JupyterNotebookTranslator.create(self.text_translator)

        # Initialize markdown translator
        self.markdown_translator = MarkdownTranslator.create(self.text_translator)

        # Get excluded directories from config
        self.excluded_dirs = self.config.get("excluded_dirs", EXCLUDED_DIRS)
        
        # Get supported extensions from config
        self.supported_image_extensions = self.config.get("extensions", {}).get("images", SUPPORTED_IMAGE_EXTENSIONS)
        self.supported_notebook_extensions = self.config.get("extensions", {}).get("notebooks", SUPPORTED_NOTEBOOK_EXTENSIONS)

        # Initialize directory manager
        self.directory_manager = DirectoryManager(
            self.project_structure,
            self.excluded_dirs,
        )
        
        # Initialize translation manager
        self.translation_manager = TranslationManager(
            self.project_structure,
            self.image_dir,
            self.excluded_dirs,
            self.supported_image_extensions,
            self.supported_notebook_extensions,
            self.markdown_translator,
            self.image_translator,
            self.notebook_translator,
            self.markdown_only,
        )

    async def translate(
        self,
        update=False,
        images_only=False,
        markdown_only=False,
        notebook_only=False,
        fix_mode=False,
        min_confidence=0.7,
        fast_mode=False,
    ):
        """
        Translate project files to target languages.

        Args:
            update: Whether to delete existing translations
            images_only: Whether to translate only images
            markdown_only: Whether to translate only markdown files
            notebook_only: Whether to translate only notebook files
            fix_mode: Whether to run in fix mode
            min_confidence: Minimum confidence threshold for fixing translations
            fast_mode: Whether to run in fast mode for image translation

        Returns:
            Dictionary containing translation results
        """
        results = {}

        # Sync directory structure to prepare for translation
        if not images_only:
            self.directory_manager.sync_directory_structure(
                markdown=(markdown_only or not images_only),
                images=(not markdown_only),
            )

        # Markdown translation
        if not images_only and not notebook_only:
            md_files = self.directory_manager.list_source_files([".md", ".markdown"])
            outdated = self.translation_manager.get_outdated_translations(md_files)
            
            # Create dictionary mapping language codes to files
            files_to_translate = {}
            for lang_code, outdated_files in outdated.items():
                if isinstance(outdated_files, list) and len(outdated_files) > 0:
                    # Handle both old and new format of get_outdated_translations
                    if isinstance(outdated_files[0], dict):
                        files_to_translate[lang_code] = [item["source"] for item in outdated_files]
                    else:
                        files_to_translate[lang_code] = outdated_files
            
            # Translate markdown files
            if any(files for files in files_to_translate.values()):
                markdown_results = await self.translation_manager.translate_markdown_files(
                    files_to_translate,
                    delete_existing=update,
                    fix_mode=fix_mode,
                    min_confidence=min_confidence,
                )
                results["markdown"] = markdown_results
            else:
                results["markdown"] = {"files_translated": 0, "message": "No files to translate"}

        # Image translation (similar logic would be implemented)
        if not markdown_only and not notebook_only and not self.markdown_only and self.image_translator:
            # Image translation logic would be implemented here
            results["images"] = {"files_translated": 0, "message": "Image translation not implemented yet"}

        # Notebook translation (similar logic would be implemented)
        if not markdown_only and not images_only and self.notebook_translator:
            # Notebook translation logic would be implemented here
            results["notebooks"] = {"files_translated": 0, "message": "Notebook translation not implemented yet"}

        # Cleanup orphaned translations if updating
        if update:
            removed = self.directory_manager.cleanup_orphaned_translations(
                markdown=(not images_only),
                images=(not markdown_only and not self.markdown_only),
            )
            results["cleanup"] = {"files_removed": removed}

        return results

    # Other methods for project evaluation, etc. would be implemented here
