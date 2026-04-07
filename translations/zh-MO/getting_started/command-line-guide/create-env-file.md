# 在根目錄建立 *.env* 檔案

在本教學中，我們將指導你如何使用 *.env* 檔案設定 Azure 服務的環境變數。環境變數允許你安全地管理敏感憑證，例如 API 金鑰，而不需將它們硬編碼在程式碼中。

> [!IMPORTANT]
> - 只需配置一個語言模型服務（Azure OpenAI 或 OpenAI）。請填寫你偏好的服務的環境變數。如果同時設定了多個語言模型的環境變數，Co-op Translator 將根據優先順序選擇其中一個。
> - 如果未設定 Computer Vision 的環境變數，翻譯器將自動切換到[只限 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要聚焦於 Azure 服務，但你可以從[支援的模型和服務清單](../README.md#-supported-models-and-services)中選擇任何支援的語言模型。

## 建立 *.env* 檔案

在專案的根目錄中，建立一個名為 *.env* 的檔案。此檔案將以簡單的格式儲存所有你的環境變數。

> [!WARNING]
> 請勿將你的 *.env* 檔案提交至像 Git 這樣的版本控制系統，請在你的 .gitignore 檔案中將 *.env* 加入忽略清單，以避免誤提交。

1. 移動到你的專案根目錄。

1. 在專案根目錄建立 *.env* 檔案。

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
> 如果你想尋找你的 API 金鑰和端點，可以參考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。文件原文版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->