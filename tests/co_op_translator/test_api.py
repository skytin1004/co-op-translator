from unittest.mock import MagicMock

import pytest

from co_op_translator.api import translation as api


@pytest.mark.asyncio
async def test_run_translation_calls_project_translator(tmp_path):
    root_dir = tmp_path

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko ja",
        root_dir=str(root_dir),
        update=False,
        images=False,
        markdown=True,
        notebook=False,
        debug=False,
        save_logs=False,
        yes=True,
    )

    assert project_translator_class.call_count == 2
    project_translator_class.assert_any_call(
        "ko ja",
        str(root_dir),
        translation_types=["markdown"],
        add_disclaimer=False,
        translations_dir=None,
        image_dir=None,
        lang_subdir=None,
    )
    project_translator_instance.translate_project.assert_called_once_with(
        update=False,
    )


@pytest.mark.asyncio
async def test_run_translation_with_disclaimer_flag(tmp_path):
    root_dir = tmp_path

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko",
        root_dir=str(root_dir),
        markdown=True,
        add_disclaimer=True,
    )

    assert project_translator_class.call_count == 2
    project_translator_class.assert_any_call(
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

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    api.run_translation(
        language_codes="ko",
        markdown=True,
        root_dirs=[str(root1), str(root2)],
    )

    assert project_translator_class.call_count == 4
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

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    project_translator_instance = MagicMock()
    project_translator_class = MagicMock(return_value=project_translator_instance)
    api.ProjectTranslator = project_translator_class

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    api.run_translation(
        language_codes="ko",
        markdown=True,
        groups=groups,
    )

    assert project_translator_class.call_count == 4
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

    api.Config.check_configuration = MagicMock(return_value=None)
    api.LLMConfig.validate_connectivity = MagicMock(return_value=None)
    api.setup_logging = MagicMock(return_value=None)

    translators = [MagicMock() for _ in range(4)]
    api.ProjectTranslator = MagicMock(side_effect=translators)

    api.estimate_translation_tokens = MagicMock(
        side_effect=[
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated_markdown": 0,
                "outdated_notebook": 0,
                "outdated_images": 0,
                "outdated": 0,
                "total": 65,
            },
            {
                "markdown": 65,
                "notebook": 0,
                "images": 0,
                "outdated_markdown": 0,
                "outdated_notebook": 0,
                "outdated_images": 0,
                "outdated": 0,
                "total": 65,
            },
        ]
    )
    api.estimate_translation_words = MagicMock(
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
    api.click.echo = echo_mock

    groups = [
        (str(root1), str(out1)),
        (str(root2), str(out2)),
    ]

    api.run_translation(
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
    grouped_progress_lines = [
        call.args[0]
        for call in echo_mock.call_args_list
        if call.args and "Translating all groups" in call.args[0]
    ]
    assert grouped_progress_lines == []
    assert (
        estimate_lines[0]
        == "📊 Estimated translation volume before translation: 130 tokens (80 words) "
        "(breakdown: translation: markdown: 130 | retranslation: outdated markdowns: 0)"
    )
