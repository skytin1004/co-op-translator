# 為 Co-op Translator 設置 Azure AI（Azure OpneAI 與 Azure AI Vision）

本指南將引導您在 Azure AI Foundry 中設置 Azure OpenAI 進行語言翻譯，以及 Azure 電腦視覺進行影像內容分析（之後可用於基於影像的翻譯）。

**先決條件：**
- 擁有活動訂閱的 Azure 帳戶。
- 具有在您的 Azure 訂閱中建立資源和部署的足夠權限。

## 建立 Azure AI 專案

您將從建立一個 Azure AI 專案開始，該專案作為管理您的 AI 資源的中心位置。

1. 前往 [https://ai.azure.com](https://ai.azure.com) 並使用您的 Azure 帳戶登入。

1. 選擇 **+Create** 建立新的專案。

1. 執行以下操作：
   - 輸入 <strong>專案名稱</strong>（例如：`CoopTranslator-Project`）。
   - 選取 **AI hub**（例如：`CoopTranslator-Hub`）（如果需要可建立新的）。

1. 點擊「<strong>檢閱並建立</strong>」以設置您的專案。您將被導向專案的概覽頁面。

## 設定 Azure OpenAI 以進行語言翻譯

在您的專案中，您將部署 Azure OpenAI 模型作為文字翻譯的後端。

### 導覽至您的專案

如果尚未在專案中，請打開您新建立的專案（如 `CoopTranslator-Project`）於 Azure AI Foundry。

### 部署 OpenAI 模型

1. 從專案左側功能表的「我的資產」中，選取「**模型 + 端點**」。

1. 選擇 **+ 部署模型**。

1. 選擇 <strong>部署基礎模型</strong>。

1. 您將看到可用模型清單。請篩選或搜尋合適的 GPT 模型。我們推薦 `gpt-4o`。

1. 選擇您要的模型並點擊 <strong>確認</strong>。

1. 選擇 <strong>部署</strong>。

### Azure OpenAI 配置

部署完成後，您可以在「**模型 + 端點**」頁面選取部署，找到其 **REST 端點 URL**、<strong>金鑰</strong>、<strong>部署名稱</strong>、<strong>模型名稱</strong> 以及 **API 版本**。這些資訊將用於將翻譯模型整合到您的應用程式中。

> [!NOTE]
> 您可以根據需求從 [API 版本終止支援](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 頁面選擇 API 版本。請留意 **API 版本** 與 Azure AI Foundry「模型 + 端點」頁面所示的 <strong>模型版本</strong> 是不同的。

## 設定 Azure 電腦視覺進行影像翻譯

若要啟用對影像中文字的翻譯，您需要找到 Azure AI 服務的 API 金鑰與端點。

1. 前往您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確定您在專案概覽頁面。

### Azure AI 服務配置

找到 Azure AI 服務的 API 金鑰與端點。

1. 前往您的 Azure AI 專案（例如 `CoopTranslator-Project`）。確定您在專案概覽頁面。

1. 從 Azure AI 服務分頁中找到 **API 金鑰** 與 <strong>端點</strong>。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此連接讓鏈結的 Azure AI 服務資源（包含影像分析）功能可用於您的 AI Foundry 專案。接著您就可以在筆記本或應用程式中使用此連接，從影像中擷取文字，並將其送至 Azure OpenAI 模型進行翻譯。

## 整合您的認證資料

至此，您應該已收集到以下資訊：

**針對 Azure OpenAI（文字翻譯）：**
- Azure OpenAI 端點
- Azure OpenAI API 金鑰
- Azure OpenAI 模型名稱（例如：`gpt-4o`）
- Azure OpenAI 部署名稱（例如：`cooptranslator-gpt4o`）
- Azure OpenAI API 版本

**針對 Azure AI 服務（透過視覺擷取影像文字）：**
- Azure AI 服務端點
- Azure AI 服務 API 金鑰

### 範例：環境變數配置（預覽）

之後在建置應用程式時，您可能會使用這些收集的認證來進行配置。例如，您可以將它們設為環境變數，如下：

```bash
# Azure AI 服務憑證（圖片翻譯必填）
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 例如，21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# 可選備用組：以後綴 _1/_2 複製變數（組內所有變數使用相同索引）
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI 憑證（文本翻譯必填）
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 例如，21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 例如，gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 例如，cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 例如，2024-12-01-preview

# 可選備用組：將完整的 AZURE_OPENAI_* 變數組以後綴 _1/_2 複製（所有變數使用相同索引）
```

---

### 延伸閱讀

- [如何在 Azure AI Foundry 建立專案](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何建立 Azure AI 資源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意自動翻譯可能包含錯誤或不準確之處。原始母語文件應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或錯誤詮釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->