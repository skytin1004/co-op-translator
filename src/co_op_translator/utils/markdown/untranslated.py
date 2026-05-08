from __future__ import annotations

import re
from dataclasses import dataclass


FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(
    r"^(?P<prefix>\s{0,3}#{1,6}\s+)(?P<text>.*?)(?P<suffix>\s+#+\s*)?$"
)
MARKDOWN_LINK_RE = re.compile(r"(!?)\[([^\]]*)]\(([^)]+)\)")

_STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "by",
    "for",
    "from",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "this",
    "to",
    "with",
}

_PRESERVED_TERMS = {
    "ai",
    "api",
    "azure",
    "bash",
    "c",
    "cli",
    "co",
    "copilot",
    "co-op",
    "discord",
    "foundry",
    "github",
    "html",
    "http",
    "https",
    "java",
    "javascript",
    "json",
    "llm",
    "markdown",
    "mcp",
    "microsoft",
    "node",
    "notebook",
    "openai",
    "op",
    "powershell",
    "python",
    "sdk",
    "typescript",
    "translator",
    "url",
    "yaml",
}


@dataclass(frozen=True)
class MarkdownTextUnit:
    kind: str
    text: str
    occurrence: int
    line_number: int
    link_index: int | None = None


@dataclass(frozen=True)
class UntranslatedTextUnit:
    kind: str
    source_text: str
    translated_text: str
    occurrence: int
    translated_line_number: int
    link_index: int | None = None


def has_translatable_english(text: str) -> bool:
    """Return True when text contains English prose likely meant for translation."""

    visible = _visible_text(text)
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]*", visible)
    for word in words:
        normalized = word.strip(".-+#").lower()
        if len(normalized) < 3:
            continue
        if normalized in _STOP_WORDS or normalized in _PRESERVED_TERMS:
            continue
        if word.isupper() and len(word) <= 5:
            continue
        return True
    return False


def find_untranslated_markdown_units(
    source_content: str, translated_content: str
) -> list[UntranslatedTextUnit]:
    source_units = _extract_visible_units(source_content)
    translated_units = _extract_visible_units(translated_content)
    source_by_key = {(unit.kind, unit.occurrence): unit for unit in source_units}
    translated_by_key = {
        (unit.kind, unit.occurrence): unit for unit in translated_units
    }

    issues: list[UntranslatedTextUnit] = []
    matched_lines: set[int] = set()

    for kind in ("heading", "link_text"):
        for key, source_unit in source_by_key.items():
            if key[0] != kind:
                continue
            translated_unit = translated_by_key.get(key)
            if not translated_unit:
                continue
            if _same_visible_text(source_unit.text, translated_unit.text):
                if not has_translatable_english(source_unit.text):
                    continue
                issues.append(_to_untranslated_unit(source_unit, translated_unit))
                matched_lines.add(translated_unit.line_number)

    for key, source_unit in source_by_key.items():
        if key[0] != "line":
            continue
        translated_unit = translated_by_key.get(key)
        if not translated_unit:
            continue
        if translated_unit.line_number in matched_lines:
            continue
        if _same_visible_text(source_unit.text, translated_unit.text):
            if not has_translatable_english(source_unit.text):
                continue
            issues.append(_to_untranslated_unit(source_unit, translated_unit))

    return issues


def apply_untranslated_markdown_replacements(
    translated_content: str,
    units: list[UntranslatedTextUnit],
    replacements: dict[UntranslatedTextUnit, str],
) -> str:
    if not units:
        return translated_content

    lines = translated_content.splitlines(keepends=True)
    for unit in sorted(units, key=lambda item: item.translated_line_number, reverse=True):
        replacement = replacements.get(unit, "").strip()
        if not replacement or _same_visible_text(unit.translated_text, replacement):
            continue
        if unit.translated_line_number < 0 or unit.translated_line_number >= len(lines):
            continue

        line = lines[unit.translated_line_number]
        ending = ""
        if line.endswith("\r\n"):
            line, ending = line[:-2], "\r\n"
        elif line.endswith("\n") or line.endswith("\r"):
            line, ending = line[:-1], line[-1]

        if unit.kind == "line":
            lines[unit.translated_line_number] = replacement + ending
        elif unit.kind == "heading":
            lines[unit.translated_line_number] = (
                _replace_heading_text(line, replacement) + ending
            )
        elif unit.kind == "link_text" and unit.link_index is not None:
            lines[unit.translated_line_number] = (
                _replace_link_text(line, unit.link_index, replacement) + ending
            )

    return "".join(lines)


