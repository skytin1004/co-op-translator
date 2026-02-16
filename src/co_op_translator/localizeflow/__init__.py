"""Localizeflow public API.

Use lazy imports to avoid importing the full translation stack when callers only
need lightweight utilities (for example estimation helpers in tests).
"""

from typing import Any

__all__ = [
    "get_glossaries",
    "set_glossaries",
    "ensure_localizeflow_frontmatter_parser",
    "run_translation",
]


def __getattr__(name: str) -> Any:
    if name in {"get_glossaries", "set_glossaries"}:
        from co_op_translator.localizeflow.glossary import get_glossaries, set_glossaries

        return {"get_glossaries": get_glossaries, "set_glossaries": set_glossaries}[name]

    if name == "ensure_localizeflow_frontmatter_parser":
        from co_op_translator.localizeflow.frontmatter import (
            ensure_localizeflow_frontmatter_parser,
        )

        return ensure_localizeflow_frontmatter_parser

    if name == "run_translation":
        from co_op_translator.localizeflow.runner import run_translation

        return run_translation

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
