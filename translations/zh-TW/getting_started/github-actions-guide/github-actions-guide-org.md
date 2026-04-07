# 使用 Co-op Translator GitHub Action（組織指南）

**目標讀者：** 本指南適用於 **Microsoft 內部用戶** 或 **擁有預建 Co-op Translator GitHub App 所需憑證的團隊**，或能自行建立自訂 GitHub App 的團隊。

利用 Co-op Translator GitHub Action，輕鬆自動化你的儲存庫文件翻譯。這份指南將帶你一步步設定，讓當你的 Markdown 檔案或圖片有變更時，自動建立包含最新翻譯的 Pull Request。

> [!IMPORTANT]
>
> **選擇正確的指南：**
>
> 本指南說明如何使用 **GitHub App ID 和 Private Key** 進行設定。當你遇到以下情況時，通常需要採用本「組織指南」方法：**`GITHUB_TOKEN` 權限受限：** 如果你的組織或儲存庫設定限制了標準 `GITHUB_TOKEN` 的預設權限，特別是當 `GITHUB_TOKEN` 無法取得必要的 `write` 權限（如 `contents: write` 或 `pull-requests: write`），那麼依照 [公開設定指南](./github-actions-guide-public.md) 的流程將因權限不足而失敗。使用專屬 GitHub App 並明確授權權限，可以避開這個限制。
>
> **如果上述情況不適用於你：**
>
> 如果你的儲存庫中的標準 `GITHUB_TOKEN` 權限足夠（即沒有被組織限制），請直接使用 **[公開設定指南（使用 GITHUB_TOKEN）](./github-actions-guide-public.md)**。公開指南不需要取得或管理 App ID 或 Private Key，只需標準的 `GITHUB_TOKEN` 及儲存庫權限即可。

## 先決條件

在設定 GitHub Action 前，請先準備好所需的 AI 服務憑證。

**1. 必要：AI 語言模型憑證**
你需要至少一組支援的語言模型憑證：

- **Azure OpenAI**：需 Endpoint、API Key、Model/Deployment Name、API Version。
- **OpenAI**：需 API Key，（可選：Org ID、Base URL、Model ID）。
- 詳細請參考 [支援的模型與服務](../../../../README.md)。
- 設定指南：[設定 Azure OpenAI](../set-up-resources/set-up-azure-openai.md)。

**2. 選用：電腦視覺憑證（用於圖片翻譯）**

- 僅當你需要翻譯圖片中的文字時才需要。
- **Azure Computer Vision**：需 Endpoint 和 Subscription Key。
- 若未提供，Action 將預設為 [僅 Markdown 模式](../markdown-only-mode.md)。
- 設定指南：[設定 Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)。

## 設定與配置

請依照下列步驟，在你的儲存庫中設定 Co-op Translator GitHub Action：

### 步驟 1：安裝並設定 GitHub App 認證

此工作流程會使用 GitHub App 認證，安全地以你的名義與儲存庫互動（如建立 Pull Request）。請選擇一種方式：

#### **選項 A：安裝預建的 Co-op Translator GitHub App（僅限 Microsoft 內部使用）**

1. 前往 [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) 頁面。

1. 選擇 **Install**，並選擇你的帳號或組織所在的目標儲存庫。

    ![安裝 app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.tw.png)

1. 選擇 **Only select repositories**，並勾選你的目標儲存庫（如 `PhiCookBook`）。點擊 **Install**。系統可能會要求你驗證身份。

    ![安裝授權](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.tw.png)

1. **取得 App 憑證（需內部流程）：** 為了讓工作流程能以 App 身份認證，你需要向 Co-op Translator 團隊取得以下兩項資訊：
  - **App ID：** Co-op Translator app 的唯一識別碼。App ID 為：`1164076`。
  - **Private Key：** 你必須向維護者聯絡人取得 **完整的 `.pem` 私鑰檔案內容**。**請將此金鑰視同密碼，妥善保管。**

1. 請繼續進行步驟 2。

#### **選項 B：使用你自訂的 GitHub App**

- 如果你希望自行建立並設定 GitHub App，請確保它擁有 Contents 和 Pull requests 的讀寫權限。你將需要 App ID 及產生的 Private Key。

### 步驟 2：設定儲存庫 Secrets

你需要將 GitHub App 憑證及 AI 服務憑證，作為加密 secrets 加入儲存庫設定。

