import pytest
from unittest.mock import AsyncMock, patch
import re

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator

# A sample markdown with a code block and a link for testing.
TEST_MD_CONTENT = """
# Sample Markdown

```python
print("Hello, world!")
```"""


class ConcreteMarkdownTranslator(MarkdownTranslator):
    """A concrete implementation of MarkdownTranslator for testing."""

    async def _run_prompt(self, prompt, index, total):
        # This implementation should be replaced by the mock in tests
        return f"[Default Translation] {prompt}"


@pytest.fixture
def real_markdown_translator(tmp_path):
    """Creates a concrete instance of MarkdownTranslator for testing."""
    return ConcreteMarkdownTranslator(root_dir=tmp_path)


@pytest.mark.asyncio
async def test_translate_markdown_partial_mock(real_markdown_translator, tmp_path):
    """Test the translation logic using the real code for:
    - replace_code_blocks
    - restore_code_blocks
    - update_links
    but mock _run_prompt to avoid calling a real external translator.

    This ensures we verify the actual internal workflow,
    while controlling the translation 'results' in _run_prompt.
    """
    # Create test file
    test_file = tmp_path / "example.md"
    test_file.write_text(TEST_MD_CONTENT)

    async def fake_prompt(prompt, index, total):
        # Return a translation that preserves markdown structure and placeholders
        # This simulates what a real translator would do with the prompt template
        if "Sample Markdown" in prompt:
            # Keep any code block placeholders in the translation
            placeholder_match = re.search(r"@@CODE_BLOCK_\d+@@", prompt)
            code_placeholder = placeholder_match.group(0) if placeholder_match else ""
            return f"# Ejemplo de Markdown\n\n{code_placeholder}"
        elif "Disclaimer" in prompt.lower():
            return "Aviso Legal: Este es un documento traducido."
        return prompt  # Return the original prompt for any other content

    # Apply the mock directly to the instance
    with patch.object(
        real_markdown_translator, "_run_prompt", new_callable=AsyncMock
    ) as mock_run_prompt:
        mock_run_prompt.side_effect = fake_prompt

        # Execute the markdown translation
        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_CONTENT, language_code="es", md_file_path=test_file
        )

        # Verify that the code block content is still present in the final output
        assert (
            'print("Hello, world!")' in result
        ), "Expected the code block to remain after the placeholder/restore cycle."

        # Verify that our translation appears (in Spanish)
        assert (
            "Ejemplo de Markdown" in result
        ), "The mocked _run_prompt response should appear in the final output."

        # Verify that _run_prompt was called at least once
        assert (
            mock_run_prompt.call_count > 0
        ), "Expected at least one call to _run_prompt for the translation process."


@pytest.mark.asyncio
async def test_translate_markdown_full_integration(real_markdown_translator, tmp_path):
    """A full integration test that avoids mocking _run_prompt at all.
    This only works if the abstract _run_prompt has a default implementation
    or if real_markdown_translator is a fully realized subclass."""
    # Create test file
    test_file = tmp_path / "example_full.md"
    test_file.write_text(TEST_MD_CONTENT)

    try:
        result = await real_markdown_translator.translate_markdown(
            document=TEST_MD_CONTENT, language_code="es", md_file_path=test_file
        )
    except NotImplementedError:
        pytest.skip(
            "Skipping because _run_prompt is not implemented in the base class."
        )

    assert (
        'print("Hello, world!")' in result
    ), "Even in a full integration scenario, the code block should remain."
    assert (
        "[Default Translation]" in result
    ), "Expected the default translation text in the output."


def test_insert_metadata_comment_after_frontmatter(tmp_path):
    translator = ConcreteMarkdownTranslator(root_dir=tmp_path)

    content_with_frontmatter = """---
layout: ../layouts/DocsLayout.astro
title: Localizeflow  Quick Start Guide
---

# Heading
Body
"""

    metadata = {
        "original_hash": "hash",
        "translation_date": "2025-10-15T03:44:55+00:00",
        "source_file": "README.md",
        "language_code": "sw",
    }
    metadata_comment = translator.format_metadata_comment(metadata)

    result = translator._insert_metadata_comment(
        content_with_frontmatter, metadata_comment
    )

    lines = result.splitlines()

    assert lines[0] == "---"
    assert lines[1].startswith("layout:")
    assert lines[2].startswith("title:")
    assert lines[3] == "---"

    # There should be a blank line after frontmatter, then the metadata comment
    assert lines[4] == ""
    assert lines[5] == "<!--"

    # CO_OP_TRANSLATOR_METADATA label should appear inside the comment block
    assert any("CO_OP_TRANSLATOR_METADATA:" in line for line in lines)


def test_update_astro_layout_path_relative(tmp_path):
    """layout: path should be rewritten relative to translations/<lang>/..."""

    # Simulate project structure: root/docs/README.md
    root_dir = tmp_path
    docs_dir = root_dir / "docs"
    docs_dir.mkdir()
    md_file = docs_dir / "README.md"

    # Content with Astro-style frontmatter
    content = """---
layout: ../layouts/DocsLayout.astro
title: Localizeflow – Quick Start Guide
---

# Heading
Body
"""

    translator = ConcreteMarkdownTranslator(root_dir=root_dir)
    # Simulate default translations_dir under root
    translator.translations_dir = None

    result = translator._update_astro_layout_path(content, md_file, "ko")

    # For root/docs/README.md, translated markdown lives at
    # root/translations/ko/docs/README.md, so layout should become
    # ../../../layouts/DocsLayout.astro relative to that.
    assert "layout: ../../../layouts/DocsLayout.astro" in result


def test_update_astro_layout_path_no_frontmatter(tmp_path):
    """Files without YAML frontmatter should remain unchanged."""

    root_dir = tmp_path
    md_file = root_dir / "README.md"
    content = "# No frontmatter\nBody"

    translator = ConcreteMarkdownTranslator(root_dir=root_dir)

    result = translator._update_astro_layout_path(content, md_file, "ko")

    assert result == content


def test_update_astro_layout_path_no_layout_key(tmp_path):
    """Frontmatter without layout key should be unchanged."""

    root_dir = tmp_path
    md_file = root_dir / "README.md"
    content = """---
title: Only Title
---

# Heading
"""

    translator = ConcreteMarkdownTranslator(root_dir=root_dir)

    result = translator._update_astro_layout_path(content, md_file, "ko")

    assert result == content
