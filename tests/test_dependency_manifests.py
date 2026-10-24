import hashlib
from pathlib import Path
import ssl

from packaging.requirements import Requirement
from packaging.specifiers import SpecifierSet
from packaging.utils import canonicalize_name
from packaging.version import Version
import yaml

import certifi
import tomllib

REPO_ROOT = Path(__file__).resolve().parents[1]
COMPROMISED_TRUST_ANCHOR_SHA256 = {
    "86a1ecba089c4a8d3bbe2734c612ba341d813e043cf9e8a862cd5c57a36bbe6b",
    "d7a7a0fb5d7e2731d771e9484ebcdef71d5f0c3e0a2948782bc83ee0ea699ef4",
}


def _poetry_dependency_names() -> tuple[set[str], set[str]]:
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    poetry = config["tool"]["poetry"]
    runtime = set(poetry["dependencies"])
    runtime.discard("python")
    development = set(poetry["group"]["dev"]["dependencies"])
    return (
        {canonicalize_name(name) for name in runtime},
        {canonicalize_name(name) for name in development},
    )


def _requirements(path: Path) -> dict[str, Requirement]:
    parsed = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("#", "-r ")):
            continue
        requirement = Requirement(line)
        parsed[canonicalize_name(requirement.name)] = requirement
    return parsed


def _pinned_version(requirement: Requirement) -> Version:
    pins = [
        Version(specifier.version)
        for specifier in requirement.specifier
        if specifier.operator == "=="
    ]
    assert len(pins) == 1, f"Expected one exact pin for {requirement.name}"
    return pins[0]


def test_direct_dependencies_are_present_in_requirements_files():
    runtime_names, development_names = _poetry_dependency_names()
    runtime_requirements = _requirements(REPO_ROOT / "requirements.txt")
    development_requirements = _requirements(REPO_ROOT / "requirements-dev.txt")

    assert runtime_names <= runtime_requirements.keys()
    assert development_names <= (
        runtime_requirements.keys() | development_requirements.keys()
    )


def test_supported_python_range_matches_ci_matrix():
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    )

    assert config["tool"]["poetry"]["dependencies"]["python"] == ">=3.11,<3.15"
    assert workflow["jobs"]["test"]["strategy"]["matrix"]["python-version"] == [
        "3.11",
        "3.12",
        "3.13",
        "3.14",
    ]


def test_export_uses_modern_numpy_release():
    numpy_requirement = _requirements(REPO_ROOT / "requirements.txt")["numpy"]

    assert _pinned_version(numpy_requirement) >= Version("2.0")


def test_typing_extensions_range_supports_semantic_kernel():
    typing_requirement = _requirements(REPO_ROOT / "requirements.txt")[
        "typing-extensions"
    ]

    assert _pinned_version(typing_requirement) >= Version("4.15.0")


def test_certifi_export_rejects_compromised_emudhra_certificates():
    certifi_requirement = _requirements(REPO_ROOT / "requirements.txt")["certifi"]

    assert _pinned_version(certifi_requirement) >= Version("2026.10.19")


def test_certifi_development_export_matches_runtime_export():
    runtime_certifi = _requirements(REPO_ROOT / "requirements.txt")["certifi"]
    development_certifi = _requirements(REPO_ROOT / "requirements-dev.txt")["certifi"]

    assert _pinned_version(development_certifi) == _pinned_version(runtime_certifi)


def test_certifi_lock_rejects_compromised_emudhra_certificates():
    lock = tomllib.loads((REPO_ROOT / "poetry.lock").read_text(encoding="utf-8"))
    certifi_package = next(
        package for package in lock["package"] if package["name"] == "certifi"
    )

    assert Version(certifi_package["version"]) >= Version("2026.10.19")


def test_certifi_poetry_constraint_rejects_vulnerable_versions():
    config = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))
    certifi_constraint = SpecifierSet(
        config["tool"]["poetry"]["dependencies"]["certifi"]
    )

    assert Version("2026.10.19") in certifi_constraint
    assert Version("2026.10.18") not in certifi_constraint


