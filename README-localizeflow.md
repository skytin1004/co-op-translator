# Localizeflow Fork Guide

This document summarizes installation and operational guidance for using the `localizeflow/localizeflow-co-op-translator` fork internally or privately. For general usage of the original project, see `README.md` and the documents under `getting_started/`.

## Installation (from a GitHub tag)

If you publish a release with a tag, you can install directly from GitHub without publishing to PyPI:

```bash
pip install git+https://github.com/localizeflow/localizeflow-co-op-translator.git@v0.11.3a1
```

- `v0.11.3a1` is an example tag. Replace it with your actual release tag.

If the repository is private, use a GitHub token:

```bash
pip install "git+https://<GITHUB_TOKEN>@github.com/localizeflow/localizeflow-co-op-translator.git@v0.11.3a1"
```

- Be careful not to leave tokens in your shell history. In CI, prefer using secrets/credential managers.

## Tagging/Versioning (recommended)

- Pre-releases: `vX.Y.ZaN` (e.g., `v0.11.3a1+lf1`) for experimental/validation releases
- Stable releases: `vX.Y.Z+lf1` for stable releases
- Add a concise change summary to the release notes for each tag to clarify installation targets.

## Keeping the fork and Localizeflow in sync

This section summarizes the recommended workflow when you:

- Pull new changes from the upstream Azure/Co-op Translator repository
- Cut a new version in this fork
- Update the Localizeflow SaaS repository to consume that new tag

### 1. Sync with upstream Azure/Co-op Translator

From your local clone of `localizeflow/localizeflow-co-op-translator`:

1. Add the upstream remote (one-time setup):

   ```bash
   git remote add upstream https://github.com/azure/co-op-translator.git
   ```

2. Fetch and merge (or rebase) the latest changes:

   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   # or: git rebase upstream/main
   ```

3. Resolve any conflicts, run tests, and push to the fork:

   ```bash
   pytest
   git push origin main
   ```

### 2. Create and tag a new fork version

After you have merged upstream changes and/or added Localizeflow-specific changes:

1. Decide the new version tag, following the conventions above, for example:

   - Pre-release: `v0.11.3a1+lf4`
   - Stable: `v0.11.4+lf1`

2. Update version metadata if needed (for example in `pyproject.toml` and/or release notes).

3. Create and push the tag:

   ```bash
   git tag v0.11.4+lf1
   git push origin v0.11.4+lf1
   ```

4. (Optional but recommended) Create a GitHub Release for this tag and summarize the key changes.

### 3. Update the Localizeflow SaaS repository

In the Localizeflow SaaS rep (https://github.com/localizeflow/localizeflow) (for example, `apps/api/pyproject.toml`):

1. Update the pinned Git dependency to point to the new tag, e.g.:

   ```toml
   localizeflow-co-op-translator = { git = "https://github.com/localizeflow/localizeflow-co-op-translator.git", tag = "v0.11.4+lf1" }
   ```

2. Regenerate the lockfile (example using Poetry):

   ```bash
   poetry update localizeflow-co-op-translator
   ```

3. Update any documentation or installation examples in the Localizeflow repo (for example in `README.md`) so that the `pip install` snippet uses the same tag:

   ```bash
   pip install git+https://github.com/localizeflow/localizeflow-co-op-translator.git@v0.11.4+lf1
   ```

4. Commit these changes together (pyproject, lockfile, README/docs) so that the version bump is clearly traceable.

This process ensures that:

- The fork stays current with the upstream Azure project
- New behavior is versioned via a clear Git tag
- The Localizeflow SaaS environment consistently uses the intended translator version

## Minimal environment variables (.env)

- At least one LLM provider required (Azure OpenAI or OpenAI)
- Azure AI Service required when using image translation (`-img`)
- Base template: see `.env.template`

Example (summary):

```bash
# Azure OpenAI (example)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# For image translation (Azure AI Service)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"
```

## Usage examples

- Only Markdown:

```bash
translate -l "ko ja" -md
```

- Markdown + image text extraction:

```bash
translate -l "pt" -md -img
```

- Only notebooks:

```bash
translate -l "zh" -nb
```

### Programmatic usage from Localizeflow

When you consume this fork from the Localizeflow SaaS repository, you can trigger
translations programmatically instead of shelling out to the `translate` CLI.

The `co_op_translator.localizeflow` namespace exposes a helper that mirrors the
CLI options and adds Localizeflow-specific glossary support:

```python
from co_op_translator.localizeflow import run_translation


