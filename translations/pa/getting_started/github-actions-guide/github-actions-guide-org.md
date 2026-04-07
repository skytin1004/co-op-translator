# ਕੋ-ਓਪ ਟ੍ਰਾਂਸਲੇਟਰ GitHub ਐਕਸ਼ਨ ਦੀ ਵਰਤੋਂ (ਸੰਗਠਨ ਲਈ ਗਾਈਡ)

**ਲਕੜੀ ਦਰਸ਼ਕ:** ਇਹ ਗਾਈਡ **Microsoft ਦੇ ਅੰਦਰੂਨੀ ਯੂਜ਼ਰਾਂ** ਜਾਂ **ਟੀਮਾਂ** ਲਈ ਹੈ, ਜਿਨ੍ਹਾਂ ਕੋਲ ਪਹਿਲਾਂ ਤੋਂ ਬਣੀ ਹੋਈ Co-op Translator GitHub App ਲਈ ਲਾਜ਼ਮੀ credentials ਹਨ ਜਾਂ ਆਪਣੀ custom GitHub App ਬਣਾਉਣ ਦੀ ਸਮਰੱਥਾ ਹੈ।

ਆਪਣੇ ਰਿਪੋਜ਼ਿਟਰੀ ਦੀ ਡੌਕੂਮੈਂਟੇਸ਼ਨ ਨੂੰ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਅਨੁਵਾਦ ਕਰਨ ਲਈ Co-op Translator GitHub Action ਦੀ ਵਰਤੋਂ ਕਰੋ। ਇਹ ਗਾਈਡ ਤੁਹਾਨੂੰ ਇਹ ਐਕਸ਼ਨ ਸੈੱਟਅੱਪ ਕਰਨ ਦੀ ਪ੍ਰਕਿਰਿਆ ਦੱਸਦੀ ਹੈ, ਤਾਂ ਜੋ ਜਦੋਂ ਵੀ ਤੁਹਾਡੇ ਸਰੋਤ Markdown ਫਾਈਲਾਂ ਜਾਂ ਚਿੱਤਰਾਂ ਵਿੱਚ ਕੋਈ ਤਬਦੀਲੀ ਆਵੇ, workflow ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਅਪਡੇਟ ਕੀਤੇ ਅਨੁਵਾਦਾਂ ਵਾਲੀ pull request ਬਣਾਏ।

