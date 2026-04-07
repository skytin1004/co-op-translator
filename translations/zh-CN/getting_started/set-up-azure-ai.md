# 为 Co-op Translator 设置 Azure AI（Azure OpneAI 和 Azure AI Vision）

本指南将引导您在 Azure AI Foundry 中设置 Azure OpenAI 进行语言翻译，以及设置 Azure 计算机视觉进行图像内容分析（然后可用于基于图像的翻译）。

**前提条件：**
- 拥有一个有效订阅的 Azure 账户。
- 在您的 Azure 订阅中具有创建资源和部署的足够权限。

## 创建 Azure AI 项目

您将首先创建一个 Azure AI 项目，该项目作为管理 AI 资源的中心位置。

1. 访问 [https://ai.azure.com](https://ai.azure.com) 并使用您的 Azure 账户登录。

1. 选择 **+Create** 创建一个新项目。

1. 执行以下任务：
   - 输入一个 <strong>项目名称</strong>（例如 `CoopTranslator-Project`）。
   - 选择 **AI 集线器**（例如 `CoopTranslator-Hub`）（如果需要，请新建一个）。

1. 点击 "<strong>审核并创建</strong>" 以设置您的项目。您将进入项目的概览页面。

## 设置 Azure OpenAI 用于语言翻译

在您的项目中，您将部署一个 Azure OpenAI 模型，作为文本翻译的后端。

### 进入您的项目

如果尚未进入，请在 Azure AI Foundry 中打开您新创建的项目（例如 `CoopTranslator-Project`）。

### 部署 OpenAI 模型

1. 在项目左侧菜单下的 "我的资产" 中，选择 "**模型 + 端点**"。

1. 选择 **+ 部署模型**。

1. 选择 <strong>部署基础模型</strong>。

1. 系统将显示可用模型列表。过滤或搜索一个合适的 GPT 模型。我们推荐使用 `gpt-4o`。

1. 选择您希望使用的模型，点击 <strong>确认</strong>。

1. 选择 <strong>部署</strong>。

### Azure OpenAI 配置

部署完成后，您可以在 "**模型 + 端点**" 页面选择该部署，查看其 **REST 端点 URL**、<strong>密钥</strong>、<strong>部署名称</strong>、<strong>模型名称</strong> 和 **API 版本**。这些信息是将翻译模型集成到您的应用中所需的。

> [!NOTE]
> 您可以从 [API 版本弃用](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 页面根据需求选择 API 版本。请注意，<strong>API 版本</strong>与 Azure AI Foundry 中 "**模型 + 端点**" 页面显示的 <strong>模型版本</strong> 是不同的。

## 设置 Azure 计算机视觉用于图像翻译

为了实现图像中文字的翻译，您需要找到 Azure AI 服务的 API 密钥和端点。

1. 进入您的 Azure AI 项目（例如 `CoopTranslator-Project`），确保您处于项目概览页面。

### Azure AI 服务配置

从 Azure AI 服务中找到 API 密钥和端点。

1. 进入您的 Azure AI 项目（例如 `CoopTranslator-Project`），确保您处于项目概览页面。

1. 在 Azure AI 服务标签页找到 **API 密钥** 和 <strong>端点</strong>。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

此连接使所关联的 Azure AI 服务资源（包括图像分析）功能可用于您的 AI Foundry 项目。您可以在笔记本或应用中使用此连接从图像中提取文本，随后将其发送到 Azure OpenAI 模型进行翻译。

## 整合您的凭据

现在，您应该已收集了以下内容：

**针对 Azure OpenAI（文本翻译）：**
- Azure OpenAI 端点
- Azure OpenAI API 密钥
- Azure OpenAI 模型名称（例如 `gpt-4o`）
- Azure OpenAI 部署名称（例如 `cooptranslator-gpt4o`）
- Azure OpenAI API 版本

**针对 Azure AI 服务（通过视觉进行图像文字提取）：**
- Azure AI 服务端点
- Azure AI 服务 API 密钥

### 示例：环境变量配置（预览）

之后在构建您的应用时，您可能会使用这些收集的凭据进行配置。例如，您可以将它们设置为环境变量，如下所示：

```bash
# Azure AI 服务凭据（图像翻译必需）
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 例如，21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# 可选备用集合：使用后缀 _1/_2 复制变量（集合中所有变量使用相同索引）
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI 凭据（文本翻译必需）
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 例如，21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 例如，gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 例如，cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 例如，2024-12-01-preview

# 可选备用集合：用后缀 _1/_2 复制完整的 AZURE_OPENAI_* 集合（所有变量使用相同索引）
```

---

### 进一步阅读

- [如何在 Azure AI Foundry 中创建项目](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [如何创建 Azure AI 资源](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [如何在 Azure AI Foundry 中部署 OpenAI 模型](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力保证准确性，但请注意自动翻译可能包含错误或不准确之处。原始语言版本的文件应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用本翻译所引起的任何误解或错误解释承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->