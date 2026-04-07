# 為 Co-op Translator 設置 Azure AI（Azure OpenAI 與 Azure AI Vision）

本指南將帶您完成在 Azure AI Foundry 中設置 Azure OpenAI 進行語言翻譯以及 Azure 計算機視覺用於圖像內容分析（然後可用於基於圖像的翻譯）。

**先決條件：**
- 擁有具有有效訂閱的 Azure 帳戶。
- 擁有在您的 Azure 訂閱中建立資源和部署的足夠權限。

## 創建 Azure AI 專案

您將從創建一個 Azure AI 專案開始，該專案作為管理您的 AI 資源的集中地點。

1. 前往 [https://ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳戶登入。

1. 選擇 **+Create** 來新增專案。

1. 執行以下操作：
   - 輸入 <strong>專案名稱</strong>（例如 `CoopTranslator-Project`）。
   - 選擇 **AI hub**（例如 `CoopTranslator-Hub`）（如有需要，請新建一個）。

1. 點擊 "**Review and Create**" 以設置您的專案。您將被導向專案的總覽頁面。

## 設置 Azure OpenAI 進行語言翻譯

在您的專案中，您將部署一個 Azure OpenAI 模型，作為文字翻譯的後端。

### 導航到您的專案

如果尚未進入，請在 Azure AI Foundry 中打開您剛創建的專案（例如 `CoopTranslator-Project`）。

### 部署 OpenAI 模型

1. 從專案左側選單中，在「My assets」下選擇 "**Models + endpoints**"。

1. 選擇 **+ Deploy model**。

1. 選擇 **Deploy Base Model**。

1. 您將看到可用模型列表。您可以篩選或搜尋合適的 GPT 模型。我們推薦 `gpt-4o`。

1. 選擇您想要的模型，然後點擊 **Confirm**。

1. 點擊 **Deploy**。

### Azure OpenAI 配置

成功部署後，您可以在 "**Models + endpoints**" 頁面選擇該部署，以查找其 **REST endpoint URL**、**Key**、**Deployment name**、**Model name** 以及 **API version**。這些資訊將用於將翻譯模型整合至您的應用程式。

> [!NOTE]
> 您可以基於需求，從 [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 頁面選擇 API 版本。請注意，**API version** 與在 Azure AI Foundry 中 "**Models + endpoints**" 頁面上顯示的 **Model version** 版本不同。

## 設置 Azure 計算機視覺以進行圖像翻譯

若要啟用圖片中文字的翻譯，您需要尋找 Azure AI Service 的 API Key 與 Endpoint。

1. 導航到您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確保您位於專案總覽頁面。

### Azure AI 服務配置

從 Azure AI Service 查找 API Key 與 Endpoint。

1. 導航到您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確保您位於專案總覽頁面。

1. 從 Azure AI Service 分頁找到 **API Key** 與 **Endpoint**。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此連接使相關 Azure AI 服務資源（包括圖像分析）的功能可用於您的 AI Foundry 專案。您可在筆記本或應用中使用此連接從圖片中提取文字，然後將該文字發送至 Azure OpenAI 模型進行翻譯。

## 整合您的憑證

現在，您應該已收集以下資訊：

**針對 Azure OpenAI（文字翻譯）：**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name（例如 `gpt-4o`）
- Azure OpenAI Deployment Name（例如 `cooptranslator-gpt4o`）
- Azure OpenAI API Version

**針對 Azure AI 服務（透過 Vision 進行圖片文字提取）：**
- Azure AI Service Endpoint
- Azure AI Service API Key

### 範例：環境變數配置（預覽）

稍後，在建立應用時，您很可能會使用這些收集的憑證進行配置。例如，您可能會像以下這樣設定環境變數：

```bash
# Azure AI 服務認証資料（影像翻譯必需）
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 例如，21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# 可選的後備組：帶有後綴 _1/_2 的重複變數（套件中所有變數索引相同）
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI 認証資料（文字翻譯必需）
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 例如，21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 例如，gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 例如，cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 例如，2024-12-01-preview

# 可選的後備組：帶有後綴 _1/_2 的完整 AZURE_OPENAI_* 套件重複（所有變數索引相同）
```

---

### 進一步閱讀

- [如何在 Azure AI Foundry 中建立專案](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何建立 Azure AI 資源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 中部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，請注意自動翻譯可能包含錯誤或不精確之處。原文文件應視為權威來源。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤釋負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->