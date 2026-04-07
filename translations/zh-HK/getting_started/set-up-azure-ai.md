# 建立 Azure AI 用於 Co-op Translator（Azure OpneAI 與 Azure AI Vision）

本指南將引導您在 Azure AI Foundry 中設定 Azure OpenAI 用於語言翻譯，以及 Azure 電腦視覺用於圖像內容分析（然後可用於基於圖像的翻譯）。

**先決條件：**
- 具備有效訂閱的 Azure 帳戶。
- 在您的 Azure 訂閱中具有建立資源和部署的足夠權限。

## 建立 Azure AI 專案

您將從建立一個 Azure AI 專案開始，該專案作為管理您的 AI 資源的中心位置。

1. 前往 [https://ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳戶登入。

1. 選擇 **+Create** 以建立新專案。

1. 執行以下操作：
   - 輸入 **Project name**（例如 `CoopTranslator-Project`）。
   - 選擇 **AI hub** （例如 `CoopTranslator-Hub`）（如有需要可建立新的）。

1. 點擊「**Review and Create**」以設定專案。系統將帶您至專案的概覽頁面。

## 設定 Azure OpenAI 用於語言翻譯

在您的專案中，您將部署 Azure OpenAI 模型，作為文本翻譯的後端。

### 導航至您的專案

如果尚未進入，請打開您新建立的專案（例如 `CoopTranslator-Project`）於 Azure AI Foundry。

### 部署 OpenAI 模型

1. 在專案左側選單中，於「My assets」下，選擇「**Models + endpoints**」。

1. 選擇 **+ Deploy model**。

1. 選擇 **Deploy Base Model**。

1. 系統將顯示可用模型列表。篩選或搜尋合適的 GPT 模型。我們建議使用 `gpt-4o`。

1. 選擇您想要的模型，然後點擊 **Confirm**。

1. 選擇 **Deploy**。

### Azure OpenAI 配置

成功部署後，您可以在「**Models + endpoints**」頁面選取該部署，查找其 **REST endpoint URL**、**Key**、**Deployment name**、**Model name** 與 **API version**。這些資訊將用於將翻譯模型整合進您的應用程式。

> [!NOTE]
> 您可以根據需求，從 [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 頁面選擇 API 版本。請注意，**API 版本** 與 Azure AI Foundry 「Models + endpoints」頁面展示的 **Model 版本** 不同。

## 設定 Azure 電腦視覺用於圖像翻譯

為了啟用圖像中的文字翻譯，您需要取得 Azure AI 服務的 API Key 及 Endpoint。

1. 導航至您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確保您在專案概覽頁面。

### Azure AI 服務配置

從 Azure AI 服務頁籤查找 API Key 和 Endpoint。

1. 導航至您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確保您在專案概覽頁面。

1. 從 Azure AI 服務標籤中找到 **API Key** 與 **Endpoint**。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此連接使得已連結的 Azure AI 服務資源（包括圖像分析）功能可用於您的 AI Foundry 專案。您便可在筆記本或應用中使用此連接從圖像萃取文字，再將其送至 Azure OpenAI 模型進行翻譯。

## 整理您的憑證

到此，您應該已收集了以下資訊：

**Azure OpenAI（文字翻譯）相關資料：**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name（例如 `gpt-4o`）
- Azure OpenAI Deployment Name（例如 `cooptranslator-gpt4o`）
- Azure OpenAI API Version

**Azure AI 服務（透過 Vision 進行圖像文字萃取）相關資料：**
- Azure AI Service Endpoint
- Azure AI Service API Key

### 範例：環境變數設定（預覽）

日後建立應用程式時，您很可能會用這些收集的憑證來設定環境變數，例如：

```bash
# Azure AI 服務憑證（圖片翻譯必需）
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 例如，21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# 可選的後備組：重複變量並加上後綴 _1/_2（同一組的所有變量索引相同）
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI 憑證（文字翻譯必需）
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 例如，21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 例如，gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 例如，cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 例如，2024-12-01-preview

# 可選的後備組：複製完整 AZURE_OPENAI_* 套組並加上後綴 _1/_2（所有變量索引相同）
```

---

### 延伸閱讀

- [如何在 Azure AI Foundry 中建立專案](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何建立 Azure AI 資源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 中部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於準確性，但請注意，機械翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->