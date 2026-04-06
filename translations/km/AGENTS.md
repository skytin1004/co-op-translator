# AGENTS.md

## Project Overview

Co‑op Translator គឺជាឧបករណ៍បញ្ជាទៅ Python និងកម្មវិធី GitHub Actions workflow ដែលបកប្រែឯកសារ Markdown, សៀវភៅ Jupyter notebooks និងអត្ថបទរូបភាពទៅជាភាសាច្រើន។ វាចងក្រងលទ្ធផលជាបណ្ណាល័យសម្រាប់ភាសាផ្សេងៗ ហើយរក្សារភាសាបកប្រែឱ្យត្រូវគ្នាជាមួយមាតិកាមូលដ្ឋាន។ គម្រោងនេះដាក់ចរន្តក្នុងបណ្ណាល័យដែលគ្រប់គ្រងដោយ Poetry មានចំណុចចូល CLI។

### Architecture overview

- ចំណុចចូល CLI (`translate`, `migrate-links`, `evaluate`) ហៅ CLI តែមួយដែលបញ្ជូនទៅកាន់ដំណើរការបកប្រែ, រំលាយតំណភ្ជាប់ និងការវាយតម្លៃ។
- អ្នកផ្ទុកការកំណត់អាន `.env` ហើយរកឃើញផ្នែកផ្គត់ផ្គង់ LLM (Azure OpenAI ឬ OpenAI) និង ប្រសិនបើត្រូវការ វិស័យ (Azure AI Service) សម្រាប់ដកអត្ថបទពីរូបភាព។
- មូលដ្ឋានបកប្រែគ្រប់គ្រង Markdown និង notebooks; បណ្តាញវិស្ស័យដកអត្ថបទពីរូបភាពពេលប្រើ `-img`។
- លទ្ធផលត្រូវបានបែងចែកក្នុង `translations/<lang>/` សម្រាប់អត្ថបទ និង `translated_images/` សម្រាប់រូបភាព រក្សាស្ថានភាពដើម។

### Key technologies and frameworks

- Python 3.10–3.12, Poetry សម្រាប់កញ្ចប់
- CLI: `click`
- SDKs LLM/AI: Azure OpenAI, OpenAI
- វិស័យ: Azure AI Service (Computer Vision)
- HTTP និងទិន្នន័យ: `httpx`, `pydantic`
- បច្ចេកវិទ្យារូបភាព: `pillow`, `opencv-python`, `matplotlib`
- គ្រឿងក្រោម: `pytest`, `black`, `ruff`

## Setup Commands

### Prerequisites

- Python 3.10–3.12
- សូមចុះឈ្មោះនៅ Azure (ប្រសិនបើចង់បាន សម្រាប់សេវា Azure AI)
- បណ្ដាញអ៊ីនធើណែតសម្រាប់ APIs LLM/Vision (ឧ. Azure OpenAI/OpenAI, Azure AI Vision)

### Option A: Poetry (recommended)

```bash
# ពីដើមឫសឃ្លាំងទិន្នន័យ
pip install poetry
poetry install

# ដំណើរការបញ្ជាក់ណាមួយតាមរយៈ Poetry
poetry run translate --help
```

### Option B: pip/venv

```bash
# បង្កើត និងដំណើរការបរិយាកាសវីរុត្វ
python -m venv .venv
# វីនដូ
.venv\\Scripts\\activate
# លីនុច/ម៉ាក់អូអេស
# ប្រើ source .venv/bin/activate

# តំឡើងអាស្រ័យភាព
pip install -r requirements.txt

# (ជាជម្រើស) ការតំឡើងដែលអាចកែប្រែសម្រាប់ការអភិវឌ្ឍន៍ក្នុងស្រុក
pip install -e .
```

## End User Usage

### Docker (published image)

```bash
# ដករូបភាពសាធារណៈពី GHCR
docker pull ghcr.io/azure/co-op-translator:latest

# បើកប្រើជាមួយថតបច្ចុប្បន្នដែលបានភ្ជាប់ និងបានផ្តល់ .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "fr es" -md

# PowerShell
docker run --rm -it --env-file .env -v ${PWD}:/work ghcr.io/azure/co-op-translator:latest -l "fr es" -md
```

សម្គាល់៖
- ចំណុចចូលលំនាំដើមគឺ `translate`។ អាចប្ដូរជាមួយ `--entrypoint migrate-links` សម្រាប់រំលាយតំណភ្ជាប់។
- បញ្ជាក់ថាកញ្ចប់ GHCR មានទិដ្ឋភាពសាធារណៈសម្រាប់ដកយកដោយគ្មានចូលប្រើប្រាស់។

### CLI (pip)

```bash
pip install co-op-translator
translate -l "fr es" -md
```

