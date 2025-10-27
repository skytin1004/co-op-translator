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

## CI tips (optional)

- In GitHub Actions, use: `pip install git+https://github.com/localizeflow/localizeflow-co-op-translator.git@<tag>`
- Secrets: store `GITHUB_TOKEN` or a PAT in repository/organization secrets with least-privilege scopes

## References

- Core command reference: `getting_started/command-line-guide/command-line-guide.md`
- Supported languages: `getting_started/supported-languages.md`
- Troubleshooting: `getting_started/troubleshooting.md`
