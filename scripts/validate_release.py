from __future__ import annotations

import argparse
import re
import sys
import tarfile
import zipfile
from pathlib import Path


class ReleaseValidationError(ValueError):
    """Raised when release metadata is not safe to publish."""


_VERSION_LINE_RE = re.compile(r'^version\s*=\s*"(?P<version>[^"]+)"\s*$')
_TAG_RE = re.compile(r"^v(?P<version>[0-9][0-9A-Za-z.!+_-]*)$")
_VERSION_METADATA_RE = re.compile(r"(?m)^Version:\s*(?P<version>[^\r\n]+)\s*$")
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
_PLACEHOLDER_RE = re.compile(
    r"\b(todo|tbd|describe|release notes here|changes here)\b",
    re.IGNORECASE,
)


def read_pyproject_version(pyproject_path: Path) -> str:
    """Read the Poetry package version from pyproject.toml."""
    in_poetry_section = False
    for raw_line in pyproject_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line == "[tool.poetry]":
            in_poetry_section = True
            continue
        if in_poetry_section and line.startswith("[") and line.endswith("]"):
            break
        if not in_poetry_section:
            continue

        match = _VERSION_LINE_RE.match(line)
        if match:
            return match.group("version")

    raise ReleaseValidationError(
        f"Could not find [tool.poetry] version in {pyproject_path}"
    )


def release_version_from_tag(tag: str) -> str:
    """Return the package version encoded by a release tag like v1.2.3."""
    match = _TAG_RE.match(tag.strip())
    if not match:
        raise ReleaseValidationError(
            f"Release tag must use the v<version> format, got {tag!r}."
        )
    return match.group("version")


def _meaningful_text(value: str) -> str:
    return _HTML_COMMENT_RE.sub("", value or "").strip()


def validate_release_notes(release_name: str | None, release_body: str | None) -> None:
    """Reject empty or placeholder-only GitHub release metadata."""
    if release_name is not None and not _meaningful_text(release_name):
        raise ReleaseValidationError("GitHub release name must not be empty.")

    if release_body is None:
        return

    body = _meaningful_text(release_body)
    if len(body) < 20:
        raise ReleaseValidationError(
            "GitHub release notes must contain at least one meaningful sentence."
        )
    if _PLACEHOLDER_RE.search(body):
        raise ReleaseValidationError(
            "GitHub release notes still look like a placeholder."
        )


def _version_from_metadata(metadata: str, artifact: Path) -> str:
    match = _VERSION_METADATA_RE.search(metadata)
    if not match:
        raise ReleaseValidationError(f"Could not read Version metadata from {artifact}")
    return match.group("version").strip()


def _wheel_version(wheel_path: Path) -> str:
    with zipfile.ZipFile(wheel_path) as archive:
        metadata_names = [
            name for name in archive.namelist() if name.endswith(".dist-info/METADATA")
        ]
        if not metadata_names:
            raise ReleaseValidationError(f"Wheel has no METADATA file: {wheel_path}")
        metadata = archive.read(metadata_names[0]).decode("utf-8")
    return _version_from_metadata(metadata, wheel_path)


def _sdist_version(sdist_path: Path) -> str:
    with tarfile.open(sdist_path, "r:gz") as archive:
        metadata_names = [
            member
            for member in archive.getmembers()
            if member.name.endswith("PKG-INFO")
        ]
        if not metadata_names:
            raise ReleaseValidationError(f"Source dist has no PKG-INFO: {sdist_path}")
        extracted = archive.extractfile(metadata_names[0])
        if extracted is None:
            raise ReleaseValidationError(f"Could not read PKG-INFO from {sdist_path}")
        metadata = extracted.read().decode("utf-8")
    return _version_from_metadata(metadata, sdist_path)


def validate_dist_versions(dist_dir: Path, expected_version: str) -> None:
    """Ensure built package artifacts all carry the release version."""
    artifacts = sorted(dist_dir.glob("*.whl")) + sorted(dist_dir.glob("*.tar.gz"))
    if not artifacts:
        raise ReleaseValidationError(f"No distribution artifacts found in {dist_dir}")

    for artifact in artifacts:
        if artifact.suffix == ".whl":
            artifact_version = _wheel_version(artifact)
        elif artifact.name.endswith(".tar.gz"):
            artifact_version = _sdist_version(artifact)
        else:
            continue

        if artifact_version != expected_version:
            raise ReleaseValidationError(
                f"{artifact.name} has version {artifact_version}, "
                f"expected {expected_version}."
            )


def validate_release(
    *,
    pyproject_path: Path,
    tag: str,
    release_name: str | None = None,
    release_body: str | None = None,
    dist_dir: Path | None = None,
    skip_release_notes: bool = False,
) -> str:
    pyproject_version = read_pyproject_version(pyproject_path)
    tag_version = release_version_from_tag(tag)

    if pyproject_version != tag_version:
        raise ReleaseValidationError(
            f"Release tag {tag!r} targets version {tag_version}, "
            f"but pyproject.toml declares {pyproject_version}."
        )

    if not skip_release_notes:
        validate_release_notes(release_name, release_body)

    if dist_dir is not None:
        validate_dist_versions(dist_dir, pyproject_version)

    return pyproject_version


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate release tag, notes, and built package versions."
    )
    parser.add_argument("--pyproject", default="pyproject.toml", type=Path)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--release-name")
    parser.add_argument("--release-body")
    parser.add_argument("--dist", type=Path)
    parser.add_argument(
        "--skip-release-notes",
        action="store_true",
        help="Skip GitHub release name/body checks.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv or sys.argv[1:])
    try:
        version = validate_release(
            pyproject_path=args.pyproject,
            tag=args.tag,
            release_name=args.release_name,
            release_body=args.release_body,
            dist_dir=args.dist,
            skip_release_notes=args.skip_release_notes,
        )
    except ReleaseValidationError as exc:
        print(f"Release validation failed: {exc}", file=sys.stderr)
        return 1

    print(f"Release validation passed for version {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
