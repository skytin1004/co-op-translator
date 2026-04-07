# Co-op Translator GitHub Action ಬಳಸಿ (ಸಂಸ್ಥೆಯ ಮಾರ್ಗದರ್ಶಿ)

**ಗುರಿ ಪ್ರೇಕ್ಷಕರು:** ಈ ಮಾರ್ಗದರ್ಶಿ **Microsoft ಆಂತರಿಕ ಬಳಕೆದಾರರು** ಅಥವಾ **ಪೂರ್ವ-ನಿರ್ಮಿತ Co-op Translator GitHub App ಗೆ ಅಗತ್ಯ ಪ್ರಮಾಣಪತ್ರಗಳ ಪ್ರವೇಶ ಹೊಂದಿರುವ ತಂಡಗಳು** ಅಥವಾ ತಮ್ಮದೇ ಆದ ಕಸ್ಟಮ್ GitHub App ರಚಿಸಬಹುದಾದವರು.

Co-op Translator GitHub Action ಬಳಸಿ ನಿಮ್ಮ repository ನ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಿಸಲು ಸುಲಭವಾಗಿ ಪ್ರಾರಂಭಿಸಿ. ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮ್ಮ ಮೂಲ Markdown ಫೈಲ್‌ಗಳು ಅಥವಾ ಚಿತ್ರಗಳು ಬದಲಾದಾಗ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಗಳನ್ನು ಹೊಂದಿರುವ pull request ಗಳನ್ನು ರಚಿಸಲು action ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವ ಪ್ರಕ್ರಿಯೆಯನ್ನು ವಿವರಿಸುತ್ತದೆ.

> [!IMPORTANT]
> 
> **ಸರಿಯಾದ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು:**
>
> ಈ ಮಾರ್ಗದರ್ಶಿ **GitHub App ID ಮತ್ತು Private Key** ಬಳಸಿ ಸೆಟ್ ಅಪ್ ವಿವರಿಸುತ್ತದೆ. ನೀವು ಸಾಮಾನ್ಯವಾಗಿ ಈ "ಸಂಸ್ಥೆಯ ಮಾರ್ಗದರ್ಶಿ" ವಿಧಾನವನ್ನು ಬಳಸಬೇಕಾಗುತ್ತದೆ, **`GITHUB_TOKEN` ಅನುಮತಿಗಳು ನಿರ್ಬಂಧಿತವಾಗಿದ್ದರೆ:** ನಿಮ್ಮ ಸಂಸ್ಥೆ ಅಥವಾ repository ಸೆಟ್ಟಿಂಗ್‌ಗಳು ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಗೆ ನೀಡಲಾಗುವ ಡೀಫಾಲ್ಟ್ ಅನುಮತಿಗಳನ್ನು ನಿರ್ಬಂಧಿಸುತ್ತವೆ. ವಿಶೇಷವಾಗಿ, `GITHUB_TOKEN` ಗೆ ಅಗತ್ಯವಾದ `write` ಅನುಮತಿಗಳು (ಉದಾ., `contents: write` ಅಥವಾ `pull-requests: write`) ನೀಡಲಾಗದಿದ್ದರೆ, [Public Setup Guide](./github-actions-guide-public.md) ನಲ್ಲಿ workflow ಅನುಮತಿಗಳ ಕೊರತೆಯಿಂದ ವಿಫಲವಾಗುತ್ತದೆ. ಸ್ಪಷ್ಟವಾಗಿ ನೀಡಲಾದ GitHub App ಅನುಮತಿಗಳನ್ನು ಬಳಸುವುದರಿಂದ ಈ ನಿರ್ಬಂಧವನ್ನು ಬಿಟ್ಟುಹೋಗಬಹುದು.
>
> **ಮೇಲಿನವು ನಿಮಗೆ ಅನ್ವಯಿಸದಿದ್ದರೆ:**
>
> ನಿಮ್ಮ repository ನಲ್ಲಿ ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಗೆ ಸಾಕಷ್ಟು ಅನುಮತಿಗಳು ಇದ್ದರೆ (ಅಂದರೆ, ನೀವು ಸಂಸ್ಥೆಯ ನಿರ್ಬಂಧಗಳಿಂದ ತಡೆಯಲ್ಪಟ್ಟಿಲ್ಲ), ದಯವಿಟ್ಟು **[Public Setup Guide using GITHUB_TOKEN](./github-actions-guide-public.md)** ಅನ್ನು ಬಳಸಿ. ಸಾರ್ವಜನಿಕ ಮಾರ್ಗದರ್ಶಿ App ID ಗಳನ್ನು ಅಥವಾ Private Key ಗಳನ್ನು ಪಡೆಯುವುದು ಅಥವಾ ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲದೆ, ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಮತ್ತು repository permissions ಮೇಲೆ ಮಾತ್ರ ಅವಲಂಬಿತವಾಗಿದೆ.

