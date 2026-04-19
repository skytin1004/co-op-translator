"""Top-level translation workflow orchestration."""

from __future__ import annotations

import logging
from typing import Protocol

from tqdm import tqdm

from co_op_translator.config.base_config import Config
from co_op_translator.core.project.directory_manager import DirectoryManager
from co_op_translator.utils.common.metadata_utils import cleanup_orphan_image_metadata
from co_op_translator.utils.common.token_estimation import (
    estimate_tokens_for_outdated,
    estimate_tokens_for_sources,
)

from .migration import run_image_and_link_migrations

logger = logging.getLogger(__name__)


class TranslationWorkflowContext(Protocol):
    """Subset of TranslationManager used by the workflow use case."""

    translation_types: list[str]
    language_codes: list[str]
    root_dir: object
    translations_dir: object
    image_dir: object
    excluded_dirs: list[str]
    directory_manager: object

    def _migrate_legacy_inline_text_metadata(self) -> int: ...

    def get_outdated_translations(self) -> list: ...

    async def retranslate_outdated_files(self, outdated_files: list) -> None: ...

    def get_outdated_images(self) -> list: ...

    async def retranslate_outdated_images(
        self, outdated_images: list, fast_mode: bool = False
    ) -> None: ...

    def _gather_pending_markdown(self, update: bool) -> list: ...

    def _gather_pending_notebooks(self, update: bool) -> list: ...

    async def translate_all_markdown_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]: ...

    async def translate_all_notebook_files(
        self, update: bool = False
    ) -> tuple[int, list[str]]: ...

    async def translate_all_image_files(
        self, update: bool = False, fast_mode: bool = False
    ) -> tuple[int, list[str]]: ...

    async def fix_incorrect_image_paths(self) -> None: ...


