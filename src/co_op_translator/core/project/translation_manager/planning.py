"""Planning helpers for determining translation work."""

from __future__ import annotations

from pathlib import Path
from typing import Protocol

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import filter_files
from co_op_translator.utils.common.token_estimation import estimate_translation_tokens


class PlanningContext(Protocol):
    """Subset of TranslationManager state required for planning."""

    root_dir: Path
    excluded_dirs: list[str]
    language_codes: list[str]
    supported_notebook_extensions: list[str]

    def _get_language_root(self, language_code: str) -> Path:
        """Return the output root for a target language."""
        ...


def estimate_tokens(context: PlanningContext, update: bool = False) -> dict:
    """Estimate tokens for the upcoming translation run."""
    return estimate_translation_tokens(context, update=update)


def gather_pending_markdown(context: PlanningContext, update: bool) -> list[Path]:
    """Collect markdown sources that need initial translation."""
    pending: list[Path] = []
    markdown_files = filter_files(context.root_dir, context.excluded_dirs)
    for md_file_path in markdown_files:
        md_file_path = md_file_path.resolve()
        if md_file_path.suffix.lower() not in SUPPORTED_MARKDOWN_EXTENSIONS:
            continue

        for language_code in context.language_codes:
            relative_path = md_file_path.relative_to(context.root_dir)
            translated_md_path = (
                context._get_language_root(language_code) / relative_path
            )
            if not update and translated_md_path.exists():
                continue
            pending.append(md_file_path)
    return pending


def gather_pending_notebooks(context: PlanningContext, update: bool) -> list[Path]:
    """Collect notebook sources that need initial translation."""
    pending: list[Path] = []
    notebook_files: list[Path] = []
    for ext in context.supported_notebook_extensions:
        notebook_files.extend(
            filter_files(context.root_dir, context.excluded_dirs, ext)
        )

    for notebook_file_path in notebook_files:
        notebook_file_path = notebook_file_path.resolve()
        for language_code in context.language_codes:
            relative_path = notebook_file_path.relative_to(context.root_dir)
            translated_notebook_path = (
                context._get_language_root(language_code) / relative_path
            )
            if translated_notebook_path.exists() and not update:
                continue
            pending.append(notebook_file_path)
    return pending
