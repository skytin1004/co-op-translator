from __future__ import annotations

from pathlib import Path

from co_op_translator.review.models import ReviewIssue, ReviewSeverity


def expected_translation_path(root_dir: Path, source_file: Path, language: str) -> Path:
    return root_dir / "translations" / language / source_file.relative_to(root_dir)


def check_translation_structure(
    root_dir: Path, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        for language in languages:
            translated_path = expected_translation_path(root_dir, source_file, language)
            if not translated_path.exists():
                issues.append(
                    ReviewIssue(
                        check="structure",
                        severity=ReviewSeverity.ERROR,
                        path=source_file.relative_to(root_dir),
                        language=language,
                        message="Missing translated file.",
                    )
                )
    return issues
