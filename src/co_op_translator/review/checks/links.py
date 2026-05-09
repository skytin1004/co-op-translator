from __future__ import annotations

from pathlib import Path
from typing import Iterator
from urllib.parse import unquote

from markdown_it import MarkdownIt

from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.review.targets import ReviewTarget

MARKDOWN_PARSER = MarkdownIt("commonmark")


def _is_external_link(target: str) -> bool:
    lowered = target.lower()
    return (
        "://" in lowered
        or lowered.startswith("#")
        or lowered.startswith("mailto:")
        or lowered.startswith("tel:")
    )


def _clean_link_target(target: str) -> str:
    target = target.strip().strip("<>")
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def _target_exists(translated_path: Path, target: str) -> bool:
    cleaned = _clean_link_target(target)
    if not cleaned:
        return True
    candidate = Path(cleaned)
    if candidate.is_absolute():
        return candidate.exists()
    return (translated_path.parent / candidate).exists()


def _iter_markdown_link_targets(content: str) -> Iterator[tuple[bool, str]]:
    for token in MARKDOWN_PARSER.parse(content):
        if token.type != "inline" or not token.children:
            continue

        for child in token.children:
            if child.type == "link_open":
                href = child.attrs.get("href") if child.attrs else None
                if href:
                    yield False, href
            elif child.type == "image":
                src = child.attrs.get("src") if child.attrs else None
                if src:
                    yield True, src


def check_local_links(
    target: ReviewTarget, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        if source_file.suffix.lower() == ".ipynb":
            continue
        for language in languages:
            translated_path = target.translated_path(source_file, language)
            if not translated_path.exists():
                continue
            content = translated_path.read_text(encoding="utf-8")
            for is_image, link_target in _iter_markdown_link_targets(content):
                if _is_external_link(link_target) or _target_exists(
                    translated_path, link_target
                ):
                    continue
                check_name = "image-link" if is_image else "local-link"
                issues.append(
                    ReviewIssue(
                        check=check_name,
                        severity=ReviewSeverity.WARNING,
                        path=target.display_translated_path(translated_path),
                        language=language,
                        message=f"Local target does not exist: {link_target}",
                    )
                )
    return issues
