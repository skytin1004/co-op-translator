"""
Jupyter notebook translator implementation.
"""
import json
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..utils.common.file_utils import read_input_file
from .text_translator import TextTranslator

logger = logging.getLogger(__name__)


class JupyterNotebookTranslator:
    """Translator for Jupyter notebook files.

    Handles translation of markdown cells in Jupyter notebooks while preserving
    code cells and notebook structure.
    """

    def __init__(self, text_translator: TextTranslator):
        """Initialize notebook translator.

        Args:
            text_translator: Text translator instance for content translation
        """
        self.text_translator = text_translator

    def translate_notebook(self, notebook_path: Path, target_language: str) -> Dict[str, Any]:
        """
        Translate markdown cells in a Jupyter notebook to target language.

        Args:
            notebook_path: Path to the notebook file
            target_language: Target language code

        Returns:
            Translated notebook as dictionary
        """
        try:
            # Read the notebook file
            content = read_input_file(notebook_path)
            if not content:
                logger.warning(f"Empty notebook file: {notebook_path}")
                return {}

            # Parse the notebook JSON
            notebook = json.loads(content)
            
            # Translate each markdown cell
            for cell in notebook.get("cells", []):
                if cell.get("cell_type") == "markdown":
                    # Get the markdown content
                    source = cell.get("source", [])
                    
                    # Join the source lines
                    if isinstance(source, list):
                        markdown_content = "".join(source)
                    else:
                        markdown_content = source
                        
                    # Skip empty cells
                    if not markdown_content.strip():
                        continue
                        
                    # Translate the markdown content
                    translated_content = self._translate_markdown_cell(markdown_content, target_language)
                    
                    # Split the translated content back into lines and update the cell
                    cell["source"] = translated_content.splitlines(True)
            
            return notebook
            
        except Exception as e:
            logger.error(f"Error translating notebook {notebook_path}: {e}")
            return {}
            
    def _translate_markdown_cell(self, content: str, target_language: str) -> str:
        """
        Translate markdown cell content.

        Args:
            content: Markdown content to translate
            target_language: Target language code

        Returns:
            Translated markdown content
        """
        try:
            # Generate prompt for translation
            prompt = f"""Translate the following Jupyter notebook markdown cell to {target_language}. 
Keep all code snippets, variable names, and function names unchanged.
Preserve all markdown formatting like headers, lists, and emphasis.

Content:
{content}

Translation:"""

            # Get translation
            translated_content = self.text_translator.get_completion(prompt)
            return translated_content
            
        except Exception as e:
            logger.error(f"Error translating markdown cell to {target_language}: {e}")
            return content

    def save_translated_notebook(self, notebook: Dict[str, Any], output_path: Path) -> bool:
        """
        Save translated notebook to file.

        Args:
            notebook: Notebook content as dictionary
            output_path: Path to save the translated notebook

        Returns:
            True if saved successfully, False otherwise
        """
        try:
            # Create parent directory if it doesn't exist
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write the notebook to file
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(notebook, f, ensure_ascii=False, indent=2)
                
            logger.info(f"Saved translated notebook to {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving translated notebook to {output_path}: {e}")
            return False

    @staticmethod
    def create(text_translator: Optional[TextTranslator] = None):
        """Factory method to create a notebook translator instance.

        Args:
            text_translator: Text translator instance (if None, one will be created)

        Returns:
            JupyterNotebookTranslator instance
        """
        # Create text translator if not provided
        if text_translator is None:
            text_translator = TextTranslator.create()
            
        return JupyterNotebookTranslator(text_translator)