## ಪೂರ್ವಶರತ್ತುಗಳು

GitHub Action ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವ ಮೊದಲು, ಅಗತ್ಯ AI ಸೇವಾ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಸಿದ್ಧಪಡಿಸಿ.

**1. ಅಗತ್ಯವಿದೆ: AI Language Model ಪ್ರಮಾಣಪತ್ರಗಳು**
ನೀವು ಕನಿಷ್ಠ ಒಂದು Language Model ಗೆ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಹೊಂದಿರಬೇಕು:

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Names, API Version ಅಗತ್ಯವಿದೆ.
- **OpenAI**: API Key ಅಗತ್ಯವಿದೆ, (ಐಚ್ಛಿಕ: Org ID, Base URL, Model ID).
- ವಿವರಗಳಿಗೆ [Supported Models and Services](../../../../README.md) ನೋಡಿ.
- ಸೆಟ್ ಅಪ್ ಮಾರ್ಗದರ್ಶಿ: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. ಐಚ್ಛಿಕ: Computer Vision ಪ್ರಮಾಣಪತ್ರಗಳು (ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ)**

- ಚಿತ್ರಗಳಲ್ಲಿ ಇರುವ ಪಠ್ಯವನ್ನು ಅನುವಾದಿಸಲು ಅಗತ್ಯವಿದೆ.
- **Azure Computer Vision**: Endpoint ಮತ್ತು Subscription Key ಅಗತ್ಯವಿದೆ.
- ಇದನ್ನು ಒದಗಿಸದಿದ್ದರೆ, action [Markdown-only mode](../markdown-only-mode.md) ಗೆ ಡೀಫಾಲ್ಟ್ ಆಗುತ್ತದೆ.
- ಸೆಟ್ ಅಪ್ ಮಾರ್ಗದರ್ಶಿ: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## ಸೆಟ್ ಅಪ್ ಮತ್ತು ಕಾನ್ಫಿಗರೇಶನ್

ನಿಮ್ಮ repository ನಲ್ಲಿ Co-op Translator GitHub Action ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಲು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ:

### ಹಂತ 1: GitHub App Authentication ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ ಮತ್ತು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ

workflow ನಿಮ್ಮ ಪರವಾಗಿ ನಿಮ್ಮ repository (ಉದಾ., pull requests ರಚಿಸಲು) ಸುರಕ್ಷಿತವಾಗಿ ಸಂವಹನ ಮಾಡಲು GitHub App authentication ಅನ್ನು ಬಳಸುತ್ತದೆ. ಒಂದು ಆಯ್ಕೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ:

#### **ಆಯ್ಕೆ A: ಪೂರ್ವ-ನಿರ್ಮಿತ Co-op Translator GitHub App ಅನ್ನು ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ (Microsoft ಆಂತರಿಕ ಬಳಕೆಗಾಗಿ)**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) ಪುಟಕ್ಕೆ ಹೋಗಿ.

1. **Install** ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಗುರಿ repository ಇರುವ ಖಾತೆ ಅಥವಾ ಸಂಸ್ಥೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.

    ![Install app](../../../../getting_started/github-actions-guide/imgs/install-app.png)

