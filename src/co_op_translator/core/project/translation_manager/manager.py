from pathlib import Path
import logging
from typing import List

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.project.directory_manager import DirectoryManager
from co_op_translator.core.project.layout import OutputLayout
from co_op_translator.core.project.translation_manager.content_translation import (
    translate_all_image_files as translate_all_image_files_for_context,
    translate_all_markdown_files as translate_all_markdown_files_for_context,
    translate_all_notebook_files as translate_all_notebook_files_for_context,
    translate_image as translate_image_for_context,
    translate_markdown as translate_markdown_for_context,
    translate_notebook as translate_notebook_for_context,
)
from co_op_translator.core.project.translation_manager.maintenance import (
    check_and_retry_translations as check_and_retry_translations_for_context,
    check_outdated_files as check_outdated_files_for_context,
    fix_incorrect_image_paths as fix_incorrect_image_paths_for_context,
    retranslate_outdated_files as retranslate_outdated_files_for_context,
    retranslate_outdated_images as retranslate_outdated_images_for_context,
)
from co_op_translator.core.project.translation_manager.planning import (
    estimate_tokens as estimate_planned_tokens,
    gather_pending_markdown,
    gather_pending_notebooks,
)
from co_op_translator.core.project.translation_manager.processing import (
    process_api_requests_parallel as process_api_requests_parallel_tasks,
    process_api_requests_sequential as process_api_requests_sequential_tasks,
)
from co_op_translator.core.project.translation_manager.stale_detection import (
    get_outdated_images as find_outdated_images,
    get_outdated_translations as find_outdated_translations,
    is_translation_outdated,
    migrate_legacy_inline_text_metadata,
    resolve_language_root,
)
from co_op_translator.core.project.translation_manager.workflow import (
    run_translation_workflow,
)

logger = logging.getLogger(__name__)