### Environment configuration

បង្កើតឯកសារ `.env` នៅឫសបណ្ណាល័យ និងផ្ដល់សំណុំបែបបទ/ចំណុចចូលសម្រាប់ម៉ូឌែលភាសាដែលអ្នកជ្រើស និង (ប្រសិនបើ) សេវាវិស័យ។ សម្រាប់ការកំណត់អ្នកផ្គត់ផ្គង់ជាក់លាក់ សូមមើល `getting_started/set-up-azure-ai.md`។

### Required Environment Variables

ត្រូវតែមានអ្នកផ្គត់ផ្គង់ LLM យ៉ាងតិចមួយ។ សម្រាប់ការបកប្រែរូបភាព បើកការកំណត់ Azure AI Service ផងដែរ។

- Azure OpenAI (បកប្រែអត្ថបទ):
  - `AZURE_OPENAI_API_KEY`
  - `AZURE_OPENAI_ENDPOINT`
  - `AZURE_OPENAI_MODEL_NAME`
  - `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`
  - `AZURE_OPENAI_API_VERSION`

- OpenAI (ជម្រើសបកប្រែអត្ថបទ):
  - `OPENAI_API_KEY`
  - `OPENAI_ORG_ID` (ថែមទាំង)
  - `OPENAI_CHAT_MODEL_ID` (ត្រូវការ ពេលប្រើៈ OpenAI provider)
  - `OPENAI_BASE_URL` (ថែមទាំង; រោយលំនាំទៅ `https://api.openai.com/v1`)

- សេវា Azure AI សម្រាប់ដកអត្ថបទរូបភាព (ត្រូវការ ពេលប្រើ `-img`):
  - `AZURE_AI_SERVICE_API_KEY` (អនុវត្ត) ឬ ជំនាន់ចាស់ `AZURE_SUBSCRIPTION_KEY`
  - `AZURE_AI_SERVICE_ENDPOINT`

ឧទាហរណ៍ snippet `.env`៖

```bash
# សេវា Azure AI (សម្រាប់ការ​បកប្រែ​រូបភាព)
AZURE_AI_SERVICE_API_KEY="..."
AZURE_AI_SERVICE_ENDPOINT="https://<your-ai-service>.cognitiveservices.azure.com/"

# Azure OpenAI (ជម្រើសសាកល្បង​លេខមួយ)
AZURE_OPENAI_API_KEY="..."
AZURE_OPENAI_ENDPOINT="https://<your-azure-openai>.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="gpt-4o"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="<your-deployment>"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# OpenAI (ជម្រើសជំនួស)
OPENAI_API_KEY="..."
OPENAI_ORG_ID="..."            # ជាជម្រើស
OPENAI_CHAT_MODEL_ID="gpt-4o"   # ត្រូវការ​ពេល​ប្រើ OpenAI
OPENAI_BASE_URL="https://api.openai.com/v1" # ជាជម្រើស
```

សម្គាល់៖

- ឧបករណ៍ស្វ័យប្រវត្តិសង្កេតអ្នកផ្គត់ផ្គង់ LLM ដែលមាន; កំណត់ Azure OpenAI ឬ OpenAI ទាំងពីរ។
- ការបកប្រែរូបភាពតម្រូវឲ្យមានទាំង `AZURE_AI_SERVICE_API_KEY` និង `AZURE_AI_SERVICE_ENDPOINT`។
- CLI នឹងបង្ហាញកំហុសច្បាស់ជារឿងបើអថេរត្រូវការ​ខ្វះ។

## Development Workflow

- កូដប្រភពស្នាក់នៅក្រោម `src/co_op_translator`; សាកល្បងក្រោម `tests/`។
- CLIs សំខាន់ៗ (ដំឡើងតាមចំណុចចូល):

```bash
# បកប្រែមាតិកាទៅជาทាសា តែមួយឬច្រើន (កូដបំបែកដោយចន្លោះ)
translate -l "fr es de"

# កំណត់ដោយប្រភេទមាតិកា
translate -l "ja" -md            # មានតែ Markdown តែប៉ុណ្ណោះ
translate -l "ko" -nb            # មានតែកំណត់វិចិត្រសារ (notebooks) តែប៉ុណ្ណោះ
translate -l "zh" -md -img       # Markdown + រូបភាព

# បច្ចុប្បន្នភាពតំណភ្ជាប់នៅក្នុងកំណត់វិចិត្រសារ/Markdown ដែលបានបកប្រែមុននេះ
migrate-links -l "all" -y
```

មើលឯកសារបន្ថែមសម្រាប់ការប្រើប្រាស់ក្នុង `getting_started/`។

## Testing Instructions

