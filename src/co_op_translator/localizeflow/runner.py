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
from co_op_translator.core.project.language_migrator import LanguageFolderMigrator
from co_op_translator.utils.common.logging_utils import setup_logging
from co_op_translator.utils.common.file_utils import (
    update_readme_languages_table,
    update_readme_other_courses,
)

from co_op_translator.localizeflow.glossary import set_glossaries
from co_op_translator.localizeflow.frontmatter import (
    ensure_localizeflow_frontmatter_parser,
)
from co_op_translator.utils.common.metadata_utils import (
    normalize_language_codes_in_lang_metadata,
)
from co_op_translator.utils.common.lang_utils import normalize_language_codes
from co_op_translator.localizeflow.utils.token_utils import estimate_translation_tokens
from co_op_translator.localizeflow.utils.words_utils import estimate_translation_words


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
    yes: bool = True,
    glossaries: Iterable[str] | None = None,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: Iterable[str] | None = None,
    groups: Iterable[tuple[str, str | None]] | None = None,
    repo_url: str | None = None,
    dry_run: bool = False,
) -> None:
    """Programmatic translation entrypoint mirroring the translate CLI options.

    This helper keeps behavior close to co_op_translator.cli.translate.translate_command
    while allowing Localizeflow to inject glossaries and avoid interactive prompts.
    """

    def _split_lang_placeholder(path: str) -> tuple[str, str | None]:
        """Split a target path containing a <lang> placeholder.

        Example:
            "i18n/<lang>/docusaurus-plugin-content-docs/current" ->
            ("i18n", "docusaurus-plugin-content-docs/current")

        If no placeholder is present, returns (path, None).
        """

        placeholder = "<lang>"
        if placeholder not in path:
            return path, None

        prefix, suffix = path.split(placeholder, 1)
        prefix = prefix.rstrip("/\\")
        suffix = suffix.lstrip("/\\")

        return prefix, (suffix or None)

    def _run_single_group(
        *,
        language_codes: str,
        root_dir: str,
        update: bool,
        images: bool,
        markdown: bool,
        notebook: bool,
        debug: bool,
        save_logs: bool,
        yes: bool,
        glossaries: Iterable[str] | None,
        add_disclaimer: bool,
        translations_dir: str | None,
        image_dir: str | None,
        lang_subdir: str | None,
        repo_url: str | None,
        dry_run: bool,
        emit_estimate: bool = True,
    ) -> dict[str, int]:
        # Validate configuration
        Config.check_configuration()
        ensure_localizeflow_frontmatter_parser()

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

        # Build normalized language list for pre-processing steps
        if all_languages_selected:
            try:
                lang_list = Config.get_language_codes()
            except Exception:
                lang_list = [
                    code.strip() for code in language_codes.split() if code.strip()
                ]
        else:
            lang_list = [
                code.strip() for code in language_codes.split() if code.strip()
            ]
        lang_list = normalize_language_codes(lang_list) if lang_list else []

        # Warn when update mode is enabled (non-interactive: no prompt)
        if update:
            click.echo(
                f"Warning: Update mode will delete all existing translations for '{language_codes}' "
                f"and re-translate them."
            )

        # Apply glossaries (Localizeflow feature)
        if glossaries is not None:
            set_glossaries(glossaries)

        # Detect and (optionally) migrate alias-based language folders BEFORE estimation
        try:
            # Resolve effective directories for scanning
            effective_translations_dir = (
                (root_path / translations_dir).resolve()
                if translations_dir is not None
                and not Path(translations_dir).is_absolute()
                else (
                    Path(translations_dir).resolve()
                    if translations_dir is not None
                    else (root_path / "translations")
                )
            )
            effective_image_dir = (
                (root_path / image_dir).resolve()
                if image_dir is not None and not Path(image_dir).is_absolute()
                else (
                    Path(image_dir).resolve()
                    if image_dir is not None
                    else (root_path / "translated_images")
                )
            )

            migrator = LanguageFolderMigrator(
                root_path,
                translations_dir=effective_translations_dir,
                image_dir=effective_image_dir,
            )
            alias_entries = migrator.detect_alias_folders()
            if alias_entries:
                canon_set = set(lang_list)
                relevant = [e for e in alias_entries if e.canonical in canon_set]
                if relevant:
                    plan = LanguageFolderMigrator.format_plan(relevant)
                    logger.info("Language folder migration plan:\n%s", plan)
                    click.echo(plan)
                    if dry_run:
                        click.echo("Dry run: no changes will be made.")
                    else:
                        renamed, msgs = migrator.execute(relevant, dry_run=False)
                        logger.info("Auto-migrated %d language folder(s).", renamed)
                        for m in msgs:
                            logger.warning(m)
        except Exception as e:  # pragma: no cover - best-effort logging only
            logger.warning(f"Language folder migration step skipped: {e}")

        # Ensure per-language metadata files store canonical language_code values BEFORE estimation
        try:
            for lang in lang_list:
                # translations/<lang>/.co-op-translator.json
                lang_root = (
                    effective_translations_dir
                    if "effective_translations_dir" in locals()
                    else (root_path / "translations")
                ) / lang
                if lang_subdir:
                    lang_root = lang_root / lang_subdir

                normalize_language_codes_in_lang_metadata(
                    lang_root,
                    lang,
                )
                # translated_images/<lang>/.co-op-translator.json
                normalize_language_codes_in_lang_metadata(
                    (
                        effective_image_dir
                        if "effective_image_dir" in locals()
                        else (root_path / "translated_images")
                    )
                    / lang,
                    lang,
                )
                # translated_images_fast/<lang>/.co-op-translator.json (best-effort)
                normalize_language_codes_in_lang_metadata(
                    root_path / "translated_images_fast" / lang,
                    lang,
                )
        except Exception as e:  # pragma: no cover - best-effort logging only
            logger.debug(f"Metadata normalization skipped: {e}")

        # Update README shared sections BEFORE estimation (mirror CLI behavior)
        readme_path = root_path / "README.md"
        try:
            # Always attempt to update, and personalize advisory using repo_url when provided
            if update_readme_languages_table(readme_path, repo_url=repo_url):
                click.echo("✅ Updated README languages table from template.")
            else:
                click.echo(
                    "ℹ️ README languages table not updated (markers missing or template unavailable)."
                )
        except Exception as e:  # pragma: no cover - best-effort logging only
            logger.warning(f"Failed to update README languages table: {e}")

        try:
            if update_readme_other_courses(readme_path):
                click.echo("✅ Updated README 'Other courses' section from template.")
        except Exception as e:  # pragma: no cover - best-effort logging only
            logger.warning(f"Failed to update README 'Other courses': {e}")

        # Initialize ProjectTranslator with determined settings
        translator = ProjectTranslator(
            language_codes,
            root_dir,
            translation_types=translation_types,
            add_disclaimer=add_disclaimer,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )

        estimated_tokens: dict[str, int] = {
            "markdown": 0,
            "notebook": 0,
            "images": 0,
            "outdated": 0,
            "total": 0,
        }
        estimated_words: dict[str, int] = {
            "markdown": 0,
            "notebook": 0,
            "images": 0,
            "outdated": 0,
            "total": 0,
        }
        try:
            est = estimate_translation_tokens(
                translator.translation_manager, update=update
            )
            for key in estimated_tokens:
                estimated_tokens[key] = int(est.get(key, 0) or 0)

            words_est = estimate_translation_words(
                translator.translation_manager, update=update
            )
            for key in estimated_words:
                estimated_words[key] = int(words_est.get(key, 0) or 0)

            parts: list[str] = []
            if "markdown" in translation_types and est.get("markdown", 0):
                parts.append(f"markdown: {est['markdown']:,}")
            if "notebook" in translation_types and est.get("notebook", 0):
                parts.append(f"notebook: {est['notebook']:,}")
            if "images" in translation_types and est.get("images", 0):
                parts.append(f"images: {est['images']:,}")
            if (
                "markdown" in translation_types or "notebook" in translation_types
            ) and est.get("outdated", 0):
                parts.append(f"retranslation: {est['outdated']:,}")
            breakdown = ", ".join(parts) if parts else "none"
            if emit_estimate:
                click.echo(
                    "📊 Estimated translation volume before translation: "
                    f"{estimated_words['total']:,} words (≈ {estimated_tokens['total']:,} tokens) "
                    f"(breakdown: {breakdown})"
                )
        except Exception as e:  # pragma: no cover - best-effort logging only
            logger.debug(f"Failed to compute estimated tokens: {e}")

        if dry_run:
            click.echo("🧪 Dry run complete: no changes made.")
            return {
                **estimated_tokens,
                "words": estimated_words["total"],
            }

        translator.translate_project(
            update=update,
        )

        logger.info(f"Project translation completed for languages: {language_codes}")
        return {
            **estimated_tokens,
            "words": estimated_words["total"],
        }

    def _merge_estimates(
        current: dict[str, int],
        incoming: dict[str, int],
    ) -> dict[str, int]:
        merged = dict(current)
        for key in ("markdown", "notebook", "images", "outdated", "total", "words"):
            merged[key] = int(merged.get(key, 0)) + int(incoming.get(key, 0))
        return merged

    def _echo_estimate_summary(
        est: dict[str, int],
        translation_types: list[str],
    ) -> None:
        parts: list[str] = []
        if "markdown" in translation_types and est.get("markdown", 0):
            parts.append(f"markdown: {est['markdown']:,}")
        if "notebook" in translation_types and est.get("notebook", 0):
            parts.append(f"notebook: {est['notebook']:,}")
        if "images" in translation_types and est.get("images", 0):
            parts.append(f"images: {est['images']:,}")
        if (
            "markdown" in translation_types or "notebook" in translation_types
        ) and est.get("outdated", 0):
            parts.append(f"retranslation: {est['outdated']:,}")
        breakdown = ", ".join(parts) if parts else "none"
        click.echo(
            "📊 Estimated translation volume before translation: "
            f"{est.get('words', 0):,} words (≈ {est.get('total', 0):,} tokens) "
            f"(breakdown: {breakdown})"
        )

    aggregate_template = {
        "markdown": 0,
        "notebook": 0,
        "images": 0,
        "outdated": 0,
        "total": 0,
        "words": 0,
    }
    translation_types_for_summary: list[str] = []
    if markdown:
        translation_types_for_summary.append("markdown")
    if images:
        translation_types_for_summary.append("images")
    if notebook:
        translation_types_for_summary.append("notebook")
    if not translation_types_for_summary:
        translation_types_for_summary = ["markdown", "notebook", "images"]

    if groups is not None:
        groups_list = list(groups)
        emit_per_group_estimate = not (dry_run and len(groups_list) > 1)
        aggregated_estimate = dict(aggregate_template)

        for per_root, per_translations in groups_list:
            per_translations_dir: str | None = per_translations
            per_lang_subdir: str | None = None

            if per_translations is not None:
                base_part, suffix = _split_lang_placeholder(per_translations)
                per_translations_dir = base_part or None
                per_lang_subdir = suffix

            per_group_estimate = _run_single_group(
                language_codes=language_codes,
                root_dir=per_root,
                update=update,
                images=images,
                markdown=markdown,
                notebook=notebook,
                debug=debug,
                save_logs=save_logs,
                yes=yes,
                glossaries=glossaries,
                add_disclaimer=add_disclaimer,
                translations_dir=per_translations_dir,
                image_dir=image_dir,
                lang_subdir=per_lang_subdir,
                repo_url=repo_url,
                dry_run=dry_run,
                emit_estimate=emit_per_group_estimate,
            )

            if dry_run and len(groups_list) > 1:
                aggregated_estimate = _merge_estimates(
                    aggregated_estimate, per_group_estimate
                )

        if dry_run and len(groups_list) > 1:
            _echo_estimate_summary(aggregated_estimate, translation_types_for_summary)
        return

    if root_dirs is not None:
        root_dirs_list = list(root_dirs)
        emit_per_root_estimate = not (dry_run and len(root_dirs_list) > 1)
        aggregated_estimate = dict(aggregate_template)

        for per_root in root_dirs_list:
            per_root_estimate = _run_single_group(
                language_codes=language_codes,
                root_dir=per_root,
                update=update,
                images=images,
                markdown=markdown,
                notebook=notebook,
                debug=debug,
                save_logs=save_logs,
                yes=yes,
                glossaries=glossaries,
                add_disclaimer=add_disclaimer,
                translations_dir=translations_dir,
                image_dir=image_dir,
                lang_subdir=None,
                repo_url=repo_url,
                dry_run=dry_run,
                emit_estimate=emit_per_root_estimate,
            )

            if dry_run and len(root_dirs_list) > 1:
                aggregated_estimate = _merge_estimates(
                    aggregated_estimate, per_root_estimate
                )

        if dry_run and len(root_dirs_list) > 1:
            _echo_estimate_summary(aggregated_estimate, translation_types_for_summary)
        return

    _run_single_group(
        language_codes=language_codes,
        root_dir=root_dir,
        update=update,
        images=images,
        markdown=markdown,
        notebook=notebook,
        debug=debug,
        save_logs=save_logs,
        yes=yes,
        glossaries=glossaries,
        add_disclaimer=add_disclaimer,
        translations_dir=translations_dir,
        image_dir=image_dir,
        lang_subdir=None,
        repo_url=repo_url,
        dry_run=dry_run,
        emit_estimate=True,
    )
