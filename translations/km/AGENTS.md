# AGENTS.md

## Project Overview

Co‑op Translator គឺជាឧបករណ៍បញ្ជាទូរស័ព្ទ Python និងការងារសកម្មភាព GitHub ដែលបកប្រែឯកសារ Markdown, សៀវភៅ Noutbek Jupyter, និងអត្ថបទរូបភាពទៅជាភាសាដ៏ច្រើន។ វាបែងចែកលទ្ធផលនៅក្រោមថតភាសាពិសេសៗ ហើយរក្សាការបកប្រែឲ្យសមត្ថភាពជាមួយនឹងមាតិកាមូលដ្ឋាន។ គម្រោងនេះត្រូវបាន រៀបចំជាបណ្ណាល័យដែលគ្រប់គ្រងដោយ Poetry រួមមានចំណុចចូល CLI។

### Architecture overview

- ចំណុចចូល CLI (`translate`, `migrate-links`, `evaluate`) ហៅ CLI តែមួយដែលចែកចាយទៅកាន់ការបកប្រែ, ការផ្លាស់ប្តូរតំណភ្ជាប់ និងដំណើរការប៉ាន់ប្រមាណ។
- ជាអ្នកផ្ទុកការកំណត់វា អាន `.env` និងស្វ័យប្រវត្តិតាំងសិទ្ធិអ្នកផ្គត់ផ្គង់ LLM (Azure OpenAI ឬ OpenAI) និង ប្រសិនបើត្រូវការ អ្នកផ្គត់ផ្គង់ចក្ខុវិស័យ (Azure AI Service) សម្រាប់ដកអត្ថបទពីរូបភាព។
- មជ្ឈមណ្ឌលបកប្រែដោះស្រាយ Markdown និង notebooks; បំពង់ចក្ខុវិស័យដកអត្ថបទពីរូបភាពនៅពេលប្រើ `-img`។
- លទ្ធផលត្រូវបានរៀបចំទៅក្នុង `translations/<lang>/` សម្រាប់អត្ថបទ និង `translated_images/` សម្រាប់រូបភាព ការរក្សារស្ថាបត្យកម្មដើម។

### Key technologies and frameworks

- Python 3.10–3.12, Poetry សម្រាប់ការវេចខ្ចប់
- CLI៖ `click`
- LLM/AI SDKs៖ Azure OpenAI, OpenAI
- ចក្ខុវិស័យ៖ Azure AI Service (Computer Vision)
- HTTP និងទិន្នន័យ៖ `httpx`, `pydantic`
- រូបភាព៖ `pillow`, `opencv-python`, `matplotlib`
- សម្ភារៈ៖ `pytest`, `black`, `ruff`

## Setup Commands

### Prerequisites

