<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "66029e3b67a3eb980ab8740367e91283",
  "translation_date": "2025-10-22T11:17:10+00:00",
  "source_file": "getting_started/command-line-guide/create-env-file.md",
  "language_code": "pcm"
}
-->
# How to create *.env* file for di main folder

For dis tutorial, we go show you how you fit set up environment variables wey Azure dey use, with *.env* file. Environment variables dey help you keep your secret credentials like API keys safe, so you no go need put am inside your code direct.

> [!IMPORTANT]
> - Na only one language model service (Azure OpenAI or OpenAI) you need configure. Just fill the environment variables for the one wey you wan use. If you set environment variables for more than one language model, the co-op translator go pick one based on priority.
> - If you no set Computer Vision environment variables, the translator go just switch to [Markdown-only mode](./markdown-only-mode.md) by itself.

> [!NOTE]
> This guide na mainly for Azure services, but you fit still use any language model wey dey inside the [supported models and services list](../README.md#-supported-models-and-services).

## How to create *.env* file

For the main folder of your project, create one file wey you go name *.env*. Na this file go hold all your environment variables for simple way.

> [!WARNING]
> No put your *.env* file for version control like Git. Make sure say you add *.env* for your .gitignore file so e no go enter your commit by mistake.

1. Go the main folder for your project.

1. Create *.env* file for the main folder of your project.

1. Open the *.env* file, then copy and paste this template inside:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"
    ```

> [!NOTE]
> If you wan find your API keys and endpoints, check [set-up-azure-ai.md](../set-up-azure-ai.md).

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate this document. Even though we try make the translation correct, abeg make you sabi say AI fit make mistake or no translate am well. Na the original document for the main language be the correct one wey you suppose follow. If the information dey important, abeg use professional human translator. We no go fit hold any responsibility for wahala or misunderstanding wey fit happen because of this translation.