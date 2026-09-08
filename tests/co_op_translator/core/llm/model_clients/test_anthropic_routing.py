"""Exercise provider routing through the actual framework with controlled responses."""

import json
import os
from unittest.mock import AsyncMock, patch

import pytest
from agent_framework import ChatResponse, Message

from co_op_translator.core.llm.markdown_translator import (
    MarkdownTranslator,
    TranslationIncompleteError,
)
from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator
from co_op_translator.core.llm.jupyter_notebook_translator import (
    JupyterNotebookTranslator,
)
from co_op_translator.core.llm.model_clients import (
    create_translation_model_client,
    ModelClientBackend,
)
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


@pytest.fixture(autouse=True)
def anthropic_environment():
    with patch.dict(
        os.environ,
        {
            "CO_OP_TRANSLATOR_PROVIDER": "anthropic",
            "ANTHROPIC_API_KEY": "test-key",
            "ANTHROPIC_CHAT_MODEL_ID": "claude-test",
        },
        clear=True,
    ):
        yield


@pytest.fixture
def connector():
    # The connector is real; only its network-facing response method is mocked.
    from agent_framework_anthropic import AnthropicClient

    client = AnthropicClient(api_key="test-key", model="claude-test")

    async def response(messages, *, options=None):
        return ChatResponse(
            messages=Message("assistant", [messages[-1].text.replace("Hello", "안녕")]),
            finish_reason="stop",
        )

    client.get_response = AsyncMock(side_effect=response)
    with (
        patch("agent_framework_anthropic.AnthropicClient", return_value=client),
        patch(
            "co_op_translator.core.llm.providers.openai.markdown_translator.asyncio.sleep",
            new=AsyncMock(),
        ),
    ):
        yield client


@pytest.mark.asyncio
async def test_markdown_preserves_links_and_code(connector, tmp_path):
    source = (
        "# Hello\n\n[Hello](https://example.com/a?q=1)\n\n"
        "```python\nprint(42)\n```\n"
    )
    translator = MarkdownTranslator.create(root_dir=tmp_path)
    result = await translator.translate_markdown(source, "ko")
    assert "안녕" in result
    assert "https://example.com/a?q=1" in result
    assert "```python\nprint(42)\n```" in result
    assert "@@LINE_" not in result
    assert connector.get_response.await_args.kwargs["options"]["max_tokens"] == 8192


@pytest.mark.asyncio
async def test_notebook_preserves_code_cells(connector):
    code_cell = {
        "cell_type": "code",
        "source": ["print(42)"],
        "metadata": {},
        "outputs": [],
        "execution_count": None,
    }
    notebook = {
        "cells": [
            {"cell_type": "markdown", "source": ["# Hello"], "metadata": {}},
            code_cell,
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    translator = JupyterNotebookTranslator.create()
    result = json.loads(await translator.translate_notebook(notebook, "ko"))
    assert result["cells"][1] == code_cell
    assert "안녕" in "".join(result["cells"][0]["source"])


@pytest.mark.asyncio
async def test_evaluation_uses_anthropic(connector):
    evaluator = MarkdownEvaluator.create()
    assert await evaluator._run_prompt("Hello", 1, 1) == "안녕"
    connector.get_response.assert_awaited_once()


@pytest.mark.asyncio
async def test_truncation_is_not_accepted(connector):
    connector.get_response.side_effect = None
    connector.get_response.return_value = ChatResponse(
        messages=Message("assistant", ["partial"]), finish_reason="length"
    )
    with pytest.raises(TranslationIncompleteError):
        await MarkdownTranslator.create()._run_prompt_once(
            f"rules{SPLIT_DELIMITER}Hello", 1, 1
        )


def test_sk_backend_cannot_be_requested_for_anthropic():
    with pytest.raises(ValueError, match="requires"):
        create_translation_model_client(
            LLMProvider.ANTHROPIC, backend=ModelClientBackend.SEMANTIC_KERNEL
        )


def test_text_only_project_never_initializes_image_text_client(connector, tmp_path):
    with patch(
        "co_op_translator.core.llm.text_translator.TextTranslator.create",
        side_effect=AssertionError("OpenAI image-text client must not be constructed"),
    ):
        project = ProjectTranslator(
            "ko", root_dir=tmp_path, translation_types=["markdown", "notebook"]
        )
        first = project.markdown_translator
        project._initialize_translators()
        assert project.markdown_translator is first
        assert project.text_translator is None
        assert project.notebook_translator is not None


def test_cli_rejects_images_before_connectivity(tmp_path):
    from click.testing import CliRunner
    from co_op_translator.cli.translate import translate_command

    with patch(
        "co_op_translator.config.llm_config.config.LLMConfig.validate_connectivity",
        side_effect=AssertionError("No network request expected"),
    ):
        result = CliRunner().invoke(
            translate_command, ["-l", "ko", "-img", "-r", str(tmp_path), "-y"]
        )
    assert result.exit_code != 0
    assert "Anthropic currently supports" in result.output


def test_missing_connector_has_actionable_error():
    with patch.dict("sys.modules", {"agent_framework_anthropic": None}):
        with pytest.raises(ValueError, match=r"co-op-translator\[anthropic\]"):
            create_translation_model_client(LLMProvider.ANTHROPIC)
