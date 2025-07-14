"""
Markdown translator implementation for handling markdown document translation.
"""
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import asyncio

from ..utils.llm.markdown_utils import (
    extract_yaml_frontmatter,
    extract_code_blocks,
    replace_code_blocks,
    markdown_summary,
)
from ..config.llm_config.config import LLMConfig
from ..config.llm_config.provider import LLMProvider
from .text_translator import TextTranslator

logger = logging.getLogger(__name__)


class MarkdownTranslator:
    """Translator for markdown documents.

    Handles preprocessing, translation, and postprocessing of markdown content.
    """

    def __init__(self, text_translator: TextTranslator):
        """Initialize markdown translator.

        Args:
            text_translator: Text translator instance for content translation
        """
        self.text_translator = text_translator

    async def translate_markdown(
        self, content: str, target_language: str, file_path: Optional[Path] = None
    ) -> str:
        """
        Translate markdown content to target language.

        Args:
            content: Markdown content to translate
            target_language: Target language code
            file_path: Path to the markdown file (for logging)

        Returns:
            Translated markdown content
        """
        if not content:
            return ""

        # Extract YAML frontmatter
        frontmatter, content_without_frontmatter = extract_yaml_frontmatter(content)

        # Extract code blocks to preserve them
        content_without_code, code_blocks = extract_code_blocks(content_without_frontmatter)

        # Get content summary for context
        content_summary = markdown_summary(content_without_code)
        
        # Generate translation prompt
        prompt = self._generate_translation_prompt(
            content_without_code, target_language, content_summary, file_path
        )

        # Get translation
        translated_content = await self._get_translation(prompt, target_language)

        # Restore code blocks
        final_content = replace_code_blocks(translated_content, code_blocks)

        return final_content

    def _generate_translation_prompt(
        self, content: str, target_language: str, summary: str, file_path: Optional[Path] = None
    ) -> str:
        """
        Generate prompt for markdown translation.

        Args:
            content: Markdown content to translate
            target_language: Target language code
            summary: Summary of the content for context
            file_path: Path to the markdown file (for context)

        Returns:
            Translation prompt
        """
        context = f"File: {file_path.name}" if file_path else ""
        summary_context = f"Content summary: {summary}" if summary else ""
        
        prompt = f"""Translate the following markdown content to {target_language}. 
{context}
{summary_context}

Important rules:
1. Preserve all markdown formatting, including headings, links, emphasis, and lists
2. DO NOT translate code blocks, variable names, function names, or commands
3. Keep HTML tags intact without translation
4. Preserve all links and image references exactly as they appear
5. Ensure translated text maintains the original meaning and tone
6. Keep all special characters like backticks, asterisks, and brackets in their original positions

Here is the content to translate:

{content}

Translation:
"""
        return prompt

    async def _get_translation(self, prompt: str, target_language: str) -> str:
        """
        Get translation from the text translator.

        Args:
            prompt: Translation prompt
            target_language: Target language code

        Returns:
            Translated content
        """
        try:
            # Use the text translator to get the translation
            translated_content = self.text_translator.get_completion(prompt)
            return translated_content
        except Exception as e:
            logger.error(f"Error translating to {target_language}: {e}")
            return ""

    @staticmethod
    def create(text_translator: Optional[TextTranslator] = None):
        """Factory method to create a markdown translator instance.

        Args:
            text_translator: Text translator instance (if None, one will be created)

        Returns:
            MarkdownTranslator instance
        """
        # Create text translator if not provided
        if text_translator is None:
            text_translator = TextTranslator.create()
            
        return MarkdownTranslator(text_translator)
