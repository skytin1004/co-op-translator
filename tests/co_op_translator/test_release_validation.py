from __future__ import annotations

import importlib.util
import tarfile
import zipfile
from pathlib import Path

import pytest

ROOT_DIR = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT_DIR / "scripts" / "validate_release.py"

spec = importlib.util.spec_from_file_location("validate_release", SCRIPT_PATH)
validate_release_module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validate_release_module)


ReleaseValidationError = validate_release_module.ReleaseValidationError
validate_release = validate_release_module.validate_release


def _write_pyproject(tmp_path: Path, version: str) -> Path:
    pyproject_path = tmp_path / "pyproject.toml"
    pyproject_path.write_text(
        "\n".join(
            [
                "[tool.poetry]",
                'name = "co_op_translator"',
                f'version = "{version}"',
                "",
                "[tool.poetry.dependencies]",
                'python = ">=3.10,<3.13"',
            ]
        ),
        encoding="utf-8",
    )
    return pyproject_path


def _write_wheel(dist_dir: Path, version: str) -> None:
    with zipfile.ZipFile(
        dist_dir / "co_op_translator-1.2.3-py3-none-any.whl", "w"
    ) as archive:
        archive.writestr(
            "co_op_translator-1.2.3.dist-info/METADATA",
            f"Name: co-op-translator\nVersion: {version}\n",
        )


def _write_sdist(dist_dir: Path, version: str) -> None:
    with tarfile.open(dist_dir / "co_op_translator-1.2.3.tar.gz", "w:gz") as archive:
        metadata = f"Name: co-op-translator\nVersion: {version}\n".encode("utf-8")
        info = tarfile.TarInfo("co_op_translator-1.2.3/PKG-INFO")
        info.size = len(metadata)
        from io import BytesIO

        archive.addfile(info, BytesIO(metadata))


def test_release_validation_accepts_matching_tag_and_notes(tmp_path: Path) -> None:
    pyproject_path = _write_pyproject(tmp_path, "1.2.3")

    version = validate_release(
        pyproject_path=pyproject_path,
        tag="v1.2.3",
        release_name="Co-op Translator v1.2.3",
        release_body="- Adds release validation before publishing packages.",
    )

    assert version == "1.2.3"


def test_release_validation_rejects_version_tag_mismatch(tmp_path: Path) -> None:
    pyproject_path = _write_pyproject(tmp_path, "1.2.3")

    with pytest.raises(ReleaseValidationError, match="pyproject.toml declares 1.2.3"):
        validate_release(
            pyproject_path=pyproject_path,
            tag="v1.2.4",
            skip_release_notes=True,
        )


def test_release_validation_rejects_placeholder_release_notes(tmp_path: Path) -> None:
    pyproject_path = _write_pyproject(tmp_path, "1.2.3")

    with pytest.raises(ReleaseValidationError, match="meaningful sentence"):
        validate_release(
            pyproject_path=pyproject_path,
            tag="v1.2.3",
            release_name="Co-op Translator v1.2.3",
            release_body="<!-- Describe changes here -->",
        )


def test_release_validation_checks_built_artifact_versions(tmp_path: Path) -> None:
    pyproject_path = _write_pyproject(tmp_path, "1.2.3")
    dist_dir = tmp_path / "dist"
    dist_dir.mkdir()
    _write_wheel(dist_dir, "1.2.3")
    _write_sdist(dist_dir, "1.2.3")

    validate_release(
        pyproject_path=pyproject_path,
        tag="v1.2.3",
        dist_dir=dist_dir,
        skip_release_notes=True,
    )


def test_release_validation_rejects_artifact_version_mismatch(tmp_path: Path) -> None:
    pyproject_path = _write_pyproject(tmp_path, "1.2.3")
    dist_dir = tmp_path / "dist"
    dist_dir.mkdir()
    _write_wheel(dist_dir, "1.2.4")

    with pytest.raises(ReleaseValidationError, match="expected 1.2.3"):
        validate_release(
            pyproject_path=pyproject_path,
            tag="v1.2.3",
            dist_dir=dist_dir,
            skip_release_notes=True,
        )
