import os

from co_op_translator.utils.common.env_set_utils import get_active_env_set, get_env_sets


class AzureAIVisionConfig:
    """Azure AI Service specific configuration."""

    _GROUP = "azure_ai_service"
    _REQUIRED = (
        "AZURE_AI_SERVICE_API_KEY",
        "AZURE_AI_SERVICE_ENDPOINT",
    )

    @staticmethod
    def get_env_sets():
        return get_env_sets(
            group=AzureAIVisionConfig._GROUP, required=AzureAIVisionConfig._REQUIRED
        )

    @staticmethod
    def get_active_env_set():
        return get_active_env_set(
            group=AzureAIVisionConfig._GROUP,
            required=AzureAIVisionConfig._REQUIRED,
        )

    @staticmethod
    def get_api_key():
        """Retrieve the Azure AI Service API key from environment variables.

        First checks for AZURE_AI_SERVICE_API_KEY (recommended), then checks numbered
        variants like AZURE_AI_SERVICE_API_KEY_1.
        """
        env_set = AzureAIVisionConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_AI_SERVICE_API_KEY")

    @staticmethod
    def get_endpoint():
        """Retrieve the Azure AI service endpoint from environment variables."""
        env_set = AzureAIVisionConfig.get_active_env_set()
        if env_set is None:
            return None
        return env_set.values.get("AZURE_AI_SERVICE_ENDPOINT")

    @staticmethod
    def get_ocr_language():
        """Return an optional OCR source-language hint for Azure AI Vision READ.

        Azure Image Analysis defaults the READ language to English when no language
        hint is supplied. Projects whose source images contain Korean, Japanese, or
        other non-English text can set this to a two-letter language code such as
        "ko" to improve OCR accuracy before translation.
        """
        language = os.getenv("AZURE_AI_SERVICE_OCR_LANGUAGE")
        if not language:
            return None
        language = language.strip()
        return language or None
