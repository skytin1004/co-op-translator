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
    # translation_types matching the CLI semantics (markdown-only here)
    project_translator_class.assert_called_once_with(
        "ko ja",
        str(root_dir),
        translation_types=["markdown"],
    )

    # And translate_project should be invoked once with the update flag
    project_translator_instance.translate_project.assert_called_once_with(
        update=False,
    )
