import warnings

from co_op_translator.config.base_config import Config
from co_op_translator.config.font_config import FontConfig
from co_op_translator.utils.common.files.readme_templates import (
    load_languages_table_template,
    load_other_courses_template,
)
from co_op_translator.utils.common.lang_utils import get_supported_language_codes
from co_op_translator.utils.common.metadata_utils import create_metadata


def test_packaged_resource_loading_is_deprecation_warning_free():
    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)

        font_config = FontConfig()
        assert font_config.get_language_name("en")
        assert font_config.get_font_path("en")
        assert get_supported_language_codes()
        assert Config.get_language_codes()
        assert load_languages_table_template()
        assert load_other_courses_template()


def test_metadata_timestamp_is_deprecation_warning_free(tmp_path):
    source_file = tmp_path / "source.md"
    source_file.write_text("# Source\n", encoding="utf-8")

    with warnings.catch_warnings():
        warnings.simplefilter("error", DeprecationWarning)
        metadata = create_metadata(source_file, "ko", tmp_path)

    assert metadata["translation_date"].endswith("+00:00")
