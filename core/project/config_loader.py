"""
Configuration loader for project structure settings.
"""
from pathlib import Path
from typing import Dict, Any, Optional
import logging
import yaml
from collections.abc import Mapping

logger = logging.getLogger(__name__)


class ConfigLoader:
    """Load and manage project structure configuration."""
    
    @classmethod
    def load_config(cls, config_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Load project configuration from file with fallback to defaults.
        
        Args:
            config_path: Path to config file (translation_config.yml)
            
        Returns:
            Dict: Configuration dictionary
        """
        # Default configuration for MS repo structure
        default_config = {
            "project_type": "ms_repo",
            "paths": {
                "translations": "translations",
                "images": "translated_images",
            },
            "metadata": {
                "use_front_matter": True,
                "description_field": "description_suffix",
            },
            "excluded_dirs": [
                ".git",
                ".github",
                "node_modules",
                "translations",
                "translated_images",
                "__pycache__",
                "venv",
                ".venv",
                "env",
                ".env",
            ],
            "extensions": {
                "markdown": [".md", ".markdown"],
                "images": [".png", ".jpg", ".jpeg", ".gif", ".svg"],
                "notebooks": [".ipynb"],
            }
        }
        
        # If config path is provided and exists, load and merge with defaults
        if config_path and config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_config = yaml.safe_load(f) or {}
                    
                # Merge user config with default config
                cls._deep_merge(default_config, user_config)
                logger.info(f"Loaded custom configuration from {config_path}")
                
            except Exception as e:
                logger.error(f"Error loading config from {config_path}: {e}")
                # Continue with default config if loading fails
        
        return default_config
    
    @classmethod
    def _deep_merge(cls, target: Dict, source: Dict) -> None:
        """
        Deep merge two dictionaries, modifying target in place.
        
        Args:
            target: Target dictionary to update
            source: Source dictionary with values to merge
        """
        for key, value in source.items():
            if key in target and isinstance(target[key], Mapping) and isinstance(value, Mapping):
                # If both values are dictionaries, merge them recursively
                cls._deep_merge(target[key], value)
            else:
                # Otherwise replace/add the value
                target[key] = value
