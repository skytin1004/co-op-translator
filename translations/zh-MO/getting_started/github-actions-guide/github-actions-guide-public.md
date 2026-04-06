# 使用 Co-op Translator GitHub Action（公開設定）

**適用對象：** 本指南適用於大多數公開或私人倉庫，只要標準 GitHub Actions 權限足夠即可。它使用內建的 `GITHUB_TOKEN`。

利用 Co-op Translator GitHub Action，輕鬆自動化你的倉庫文件翻譯。這份指南會一步步教你如何設定這個 Action，讓它在你的 Markdown 原始檔或圖片有變動時，自動建立包含最新翻譯的 Pull Request。

> [!IMPORTANT]
>
> **選擇合適的指南：**
>
> 本指南介紹的是**使用標準 `GITHUB_TOKEN` 的簡易設定**。這是大多數使用者推薦的方式，因為不需要管理敏感的 GitHub App 私密金鑰。
>

## 事前準備

在設定 GitHub Action 之前，請先準備好所需的 AI 服務憑證。

**1. 必備：AI 語言模型憑證**
你需要至少一種支援的語言模型憑證：

- **Azure OpenAI**：需要 Endpoint、API Key、模型/部署名稱、API 版本。
- **OpenAI**：需要 API Key，（選填：Org ID、Base URL、Model ID）。
- 詳細請參考 [支援的模型與服務](../../../../README.md)。

**2. 選填：AI Vision 憑證（用於圖片翻譯）**

- 只有需要翻譯圖片中的文字時才需要。
- **Azure AI Vision**：需要 Endpoint 和 Subscription Key。
- 如果沒提供，Action 會自動切換到 [僅 Markdown 模式](../markdown-only-mode.md)。

## 設定與配置

請依照以下步驟，使用標準 `GITHUB_TOKEN` 在你的倉庫設定 Co-op Translator GitHub Action。

### 步驟 1：了解認證方式（使用 `GITHUB_TOKEN`）

這個流程會用到 GitHub Actions 內建的 `GITHUB_TOKEN`。這個 Token 會根據你在**步驟 3**設定的權限，自動授權流程操作你的倉庫。

### 步驟 2：設定倉庫密碼

你只需要將**AI 服務憑證**加到倉庫設定的加密密碼中。

1. 進入你的目標 GitHub 倉庫。
2. 點選 **Settings** > **Secrets and variables** > **Actions**。
3. 在 **Repository secrets** 下，針對每個需要的 AI 服務密碼，點選 **New repository secret**。

    <img src="../../../../translated_images/zh-MO/select-setting-action.3b95c915d6031159.webp" alt="選擇設定動作"> *(圖片說明：顯示如何新增密碼)*

**必備 AI 服務密碼（根據你的事前準備，全部都要加）：**

| 密碼名稱                         | 說明                                   | 來源                           |
| :------------------------------ | :------------------------------------- | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service（Computer Vision）金鑰  | 你的 Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service（Computer Vision）端點 | 你的 Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 服務金鑰                  | 你的 Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 服務端點                  | 你的 Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI 模型名稱                  | 你的 Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI 部署名稱                  | 你的 Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 版本                  | 你的 Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI API 金鑰                        | 你的 OpenAI 平台                    |
| `OPENAI_ORG_ID`                     | OpenAI 組織 ID（選填）                 | 你的 OpenAI 平台                    |
| `OPENAI_CHAT_MODEL_ID`              | 指定 OpenAI 模型 ID（選填）            | 你的 OpenAI 平台                    |
| `OPENAI_BASE_URL`                   | 自訂 OpenAI API Base URL（選填）       | 你的 OpenAI 平台                    |

### 步驟 3：設定流程權限

GitHub Action 需要透過 `GITHUB_TOKEN` 取得 checkout 及建立 Pull Request 的權限。

1. 在你的倉庫，點選 **Settings** > **Actions** > **General**。
2. 往下捲到 **Workflow permissions** 區塊。
3. 選擇 **Read and write permissions**。這會讓 `GITHUB_TOKEN` 取得 `contents: write` 和 `pull-requests: write` 權限。
4. 確認 **Allow GitHub Actions to create and approve pull requests** 的勾選框有**打勾**。
5. 點選 **Save**。

<img src="../../../../translated_images/zh-MO/permission-setting.ae2f02748b0579e7.webp" alt="權限設定">

### 步驟 4：建立流程檔案

最後，建立 YAML 檔案，定義使用 `GITHUB_TOKEN` 的自動化流程。

1. 在你的倉庫根目錄下，建立 `.github/workflows/` 資料夾（如果還沒建立）。
2. 在 `.github/workflows/` 裡面，建立一個名為 `co-op-translator.yml` 的檔案。
3. 把以下內容貼到 `co-op-translator.yml`。

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
4.  **自訂流程：**
  - **[!IMPORTANT] 目標語言：** 在 `Run Co-op Translator` 步驟中，你**必須檢查並修改 `translate -l "..." -y` 指令裡的語言代碼清單**，以符合你的專案需求。範例清單（`ar de es...`）需要替換或調整。
  - **觸發條件（`on:`）：** 目前設定是每次 push 到 `main` 都會觸發。若你的倉庫很大，建議加上 `paths:` 過濾（YAML 裡有註解範例），只在相關檔案（例如原始文件）變動時才執行，節省 runner 時間。
  - **PR 詳細設定：** 如有需要，可自訂 `commit-message`、`title`、`body`、`branch` 名稱及 `labels`。

## 執行流程

> [!WARNING]  
> **GitHub 託管 Runner 時間限制：**  
> GitHub 託管的 runner（如 `ubuntu-latest`）**最多執行 6 小時**。  
> 如果你的文件倉庫很大，翻譯流程超過 6 小時，流程會自動被終止。  
> 避免這種情況的方法：  
> - 使用**自架 runner**（沒時間限制）  
> - 每次執行時減少目標語言數量

當 `co-op-translator.yml` 檔案合併到你的主分支（或 `on:` 觸發條件指定的分支）後，只要有變更 push 到該分支（且符合 `paths` 過濾條件），流程就會自動執行。

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。