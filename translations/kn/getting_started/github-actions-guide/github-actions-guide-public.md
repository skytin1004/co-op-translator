# Co-op Translator GitHub Action ಬಳಸಿ (ಸಾರ್ವಜನಿಕ ಸೆಟಪ್)

**ಗುರಿ ಪ್ರೇಕ್ಷಕರು:** ಈ ಮಾರ್ಗದರ್ಶಿ ಸಾಮಾನ್ಯ GitHub Actions ಅನುಮತಿಗಳು ಸಾಕಾಗುವ ಬಹುತೇಕ ಸಾರ್ವಜನಿಕ ಅಥವಾ ಖಾಸಗಿ ರೆಪೊಸಿಟರಿಗಳ ಬಳಕೆದಾರರಿಗೆ ಉದ್ದೇಶಿಸಲಾಗಿದೆ. ಇದು ಅಂತರ್ನಿಹಿತ `GITHUB_TOKEN` ಅನ್ನು ಬಳಸುತ್ತದೆ.

ನಿಮ್ಮ ರೆಪೊಸಿಟರಿಯ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ಅನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಅನುವಾದಿಸಲು Co-op Translator GitHub Action ಅನ್ನು ಬಳಸಬಹುದು. ಈ ಮಾರ್ಗದರ್ಶಿ ನಿಮ್ಮ ಮೂಲ Markdown ಫೈಲ್‌ಗಳು ಅಥವಾ ಚಿತ್ರಗಳು ಬದಲಾದಾಗ ನವೀಕರಿಸಿದ ಅನುವಾದಗಳೊಂದಿಗೆ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್‌ಗಳನ್ನು ರಚಿಸಲು ಆಕ್ಷನ್ ಅನ್ನು ಸೆಟಪ್ ಮಾಡುವುದು ಹೇಗೆ ಎಂಬುದನ್ನು ವಿವರಿಸುತ್ತದೆ.

> [!IMPORTANT]
>
> **ಸರಿಯಾದ ಮಾರ್ಗದರ್ಶಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು:**
>
> ಈ ಮಾರ್ಗದರ್ಶಿ **ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಬಳಸಿ ಸರಳ ಸೆಟಪ್** ಅನ್ನು ವಿವರಿಸುತ್ತದೆ. ಇದು ಹೆಚ್ಚಿನ ಬಳಕೆದಾರರಿಗೆ ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ ಏಕೆಂದರೆ ಇದು ಸಂವೇದನಶೀಲ GitHub App ಖಾಸಗಿ ಕೀಗಳನ್ನು ನಿರ್ವಹಿಸುವ ಅಗತ್ಯವಿಲ್ಲ.
>

## ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳು

GitHub Action ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡುವ ಮೊದಲು, ಅಗತ್ಯ AI ಸೇವಾ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು ಸಿದ್ಧವಾಗಿಡಿ.

**1. ಅಗತ್ಯವಿದೆ: AI ಭಾಷಾ ಮಾದರಿ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳು**
ನೀವು ಕನಿಷ್ಠ ಒಂದು ಬೆಂಬಲಿತ ಭಾಷಾ ಮಾದರಿಗಾಗಿ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು ಹೊಂದಿರಬೇಕು:

- **Azure OpenAI**: ಎಂಡ್‌ಪಾಯಿಂಟ್, API ಕೀ, ಮಾದರಿ/ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರುಗಳು, API ಆವೃತ್ತಿ ಅಗತ್ಯವಿದೆ.
- **OpenAI**: API ಕೀ ಅಗತ್ಯವಿದೆ, (ಐಚ್ಛಿಕ: Org ID, Base URL, Model ID).
- ವಿವರಗಳಿಗೆ [Supported Models and Services](../../../../README.md) ನೋಡಿ.

**2. ಐಚ್ಛಿಕ: AI Vision ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳು (ಚಿತ್ರ ಅನುವಾದಕ್ಕಾಗಿ)**

- ಚಿತ್ರಗಳಲ್ಲಿ ಪಠ್ಯವನ್ನು ಅನುವಾದಿಸಲು ಅಗತ್ಯವಿದೆ.
- **Azure AI Vision**: ಎಂಡ್‌ಪಾಯಿಂಟ್ ಮತ್ತು ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಕೀ ಅಗತ್ಯವಿದೆ.
- ಒದಗಿಸಲಾಗದಿದ್ದರೆ, ಆಕ್ಷನ್ [Markdown-only mode](../markdown-only-mode.md) ಗೆ ಡೀಫಾಲ್ಟ್ ಆಗುತ್ತದೆ.

