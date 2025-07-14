"""
Base project structure interface for different documentation frameworks.
"""
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any


class ProjectStructure(ABC):
    """Abstract base class for handling project-specific directory structures.
    
    This interface defines methods for mapping between original and translated paths,
    creating necessary directory structures, and formatting metadata according to
    project-specific requirements.
    """
    
    def __init__(self, root_dir: Path, translations_dir: Path, language_codes: list):
        """
        Initialize project structure handler.
        
        Args:
            root_dir: Root directory of the project
            translations_dir: Directory for translations
            language_codes: List of language codes to support
        """
        self.root_dir = root_dir
        self.translations_dir = translations_dir
        self.language_codes = language_codes
    
    @abstractmethod
    def get_translation_path(self, original_path: Path, lang_code: str) -> Path:
        """
        Map an original file path to its translation path for a specific language.
        
        Args:
            original_path: Path to the original file
            lang_code: Target language code
            
        Returns:
            Path: The corresponding translation path
        """
        pass
    
    @abstractmethod
    def get_original_path(self, translation_path: Path) -> Path:
        """
        Map a translation path back to its original file path.
        
        Args:
            translation_path: Path to the translation file
            
        Returns:
            Path: The corresponding original file path
        """
        pass
    
    @abstractmethod
    def create_directory_structure(self) -> bool:
        """
        Create necessary directory structure for translations.
        
        Returns:
            bool: True if successful, False otherwise
        """
        pass
    
    @abstractmethod
    def format_metadata(self, metadata: Dict[str, Any], format_type: str) -> str:
        """
        Format metadata according to project-specific requirements.
        
        Args:
            metadata: Dictionary of metadata
            format_type: Type of formatting to apply (e.g., "markdown", "yaml")
            
        Returns:
            str: Formatted metadata string
        """
        pass
    
    def get_language_code_from_path(self, translation_path: Path) -> str:
        """
        Extract language code from a translation path.
        
        Args:
            translation_path: Path to a translation file
            
        Returns:
            str: The language code
        """
        # This default implementation assumes the language code is the direct parent
        # directory name of the translation file relative to the translations directory
        rel_path = translation_path.relative_to(self.translations_dir)
        return rel_path.parts[0] if rel_path.parts else ""
