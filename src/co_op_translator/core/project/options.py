"""Shared option normalization for CLI and programmatic APIs."""

from __future__ import annotations


def resolve_translation_types(
    *,
    markdown: bool = False,
    images: bool = False,
    notebook: bool = False,
) -> list[str]:
    """Resolve content-type flags into the canonical translation type list."""
    translation_types: list[str] = []
    if markdown:
        translation_types.append("markdown")
    if images:
        translation_types.append("images")
    if notebook:
        translation_types.append("notebook")
    if not translation_types:
        translation_types = ["markdown", "notebook", "images"]
    return translation_types
