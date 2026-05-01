from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

from co_op_translator.review.checks.structure import expected_translation_path
from co_op_translator.review.models import ReviewIssue, ReviewSeverity

MARKDOWN_LINK_PATTERN = re.compile(r"(!?)\[[^\]]*]\(([^)]+)\)")


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


def check_local_links(
    root_dir: Path, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        if source_file.suffix.lower() == ".ipynb":
            continue
        for language in languages:
            translated_path = expected_translation_path(root_dir, source_file, language)
            if not translated_path.exists():
                continue
            content = translated_path.read_text(encoding="utf-8")
            for is_image, target in MARKDOWN_LINK_PATTERN.findall(content):
                if _is_external_link(target) or _target_exists(translated_path, target):
                    continue
                check_name = "image-link" if is_image else "local-link"
                issues.append(
                    ReviewIssue(
                        check=check_name,
                        severity=ReviewSeverity.WARNING,
                        path=translated_path.relative_to(root_dir),
                        language=language,
                        message=f"Local target does not exist: {target}",
                    )
                )
    return issues