1. **Only select repositories** ಆಯ್ಕೆ ಮಾಡಿ ಮತ್ತು ನಿಮ್ಮ ಗುರಿ repository (ಉದಾ., `PhiCookBook`) ಆಯ್ಕೆಮಾಡಿ. **Install** ಕ್ಲಿಕ್ ಮಾಡಿ. ನೀವು authenticate ಮಾಡಲು ಕೇಳಬಹುದು.

    ![Install authorize](../../../../getting_started/github-actions-guide/imgs/install-authorize.png)

1. **App Credentials ಪಡೆಯಿರಿ (ಆಂತರಿಕ ಪ್ರಕ್ರಿಯೆ ಅಗತ್ಯವಿದೆ):** workflow ಗೆ app ಆಗಿ authenticate ಮಾಡಲು, ನಿಮಗೆ Co-op Translator ತಂಡದಿಂದ ಒದಗಿಸಲಾದ ಎರಡು ಮಾಹಿತಿಗಳು ಬೇಕಾಗುತ್ತದೆ:
  - **App ID:** Co-op Translator app ಗೆ ಅನನ್ಯ ಗುರುತಿನ ಸಂಖ್ಯೆ. App ID: `1164076`.
  - **Private Key:** `.pem` private key ಫೈಲ್‌ನ **ಪೂರ್ಣ ವಿಷಯವನ್ನು** maintainer ಸಂಪರ್ಕದಿಂದ ಪಡೆಯಬೇಕು. **ಈ key ಅನ್ನು ಪಾಸ್ವರ್ಡ್‌ನಂತೆ ಸಂರಕ್ಷಿಸಿ ಮತ್ತು ಸುರಕ್ಷಿತವಾಗಿ ಇಟ್ಟುಕೊಳ್ಳಿ.**

1. ಹಂತ 2 ಗೆ ಮುಂದುವರಿಯಿರಿ.

#### **ಆಯ್ಕೆ B: ನಿಮ್ಮದೇ ಆದ ಕಸ್ಟಮ್ GitHub App ಬಳಸಿ**

- ನೀವು ಬಯಸಿದರೆ, ನಿಮ್ಮದೇ GitHub App ರಚಿಸಿ ಮತ್ತು ಕಾನ್ಫಿಗರ್ ಮಾಡಬಹುದು. ಇದು Contents ಮತ್ತು Pull requests ಗೆ Read & write access ಹೊಂದಿರಬೇಕು. ನೀವು ಇದರ App ID ಮತ್ತು Private Key ಅನ್ನು ರಚಿಸಬೇಕು.

### ಹಂತ 2: Repository Secrets ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ

GitHub App ಪ್ರಮಾಣಪತ್ರಗಳು ಮತ್ತು ನಿಮ್ಮ AI ಸೇವಾ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು repository ಸೆಟ್ಟಿಂಗ್‌ಗಳಲ್ಲಿ ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಿದ secrets ಆಗಿ ಸೇರಿಸಬೇಕು.

1. ನಿಮ್ಮ ಗುರಿ GitHub repository (ಉದಾ., `PhiCookBook`) ಗೆ ಹೋಗಿ.

1. **Settings** > **Secrets and variables** > **Actions** ಗೆ ಹೋಗಿ.

1. **Repository secrets** ಅಡಿಯಲ್ಲಿ, ಕೆಳಗಿನ ಪ್ರತಿ secret ಗೆ **New repository secret** ಕ್ಲಿಕ್ ಮಾಡಿ.

   ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png)

**GitHub App Authentication ಗೆ ಅಗತ್ಯವಿರುವ Secrets:**

| Secret Name          | ವಿವರಣೆ                                      | ಮೌಲ್ಯದ ಮೂಲ                                     |
| :------------------- | :------------------------------------------- | :--------------------------------------------- |
| `GH_APP_ID`          | GitHub App ನ App ID (ಹಂತ 1 ರಿಂದ).           | GitHub App Settings                              |
| `GH_APP_PRIVATE_KEY` | ಡೌನ್‌ಲೋಡ್ ಮಾಡಿದ `.pem` ಫೈಲ್‌ನ **ಪೂರ್ಣ ವಿಷಯ**. | `.pem` ಫೈಲ್ (ಹಂತ 1 ರಿಂದ)                      |

