from __future__ import annotations

import subprocess
from pathlib import Path

SOURCE_EXTENSIONS = {".md", ".mdx", ".ipynb"}
DEFAULT_EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "dist",
    "htmlcov",
    "logs",
    "node_modules",
    "site",
    "translated_images",
    "translations",
    "venv",
}


def is_source_file(path: Path) -> bool:
    return path.suffix.lower() in SOURCE_EXTENSIONS


def is_excluded(path: Path, excluded_dirs: set[str]) -> bool:
    return any(part in excluded_dirs for part in path.parts)


def discover_languages(root_dir: Path) -> list[str]:
    translations_dir = root_dir / "translations"
    if not translations_dir.is_dir():
        return []
    return sorted(
        path.name
        for path in translations_dir.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )


def discover_source_files(root_dir: Path, excluded_dirs: set[str]) -> list[Path]:
    files: list[Path] = []
    for path in root_dir.rglob("*"):
        if not path.is_file() or not is_source_file(path):
            continue
        relative_path = path.relative_to(root_dir)
        if is_excluded(relative_path, excluded_dirs):
            continue
        files.append(path)
    return sorted(files)


def discover_changed_source_files(
    root_dir: Path, changed_from: str, excluded_dirs: set[str]
) -> list[Path]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", f"{changed_from}...HEAD"],
        cwd=root_dir,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return discover_source_files(root_dir, excluded_dirs)

    files: list[Path] = []
    for line in result.stdout.splitlines():
        relative_path = Path(line.strip())
        if not line.strip() or not is_source_file(relative_path):
            continue
        if is_excluded(relative_path, excluded_dirs):
            continue
        full_path = root_dir / relative_path
        if full_path.is_file():
            files.append(full_path)
    return sorted(files)
