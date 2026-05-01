from __future__ import annotations

from pathlib import Path

import click

from co_op_translator.review.runner import ReviewConfig, ReviewRunner


def _split_language_options(values: tuple[str, ...]) -> list[str]:
    languages: list[str] = []
    for value in values:
        languages.extend(part for part in value.split() if part)
    return languages


@click.command(name="co-op-review")
@click.option(
    "--root-dir",
    "-r",
    default=".",
    help="Root directory of the project to review.",
)
@click.option(
    "--language-code",
    "-l",
    multiple=True,
    help='Language code to review. Can be passed multiple times or as "ko ja".',
)
@click.option(
    "--changed-from",
    help="Git ref to diff against. When provided, only changed source files are reviewed.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["text", "github"]),
    default="text",
    show_default=True,
    help="Output format.",
)
def review_command(
    root_dir: str,
    language_code: tuple[str, ...],
    changed_from: str | None,
    output_format: str,
) -> None:
    """Run deterministic translation review checks without API credentials."""
    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        raise click.ClickException(f"Root directory does not exist: {root_dir}")
    if not root_path.is_dir():
        raise click.ClickException(f"Root path is not a directory: {root_dir}")

    config = ReviewConfig(
        root_dir=root_path,
        languages=_split_language_options(language_code),
        changed_from=changed_from,
    )
    summary = ReviewRunner(config).run()

    if output_format == "github":
        click.echo(summary.to_github_markdown())
    else:
        click.echo(summary.to_text())

    if summary.error_count:
        raise click.ClickException(
            f"co-op-review found {summary.error_count} blocking issue(s)."
        )
