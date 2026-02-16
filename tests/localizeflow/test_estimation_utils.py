from pathlib import Path

from co_op_translator.localizeflow.utils.token_utils import estimate_translation_tokens
from co_op_translator.localizeflow.utils.words_utils import estimate_translation_words


class DummyManager:
    def __init__(self, root: Path):
        self.root_dir = root
        self.translation_types = ["markdown"]
        self.language_codes = ["ko"]
        self.supported_notebook_extensions = [".ipynb"]

    def get_outdated_images(self):
        return []

    def get_outdated_translations(self):
        return []

    def _gather_pending_markdown(self, update: bool = False):
        return [self.root_dir / "README.md"]

    def _gather_pending_notebooks(self, update: bool = False):
        return []


def test_estimate_translation_tokens_normalizes_breakdown(tmp_path: Path):
    readme = tmp_path / "README.md"
    readme.write_text("token estimation baseline", encoding="utf-8")
    manager = DummyManager(tmp_path)

    est = estimate_translation_tokens(manager)

    assert est["markdown"] > 0
    assert est["notebook"] == 0
    assert est["images"] == 0
    assert est["outdated_markdown"] == 0
    assert est["outdated_notebook"] == 0
    assert est["outdated_images"] == 0
    assert est["outdated"] == 0
    assert est["total"] == est["markdown"]


def test_estimate_translation_words_counts_source_words(tmp_path: Path):
    md = tmp_path / "README.md"
    md.write_text("hello world localizeflow", encoding="utf-8")
    manager = DummyManager(tmp_path)

    est = estimate_translation_words(manager)

    assert est["markdown"] == 3
    assert est["notebook"] == 0
    assert est["outdated"] == 0
    assert est["images"] == 0
    assert est["total"] == 3
