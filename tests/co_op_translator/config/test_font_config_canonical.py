import pytest
import yaml
from pathlib import Path
from unittest.mock import MagicMock, patch

from co_op_translator.config.font_config import FontConfig

sample_yaml = """
zh-TW:
  name: Chinese (Traditional, Taiwan)
  font: "NotoSansCJK-Medium.ttc"
pt-PT:
  name: Portuguese (Portugal)
  font: "NotoSans-Medium.ttf"
pt-BR:
  name: Portuguese (Brazil)
  font: "NotoSans-Medium.ttf"
"""


def test_font_config_resolves_canonical_to_alias_keys():
    fc = FontConfig.__new__(FontConfig)
    fc.font_mappings = yaml.safe_load(sample_yaml)

    # get_font_path should resolve alias input 'tw' to canonical 'zh-TW'
    mock_package_files = MagicMock()
    mock_package_files.joinpath.return_value = Path("fake_fonts/NotoSansCJK-Medium.ttc")
    with patch(
        "importlib.resources.files", return_value=mock_package_files
    ) as mock_files:
        path = fc.get_font_path("tw")
        assert Path(path).name == "NotoSansCJK-Medium.ttc"
        mock_files.assert_called_once_with("co_op_translator.fonts")
        mock_package_files.joinpath.assert_called_once_with("NotoSansCJK-Medium.ttc")

    # get_language_name should resolve alias input 'br' to canonical 'pt-BR'
    name = fc.get_language_name("br")
    assert name == "Portuguese (Brazil)"

    # is_rtl defaults to False if not set
    assert fc.is_rtl("zh-TW") is False


def test_font_config_invalid_language_errors():
    fc = FontConfig.__new__(FontConfig)
    fc.font_mappings = yaml.safe_load(sample_yaml)

    with pytest.raises(ValueError) as excinfo:
        fc.get_language_name("xx")
    assert "Language code 'xx' is not supported." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo2:
        fc.is_rtl("xx")
    assert "Language code 'xx' is not supported." in str(excinfo2.value)
