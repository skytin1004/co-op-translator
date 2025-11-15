import logging
from pathlib import Path
from typing import Iterable
import importlib.resources

import click
import yaml

from co_op_translator.config.base_config import Config
from co_op_translator.config.llm_config.config import LLMConfig
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.utils.common.logging_utils import setup_logging

from co_op_translator.localizeflow.glossary import set_glossaries


logger = logging.getLogger(__name__)


def run_translation(
    language_codes: str,
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = False,
    glossaries: Iterable[str] | None = None,
) -> None:
    """Programmatic translation entrypoint mirroring the translate CLI options.

    This helper keeps behavior close to co_op_translator.cli.translate.translate_command
    while allowing Localizeflow to inject glossaries and avoid interactive prompts.
    """

    # Validate configuration
    Config.check_configuration()

    # Build translation types list
    translation_types: list[str] = []
    if markdown:
        translation_types.append("markdown")
    if images:
        translation_types.append("images")
    if notebook:
        translation_types.append("notebook")
    if not translation_types:
        translation_types = ["markdown", "notebook", "images"]

    # If images enabled, ensure Vision config is available
    if "images" in translation_types:
        cv_available = VisionConfig.check_configuration()
        if not cv_available:
            raise RuntimeError(
                "Image translation is enabled but Azure AI Service is not configured.\n"
                "Please add AZURE_AI_SERVICE_API_KEY to your environment variables or use "
                "translation_types without 'images'.\n"
                "See the .env.template file for required variables."
            )

    # Log selected translation mode
    mode_msg = f"🚀 Translation mode: {', '.join(translation_types)}"
    click.echo(mode_msg)

    # Validate root directory and configure logging
    root_path = Path(root_dir).resolve()
    if not root_path.exists():
        raise ValueError(f"Root directory does not exist: {root_dir}")
    if not root_path.is_dir():
        raise ValueError(f"Root path is not a directory: {root_dir}")

    log_file_path = setup_logging(
        root_path, debug=debug, save_logs=save_logs, command_name="translate"
    )
    if debug:
        logging.debug("Debug mode enabled.")
    if save_logs and log_file_path is not None:
        click.echo(f"📄 Logs will be saved to: {log_file_path}")

    # LLM health check (raises on failure)
    LLMConfig.validate_connectivity()
    logger.info("LLM health check passed.")
    click.echo("✅ LLM health check passed.")

    # Vision health check when images are enabled
    if "images" in translation_types:
        VisionConfig.validate_connectivity()
        logger.info("Vision health check passed.")
        click.echo("✅ Vision health check passed.")

    # Handle 'all' languages selection (non-interactive: auto-proceed)
    all_languages_selected = language_codes == "all"
    if all_languages_selected:
        click.echo(
            "Warning: Translating all languages at once can take a significant amount of time, "
            "especially for large projects."
        )
        if not yes:
            logger.info("Auto-confirming 'all' languages in non-interactive mode.")
            click.echo("Auto-confirming translation for all languages...")

        try:
            with importlib.resources.path(
                "co_op_translator.fonts", "font_language_mappings.yml"
            ) as mappings_path:
                with open(mappings_path, "r", encoding="utf-8") as file:
                    font_mappings = yaml.safe_load(file)
                    if not font_mappings:
                        raise RuntimeError("Empty font mappings file")
                    language_codes = " ".join(
                        [
                            lang_code
                            for lang_code in font_mappings
                            if isinstance(font_mappings[lang_code], dict)
                        ]
                    )
                    if not language_codes:
                        raise RuntimeError(
                            "No valid language codes found in font mappings"
                        )
                    logging.debug(
                        f"Loaded language codes from font mapping: {language_codes}"
                    )
        except (FileNotFoundError, yaml.YAMLError) as e:
            raise RuntimeError(f"Failed to load font mappings: {str(e)}") from e

    # Warn when update mode is enabled (non-interactive: no prompt)
    if update:
        click.echo(
            f"Warning: Update mode will delete all existing translations for '{language_codes}' "
            f"and re-translate them."
        )

    # Apply glossaries (Localizeflow feature)
    if glossaries is not None:
        set_glossaries(glossaries)

    # Initialize ProjectTranslator with determined settings
    translator = ProjectTranslator(
        language_codes, root_dir, translation_types=translation_types
    )

    # Estimate tokens before running translation and print a concise summary
    try:
        est = translator.translation_manager.estimate_tokens(update=update)
        parts: list[str] = []
        if "markdown" in translation_types and est.get("markdown", 0):
            parts.append(f"markdown: {est['markdown']:,}")
        if "notebook" in translation_types and est.get("notebook", 0):
            parts.append(f"notebook: {est['notebook']:,}")
        if (
            "markdown" in translation_types or "notebook" in translation_types
        ) and est.get("outdated", 0):
            parts.append(f"retranslation: {est['outdated']:,}")
        breakdown = ", ".join(parts) if parts else "none"
        click.echo(
            f"📊 Estimated tokens before translation: {est.get('total', 0):,} (breakdown: {breakdown})"
        )
    except Exception as e:  # pragma: no cover - best-effort logging only
        logger.debug(f"Failed to compute estimated tokens: {e}")

    translator.translate_project(
        update=update,
    )

    logger.info(f"Project translation completed for languages: {language_codes}")
