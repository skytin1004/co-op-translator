from __future__ import annotations

import json
import re
from pathlib import Path

from markdown_it import MarkdownIt

from co_op_translator.utils.llm.markdown_utils import process_markdown

FIXTURE_ROOT = Path(__file__).parent / "fixtures" / "public_issues"
REGISTRY_PATH = FIXTURE_ROOT / "registry.json"
PRIORITY_ISSUES = {357, 400, 406, 230, 219, 381, 388}


def _load_registry() -> list[dict]:
    with REGISTRY_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def _read_fixture(entry: dict, key: str) -> str:
    return (FIXTURE_ROOT / entry[key]).read_text(encoding="utf-8")


def _fence_marker_count(markdown_text: str) -> int:
    return sum(
        1 for line in markdown_text.splitlines() if re.match(r"^\s*(`{3,}|~{3,})", line)
    )


def test_public_issue_fixture_registry_covers_priority_issues():
    registry = _load_registry()

    assert {entry["issue"] for entry in registry} == PRIORITY_ISSUES
    assert len({entry["issue"] for entry in registry}) == len(registry)


def test_public_issue_fixture_files_are_registered_and_parseable():
    parser = MarkdownIt()

    for entry in _load_registry():
        assert entry["url"] == (
            f"https://github.com/Azure/co-op-translator/issues/{entry['issue']}"
        )
        assert entry["target_language"] == "ja"
        assert entry["source"].endswith("source.md")
        assert entry["problem"].endswith(".ja.md")
        assert entry["expected"].endswith(".ja.md")

        for key in ("source", "problem", "expected"):
            path = FIXTURE_ROOT / entry[key]
            assert path.exists(), f"{entry['issue']} missing {key}: {path}"
            content = path.read_text(encoding="utf-8")
            assert content.strip(), f"{entry['issue']} {key} is empty"
            parser.parse(content)


def test_public_issue_expected_outputs_remove_known_bad_markers():
    for entry in _load_registry():
        problem = _read_fixture(entry, "problem")
        expected = _read_fixture(entry, "expected")

        assert problem != expected
        for marker in entry["known_bad_markers"]:
            assert marker in problem, f"{entry['issue']} fixture no longer models bug"
            assert (
                marker not in expected
            ), f"{entry['issue']} expected output still contains {marker!r}"


def test_public_issue_expected_outputs_keep_markdown_fences_balanced():
    for entry in _load_registry():
        expected = _read_fixture(entry, "expected")
        assert (
            _fence_marker_count(expected) % 2 == 0
        ), f"{entry['issue']} expected output has unbalanced code fences"


def test_issue_357_source_chunking_keeps_fenced_code_atomic():
    entry = next(item for item in _load_registry() if item["issue"] == 357)
    source = _read_fixture(entry, "source")

    chunks = process_markdown(source, max_tokens=25)
    code_chunks = [chunk for chunk in chunks if 'print("train")' in chunk]

    assert "".join(chunks) == source
    assert len(code_chunks) == 1
    assert "```python" in code_chunks[0]
    assert _fence_marker_count(code_chunks[0]) == 2
