# Create the *.env* file for root directory

For this tutorial, we go guide you how to set up your environment variables for Azure services using *.env* file. Environment variables dey allow you manage sensitive credentials well-well, like API keys, without putting dem hard-hard inside your codebase.

> [!IMPORTANT]
> - Only one language model service (Azure OpenAI or OpenAI) need to be configured. Make you fill environment variables for the service wey you like. If environment variables for plenty language models dey set, the co-op translator go choose one based on priority.
> - If Computer Vision environment variables no set, the translator go automatically switch to [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> This guide mainly dey focus for Azure services, but you fit choose any language model wey support from the [supported models and services list](../README.md#-supported-models-and-services).

## Create the *.env* file

For your project root directory, create file wey dem go call *.env*. This file go hold all your environment variables for simple format.

> [!WARNING]
> No go commit your *.env* file go version control system like Git. Add *.env* for your .gitignore file make e no go commit by mistake.

1. Enter your project root directory.

1. Create *.env* file for project root directory.

1. Open the *.env* file and put this template inside:

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
> If you wan find your API keys and endpoints, you fit check [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translations fit get mistakes or wahala. Di original document wey na di native language na di true source. For important information, better make person wey sabi do human translation help you. We no go responsible for any kasala or wrong understanding wey fit show from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->