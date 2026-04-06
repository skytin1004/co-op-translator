# Create the *.env* file for inside root directory

For dis tutorial, we go show you how to setup your environment variables for Azure services using *.env* file. Environment variables dey allow you manage your sensitive credentials like API keys well well without to put dem directly for your code.

> [!IMPORTANT]
> - Only one language model service (Azure OpenAI or OpenAI) na the one wey you need to configure. Fill the environment variables for the service wey you prefer. If environment variables for plenty language models set, the co-op translator go choose one based on priority.
> - If Computer Vision environment variables no set, the translator go automatically change to [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Dis guide mainly dey focus on Azure services, but you fit choose any supported language model from the [supported models and services list](../README.md#-supported-models-and-services).

## Create the *.env* file

For your project root directory, create one file wey dem go call *.env*. Dis file go hold all your environment variables for one simple format.

> [!WARNING]
> No put your *.env* file for version control systems like Git. Add *.env* to your .gitignore file to avoid make you accidentally commit am.

1. waka go your project root directory.

1. Create *.env* file inside your project root directory.

1. Open the *.env* file come paste this template:

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
> If you want find your API keys and endpoints, you fit refer to [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). As we dey try make am correct, abeg sabi say automated translations fit get errors or mistakes. Di original document wey dey im normal language na im be di correct source. For important information, e better make professional human translation do am. We no go responsible for any misunderstanding or wrong interpretation wey fit come from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->