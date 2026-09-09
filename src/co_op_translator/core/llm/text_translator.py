import asyncio
from collections.abc import Awaitable, Callable
from typing import TypeVar

from co_op_translator.config.llm_config.config import LLMConfig


class TextTranslator:
    """Translate short text used by the image rendering pipeline."""

    def translate_image_text(self, text_data: list, target_language: str) -> list:
        """Translate extracted image lines while preserving their count."""
        raise NotImplementedError

    async def translate_image_text_async(
        self,
        text_data: list,
        target_language: str,
    ) -> list:
        """Run a synchronous text translator without blocking the event loop."""
        return await asyncio.to_thread(
            self.translate_image_text,
            text_data,
            target_language,
        )

    def translate_text(self, text: str, target_language: str) -> str:
        """Translate plain text to the target language."""
        raise NotImplementedError

    @classmethod
    def create(cls) -> "TextTranslator":
        """Create the common structured-output translator for the provider."""
        from co_op_translator.core.llm.model_client_text_translator import (
            ModelClientTextTranslator,
        )

        provider = LLMConfig.get_available_provider()
        return ModelClientTextTranslator(provider=provider)


ResultT = TypeVar("ResultT")


def run_async_from_sync(factory: Callable[[], Awaitable[ResultT]]) -> ResultT:
    """Run an async model call from the public synchronous image API."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(factory())
    raise RuntimeError(
        "Synchronous image translation cannot run inside an active event loop. "
        "Use translate_image_text_async instead."
    )
