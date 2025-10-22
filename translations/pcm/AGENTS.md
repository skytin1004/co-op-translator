<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3fd2055f97f093b6fe102ea24df4458b",
  "translation_date": "2025-10-22T11:14:22+00:00",
  "source_file": "AGENTS.md",
  "language_code": "pcm"
}
-->
# Project Overview

Co‑op Translator na Python command line tool wey dey work with GitHub Actions workflow wey dey help translate Markdown files, Jupyter notebooks, and image text go plenty languages. E dey arrange the translated files inside folders wey get language name, and e dey make sure say translation dey up to date with the original content. The project na Poetry dey manage am as library, and e get CLI entry points.

### How the Project Take Work

- CLI entry points (`translate`, `migrate-links`, `evaluate`) dey call one CLI wey fit do translation, link migration, and evaluation.
- Configuration loader dey read `.env` and e fit know the LLM provider (Azure OpenAI or OpenAI) and, if you need am, the vision provider (Azure AI Service) for image text extraction.
- Translation core dey handle Markdown and notebooks; vision pipeline dey extract text from images if you use `-img`.
- Outputs dey go `translations/<lang>/` for text and `translated_images/` for images, and e dey keep the original arrangement.

### Main Technologies and Frameworks

- Python 3.10–3.12, Poetry for packaging
- CLI: `click`
- LLM/AI SDKs: Azure OpenAI, OpenAI
- Vision: Azure AI Service (Computer Vision)
- HTTP and data: `httpx`, `pydantic`
- Imaging: `pillow`, `opencv-python`, `matplotlib`
- Tooling: `pytest`, `black`, `ruff`

## How to Set Up

### Wetin You Need Before You Start

