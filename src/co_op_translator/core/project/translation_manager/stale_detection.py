"""Outdated translation detection and legacy metadata migration."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Protocol

from co_op_translator.config.constants import SUPPORTED_MARKDOWN_EXTENSIONS
from co_op_translator.utils.common.file_utils import (
    filter_files,
    generate_translated_filename,
    get_filename_and_extension,
)
from co_op_translator.utils.common.metadata_utils import (
    calculate_file_hash,
    extract_content_without_metadata,
    extract_metadata_from_content,
    is_image_up_to_date,
    is_notebook_up_to_date,
    read_text_metadata_for_source,
    save_text_metadata_for_source,
)

logger = logging.getLogger(__name__)


class StaleDetectionContext(Protocol):
    """Subset of TranslationManager state required for stale detection."""

    root_dir: Path
    translations_dir: Path
    image_dir: Path
    language_codes: list[str]
    excluded_dirs: list[str]
    supported_image_extensions: list[str]
    supported_notebook_extensions: list[str]
    lang_subdir: Path | None

    def _get_language_root(self, language_code: str) -> Path:
        """Return the output root for a target language."""
        ...


def resolve_language_root(context: StaleDetectionContext, language_code: str) -> Path:
    """Return a concrete language root even for partially mocked managers in tests."""
    try:
        lang_dir = context._get_language_root(language_code)
        if isinstance(lang_dir, Path):
            return lang_dir
    except Exception:
        pass

    lang_dir = Path(context.translations_dir) / language_code
    lang_subdir = getattr(context, "lang_subdir", None)
    if isinstance(lang_subdir, (str, Path)) and str(lang_subdir):
        lang_dir = lang_dir / Path(lang_subdir)
    return lang_dir


def get_outdated_translations(
    context: StaleDetectionContext,
) -> list[tuple[Path, Path]]:
    """Identify text translations that need updates based on metadata hashes."""
    outdated_files: list[tuple[Path, Path]] = []
    all_translation_files: list[tuple[str, Path]] = []

    for lang_code in context.language_codes:
        translation_dir = resolve_language_root(context, lang_code)
        if not translation_dir.exists():
            continue
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            for md_file in translation_dir.rglob(f"*{ext}"):
                all_translation_files.append((lang_code, md_file))
        for ext in context.supported_notebook_extensions:
            for nb_file in translation_dir.rglob(f"*{ext}"):
                all_translation_files.append((lang_code, nb_file))

    if not all_translation_files:
        return []

    for lang_code, trans_file in all_translation_files:
        try:
            lang_dir = resolve_language_root(context, lang_code)
            relative_path = trans_file.relative_to(lang_dir)
            original_file = context.root_dir / relative_path

            if not original_file.exists():
                continue

            if is_translation_outdated(context, original_file, trans_file):
                outdated_files.append((original_file, trans_file))
        except ValueError:
            logger.warning(f"Error calculating relative path for {trans_file}")
            continue

    return outdated_files


def get_outdated_images(
    context: StaleDetectionContext,
) -> list[tuple[Path, Path, str]]:
    """Identify translated images that need updates based on metadata hashes."""
    outdated_images: list[tuple[Path, Path, str]] = []

    image_files = filter_files(context.root_dir, context.excluded_dirs)
    original_images = [
        f.resolve()
        for f in image_files
        if get_filename_and_extension(f)[1] in context.supported_image_extensions
    ]

    if not original_images:
        return []

    for image_file_path in original_images:
        for language_code in context.language_codes:
            translated_filename = generate_translated_filename(
                image_file_path, language_code, context.root_dir
            )
            translated_image_path = (
                Path(context.image_dir) / language_code / translated_filename
            )

            if not translated_image_path.exists():
                continue

            if not is_image_up_to_date(
                image_file_path, translated_image_path, context.image_dir
            ):
                outdated_images.append(
                    (image_file_path, translated_image_path, language_code)
                )

    return outdated_images


def is_translation_outdated(
    context: StaleDetectionContext,
    original_file: Path,
    translation_file: Path,
) -> bool:
    """Determine if a translation file needs updating based on content hash."""
    if not translation_file.exists():
        return True

    try:
        if translation_file.suffix.lower() in context.supported_notebook_extensions:
            return not is_notebook_up_to_date(original_file, translation_file)

        lang_dir = None
        try:
            for language_code in context.language_codes:
                root = resolve_language_root(context, language_code)
                try:
                    translation_file.resolve().relative_to(root.resolve())
                    lang_dir = root
                    break
                except (ValueError, IndexError):
                    continue

            if not lang_dir:
                rel = translation_file.resolve().relative_to(
                    context.translations_dir.resolve()
                )
                lang_dir = context.translations_dir / rel.parts[0]
        except Exception:
            lang_dir = translation_file.parent

        try:
            source_key: str | Path = str(
                original_file.relative_to(context.root_dir)
            ).replace("\\", "/")
        except Exception:
            source_key = original_file

        metadata = read_text_metadata_for_source(lang_dir, source_key)
        if metadata and isinstance(metadata, dict):
            stored_hash = metadata.get("original_hash")
            if stored_hash:
                current_hash = calculate_file_hash(original_file)
                return stored_hash != current_hash

        try:
            content = translation_file.read_text(encoding="utf-8")
        except Exception:
            return True

        legacy_meta = extract_metadata_from_content(content)
        stored_hash = (
            legacy_meta.get("original_hash") if isinstance(legacy_meta, dict) else None
        )
        if stored_hash:
            current_hash = calculate_file_hash(original_file)
            return stored_hash != current_hash

        return True

    except Exception:
        return True


def migrate_legacy_inline_text_metadata(context: StaleDetectionContext) -> int:
    """Move legacy inline markdown metadata into centralized language metadata."""
    migrated = 0

    for lang_code in context.language_codes:
        lang_dir = resolve_language_root(context, lang_code)
        if not lang_dir.exists():
            continue

        md_files: list[Path] = []
        for ext in SUPPORTED_MARKDOWN_EXTENSIONS:
            md_files.extend(list(lang_dir.rglob(f"*{ext}")))

        for trans_file in md_files:
            try:
                rel_to_lang = trans_file.relative_to(lang_dir)
                original_file = (context.root_dir / rel_to_lang).resolve()
                if not original_file.exists():
                    continue

                try:
                    source_key: str | Path = str(
                        original_file.relative_to(context.root_dir)
                    ).replace("\\", "/")
                except Exception:
                    source_key = original_file

                existing = read_text_metadata_for_source(lang_dir, source_key)
                if isinstance(existing, dict) and existing.get("original_hash"):
                    continue

                content = trans_file.read_text(encoding="utf-8")
                legacy_meta = extract_metadata_from_content(content)
                legacy_hash = (
                    legacy_meta.get("original_hash")
                    if isinstance(legacy_meta, dict)
                    else None
                )
                if not legacy_hash:
                    continue

                extra_fields = {"original_hash": legacy_hash}
                if isinstance(legacy_meta, dict) and legacy_meta.get(
                    "translation_date"
                ):
                    extra_fields["translation_date"] = legacy_meta.get(
                        "translation_date"
                    )

                save_text_metadata_for_source(
                    lang_dir,
                    original_file,
                    lang_code,
                    root_dir=context.root_dir,
                    extra_fields=extra_fields,
                )

                cleaned = extract_content_without_metadata(content)
                if cleaned != content:
                    try:
                        trans_file.write_text(cleaned, encoding="utf-8")
                    except Exception:
                        pass

                migrated += 1
            except Exception:
                continue

    return migrated
