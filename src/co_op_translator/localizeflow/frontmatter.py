"""Localizeflow-specific frontmatter helpers.

This module augments the default Co-op Translator frontmatter handling so that
nested quickLinks entries get translated (title/description) while their slugs
remain untouched. The behavior is applied only when Localizeflow invokes the
translator, leaving the upstream CLI unaffected.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List, Tuple

from co_op_translator.utils.llm.frontmatter_utils import (
    FrontmatterConfig,
    FrontmatterParser,
)


class LocalizeflowFrontmatterParser(FrontmatterParser):
    """Frontmatter parser that understands Localizeflow quickLinks."""

    QUICKLINKS_FIELD_NAME = "quickLinks"
    QUICKLINKS_TRANSLATABLE_FIELDS = ("title", "description")
    QUICKLINKS_KEY_PATTERN = re.compile(r"^quickLinks\[(\d+)\]\.(\w+)$")

    def __init__(self, config: FrontmatterConfig | None = None) -> None:
        super().__init__(config)

    def split_fields(
        self, frontmatter: Dict[str, Any]
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        preserve, translate = super().split_fields(frontmatter)

        quicklinks = frontmatter.get(self.QUICKLINKS_FIELD_NAME)
        if isinstance(quicklinks, list):
            preserve[self.QUICKLINKS_FIELD_NAME] = quicklinks
            translate.update(self._collect_quicklinks_translation_fields(quicklinks))

        return preserve, translate

    def merge_fields(
        self, preserve_fields: Dict[str, Any], translated_fields: Dict[str, Any]
    ) -> Dict[str, Any]:
        preserve_copy = dict(preserve_fields)
        translated_copy = dict(translated_fields)

        self._apply_nested_field_translations(preserve_copy, translated_copy)

        return super().merge_fields(preserve_copy, translated_copy)

    def _collect_quicklinks_translation_fields(
        self, quicklinks: List[Any]
    ) -> Dict[str, str]:
        pseudo_fields: Dict[str, str] = {}
        for index, item in enumerate(quicklinks):
            if not isinstance(item, dict):
                continue

            for field in self.QUICKLINKS_TRANSLATABLE_FIELDS:
                value = item.get(field)
                if isinstance(value, str):
                    pseudo_key = f"{self.QUICKLINKS_FIELD_NAME}[{index}].{field}"
                    pseudo_fields[pseudo_key] = value
        return pseudo_fields

    def _apply_nested_field_translations(
        self,
        preserve_fields: Dict[str, Any],
        translated_fields: Dict[str, Any],
    ) -> None:
        quicklinks = preserve_fields.get(self.QUICKLINKS_FIELD_NAME)
        if not isinstance(quicklinks, list):
            return

        keys_to_remove: List[str] = []
        for key, value in list(translated_fields.items()):
            match = self.QUICKLINKS_KEY_PATTERN.match(key)
            if not match:
                continue

            index = int(match.group(1))
            field_name = match.group(2)

            if field_name not in self.QUICKLINKS_TRANSLATABLE_FIELDS:
                keys_to_remove.append(key)
                continue

            if 0 <= index < len(quicklinks):
                item = quicklinks[index]
                if isinstance(item, dict):
                    item[field_name] = value
            keys_to_remove.append(key)

        for key in keys_to_remove:
            translated_fields.pop(key, None)


def ensure_localizeflow_frontmatter_parser() -> LocalizeflowFrontmatterParser:
    """Ensure the global parser is patched with Localizeflow behavior."""

    # Import locally to avoid circular imports
    from co_op_translator.utils.llm import frontmatter_utils as fm_utils

    parser = fm_utils.get_frontmatter_parser()
    if isinstance(parser, LocalizeflowFrontmatterParser):
        return parser

    config = getattr(parser, "config", None)
    lf_parser = LocalizeflowFrontmatterParser(config=config)
    fm_utils._default_parser = lf_parser  # type: ignore[attr-defined]
    return lf_parser
