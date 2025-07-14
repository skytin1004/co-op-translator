"""
Factory for creating project structure handlers.
"""
from pathlib import Path
from typing import Dict, Any, Optional, Type

from .base_structure import ProjectStructure
from .ms_structure import MSRepoStructure


class ProjectStructureFactory:
    """Factory for creating appropriate project structure implementations.
    
    This factory creates the appropriate ProjectStructure implementation
    based on the provided configuration.
    """
    
    @classmethod
    def create_structure(cls, 
                       config: Dict[str, Any], 
                       root_dir: Path, 
                       translations_dir: Optional[Path] = None,
                       language_codes: list = None) -> ProjectStructure:
        """
        Create appropriate project structure implementation.
        
        Args:
            config: Configuration dictionary
            root_dir: Root directory of the project
            translations_dir: Directory for translations (if None, derived from config and root_dir)
            language_codes: List of language codes to support
            
        Returns:
            ProjectStructure: Appropriate implementation based on config
        """
        # Set default values if not provided
        if translations_dir is None:
            translations_path = config.get("paths", {}).get("translations", "translations")
            translations_dir = root_dir / translations_path
            
        if language_codes is None:
            language_codes = []
        
        # Get project type from config
        project_type = config.get("project_type", "ms_repo").lower()
        
        # Create appropriate structure handler
        if project_type == "ms_repo":
            return MSRepoStructure(root_dir, translations_dir, language_codes)
        
        # For other types, would implement conditional imports and initialization
        # This allows us to keep the open-source version clean while supporting
        # extended functionality in LocalizeFlow
        
        # E.g., for Docusaurus:
        # if project_type == "docusaurus":
        #     try:
        #         from web.localizeflow.adapters.docusaurus import DocusaurusStructure
        #         return DocusaurusStructure(root_dir, translations_dir, language_codes)
        #     except ImportError:
        #         # Fallback to MS repo structure if adapter not available
        #         return MSRepoStructure(root_dir, translations_dir, language_codes)
        
        # Default to MS repo structure for unknown types
        return MSRepoStructure(root_dir, translations_dir, language_codes)
