from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from co_op_translator.review.checks.freshness import check_translation_freshness
from co_op_translator.review.checks.links import check_local_links
from co_op_translator.review.checks.markdown_integrity import check_markdown_integrity
from co_op_translator.review.checks.structure import check_translation_structure
from co_op_translator.review.discovery import (
    DEFAULT_EXCLUDED_DIRS,
    discover_changed_source_files,
    discover_languages,
    discover_source_files,
)
from co_op_translator.review.models import ReviewSummary


@dataclass(frozen=True)
class ReviewConfig:
    root_dir: Path
    languages: list[str] = field(default_factory=list)
    changed_from: str | None = None
    excluded_dirs: set[str] = field(default_factory=lambda: set(DEFAULT_EXCLUDED_DIRS))


class ReviewRunner:
    def __init__(self, config: ReviewConfig):
        self.config = config

    def run(self) -> ReviewSummary:
        root_dir = self.config.root_dir.resolve()
        languages = self.config.languages or discover_languages(root_dir)

        if self.config.changed_from:
            source_files = discover_changed_source_files(
                root_dir, self.config.changed_from, self.config.excluded_dirs
            )
        else:
            source_files = discover_source_files(root_dir, self.config.excluded_dirs)

        issues = []
        if languages:
            issues.extend(
                check_translation_structure(root_dir, source_files, languages)
            )
            issues.extend(
                check_translation_freshness(root_dir, source_files, languages)
            )
            issues.extend(check_markdown_integrity(root_dir, source_files, languages))
            issues.extend(check_local_links(root_dir, source_files, languages))

        return ReviewSummary(
            root_dir=root_dir,
            source_files=[path.relative_to(root_dir) for path in source_files],
            languages=languages,
            issues=issues,
        )