async def run_translation_workflow(
    context: TranslationWorkflowContext,
    *,
    update: bool = False,
    fast_mode: bool = False,
) -> tuple[int, list[str]]:
    """Run the end-to-end project translation workflow."""
    logger.info("Starting project translation...")
    total_modified = 0
    all_errors: list[str] = []

    try:
        run_image_and_link_migrations(context)

        logger.info("Removing orphaned files...")
        with tqdm(total=1, desc="🧹 Cleaning orphaned files") as cleanup_progress:
            removed_md_nb = context.directory_manager.cleanup_orphaned_translations(
                markdown="markdown" in context.translation_types,
                images=False,
                notebooks="notebook" in context.translation_types,
            )

            removed_imgs = 0
            if "images" in context.translation_types:
                cleanup_langs = Config.get_language_codes()
                img_dm = DirectoryManager(
                    context.root_dir,
                    context.translations_dir,
                    cleanup_langs,
                    context.excluded_dirs,
                    image_dir=context.image_dir,
                )
                removed_imgs = img_dm.cleanup_orphaned_translations(
                    markdown=False,
                    images=True,
                    notebooks=False,
                )

            removed_total = (removed_md_nb or 0) + (removed_imgs or 0)
            cleanup_progress.set_postfix_str(
                "None" if removed_total == 0 else f"Removed: {removed_total}"
            )
            cleanup_progress.update(1)

        logger.info("Synchronizing directory structure...")
        with tqdm(total=1, desc="📁 Synchronizing directories") as sync_progress:
            created, removed, _ = context.directory_manager.sync_directory_structure(
                markdown="markdown" in context.translation_types,
                images="images" in context.translation_types,
                notebooks="notebook" in context.translation_types,
            )
            sync_progress.set_postfix_str(
                "None"
                if (created == 0 and removed == 0)
                else f"Created: {created}, Removed: {removed}"
            )
            sync_progress.update(1)

        if (
            "markdown" in context.translation_types
            or "notebook" in context.translation_types
        ):
            try:
                context._migrate_legacy_inline_text_metadata()
            except Exception as e:
                logger.warning(f"Legacy text metadata migration skipped: {e}")

            with tqdm(total=1, desc="🔍 Checking translations") as check_progress:
                outdated_files = context.get_outdated_translations()
                check_progress.set_postfix_str(
                    "None" if not outdated_files else f"Found: {len(outdated_files)}"
                )
                check_progress.update(1)

            if outdated_files:
                try:
                    est_tokens = estimate_tokens_for_outdated(
                        context,
                        outdated_files,
                        content_type="markdown",
                    ) + estimate_tokens_for_outdated(
                        context,
                        outdated_files,
                        content_type="notebook",
                    )
                    logger.info(
                        f"Estimated tokens for selected retranslation targets: {est_tokens:,}"
                    )
                except Exception as e:
                    logger.debug(f"Failed to estimate tokens for outdated files: {e}")
                await context.retranslate_outdated_files(outdated_files)

        if "images" in context.translation_types:
            for lang_code in context.language_codes:
                lang_dir = context.image_dir / lang_code
                if lang_dir.exists():
                    cleanup_orphan_image_metadata(lang_dir)

            with tqdm(total=1, desc="🔍 Checking images") as check_progress:
                outdated_images = context.get_outdated_images()
                check_progress.set_postfix_str(
                    "None" if not outdated_images else f"Found: {len(outdated_images)}"
                )
                check_progress.update(1)

            if outdated_images:
                await context.retranslate_outdated_images(
                    outdated_images, fast_mode=fast_mode
                )

        if "markdown" in context.translation_types:
            try:
                md_pending = context._gather_pending_markdown(update=update)
                md_tokens = estimate_tokens_for_sources(md_pending)
                logger.info(
                    f"Estimated tokens for markdown translations: {md_tokens:,} (files: {len(md_pending)})"
                )
            except Exception as e:
                logger.debug(f"Failed to estimate markdown tokens: {e}")
            md_modified, md_errors = await context.translate_all_markdown_files(
                update=update
            )
            total_modified += md_modified
            all_errors.extend(md_errors)

        if "notebook" in context.translation_types:
            try:
                nb_pending = context._gather_pending_notebooks(update=update)
                nb_tokens = estimate_tokens_for_sources(nb_pending)
                logger.info(
                    f"Estimated tokens for notebook translations: {nb_tokens:,} (files: {len(nb_pending)})"
                )
            except Exception as e:
                logger.debug(f"Failed to estimate notebook tokens: {e}")
            nb_modified, nb_errors = await context.translate_all_notebook_files(
                update=update
            )
            total_modified += nb_modified
            all_errors.extend(nb_errors)

        if "images" in context.translation_types:
            img_modified, img_errors = await context.translate_all_image_files(
                update=update, fast_mode=fast_mode
            )
            total_modified += img_modified
            all_errors.extend(img_errors)

            cleanup_langs = Config.get_language_codes()
            logger.info(
                "Performing final cleanup of translated images across ALL supported languages..."
            )

            dm_all = DirectoryManager(
                context.root_dir,
                context.translations_dir,
                cleanup_langs,
                context.excluded_dirs,
                image_dir=context.image_dir,
            )
            with tqdm(total=1, desc="🧹 Final image cleanup") as cleanup_progress:
                removed_after = dm_all.cleanup_orphaned_translations(
                    markdown=False,
                    images=True,
                    notebooks=False,
                )
                cleanup_progress.set_postfix_str(
                    "None" if removed_after == 0 else f"Removed: {removed_after}"
                )
                cleanup_progress.update(1)

            fast_image_dir = context.root_dir / "translated_images_fast"
            if fast_image_dir.exists():
                temp_dm = DirectoryManager(
                    context.root_dir,
                    context.translations_dir,
                    cleanup_langs,
                    context.excluded_dirs,
                    image_dir=fast_image_dir,
                )
                removed_fast = temp_dm.cleanup_orphaned_translations(
                    markdown=False, images=True, notebooks=False
                )
                logger.info(
                    f"Final cleanup (fast) removed {removed_fast} files from {fast_image_dir}"
                )

        if (
            "markdown" in context.translation_types
            and "images" in context.translation_types
        ):
            await context.fix_incorrect_image_paths()

    except Exception as e:
        logger.error(f"Error during translation: {e}")
        raise

    logger.info(f"Translation completed. Modified {total_modified} files.")
    if all_errors:
        logger.warning(f"Encountered {len(all_errors)} errors during translation")

    return total_modified, all_errors
