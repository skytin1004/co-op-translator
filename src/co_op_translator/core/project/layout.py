"""Output layout helpers for translated project artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OutputLayout:
    """Resolved output paths for a translation run."""

    root_dir: Path
    translations_dir: Path
    image_dir: Path
    lang_subdir: Path | None = None

    @classmethod
    def from_paths(
        cls,
        *,
        root_dir: str | Path = ".",
        translations_dir: str | Path | None = None,
        image_dir: str | Path | None = None,
        lang_subdir: str | Path | None = None,
    ) -> "OutputLayout":
        root = Path(root_dir).resolve()
        resolved_translations = cls._resolve_optional_output_dir(
            root, translations_dir, default="translations"
        )
        resolved_images = cls._resolve_optional_output_dir(
            root, image_dir, default="translated_images"
        )
        resolved_lang_subdir = Path(lang_subdir) if lang_subdir else None
        return cls(
            root_dir=root,
            translations_dir=resolved_translations,
            image_dir=resolved_images,
            lang_subdir=resolved_lang_subdir,
        )

    @staticmethod
    def _resolve_optional_output_dir(
        root_dir: Path,
        value: str | Path | None,
        *,
        default: str,
    ) -> Path:
        if value is None:
            return root_dir / default

        path = Path(value)
        if path.is_absolute():
            return path.resolve()
        return (root_dir / path).resolve()

    def language_root(self, language_code: str) -> Path:
        """Return the text translation root for a language."""
        lang_dir = self.translations_dir / language_code
        if self.lang_subdir:
            lang_dir = lang_dir / self.lang_subdir
        return lang_dir
