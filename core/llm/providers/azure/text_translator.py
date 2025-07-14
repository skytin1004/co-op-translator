"""
Azure OpenAI text translator implementation.
"""
import logging
import os
from typing import Any, Dict, Optional

from openai import AzureOpenAI
from ....config.llm_config.config import LLMConfig

from ...text_translator import TextTranslator

logger = logging.getLogger(__name__)


class AzureTextTranslator(TextTranslator):
    """Azure OpenAI implementation for text translation services."""

    def get_openai_client(self):
        """Create and configure an Azure OpenAI client instance.

        Returns:
            AzureOpenAI client configured with Azure credentials
        """
        # Get Azure configuration
        azure_config = LLMConfig.get_azure_config()
        
        # Create Azure OpenAI client
        client = AzureOpenAI(
            api_key=azure_config.get("api_key"),
            api_version=azure_config.get("api_version", "2023-05-15"),
            azure_endpoint=azure_config.get("endpoint")
        )
        
        return client

    def get_model_name(self) -> str:
        """Retrieve the configured Azure model deployment name.

        Returns:
            str: Model deployment name
        """
        azure_config = LLMConfig.get_azure_config()
        return azure_config.get("model", "gpt-4")

    def get_completion(self, prompt: str) -> str:
        """Get completion from Azure OpenAI.

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
            logger.error(f"Error getting completion from Azure OpenAI: {e}")
            return ""
