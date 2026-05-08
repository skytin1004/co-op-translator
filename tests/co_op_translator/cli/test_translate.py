from unittest.mock import MagicMock

from click.testing import CliRunner

from co_op_translator.cli import translate as cli_translate
from co_op_translator.glossary import get_glossary_terms, set_glossary_terms


def test_translate_cli_help_includes_glossary_option():
    result = CliRunner().invoke(cli_translate.translate_command, ["--help"])

    assert result.exit_code == 0
    assert "--glossary" in result.output
    assert "-g" in result.output


def test_translate_cli_accepts_glossaries_and_restores_previous_terms(
    tmp_path, monkeypatch
):
    monkeypatch.setattr(
        cli_translate.Config,
        "check_configuration",
        MagicMock(return_value=None),
    )
    monkeypatch.setattr(
        cli_translate.LLMConfig,
        "validate_connectivity",
        MagicMock(return_value=None),
    )
    monkeypatch.setattr(cli_translate, "setup_logging", MagicMock(return_value=None))
    monkeypatch.setattr(
        cli_translate,
        "update_readme_languages_table",
        MagicMock(return_value=False),
    )
    monkeypatch.setattr(
        cli_translate,
        "update_readme_other_courses",
        MagicMock(return_value=False),
    )

    migrator = MagicMock()
    migrator.detect_alias_folders.return_value = []
    monkeypatch.setattr(
        cli_translate,
        "LanguageFolderMigrator",
        MagicMock(return_value=migrator),
    )

    observed_terms: list[list[str]] = []

    def fake_estimate_tokens(*args, **kwargs):
        observed_terms.append(get_glossary_terms())
        return {
            "markdown": 10,
            "notebook": 0,
            "images": 0,
            "outdated_markdown": 0,
            "outdated_notebook": 0,
            "outdated_images": 0,
            "outdated": 0,
            "total": 10,
        }

    translator = MagicMock()
    translator.translation_manager.estimate_tokens.side_effect = fake_estimate_tokens
    monkeypatch.setattr(
        cli_translate,
        "ProjectTranslator",
        MagicMock(return_value=translator),
    )

    set_glossary_terms(["Existing Term"])
    try:
        result = CliRunner().invoke(
            cli_translate.translate_command,
            [
                "-l",
                "ko",
                "-r",
                str(tmp_path),
                "-md",
                "-y",
                "--glossary",
                " Co-op Translator ",
                "-g",
                "Co-op Translator",
                "-g",
                "Azure AI",
            ],
        )

        assert result.exit_code == 0, result.output
        assert observed_terms == [["Co-op Translator", "Azure AI"]]
        assert get_glossary_terms() == ["Existing Term"]
        translator.translate_project.assert_called_once_with(
            update=False,
            fast_mode=False,
        )
    finally:
        set_glossary_terms([])
