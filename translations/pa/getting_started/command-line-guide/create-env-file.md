# ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿਚ *.env* ਫਾਇਲ ਬਣਾਓ

ਇਸ ਟਿਊਟੋਰਿਅਲ ਵਿੱਚ, ਅਸੀਂ ਤੁਹਾਨੂੰ Azure ਸੇਵਾਵਾਂ ਲਈ ਆਪਣੇ Environment variables ਸੈਟਅੱਪ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਾਂਗੇ ਜਿਸ ਲਈ *.env* ਫਾਇਲ ਦੀ ਵਰਤੋਂ ਕੀਤੀ ਜਾਵੇਗੀ। Environment variables ਤੁਹਾਨੂੰ ਸੰਵੇਦਨਸ਼ੀਲ ਕ੍ਰੇਡੈਂਸ਼ੀਅਲਜ਼, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀਆਂ, ਆਪਣੇ ਕੋਡਬੇਸ ਵਿਚ ਹਾਰਡ-ਕੋਡ ਕੀਤੇ ਬਿਨਾਂ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ।

> [!IMPORTANT]
> - ਸਿਰਫ਼ ਇੱਕ ਭਾਸ਼ਾ ਮਾਡਲ ਸੇਵਾ (Azure OpenAI ਜਾਂ OpenAI) ਦੀ ਸੰਰਚਨਾ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਆਪਣੀ ਪਸੰਦੀਦਾ ਸੇਵਾ ਲਈ Environment variables ਭਰੋ। ਜੇਕਰ ਇੱਕ ਤੋਂ ਵੱਧ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਲਈ Environment variables ਸੈੱਟ ਕਰੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ co-op translator ਤਰਜੀਹ ਦੇ ਅਧਾਰ 'ਤੇ ਇੱਕ ਚੁਣੇਗਾ।
> - ਜੇਕਰ Computer Vision ਦੇ Environment variables ਸੈੱਟ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ, ਤਾਂ translator ਆਪੋआप [Markdown-only mode](./markdown-only-mode.md) ਵਿੱਚ ਸਵਿੱਚ ਕਰ ਜਾਵੇਗਾ।

> [!NOTE]
> ਇਹ ਮਾਰਗਦਰਸ਼ਿਕਾ ਖਾਸ ਤੌਰ 'ਤੇ Azure ਸੇਵਾਵਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦਰਿਤ ਕਰਦੀ ਹੈ, ਪਰ ਤੁਸੀਂ [supported models and services list](../README.md#-supported-models-and-services) ਤੋਂ ਕਿਸੇ ਵੀ ਸਮਰਥਿਤ ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ ਚੁਣ ਸਕਦੇ ਹੋ।

## *.env* ਫਾਇਲ ਬਣਾਓ

ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *.env* ਨਾਮ ਦੀ ਫਾਇਲ ਬਣਾਓ। ਇਹ ਫਾਇਲ ਤੁਹਾਡੇ ਸਾਰੇ Environment variables ਨੂੰ ਇੱਕ ਸਧਾਰਣ ਫਾਰਮੈਟ ਵਿੱਚ ਸਟੋਰ ਕਰੇਗੀ।

> [!WARNING]
> ਆਪਣੀ *.env* ਫਾਇਲ ਨੂੰ Git ਵਰਗੇ ਵਰਜਨ ਕੰਟਰੋਲ ਸਿਸਟਮਾਂ ਵਿੱਚ ਕਾਮਿਟ ਨਾ ਕਰੋ। ਅਚਾਨਕ ਕਾਮਿਟ ਨੂੰ ਰੋਕਣ ਲਈ *.env* ਨੂੰ ਆਪਣੇ .gitignore ਫਾਇਲ ਵਿੱਚ ਜੋੜੋ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਰੂਟ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *.env* ਫਾਇਲ ਬਣਾਓ।

1. *.env* ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਟੈਂਪਲੇਟ ਪੇਸਟ ਕਰੋ:

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
> ਜੇਕਰ ਤੁਸੀਂ ਆਪਣੀਆਂ API ਕੁੰਜੀਆਂ ਅਤੇ ਐਂਡਪੋਇੰਟ ਲੱਭਣਾ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [set-up-azure-ai.md](../set-up-azure-ai.md) ਨੂੰ ਦੇਖ ਸਕਦੇ ਹੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋक्तੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸੁਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਦੁਸ਼ਪ੍ਰਭਾਵ ਜਾਂ ਅਸੂਚਿਤਤਾ ਹੋ ਸਕਦੀ ਹੈ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀ ਕਿਸੇ ਵੀ ਗਲਤ ਸਮਝ ਜਾਂ ਗਲਤ ਫ਼ਹਿਮੀ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->