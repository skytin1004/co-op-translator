"""Content translation operations for TranslationManager."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Protocol

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    delete_translated_images_by_language_code,
    delete_translated_markdown_files_by_language_code,
    filter_files,
    generate_translated_filename,
    get_filename_and_extension,
    handle_empty_document,
    read_input_file,
)
from co_op_translator.utils.common.metadata_utils import (
    is_image_up_to_date,
    is_notebook_up_to_date,
    save_text_metadata_for_source,
)
from co_op_translator.utils.llm.markdown_utils import compare_line_breaks

logger = logging.getLogger(__name__)


class ContentTranslationContext(Protocol):
    """Subset of TranslationManager required for content translation."""

    root_dir: Path
    translations_dir: Path
    image_dir: Path
    language_codes: list[str]
    excluded_dirs: list[str]
    supported_image_extensions: list[str]
    supported_notebook_extensions: list[str]
    translation_types: list[str]
    add_disclaimer: bool
    lang_subdir: Path | None
    markdown_translator: object
    image_translator: object
    notebook_translator: object

    def _get_language_root(self, language_code: str) -> Path: ...

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str: ...

    async def translate_markdown(self, file_path: Path, language_code: str) -> str: ...

    async def translate_notebook(self, file_path: Path, language_code: str) -> str: ...

    async def process_api_requests_parallel(self, tasks, task_desc) -> list: ...

    async def process_api_requests_sequential(
        self, tasks, task_desc, file_names=None
    ) -> list: ...


async def translate_image(
    context: ContentTranslationContext,
    image_path: Path,
    language_code: str,
    fast_mode: bool = False,
) -> str:
    """Translate an image to the target language."""
    image_path = Path(image_path).resolve()
    if not context.image_translator:
        logger.info(
            "Image translation skipped for %s due to missing Azure AI Service configuration",
            image_path,
        )
        return str(image_path)

    if image_path.exists() and image_path.is_file():
        logger.info("Image exists: %s", image_path)
        if os.access(image_path, os.R_OK):
            logger.info("Read permission granted for: %s", image_path)
        else:
            logger.warning("Read permission denied for: %s", image_path)
            return str(image_path)
    else:
        logger.error("Image does not exist or is not a valid file: %s", image_path)
        return str(image_path)

    try:
        translated_image_path = context.image_translator.translate_image(
            image_path, language_code, context.image_dir, fast_mode=fast_mode
        )
        logger.info(
            "Translated %s to %s and saved to %s",
            image_path,
            language_code,
            translated_image_path,
        )
        return str(translated_image_path)
    except Exception as e:
        logger.error("Failed to translate image %s: %s", image_path, e, exc_info=True)
        return str(image_path)


async def translate_markdown(
    context: ContentTranslationContext,
    file_path: Path,
    language_code: str,
) -> str:
    """Translate a markdown file to the specified language."""
    file_path = Path(file_path).resolve()
    try:
        document = read_input_file(file_path)
        if not document:
            relative_path = file_path.relative_to(context.root_dir)
            output_file = context._get_language_root(language_code) / relative_path
            handle_empty_document(file_path, output_file)
            return str(output_file)

        translated_content = await context.markdown_translator.translate_markdown(
            document,
            language_code,
            file_path,
            translation_types=context.translation_types,
            add_metadata=False,
            add_disclaimer=context.add_disclaimer,
        )
        if not translated_content:
            logger.error(
                "Translation failed for %s: Empty translation result", file_path
            )
            raise RuntimeError(
                f"Markdown translation returned empty content for {file_path}"
            )

        if compare_line_breaks(document, translated_content):
            logger.warning("Translation failed for %s. Retrying...", file_path)
            translated_content = await context.markdown_translator.translate_markdown(
                document,
                language_code,
                file_path,
                translation_types=context.translation_types,
                add_metadata=False,
                add_disclaimer=context.add_disclaimer,
            )
            if not translated_content:
                logger.error(
                    "Retry translation failed for %s: Empty translation result",
                    file_path,
                )
                raise RuntimeError(
                    f"Markdown translation retry returned empty content for {file_path}"
                )

        relative_path = file_path.relative_to(context.root_dir)
        translated_path = context._get_language_root(language_code) / relative_path
        translated_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(translated_path, "w", encoding="utf-8") as f:
                f.write(translated_content)
            logger.info(
                "Translated %s to %s and saved to %s",
                file_path,
                language_code,
                translated_path,
            )
            save_text_metadata_for_source(
                context._get_language_root(language_code),
                file_path,
                language_code,
                root_dir=context.root_dir,
            )
            return str(translated_path)
        except Exception as e:
            logger.error("Failed to write translation to %s: %s", translated_path, e)
            raise

    except Exception as e:
        logger.error("Failed to translate %s: %s", file_path, e)
        raise


async def translate_notebook(
    context: ContentTranslationContext,
    file_path: Path,
    language_code: str,
) -> str:
    """Translate a Jupyter notebook file to the specified language."""
    file_path = Path(file_path).resolve()
    try:
        document = read_input_file(file_path)
        if not document:
            relative_path = file_path.relative_to(context.root_dir)
            output_file = context._get_language_root(language_code) / relative_path
            handle_empty_document(file_path, output_file)
            return str(output_file)

        use_translated_images = "images" in context.translation_types
        translated_content = await context.notebook_translator.translate_notebook(
            file_path,
            language_code,
            use_translated_images=use_translated_images,
            add_disclaimer=context.add_disclaimer,
        )
        if not translated_content:
            logger.error(
                "Translation failed for %s: Empty translation result", file_path
            )
            return ""

        relative_path = file_path.relative_to(context.root_dir)
        translated_path = context._get_language_root(language_code) / relative_path
        translated_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(translated_path, "w", encoding="utf-8") as f:
                f.write(translated_content)
            logger.info(
                "Translated %s to %s and saved to %s",
                file_path,
                language_code,
                translated_path,
            )
            save_text_metadata_for_source(
                context._get_language_root(language_code),
                file_path,
                language_code,
                root_dir=context.root_dir,
            )
            return str(translated_path)
        except Exception as e:
            logger.error("Failed to write translation to %s: %s", translated_path, e)
            return ""

    except Exception as e:
        logger.error("Failed to translate %s: %s", file_path, e)
        return ""


async def translate_all_markdown_files(
    context: ContentTranslationContext,
    update: bool = False,
) -> tuple[int, list[str]]:
    """Process and translate all markdown files in the project directory."""
    modified_count = 0
    errors = []

    if update:
        for language_code in context.language_codes:
            delete_translated_markdown_files_by_language_code(
                language_code, context.translations_dir, context.lang_subdir
            )
            logger.info(
                "Deleted all translated markdown files for language: %s",
                language_code,
            )

    markdown_files = filter_files(context.root_dir, context.excluded_dirs)
    tasks = []
    task_info = []

    for md_file_path in markdown_files:
        md_file_path = md_file_path.resolve()
        if md_file_path.suffix.lower() not in SUPPORTED_MARKDOWN_EXTENSIONS:
            continue

        for language_code in context.language_codes:
            relative_path = md_file_path.relative_to(context.root_dir)
            translated_md_path = (
                context._get_language_root(language_code) / relative_path
            )

            if not update and translated_md_path.exists():
                logger.info(
                    "Skipping already translated markdown file: %s", translated_md_path
                )
                continue

            logger.info(
                "Translating markdown file: %s for language: %s",
                md_file_path,
                language_code,
            )
            tasks.append(
                lambda md_file_path=md_file_path, language_code=language_code: context.translate_markdown(
                    md_file_path, language_code
                )
            )
            task_info.append((str(md_file_path), language_code))

    if tasks:
        results = await context.process_api_requests_sequential(
            tasks, "🛠️  Translating markdown files"
        )
        modified_count = sum(1 for result in results if result)
        errors = [
            f"Failed to translate markdown file: {file_path} (lang: {lang_code})"
            for (file_path, lang_code), result in zip(task_info, results)
            if not result
        ]
    else:
        logger.warning("No markdown files found for translation.")

    return modified_count, errors


async def translate_all_notebook_files(
    context: ContentTranslationContext,
    update: bool = False,
) -> tuple[int, list[str]]:
    """Process and translate all Jupyter notebook files in the project directory."""
    modified_count = 0
    errors = []

    if not context.notebook_translator:
        logger.info("Notebook translator not available, skipping notebook files")
        return modified_count, errors

    if update:
        for language_code in context.language_codes:
            translation_dir = context._get_language_root(language_code)
            if translation_dir.exists():
                for ext in context.supported_notebook_extensions:
                    for notebook_file in translation_dir.rglob(f"*{ext}"):
                        notebook_file.unlink()
                        logger.info("Deleted translated notebook: %s", notebook_file)

    notebook_files = []
    for ext in context.supported_notebook_extensions:
        notebook_files.extend(
            filter_files(context.root_dir, context.excluded_dirs, ext)
        )

    tasks = []
    task_info = []

    for notebook_file_path in notebook_files:
        notebook_file_path = notebook_file_path.resolve()

        for language_code in context.language_codes:
            relative_path = notebook_file_path.relative_to(context.root_dir)
            translated_notebook_path = (
                context._get_language_root(language_code) / relative_path
            )

            if translated_notebook_path.exists() and not update:
                if is_notebook_up_to_date(notebook_file_path, translated_notebook_path):
                    logger.info(
                        "Skipping up-to-date notebook: %s", translated_notebook_path
                    )
                    continue
                logger.info(
                    "Notebook is outdated, will retranslate: %s -> %s",
                    notebook_file_path,
                    translated_notebook_path,
                )

            logger.info(
                "Translating notebook file: %s for language: %s",
                notebook_file_path,
                language_code,
            )
            tasks.append(
                lambda notebook_file_path=notebook_file_path, language_code=language_code: context.translate_notebook(
                    notebook_file_path, language_code
                )
            )
            task_info.append((str(notebook_file_path), language_code))

    if tasks:
        results = await context.process_api_requests_sequential(
            tasks, "📓 Translating notebook files"
        )
        modified_count = sum(1 for result in results if result)
        errors = [
            f"Failed to translate notebook file: {file_path} (lang: {lang_code})"
            for (file_path, lang_code), result in zip(task_info, results)
            if not result
        ]
    else:
        logger.warning("No notebook files found for translation.")

    return modified_count, errors


async def translate_all_image_files(
    context: ContentTranslationContext,
    update: bool = False,
    fast_mode: bool = False,
) -> tuple[int, list[str]]:
    """Process and translate all image files in the project directory."""
    modified_count = 0
    errors = []

    logger.info("Starting image translation tasks...")

    if update:
        for language_code in context.language_codes:
            delete_translated_images_by_language_code(language_code, context.image_dir)
            logger.info("Deleted all translated images for language: %s", language_code)

    image_files = filter_files(context.root_dir, context.excluded_dirs)
    tasks = []
    task_info = []

    for image_file_path in image_files:
        image_file_path = image_file_path.resolve()
        if (
            get_filename_and_extension(image_file_path)[1]
            not in context.supported_image_extensions
        ):
            continue

        for language_code in context.language_codes:
            translated_filename = generate_translated_filename(
                image_file_path, language_code, context.root_dir
            )
            translated_image_path = (
                Path(context.image_dir) / language_code / translated_filename
            )

            if translated_image_path.exists() and not update:
                if is_image_up_to_date(
                    image_file_path, translated_image_path, context.image_dir
                ):
                    logger.info("Skipping up-to-date image: %s", translated_image_path)
                    continue
                logger.info(
                    "Image metadata mismatch detected: %s -> %s",
                    image_file_path,
                    translated_image_path,
                )

            logger.info(
                "Translating image: %s for language: %s",
                image_file_path,
                language_code,
            )
            tasks.append(
                context.translate_image(
                    image_file_path, language_code, fast_mode=fast_mode
                )
            )
            task_info.append((str(image_file_path), language_code))

    if tasks:
        results = await context.process_api_requests_parallel(
            tasks, f"{'🏎️  (fast mode)' if fast_mode else '🖼️ '} Translating images"
        )
        modified_count = sum(
            1
            for (file_path, _), result in zip(task_info, results)
            if result and result != file_path
        )
        errors = [
            f"Failed to translate image file: {file_path} (lang: {lang_code})"
            for (file_path, lang_code), result in zip(task_info, results)
            if result == file_path
        ]
    else:
        logger.warning("No image files found for translation.")

    return modified_count, errors
