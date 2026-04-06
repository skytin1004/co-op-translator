# 在根目錄中建立 *.env* 檔案

在本教學中，我們將指導您如何使用 *.env* 檔案設定 Azure 服務的環境變數。環境變數讓您可以安全管理敏感憑證，例如 API 金鑰，而無需將其硬編碼在您的程式碼庫中。

> [!IMPORTANT]
> - 僅需配置一個語言模型服務（Azure OpenAI 或 OpenAI）。請填寫您偏好的服務對應的環境變數。如果設定了多個語言模型的環境變數，協作翻譯器將根據優先順序選擇其中一個。
> - 若未設定 Computer Vision 環境變數，翻譯器將自動切換至[僅限 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要聚焦於 Azure 服務，但您也可以從[支援的模型及服務列表](../README.md#-supported-models-and-services)中選擇任何支持的語言模型。

## 建立 *.env* 檔案

在您專案的根目錄中，建立一個名為 *.env* 的檔案。此檔案將以簡單格式存放所有環境變數。

> [!WARNING]
> 請勿將 *.env* 檔案提交至像 Git 這類版本控制系統。請將 *.env* 添加到您的 .gitignore 檔案中，避免意外提交。

1. 移動到您專案的根目錄。

1. 在專案根目錄中建立一個 *.env* 檔案。

1. 開啟 *.env* 檔案並貼上以下範本：

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> 若您想查看您的 API 金鑰與端點，可以參考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的原文版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->