def test_installed_certifi_bundle_distrusts_compromised_emudhra_root():
    context = ssl.create_default_context(cafile=certifi.where())
    fingerprints = {
        hashlib.sha256(certificate).hexdigest()
        for certificate in context.get_ca_certs(binary_form=True)
    }

    assert COMPROMISED_TRUST_ANCHOR_SHA256.isdisjoint(fingerprints)


def test_docker_build_refreshes_system_and_python_ca_stores():
    dockerfile = (REPO_ROOT / "Dockerfile").read_text(encoding="utf-8")

    assert dockerfile.count("ca-certificates") >= 2
    assert "pip-26.2.2-py3-none-any.whl" in dockerfile
    assert (
        "sha256=fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70"
        in dockerfile
    )
    assert "pip==26.2.2 /tmp/*.whl" in dockerfile


def test_docker_publish_forces_a_fresh_base_and_uncached_rebuild():
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github" / "workflows" / "docker-publish.yml").read_text(
            encoding="utf-8"
        )
    )
    build_step = next(
        step
        for step in workflow["jobs"]["build-and-push"]["steps"]
        if str(step.get("uses", "")).startswith("docker/build-push-action@")
    )

    assert build_step["with"]["pull"] is True
    assert build_step["with"]["no-cache"] is True


def test_ci_bootstraps_patched_pip_before_installing_dependencies():
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    )

    for job_name in ("requirements", "test"):
        commands = "\n".join(
            str(step.get("run", "")) for step in workflow["jobs"][job_name]["steps"]
        )
        assert "pip-26.2.2-py3-none-any.whl" in commands
        assert (
            "sha256=fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70"
            in commands
        )
        assert "pip install --upgrade pip" not in commands


def test_ci_builds_and_smoke_tests_the_runtime_container():
    workflow = yaml.safe_load(
        (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    )
    container_steps = workflow["jobs"]["container"]["steps"]
    build_step = next(
        step
        for step in container_steps
        if str(step.get("uses", "")).startswith("docker/build-push-action@")
    )
    arm_build_step = next(
        step
        for step in container_steps
        if step.get("name") == "Build fresh ARM64 runtime image"
    )
    commands = "\n".join(str(step.get("run", "")) for step in container_steps)

    assert build_step["with"]["load"] is True
    assert build_step["with"]["pull"] is True
    assert build_step["with"]["no-cache"] is True
    assert all(
        fingerprint in commands for fingerprint in COMPROMISED_TRUST_ANCHOR_SHA256
    )
    assert arm_build_step["with"]["platforms"] == "linux/arm64"
    assert arm_build_step["with"]["pull"] is True
    assert arm_build_step["with"]["no-cache"] is True
    assert "--dry-run" in commands


def test_ai_sdk_exports_are_on_current_compatible_generations():
    requirements = _requirements(REPO_ROOT / "requirements.txt")

    assert Version("2.25") <= _pinned_version(requirements["openai"]) < Version("3")
    assert _pinned_version(requirements["semantic-kernel"]) >= Version("1.44.1")
    assert _pinned_version(requirements["agent-framework-core"]) >= Version("1.16.0")
    assert _pinned_version(requirements["agent-framework-openai"]) >= Version("1.14.1")


def test_agent_framework_provider_exports_match_runtime_support():
    runtime = _requirements(REPO_ROOT / "requirements.txt")
    development = _requirements(REPO_ROOT / "requirements-dev.txt")

    assert "agent-framework-anthropic" in runtime
    assert "agent-framework-ollama" not in runtime
    assert "agent-framework-ollama" in development


def test_runtime_export_preserves_required_extras():
    requirements = _requirements(REPO_ROOT / "requirements.txt")

    assert requirements["az-ai-healthcheck"].extras == {"vision"}
    assert requirements["pyjwt"].extras == {"crypto"}