## ಸೆಟಪ್ ಮತ್ತು ಕಾನ್ಫಿಗರೇಶನ್

ಸಾಮಾನ್ಯ `GITHUB_TOKEN` ಬಳಸಿ ನಿಮ್ಮ ರೆಪೊಸಿಟರಿಯಲ್ಲಿ Co-op Translator GitHub Action ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಲು ಈ ಹಂತಗಳನ್ನು ಅನುಸರಿಸಿ.

### ಹಂತ 1: ಪ್ರಾಮಾಣೀಕರಣವನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿ (`GITHUB_TOKEN` ಬಳಸಿ)

ಈ ವರ್ಕ್‌ಫ್ಲೋ GitHub Actions ಒದಗಿಸುವ ಅಂತರ್ನಿಹಿತ `GITHUB_TOKEN` ಅನ್ನು ಬಳಸುತ್ತದೆ. ಈ ಟೋಕನ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ **ಹಂತ 3** ನಲ್ಲಿ ಕಾನ್ಫಿಗರ್ ಮಾಡಿದ ಸೆಟ್ಟಿಂಗ್‌ಗಳ ಆಧಾರದ ಮೇಲೆ ನಿಮ್ಮ ರೆಪೊಸಿಟರಿಯೊಂದಿಗೆ ಸಂವಹನ ಮಾಡಲು ವರ್ಕ್‌ಫ್ಲೋಗೆ ಅನುಮತಿಗಳನ್ನು ನೀಡುತ್ತದೆ.

### ಹಂತ 2: ರೆಪೊಸಿಟರಿ ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ

ನೀವು ನಿಮ್ಮ **AI ಸೇವಾ ಕ್ರೆಡೆನ್ಷಿಯಲ್‌ಗಳನ್ನು** ನಿಮ್ಮ ರೆಪೊಸಿಟರಿ ಸೆಟ್ಟಿಂಗ್‌ಗಳಲ್ಲಿ ಎನ್‌ಕ್ರಿಪ್ಟ್ ಮಾಡಿದ ಸೀಕ್ರೆಟ್‌ಗಳಾಗಿ ಸೇರಿಸಬೇಕು.

1.  ನಿಮ್ಮ ಗುರಿ GitHub ರೆಪೊಸಿಟರಿಯ ಕಡೆಗೆ ಹೋಗಿ.
2.  **Settings** > **Secrets and variables** > **Actions** ಗೆ ಹೋಗಿ.
3.  **Repository secrets** ಅಡಿಯಲ್ಲಿ, ಕೆಳಗಿನ ಅಗತ್ಯ AI ಸೇವಾ ಸೀಕ್ರೆಟ್‌ಗಳಿಗಾಗಿ **New repository secret** ಕ್ಲಿಕ್ ಮಾಡಿ.

    ![ಸೆಟ್ಟಿಂಗ್ ಆಕ್ಷನ್ ಆಯ್ಕೆಮಾಡಿ](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(ಚಿತ್ರ ಉಲ್ಲೇಖ: ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು ಸೇರಿಸುವ ಸ್ಥಳವನ್ನು ತೋರಿಸುತ್ತದೆ)*

**ಅಗತ್ಯ AI ಸೇವಾ ಸೀಕ್ರೆಟ್‌ಗಳು (ನಿಮ್ಮ ಪೂರ್ವಾಪೇಕ್ಷಿತಗಳ ಆಧಾರದ ಮೇಲೆ ಅನ್ವಯಿಸುವ ಎಲ್ಲಾ ಸೀಕ್ರೆಟ್‌ಗಳನ್ನು ಸೇರಿಸಿ):**

| ಸೀಕ್ರೆಟ್ ಹೆಸರು                         | ವಿವರಣೆ                               | ಮೌಲ್ಯ ಮೂಲ                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) ಗೆ ಕೀ  | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) ಗೆ ಎಂಡ್‌ಪಾಯಿಂಟ್ | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI ಸೇವೆಗೆ ಕೀ              | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI ಸೇವೆಗೆ ಎಂಡ್‌ಪಾಯಿಂಟ್         | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | ನಿಮ್ಮ Azure OpenAI ಮಾದರಿ ಹೆಸರು              | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | ನಿಮ್ಮ Azure OpenAI ಡಿಪ್ಲಾಯ್‌ಮೆಂಟ್ ಹೆಸರು         | ನಿಮ್ಮ Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI ಗೆ API ಆವೃತ್ತಿ              | ನಿಮ್ಮ Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI ಗೆ API ಕೀ                        | ನಿಮ್ಮ OpenAI ಪ್ಲಾಟ್‌ಫಾರ್ಮ್              |
| `OPENAI_ORG_ID`                     | OpenAI ಸಂಸ್ಥೆ ID (ಐಚ್ಛಿಕ)         | ನಿಮ್ಮ OpenAI ಪ್ಲಾಟ್‌ಫಾರ್ಮ್              |
| `OPENAI_CHAT_MODEL_ID`              | ನಿರ್ದಿಷ್ಟ OpenAI ಮಾದರಿ ID (ಐಚ್ಛಿಕ)       | ನಿಮ್ಮ OpenAI ಪ್ಲಾಟ್‌ಫಾರ್ಮ್              |
| `OPENAI_BASE_URL`                   | ಕಸ್ಟಮ್ OpenAI API Base URL (ಐಚ್ಛಿಕ)     | ನಿಮ್ಮ OpenAI ಪ್ಲಾಟ್‌ಫಾರ್ಮ್              |

