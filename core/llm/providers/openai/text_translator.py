"""
OpenAI text translator implementation.
"""
import logging
from typing import Any, Dict, Optional

from openai import OpenAI
from ....config.llm_config.config import LLMConfig

from ...text_translator import TextTranslator

logger = logging.getLogger(__name__)


class OpenAITextTranslator(TextTranslator):
    """OpenAI implementation for text translation services."""

    def get_openai_client(self):
        """Create and configure an OpenAI client instance.

        Returns:
            OpenAI client configured with appropriate credentials
        """
        # Get OpenAI configuration
        openai_config = LLMConfig.get_openai_config()
        
        # Create OpenAI client
        client = OpenAI(
            api_key=openai_config.get("api_key")
        )
        
        return client

    def get_model_name(self) -> str:
        """Retrieve the configured OpenAI model name.

        Returns:
            str: Model name
        """
        openai_config = LLMConfig.get_openai_config()
        return openai_config.get("model", "gpt-4")

    def get_completion(self, prompt: str) -> str:
        """Get completion from OpenAI.

        Args:
            prompt: Prompt to send to the model

        Returns:
            Model completion as text
        """
        try:
            completion = self.client.chat.completions.create(
                model=self.get_model_name(),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=2000,
            )
            
            # Extract content from the response
            if completion.choices and completion.choices[0].message:
                return completion.choices[0].message.content
            else:
                logger.error("No content in completion response")
                return ""
        except Exception as e:
            logger.error(f"Error getting completion from OpenAI: {e}")
            return ""
