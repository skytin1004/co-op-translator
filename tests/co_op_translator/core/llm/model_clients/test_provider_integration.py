from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.llm.model_clients import ModelResponse
from co_op_translator.core.llm.model_client_evaluator import (
    ModelClientMarkdownEvaluator,
)
from co_op_translator.core.llm.model_client_translator import (
    ModelClientMarkdownTranslator,
)
from co_op_translator.core.llm.providers.azure.markdown_evaluator import (
    AzureMarkdownEvaluator,
)
from co_op_translator.core.llm.providers.azure.markdown_translator import (
    AzureMarkdownTranslator,
)
from co_op_translator.core.llm.providers.openai.markdown_evaluator import (
    OpenAIMarkdownEvaluator,
)
from co_op_translator.core.llm.providers.openai.markdown_translator import (
    OpenAIMarkdownTranslator,
)
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER


class RecordingModelClient:
    def __init__(self, response: ModelResponse) -> None:
        self.response = response
        self.calls = []

    async def complete(
        self,
        system_prompt,
        user_content,
        *,
        temperature=None,
    ):
        self.calls.append((system_prompt, user_content, temperature))
        return self.response


@pytest.mark.parametrize("provider", list(LLMProvider))
def test_markdown_factory_uses_common_model_client_translator(tmp_path, provider):
    client = RecordingModelClient(ModelResponse("translated", "stop"))
    with (
        patch(
            "co_op_translator.core.llm.markdown_translator.LLMConfig.get_available_provider",
            return_value=provider,
        ),
        patch(
            "co_op_translator.core.llm.model_client_translator.create_translation_model_client",
            return_value=client,
        ),
    ):
        translator = MarkdownTranslator.create(root_dir=tmp_path)

    assert type(translator) is ModelClientMarkdownTranslator
    assert translator.provider == provider


@pytest.mark.parametrize("provider", list(LLMProvider))
def test_evaluator_factory_uses_common_model_client_evaluator(tmp_path, provider):
    client = RecordingModelClient(ModelResponse('{"score": 1}', "stop"))
    with (
        patch(
            "co_op_translator.core.llm.markdown_evaluator.LLMConfig.get_available_provider",
            return_value=provider,
        ),
        patch(
            "co_op_translator.core.llm.model_client_evaluator.create_translation_model_client",
            return_value=client,
        ),
    ):
        evaluator = MarkdownEvaluator.create(root_dir=tmp_path)

    assert type(evaluator) is ModelClientMarkdownEvaluator
    assert evaluator.provider == provider


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("translator_type", "sleep_target"),
    [
        (
            AzureMarkdownTranslator,
            "co_op_translator.core.llm.model_client_translator.asyncio.sleep",
        ),
        (
            OpenAIMarkdownTranslator,
            "co_op_translator.core.llm.model_client_translator.asyncio.sleep",
        ),
        (
            ModelClientMarkdownTranslator,
            "co_op_translator.core.llm.model_client_translator.asyncio.sleep",
        ),
    ],
)
async def test_provider_translators_use_framework_neutral_client(
    tmp_path,
    translator_type,
    sleep_target,
):
    client = RecordingModelClient(ModelResponse("translated", "stop"))
    translator = translator_type(root_dir=tmp_path, model_client=client)

    with patch(sleep_target, new=AsyncMock()):
        result = await translator._run_prompt_once(
            f"system rules{SPLIT_DELIMITER}source content",
            1,
            1,
        )

    assert result == "translated"
    assert client.calls == [("system rules", "source content", None)]


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("evaluator_type", "sleep_target"),
    [
        (
            AzureMarkdownEvaluator,
            "co_op_translator.core.llm.model_client_evaluator.asyncio.sleep",
        ),
        (
            OpenAIMarkdownEvaluator,
            "co_op_translator.core.llm.model_client_evaluator.asyncio.sleep",
        ),
        (
            ModelClientMarkdownEvaluator,
            "co_op_translator.core.llm.model_client_evaluator.asyncio.sleep",
        ),
    ],
)
async def test_provider_evaluators_use_framework_neutral_client(
    tmp_path,
    evaluator_type,
    sleep_target,
):
    client = RecordingModelClient(ModelResponse('{"score": 1}', "stop"))
    evaluator = evaluator_type(root_dir=tmp_path, model_client=client)

    with patch(sleep_target, new=AsyncMock()):
        result = await evaluator._run_prompt("evaluation prompt", 1, 1)

    assert result == '{"score": 1}'
    assert client.calls == [("", "evaluation prompt", None)]


@pytest.mark.asyncio
async def test_injected_model_client_bypasses_provider_credential_fallback(tmp_path):
    client = RecordingModelClient(ModelResponse("translated", "stop"))
    translator = OpenAIMarkdownTranslator(root_dir=tmp_path, model_client=client)

    with (
        patch(
            "co_op_translator.config.llm_config.openai.OpenAIConfig.get_env_sets",
            side_effect=AssertionError("provider fallback should not be queried"),
        ),
        patch(
            "co_op_translator.core.llm.model_client_translator.asyncio.sleep",
            new=AsyncMock(),
        ),
    ):
        result = await translator._run_prompt(
            f"system rules{SPLIT_DELIMITER}source content",
            1,
            1,
        )

    assert result == "translated"
