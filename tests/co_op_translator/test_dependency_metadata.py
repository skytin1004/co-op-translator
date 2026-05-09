from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
PYPROJECT = ROOT_DIR / "pyproject.toml"

IMAGE_DEPENDENCIES = {
    "arabic-reshaper",
    "azure-ai-vision-imageanalysis",
    "azure-core",
    "matplotlib",
    "numpy",
    "opencv-python",
    "pillow",
    "python-bidi",
}


def _section_text(header: str) -> str:
    lines = PYPROJECT.read_text(encoding="utf-8").splitlines()
    start = lines.index(header)
    body: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("[") and line.endswith("]"):
            break
        body.append(line)
    return "\n".join(body)


def test_image_dependencies_are_optional_extras() -> None:
    dependencies = _section_text("[tool.poetry.dependencies]")
    extras = _section_text("[tool.poetry.extras]")

    for dependency in IMAGE_DEPENDENCIES:
        matching_lines = [
            line for line in dependencies.splitlines() if line.startswith(dependency)
        ]
        assert matching_lines, f"{dependency} is missing from Poetry dependencies"
        assert "optional = true" in matching_lines[0]
        assert f'"{dependency}"' in extras


def test_runtime_dependencies_do_not_pin_known_transitive_or_dev_packages() -> None:
    dependencies = _section_text("[tool.poetry.dependencies]")

    removed_direct_dependencies = {
        "appnope",
        "asttokens",
        "azure-cognitiveservices-vision-computervision",
        "comm",
        "jedi",
        "matplotlib-inline",
        "prompt_toolkit",
        "pyzmq",
        "stack-data",
        "traitlets",
    }
    for dependency in removed_direct_dependencies:
        assert not any(
            line.startswith(f"{dependency} ") or line.startswith(f"{dependency} =")
            for line in dependencies.splitlines()
        )


def test_core_vision_package_does_not_eager_import_azure_provider() -> None:
    provider_module = "co_op_translator.core.vision.providers.azure.image_translator"
    sys.modules.pop(provider_module, None)

    importlib.reload(importlib.import_module("co_op_translator.core.vision"))

    assert provider_module not in sys.modules