run_translation(
    language_codes="ko ja",  # same syntax as -l/--language-codes
    root_dir=".",            # project root
    markdown=True,            # enable markdown translation
    images=True,              # enable image translation (requires Azure AI Service)
    notebook=False,           # enable notebook translation if needed
    debug=False,              # enable debug logging
    save_logs=True,           # write logs under <root_dir>/logs
    yes=True,                 # auto-confirm "all"/update warnings (non-interactive)
    glossaries=["PR", "Issue"],  # glossary terms to preserve as-is in translations
)
```

Notes:

- `run_translation` runs the same internal pipeline as the `translate` CLI:
  environment checks, LLM/Vision health checks, token estimation, and
  progress bars.
- When `glossaries` is provided, the terms are injected into the markdown and
  image translation prompts so that those terms are preserved in the output.

### `run_translation` API reference (Localizeflow only)

This section is a **precise API reference** for calling
`co_op_translator.localizeflow.run_translation` directly from Localizeflow SaaS
code. It is written so that LLMs and code readers can easily parse parameters,
types, and defaults.

#### Signature (summary)

```python
from co_op_translator.localizeflow import run_translation

def run_translation(
    language_codes: str,
    root_dir: str = ".",
    update: bool = False,
    images: bool = False,
    markdown: bool = False,
    notebook: bool = False,
    debug: bool = False,
    save_logs: bool = False,
    yes: bool = True,
    glossaries: Iterable[str] | None = None,
    add_disclaimer: bool = False,
    translations_dir: str | None = None,
    image_dir: str | None = None,
    root_dirs: Iterable[str] | None = None,
    groups: Iterable[tuple[str, str | None]] | None = None,
) -> None:
    ...
