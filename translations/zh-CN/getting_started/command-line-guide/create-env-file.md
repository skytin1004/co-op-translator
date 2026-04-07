# 在根目录中创建 *.env* 文件

在本教程中，我们将指导您如何使用 *.env* 文件设置 Azure 服务的环境变量。环境变量允许您安全地管理敏感凭据，如 API 密钥，而无需将其硬编码到代码库中。

> [!IMPORTANT]
> - 只需配置一个语言模型服务（Azure OpenAI 或 OpenAI）。填写您首选服务的环境变量。如果设置了多个语言模型的环境变量，Co-op Translator 将根据优先级选择一个。
> - 如果未设置计算机视觉的环境变量，翻译器将自动切换到[仅 Markdown 模式](./markdown-only-mode.md)。

> [!NOTE]
> 本指南主要关注 Azure 服务，但您也可以从[支持的模型和服务列表](../README.md#-supported-models-and-services)中选择任何支持的语言模型。

## 创建 *.env* 文件

在项目的根目录中，创建一个名为 *.env* 的文件。此文件将以简单格式存储您所有的环境变量。

> [!WARNING]
> 请勿将 *.env* 文件提交到版本控制系统如 Git。请将 *.env* 添加到您的 .gitignore 文件中，以防止意外提交。

1. 进入项目的根目录。

1. 在项目的根目录中创建一个 *.env* 文件。

1. 打开 *.env* 文件并粘贴以下模板：

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
> 如果您想查找 API 密钥和端点，可以参考 [set-up-azure-ai.md](../set-up-azure-ai.md)。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们努力保证准确性，但请注意自动翻译可能包含错误或不准确之处。原始文档的母语版本应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->