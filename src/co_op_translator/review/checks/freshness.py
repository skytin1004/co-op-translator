from __future__ import annotations

from pathlib import Path

from co_op_translator.review.checks.structure import expected_translation_path
from co_op_translator.review.models import ReviewIssue, ReviewSeverity
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    read_text_metadata_for_source,
)


def check_translation_freshness(
    root_dir: Path, source_files: list[Path], languages: list[str]
) -> list[ReviewIssue]:
    issues: list[ReviewIssue] = []
    for source_file in source_files:
        current_hash = calculate_file_hash(source_file)
        for language in languages:
            translated_path = expected_translation_path(root_dir, source_file, language)
            if not translated_path.exists():
                continue

            lang_dir = root_dir / "translations" / language
            metadata = read_text_metadata_for_source(lang_dir, source_file)
            stored_hash = metadata.get("original_hash")
            if not stored_hash:
                issues.append(
                    ReviewIssue(
                        check="freshness",
                        severity=ReviewSeverity.ERROR,
                        path=source_file.relative_to(root_dir),
                        language=language,
                        message="Missing translation metadata.",
                    )
                )
            elif stored_hash != current_hash:
                issues.append(
                    ReviewIssue(
                        check="freshness",
                        severity=ReviewSeverity.ERROR,
                        path=source_file.relative_to(root_dir),
                        language=language,
                        message="Translation metadata is stale.",
                    )
                )
    return issues
