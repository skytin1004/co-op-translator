"""Markdown and notebook link rewriting helpers."""

from __future__ import annotations

import logging
from pathlib import Path

from co_op_translator.utils.llm.file_links import (
    update_readme_translation_links,
    update_untranslated_file_links,
)
from co_op_translator.utils.llm.image_links import (
    build_translated_image_link,
    get_translated_markdown_dir,
    update_image_links,
)
from co_op_translator.utils.llm.notebook_links import (
    migrate_notebook_links,
    update_notebook_links,
)
from co_op_translator.utils.llm.anchor_links import normalize_internal_anchor_links

logger = logging.getLogger(__name__)


def update_links(
    md_file_path: Path,
    markdown_string: str,
    language_code: str,
    root_dir: Path,
    translations_dir: Path | None = None,
    translated_images_dir: Path | None = None,
    translation_types: list[str] = None,
) -> str:
    logger.info("Updating links in the markdown file")

    if translation_types is None:
        translation_types = ["markdown", "notebook", "images"]

    if translations_dir is None:
        translations_dir = root_dir / "translations"
    if translated_images_dir is None:
        translated_images_dir = root_dir / "translated_images"

    markdown_string = update_image_links(
        markdown_string,
        md_file_path,
        language_code,
        translations_dir,
        translated_images_dir,
        root_dir,
        use_translated_images="images" in translation_types,
    )
    markdown_string = update_untranslated_file_links(
        markdown_string,
        md_file_path,
        language_code,
        translations_dir,
        root_dir,
        use_translated_notebook="notebook" in translation_types,
    )
    return update_readme_translation_links(
        markdown_string, language_code, translations_dir
    )


__all__ = [
    "build_translated_image_link",
    "get_translated_markdown_dir",
    "migrate_notebook_links",
    "normalize_internal_anchor_links",
    "update_image_links",
    "update_links",
    "update_notebook_links",
    "update_readme_translation_links",
    "update_untranslated_file_links",
]
