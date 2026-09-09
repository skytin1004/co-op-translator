from pathlib import Path

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_client_translator import (
    ModelClientMarkdownTranslator,
)
from co_op_translator.core.llm.model_clients import TranslationModelClient


class OpenAIMarkdownTranslator(ModelClientMarkdownTranslator):
    """Backward-compatible OpenAI translator."""

    def __init__(
        self,
        root_dir: Path | None = None,
        translations_dir: Path | None = None,
        image_dir: Path | None = None,
        lang_subdir: Path | None = None,
        model_client: TranslationModelClient | None = None,
    ):
        super().__init__(
            provider=LLMProvider.OPENAI,
            root_dir=root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
            model_client=model_client,
        )