- Python 3.10–3.12
- Azure subscription (if you wan use Azure AI services)
- Internet wey go fit reach LLM/Vision APIs (like Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (na the best way)

```bash
# From repository root
pip install poetry
poetry install

# Run any command via Poetry
poetry run translate --help
```

### Option B: pip/venv

```bash
# Create & activate virtual environment
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Optional) Editable install for local development
pip install -e .
```

## How End User Go Use Am

### Docker (published image)

```bash
# Pull public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

Notes:
- The default entrypoint na `translate`. If you wan migrate links, use `--entrypoint migrate-links`.
- Make sure say GHCR package dey Public so anybody fit pull am.

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### How to Set Environment

Create `.env` file for the root of the repo, put your credentials/endpoints for the language model wey you wan use and (if you wan) vision service. If you wan know how to set up for each provider, check `getting_started/set-up-azure-ai.md`.

### Environment Variables Weh You Must Put

At least one LLM provider must dey set. If you wan translate image, you must set Azure AI Service too.

- Azure OpenAI (for text translation):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (another way for text translation):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (if you wan)
  - `OPENAI_CHAT_MODEL_ID` (you must put am if you dey use OpenAI provider)
  - `OPENAI_BASE_URL` (if you wan; default na `https://api.openai.com/v1`)

- Azure AI Service for image text extraction (if you dey use `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (na the best) or old `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

Example for `.env`:

```bash
# Azure AI Service (for image translation)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (primary option)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (alternative option)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # optional
OPENAI_CHAT_MODEL_ID="gpt-4o"   # required when using OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # optional
```

Notes:

- The tool go check which LLM provider dey; just set Azure OpenAI or OpenAI.
- If you wan translate image, you must set both `AZURE_AI_SERVICE_API_KEY` and `AZURE_AI_SERVICE_ENDPOINT`.
- If you no set the required variables, CLI go show you clear error.

## How to Work as Developer

- Source code dey inside `src/co_op_translator`; tests dey inside `tests/`.
- Main CLIs (you fit install am with entry points):

```bash
# Translate content to one or more languages (space‑separated codes)
translate -l "fr es de"

# Restrict by content type
translate -l "ja" -md            # only Markdown
translate -l "ko" -nb            # only notebooks
translate -l "zh" -md -img       # Markdown + images

# Update links in previously translated notebooks/Markdown
migrate-links -l "all" -y
```

Check more usage docs for `getting_started/`.

## How to Run Tests

Run tests from the root of the repo. Some tests fit need API credentials; if you no get, skip those ones.

```bash
# Run full test suite
pytest

# Skip tests that require live API keys
pytest -m "not api_key_required"

# Run a subset
pytest tests/co_op_translator -k "name_substring"
```

If you wan check coverage (you need `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # outputs to ./htmlcov
```

## Code Style Guidelines

- Formatter: Black (e dey set for `pyproject.toml`, line length 88)
- Linter: Ruff (e dey set for `pyproject.toml`, line length 120)
- Type checks: mypy (configuration dey; enable am if you install mypy)

Commands:

```bash
# Via Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # safe auto‑fixes

# Or with global tools
black .
ruff check .
```

Arrange Python code inside `src/`, tests inside `tests/`, and try use explicit imports inside the package namespace (`co_op_translator.*`).

## How to Build and Deploy

Build artifacts dey go `dist/`.

```bash
# Build (Poetry)
poetry build

# Local install of the built wheel
pip install dist/*.whl
```

Automation dey with GitHub Actions; check:

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- Official image: `ghcr.io/azure/co-op-translator:<tag>`
- Tags: `latest` (for main), semantic tags like `vX.Y.Z`, and `sha` tag
- Multi-arch: `linux/amd64, linux/arm64` dey work with Buildx
- Dockerfile style: build dependency wheels for builder (with `build-essential` and `python3-dev`) and install from local wheelhouse for runtime (`pip install --no-index --find-links=/wheels`)
- Workflow: `.github/workflows/docker-publish.yml` dey build and push go GHCR

## Security Matter

- Keep your API keys and endpoints inside `.env` or your CI secrets store; no ever commit secrets.
- If you wan translate image, you need Azure AI Vision keys/endpoints; if you no get, no use `-img`.
- Check provider quotas/rate limits if you dey run plenty translation at once.

## Pull Request Guidelines

### Before You Submit

1. **Test your changes:**
   - Run all the notebooks wey you change
   - Make sure all cells dey run without error
   - Check say the outputs correct

2. **Update Documentation:**
   - Update `README.md` if you add new things
   - Put comments for notebooks if code dey complex
   - Make sure markdown cells dey explain wetin dey happen

3. **File changes:**
   - No commit `.env` files (use `.env.example`)
   - No commit `venv/` or `__pycache__/` folders
   - Keep notebook outputs if dem dey show example
   - Remove temporary files and backup notebooks (`*-backup.ipynb`)

4. **Style and formatting:**
   - Follow the style and formatting rules
   - Run `poetry run black .` and `poetry run ruff check .` to check for style and formatting wahala

5. **Add/update tests and CLI help:**
   - Add or update tests if you change how something dey work
   - Make CLI help match the changes

### Commit Message and Merge Style

We dey use Squash and Merge as default. The final squash commit message suppose follow this style:

```bash
<type>: <description> (#<PR number>)
```

Allowed types:
- `Docs` — for documentation update
- `Build` — for build system, dependencies, configuration/CI
- `Core` — for main functionality and features (like `src/co_op_translator/core`)

Examples:
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

Notes:
- PR titles dey auto-prefix based on labels; check say the prefix correct.

### PR Title Format

Use clear, short titles. Use the same style as the final squash commit:
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- Common issues and how to fix: `getting_started/troubleshooting.md`
- Supported languages and notes (fonts/known issues): `getting_started/supported-languages.md`
- If you get link wahala for notebooks, run: `migrate-links -l "all" -y`

## Notes for Agents

- Use Poetry for environment wey you fit repeat; if you no wan, use `requirements.txt`.
- If you dey run CLI for CI, provide secrets with environment variables or `.env`.
- For monorepo users, this repo dey work as standalone package; you no need coordinate sub‑package.

- For multi-arch: keep `linux/arm64` if ARM users (Apple Silicon/ARM servers) dey use am; if not, only `linux/amd64` dey okay for easy setup.
- If user prefer Docker, point them to Docker Quick Start for `README.md`; show Bash and PowerShell examples because of how dem dey handle quotes.

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate this document. Even though we try make the translation correct, abeg make you sabi say machine translation fit get mistake or no too dey accurate. Na the original document for the main language be the correct one wey you suppose follow. If the information dey important, abeg use professional human translation. We no go fit hold any responsibility for wahala or misunderstanding wey fit happen because of this translation.