> [!IMPORTANT]
> 
> **ਸਹੀ ਗਾਈਡ ਚੁਣੋ:**
>
> ਇਹ ਗਾਈਡ **GitHub App ID ਅਤੇ Private Key** ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੈੱਟਅੱਪ ਕਰਨ ਦੀ ਵਿਸਥਾਰ ਦਿੰਦੀ ਹੈ। ਤੁਹਾਨੂੰ ਆਮ ਤੌਰ 'ਤੇ ਇਹ "ਸੰਗਠਨ ਗਾਈਡ" ਤਦੋਂ ਲੋੜੀਂਦੀ ਹੁੰਦੀ ਹੈ ਜਦੋਂ: **`GITHUB_TOKEN` ਦੀਆਂ Permissions ਸੀਮਤ ਹਨ:** ਤੁਹਾਡੇ ਸੰਗਠਨ ਜਾਂ ਰਿਪੋਜ਼ਿਟਰੀ ਦੀਆਂ settings, standard `GITHUB_TOKEN` ਨੂੰ ਮਿਲਣ ਵਾਲੀਆਂ permissions ਨੂੰ ਸੀਮਤ ਕਰਦੀਆਂ ਹਨ। ਖਾਸ ਕਰਕੇ, ਜੇ `GITHUB_TOKEN` ਨੂੰ ਲਾਜ਼ਮੀ `write` permissions (ਜਿਵੇਂ `contents: write` ਜਾਂ `pull-requests: write`) ਨਹੀਂ ਮਿਲਦੀਆਂ, ਤਾਂ [Public Setup Guide](./github-actions-guide-public.md) ਵਿੱਚ ਦਿੱਤਾ workflow permissions ਦੀ ਘਾਟ ਕਾਰਨ ਫੇਲ ਹੋ ਜਾਵੇਗਾ। Dedicated GitHub App ਦੀ ਵਰਤੋਂ, ਜਿਸਨੂੰ permissions explicit ਤੌਰ 'ਤੇ ਦਿੱਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ, ਇਸ ਸੀਮਤ ਨੂੰ ਦੂਰ ਕਰਦੀ ਹੈ।
>
> **ਜੇ ਉਪਰੋਕਤ ਤੁਹਾਡੇ ਲਈ ਲਾਗੂ ਨਹੀਂ ਹੁੰਦਾ:**
>
> ਜੇ standard `GITHUB_TOKEN` ਨੂੰ ਤੁਹਾਡੇ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ ਪੂਰੀ permissions ਮਿਲੀਆਂ ਹੋਈਆਂ ਹਨ (ਅਰਥਾਤ, ਤੁਸੀਂ ਸੰਗਠਨ ਦੀਆਂ ਸੀਮਤਾਂ ਕਾਰਨ ਰੋਕੇ ਨਹੀਂ ਹੋ), ਤਾਂ **[Public Setup Guide using GITHUB_TOKEN](./github-actions-guide-public.md)** ਦੀ ਵਰਤੋਂ ਕਰੋ। Public guide ਵਿੱਚ App IDs ਜਾਂ Private Keys ਲੈਣ ਜਾਂ ਸੰਭਾਲਣ ਦੀ ਲੋੜ ਨਹੀਂ ਹੁੰਦੀ, ਸਿਰਫ standard `GITHUB_TOKEN` ਅਤੇ ਰਿਪੋਜ਼ਿਟਰੀ permissions 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ।

## ਪੂਰਵ-ਸ਼ਰਤਾਂ

GitHub Action ਨੂੰ configure ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਲਾਜ਼ਮੀ AI service credentials ਤਿਆਰ ਹਨ।

**1. ਲਾਜ਼ਮੀ: AI Language Model Credentials**
ਤੁਹਾਨੂੰ ਘੱਟੋ-ਘੱਟ ਇੱਕ supported Language Model ਲਈ credentials ਚਾਹੀਦੇ ਹਨ:

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Names, API Version ਦੀ ਲੋੜ।
- **OpenAI**: API Key, (Optional: Org ID, Base URL, Model ID) ਦੀ ਲੋੜ।
- ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ [Supported Models and Services](../../../../README.md) ਵੇਖੋ।
- Setup Guide: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)।

**2. ਵਿਕਲਪਿਕ: Computer Vision Credentials (ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ)**

- ਜੇ ਤੁਸੀਂ ਚਿੱਤਰਾਂ ਵਿੱਚ ਲਿਖੀ ਟੈਕਸਟ ਦਾ ਅਨੁਵਾਦ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਹੀ ਲੋੜੀਂਦੇ ਹਨ।
- **Azure Computer Vision**: Endpoint ਅਤੇ Subscription Key ਦੀ ਲੋੜ।
- ਜੇ ਨਾ ਦਿੱਤੇ ਜਾਣ, ਤਾਂ action [Markdown-only mode](../markdown-only-mode.md) 'ਤੇ ਚੱਲੇਗਾ।
- Setup Guide: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)।

## ਸੈੱਟਅੱਪ ਅਤੇ configuration

ਹੇਠਾਂ ਦਿੱਤੇ ਕਦਮਾਂ ਦੀ ਪਾਲਣਾ ਕਰਕੇ ਆਪਣੇ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ Co-op Translator GitHub Action configure ਕਰੋ:

### ਕਦਮ 1: GitHub App Authentication install ਅਤੇ configure ਕਰੋ

