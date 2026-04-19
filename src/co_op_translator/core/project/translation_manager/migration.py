"""Migration steps used by the project translation workflow."""

from __future__ import annotations

import logging
from typing import Protocol

from co_op_translator.utils.common.file_utils import (
    canonicalize_image_links_in_translations,
    migrate_images_to_webp,
    migrate_translated_image_filenames,
)

logger = logging.getLogger(__name__)


class MigrationContext(Protocol):
    """Subset of TranslationManager state required for migration steps."""

    image_dir: object
    language_codes: list[str]
    translation_types: list[str]
    translations_dir: object
    directory_manager: object


def run_image_and_link_migrations(context: MigrationContext) -> None:
    """Run translated-image migrations and keep content links in sync.

    Image file migrations only run when image translation is enabled, but link
    migrations still run for markdown/notebook modes to rewrite legacy links.
    """
    rename_map: dict[str, str] = {}
    migrated_image_count = 0
    should_migrate_links = (
        "markdown" in context.translation_types
        or "notebook" in context.translation_types
    )

    if "images" in context.translation_types:
        try:
            rename_map = migrate_translated_image_filenames(
                context.image_dir, context.language_codes
            )
            migrated_image_count += len(rename_map)
        except Exception as e:
            logger.warning(f"Image filename migration skipped: {e}")
            rename_map = {}

        try:
            webp_rename_map = migrate_images_to_webp(
                context.image_dir, context.language_codes
            )
        except Exception as e:
            logger.warning(f"WebP migration skipped: {e}")
        else:
            rename_map.update(webp_rename_map)
            migrated_image_count += len(webp_rename_map)
    else:
        logger.info(
            "Skipping translated image migration because image translation is disabled"
        )

    if not should_migrate_links:
        return

    try:
        migrated_md = context.directory_manager.migrate_markdown_image_links(rename_map)
        migrated_nb = context.directory_manager.migrate_notebook_image_links(rename_map)
        logger.info(
            "Updated image links in %d markdown and %d notebook files (migrated image files: %d)",
            migrated_md,
            migrated_nb,
            migrated_image_count,
        )
    except Exception as e:
        logger.warning(f"Image link migration skipped: {e}")

    try:
        md_fix, nb_fix = canonicalize_image_links_in_translations(
            context.translations_dir, context.image_dir
        )
        if md_fix or nb_fix:
            logger.info(
                "Canonicalized image links in %d markdown and %d notebooks",
                md_fix,
                nb_fix,
            )
    except Exception as e:
        logger.warning(f"Image link canonicalization skipped: {e}")