```

#### Parameter reference

- **`language_codes`**
  - Type: `str`
  - Examples: `"ko"`, `"ko ja"`, `"all"`
  - Meaning: Same as CLI `-l/--language-codes`. Space-separated list of target language codes.
  - Special value `"all"`:
    - Uses `font_language_mappings.yml` to expand to all supported language codes.
    - Unlike the interactive CLI with `yes=False`, Localizeflow usage proceeds non-interactively, printing warnings but not prompting.

- **`root_dir`**
  - Type: `str`
  - Default: `"."`
  - Meaning: Project root directory to translate. Same as CLI `--root-dir`.
  - Recommendation: Interpret all relative paths (including `translations_dir`, `image_dir`) relative to `root_dir`.

- **`update`**
  - Type: `bool`
  - Default: `False`
  - Meaning: When `True`, delete existing translations for the given languages and re-translate (same semantics and warnings as CLI `-u/--update`).

- **`images`**
  - Type: `bool`
  - Default: `False`
  - Meaning: Enable image translation. When `True`, the image pipeline is enabled and Azure AI Service configuration is validated.
  - Internal effect: Adds `"images"` to the internal `translation_types` list.

- **`markdown`**
  - Type: `bool`
  - Default: `False`
  - Meaning: Enable markdown translation. When `True`, `.md` files are translated.
  - Internal effect: Adds `"markdown"` to `translation_types`.

- **`notebook`**
  - Type: `bool`
  - Default: `False`
  - Meaning: Enable Jupyter Notebook (`.ipynb`) translation.
  - Internal effect: Adds `"notebook"` to `translation_types`.

- **`debug`**
  - Type: `bool`
  - Default: `False`
  - Meaning: When `True`, enable DEBUG-level logging and emit verbose logs.

- **`save_logs`**
  - Type: `bool`
  - Default: `False`
  - Meaning: When `True`, write `translate` logs to `<root_dir>/logs/`.

- **`yes`**
  - Type: `bool`
  - Default: `True`
  - Meaning: Equivalent to CLI `-y/--yes`. Automatically confirm warnings (e.g., `all`, `update`) instead of prompting.
  - In Localizeflow scenarios, this default ensures non-interactive execution. Set to `False` only when debugging locally and you want more CLI-like behavior.

- **`glossaries`**
  - Type: `Iterable[str] | None`
  - Default: `None`
  - Meaning: List of terms that should be preserved **as-is** during translation (e.g., PR/Issue labels or product terms).
  - Behavior:
    - When provided, `co_op_translator.localizeflow.glossary.set_glossaries(glossaries)` is called before translation.
    - Markdown/image prompts are constructed to encourage the LLM to keep these terms unmodified.

- **`add_disclaimer`**
  - Type: `bool`
  - Default: `False`
  - Meaning: Whether to append a machine-translation disclaimer block to translated markdown/notebook files.
  - Localizeflow default is `False` so that output is suitable for direct end-user display. Set to `True` only if you explicitly want the disclaimer.

- **`translations_dir`**
  - Type: `str | None`
  - Default: `None`
  - Meaning: Root directory where translated text files (markdown/notebooks) are written.
  - Behavior:
    - If `None`: `ProjectTranslator` defaults to `root_dir / "translations"`.
    - If a string: Resolved via `Path(translations_dir).resolve()` and used as the translations root.
    - Actual output paths: `translations_dir / <lang> / <original_relative_path>`.
  - Recommended usage:
    - `translations_dir=str(root_dir / "content" / "i18n")`

- **`image_dir`**
  - Type: `str | None`
  - Default: `None`
  - Meaning: Root directory where translated images are written.
  - Behavior:
    - If `None`: Defaults to `root_dir / "translated_images"`.
    - If a string: Resolved via `Path(image_dir).resolve()` and used as the translated images root.
    - Actual output paths: Under `image_dir`, organized by language and file naming conventions.
  - Recommended usage:
    - `image_dir=str(root_dir / "public" / "translated_media")`

- **`root_dirs`**
  - Type: `Iterable[str] | None`
  - Default: `None`
  - Meaning: Optional list of additional source roots to translate when you want to run the same settings across multiple trees.
  - Behavior:
    - When provided (and `groups` is not set), `run_translation` runs once per `root_dir` in `root_dirs`.
    - Each root uses the same `translations_dir` / `image_dir` configuration.

- **`groups`**
  - Type: `Iterable[tuple[str, str | None]] | None`
  - Default: `None`
  - Meaning: Advanced multi-root mapping. Each tuple is `(source_root, target_path)` and results in a separate `ProjectTranslator`.
  - Behavior:
    - When `groups` is provided, it takes precedence over `root_dir` and `root_dirs`.
    - For a tuple `(src, dst)` **without** a `<lang>` placeholder:
      - Outputs go under: `dst / <lang> / <relative_path_from_src>`.
    - For a tuple where `dst` **contains** `<lang>`, for example `"i18n/<lang>/docusaurus-plugin-content-docs/current"`:
      - The part before `<lang>` (here `"i18n"`) is used as `translations_dir`.
      - The part after `<lang>` (here `"docusaurus-plugin-content-docs/current"`) becomes a language-specific subdirectory (`lang_subdir`).
      - Final layout: `i18n/<lang>/docusaurus-plugin-content-docs/current/<relative_path_from_src>`.

#### Behavioral differences vs CLI `translate`

-  By default, Localizeflow `run_translation` constructs `ProjectTranslator` with `add_disclaimer=False`.
-  As a result, translated markdown/notebooks do **not** include the machine-translation disclaimer block at the end unless you explicitly set `add_disclaimer=True`.
-  CLI `translate` defaults to `--add-disclaimer` (enabled), but for Localizeflow integration this is disabled by design for better UX.

- **Output directories**
  - CLI `translate`:
    - Always uses `root_dir/translations` and `root_dir/translated_images`.
  - Localizeflow `run_translation`:
    - Accepts `translations_dir` / `image_dir` as **optional overrides** to change output locations.
    - When not provided, falls back to the same defaults as the CLI.

- **Pipeline**
  - Both entry points use the same internal pipeline:
    1. Configuration and environment checks (`Config.check_configuration`, `LLMConfig`, `VisionConfig`)
    2. Token estimation (`TranslationManager.estimate_tokens`)
    3. Directory cleanup and synchronization (`DirectoryManager`)
    4. Markdown/notebook/image translation (`TranslationManager.translate_project_async`)

#### Usage examples from Localizeflow

- **Basic usage (markdown only, default output directories)**
from pathlib import Path
from co_op_translator.localizeflow import run_translation

root_dir = Path("/path/to/project").resolve()

run_translation(
    language_codes="ko ja",
    root_dir=str(root_dir),
    update=False,
    markdown=True,
    images=False,
    notebook=False,
    debug=False,
    save_logs=True,
    yes=True,
    glossaries=["PR", "Issue"],
)
```

- **Custom output directories**