Workflow ਤੁਹਾਡੇ ਰਿਪੋਜ਼ਿਟਰੀ ਨਾਲ securely interact ਕਰਨ ਲਈ GitHub App authentication ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ (ਜਿਵੇਂ pull requests ਬਣਾਉਣਾ)। ਹੇਠਾਂ ਦਿੱਤੇ options ਵਿੱਚੋਂ ਇੱਕ ਚੁਣੋ:

#### **Option A: Pre-built Co-op Translator GitHub App install ਕਰੋ (Microsoft ਅੰਦਰੂਨੀ ਵਰਤੋਂਕਾਰਾਂ ਲਈ)**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) ਪੇਜ 'ਤੇ ਜਾਓ।

1. **Install** ਚੁਣੋ ਅਤੇ ਉਹ account ਜਾਂ organization ਚੁਣੋ ਜਿੱਥੇ ਤੁਹਾਡਾ target repository ਹੈ।

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.pa.png)

1. **Only select repositories** ਚੁਣੋ ਅਤੇ ਆਪਣਾ target repository (ਜਿਵੇਂ `PhiCookBook`) ਚੁਣੋ। **Install** 'ਤੇ ਕਲਿੱਕ ਕਰੋ। ਤੁਹਾਨੂੰ authenticate ਕਰਨ ਲਈ ਕਿਹਾ ਜਾ ਸਕਦਾ ਹੈ।

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.pa.png)

1. **App Credentials ਲਵੋ (ਅੰਦਰੂਨੀ ਪ੍ਰਕਿਰਿਆ ਲਾਜ਼ਮੀ):** Workflow ਨੂੰ app ਵਜੋਂ authenticate ਕਰਨ ਲਈ ਤੁਹਾਨੂੰ Co-op Translator ਟੀਮ ਵਲੋਂ ਦੋ ਚੀਜ਼ਾਂ ਲੈਣੀਆਂ ਪੈਣਗੀਆਂ:
  - **App ID:** Co-op Translator app ਲਈ unique identifier। App ID ਹੈ: `1164076`।
  - **Private Key:** `.pem` private key ਫਾਈਲ ਦੀ **ਪੂਰੀ ਸਮੱਗਰੀ** maintainer contact ਤੋਂ ਲਵੋ। **ਇਸ key ਨੂੰ password ਵਾਂਗ ਸੰਭਾਲੋ ਅਤੇ ਸੁਰੱਖਿਅਤ ਰੱਖੋ।**

1. Step 2 'ਤੇ ਜਾਓ।

#### **Option B: ਆਪਣੀ custom GitHub App ਵਰਤੋਂ ਕਰੋ**

- ਜੇ ਤੁਸੀਂ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਆਪਣੀ GitHub App ਬਣਾਓ ਅਤੇ configure ਕਰੋ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਇਸਨੂੰ Contents ਅਤੇ Pull requests ਲਈ Read & write access ਮਿਲੀ ਹੋਵੇ। ਤੁਹਾਨੂੰ ਇਸਦੀ App ID ਅਤੇ generated Private Key ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

### ਕਦਮ 2: Repository Secrets configure ਕਰੋ

GitHub App credentials ਅਤੇ ਆਪਣੇ AI service credentials ਨੂੰ encrypted secrets ਵਜੋਂ ਆਪਣੇ repository settings ਵਿੱਚ add ਕਰੋ।

1. ਆਪਣੇ target GitHub repository (ਜਿਵੇਂ `PhiCookBook`) 'ਤੇ ਜਾਓ।

1. **Settings** > **Secrets and variables** > **Actions** 'ਤੇ ਜਾਓ।

1. **Repository secrets** ਹੇਠਾਂ, ਹਰੇਕ secret ਲਈ **New repository secret** 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.pa.png)

**ਲਾਜ਼ਮੀ Secrets (GitHub App Authentication ਲਈ):**

| Secret Name          | Description                                      | Value Source                                     |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | GitHub App ਦੀ App ID (Step 1 ਤੋਂ)                | GitHub App Settings                              |
| `GH_APP_PRIVATE_KEY` | Download ਕੀਤੀ `.pem` ਫਾਈਲ ਦੀ **ਪੂਰੀ ਸਮੱਗਰੀ**   | `.pem` file (Step 1 ਤੋਂ)                         |

