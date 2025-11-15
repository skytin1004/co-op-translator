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

## CI tips (optional)

- In GitHub Actions, use: `pip install git+https://github.com/localizeflow/localizeflow-co-op-translator.git@<tag>`
- Secrets: store `GITHUB_TOKEN` or a PAT in repository/organization secrets with least-privilege scopes

## References

- Core command reference: `getting_started/command-line-guide/command-line-guide.md`
- Supported languages: `getting_started/supported-languages.md`
- Troubleshooting: `getting_started/troubleshooting.md`
