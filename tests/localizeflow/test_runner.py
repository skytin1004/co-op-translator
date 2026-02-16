from unittest.mock import MagicMock

import pytest

from co_op_translator.localizeflow import runner


@pytest.mark.asyncio
async def test_run_translation_calls_project_translator_and_sets_glossaries(tmp_path):
    """run_translation should set glossaries and delegate to ProjectTranslator.

    This test avoids real network/API calls by patching configuration checks,
    logging setup, and ProjectTranslator, and focuses on wiring/arguments.
    """

    # Ensure the temporary directory exists and use it as root_dir
    root_dir = tmp_path

    # Patch configuration and health checks to no-op
    runner.Config.check_configuration = MagicMock(return_value=None)
    runner.LLMConfig.validate_connectivity = MagicMock(return_value=None)

    # Avoid real logging setup
    runner.setup_logging = MagicMock(return_value=None)

    # Patch glossary setter to observe calls
    set_glossaries_mock = MagicMock()
    runner.set_glossaries = set_glossaries_mock

    # Patch ProjectTranslator to avoid touching real translators
    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    runner.ProjectTranslator = project_translator_class

    # Execute: markdown-only, no images/notebooks, with glossaries
    runner.run_translation(
        language_codes="ko ja",
        root_dir=str(root_dir),
        update=False,
        images=False,
        markdown=True,
        notebook=False,
        debug=False,
        save_logs=False,
        yes=True,
        glossaries=["PR", "Issue"],
    )

    # Glossaries should be applied once with the provided list
    set_glossaries_mock.assert_called_once_with(["PR", "Issue"])

    # ProjectTranslator should be constructed with language codes, root_dir, and
    # translation_types matching the CLI semantics (markdown-only here), with
    # disclaimers disabled for Localizeflow and default output dirs.
    project_translator_class.assert_called_once_with(
        "ko ja",
        str(root_dir),
        translation_types=["markdown"],
        add_disclaimer=False,
        translations_dir=None,
        image_dir=None,
        lang_subdir=None,
    )

    # And translate_project should be invoked once with the update flag
    project_translator_instance.translate_project.assert_called_once_with(
        update=False,
    )


@pytest.mark.asyncio
async def test_run_translation_with_disclaimer_flag(tmp_path):
    root_dir = tmp_path

    runner.Config.check_configuration = MagicMock(return_value=None)
    runner.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    runner.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    runner.ProjectTranslator = project_translator_class

    runner.run_translation(
        language_codes="ko",
        root_dir=str(root_dir),
        markdown=True,
        add_disclaimer=True,
    )

    project_translator_class.assert_called_once_with(
        "ko",
        str(root_dir),
        translation_types=["markdown"],
        add_disclaimer=True,
        translations_dir=None,
        image_dir=None,
        lang_subdir=None,
    )


@pytest.mark.asyncio
async def test_run_translation_with_multiple_root_dirs(tmp_path):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    root1.mkdir()
    root2.mkdir()

    runner.Config.check_configuration = MagicMock(return_value=None)
    runner.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    runner.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    runner.ProjectTranslator = project_translator_class

    runner.run_translation(
        language_codes="ko",
        markdown=True,
        root_dirs=[str(root1), str(root2)],
    )

    assert project_translator_class.call_count == 2
    called_roots = {call.args[1] for call in project_translator_class.call_args_list}
    assert called_roots == {str(root1), str(root2)}


@pytest.mark.asyncio
async def test_run_translation_with_groups(tmp_path):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    out1 = tmp_path / "out1"
    out2 = tmp_path / "out2"
    root1.mkdir()
    root2.mkdir()
    out1.mkdir()
    out2.mkdir()

    runner.Config.check_configuration = MagicMock(return_value=None)
    runner.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    runner.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    runner.ProjectTranslator = project_translator_class

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    runner.run_translation(
        language_codes="ko",
        markdown=True,
        groups=groups,
    )

    assert project_translator_class.call_count == 2
    called = {
        (call.args[1], call.kwargs["translations_dir"])
        for call in project_translator_class.call_args_list
    }
    assert called == {(str(root1), str(out1)), (str(root2), str(out2))}


@pytest.mark.asyncio
async def test_run_translation_dry_run_groups_shows_single_aggregated_estimate(
    tmp_path,
):
    root1 = tmp_path / "content1"
    root2 = tmp_path / "content2"
    out1 = tmp_path / "out1"
    out2 = tmp_path / "out2"
    root1.mkdir()
    root2.mkdir()
    out1.mkdir()
    out2.mkdir()

    runner.Config.check_configuration = MagicMock(return_value=None)
    runner.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    runner.setup_logging = MagicMock(return_value=None)

    translator_1 = MagicMock()
    translator_2 = MagicMock()
    runner.ProjectTranslator = MagicMock(side_effect=[translator_1, translator_2])

    runner.estimate_translation_tokens = MagicMock(
        side_effect=[
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 65,
            },
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 65,
            },
        ]
    )
    runner.estimate_translation_words = MagicMock(
        side_effect=[
            {
                "markdown": 40,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 40,
            },
            {
                "markdown": 40,
                "notebook": 0,
                "images": 0,
                "outdated": 0,
                "total": 40,
            },
        ]
    )

    echo_mock = MagicMock()
    runner.click.echo = echo_mock

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    runner.run_translation(
        language_codes="ko",
        markdown=True,
        groups=groups,
        dry_run=True,
    )

    estimate_lines = [
        call.args[0]
        for call in echo_mock.call_args_list
        if call.args
        and "Estimated translation volume before translation" in call.args[0]
    ]
    assert len(estimate_lines) == 1
    assert (
        estimate_lines[0]
        == "📊 Estimated translation volume before translation: 130 tokens (80 words) "
        "(breakdown: translation: markdown: 130 | retranslation: outdated markdowns: 0)"
    )
