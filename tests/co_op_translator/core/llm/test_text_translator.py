from unittest.mock import MagicMock, patch

import pytest

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_client_text_translator import (
    ModelClientTextTranslator,
)
from co_op_translator.core.llm.model_clients import ModelClientBackend, ModelResponse
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.utils.llm.text_utils import TranslationResponse


class RecordingStructuredModelClient:
    def __init__(self) -> None:
        self.calls = []

    async def complete(
        self,
        system_prompt,
        user_content,
        *,
        temperature=None,
    ):
        self.calls.append(("text", system_prompt, user_content, temperature))
        return ModelResponse("```\nTranslated Text\n```", "stop")

    async def complete_structured(
        self,
        system_prompt,
        user_content,
        response_format,
        *,
        temperature=None,
    ):
        self.calls.append(
            (
                "structured",
                system_prompt,
                user_content,
                response_format,
                temperature,
            )
        )
        return TranslationResponse(
            translations=["Translated line 1", "Translated line 2"]
        )


@pytest.fixture
def text_translator():
    translator = ModelClientTextTranslator(
        model_client=RecordingStructuredModelClient()
    )
    translator.font_config = MagicMock()
    translator.font_config.get_language_name.return_value = "Korean"
    return translator


def test_translate_text(text_translator):
    result = text_translator.translate_text("Text to translate", "es")

    assert result == "Translated Text"


def test_translate_image_text(text_translator):
    result = text_translator.translate_image_text(["Line 1", "Line 2"], "ko")

    assert result == ["Translated line 1", "Translated line 2"]
    assert len(result) == 2
    call = text_translator.model_client.calls[-1]
    assert call[0] == "structured"
    assert call[3] is TranslationResponse


@pytest.mark.asyncio
async def test_translate_image_text_async(text_translator):
    result = await text_translator.translate_image_text_async(
        ["Line 1", "Line 2"],
        "ko",
    )

    assert result == ["Translated line 1", "Translated line 2"]


def test_translate_image_text_empty(text_translator):
    assert text_translator.translate_image_text([], "ko") == []


@pytest.mark.parametrize("provider", list(LLMProvider))
def test_text_translator_factory_uses_common_agent_framework_path(provider):
    client = RecordingStructuredModelClient()
    with (
        patch(
            "co_op_translator.core.llm.text_translator.LLMConfig.get_available_provider",
            return_value=provider,
        ),
        patch(
            "co_op_translator.core.llm.model_client_text_translator.create_translation_model_client",
            return_value=client,
        ) as create_client,
    ):
        translator = TextTranslator.create()

    assert isinstance(translator, ModelClientTextTranslator)
    assert translator.provider == provider
    create_client.assert_called_once_with(
        provider,
        backend=ModelClientBackend.AGENT_FRAMEWORK,
    )
