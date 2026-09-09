import asyncio
import logging
import time
from pathlib import Path

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_evaluator import MarkdownEvaluator
from co_op_translator.core.llm.model_clients import (
    TranslationModelClient,
    create_translation_model_client,
)

logger = logging.getLogger(__name__)


class ModelClientMarkdownEvaluator(MarkdownEvaluator):
    """Evaluate Markdown through the framework-neutral model client boundary."""

    def __init__(
        self,
        provider: LLMProvider | None = None,
        root_dir: Path | None = None,
        use_llm: bool = True,
        use_rule: bool = True,
        model_client: TranslationModelClient | None = None,
    ):
        super().__init__(root_dir, use_llm, use_rule)
        if provider is None and model_client is None:
            raise ValueError("A provider or injected model client is required.")
        self.provider = provider
        self.model_client = model_client or self._initialize_model_client()

    def _initialize_model_client(self) -> TranslationModelClient:
        if self.provider is None:
            raise ValueError("An injected model client is required without a provider.")
        return create_translation_model_client(self.provider)

    async def _run_prompt(self, prompt: str, index: int, total: int) -> str:
        try:
            logger.info("Running evaluation prompt %s/%s", index, total)
            start_time = time.time()
            response = await self.model_client.complete("", prompt)
            logger.info(
                "Prompt %s/%s completed in %s seconds",
                index,
                total,
                time.time() - start_time,
            )
            await asyncio.sleep(1)
            return response.content
        except Exception as e:
            logger.error("Error in prompt %s/%s - %s: %s", index, total, prompt, e)
            return ""