**AI Service Secrets (ਆਪਣੀ ਪੂਰਵ-ਸ਼ਰਤਾਂ ਅਨੁਸਾਰ ਸਾਰੇ ਲਾਗੂ ਕਰਕੇ ਜੋੜੋ):**

| Secret Name                         | Description                               | Value Source                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) ਲਈ key | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) ਲਈ endpoint | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI service ਲਈ key              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI service ਲਈ endpoint         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | ਤੁਹਾਡਾ Azure OpenAI Model Name           | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | ਤੁਹਾਡਾ Azure OpenAI Deployment Name      | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI ਲਈ API Version              | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | OpenAI ਲਈ API Key                        | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | ਖਾਸ OpenAI model ID                       | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | Custom OpenAI API Base URL                | OpenAI Platform                    |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.pa.png)

### ਕਦਮ 3: Workflow ਫਾਈਲ ਬਣਾਓ

ਆਖ਼ਰਕਾਰ, YAML ਫਾਈਲ ਬਣਾਓ ਜੋ automated workflow define ਕਰਦੀ ਹੈ।

1. ਆਪਣੇ repository ਦੀ root directory ਵਿੱਚ `.github/workflows/` ਡਾਇਰੈਕਟਰੀ ਬਣਾਓ, ਜੇ ਪਹਿਲਾਂ ਨਹੀਂ ਹੈ।

1. `.github/workflows/` ਵਿੱਚ `co-op-translator.yml` ਨਾਂ ਦੀ ਫਾਈਲ ਬਣਾਓ।

1. ਹੇਠਾਂ ਦਿੱਤਾ ਸਮੱਗਰੀ co-op-translator.yml ਵਿੱਚ ਪੇਸਟ ਕਰੋ।

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

4.  **Workflow ਨੂੰ customize ਕਰੋ:**
  - **[!IMPORTANT] Target Languages:** `Run Co-op Translator` step ਵਿੱਚ, ਤੁਸੀਂ **ਭਾਸ਼ਾ ਕੋਡਾਂ ਦੀ ਲਿਸਟ** `translate -l "..." -y` ਕਮਾਂਡ ਵਿੱਚ review ਅਤੇ modify ਕਰਨੀ ਲਾਜ਼ਮੀ ਹੈ, ਤਾਂ ਜੋ ਤੁਹਾਡੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਲੋੜ ਮੁਤਾਬਕ ਹੋਵੇ। Example ਲਿਸਟ (`ar de es...`) ਨੂੰ ਬਦਲੋ ਜਾਂ edit ਕਰੋ।
  - **Trigger (`on:`):** ਮੌਜੂਦਾ trigger ਹਰ push 'ਤੇ `main` 'ਤੇ ਚਲਦਾ ਹੈ। ਵੱਡੇ repositories ਲਈ, `paths:` filter (YAML ਵਿੱਚ comment ਕੀਤੇ example ਵੇਖੋ) add ਕਰਨ 'ਤੇ ਵਿਚਾਰ ਕਰੋ, ਤਾਂ workflow ਸਿਰਫ਼ ਜਦੋਂ ਲਾਜ਼ਮੀ ਫਾਈਲਾਂ (ਜਿਵੇਂ source documentation) ਵਿੱਚ ਤਬਦੀਲੀ ਆਵੇ, ਤਦੋਂ ਹੀ ਚੱਲੇ, runner minutes ਬਚਾਉਣ ਲਈ।
  - **PR Details:** ਜੇ ਲੋੜ ਹੋਵੇ, ਤਾਂ `commit-message`, `title`, `body`, `branch` name, ਅਤੇ `labels` ਨੂੰ `Create Pull Request` step ਵਿੱਚ customize ਕਰੋ।

## Credential Management ਅਤੇ Renewal

