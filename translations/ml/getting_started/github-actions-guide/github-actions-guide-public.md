# Co-op Translator GitHub Action ഉപയോഗിച്ച് (പബ്ലിക് സെറ്റപ്പ്)

**ലക്ഷ്യ പ്രേക്ഷകർ:** സാധാരണ GitHub Actions അനുമതികൾ മതിയാകുന്ന പൊതുവായ അല്ലെങ്കിൽ സ്വകാര്യ റിപോസിറ്ററികളിലെ ഉപയോക്താക്കൾക്കായി ഈ മാർഗ്ഗനിർദ്ദേശം ഉദ്ദേശിച്ചിരിക്കുന്നു. ഇത് ഉൾനിർമ്മിത `GITHUB_TOKEN` ഉപയോഗിക്കുന്നു.

നിങ്ങളുടെ റിപോസിറ്ററിയിലെ ഡോക്യുമെന്റേഷൻ സ്വയംമാറ്റം ചെയ്യാൻ Co-op Translator GitHub Action ഉപയോഗിച്ച് എളുപ്പത്തിൽ ഓട്ടോമേറ്റ് ചെയ്യുക. നിങ്ങളുടെ സോഴ്‌സ് Markdown ഫയലുകൾ അല്ലെങ്കിൽ ചിത്രങ്ങൾ മാറ്റുമ്പോൾ അപ്ഡേറ്റ് ചെയ്ത വിവർത്തനങ്ങളുള്ള പുൾ റിക്വസ്റ്റുകൾ സ്വയം സൃഷ്ടിക്കാൻ ആക്ഷൻ സെറ്റപ്പ് ചെയ്യുന്നതിന് ഈ മാർഗ്ഗനിർദ്ദേശം നിങ്ങളെ സഹായിക്കുന്നു.

> [!IMPORTANT]
>
> **ശരിയായ മാർഗ്ഗനിർദ്ദേശം തിരഞ്ഞെടുക്കൽ:**
>
> ഈ മാർഗ്ഗനിർദ്ദേശം **സാധാരണ `GITHUB_TOKEN` ഉപയോഗിച്ച് ലളിതമായ സെറ്റപ്പ്** വിശദീകരിക്കുന്നു. ഇത് കൂടുതൽ ഉപയോക്താക്കൾക്കായി ശുപാർശ ചെയ്യപ്പെടുന്ന രീതിയാണ്, കാരണം ഇത് സങ്കീർണ്ണമായ GitHub App Private Keys കൈകാര്യം ചെയ്യേണ്ടതില്ല.
>

## മുൻ‌വശങ്ങൾ

GitHub Action കോൺഫിഗർ ചെയ്യുന്നതിന് മുമ്പ്, ആവശ്യമായ AI സേവന ക്രെഡൻഷ്യലുകൾ തയ്യാറായിരിക്കണം.

**1. ആവശ്യമായത്: AI ഭാഷാ മോഡൽ ക്രെഡൻഷ്യലുകൾ**
കുറഞ്ഞത് ഒരു പിന്തുണയുള്ള ഭാഷാ മോഡലിനുള്ള ക്രെഡൻഷ്യലുകൾ നിങ്ങൾക്ക് ആവശ്യമാണ്:

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Names, API Version ആവശ്യമാണ്.
- **OpenAI**: API Key ആവശ്യമാണ്, (ഓപ്ഷണൽ: Org ID, Base URL, Model ID).
- വിശദാംശങ്ങൾക്കായി [Supported Models and Services](../../../../README.md) കാണുക.

**2. ഓപ്ഷണൽ: AI Vision ക്രെഡൻഷ്യലുകൾ (ചിത്ര വിവർത്തനത്തിനായി)**

- ചിത്രങ്ങളിലെ ടെക്സ്റ്റ് വിവർത്തനം ചെയ്യേണ്ടതുണ്ടെങ്കിൽ മാത്രമേ ആവശ്യമായുള്ളൂ.
- **Azure AI Vision**: Endpoint, Subscription Key ആവശ്യമാണ്.
- ഇത് നൽകാത്ത പക്ഷം, ആക്ഷൻ [Markdown-only mode](../markdown-only-mode.md) ആയി ഡിഫോൾട്ട് ചെയ്യും.

## സെറ്റപ്പ് & കോൺഫിഗറേഷൻ

സാധാരണ `GITHUB_TOKEN` ഉപയോഗിച്ച് Co-op Translator GitHub Action നിങ്ങളുടെ റിപോസിറ്ററിയിൽ കോൺഫിഗർ ചെയ്യുന്നതിന് ഈ ഘട്ടങ്ങൾ പിന്തുടരുക.

