"""Compatibility facade for markdown utility helpers.

The implementation is split across focused modules, but this file preserves the
historical import path used by CLI, core translators, and tests.
"""

import logging

from co_op_translator.utils.llm.anchor_links import (
    _extract_headings_with_slugs,
    _extract_internal_link_fragments,
    _slugify_heading_text,
)
from co_op_translator.utils.llm.cjk_emphasis import (
    CJK_CHAR_CLASS,
    CJK_EMPHASIS_LANGUAGE_PREFIXES,
    _apply_cjk_emphasis_pattern,
    _build_cjk_emphasis_pattern,
    _CJK_CHAR_RE,
    _CJK_EMPHASIS_PATTERNS,
    _CJK_FULL_TEXT_RE,
    _collect_inline_code_spans_with_markdown_ast,
    _EMPHASIS_INNER_TEXT_PATTERN,
    normalize_cjk_emphasis_markers,
)
from co_op_translator.utils.llm.chunking import (
    _group_lines_preserving_list_items,
    _parse_markdown_text_and_code_parts,
    count_links_in_markdown,
    count_tokens,
    get_tokenizer,
    process_markdown,
    process_markdown_with_many_links,
    split_markdown_content,
)
from co_op_translator.utils.llm.code_blocks import (
    extract_json_from_markdown_codeblock,
    replace_code_blocks,
    restore_code_blocks,
)
from co_op_translator.utils.llm.link_rewriter import (
    build_translated_image_link,
    get_translated_markdown_dir,
    migrate_notebook_links,
    normalize_internal_anchor_links,
    update_image_links,
    update_links,
    update_notebook_links,
    update_readme_translation_links,
    update_untranslated_file_links,
)
from co_op_translator.utils.llm.prompt_builder import (
    SPLIT_DELIMITER,
    _read_language_prompt_template,
    generate_prompt_template,
)
from co_op_translator.utils.llm.quality import (
    compare_line_breaks,
    generate_evaluation_prompt,
)

logger = logging.getLogger(__name__)

__all__ = [
    "SPLIT_DELIMITER",
    "_read_language_prompt_template",
    "_apply_cjk_emphasis_pattern",
    "_build_cjk_emphasis_pattern",
    "_CJK_CHAR_RE",
    "_CJK_EMPHASIS_PATTERNS",
    "_CJK_FULL_TEXT_RE",
    "_collect_inline_code_spans_with_markdown_ast",
    "_EMPHASIS_INNER_TEXT_PATTERN",
    "_extract_headings_with_slugs",
    "_extract_internal_link_fragments",
    "_group_lines_preserving_list_items",
    "_parse_markdown_text_and_code_parts",
    "_slugify_heading_text",
    "build_translated_image_link",
    "CJK_CHAR_CLASS",
    "CJK_EMPHASIS_LANGUAGE_PREFIXES",
    "compare_line_breaks",
    "count_links_in_markdown",
    "count_tokens",
    "extract_json_from_markdown_codeblock",
    "generate_evaluation_prompt",
    "generate_prompt_template",
    "get_tokenizer",
    "get_translated_markdown_dir",
    "migrate_notebook_links",
    "normalize_cjk_emphasis_markers",
    "normalize_internal_anchor_links",
    "process_markdown",
    "process_markdown_with_many_links",
    "replace_code_blocks",
    "restore_code_blocks",
    "split_markdown_content",
    "update_image_links",
    "update_links",
    "update_notebook_links",
    "update_readme_translation_links",
    "update_untranslated_file_links",
]