class TranslationManager:
    """Manages translation of markdown and image files for a project.

    Coordinates file discovery, translation tasks, and maintains translation metadata
    to efficiently track and update translations.
    """

    def __init__(
        self,
        root_dir: Path,
        translations_dir: Path,
        image_dir: Path,
        language_codes: list[str],
        excluded_dirs: list[str],
        supported_image_extensions: list[str],
        supported_notebook_extensions: list[str],
        markdown_translator: MarkdownTranslator,
        image_translator=None,
        notebook_translator=None,
        translation_types: list[str] = None,
        add_disclaimer: bool = True,
        lang_subdir: Path | None = None,
    ):
        """Initialize translation manager with required components and settings.

        Sets up paths, translators, and configurations needed for managing translations.

        Args:
            root_dir: Root directory containing original files
            translations_dir: Directory for translated files
            image_dir: Directory for translated images
            language_codes: List of target language codes
            excluded_dirs: List of directories to exclude
            supported_image_extensions: List of supported image extensions
            supported_notebook_extensions: List of supported notebook extensions
            markdown_translator: Translator instance for markdown files
            image_translator: Translator instance for image files
            notebook_translator: Translator instance for notebook files
            translation_types: List of file types to translate (e.g., ["markdown", "images", "notebook"])
        """
        self.output_layout = OutputLayout.from_paths(
            root_dir=root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )
        self.root_dir = self.output_layout.root_dir
        self.translations_dir = self.output_layout.translations_dir
        self.image_dir = self.output_layout.image_dir
        self.language_codes = language_codes
        self.excluded_dirs = excluded_dirs
        self.supported_image_extensions = supported_image_extensions
        self.supported_notebook_extensions = supported_notebook_extensions
        self.markdown_translator = markdown_translator
        self.image_translator = image_translator
        self.notebook_translator = notebook_translator

        # Default translation types if not specified
        if translation_types is None:
            translation_types = ["markdown", "notebook", "images"]
        self.translation_types = translation_types
        self.add_disclaimer = add_disclaimer
        self.lang_subdir = self.output_layout.lang_subdir
        self.directory_manager = DirectoryManager(
            self.root_dir,
            self.translations_dir,
            language_codes,
            excluded_dirs,
            image_dir=self.image_dir,
        )

    def _get_language_root(self, language_code: str) -> Path:
        """Return the root directory for a specific language.

        Default layout is translations_dir / language_code. When lang_subdir is
        set, we append it, yielding translations_dir / language_code / lang_subdir.
        """
        return self.output_layout.language_root(language_code)

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str:
        return await translate_image_for_context(
            self, image_path, language_code, fast_mode=fast_mode
        )

    async def translate_markdown(self, file_path: Path, language_code: str) -> str:
        return await translate_markdown_for_context(self, file_path, language_code)

    async def translate_notebook(self, file_path: Path, language_code: str) -> str:
        return await translate_notebook_for_context(self, file_path, language_code)

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        return await translate_all_markdown_files_for_context(self, update=update)

    async def translate_all_notebook_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]:
        return await translate_all_notebook_files_for_context(self, update=update)

    async def translate_all_image_files(
        self, update: bool = False, fast_mode: bool = False
    ) -> tuple[int, list[str]]:
        return await translate_all_image_files_for_context(
            self, update=update, fast_mode=fast_mode
        )

    async def check_outdated_files(self, update: bool = False) -> tuple[int, List[str]]:
        return await check_outdated_files_for_context(self, update=update)

    async def translate_project_async(
        self,
        update: bool = False,
        fast_mode: bool = False,
    ) -> tuple[int, list[str]]:
        """Translate project files asynchronously following a structured workflow.

        The translation process follows these steps:
        1. Remove orphaned files
        2. Synchronize directory structure with source
        3. Identify outdated translations
        4. Perform translation on required files

        Translation types are determined by the translation_types list set during initialization.

        Args:
            update: Whether to update existing translations
            fast_mode: Whether to use faster translation method

        Returns:
            Tuple containing (total_modified_files, error_messages_list)
        """
        return await run_translation_workflow(
            self,
            update=update,
            fast_mode=fast_mode,
        )

    def estimate_tokens(self, update: bool = False) -> dict:
        """Estimate tokens for the upcoming translation run.

        Backward-compatible shim that delegates token-estimation breakdown
        calculation to shared estimation utilities.
        """
        return estimate_planned_tokens(self, update=update)

    def _gather_pending_markdown(self, update: bool) -> List[Path]:
        return gather_pending_markdown(self, update=update)

    def _gather_pending_notebooks(self, update: bool) -> List[Path]:
        return gather_pending_notebooks(self, update=update)

    def get_outdated_translations(self) -> List[tuple[Path, Path]]:
        """Identify translations that need updates based on file hash comparison.

        Scans all translation files and compares their metadata with source files.

        Returns:
            List of (original_file, translation_file) tuples that need updates
        """
        return find_outdated_translations(self)

    def _resolve_language_root(self, language_code: str) -> Path:
        """Return a concrete language root even for partially mocked managers in tests."""
        return resolve_language_root(self, language_code)

    async def retranslate_outdated_files(
        self, outdated_files: List[tuple[Path, Path]]
    ) -> None:
        return await retranslate_outdated_files_for_context(self, outdated_files)

    def get_outdated_images(self) -> List[tuple[Path, Path, str]]:
        """Identify translated images that need updates based on metadata hash comparison.

        Scans all translated image files and compares their metadata with source images.

        Returns:
            List of (original_file, translated_file, language_code) tuples that need updates
        """
        return find_outdated_images(self)

    async def retranslate_outdated_images(
        self, outdated_images: List[tuple[Path, Path, str]], fast_mode: bool = False
    ) -> None:
        return await retranslate_outdated_images_for_context(
            self, outdated_images, fast_mode=fast_mode
        )

    async def fix_incorrect_image_paths(self):
        return await fix_incorrect_image_paths_for_context(self)

    async def check_and_retry_translations(self):
        return await check_and_retry_translations_for_context(self)

    async def process_api_requests_parallel(self, tasks, task_desc) -> list:
        """Execute multiple API requests concurrently with controlled parallelism.

        Uses a queue system to manage API requests efficiently while providing
        progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        return await process_api_requests_parallel_tasks(tasks, task_desc)

    async def process_api_requests_sequential(
        self, tasks, task_desc, file_names=None
    ) -> list:
        """Execute API requests one at a time in sequence.

        Ensures requests are processed in order while providing progress feedback.

        Args:
            tasks: List of task functions to execute
            task_desc: Description for progress display

        Returns:
            List of results from completed tasks
        """
        return await process_api_requests_sequential_tasks(
            tasks, task_desc, file_names=file_names
        )

    def _is_translation_outdated(
        self, original_file: Path, translation_file: Path
    ) -> bool:
        """Determine if a translation file needs updating based on content hash.

        Compares the hash of the original file with the hash stored in the translation
        file's metadata. Handles both markdown and notebook files.

        Args:
            original_file: Path to the original file
            translation_file: Path to the translation file

        Returns:
            True if translation needs updating, False if it's current
        """
        return is_translation_outdated(self, original_file, translation_file)

    def _migrate_legacy_inline_text_metadata(self) -> int:
        return migrate_legacy_inline_text_metadata(self)
