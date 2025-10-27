import logging
from typing import Optional

import tiktoken

from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig

logger = logging.getLogger(__name__)


def _resolve_model_name() -> Optional[str]:
    """
    Resolve a model name suitable for tiktoken based on the currently available provider.
    Falls back to cl100k_base-compatible encoding when the exact model is unknown.
    """
    try:
        provider = LLMConfig.get_available_provider()
        if provider == LLMProvider.AZURE_OPENAI:
            # Use configured base model name if available
            name = AzureOpenAIConfig.get_model_name()
            return name or None
        elif provider == LLMProvider.OPENAI:
            return OpenAIConfig.get_chat_model_id()
    except Exception:
        # Provider resolution failed; fall back to default encoding
        return None
    return None


def _get_encoding():
    model = _resolve_model_name()
    try:
        if model:
            return tiktoken.encoding_for_model(model)
    except Exception:
        # Unknown model to tiktoken; fall back to cl100k_base
        pass
    return tiktoken.get_encoding("cl100k_base")


_ENCODING = _get_encoding()


def count_tokens(text: str) -> int:
    """Return token count for the given text using a best-effort encoding."""
    if not text:
        return 0
    try:
        return len(_ENCODING.encode(text))
    except Exception as e:
        # Extremely defensive: if encoding fails for any reason, approximate by characters/4
        logger.debug(f"Tokenization failed, falling back to heuristic: {e}")
        return max(1, len(text) // 4)
