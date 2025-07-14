"""
Microsoft open-source repository structure implementation.
"""
from pathlib import Path
from typing import Dict, Any
import os

from .base_structure import ProjectStructure


class MSRepoStructure(ProjectStructure):
    """Implementation for Microsoft open-source repository structure.
    
    Handles path mapping and metadata formatting according to Microsoft's
    open-source documentation conventions.
    """
    
    def get_translation_path(self, original_path: Path, lang_code: str) -> Path:
        """
        Map original file path to translation path.
        
        For MS repos, translations are stored under translations/{lang_code}/
        preserving the original file structure.
        
        Args:
            original_path: Path to the original file
            lang_code: Target language code
            
        Returns:
            Path: The corresponding translation path
        """
        rel_path = original_path.relative_to(self.root_dir)
        return self.translations_dir / lang_code / rel_path
    
    def get_original_path(self, translation_path: Path) -> Path:
        """
        Map translation path back to original file path.
        
        Args:
            translation_path: Path to the translation file
            
        Returns:
            Path: The corresponding original file path
        """
        # Extract relative path after language code directory
        try:
            # First get the path relative to translations directory
            rel_to_translations = translation_path.relative_to(self.translations_dir)
            
            # The first part should be the language code
            if len(rel_to_translations.parts) < 2:
                raise ValueError(f"Invalid translation path structure: {translation_path}")
                
            # Remove language code to get path relative to root
            lang_code = rel_to_translations.parts[0]
            rel_path = Path(*rel_to_translations.parts[1:])
            
            # Construct original path
            return self.root_dir / rel_path
        except Exception as e:
            # If there's an error, log and return the translation path
            return translation_path
    
    def create_directory_structure(self) -> bool:
        """
        Create necessary directory structure for translations.
        
        For MS repos, creates:
        - translations/{lang_code}/ for each language code
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            for lang_code in self.language_codes:
                lang_dir = self.translations_dir / lang_code
                os.makedirs(lang_dir, exist_ok=True)
            return True
        except Exception:
            return False
    
    def format_metadata(self, metadata: Dict[str, Any], format_type: str) -> str:
        """
        Format metadata according to MS repo requirements.
        
        Args:
            metadata: Dictionary of metadata
            format_type: Type of formatting (e.g., "markdown", "yaml")
            
        Returns:
            str: Formatted metadata string
        """
        if format_type == "markdown":
            # Format for markdown files (front matter)
            lines = ["---"]
            
            for key, value in metadata.items():
                if key == "description":
                    # MS repos typically use description_suffix for translations
                    lines.append(f"description_suffix: '{value}'")
                else:
                    # Format other metadata fields
                    if isinstance(value, str):
                        lines.append(f"{key}: '{value}'")
                    else:
                        lines.append(f"{key}: {value}")
            
            lines.append("---")
            return "\n".join(lines)
        
        elif format_type == "yaml":
            # Format for YAML metadata files
            lines = []
            
            for key, value in metadata.items():
                if isinstance(value, str):
                    lines.append(f"{key}: '{value}'")
                else:
                    lines.append(f"{key}: {value}")
            
            return "\n".join(lines)
        
        # Default to empty string for unsupported formats
        return ""
    
    def get_language_code_from_path(self, translation_path: Path) -> str:
        """
        Extract language code from a translation path.
        
        Args:
            translation_path: Path to a translation file
            
        Returns:
            str: The language code
        """
        # In MS repo structure, language code is the first directory under translations/
        try:
            rel_path = translation_path.relative_to(self.translations_dir)
            if rel_path.parts:
                return rel_path.parts[0]
        except (ValueError, IndexError):
            pass
        
        # Return empty string if extraction fails
        return ""
