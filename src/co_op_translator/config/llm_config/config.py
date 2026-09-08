from dataclasses import dataclass
from typing import Dict, Optional
import logging
import os

from ai_healthcheck import check_openai
from az_ai_healthcheck import check_azure_openai

from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.llm_config.azure_openai import AzureOpenAIConfig
from co_op_translator.config.llm_config.openai import OpenAIConfig
from co_op_translator.config.llm_config.anthropic import (
    AnthropicConfig,
    ANTHROPIC_INSTALL_MESSAGE,
)
from co_op_translator.utils.common.env_set_utils import (
    any_env_var_present,
    set_preferred_env_set,
)

logger = logging.getLogger(__name__)


@dataclass
class LLMServiceConfig:
    """Configuration for a specific LLM service."""

    required: bool
    env_vars: Dict[str, Optional[str]]


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
        if provider == LLMProvider.OPENAI:
            bases = [
                "OPENAI_API_KEY",
                "OPENAI_CHAT_MODEL_ID",
                "OPENAI_ORG_ID",
                "OPENAI_BASE_URL",
            ]
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_OPENAI")

            if not env_vars.get("OPENAI_API_KEY"):
                raise ValueError(
                    "Incomplete OpenAI configuration. The 'OPENAI_API_KEY' must be set."
                )

            if not env_vars.get("OPENAI_CHAT_MODEL_ID"):
                raise ValueError(
                    "Incomplete OpenAI configuration. The 'OPENAI_CHAT_MODEL_ID' must be set."
                )

        elif provider == LLMProvider.AZURE_OPENAI:
            bases = list(env_vars.keys())
            if not any_env_var_present(bases):
                raise ValueError("NO_CONFIG_AZURE")

            if any(v is None or not str(v).strip() for v in env_vars.values()):
                raise ValueError(
                    f"Incomplete {provider.name} configuration. Ensure all required environment variables are set."
                )

    @classmethod
    def get_service_config(cls, provider: LLMProvider) -> LLMServiceConfig:
        """
        Build env_vars for each provider, validate them, and return LLMServiceConfig if valid.
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
            return LLMServiceConfig(required=True, env_vars=env_vars)

        elif provider == LLMProvider.OPENAI:
            openai_config = OpenAIConfig()
            env_vars = {
                "OPENAI_API_KEY": openai_config.get_api_key(),
                "OPENAI_ORG_ID": openai_config.get_org_id(),
                "OPENAI_CHAT_MODEL_ID": openai_config.get_chat_model_id(),
            }
            cls.validate_env_vars(env_vars, provider)
            return LLMServiceConfig(required=False, env_vars=env_vars)

        elif provider == LLMProvider.ANTHROPIC:
            env_vars = {
                "ANTHROPIC_API_KEY": AnthropicConfig.get_api_key(),
                "ANTHROPIC_CHAT_MODEL_ID": AnthropicConfig.get_chat_model_id(),
            }
            if not any(env_vars.values()) and not os.getenv("ANTHROPIC_MAX_TOKENS"):
                raise ValueError("NO_CONFIG_ANTHROPIC")
            missing = [name for name, value in env_vars.items() if not value]
            if missing:
                raise ValueError(
                    "Incomplete Anthropic configuration. Set " + ", ".join(missing) + "."
                )
            AnthropicConfig.get_max_tokens()
            AnthropicConfig.validate_backend()
            return LLMServiceConfig(required=False, env_vars=env_vars)

        else:
            raise ValueError(
                f"Unknown LLM provider: {provider}. Expected one of: {[e.name for e in LLMProvider]}"
            )

    @classmethod
    def get_available_provider(cls) -> LLMProvider:
        """Select an explicit provider, or preserve Azure/OpenAI auto-detection priority."""
        selected = os.getenv("CO_OP_TRANSLATOR_PROVIDER", "").strip().lower()
        if selected:
            try:
                provider = LLMProvider(selected)
            except ValueError:
                raise ValueError(
                    "Invalid CO_OP_TRANSLATOR_PROVIDER. Expected azure_openai, openai, or anthropic."
                ) from None
            try:
                cls.get_service_config(provider)
            except ValueError as exc:
                if str(exc).startswith("NO_CONFIG_"):
                    required = {
                        LLMProvider.AZURE_OPENAI: "AZURE_OPENAI_* variables",
                        LLMProvider.OPENAI: "OPENAI_API_KEY and OPENAI_CHAT_MODEL_ID",
                        LLMProvider.ANTHROPIC: "ANTHROPIC_API_KEY and ANTHROPIC_CHAT_MODEL_ID",
                    }[provider]
                    raise ValueError(
                        f"Selected provider {selected} is not configured. Set {required}."
                    ) from None
                raise
            return provider

        errors = []
        for provider in LLMProvider:
            try:
                cls.get_service_config(provider)
                return provider
            except ValueError as exc:
                if not str(exc).startswith("NO_CONFIG_"):
                    errors.append(exc)
        if errors:
            raise errors[0]
        raise ValueError("No LLM service is properly configured")

    @classmethod
    def validate_image_support(cls) -> None:
        """Reject unsupported image translation before any provider calls."""
        if cls.get_available_provider() == LLMProvider.ANTHROPIC:
            raise ValueError(
                "Anthropic currently supports Markdown, notebooks, and LLM evaluation only. "
                "Use -md and/or -nb (API: images=False), or select OpenAI/Azure OpenAI for images."
            )

    @classmethod
    def check_configuration(cls):
        """
        Checks if at least one LLM provider is properly configured.
        Raises ValueError if no LLM service is properly configured.
        """
        cls.get_available_provider()

    @classmethod
    def validate_connectivity(cls) -> bool:
        """
        Perform a lightweight connectivity and credential validation for the configured LLM provider.

        - Azure OpenAI: use az-ai-healthcheck. Return True when ok; otherwise raise ValueError.
        - OpenAI: use ai-healthcheck. Return True when ok; otherwise raise ValueError with details.

        Raises:
            ValueError: with actionable message if validation fails.
        """
        provider = cls.get_available_provider()

        if provider == LLMProvider.ANTHROPIC:
            try:
                from anthropic import Anthropic
                from agent_framework_anthropic import AnthropicClient  # noqa: F401
            except ImportError:
                raise ValueError(ANTHROPIC_INSTALL_MESSAGE) from None
            try:
                with Anthropic(
                    api_key=AnthropicConfig.get_api_key(), timeout=10.0, max_retries=0
                ) as client:
                    client.messages.create(
                        model=AnthropicConfig.get_chat_model_id(),
                        max_tokens=1,
                        messages=[{"role": "user", "content": "Hi"}],
                    )
            except Exception as exc:
                # Do not expose credentials or provider response bodies in CLI errors.
                status = getattr(exc, "status_code", None)
                detail = f" (HTTP {status})" if isinstance(status, int) else ""
                raise ValueError(
                    f"Anthropic connectivity check failed{detail}. Check ANTHROPIC_API_KEY, "
                    "ANTHROPIC_CHAT_MODEL_ID, model access, quota, and network connectivity."
                ) from None
            return True

        if provider == LLMProvider.AZURE_OPENAI:
            env_sets = AzureOpenAIConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "Azure OpenAI configuration missing required values. Ensure AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_API_KEY, and AZURE_OPENAI_CHAT_DEPLOYMENT_NAME are set."
                )

            last_message: Optional[str] = None
            for env_set in env_sets:
                endpoint = (env_set.values.get("AZURE_OPENAI_ENDPOINT") or "").rstrip(
                    "/"
                )
                api_version = env_set.values.get("AZURE_OPENAI_API_VERSION")
                api_key = env_set.values.get("AZURE_OPENAI_API_KEY")
                deployment = env_set.values.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")

                if not endpoint or not api_version or not api_key or not deployment:
                    continue

                try:
                    res = check_azure_openai(
                        endpoint=endpoint,
                        api_key=api_key,
                        api_version=api_version,
                        deployment=deployment,
                        timeout=10.0,
                    )
                except Exception as e:
                    last_message = str(e)
                    continue

                if res.ok:
                    set_preferred_env_set(AzureOpenAIConfig._GROUP, env_set.index)
                    return True
                last_message = res.message

            raise ValueError(last_message or "Azure OpenAI connectivity check failed")

        elif provider == LLMProvider.OPENAI:
            env_sets = OpenAIConfig.get_env_sets()
            if not env_sets:
                raise ValueError(
                    "OpenAI configuration missing required values. Ensure OPENAI_API_KEY and OPENAI_CHAT_MODEL_ID are set."
                )

            last_message: Optional[str] = None
            for env_set in env_sets:
                api_key = env_set.values.get("OPENAI_API_KEY")
                base_url = env_set.values.get("OPENAI_BASE_URL")
                org_id = env_set.values.get("OPENAI_ORG_ID")
                model_id = env_set.values.get("OPENAI_CHAT_MODEL_ID")

                if not api_key or not model_id:
                    continue

                try:
                    res = check_openai(
                        endpoint=base_url,
                        api_key=api_key,
                        model=model_id,
                        org_id=org_id,
                        timeout=10.0,
                    )
                except Exception as e:
                    last_message = str(e)
                    continue

                if res.ok:
                    set_preferred_env_set(OpenAIConfig._GROUP, env_set.index)
                    return True
                last_message = res.message

            raise ValueError(last_message or "OpenAI connectivity check failed")
        else:
            # Should not happen because get_available_provider() would have raised earlier otherwise
            raise ValueError("No LLM provider available for connectivity validation.")