ដំណើរការសាកល្បងពីឫសបណ្ណាល័យ។ យកចិត្តទុកដាក់ថាពីព្រោះអាចត្រូវការអ៊ីភីយិការពារសម្រាប់សាកល្បងខ្លះ; ប្រសិនបើចាំបាច់អាចរំលងបាន។

```bash
# ដំណើរការប្រឡងពេញលេញ
pytest

# រំលងការប្រឡងដែលត្រូវការកូនសោ API រស់
pytest -m "not api_key_required"

# ដំណើរការតែក្រុមរងប៉ុណ្ណោះ
pytest tests/co_op_translator -k "name_substring"
```

ការត្រួតពិនិត្យបន្ថែម (ត្រូវការម៉ូឌុល `coverage`):

```bash
coverage run -m pytest -m "not api_key_required"
coverage html  # បញ្ចេញទៅ ./htmlcov
```

## Code Style Guidelines

- កម្មវិធីផែនការ: Black (បានកំណត់នៅក្នុង `pyproject.toml`, ប្រវែងជួរដេក 88)
- កម្មវិធីពិនិត្យលំអិត: Ruff (បានកំណត់នៅក្នុង `pyproject.toml`, ប្រវែងជួរដេក 120)
- ពិនិត្យប្រភេទ: mypy (មានការកំណត់; បើកប្រសិនបើបានដំឡើង)

ពាក្យបញ្ជា:

```bash
# តាមរយៈ Poetry
poetry run black .
poetry run ruff check .
poetry run ruff check . --fix   # ការជួសជុលស្វ័យប្រវត្តិដែលមានសុវត្ថិភាព

# ឬជាមួយឧបករណ៍សកល
black .
ruff check .
```

ចងកូដ Python នៅក្រោម `src/`, សាកល្បងក្រោម `tests/`, ហើយចូលចិត្តនាំចូលច្បាស់លាស់នៅក្នុងវិទ្យាស្ថានកញ្ចប់ (`co_op_translator.*`)។

## Build and Deployment

ផលិតផលកែលេខត្រូវបានផ្សាយនៅ `dist/`។

```bash
# សាងសង់ (Poetry)
poetry build

# ការតំឡើងក្នុងម៉ាសីែនៃកង់ដែលបានសាងសង់
pip install dist/*.whl
```

គាំទ្រដំណើរការដោយ GitHub Actions; មើល៖

- `getting_started/github-actions-guide/github-actions-guide-public.md`
- `getting_started/github-actions-guide/github-actions-guide-org.md`

### Container Image (GHCR)

- រូបភាពផ្លូវការ៖ `ghcr.io/azure/co-op-translator:<tag>`
- ស្លាក: `latest` (នៅ main), ស្លាកអត្ថន័យដូចជា `vX.Y.Z`, និងស្លាក `sha`
- Multi-arch: គាំទ្រដោយ Buildx សម្រាប់ `linux/amd64, linux/arm64`
- រូបចំលង Dockerfile: បង្កើតរបារពន្លឺនៅក្នុង builder (ជាមួយ `build-essential` និង `python3-dev`) ហើយដំឡើងពី wheelhouse ផ្លូវការនៅ runtime (`pip install --no-index --find-links=/wheels`)
- workflow: `.github/workflows/docker-publish.yml` បង្កើត និងបញ្ចូលទៅ GHCR

## Security Considerations

- រក្សាគន្លង API និងចំណុចចូលនៅក្នុង `.env` ឬហាង CI របស់អ្នក; កុំបង្ហោះសម្ងាត់ក្នុងកូដ។
- សម្រាប់ការបកប្រែរូបភាព តម្រូវឲ្យមានកូនសោ Azure AI Vision និងចំណុចចូល។ បើមិនដូច្នោះទេ មិនត្រូវប្រើ `-img`។
- ពិនិត្យឲ្យបានថាបរិមាណអ្នកផ្គត់ផ្គង់/កំណត់ត្រាទំនាក់ទំនងប្រសិនបើដំណើរការជាច្រើនលើបរិមាណធំ។

## Pull Request Guidelines

### Before Submitting

1. **សាកល្បងការផ្លាស់ប្តូរ:**
   - ដើរកម្មវិធីក្នុងសៀវភៅ notebook ដែលទាក់ទងទាំងស្រុង
   - ពិនិត្យថាទម្រង់គឺដំណើរការដោយគ្មានកំហុស
   - ធ្វើការពិនិត្យមើលលទ្ធផលថាបានត្រឹមត្រូវ

2. **កែប្រែឯកសារព័ត៌មាន៖**
   - កែប្រែ `README.md` ប្រសិនបើបន្ថែមមេរៀនថ្មី
   - បន្ថែមមតិយោងនៅក្នុង notebooks សម្រាប់កូដស្មុគស្មាញ
   - គោរពឲ្យស្លឹក Markdown ពន្យល់គោលដៅ

