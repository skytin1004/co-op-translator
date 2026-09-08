"""Configuration for the optional Anthropic text translation provider."""

import os


class AnthropicConfig:
    @staticmethod
    def get_api_key() -> str:
        return os.getenv("ANTHROPIC_API_KEY", "").strip()

    @staticmethod
    def get_chat_model_id() -> str:
        return os.getenv("ANTHROPIC_CHAT_MODEL_ID", "").strip()

    @staticmethod
    def get_max_tokens() -> int:
        try:
            value = int(os.getenv("ANTHROPIC_MAX_TOKENS", "8192"))
        except ValueError:
            raise ValueError("ANTHROPIC_MAX_TOKENS must be a positive integer.") from None
        if value <= 0:
            raise ValueError("ANTHROPIC_MAX_TOKENS must be a positive integer.")
        return value

    @staticmethod
    def validate_backend() -> None:
        backend = os.getenv("CO_OP_TRANSLATOR_MODEL_CLIENT", "agent-framework")
        if backend.strip().lower().replace("_", "-") != "agent-framework":
            raise ValueError(
                "Anthropic requires Agent Framework. Set "
                "CO_OP_TRANSLATOR_MODEL_CLIENT=agent-framework or unset it."
            )


ANTHROPIC_INSTALL_MESSAGE = (
    "Anthropic support is not installed. "
    "Install it with: pip install 'co-op-translator[anthropic]'"
)