**AI Service Secrets (ನಿಮ್ಮ ಪೂರ್ವಶರತ್ತುಗಳ ಆಧಾರದ ಮೇಲೆ ಎಲ್ಲಾ ಸೇರಿಸಿ):**

| Secret Name                         | ವಿವರಣೆ                               | ಮೌಲ್ಯದ ಮೂಲ                     |
| :---------------------------------- | :------------------------------------ | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) ಗೆ Key  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) ಗೆ Endpoint | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI ಸೇವೆಗೆ Key              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI ಸೇವೆಗೆ Endpoint         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | ನಿಮ್ಮ Azure OpenAI Model Name         | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | ನಿಮ್ಮ Azure OpenAI Deployment Name    | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI ಗೆ API Version          | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | OpenAI ಗೆ API Key                    | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID               | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | OpenAI ಗೆ ವಿಶೇಷ Model ID            | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | OpenAI API ಗೆ ಕಸ್ಟಮ್ Base URL         | OpenAI Platform                    |

![Enter environment variable name](../../../../getting_started/github-actions-guide/imgs/add-secrets-done.png)

### ಹಂತ 3: Workflow ಫೈಲ್ ರಚಿಸಿ

ಕೊನೆಗೆ, automated workflow ಅನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವ YAML ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ.

1. ನಿಮ್ಮ repository ನ root ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ `.github/workflows/` ಡೈರೆಕ್ಟರಿಯನ್ನು ರಚಿಸಿ (ಇದು ಇಲ್ಲದಿದ್ದರೆ).

1. `.github/workflows/` ಒಳಗೆ, `co-op-translator.yml` ಎಂಬ ಫೈಲ್ ರಚಿಸಿ.

1. co-op-translator.yml ಗೆ ಕೆಳಗಿನ ವಿಷಯವನ್ನು ಪೇಸ್ಟ್ ಮಾಡಿ.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **Workflow ಅನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ:**
  - **[!IMPORTANT] Target Languages:** `Run Co-op Translator` ಹಂತದಲ್ಲಿ, ನೀವು **`translate -l "..." -y` ಆಜ್ಞೆಯಲ್ಲಿನ ಭಾಷಾ ಕೋಡ್‌ಗಳ ಪಟ್ಟಿ** ಅನ್ನು ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್‌ನ ಅಗತ್ಯಗಳಿಗೆ ಹೊಂದಿಸಲು ಪರಿಶೀಲಿಸಿ ಮತ್ತು ತಿದ್ದುಪಡಿಸಬೇಕು. ಉದಾಹರಣೆಯ ಪಟ್ಟಿ (`ar de es...`) ಅನ್ನು ಬದಲಾಯಿಸಬೇಕು ಅಥವಾ ಹೊಂದಿಸಬೇಕು.
  - **Trigger (`on:`):** ಪ್ರಸ್ತುತ trigger ಪ್ರತಿ push ಗೆ `main` ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ. ದೊಡ್ಡ repository ಗಳಿಗೆ, `paths:` ಫಿಲ್ಟರ್ ಅನ್ನು ಸೇರಿಸುವುದನ್ನು ಪರಿಗಣಿಸಿ (YAML ನಲ್ಲಿ ಕಾಮೆಂಟ್ ಮಾಡಿದ ಉದಾಹರಣೆಯನ್ನು ನೋಡಿ) workflow ಅನ್ನು ಸಂಬಂಧಿತ ಫೈಲ್‌ಗಳು (ಉದಾ., ಮೂಲ ಡಾಕ್ಯುಮೆಂಟೇಶನ್) ಬದಲಾದಾಗ ಮಾತ್ರ ಕಾರ್ಯನಿರ್ವಹಿಸಲು, runner ನಿಮಿಷಗಳನ್ನು ಉಳಿಸಲು.
  - **PR ವಿವರಗಳು:** `Create Pull Request` ಹಂತದಲ್ಲಿ `commit-message`, `title`, `body`, `branch` ಹೆಸರು, ಮತ್ತು `labels` ಅನ್ನು ಅಗತ್ಯವಿದ್ದರೆ ಕಸ್ಟಮೈಸ್ ಮಾಡಿ.