### ಹಂತ 3: ವರ್ಕ್‌ಫ್ಲೋ ಅನುಮತಿಗಳನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ

GitHub Action ಈ ವರ್ಕ್‌ಫ್ಲೋಗೆ ಕೋಡ್ ಅನ್ನು ಚೆಕ್‌ಔಟ್ ಮಾಡಲು ಮತ್ತು ಪುಲ್ ರಿಕ್ವೆಸ್ಟ್‌ಗಳನ್ನು ರಚಿಸಲು `GITHUB_TOKEN` ಮೂಲಕ ಅನುಮತಿಗಳನ್ನು ನೀಡಬೇಕಾಗಿದೆ.

1.  ನಿಮ್ಮ ರೆಪೊಸಿಟರಿಯಲ್ಲಿ, **Settings** > **Actions** > **General** ಗೆ ಹೋಗಿ.
2.  **Workflow permissions** ವಿಭಾಗದ ಕಡೆಗೆ ಸ್ಕ್ರೋಲ್ ಮಾಡಿ.
3.  **Read and write permissions** ಆಯ್ಕೆಮಾಡಿ. ಇದು ಈ ವರ್ಕ್‌ಫ್ಲೋಗೆ `contents: write` ಮತ್ತು `pull-requests: write` ಅನುಮತಿಗಳನ್ನು ನೀಡುತ್ತದೆ.
4.  **Allow GitHub Actions to create and approve pull requests** ಎಂಬ ಚೌಕವನ್ನು **ಚೆಕ್ ಮಾಡಿ**.
5.  **Save** ಆಯ್ಕೆಮಾಡಿ.