def _extract_visible_units(content: str) -> list[MarkdownTextUnit]:
    units: list[MarkdownTextUnit] = []
    heading_occurrence = 0
    link_occurrence = 0
    line_occurrence = 0

    for line_number, line in _iter_non_code_lines(content):
        raw_line = line.rstrip("\r\n")
        if _is_structural_line(raw_line):
            continue

        heading_match = HEADING_RE.match(raw_line)
        if heading_match:
            text = heading_match.group("text").strip()
            if text:
                units.append(
                    MarkdownTextUnit(
                        kind="heading",
                        text=text,
                        occurrence=heading_occurrence,
                        line_number=line_number,
                    )
                )
                heading_occurrence += 1

        link_index_on_line = 0
        for is_image, label, _target in MARKDOWN_LINK_RE.findall(raw_line):
            if is_image or not label.strip():
                continue
            units.append(
                MarkdownTextUnit(
                    kind="link_text",
                    text=label.strip(),
                    occurrence=link_occurrence,
                    line_number=line_number,
                    link_index=link_index_on_line,
                )
            )
            link_occurrence += 1
            link_index_on_line += 1

        visible_line = _visible_text(raw_line)
        if visible_line:
            units.append(
                MarkdownTextUnit(
                    kind="line",
                    text=visible_line,
                    occurrence=line_occurrence,
                    line_number=line_number,
                )
            )
            line_occurrence += 1

    return units


def _iter_non_code_lines(content: str):
    in_fence = False
    in_frontmatter = False
    frontmatter_possible = True

    for line_number, line in enumerate(content.splitlines(keepends=True)):
        stripped = line.strip()
        if line_number == 0 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---" and line_number != 0:
                in_frontmatter = False
            continue

        if frontmatter_possible and stripped:
            frontmatter_possible = False

        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield line_number, line


def _is_structural_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped in {"---", "***", "___"}:
        return True
    if stripped.startswith("<!--") or stripped.endswith("-->"):
        return True
    if re.fullmatch(r"\|?[\s:|-]+\|?", stripped):
        return True
    return False


def _visible_text(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = MARKDOWN_LINK_RE.sub(lambda m: m.group(2), text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s+", "", text)
    text = re.sub(r"^\s{0,3}>\s?", "", text)
    text = re.sub(r"^\s*(?:[-+*]|\d+[.)])\s+", "", text)
    text = re.sub(r"^\s*\[[ xX]]\s+", "", text)
    text = re.sub(r"[*_~]+", "", text)
    return _normalize_visible_text(text)


def _normalize_visible_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _same_visible_text(left: str, right: str) -> bool:
    return _visible_text(left).casefold() == _visible_text(right).casefold()


def _to_untranslated_unit(
    source_unit: MarkdownTextUnit, translated_unit: MarkdownTextUnit
) -> UntranslatedTextUnit:
    return UntranslatedTextUnit(
        kind=source_unit.kind,
        source_text=source_unit.text,
        translated_text=translated_unit.text,
        occurrence=source_unit.occurrence,
        translated_line_number=translated_unit.line_number,
        link_index=translated_unit.link_index,
    )


def _replace_heading_text(line: str, replacement: str) -> str:
    match = HEADING_RE.match(line)
    if not match:
        return line
    return f"{match.group('prefix')}{replacement}{match.group('suffix')}"


def _replace_link_text(line: str, target_link_index: int, replacement: str) -> str:
    current_index = 0

    def _replace(match: re.Match[str]) -> str:
        nonlocal current_index
        if match.group(1):
            return match.group(0)
        if current_index == target_link_index:
            current_index += 1
            return f"[{replacement}]({match.group(3)})"
        current_index += 1
        return match.group(0)

    return MARKDOWN_LINK_RE.sub(_replace, line)
