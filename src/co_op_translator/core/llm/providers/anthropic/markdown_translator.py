import asyncio
import logging
import time
from pathlib import Path

from co_op_translator.config.llm_config.anthropic import AnthropicConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.llm.model_clients import (
    TranslationModelClient,
    create_translation_model_client,
)
from co_op_translator.utils.common.env_set_utils import run_with_env_set_fallback_async
from co_op_translator.utils.markdown.constants import SPLIT_DELIMITER

logger = logging.getLogger(__name__)


class AnthropicMarkdownTranslator(MarkdownTranslator):
    """Claude implementation for Markdown translation."""

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
        model_client: TranslationModelClient | None = None,
    ):
        super().__init__(
            root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )
        self._model_client_injected = model_client is not None
        self.model_client = model_client or self._initialize_model_client()
        active = (
            None
            if self._model_client_injected
            else AnthropicConfig.get_active_env_set()
        )
        self._env_set_index = active.index if active is not None else None

    def _initialize_model_client(self) -> TranslationModelClient:
        return create_translation_model_client(LLMProvider.ANTHROPIC)

    async def _run_prompt_once(self, prompt: str, index: int | str, total: int) -> str:
        if isinstance(index, str):
            logger.info("Running system prompt: %s", index)
        else:
            logger.info("Running translation prompt %s/%s", index, total)

        parts = prompt.split(SPLIT_DELIMITER, 1)
        if len(parts) != 2:
            raise ValueError(
                "Prompt did not contain expected system/user split "
                "(missing SPLIT_DELIMITER)."
            )
        system_text, user_text = parts[0].strip(), parts[1]

        start_time = time.time()
        response = await self.model_client.complete(system_text, user_text)
        self._raise_for_finish_reason(response.finish_reason, index, total)
        logger.info(
            "Prompt %s/%s completed in %s seconds",
            index,
            total,
            time.time() - start_time,
        )
        await asyncio.sleep(1)
        return response.content

    async def _run_prompt(self, prompt: str, index: int | str, total: int) -> str:
        env_sets = [] if self._model_client_injected else AnthropicConfig.get_env_sets()
        if not env_sets:
            return await self._run_prompt_once(prompt, index, total)

        async def _call_once():
            return await self._run_prompt_once(prompt, index, total)

        def _on_env_set_change(env_set):
            if self._env_set_index != env_set.index:
                self.model_client = self._initialize_model_client()
                self._env_set_index = env_set.index

        return await run_with_env_set_fallback_async(
            env_sets=env_sets,
            group=AnthropicConfig._GROUP,
            op_name=f"Anthropic prompt {index}/{total}",
            fn=_call_once,
            on_env_set_change=_on_env_set_change,
            call_on_env_set_change_for_first_attempt=True,
        )