- Python 3.10–3.12
- ការជាវ Azure (ជាជម្រើស សម្រាប់សេវាកម្ម Azure AI)
- ការចូលប្រើអ៊ីនធឺណិតសម្រាប់ API LLM/ចក្ខុវិស័យ (ឧ. Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (recommended)

```bash
# ពីថ្ពល់ឃ្លាំងដើម
pip install poetry
poetry install

# បើកបង្កើតពាក្យបញ្ជាណាមួយតាមរយៈ Poetry
poetry run translate --help
```

### Option B: pip/venv

```bash
# បង្កើត និងដំណើរការបរិស្ថានចម្រង់
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
# source .venv/bin/activate

# ដំឡើងអាស្រ័យការ
pip install -r requirements.txt

# (ជាជម្រើស) ដំឡើងអាចកែតម្រូវសម្រាប់ការអភិវឌ្ឍន៍ក្នុងស្រុក
pip install -e .
```

## End User Usage

### Docker (published image)

```bash
# ទាញរូបភាពសាធារណៈពី GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# វេចខ្ចប់ជាមួយថតបច្ចុប្បន្នបានភ្ជាប់ និងផ្គត់ផ្គង់ .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

កំណត់ចំណាំ:
- ចំណុចចូលលំនាំដើមគឺ `translate`។ អាចរំខានបានជាមួយ `--entrypoint migrate-links` សម្រាប់ការផ្លាស់ប្តូរតំណភ្ជាប់។
- ប្រាកដថាការមើលឃើញកញ្ចប់ GHCR គឺសាធារណៈសម្រាប់ការទាញយកដោយមិនបង្ហាញអត្តសញ្ញាណ។

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Environment configuration

បង្កើតឯកសារ `.env` នៅឫសតំបន់ repositoriy ហើយផ្ដល់សក្ខីប័ត្រនិងចំណុចចេញសម្រាប់ម៉ូឌែលភាសាដែលបានជ្រើស និង (ជាជម្រើស) សេវាកម្មចក្ខុវិស័យ។ សម្រាប់ការកំណត់ជាក់លាក់អ្នកផ្គត់ផ្គង់ មើល `getting_started/set-up-azure-ai.md`។

### Required Environment Variables

យ៉ាងហោចណាស់ត្រូវបានកំណត់អ្នកផ្គត់ផ្គង់ LLM ម្នាក់។ សម្រាប់ការបកប្រែរូបភាព អ្នកផ្គត់ផ្គង់ Azure AI Service ត្រូវបានដាច់ខាត។

- Azure OpenAI (បកប្រែអត្ថបទ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ជំនួសការបកប្រែអត្ថបទ):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ជាជម្រើស)
  - `OPENAI_CHAT_MODEL_ID` (ទាមទ្រែនៅពេលប្រើអ្នកផ្គត់ផ្គង់ OpenAI)
  - `OPENAI_BASE_URL` (ជាជម្រើស; ដើមតម្លៃទៅ `https://api.openai.com/v1`)

- Azure AI Service សម្រាប់ដកអត្ថបទរូបភាព (ទាមទ្រែនៅពេលប្រើ `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (ចូលចិត្ត) ឬ legacy `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

ឧទាហរណ៍ផ្នែក `.env`៖

```bash
# បម្រើការផ្ទេរប្រែរូបភាព Azure AI
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (ជាជម្រើស​សំខាន់)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (ជាជម្រើសជំនួស)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # ជាជម្រើស
OPENAI_CHAT_MODEL_ID="gpt-4o"   # ត្រូវការ​បន្ទាប់​ពេលប្រើ OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # ជាជម្រើស
```

កំណត់ចំណាំ៖

- ឧបករណ៍នេះស្វ័យប្រវត្តិរកឃើញអ្នកផ្គត់ផ្គង់ LLM ដែលមាន; កំណត់មួយក្នុង Azure OpenAI ឬ OpenAI។
- ការបកប្រែរូបភាពត្រូវការ `AZURE_AI_SERVICE_API_KEY` និង `AZURE_AI_SERVICE_ENDPOINT` ទាំងពីរ។
- CLI នឹងរាយការណ៍កំហុសច្បាស់ប្រសិនបើខ្វះអថេរដែលត្រូវការ។

## Development Workflow

- កូដប្រភពស្ថិតក្រោម `src/co_op_translator`; តេស្តនៅក្រោម `tests/`។
- CLI សំខាន់ៗ (តម្លើងតាមចំណុចចូល)៖

```bash
# ប្រែចំាអត្ថបទទៅជាភាសាមួយឬច្រើនជាភាសា (កូដដាច្បាប់ដោយចន្លោះ)
translate -l "fr es de"

# កំណត់តាមប្រភេទខ្លឹមសារ
translate -l "ja" -md            # សម្រាប់ Markdown តែមួយ
translate -l "ko" -nb            # សម្រាប់សៀវភៅកំណត់ត្រាតែមួយ
translate -l "zh" -md -img       # Markdown + រូបភាព

# កែប្រែតំណភ្ជាប់នៅក្នុងសៀវភៅកំណត់ត្រា/Markdown ដែលបានប្រែរួច
migrate-links -l "all" -y
```

មើលឯកសារបន្ថែមសម្រាប់ការប្រើប្រាស់ក្នុង `getting_started/`។

## Testing Instructions

រត់តេស្តពីឫសនៃ repository។ តេស្តខ្លះប្រហែលត្រូវការសក្ខីប័ត្រ API; ហៅលោតពួកវាពេលទេ។

```bash
# ធ្វើប្រតិបត្តិការសោភ័ណ្ឌតេស្តទាំងមូល
pytest

# មិនធ្វើតេស្តដែលត្រូវការជាគន្លង API ភាពរស់
pytest -m "not api_key_required"

# ធ្វើតេស្តមួយផ្នែកគត់
pytest tests/co_op_translator -k "name_substring"
```

ការគ្របដណ្តប់ជាជម្រើស (ត្រូវការនៅ `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # ផ្លាស់ប្តូរចេញទៅ ./htmlcov
```

## Code Style Guidelines

- Formatter: Black (បានកំណត់ក្នុង `pyproject.toml`, ប្រវែងជួរបន្ទាត់ ៨៨)
- Linter: Ruff (បានកំណត់ក្នុង `pyproject.toml`, ប្រវែងជួរបន្ទាត់ ១២០)
- ការត្រួតពិនិត្យប្រភេទ: mypy (អ្នកកំណត់មាន; បើកប្រសិនបើបានដំឡើង)

ពាក្យបញ្ជា៖

```bash
# តាមរយៈ Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # ការជួសជុលស្វ័យប្រវត្តិសុវត្ថិភាព

# ឬជាមួយឧបករណ៍សកល
black .
ruff check .
```

រៀបចំប្រភព Python នៅក្រោម `src/`, តេស្តក្រោម `tests/`, ហើយចូលចិត្តនាំចូលច្បាស់លាស់នៅក្នុងឈ្មោះកន្លែងកញ្ចប់ (`co_op_translator.*`)។

## Build and Deployment

ឯកសារសាងសង់ត្រូវបានផ្សាយទៅ `dist/`។

```bash
# បង្កើត (Poetry)
poetry build

# ដំឡើងក្នុងតំបន់នៃរ៉ូតស៊ុយដែលបានបង្កើត
pip install dist/*.whl
```

ការជំនួយដោយ GitHub Actions ត្រូវបានគាំទ្រ; មើល៖

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- រូបភាពផ្លូវការជា `ghcr.io/azure/co-op-translator:<tag>`
- ស្លាកៈ `latest` (នៅលើ main), ស្លាកសំគាល់ដូចជា `vX.Y.Z`, និងស្លាក `sha`
- Multi-arch៖ `linux/amd64, linux/arm64` គាំទ្រដោយ Buildx
- លំនាំ Dockerfile ៖ សាងសង់ពងរូបមន្តក្នុង builder (ជាមួយ `build-essential` និង `python3-dev`) ហើយដំឡើងពីដុំរូបមន្តក្នុង runtime (`pip install --no-index --find-links=/wheels`)
- Workflow ៖ `.github/workflows/docker-publish.yml` សាងសង់ និងផ្សាយទៅ GHCR

## Security Considerations

- រក្សាគន្លង API និងចំណុចចេញនៅក្នុង `.env` ឬហាងសម្ងាត់ CI របស់អ្នក; កុំបញ្ជូលសម្ងាត់ឡើយ។
- សម្រាប់ការបកប្រែរូបភាព ត្រូវការ key និងចំណុចចេញ Azure AI Vision បើគ្មានកុំប្រើ `-img`។
- ផ្ទៀងផ្ទាត់គោលការណ៍/កម្រិតពីរមាត្រឲ្យបានត្រឹមត្រូវ នៅពេលរត់ប៉ុនប៉ងបកប្រែច្រើន។

## Pull Request Guidelines

### Before Submitting

1. **សាកល្បងការផ្លាស់ប្តូរ៖**
   - រត់ notebooks ដែលទាក់ទងពេញលេញ
   - ពិនិត្យមើលថាសែលទាំងអស់ដំណើរការដោយគ្មានកំហុស
   - ធ្វើការត្រួតពិនិត្យថាលទ្ធផលអាចអានបាន

2. **ធ្វើបច្ចុប្បន្នភាពឯកសារ៖**
   - កែសម្រួល `README.md` ប្រសិនបើបន្ថែមមុខងារថ្មី
   - បន្ថែមការអធិប្បាយក្នុង notebooks សម្រាប់កូដស្មុគស្មាញ
   - ប្រាកដថាឯកសារ markdown ពន្យល់គោលបំណង

3. **ការផ្លាស់ប្តូរឯកសារ៖**
   - មិនបញ្ជូល `.env` (ប្រើ `.env.example`)
   - មិនបញ្ជូលថត `venv/` ឬ `__pycache__/`
   - រក្សាលទ្ធផល notebook បើបង្ហាញគំនិត
   - លុបឯកសារស្ថិតិសំរបសំរួល និងគាំទ្រ (`*-backup.ipynb`)

4. **រចនាបថ និងការតំរូវការជាច្រើន៖**
   - តាមរចនាបថនិងការតំរូវការនានា
   - រត់ `poetry run black .` និង `poetry run ruff check .` ដើម្បីពិនិត្យកំហុសរចនាបថ

5. **បន្ថែម/ធ្វើបច្ចុប្បន្នភាពតេស្ត និងជំនួយ CLI៖**
   - បន្ថែមឬធ្វើបច្ចុប្បន្នភាពតេស្តពេលបម្លែងលក្ខណៈ
   - រក្សាជំនួយ CLI អោយត្រូវគ្នាជាមួយការផ្លាស់ប្តូរ

### Commit message and merge strategy

យើងប្រើ Squash and Merge ជាលំនាំដើម។ សារបញ្ចូលនៅចុងក្រោយក្នុងលក្ខណៈ squash commit គួរតែបង្វិលទៅដូចជា ៖

```bash
<type>: <description> (#<លេខ PR>)
```

ប្រភេទដែលអនុញ្ញាត៖
- `Docs` — ការអាប់ដេតឯកសារ
- `Build` — ប្រព័ន្ធសាងសង់, អាសន្នភាព, ការកំណត់/CI
- `Core` — មុខងារចម្បង និងលក្ខណៈពិសេស (ឧ. `src/co_op_translator/core`)

ឧទាហរណ៍៖
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

កំណត់ចំណាំ៖
- ចំណងជើង PR ជាញឹកញាប់ត្រូវបានបង្កើតដោយស្វ័យប្រវត្តិផ្អែកលើស្លាក; ត្រួតពិនិត្យ prefix ដែលបានបង្កើតថាត្រឹមត្រូវ។

### PR Title Format

ប្រើចំណងជើងច្បាស់លាស់និងខ្លី។ ចូលចិត្តរចនាសម្ព័ន្ធដូច squash commit នៅចុងក្រោយ៖
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- បញ្ហាទូទៅ និងដំណោះស្រាយ៖ `getting_started/troubleshooting.md`
- ភាសាគាំទ្រ និងកំណត់ចំណាំ (រួមមានពុម្ពអក្សរ/បញ្ហារួចរាល់) ៖ `getting_started/supported-languages.md`
- សម្រាប់បញ្ហាតំណភ្ជាប់ក្នុង notebooks, រត់ឡើងវិញ៖ `migrate-links -l "all" -y`

## Notes for Agents

- ចូលចិត្ត Poetry សម្រាប់បរិយាកាសអាចគ្រប់គ្រងបានឡើងវិញ; អរគុណប្រើ `requirements.txt` ប្រសិនបើមិនដូច្នេះ។
- នៅពេលហៅ CLI ក្នុង CI, ផ្ដល់សម្ងាត់តាមអថេរបរិស្ថាន ឬការចាក់បញ្ចូល `.env`។
- សម្រាប់អ្នកប្រើ monorepo, repo នេះដំណើរការជាកញ្ចប់ផ្ទាល់ខ្លួន; មិនត្រូវការសម្របសម្រួលកញ្ចប់រង។

- ដំណោះស្រាយ Multi-arch៖ រក្សា `linux/arm64` នៅពេលអ្នកប្រើ ARM (Apple Silicon/ARM servers) ជាគោលដៅ; មិនប៉ុនប៉ង `linux/amd64` តែប៉ុណ្ណោះសម្រាប់ភាពសាមញ្ញ។
- បង្ហាញអ្នកប្រើទៅ Docker Quick Start នៅក្នុង `README.md` នៅពេលពួកគេចូលចិត្តប្រើ container; រួមបញ្ចូលបម្រាំង Bash និង PowerShell ដោយសារបម្លែងយ៉ាងខុសគ្នានៃសញ្ញា។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបម្លែងភាសា ដោយប្រើសេវាបម្លែងភាសា AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខ្ញុំមានក្តីប្រាថ្នាឱ្យបានច្បាស់លាស់ តែសូមយល់ដឹងថាការបម្លែងដោយស្វ័យប្រវត្តិក៏អាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាទីតាំងគួរត្រូវបានគេប្រើជាប្រភពច្បាស់លាស់។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឱ្យប្រើប្រាស់ការប្រែដោយមនុស្សជំនាញ។ យើងខ្ញុំមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសបន្ទាប់ពីការប្រើប្រាស់ការបម្លែងនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->