- **Security:** Sensitive credentials (API keys, private keys) ਨੂੰ ਹਮੇਸ਼ਾ GitHub Actions secrets ਵਜੋਂ store ਕਰੋ। Workflow ਫਾਈਲ ਜਾਂ repository code ਵਿੱਚ ਕਦੇ ਵੀ expose ਨਾ ਕਰੋ।
- **[!IMPORTANT] Key Renewal (Microsoft ਅੰਦਰੂਨੀ ਵਰਤੋਂਕਾਰ):** ਧਿਆਨ ਰੱਖੋ ਕਿ Azure OpenAI key, ਜੋ Microsoft ਵਿੱਚ ਵਰਤੀ ਜਾਂਦੀ ਹੈ, ਉਸਦੀ renewal policy ਹੋ ਸਕਦੀ ਹੈ (ਜਿਵੇਂ, ਹਰ 5 ਮਹੀਨੇ)। Workflow failures ਤੋਂ ਬਚਣ ਲਈ, GitHub secrets (`AZURE_OPENAI_...` keys) **expire ਹੋਣ ਤੋਂ ਪਹਿਲਾਂ** update ਕਰ ਲਵੋ।

## Workflow ਚਲਾਉਣਾ

> [!WARNING]  
> **GitHub-hosted Runner Time Limit:**  
> GitHub-hosted runners ਜਿਵੇਂ `ubuntu-latest` ਦੀ **ਵੱਧ ਤੋਂ ਵੱਧ execution time limit 6 ਘੰਟੇ** ਹੈ।  
> ਜੇ ਵੱਡੇ documentation repositories ਵਿੱਚ translation process 6 ਘੰਟਿਆਂ ਤੋਂ ਵੱਧ ਲੈਂਦੀ ਹੈ, ਤਾਂ workflow ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ terminate ਹੋ ਜਾਵੇਗਾ।  
> ਇਸ ਤੋਂ ਬਚਣ ਲਈ, ਵਿਚਾਰ ਕਰੋ:  
> - **Self-hosted runner** ਵਰਤੋਂ (ਕੋਈ time limit ਨਹੀਂ)  
> - ਹਰ run ਵਿੱਚ target languages ਦੀ ਗਿਣਤੀ ਘੱਟ ਕਰੋ

ਜਦੋਂ `co-op-translator.yml` ਫਾਈਲ ਤੁਹਾਡੇ main branch (ਜਾਂ `on:` trigger ਵਿੱਚ ਦਿੱਤੇ branch) ਵਿੱਚ merge ਹੋ ਜਾਂਦੀ ਹੈ, workflow ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਚੱਲੇਗਾ ਜਦੋਂ ਵੀ ਉਸ branch 'ਤੇ ਤਬਦੀਲੀਆਂ push ਕੀਤੀਆਂ ਜਾਂਦੀਆਂ ਹਨ (ਅਤੇ `paths` filter match ਕਰਦਾ ਹੋਵੇ, ਜੇ configure ਕੀਤਾ ਹੋਵੇ)।

ਜੇ ਅਨੁਵਾਦ ਬਣਦੇ ਜਾਂ update ਹੁੰਦੇ ਹਨ, ਤਾਂ action ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ Pull Request ਬਣਾਏਗਾ, ਜਿਸ ਵਿੱਚ ਤਬਦੀਲੀਆਂ ਹੋਣਗੀਆਂ, ਜੋ ਤੁਹਾਡੇ review ਅਤੇ merge ਲਈ ਤਿਆਰ ਹੋਵੇਗੀ।

---

**ਅਸਵੀਕਰਨ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਯਥਾਸੰਭਵ ਸਹੀ ਅਨੁਵਾਦ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਪਛਾਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼, ਜਿਸ ਭਾਸ਼ਾ ਵਿੱਚ ਉਹ ਲਿਖਿਆ ਗਿਆ ਹੈ, ਨੂੰ ਹੀ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜੇਕਰ ਜਾਣਕਾਰੀ ਮਹੱਤਵਪੂਰਨ ਹੈ, ਤਾਂ ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।