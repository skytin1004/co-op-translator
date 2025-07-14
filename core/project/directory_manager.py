"""
Manages directory structure and file cleanup for translation project.
"""
from pathlib import Path
import logging
import json
from typing import List, Set, Tuple, Dict, Any, Optional

from ..utils.common.file_utils import get_unique_id
from .base_structure import ProjectStructure

logger = logging.getLogger(__name__)


class DirectoryManager:
    """
    Manages directory structure and file cleanup for translation project.
    """

    def __init__(
        self,
        project_structure: ProjectStructure,
        excluded_dirs: List[str],
    ):
        """Initialize directory manager with project configuration.

        Args:
            project_structure: Project structure handler
            excluded_dirs: List of directories to exclude
        """
        self.project_structure = project_structure
        self.root_dir = project_structure.root_dir
        self.translations_dir = project_structure.translations_dir
        self.language_codes = project_structure.language_codes
        self.excluded_dirs = excluded_dirs

    def sync_directory_structure(
        self, markdown: bool = True, images: bool = True
    ) -> Tuple[int, int, int]:
        """
        Synchronize the directory structure of translations with the original structure.

        Process:
        1. Scan original directory structure
        2. For each language:
           - Create missing directories that exist in original
           - Remove directories that don't exist in original

        Args:
            markdown: Whether to sync markdown directories
            images: Whether to sync image directories

        Returns:
            Tuple containing counts of created directories, removed directories,
            and number of languages synchronized
        """
        created_count = 0
        removed_count = 0

        # Get original directory structure (excluding files)
        original_dirs = set()
        for path in self.root_dir.rglob("*"):
            if path.is_dir() and not any(
                excluded in str(path) for excluded in self.excluded_dirs
            ):
                # For image-only mode, only include image directories
                if (
                    not markdown
                    and not any(path.glob("*.png"))
                    and not any(path.glob("*.jpg"))
                ):
                    continue
                # For markdown-only mode, only include markdown directories
                if not images and not any(path.glob("*.md")):
                    continue
                # Store relative path for comparison
                original_dirs.add(path.relative_to(self.root_dir))

        # Sync each language directory
        for lang_code in self.language_codes:
            lang_dir = self.translations_dir / lang_code
            if not lang_dir.exists():
                lang_dir.mkdir(parents=True, exist_ok=True)
                logger.info(f"Created language directory: {lang_dir}")

            # Get existing translation directories
            translation_dirs = set()
            if lang_dir.exists():
                for path in lang_dir.rglob("*"):
                    if path.is_dir():
                        try:
                            translation_dirs.add(path.relative_to(lang_dir))
                        except ValueError:
                            continue

            # Create missing directories
            for orig_dir in original_dirs:
                # Use project structure to map to translation path
                orig_dir_full = self.root_dir / orig_dir
                target_dir = self.project_structure.get_translation_path(orig_dir_full, lang_code).parent
                if not target_dir.exists():
                    target_dir.mkdir(parents=True, exist_ok=True)
                    created_count += 1
                    logger.info(f"Created directory: {target_dir}")

            # Remove extra directories that don't exist in original
            for trans_dir in sorted(
                translation_dirs, reverse=True
            ):  # Sort reverse to handle deep paths first
                if trans_dir not in original_dirs:
                    target_dir = lang_dir / trans_dir
                    try:
                        # Only remove if empty or contains no relevant files
                        has_relevant_files = False
                        if markdown and any(target_dir.rglob("*.md")):
                            has_relevant_files = True
                        if images and (
                            any(target_dir.rglob("*.png"))
                            or any(target_dir.rglob("*.jpg"))
                        ):
                            has_relevant_files = True

                        if not has_relevant_files:
                            target_dir.rmdir()  # This will only remove empty directories
                            removed_count += 1
                            logger.info(f"Removed empty directory: {target_dir}")
                        else:
                            logger.info(f"Skipping non-empty directory: {target_dir}")
                    except OSError as e:
                        logger.warning(f"Could not remove directory {target_dir}: {e}")

        return created_count, removed_count, len(self.language_codes)

    def cleanup_orphaned_translations(
        self, markdown: bool = True, images: bool = True
    ) -> int:
        """Remove orphaned translation files that no longer have source files.

        Identifies and removes translation files where the original source file
        has been deleted or moved. Processes files by matching metadata to determine
        the correct language code and source file relationship.

        Args:
            markdown: Whether to clean up markdown files
            images: Whether to clean up image files

        Returns:
            Number of removed translation files
        """
        removed_count = 0
        logger.info(f"Starting cleanup with markdown={markdown}, images={images}")

        # Handle markdown files
        if markdown:
            # Get all markdown translation files
            markdown_files = []
            for lang_code in self.language_codes:
                lang_dir = self.translations_dir / lang_code
                if lang_dir.exists():
                    for md_file in lang_dir.rglob("*.md"):
                        # Store tuple of (file_path, language_code) to ensure we keep track of 
                        # which language directory this file belongs to
                        markdown_files.append((md_file, lang_code))

            # Check each translation file to see if its source still exists
            for md_file, lang_code in markdown_files:
                # Use project structure to get the original path
                original_path = self.project_structure.get_original_path(md_file)
                
                # Skip if the original path doesn't exist
                if not original_path.exists():
                    try:
                        md_file.unlink()
                        removed_count += 1
                        logger.info(f"Removed orphaned translation: {md_file}")
                    except OSError as e:
                        logger.warning(f"Could not remove file {md_file}: {e}")

        # Similar logic for images
        if images:
            # Logic for images would be similar, using the project structure

        return removed_count

    def list_source_files(self, extensions: List[str]) -> List[Path]:
        """
        List all source files with given extensions in the project directory.

        Args:
            extensions: List of file extensions to include (e.g., ['.md', '.markdown'])

        Returns:
            List of paths to source files
        """
        source_files = []
        for ext in extensions:
            for path in self.root_dir.rglob(f"*{ext}"):
                if path.is_file() and not any(
                    excluded in str(path) for excluded in self.excluded_dirs
                ):
                    source_files.append(path)
        return source_files

    def get_translation_file_path(self, source_file: Path, lang_code: str) -> Path:
        """
        Get the path where a translation should be stored.

        Args:
            source_file: Path to the source file
            lang_code: Target language code

        Returns:
            Path where the translation should be stored
        """
        return self.project_structure.get_translation_path(source_file, lang_code)

    def get_outdated_translations(
        self, source_files: List[Path], extensions: List[str] = None
    ) -> Dict[str, List[Path]]:
        """
        Identify translations that are outdated compared to their source files.

        Args:
            source_files: List of source file paths
            extensions: List of file extensions to check

        Returns:
            Dictionary mapping language codes to lists of outdated translation paths
        """
        outdated = {lang_code: [] for lang_code in self.language_codes}
        extensions = extensions or [".md"]

        # Check each source file
        for source_file in source_files:
            source_mtime = source_file.stat().st_mtime
            
            # Check translation for each language
            for lang_code in self.language_codes:
                # Get translation path using project structure
                trans_path = self.project_structure.get_translation_path(source_file, lang_code)
                
                # If translation doesn't exist or is older than source, it's outdated
                if not trans_path.exists() or trans_path.stat().st_mtime < source_mtime:
                    outdated[lang_code].append(source_file)

        return outdated
