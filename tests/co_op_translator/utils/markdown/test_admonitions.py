from co_op_translator.utils.markdown import (
    find_collapsed_github_admonitions,
    normalize_github_admonitions,
)


def test_normalize_github_admonitions_splits_collapsed_note_line():
    content = "> [!NOTE] Foreign keys are often abbreviated as FK\n"

    normalized = normalize_github_admonitions(content)

    assert normalized == "> [!NOTE]\n> Foreign keys are often abbreviated as FK\n"


def test_normalize_github_admonitions_preserves_crlf_line_endings():
    content = "> [!WARNING] Be careful\r\nNext paragraph\r\n"

    normalized = normalize_github_admonitions(content)

    assert normalized == "> [!WARNING]\r\n> Be careful\r\nNext paragraph\r\n"


def test_normalize_github_admonitions_keeps_valid_block_unchanged():
    content = "> [!TIP]\n> Keep the content on the next blockquote line.\n"

    normalized = normalize_github_admonitions(content)

    assert normalized == content


def test_normalize_github_admonitions_skips_fenced_code_blocks():
    content = "```md\n> [!NOTE] Example stays literal\n```\n"

    normalized = normalize_github_admonitions(content)

    assert normalized == content


def test_find_collapsed_github_admonitions_reports_line_numbers():
    content = "# Heading\n\n> [!IMPORTANT] Review this\n"

    collapsed = find_collapsed_github_admonitions(content)

    assert len(collapsed) == 1
    assert collapsed[0].line_number == 3
    assert collapsed[0].marker == "[!IMPORTANT]"
    assert collapsed[0].trailing_text == "Review this"
