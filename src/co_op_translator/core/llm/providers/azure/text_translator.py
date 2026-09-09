from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_client_text_translator import (
    ModelClientTextTranslator,
)
from co_op_translator.core.llm.model_clients import StructuredTranslationModelClient


class AzureTextTranslator(ModelClientTextTranslator):
    """Backward-compatible Azure OpenAI image-text translator."""

    def __init__(
        self,
        model_client: StructuredTranslationModelClient | None = None,
    ) -> None:
        super().__init__(
            provider=LLMProvider.AZURE_OPENAI,
            model_client=model_client,
        )
