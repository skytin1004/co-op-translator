from __future__ import annotations

import json
import re
from pathlib import Path

from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.notebooks import notebook_markdown_cells, read_notebook
from co_op_translator.review.targets import ReviewTarget

FENCE_PATTERN = re.compile(r"^\s*(```|~~~)", re.MULTILINE)
ADMONITION_PATTERN = re.compile(
    r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def _has_frontmatter(content: str) -> bool:
    return content.startswith("---\n")


def _frontmatter_is_closed(content: str) -> bool:
    if not _has_frontmatter(content):
        return True
    return content.find("\n---", 4) != -1


def _fence_count(content: str) -> int:
    return len(FENCE_PATTERN.findall(content))


def _admonition_count(content: str) -> int:
    return len(ADMONITION_PATTERN.findall(content))


def _check_markdown_file(
    target: ReviewTarget, source_file: Path, translated_path: Path, language: str
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    source_content = source_file.read_text(encoding="utf-8")
    translated_content = translated_path.read_text(encoding="utf-8")
    relative_path = target.display_source_path(source_file)

    if _has_frontmatter(source_content):
        if not _has_frontmatter(translated_content):
            issues.append(
                ReviewIssue(
                    check="markdown-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message="Translated file is missing source frontmatter.",
                )
            )
        elif not _frontmatter_is_closed(translated_content):
            issues.append(
                ReviewIssue(
                    check="markdown-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message="Translated frontmatter is not closed.",
                )
            )

    if _fence_count(source_content) != _fence_count(translated_content):
        issues.append(
            ReviewIssue(
                check="markdown-integrity",
                severity=ReviewSeverity.ERROR,
                path=relative_path,
                language=language,
                message="Code fence count differs from the source file.",
            )
        )

    return issues


def _check_notebook_file(
    target: ReviewTarget, source_file: Path, translated_path: Path, language: str
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    relative_path = target.display_source_path(source_file)

    try:
        translated_notebook = read_notebook(translated_path)
    except (OSError, json.JSONDecodeError):
        return [
            ReviewIssue(
                check="notebook-integrity",
                severity=ReviewSeverity.ERROR,
                path=relative_path,
                language=language,
                message="Translated notebook is not valid JSON.",
            )
        ]

    try:
        source_notebook = read_notebook(source_file)
    except (OSError, json.JSONDecodeError):
        return issues

    source_cells = notebook_markdown_cells(source_notebook)
    translated_cells = notebook_markdown_cells(translated_notebook)

    for cell_position, source_cell in enumerate(source_cells):
        if cell_position >= len(translated_cells):
            issues.append(
                ReviewIssue(
                    check="notebook-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message=(
                        f"Translated notebook is missing markdown cell "
                        f"{source_cell.ordinal} from the source notebook."
                    ),
                )
            )
            continue

        translated_cell = translated_cells[cell_position]
        if _fence_count(source_cell.content) != _fence_count(translated_cell.content):
            issues.append(
                ReviewIssue(
                    check="notebook-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message=(
                        f"Markdown cell {source_cell.ordinal} code fence count "
                        "differs from the source cell."
                    ),
                )
            )

        if _admonition_count(source_cell.content) != _admonition_count(
            translated_cell.content
        ):
            issues.append(
                ReviewIssue(
                    check="notebook-integrity",
                    severity=ReviewSeverity.ERROR,
                    path=relative_path,
                    language=language,
                    message=(
                        f"Markdown cell {source_cell.ordinal} GitHub admonition "
                        "count differs from the source cell."
                    ),
                )
            )

    return issues


def check_markdown_integrity(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        for language in languages:
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                continue
            if source_file.suffix.lower() == ".ipynb":
                issues.extend(
                    _check_notebook_file(target, source_file, translated_path, language)
                )
            else:
                issues.extend(
                    _check_markdown_file(target, source_file, translated_path, language)
                )
    return issues