3. **ការផ្លាស់ប្តូរឯកសារ:**
   - កុំបញ្ជូនឯកសារ `.env` (ប្រើ `.env.example`)
   - កុំបញ្ជូនថត `venv/` ឬ `__pycache__/`
   - រក្សាលទ្ធផល notebook ដែលបង្ហាញមេរៀន
   - ដកឯកសារបណ្ដោះអាសន្ន និងសៀវភៅបម្រុង (`*-backup.ipynb`)

4. **រចនាបទ និងការរៀបចំ:**
   - តាមដានការរចនាបទ និងការរៀបចំ
   - បញ្ជា `poetry run black .` និង `poetry run ruff check .` ដើម្បីពិនិត្យរចនាបទ

5. **បន្ថែម/កែប្រែសាកល្បង និងជំនួយ CLI:**
   - បន្ថែម ឬកែប្រែសាកល្បងពេលផ្លាស់ប្តូរផ្នែកសកម្មភាព
   - រក្សាជំនួយ CLI ឲ្យត្រូវគ្នានឹងការផ្លាស់ប្តូរ

### Commit message and merge strategy

យើងប្រើ Squash and Merge ជាលំនាំដើម។ សារពាក្យចុងក្រោយនៅក្នុង commit squash គួរត្រូវទៅតាម៖

```bash
<type>: <description> (#<លេខ PR>)
```

ប្រភេទបានអនុញ្ញាត៖
- `Docs` — កែប្រែឯកសារព័ត៌មាន
- `Build` — ប្រព័ន្ធកំណត់កញ្ចប់, សម្រាប់ការជំនួយ/CI
- `Core` — មុខងារ និងបច្ចេកទេសសំខាន់ (ឧ. `src/co_op_translator/core`)

ឧទាហរណ៍៖
- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

សម្គាល់ៈ
- ចំណងជើង PR សម្រាប់មួយច្រើនត្រូវបានបង្កើតដោយស្វ័យប្រវត្តិផ្អែកលើស្លាក; ជំពូកប្រដៅឲ្យមានភាពត្រឹមត្រូវ។

### PR Title Format

ប្រើចំណងជើងច្បាស់ បោយសក្តានុពលនៃតំណាង commit squash ចុងក្រោយ៖
- `Docs: Update installation instructions for clarity`
- `Core: Improve handling of image translation`

## Debugging and Troubleshooting

- បញ្ហាទូទៅ និងដោះស្រាយ៖ `getting_started/troubleshooting.md`
- ភាសាគាំទ្រ និងសម្គាល់ (រួមមានអក្សរ/បញ្ហាទទួលស្គាល់): `getting_started/supported-languages.md`
- សម្រាប់បញ្ហាដំណាក់កាលតំណភ្ជាប់ 在 notebooks, ដំណើរការ៖ `migrate-links -l "all" -y`

## Notes for Agents

- ចូលចិត្ត Poetry សម្រាប់បរិយាកាសចម្លងអាចធ្វើឡើង; ប្រសិនបើមិនដូច្នោះប្រើ `requirements.txt`។
- ពេលហៅ CLIs នៅក្នុង CI, ផ្ដល់សម្ងាត់តាមអថេរបរិស្ថាន ឬការចាក់បញ្ចូល `.env`។
- សម្រាប់អ្នកប្រើ monorepo, យោងទាំងនេះជាកញ្ចប់ឯករាជ្យ; មិនចាំបាច់មានផ្សារភ្ជាប់រង។

- ជំនួយ multi-arch: រក្សា `linux/arm64` ពេលអ្នកប្រើ ARM (Apple Silicon/ARM servers) ជាគោលដៅ; ផ្ទាំងតែ `linux/amd64` គឺគ្រប់គ្រងបានស្រួល។
- បញ្ជូនអ្នកប្រើទៅកាន់ Docker Quick Start នៅ `README.md` ពេលចូលចិត្តប្រើ containers; រួមបញ្ចូលម៉ូដែល Bash និង PowerShell ដោយសារតែភាពខុសគ្នាលើការotequoting។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**:
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងព្យាយាមឲ្យមានភាពត្រឹមត្រូវកាន់តែខ្ពស់ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិនោះអាចមានកំហុសឬការខ្វះភាពត្រឹមត្រូវ។ ឯកសារដើមនៅភាសាដំបូងគួរត្រូវបានកត់សម្គាល់ថាជារបៀបវិនិយោគដ៏មានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សជំនាញត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសរបស់ការប្រើប្រាស់ការបកប្រែនេះនោះទេ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->