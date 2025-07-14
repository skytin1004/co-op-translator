"""
LLM configuration management module.
"""
from dataclasses import dataclass
from typing import Dict, Optional, Any
import logging

from .provider import LLMProvider
from .azure_openai import AzureOpenAIConfig
from .openai import OpenAIConfig

logger = logging.getLogger(__name__)


class LLMConfig:
    """Configuration for LLM-related services."""

    @classmethod
    def validate_env_vars(
        cls, env_vars: Dict[str, Optional[str]], provider: LLMProvider
    ):
        """
        Validate environment variables for a given provider.
        - For OpenAI, only 'OPENAI_API_KEY' is required.
        - For Azure, all listed env_vars must be non-empty.

        Additionally, distinguish between:
        - "NO_CONFIG" if no variables are set at all.
        - "Incomplete" if some are set but not all (or required ones are missing).
        """
        non_empty_count = sum(bool(v) for v in env_vars.values())

        if provider == LLMProvider.OPENAI:
            # If there's no environment variable filled at all
            if non_empty_count == 0:
                raise ValueError("NO_CONFIG_OPENAI")

            # If OPENAI_API_KEY is missing or empty, it's incomplete
            if not env_vars.get("OPENAI_API_KEY"):
                raise ValueError(
                    "Incomplete OpenAI configuration. The 'OPENAI_API_KEY' must be set."
                )

        elif provider == LLMProvider.AZURE_OPENAI:
            # If there's no environment variable filled at all
            if non_empty_count == 0:
                raise ValueError("NO_CONFIG_AZURE")

            # If some but not all are filled, it's incomplete
            if non_empty_count < len(env_vars):
                raise ValueError(
                    f"Incomplete {provider.name} configuration. Ensure all required environment variables are set."
                )

    @classmethod
    def get_service_config(cls, provider: LLMProvider) -> Dict[str, Any]:
        """
        Build env_vars for each provider, validate them, and return configuration if valid.
        """
        if provider == LLMProvider.AZURE_OPENAI:
            azure_config = AzureOpenAIConfig()
            env_vars = {
                "AZURE_OPENAI_API_KEY": azure_config.get_api_key(),
                "AZURE_OPENAI_ENDPOINT": azure_config.get_endpoint(),
                "AZURE_OPENAI_MODEL_NAME": azure_config.get_model_name(),
                "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME": azure_config.get_chat_deployment_name(),
                "AZURE_OPENAI_API_VERSION": azure_config.get_api_version(),
            }
            cls.validate_env_vars(env_vars, provider)
            return {
                "api_key": env_vars["AZURE_OPENAI_API_KEY"],
                "endpoint": env_vars["AZURE_OPENAI_ENDPOINT"],
                "model": env_vars["AZURE_OPENAI_MODEL_NAME"],
                "deployment": env_vars["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
                "api_version": env_vars["AZURE_OPENAI_API_VERSION"],
            }

        elif provider == LLMProvider.OPENAI:
            openai_config = OpenAIConfig()
            env_vars = {
                "OPENAI_API_KEY": openai_config.get_api_key(),
                "OPENAI_ORG_ID": openai_config.get_org_id(),
                "OPENAI_CHAT_MODEL_ID": openai_config.get_chat_model_id(),
            }
            cls.validate_env_vars(env_vars, provider)
            return {
                "api_key": env_vars["OPENAI_API_KEY"],
                "organization": env_vars["OPENAI_ORG_ID"],
                "model": env_vars["OPENAI_CHAT_MODEL_ID"] or "gpt-4",
            }

        else:
            raise ValueError(
                f"Unknown LLM provider: {provider}. Expected one of: {[e.name for e in LLMProvider]}"
            )

    @classmethod
    def get_available_provider(cls) -> LLMProvider:
        """
        1) Attempt Azure. If it fails:
           - If error string contains "NO_CONFIG_AZURE", ignore it (means Azure is not set at all).
           - Otherwise, raise that error (it must be an Incomplete config).
        2) Attempt OpenAI similarly.
        3) If both providers are "no config," raise "No LLM service is properly configured."
        """
        azure_error = None
        try:
            cls.get_service_config(LLMProvider.AZURE_OPENAI)
            return LLMProvider.AZURE_OPENAI
        except ValueError as e:
            if "NO_CONFIG_AZURE" in str(e):
                azure_error = None  # Means Azure is not configured at all
            else:
                azure_error = e  # Incomplete or other error

        openai_error = None
        try:
            cls.get_service_config(LLMProvider.OPENAI)
            return LLMProvider.OPENAI
        except ValueError as e:
            if "NO_CONFIG_OPENAI" in str(e):
                openai_error = None  # Means OpenAI is not configured at all
            else:
                openai_error = e

        # If azure_error and openai_error are both None => neither configured at all
        if not azure_error and not openai_error:
            raise ValueError("No LLM service is properly configured")

        # Otherwise, raise the first "incomplete" error if it exists
        if azure_error:
            raise azure_error
        if openai_error:
            raise openai_error

        # Fallback if something unexpected happened
        raise ValueError("No LLM service is properly configured")

    @classmethod
    def check_configuration(cls):
        """
        Checks if at least one LLM provider is properly configured.
        Raises ValueError if no LLM service is properly configured.
        """
        cls.get_available_provider()
        
    @classmethod
    def get_llm_config(cls) -> Dict[str, Any]:
        """
        Get the configuration for the available LLM provider.
        
        Returns:
            Configuration dictionary for the available provider
            
        Raises:
            ValueError: If no LLM service is properly configured
        """
        provider = cls.get_available_provider()
        return cls.get_service_config(provider)
        
    @classmethod
    def get_azure_config(cls) -> Dict[str, Any]:
        """
        Get Azure OpenAI configuration.
        
        Returns:
            Configuration dictionary for Azure OpenAI
            
        Raises:
            ValueError: If Azure OpenAI is not configured
        """
        return cls.get_service_config(LLMProvider.AZURE_OPENAI)
        
    @classmethod
    def get_openai_config(cls) -> Dict[str, Any]:
        """
        Get OpenAI configuration.
        
        Returns:
            Configuration dictionary for OpenAI
            
        Raises:
            ValueError: If OpenAI is not configured
        """
        return cls.get_service_config(LLMProvider.OPENAI)
