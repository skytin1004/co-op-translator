from __future__ import annotations

from dataclasses import dataclass
import re

GITHUB_ADMONITION_TYPES = ("NOTE", "TIP", "IMPORTANT", "WARNING", "CAUTION")

_GITHUB_ADMONITION_LINE_RE = re.compile(
    r"^(?P<prefix>[ \t]*(?:>[ \t]*)+)"
    r"(?P<marker>\[!(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION)\])"
    r"(?P<trailing>[^\r\n]*)$"
)
_FENCE_LINE_RE = re.compile(r"^[ \t]*(?:`{3,}|~{3,})")


@dataclass(frozen=True)
class CollapsedGitHubAdmonition:
    line_number: int
    marker: str
    trailing_text: str


def find_collapsed_github_admonitions(
    content: str,
) -> list[CollapsedGitHubAdmonition]:
    """Find GitHub admonition markers that lost the required following line break."""

    collapsed: list[CollapsedGitHubAdmonition] = []
    in_fence = False

    for line_number, line in enumerate(content.splitlines(keepends=True), start=1):
        body, _line_ending = _split_line_ending(line)
        if _is_fence_line(body):
            in_fence = not in_fence
            continue

        if in_fence:
            continue

        match = _GITHUB_ADMONITION_LINE_RE.match(body)
        if not match:
            continue

        trailing_text = match.group("trailing").strip()
        if not trailing_text:
            continue

        collapsed.append(
            CollapsedGitHubAdmonition(
                line_number=line_number,
                marker=match.group("marker"),
                trailing_text=trailing_text,
            )
        )

    return collapsed


def normalize_github_admonitions(content: str) -> str:
    """Repair collapsed GitHub admonition markers while preserving line endings."""

    output_lines: list[str] = []
    in_fence = False

    for line in content.splitlines(keepends=True):
        body, line_ending = _split_line_ending(line)
        if _is_fence_line(body):
            in_fence = not in_fence
            output_lines.append(line)
            continue

        if not in_fence:
            match = _GITHUB_ADMONITION_LINE_RE.match(body)
            if match and match.group("trailing").strip():
                prefix = match.group("prefix")
                marker = match.group("marker")
                trailing_text = match.group("trailing").lstrip()
                separator = line_ending or "\n"
                output_lines.append(f"{prefix}{marker}{separator}")
                output_lines.append(f"{prefix}{trailing_text}{line_ending}")
                continue

        output_lines.append(line)

    return "".join(output_lines)


def _split_line_ending(line: str) -> tuple[str, str]:
    if line.endswith("\r\n"):
        return line[:-2], "\r\n"
    if line.endswith("\n"):
        return line[:-1], "\n"
    if line.endswith("\r"):
        return line[:-1], "\r"
    return line, ""


def _is_fence_line(line: str) -> bool:
    return bool(_FENCE_LINE_RE.match(line))