```python
from pathlib import Path
from co_op_translator.localizeflow import run_translation

root_dir = Path("/path/to/project").resolve()

run_translation(
    language_codes="ko",
    root_dir=str(root_dir),
    update=False,
    markdown=True,
    images=False,
    notebook=False,
    debug=False,
    save_logs=True,
    yes=True,
    glossaries=["PR", "Issue"],
    translations_dir=str(root_dir / "content" / "i18n"),
    image_dir=str(root_dir / "content" / "i18n" / "translated_images"),
)
```

In this setup:

- Translated markdown/notebooks are written under: `content/i18n/<lang>/...`
- Translated images are written under: `content/i18n/translated_images/...`
- No machine-translation disclaimer is added to any output, making the results
  suitable for direct use in Localizeflow’s UI and review flows.

### Advanced: multiple roots via `groups` (Localizeflow only)

In addition to a single `root_dir` or a simple list of `root_dirs`, Localizeflow
can orchestrate **multiple independent source/output roots** by using the
`groups` parameter on `run_translation`.

This is especially useful for Astro-style or multi-root documentation repos
where you want to keep several content trees in sync, or for Docusaurus-style
sites that use an `i18n/<lang>/...` layout.

#### 1) Astro-style layout (basic `groups` usage)

Example (two content groups: `docs/en` and `blog/en`):

```python
from pathlib import Path
from co_op_translator.localizeflow import run_translation

project_root = Path("/path/to/astro-project").resolve()

groups = [
    # docs: src/content/docs/en -> src/content/docs/<lang>/...
    (
        str(project_root / "src" / "content" / "docs" / "en"),
        str(project_root / "src" / "content" / "docs"),
    ),
    # blog: src/content/blog/en -> src/content/blog/<lang>/...
    (
        str(project_root / "src" / "content" / "blog" / "en"),
        str(project_root / "src" / "content" / "blog"),
    ),
]

run_translation(
    language_codes="ko",
    root_dir=str(project_root),  # ignored when groups is provided
    markdown=True,
    images=False,
    notebook=False,
    debug=False,
    save_logs=True,
    yes=True,
    glossaries=["PR", "Issue"],
    groups=groups,
)
```

In this setup:

- Files under `src/content/docs/en/...` become
  `src/content/docs/ko/...`, `src/content/docs/ja/...`, etc.
- Files under `src/content/blog/en/...` become
  `src/content/blog/ko/...`, `src/content/blog/ja/...`, etc.
- Each group is isolated via its own `ProjectTranslator` instance, so
  translated trees are automatically excluded from subsequent source scans.

#### 2) Docusaurus-style layout (`i18n/<lang>/...` with `<lang>` placeholder)

For Docusaurus sites, translations are typically stored under an
`i18n/<lang>/...` directory. You can achieve this layout by using a `<lang>`
placeholder in each group's `target_path`.

Example (Docusaurus docs + pages):

```python
from pathlib import Path
from co_op_translator.localizeflow import run_translation

project_root = Path("/path/to/docusaurus-project").resolve()

groups = [
    # Docs content → i18n/<lang>/docusaurus-plugin-content-docs/current/...
    (
        str(project_root / "docs"),
        "i18n/<lang>/docusaurus-plugin-content-docs/current",
    ),
    # Pages content → i18n/<lang>/docusaurus-plugin-content-pages/...
    (
        str(project_root / "src" / "pages"),
        "i18n/<lang>/docusaurus-plugin-content-pages",
    ),
]

run_translation(
    language_codes="ko ja",
    root_dir=str(project_root),  # ignored when groups is provided
    markdown=True,
    images=False,
    notebook=False,
    debug=False,
    save_logs=True,
    yes=True,
    glossaries=["PR", "Issue"],
    groups=groups,
)
```

In this setup:

- Files under `docs/...` become
  `i18n/<lang>/docusaurus-plugin-content-docs/current/docs/...`.
- Files under `src/pages/...` become
  `i18n/<lang>/docusaurus-plugin-content-pages/src/pages/...`.
- The `<lang>` placeholder is replaced with each language code from
  `language_codes`, and the part of the path after `<lang>` is treated as a
  language-specific subdirectory for that content group.

## CI tips (optional)

- In GitHub Actions, use: `pip install git+https://github.com/localizeflow/localizeflow-co-op-translator.git@<tag>`
- Secrets: store `GITHUB_TOKEN` or a PAT in repository/organization secrets with least-privilege scopes

## References

- Core command reference: `getting_started/command-line-guide/command-line-guide.md`
- Supported languages: `getting_started/supported-languages.md`
- Troubleshooting: `getting_started/troubleshooting.md`
