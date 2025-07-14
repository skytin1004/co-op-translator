"""
Provider-related configurations and enums.
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Optional


class LLMProvider(Enum):
    """LLM service providers with their configurations."""

    AZURE_OPENAI = "azure_openai"
    OPENAI = "openai"

    @property
    def display_name(self) -> str:
        """Get a human-readable display name."""
        return self.value.replace("_", " ").title()
    
    @classmethod
    def from_string(cls, provider_str: str) -> 'LLMProvider':
        """Convert a string representation to enum value.
        
        This is helpful for testing and configuration loading.
        
        Args:
            provider_str: String representation of the provider
            
        Returns:
            LLMProvider enum value
            
        Raises:
            ValueError: If the string does not match any provider
        """
        for provider in cls:
            if provider.value == provider_str:
                return provider
        raise ValueError(f"Unknown provider: {provider_str}")


@dataclass
class LLMServiceConfig:
    """Configuration for a specific LLM service."""

    required: bool
    priority: int
    env_vars: Dict[str, Optional[str]]