### ഘട്ടം 1: Authentication (Using `GITHUB_TOKEN`) മനസ്സിലാക്കുക

ഈ workflow GitHub Actions നൽകുന്ന ഉൾനിർമ്മിത `GITHUB_TOKEN` ഉപയോഗിക്കുന്നു. **ഘട്ടം 3**-ൽ കോൺഫിഗർ ചെയ്ത സെറ്റിംഗുകൾ അടിസ്ഥാനമാക്കി നിങ്ങളുടെ റിപോസിറ്ററിയുമായി workflow ഇടപെടാൻ ഈ ടോക്കൻ സ്വയം അനുമതികൾ നൽകുന്നു.

### ഘട്ടം 2: Repository Secrets കോൺഫിഗർ ചെയ്യുക

നിങ്ങളുടെ **AI സേവന ക്രെഡൻഷ്യലുകൾ** മാത്രമേ repository settings-ൽ എൻക്രിപ്റ്റ് ചെയ്ത രഹസ്യങ്ങൾ ആയി ചേർക്കേണ്ടതുള്ളൂ.

1.  നിങ്ങളുടെ ലക്ഷ്യ GitHub റിപോസിറ്ററിയിലേക്ക് പോകുക.
2.  **Settings** > **Secrets and variables** > **Actions** എന്നതിലേക്ക് പോകുക.
3.  **Repository secrets**-ൽ, താഴെ നൽകിയിരിക്കുന്ന ഓരോ ആവശ്യമായ AI സേവന രഹസ്യത്തിനും **New repository secret** ക്ലിക്ക് ചെയ്യുക.

    ![സെറ്റിംഗ് ആക്ഷൻ തിരഞ്ഞെടുക്കുക](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(ചിത്രം: രഹസ്യങ്ങൾ എവിടെ ചേർക്കണമെന്ന് കാണിക്കുന്നു)*

**ആവശ്യമായ AI സേവന രഹസ്യങ്ങൾ (മുൻ‌വശങ്ങൾ അടിസ്ഥാനമാക്കി ബാധകമായവ എല്ലാം ചേർക്കുക):**

| രഹസ്യത്തിന്റെ പേര്                  | വിവരണം                                | മൂല്യത്തിന്റെ ഉറവിടം              |
| :---------------------------------- | :------------------------------------- | :-------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) നുള്ള Key | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) നുള്ള Endpoint | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI സേവനത്തിനുള്ള Key         | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI സേവനത്തിനുള്ള Endpoint    | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_OPENAI_MODEL_NAME`           | നിങ്ങളുടെ Azure OpenAI മോഡൽ പേര്     | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | നിങ്ങളുടെ Azure OpenAI Deployment Name | നിങ്ങളുടെ Azure AI Foundry         |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API Version               | നിങ്ങളുടെ Azure AI Foundry         |
| `OPENAI_API_KEY`                    | OpenAI-നുള്ള API Key                   | നിങ്ങളുടെ OpenAI Platform         |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID (ഓപ്ഷണൽ)      | നിങ്ങളുടെ OpenAI Platform         |
| `OPENAI_CHAT_MODEL_ID`              | പ്രത്യേക OpenAI മോഡൽ ID (ഓപ്ഷണൽ)     | നിങ്ങളുടെ OpenAI Platform         |
| `OPENAI_BASE_URL`                   | കസ്റ്റം OpenAI API Base URL (ഓപ്ഷണൽ)   | നിങ്ങളുടെ OpenAI Platform         |

### ഘട്ടം 3: Workflow Permissions കോൺഫിഗർ ചെയ്യുക

GitHub Action-ന് `GITHUB_TOKEN` വഴി കോഡ് പരിശോധിക്കാനും പുൾ റിക്വസ്റ്റുകൾ സൃഷ്ടിക്കാനും അനുമതികൾ നൽകേണ്ടതുണ്ട്.

1.  നിങ്ങളുടെ റിപോസിറ്ററിയിൽ **Settings** > **Actions** > **General** എന്നതിലേക്ക് പോകുക.
2.  **Workflow permissions** വിഭാഗത്തിലേക്ക് സ്ക്രോൾ ചെയ്യുക.
3.  **Read and write permissions** തിരഞ്ഞെടുക്കുക. ഇത് workflow-യ്ക്ക് ആവശ്യമായ `contents: write` & `pull-requests: write` permissions നൽകുന്നു.
4.  **Allow GitHub Actions to create and approve pull requests** എന്നതിന്റെ checkbox **ചെക്ക് ചെയ്യുക**.
5.  **Save** തിരഞ്ഞെടുക്കുക.

![Permission setting](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### ഘട്ടം 4: Workflow ഫയൽ സൃഷ്ടിക്കുക

അവസാനമായി, `GITHUB_TOKEN` ഉപയോഗിച്ച് ഓട്ടോമേറ്റഡ് workflow നിർവചിക്കുന്ന YAML ഫയൽ സൃഷ്ടിക്കുക.

1.  നിങ്ങളുടെ റിപോസിറ്ററിയുടെ റൂട്ട് ഡയറക്ടറിയിൽ `.github/workflows/` ഡയറക്ടറി ഇല്ലെങ്കിൽ സൃഷ്ടിക്കുക.
2.  `.github/workflows/`-ൽ, `co-op-translator.yml` എന്ന പേരിൽ ഒരു ഫയൽ സൃഷ്ടിക്കുക.
3.  താഴെ നൽകിയ ഉള്ളടക്കം `co-op-translator.yml`-ൽ പേസ്റ്റ് ചെയ്യുക.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Workflow കസ്റ്റമൈസ് ചെയ്യുക:**
  - **[!IMPORTANT] ലക്ഷ്യ ഭാഷകൾ:** `Run Co-op Translator` ഘട്ടത്തിൽ, നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ ആവശ്യകതകൾക്ക് അനുയോജ്യമായ ഭാഷാ കോഡുകളുടെ പട്ടിക **നോക്കുകയും മാറ്റുകയും** ചെയ്യേണ്ടതുണ്ട്. ഉദാഹരണ പട്ടിക (`ar de es...`) മാറ്റുകയോ ക്രമീകരിക്കുകയോ ചെയ്യേണ്ടതുണ്ട്.
  - **Trigger (`on:`):** നിലവിലെ trigger `main`-ലേക്ക് ഓരോ push-ലും പ്രവർത്തിക്കുന്നു. വലിയ റിപോസിറ്ററികൾക്കായി, workflow പ്രാസംഗികമായ ഫയലുകൾ (ഉദാ: സോഴ്‌സ് ഡോക്യുമെന്റേഷൻ) മാറ്റുമ്പോൾ മാത്രം പ്രവർത്തിക്കാൻ `paths:` ഫിൽട്ടർ ചേർക്കുക (YAML-ൽ കമന്റുചെയ്ത ഉദാഹരണം കാണുക), runner minutes സംരക്ഷിക്കുന്നു.
  - **PR വിശദാംശങ്ങൾ:** `Create Pull Request` ഘട്ടത്തിൽ `commit-message`, `title`, `body`, `branch` name, `labels` എന്നിവ ആവശ്യാനുസരണം കസ്റ്റമൈസ് ചെയ്യുക.

## Workflow പ്രവർത്തിപ്പിക്കൽ

> [!WARNING]  
> **GitHub-hosted Runner Time Limit:**  
> `ubuntu-latest` പോലുള്ള GitHub-hosted runners-ന് **പരമാവധി പ്രവർത്തന സമയ പരിധി 6 മണിക്കൂർ**.  
> വലിയ ഡോക്യുമെന്റേഷൻ റിപോസിറ്ററികൾക്കായി, വിവർത്തന പ്രക്രിയ 6 മണിക്കൂറിൽ കൂടുതൽ നീണ്ടാൽ workflow സ്വയം അവസാനിപ്പിക്കും.  
> ഇത് തടയാൻ, പരിഗണിക്കുക:  
> - **Self-hosted runner** ഉപയോഗിക്കുക (സമയം പരിധിയില്ല)  
> - ഓരോ റൺ-ലും ലക്ഷ്യ ഭാഷകളുടെ എണ്ണം കുറയ്ക്കുക

`co-op-translator.yml` ഫയൽ നിങ്ങളുടെ main branch-ലേക്ക് (അല്ലെങ്കിൽ `on:` trigger-ൽ വ്യക്തമാക്കിയ ബ്രാഞ്ചിലേക്ക്) മർജ് ചെയ്താൽ, workflow ആ ബ്രാഞ്ചിലേക്ക് മാറ്റങ്ങൾ push ചെയ്യുമ്പോൾ (കോണ്ഫിഗർ ചെയ്ത `paths` ഫിൽട്ടർ പൊരുത്തപ്പെടുന്നുവെങ്കിൽ) സ്വയം പ്രവർത്തിക്കും.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അറിയിപ്പ്**:  
ഈ പ്രമാണം AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്കായി ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാൻ സാധ്യതയുണ്ട്. പ്രമാണത്തിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ പതിപ്പ് പ്രാമാണികമായ ഉറവിടമായി പരിഗണിക്കണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ചെയ്യുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന തെറ്റിദ്ധാരണകൾ അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കായി ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->