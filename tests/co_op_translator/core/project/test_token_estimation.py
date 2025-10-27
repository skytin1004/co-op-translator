import json
from pathlib import Path

from co_op_translator.core.project.translation_manager import TranslationManager
from co_op_translator.config.constants import (
    EXCLUDED_DIRS,
    SUPPORTED_IMAGE_EXTENSIONS,
    SUPPORTED_NOTEBOOK_EXTENSIONS,
)
from co_op_translator.utils.llm.token_utils import count_tokens


def _make_manager(
    root: Path, languages: list[str], types: list[str]
) -> TranslationManager:
    translations_dir = root / "translations"
    image_dir = root / "translated_images"
    translations_dir.mkdir(parents=True, exist_ok=True)
    image_dir.mkdir(parents=True, exist_ok=True)

    # We don't use translators in estimation; pass minimal placeholders
    markdown_translator = None  # type: ignore
    image_translator = None
    notebook_translator = None

    return TranslationManager(
        root,
        translations_dir,
        image_dir,
        languages,
        EXCLUDED_DIRS,
        SUPPORTED_IMAGE_EXTENSIONS,
        SUPPORTED_NOTEBOOK_EXTENSIONS,
        markdown_translator,  # type: ignore
        image_translator,
        notebook_translator,
        types,
    )


def test_estimate_tokens_markdown_only(tmp_path: Path):
    root = tmp_path
    # Create a simple markdown file
    md = root / "README.md"
    content = "Hello world! This is a small test."
    md.write_text(content, encoding="utf-8")

    mgr = _make_manager(root, ["ko", "ja"], ["markdown"])  # two languages
    est = mgr.estimate_tokens(update=False)

    expected = count_tokens(content) * 2

    assert est["markdown"] == expected
    assert est["notebook"] == 0
    assert est["outdated"] == 0
    assert est["total"] == expected


def test_estimate_tokens_notebook_only(tmp_path: Path):
    root = tmp_path
    # Create a simple notebook (.ipynb) file with some text in cells
    nb = root / "example.ipynb"
    nb_content = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["Notebook example text for token estimation."],
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    nb.write_text(json.dumps(nb_content), encoding="utf-8")

    mgr = _make_manager(root, ["fr", "de", "es"], ["notebook"])  # three languages
    est = mgr.estimate_tokens(update=False)

    # Use raw file text because that's what read_input_file() reads
    text = nb.read_text(encoding="utf-8")
    expected = count_tokens(text) * 3

    assert est["markdown"] == 0
    assert est["notebook"] == expected
    assert est["outdated"] == 0
    assert est["total"] == expected