1. 前往你的目標 GitHub 儲存庫（如 `PhiCookBook`）。

1. 點選 **Settings** > **Secrets and variables** > **Actions**。

1. 在 **Repository secrets** 下，針對下方每一個 secret 點選 **New repository secret**。

   ![選擇設定 action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.tw.png)

**必要 Secrets（GitHub App 認證用）：**

| Secret Name          | 說明                                      | 來源                                     |
| :------------------- | :---------------------------------------- | :--------------------------------------- |
| `GH_APP_ID`          | GitHub App 的 App ID（來自步驟 1）         | GitHub App 設定                          |
| `GH_APP_PRIVATE_KEY` | 下載的 `.pem` 檔案 **完整內容**            | `.pem` 檔案（來自步驟 1）                |

**AI 服務 Secrets（根據你的先決條件，全部加入）：**

| Secret Name                         | 說明                               | 來源                     |
| :---------------------------------- | :-------------------------------- | :----------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service（Computer Vision）金鑰  | Azure AI Foundry         |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service（Computer Vision）端點 | Azure AI Foundry         |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 服務金鑰              | Azure AI Foundry         |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 服務端點              | Azure AI Foundry         |
| `AZURE_OPENAI_MODEL_NAME`           | 你的 Azure OpenAI 模型名稱         | Azure AI Foundry         |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | 你的 Azure OpenAI 部署名稱         | Azure AI Foundry         |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 版本              | Azure AI Foundry         |
| `OPENAI_API_KEY`                    | OpenAI API 金鑰                    | OpenAI Platform          |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID                     | OpenAI Platform          |
| `OPENAI_CHAT_MODEL_ID`              | 指定的 OpenAI 模型 ID              | OpenAI Platform          |
| `OPENAI_BASE_URL`                   | 自訂 OpenAI API Base URL           | OpenAI Platform          |

![輸入環境變數名稱](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.tw.png)

### 步驟 3：建立 Workflow 檔案

最後，建立自動化工作流程的 YAML 檔案。

1. 在你的儲存庫根目錄下，若尚未存在，請建立 `.github/workflows/` 目錄。

1. 在 `.github/workflows/` 內建立名為 `co-op-translator.yml` 的檔案。

1. 將下方內容貼入 co-op-translator.yml。

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

4.  **自訂工作流程：**
  - **[!IMPORTANT] 目標語言：** 在 `Run Co-op Translator` 步驟中，你**必須檢查並修改 `translate -l "..." -y` 指令中的語言代碼清單**，以符合你的專案需求。範例中的清單（`ar de es...`）請依實際需求調整。
  - **觸發條件（`on:`）：** 目前設定為每次 push 到 `main` 都會觸發。若你的儲存庫很大，建議加上 `paths:` 過濾條件（可參考 YAML 中的註解範例），僅在相關檔案（如原始文件）變更時才執行，節省 runner 時間。
  - **PR 詳細資訊：** 如有需要，可自訂 `commit-message`、`title`、`body`、`branch` 名稱及 `labels`。

## 憑證管理與更新

- **安全性：** 請務必將敏感憑證（API 金鑰、私鑰）存放於 GitHub Actions secrets，切勿在 workflow 檔案或儲存庫程式碼中暴露。
- **[!IMPORTANT] 金鑰更新（Microsoft 內部用戶）：** 請注意，Microsoft 內部使用的 Azure OpenAI 金鑰可能有強制定期更新政策（如每 5 個月）。請務必在金鑰到期前，更新對應的 GitHub secrets（`AZURE_OPENAI_...` 金鑰），以避免工作流程失敗。

## 執行工作流程

> [!WARNING]  
> **GitHub-hosted Runner 執行時間限制：**  
> GitHub-hosted runner（如 `ubuntu-latest`）**最長執行時間為 6 小時**。  
> 若你的文件儲存庫很大，翻譯過程超過 6 小時，工作流程將自動終止。  
> 為避免此情況，建議：  
> - 使用 **自架 runner**（無時間限制）  
> - 每次執行時減少目標語言數量

當 `co-op-translator.yml` 檔案合併到你的主分支（或 `on:` 觸發條件指定的分支）後，每當有變更 push 到該分支（且符合 `paths` 過濾條件時，如有設定），工作流程就會自動執行。

若有產生或更新翻譯，Action 會自動建立包含變更內容的 Pull Request，等你審查與合併。

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。