![ಅನುಮತಿ ಸೆಟ್ಟಿಂಗ್](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### ಹಂತ 4: ವರ್ಕ್‌ಫ್ಲೋ ಫೈಲ್ ರಚಿಸಿ

ಕೊನೆಗೆ, `GITHUB_TOKEN` ಬಳಸಿ ಸ್ವಯಂಚಾಲಿತ ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ವ್ಯಾಖ್ಯಾನಿಸುವ YAML ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ.

1.  ನಿಮ್ಮ ರೆಪೊಸಿಟರಿಯ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ `.github/workflows/` ಡೈರೆಕ್ಟರಿಯನ್ನು ರಚಿಸಿ (ಇದು ಇಲ್ಲದಿದ್ದರೆ).
2.  `.github/workflows/` ಒಳಗೆ, `co-op-translator.yml` ಎಂಬ ಫೈಲ್ ಅನ್ನು ರಚಿಸಿ.
3.  ಈ ವಿಷಯವನ್ನು `co-op-translator.yml` ಗೆ ಪೇಸ್ಟ್ ಮಾಡಿ.

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
4.  **ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ಕಸ್ಟಮೈಸ್ ಮಾಡಿ:**
  - **[!IMPORTANT] ಗುರಿ ಭಾಷೆಗಳು:** `Run Co-op Translator` ಹಂತದಲ್ಲಿ, ನೀವು **ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಅಗತ್ಯಗಳಿಗೆ ಹೊಂದಾಣಿಕೆ ಮಾಡಲು** `translate -l "..." -y` ಆಜ್ಞೆಯಲ್ಲಿನ ಭಾಷಾ ಕೋಡ್‌ಗಳ ಪಟ್ಟಿ ಪರಿಶೀಲಿಸಿ ಮತ್ತು ಬದಲಾಯಿಸಬೇಕು. ಉದಾಹರಣೆಯ ಪಟ್ಟಿ (`ar de es...`) ಅನ್ನು ಬದಲಾಯಿಸಬೇಕು ಅಥವಾ ಹೊಂದಿಸಬೇಕು.
  - **ಟ್ರಿಗರ್ (`on:`):** ಪ್ರಸ್ತುತ ಟ್ರಿಗರ್ `main` ಗೆ ಪ್ರತಿ ಪುಶ್‌ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ. ದೊಡ್ಡ ರೆಪೊಸಿಟರಿಗಳಿಗಾಗಿ, ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ಸಂಬಂಧಿತ ಫೈಲ್‌ಗಳು (ಉದಾ., ಮೂಲ ಡಾಕ್ಯುಮೆಂಟೇಶನ್) ಬದಲಾದಾಗ ಮಾತ್ರ ಕಾರ್ಯನಿರ್ವಹಿಸಲು `paths:` ಫಿಲ್ಟರ್ ಅನ್ನು ಸೇರಿಸುವುದನ್ನು ಪರಿಗಣಿಸಿ, ರನ್ನರ್ ನಿಮಿಷಗಳನ್ನು ಉಳಿಸಲು.
  - **PR ವಿವರಗಳು:** `Create Pull Request` ಹಂತದಲ್ಲಿ `commit-message`, `title`, `body`, `branch` ಹೆಸರು, ಮತ್ತು `labels` ಅನ್ನು ಅಗತ್ಯವಿದ್ದರೆ ಕಸ್ಟಮೈಸ್ ಮಾಡಿ.

## ವರ್ಕ್‌ಫ್ಲೋವನ್ನು ಚಲಾಯಿಸುವುದು

> [!WARNING]  
> **GitHub-ಹೋಸ್ಟ್ ಮಾಡಿದ ರನ್ನರ್ ಸಮಯ ಮಿತಿಯು:**  
> `ubuntu-latest` ಮುಂತಾದ GitHub-ಹೋಸ್ಟ್ ಮಾಡಿದ ರನ್ನರ್‌ಗಳಿಗೆ **ಗರಿಷ್ಠ ಕಾರ್ಯನಿರ್ವಹಣಾ ಸಮಯ ಮಿತಿ 6 ಗಂಟೆ** ಇದೆ.  
> ದೊಡ್ಡ ಡಾಕ್ಯುಮೆಂಟೇಶನ್ ರೆಪೊಸಿಟರಿಗಳಿಗಾಗಿ, ಅನುವಾದ ಪ್ರಕ್ರಿಯೆ 6 ಗಂಟೆ ಮಿತಿಯನ್ನು ಮೀರಿದರೆ, ವರ್ಕ್‌ಫ್ಲೋ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ರದ್ದುಗೊಳ್ಳುತ್ತದೆ.  
> ಇದನ್ನು ತಡೆಯಲು, ಪರಿಗಣಿಸಿ:  
> - **ಸ್ವಯಂ-ಹೋಸ್ಟ್ ಮಾಡಿದ ರನ್ನರ್** ಬಳಸಿ (ಸಮಯ ಮಿತಿ ಇಲ್ಲ)  
> - ಪ್ರತಿ ರನ್‌ಗೆ ಗುರಿ ಭಾಷೆಗಳ ಸಂಖ್ಯೆಯನ್ನು ಕಡಿಮೆ ಮಾಡುವುದು

`co-op-translator.yml` ಫೈಲ್ ನಿಮ್ಮ ಮುಖ್ಯ ಶಾಖೆಗೆ (ಅಥವಾ `on:` ಟ್ರಿಗರ್‌ನಲ್ಲಿ ನಿರ್ದಿಷ್ಟಗೊಳಿಸಿದ ಶಾಖೆಗೆ) ವಿಲೀನಗೊಂಡ ನಂತರ, ಈ ವರ್ಕ್‌ಫ್ಲೋ ಶಾಖೆಗೆ ಪುಶ್ ಮಾಡಿದಾಗ (ಮತ್ತು `paths` ಫಿಲ್ಟರ್ ಹೊಂದಾಣಿಕೆ ಮಾಡಿದರೆ) ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸಮಾಕ್ಷಿಕೆ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ದಯವಿಟ್ಟು ಗಮನಿಸಿ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸಮಾಕ್ಷಿತೆಗಳು ಇರಬಹುದು. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜು ಪ್ರಾಮಾಣಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸುವ ಮೂಲಕ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗಳ ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳ ಬಗ್ಗೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->