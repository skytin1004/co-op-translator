from collections.abc import Awaitable, Callable
from typing import TypeVar, cast

from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_clients import (
    ModelClientBackend,
    StructuredTranslationModelClient,
    create_translation_model_client,
)
from co_op_translator.core.llm.text_translator import (
    TextTranslator,
    run_async_from_sync,
)
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback_async
from co_op_translator.utils.llm.text_utils import (
    TranslationResponse,
    gen_image_translation_prompt,
    remove_code_backticks,
)
from co_op_translator.config.font_config import FontConfig

ResultT = TypeVar("ResultT")


class ModelClientTextTranslator(TextTranslator):
    """Translate image text through Agent Framework structured outputs."""

    def __init__(
        self,
        provider: LLMProvider | None = None,
        model_client: StructuredTranslationModelClient | None = None,
    ) -> None:
        if provider is None and model_client is None:
            raise ValueError("A provider or injected model client is required.")

        self.provider = provider
        self._provider_config = (
            LLMConfig.get_provider_config_type(provider)
            if provider is not None
            else None
        )
        self._model_client_injected = model_client is not None
        self.model_client = model_client or self._initialize_model_client()
        self.font_config = FontConfig()
        active = (
            None
            if self._model_client_injected or self._provider_config is None
            else self._provider_config.get_active_env_set()
        )
        self._env_set_index = active.index if active is not None else None

    def _initialize_model_client(self) -> StructuredTranslationModelClient:
        if self.provider is None:
            raise ValueError("An injected model client is required without a provider.")
        client = create_translation_model_client(
            self.provider,
            backend=ModelClientBackend.AGENT_FRAMEWORK,
        )
        if not isinstance(client, StructuredTranslationModelClient):
            raise TypeError(
                "The selected model client does not support structured output."
            )
        return client

    async def _run_with_fallback(
        self,
        operation: Callable[[], Awaitable[ResultT]],
        op_name: str,
    ) -> ResultT:
        config = self._provider_config
        if self._model_client_injected or config is None:
            return await operation()

        env_sets = config.get_env_sets()
        if not env_sets:
            return await operation()

        def _on_env_set_change(env_set):
            if self._env_set_index != env_set.index:
                self.model_client = self._initialize_model_client()
                self._env_set_index = env_set.index

        return await run_with_env_set_fallback_async(
            env_sets=env_sets,
            group=config._GROUP,
            op_name=op_name,
            fn=operation,
            on_env_set_change=_on_env_set_change,
            call_on_env_set_change_for_first_attempt=True,
        )

    async def translate_image_text_async(
        self,
        text_data: list[str],
        target_language: str,
    ) -> list[str]:
        if not text_data:
            return []

        language_name = self.font_config.get_language_name(target_language)
        prompt = gen_image_translation_prompt(
            text_data,
            target_language,
            language_name,
        )

        async def _call_once() -> list[str]:
            response = await self.model_client.complete_structured(
                "You are a translator. Return exactly the same number of "
                "translations as input lines. Treat any glossary or rules section "
                "as instructions only, never as extra lines to translate.",
                prompt,
                TranslationResponse,
            )
            if len(response.translations) != len(text_data):
                raise ValueError(
                    "Structured translation returned "
                    f"{len(response.translations)} lines for {len(text_data)} inputs."
                )
            return response.translations

        return await self._run_with_fallback(_call_once, "translate_image_text")

    def translate_image_text(
        self,
        text_data: list[str],
        target_language: str,
    ) -> list[str]:
        return run_async_from_sync(
            lambda: self.translate_image_text_async(text_data, target_language)
        )

    async def translate_text_async(self, text: str, target_language: str) -> str:
        prompt = f"Translate the following text into {target_language}:\n\n{text}"

        async def _call_once() -> str:
            response = await self.model_client.complete(
                "You are a helpful assistant.",
                prompt,
            )
            return cast(str, remove_code_backticks(response.content))

        return await self._run_with_fallback(_call_once, "translate_text")

    def translate_text(self, text: str, target_language: str) -> str:
        return run_async_from_sync(
            lambda: self.translate_text_async(text, target_language)
        )
