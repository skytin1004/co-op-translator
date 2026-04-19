"""Maintenance and retry operations for TranslationManager."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Protocol

from tqdm import tqdm

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import filter_files, read_input_file
from co_op_translator.utils.common.metadata_utils import remove_image_metadata
from co_op_translator.utils.llm.markdown_utils import (
    compare_line_breaks,
    update_image_links,
)

logger = logging.getLogger(__name__)


class MaintenanceContext(Protocol):
    """Subset of TranslationManager required for maintenance operations."""

    root_dir: Path
    translations_dir: Path
    image_dir: Path
    language_codes: list[str]
    excluded_dirs: list[str]
    supported_notebook_extensions: list[str]

    def _get_language_root(self, language_code: str) -> Path: ...

    def get_outdated_translations(self) -> list[tuple[Path, Path]]: ...

    async def retranslate_outdated_files(
        self, outdated_files: list[tuple[Path, Path]]
    ) -> None: ...

    async def translate_markdown(self, file_path: Path, language_code: str) -> str: ...

    async def translate_image(
        self, image_path: Path, language_code: str, fast_mode: bool = False
    ) -> str: ...

    def _migrate_legacy_inline_text_metadata(self) -> int: ...


async def check_outdated_files(
    context: MaintenanceContext, update: bool = False
) -> tuple[int, list[str]]:
    """Identify and update outdated translations."""
    errors: list[str] = []

    try:
        if update:
            files: list[tuple[Path, Path]] = []
            for lang_code in context.language_codes:
                translation_dir = context.translations_dir / lang_code
                if not translation_dir.exists():
                    continue

                trans_files: list[Path] = []
                for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
                    trans_files.extend(translation_dir.rglob(f"*{ext}"))
                for ext in context.supported_notebook_extensions:
                    trans_files.extend(translation_dir.rglob(f"*{ext}"))

                for trans_file in trans_files:
                    try:
                        rel = trans_file.relative_to(translation_dir)
                        original = context.root_dir / rel
                        if original.exists():
                            files.append((original, trans_file))
                    except Exception:
                        continue
            outdated_files = files
        else:
            try:
                context._migrate_legacy_inline_text_metadata()
            except Exception as e:
                logger.warning("Legacy text metadata migration skipped: %s", e)
            outdated_files = context.get_outdated_translations()

        modified_count = len(outdated_files)
        if outdated_files:
            await context.retranslate_outdated_files(outdated_files)
        return modified_count, errors
    except Exception as e:
        logger.error("Failed to check outdated files: %s", e)
        errors.append(str(e))
        return 0, errors


async def retranslate_outdated_files(
    context: MaintenanceContext,
    outdated_files: list[tuple[Path, Path]],
) -> None:
    """Translate files identified as outdated or requiring updates."""
    if not outdated_files:
        return

    files_to_translate = []
    for original_file, translation_file in outdated_files:
        try:
            relative_path = translation_file.relative_to(context.translations_dir)
            lang_code = relative_path.parts[0]

            if lang_code not in context.language_codes:
                logger.warning(
                    "Unknown language code in path: %s, skipping %s",
                    lang_code,
                    translation_file,
                )
                continue

            files_to_translate.append((original_file, lang_code))
        except (ValueError, IndexError) as e:
            logger.error(
                "Failed to extract language code from %s: %s", translation_file, e
            )
            continue

    notebook_items = [
        (original_file, language_code)
        for original_file, language_code in files_to_translate
        if original_file.suffix.lower() in context.supported_notebook_extensions
    ]
    markdown_items = [
        (original_file, language_code)
        for original_file, language_code in files_to_translate
        if original_file.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS
    ]

    if notebook_items:
        with tqdm(
            total=len(notebook_items), desc="📓 Retranslating outdated notebooks"
        ) as progress_bar:
            for original_file, language_code in notebook_items:
                await context.translate_notebook(original_file, language_code)  # type: ignore[attr-defined]
                progress_bar.update(1)
                progress_bar.set_postfix_str(f"Current: {original_file.name}")

    if markdown_items:
        with tqdm(
            total=len(markdown_items), desc="📝 Retranslating outdated markdowns"
        ) as progress_bar:
            for original_file, language_code in markdown_items:
                await context.translate_markdown(original_file, language_code)
                progress_bar.update(1)
                progress_bar.set_postfix_str(f"Current: {original_file.name}")


async def retranslate_outdated_images(
    context: MaintenanceContext,
    outdated_images: list[tuple[Path, Path, str]],
    fast_mode: bool = False,
) -> None:
    """Retranslate images identified as outdated."""
    if not outdated_images:
        return

    with tqdm(
        total=len(outdated_images), desc="🖼️  Retranslating outdated images"
    ) as progress_bar:
        for original_file, translated_file, language_code in outdated_images:
            try:
                translated_file.unlink()
                remove_image_metadata(translated_file, context.image_dir)
            except Exception as e:
                logger.warning(
                    "Failed to delete outdated image %s: %s", translated_file, e
                )

            await context.translate_image(
                original_file, language_code, fast_mode=fast_mode
            )
            progress_bar.update(1)
            progress_bar.set_postfix_str(f"Current: {original_file.name}")


async def fix_incorrect_image_paths(context: MaintenanceContext) -> int:
    """Scan all translated markdown files and fix incorrect relative image paths."""
    logger.info("Checking for incorrect image paths in existing translations...")
    fixed_count = 0

    for lang_code in context.language_codes:
        lang_dir = context.translations_dir / lang_code
        if not lang_dir.exists():
            continue

        md_files = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            md_files.extend(list(lang_dir.rglob(f"*{ext}")))

        for md_translated in md_files:
            try:
                content = md_translated.read_text(encoding="utf-8")
                rel_to_lang = md_translated.relative_to(lang_dir)
                original_md_path = (context.root_dir / rel_to_lang).resolve()

                updated = update_image_links(
                    content,
                    original_md_path,
                    lang_code,
                    translations_dir=context.translations_dir,
                    translated_images_dir=context.image_dir,
                    root_dir=context.root_dir,
                    use_translated_images=True,
                )

                if updated != content:
                    md_translated.write_text(updated, encoding="utf-8")
                    fixed_count += 1
                    logger.debug("Fixed image paths in: %s", md_translated)
            except Exception as e:
                logger.error("Failed to fix paths in %s: %s", md_translated, e)

    if fixed_count > 0:
        logger.info("Successfully fixed image paths in %d files.", fixed_count)
    else:
        logger.info("No incorrect image paths found.")

    return fixed_count


async def check_and_retry_translations(context: MaintenanceContext) -> None:
    """Check translated files for formatting errors and retry failed translations."""
    total_files_checked = 0
    files_to_translate = []

    markdown_files = [
        file
        for file in filter_files(context.root_dir, context.excluded_dirs)
        if file.suffix.lower() in SUPPORTED_MARKDOWN_EXTENSIONS
    ]
    all_markdown_files = [
        (file, language_code)
        for file in markdown_files
        for language_code in context.language_codes
    ]

    total_files = len(all_markdown_files)
    if total_files == 0:
        logger.warning("No markdown files found for checking.")
        return

    logger.info("Checking translated files for errors...")

    with tqdm(total=total_files, desc="Checking files", unit="file") as progress_bar:
        for md_file_path, language_code in all_markdown_files:
            md_file_path = Path(md_file_path).resolve()
            total_files_checked += 1

            relative_path = md_file_path.relative_to(context.root_dir)
            translated_md_file_path = (
                context._get_language_root(language_code) / relative_path
            )

            if not translated_md_file_path.exists():
                logger.warning(
                    "Translated file does not exist: %s", translated_md_file_path
                )
                files_to_translate.append((md_file_path, language_code))
                progress_bar.update(1)
                continue

            original_content = read_input_file(md_file_path)
            translated_content = read_input_file(translated_md_file_path)
            if compare_line_breaks(original_content, translated_content):
                files_to_translate.append((md_file_path, language_code))
                logger.warning(
                    "Detected formatting issue in %s", translated_md_file_path
                )

            progress_bar.update(1)

    if files_to_translate:
        logger.info("Starting translation for %d files...", len(files_to_translate))

        with tqdm(
            total=len(files_to_translate), desc="Translating files", unit="file"
        ) as translation_progress_bar:
            for md_file_path, language_code in files_to_translate:
                logger.info("Translating %s to %s...", md_file_path, language_code)
                await context.translate_markdown(
                    file_path=md_file_path,
                    language_code=language_code,
                )
                translation_progress_bar.update(1)

        logger.info("Total files translated: %d", len(files_to_translate))
    else:
        logger.info("No formatting issues found in the translated files.")

    logger.info("Total files checked: %d", total_files_checked)
