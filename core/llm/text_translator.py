"""
Base text translation interface for different LLM providers.
"""
from abc import ABC, abstractmethod
import logging
from pathlib import Path

from ..utils.llm.text_utils import (
    gen_image_translation_prompt,
    remove_code_backticks,
    extract_yaml_lines,
)
from ..config.llm_config.config import LLMConfig
from ..config.llm_config.provider import LLMProvider
from ..config.font_config import FontConfig

logger = logging.getLogger(__name__)


class TextTranslator(ABC):
    """Define interface for text translation services.

    Provides common functionality and abstract methods to be implemented by providers.
    """

    def __init__(self):
        self.client = self.get_openai_client()
        self.font_config = FontConfig()

    @abstractmethod
    def get_openai_client(self):
        """Create and configure a model client instance.

        Returns:
            Initialized AI model client for the specific provider
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Retrieve the configured model name for the provider."""
        pass

    def translate_image_text(self, text_data: list, target_language: str) -> list:
        """Translate extracted text from images to target language.

        Processes text discovered through OCR and generates translations
        formatted for placement back onto images.

        Args:
            text_data: List of text lines to translate
            target_language: Target language code

        Returns:
            List of translated text lines
        """
        if not text_data:
            return []

        # Generate the translation prompt
        prompt = gen_image_translation_prompt(text_data, target_language)

        # Get translation from the model
        completion = self.get_completion(prompt)

        # Process translation result
        response_lines = completion.strip().split("\n")
        translated_lines = []
        for line in response_lines:
            # Clean up response formatting
            line = line.strip()
            if line and not line.startswith("```") and not line.endswith("```"):
                # Handle numbered responses
                if line[0].isdigit() and len(line) > 2 and line[1] == "." and line[2] == " ":
                    line = line[3:]
                translated_lines.append(line)

        return translated_lines

    def translate_text(self, text: str, target_language: str) -> str:
        """Translate plain text to target language.

        Args:
            text: Text to translate
            target_language: Target language code

        Returns:
            Translated text
        """
        prompt = f"Translate the following text to {target_language}:\n\n{text}\n\nTranslation:"
        return self.get_completion(prompt)

    @abstractmethod
    def get_completion(self, prompt: str) -> str:
        """Get completion from the model.

        Args:
            prompt: Prompt to send to the model

        Returns:
            Model completion as text
        """
        pass

    @staticmethod
    def create():
        """Factory method to create the appropriate TextTranslator instance.

        Creates an instance of the translator for the currently configured LLM provider.

        Returns:
            TextTranslator: An instance of a concrete TextTranslator implementation
        """
        # Get configured provider
        provider = LLMConfig.get_available_provider()

        # Import appropriate implementation based on provider
        if provider == LLMProvider.AZURE_OPENAI:
            from .providers.azure.text_translator import AzureTextTranslator
            return AzureTextTranslator()
        elif provider == LLMProvider.OPENAI:
            from .providers.openai.text_translator import OpenAITextTranslator
            return OpenAITextTranslator()
        else:
            raise ValueError(f"Unsupported LLM provider: {provider}")
