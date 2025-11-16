from abc import ABC, abstractmethod
import logging
from co_op_translator.utils.llm.text_utils import (
    gen_image_translation_prompt,
    remove_code_backticks,
    TranslationResponse,
)
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.llm_config.provider import LLMProvider
from co_op_translator.config.font_config import FontConfig

logger = logging.getLogger(__name__)


class TextTranslator(ABC):
    """Define interface for text translation services.

    Provides common functionality and abstract methods to be implemented by providers.
    """

    def __init__(self):
        self.client = self.get_openai_client()
        self.font_config = FontConfig()

    @abstractmethod
    def get_openai_client(self):
        """Create and configure a model client instance.

        Returns:
            Initialized AI model client for the specific provider
        """
        pass

    @abstractmethod
    def get_model_name(self) -> str:
        """Retrieve the configured model name for the provider."""
        pass

    def _should_passthrough_image_line(self, line: str) -> bool:
        stripped = (line or "").strip()
        if not stripped:
            return False

        lower = stripped.lower()
        passthrough_lang_codes = {
            "en",
            "fr",
            "es",
            "de",
            "ru",
            "ar",
            "fa",
            "ur",
            "zh",
            "mo",
            "hk",
            "tw",
            "ja",
            "ko",
            "hi",
            "bn",
            "mr",
            "ne",
            "pa",
        }

        if lower in passthrough_lang_codes:
            return True

        if lower.endswith((".ttf", ".ttc", ".otf")):
            if " " not in stripped and any(c.isalpha() for c in stripped):
                return True

        return False

    def translate_image_text(self, text_data: list, target_language: str) -> list:
        """Translate extracted text from images to target language.

        Uses structured outputs to ensure 1:1 line mapping and prevent
        Arabic ligature rendering issues.

        Args:
            text_data: List of text lines to translate
            target_language: Target language code

        Returns:
            List of translated text lines with exact count matching input
        """
        if not text_data:
            return []

        passthrough_mask: list[bool] = []
        llm_input_lines: list[str] = []
        for line in text_data:
            if self._should_passthrough_image_line(line):
                passthrough_mask.append(True)
            else:
                passthrough_mask.append(False)
                llm_input_lines.append(line)

        if not llm_input_lines:
            return text_data.copy()

        language_name = self.font_config.get_language_name(target_language)
        prompt = gen_image_translation_prompt(
            llm_input_lines, target_language, language_name
        )

        response = self.client.chat.completions.parse(
            model=self.get_model_name(),
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a professional translator. For each input line, "
                        "output exactly one short translated line in the target language. "
                        "Do not add explanations, examples, notes, or commentary. "
                        "Return exactly the same number of translations as input lines."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            response_format=TranslationResponse,
            max_tokens=2000,
            temperature=0,
        )

        translations_llm = response.choices[0].message.parsed.translations
        logger.debug(
            f"Structured output: {len(translations_llm)} translations for {len(llm_input_lines)} non-passthrough input lines "
            f"(total original lines: {len(text_data)})"
        )

        # Ensure 1:1 mapping between detected lines and translated lines for the
        # subset that was actually sent to the LLM. If the structured output
        # returns a different number of translations (e.g., merges multiple
        # lines into a single chunk), fall back to per-line translation for the
        # non-passthrough lines to preserve layout alignment.
        if len(translations_llm) != len(llm_input_lines):
            logger.warning(
                "Structured output line-count mismatch: "
                f"{len(translations_llm)} translations for {len(llm_input_lines)} non-passthrough input lines. "
                "Falling back to per-line translation to preserve 1:1 mapping."
            )

            fallback_translations: list[str] = []
            for line in llm_input_lines:
                if not line:
                    fallback_translations.append("")
                    continue
                try:
                    fallback_translations.append(
                        self.translate_text(line, target_language)
                    )
                except Exception:
                    logger.exception(
                        "Failed to translate individual image text line; "
                        "using source text as fallback."
                    )
                    fallback_translations.append(line)

            translated_non_passthrough = fallback_translations
        else:
            translated_non_passthrough = translations_llm

        result: list[str] = []
        non_passthrough_index = 0
        for is_passthrough, original in zip(passthrough_mask, text_data):
            if is_passthrough:
                result.append(original)
            else:
                result.append(translated_non_passthrough[non_passthrough_index])
                non_passthrough_index += 1

        return result

    def translate_text(self, text: str, target_language: str) -> str:
        """Translate plain text to specified target language.

        Args:
            text: Source text content to translate
            target_language: Target language code

        Returns:
            Translated text content
        """
        prompt = f"Translate the following text into {target_language}:\n\n{text}"
        response = self.client.chat.completions.create(
            model=self.get_model_name(),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=2000,
            temperature=0,
        )
        translated_text = remove_code_backticks(response.choices[0].message.content)
        return translated_text

    @classmethod
    def create(cls) -> "TextTranslator":
        """Create appropriate text translator implementation based on configuration.

        Factory method that instantiates the correct translator class based on
        the LLM provider settings.

        Returns:
            Configured text translator instance

        Raises:
            ValueError: When no valid LLM provider is configured
        """
        provider = LLMConfig.get_available_provider()
        if provider == LLMProvider.AZURE_OPENAI:
            from co_op_translator.core.llm.providers.azure.text_translator import (
                AzureTextTranslator,
            )

            return AzureTextTranslator()
        elif provider == LLMProvider.OPENAI:
            from co_op_translator.core.llm.providers.openai.text_translator import (
                OpenAITextTranslator,
            )

            return OpenAITextTranslator()
        else:
            raise ValueError("No valid LLM provider configured")
