"""Compatibility helpers for Co-op Translator integrations."""

from typing import Any

__all__ = [
    "get_glossaries",
    "set_glossaries",
]


def __getattr__(name: str) -> Any:
    if name in {"get_glossaries", "set_glossaries"}:
        from co_op_translator.localizeflow.glossary import get_glossaries, set_glossaries

        return {"get_glossaries": get_glossaries, "set_glossaries": set_glossaries}[name]

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
