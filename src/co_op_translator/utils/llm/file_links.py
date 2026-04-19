"""Non-image file and README language link rewriting helpers."""

from __future__ import annotations

import logging
import os
import re
from pathlib import Path
from urllib.parse import urlparse

from co_op_translator.config.constants import (
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_MARKDOWN_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.common.file_utils import get_filename_and_extension

logger = logging.getLogger(__name__)


def update_untranslated_file_links(
    markdown_string: str,
    md_file_path: Path,
    language_code: str,
    translations_dir: Path,
    root_dir: Path,
    use_translated_notebook: bool = True,
) -> str:
    """Update links to untranslated files to point to original source files.

    Processes links to files that are not translated (videos, documents, PDFs, etc.)
    and updates their paths to maintain correct relative links from translated markdown
    files back to the original source files.

    Skips:
    - Web URLs (http, https, mailto)
    - Image files (handled by update_image_links)
    - Markdown files (always translated)
    - Notebook files (if use_translated_notebook=True, they are translated; if False, processed here)

    Args:
        markdown_string (str): The markdown content to process
        md_file_path (Path): Path to the markdown file being processed
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations
        root_dir (Path): Root directory of the project
        use_translated_notebook (bool): Whether to use translated notebooks (False = process notebook links here)

    Returns:
        str: Updated markdown content with corrected untranslated file links
    """
    file_pattern = r"\[(.*?)\]\((.*?)\)"
    file_matches = re.findall(file_pattern, markdown_string)

    for alt_text, link in file_matches:
        parsed_url = urlparse(link)

        # Keep same-document anchors untouched (e.g., [Section](#section)).
        if parsed_url.fragment and not parsed_url.path:
            logger.info(f"Skipping internal anchor link {link}")
            continue

        if (
            parsed_url.scheme in ("mailto", "http", "https")
            or "@" in link
            or link.endswith((".com", ".org", ".net"))
        ):
            logger.info(f"Skipped {link} as it is an email or web URL")
            continue

        path = parsed_url.path
        original_filename, file_ext = get_filename_and_extension(path)

        if file_ext in SUPPORTED_IMAGE_EXTENSIONS:
            logger.info(f"Skipping image file {link}")
            continue

        if file_ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            logger.info(f"Skipping markdown file {link}")
            continue

        if file_ext in SUPPORTED_NOTEBOOK_EXTENSIONS and use_translated_notebook:
            logger.info(f"Skipping notebook file {link}")
            continue

        logger.info(f"Processing untranslated file link {link}")
        try:
            translated_md_dir = (
                translations_dir
                / language_code
                / md_file_path.relative_to(root_dir).parent
            )
            original_linked_file_path = (md_file_path.parent / path).resolve()

            updated_link = os.path.relpath(
                original_linked_file_path, translated_md_dir
            ).replace(os.path.sep, "/")

            old_file_markup = f"[{alt_text}]({link})"
            new_file_markup = f"[{alt_text}]({updated_link})"
            markdown_string = markdown_string.replace(old_file_markup, new_file_markup)

            logger.info(f"Updated untranslated file link: {new_file_markup}")

        except Exception as e:
            logger.error(f"Error processing untranslated file link {link}: {e}")
            continue

    return markdown_string


def update_readme_translation_links(
    markdown_string: str,
    language_code: str,
    translations_dir: Path,
) -> str:
    """Update README translation navigation links in markdown content.

    Processes links that point to other language versions of README files
    (e.g., translations/ko/README.md, translations/es/README.md) and updates
    them to maintain correct relative paths in translated files.

    Args:
        markdown_string (str): The markdown content to process
        language_code (str): Target language code
        translations_dir (Path): Directory containing translations

    Returns:
        str: Updated markdown content with corrected README translation links
    """
    logger.info("Updating README translation navigation links in the markdown file")

    translation_link_pattern = (
        r"(\[.*?\])\((?:\.?/)?translations/([a-zA-Z\-]+)/README\.md\)"
    )

    def replace_link(match):
        alt_text_with_brackets = match.group(1)
        other_language_code = match.group(2)
        logger.info(
            f"Found language code in link: {other_language_code} with alt text '{alt_text_with_brackets}'"
        )

        other_translated_md_path = (
            translations_dir / other_language_code / "README.md"
        ).resolve()
        logger.debug(
            f"Other translated markdown path (absolute): {other_translated_md_path}"
        )

        current_translated_md_path = (
            translations_dir / language_code / "README.md"
        ).resolve()
        current_md_dir = current_translated_md_path.parent
        logger.debug(f"Current markdown directory (current_md_dir): {current_md_dir}")

        try:
            relative_dir = os.path.relpath(
                other_translated_md_path.parent, current_md_dir
            ).replace(os.path.sep, "/")
            relative_path_to_translation = f"{relative_dir}/README.md"
            logger.info(
                f"Relative path to {other_language_code} translation: {relative_path_to_translation}"
            )

            new_translation_link_markup = (
                f"{alt_text_with_brackets}({relative_path_to_translation})"
            )
            logger.info(
                f"Updated translation link markdown: {new_translation_link_markup}"
            )
            return new_translation_link_markup
        except Exception as e:
            logger.error(
                f"Error updating translation links for {other_language_code}: {e}"
            )
            return match.group(0)

    markdown_string = re.sub(translation_link_pattern, replace_link, markdown_string)

    return markdown_string
