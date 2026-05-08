import json
from pathlib import Path

import pytest

from co_op_translator.core.llm.markdown_translator import MarkdownTranslator
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.core.project.project_translator import ProjectTranslator
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.utils.common.file_utils import generate_translated_filename
from co_op_translator.utils.llm.markdown_utils import SPLIT_DELIMITER


class MockPromptMarkdownTranslator(MarkdownTranslator):
    async def _run_prompt(self, prompt, index, total):
        body = prompt.split(SPLIT_DELIMITER, 1)[1]
        replacements = {
            "# Project Guide": "# 프로젝트 가이드",
            "Open the": "다음 항목 열기:",
            "[Notebook]": "[노트북]",
            "![Architecture]": "![아키텍처]",
            "# Notebook Walkthrough": "# 노트북 실습",
            "Read the": "다음 문서를 읽습니다:",
            "[Guide]": "[가이드]",
        }
        for source, translated in replacements.items():
            body = body.replace(source, translated)
        return body


class MockImageTranslator:
    def __init__(self, default_output_dir, root_dir):
        self.default_output_dir = Path(default_output_dir)
        self.root_dir = Path(root_dir)
        self.calls = []

    def translate_image(
        self, image_path, language_code, destination_path, fast_mode=False
    ):
        image_path = Path(image_path)
        destination_path = Path(destination_path)
        self.calls.append((image_path, language_code, destination_path, fast_mode))
        translated_filename = generate_translated_filename(
            image_path, language_code, self.root_dir
        )
        output_path = destination_path / language_code / translated_filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(image_path.read_bytes())
        return str(output_path)


def _write_mock_project(root_dir: Path) -> Path:
    docs_dir = root_dir / "docs"
    notebooks_dir = root_dir / "notebooks"
    images_dir = root_dir / "images"
    docs_dir.mkdir()
    notebooks_dir.mkdir()
    images_dir.mkdir()

    (docs_dir / "guide.md").write_text(
        "# Project Guide\n\n"
        "Open the [Notebook](../notebooks/demo.ipynb).\n\n"
        "![Architecture](../images/diagram.png)\n",
        encoding="utf-8",
    )
    (images_dir / "diagram.png").write_bytes(b"mock image bytes")
    (notebooks_dir / "demo.ipynb").write_text(
        json.dumps(
            {
                "cells": [
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": [
                            "# Notebook Walkthrough\n",
                            "\n",
                            "Read the [Guide](../docs/guide.md).\n",
                            "\n",
                            "![Architecture](../images/diagram.png)\n",
                        ],
                    },
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": ["print('keep me')\n"],
                    },
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            },
            ensure_ascii=False,
            indent=1,
        ),
        encoding="utf-8",
    )
    return images_dir / "diagram.png"


@pytest.mark.asyncio
async def test_project_translation_e2e_with_mocked_providers(monkeypatch, tmp_path):
    source_image = _write_mock_project(tmp_path)
    fake_image_translator = MockImageTranslator(
        tmp_path / "translated_images", tmp_path
    )

    def create_markdown_translator(
        cls, root_dir=None, translations_dir=None, image_dir=None, lang_subdir=None
    ):
        return MockPromptMarkdownTranslator(
            root_dir=root_dir,
            translations_dir=translations_dir,
            image_dir=image_dir,
            lang_subdir=lang_subdir,
        )

    monkeypatch.setattr(
        MarkdownTranslator, "create", classmethod(create_markdown_translator)
    )
    monkeypatch.setattr(TextTranslator, "create", classmethod(lambda cls: object()))
    monkeypatch.setattr(
        ImageTranslator,
        "create",
        classmethod(
            lambda cls, default_output_dir="./translated_images", root_dir=".": fake_image_translator
        ),
    )

    translator = ProjectTranslator(
        "ko",
        root_dir=tmp_path,
        translation_types=["markdown", "notebook", "images"],
        add_disclaimer=False,
    )

    total_modified, errors = (
        await translator.translation_manager.translate_project_async()
    )

    translated_image_name = generate_translated_filename(source_image, "ko", tmp_path)
    translated_image_link = f"../../../translated_images/ko/{translated_image_name}"
    translated_markdown = (
        tmp_path / "translations" / "ko" / "docs" / "guide.md"
    ).read_text(encoding="utf-8")
    translated_notebook = json.loads(
        (tmp_path / "translations" / "ko" / "notebooks" / "demo.ipynb").read_text(
            encoding="utf-8"
        )
    )
    notebook_markdown = "".join(translated_notebook["cells"][0]["source"])

    assert total_modified == 3
    assert errors == []
    assert "# 프로젝트 가이드" in translated_markdown
    assert "[노트북](../notebooks/demo.ipynb)" in translated_markdown
    assert f"![아키텍처]({translated_image_link})" in translated_markdown
    assert "# 노트북 실습" in notebook_markdown
    assert "[가이드](../docs/guide.md)" in notebook_markdown
    assert f"![아키텍처]({translated_image_link})" in notebook_markdown
    assert translated_notebook["cells"][1]["source"] == ["print('keep me')\n"]
    assert (tmp_path / "translated_images" / "ko" / translated_image_name).exists()
    assert fake_image_translator.calls == [
        (source_image.resolve(), "ko", tmp_path / "translated_images", False)
    ]