## ಪ್ರಮಾಣಪತ್ರ ನಿರ್ವಹಣೆ ಮತ್ತು ನವೀಕರಣ

- **ಸುರಕ್ಷತೆ:** ಸಂವೇದನಶೀಲ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು (API keys, private keys) ಯಾವಾಗಲೂ GitHub Actions secrets ಆಗಿ ಸಂಗ್ರಹಿಸಿ. ಅವುಗಳನ್ನು ನಿಮ್ಮ workflow ಫೈಲ್ ಅಥವಾ repository ಕೋಡ್‌ನಲ್ಲಿ ಬಹಿರಂಗಪಡಿಸಬೇಡಿ.
- **[!IMPORTANT] Key Renewal (Microsoft ಆಂತರಿಕ ಬಳಕೆದಾರರು):** Microsoft ಒಳಗೆ ಬಳಸುವ Azure OpenAI key ಗೆ ಕಡ್ಡಾಯ ನವೀಕರಣ ನೀತಿ (ಉದಾ., ಪ್ರತಿ 5 ತಿಂಗಳು) ಇರಬಹುದು. workflow ವಿಫಲವಾಗದಂತೆ **ಅವುಗಳ ಅವಧಿ ಮುಗಿಯುವ ಮೊದಲು** GitHub secrets (`AZURE_OPENAI_...` keys) ಅನ್ನು ನವೀಕರಿಸಿ.

## Workflow ಅನ್ನು ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು

> [!WARNING]  
> **GitHub-hosted Runner ಸಮಯದ ಮಿತಿಯು:**  
> `ubuntu-latest` ಮುಂತಾದ GitHub-hosted runners ಗೆ **ಅತೀ ಹೆಚ್ಚು ಕಾರ್ಯನಿರ್ವಹಣಾ ಸಮಯದ ಮಿತಿ 6 ಗಂಟೆಗಳು** ಇದೆ.  
> ದೊಡ್ಡ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ repository ಗಳಿಗೆ, ಅನುವಾದ ಪ್ರಕ್ರಿಯೆ 6 ಗಂಟೆಗಳನ್ನು ಮೀರಿದರೆ, workflow ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರದ್ದುಗೊಳ್ಳುತ್ತದೆ.  
> ಇದನ್ನು ತಡೆಯಲು, ಪರಿಗಣಿಸಿ:  
> - **Self-hosted runner** ಬಳಸಿ (ಸಮಯದ ಮಿತಿ ಇಲ್ಲ)  
> - ಪ್ರತಿ ಕಾರ್ಯನಿರ್ವಹಣೆಗೆ ಗುರಿ ಭಾಷೆಗಳ ಸಂಖ್ಯೆಯನ್ನು ಕಡಿಮೆ ಮಾಡುವುದು

`co-op-translator.yml` ಫೈಲ್ ನಿಮ್ಮ main branch ಗೆ (ಅಥವಾ `on:` trigger ನಲ್ಲಿ ನಿರ್ದಿಷ್ಟಪಡಿಸಿದ branch ಗೆ) ಮರ್ಜ್ ಮಾಡಿದ ನಂತರ, ಈ workflow ಆ branch ಗೆ push ಮಾಡಿದಾಗ (ಮತ್ತು `paths` ಫಿಲ್ಟರ್ ಹೊಂದಿದ್ದರೆ, ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಫೈಲ್‌ಗಳಿಗೆ ಹೊಂದಾಣಿಕೆ) ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

ಅನುವಾದಗಳು ರಚಿಸಲ್ಪಟ್ಟಿದ್ದರೆ ಅಥವಾ ನವೀಕರಿಸಲ್ಪಟ್ಟಿದ್ದರೆ, action ಬದಲಾವಣೆಗಳನ್ನು ಹೊಂದಿರುವ Pull Request ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರಚಿಸುತ್ತದೆ, ನಿಮ್ಮ ಪರಿಶೀಲನೆ ಮತ್ತು ಮರ್ಜ್ ಮಾಡಲು ಸಿದ್ಧವಾಗಿದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮಾಕ್ಷ್ಯತೆ**:  
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮಾಕ್ಷ್ಯತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವುದರಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->