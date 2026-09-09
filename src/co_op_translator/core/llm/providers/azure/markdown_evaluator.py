from pathlib import Path

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.core.llm.model_client_evaluator import (
    ModelClientMarkdownEvaluator,
)
from co_op_translator.core.llm.model_clients import TranslationModelClient


class AzureMarkdownEvaluator(ModelClientMarkdownEvaluator):
    """Backward-compatible Azure OpenAI evaluator."""

    def __init__(
        self,
        root_dir: Path | None = None,
        use_llm: bool = True,
        use_rule: bool = True,
        model_client: TranslationModelClient | None = None,
    ):
        super().__init__(
            provider=LLMProvider.AZURE_OPENAI,
            root_dir=root_dir,
            use_llm=use_llm,
            use_rule=use_rule,
            model_client=model_client,
        )
