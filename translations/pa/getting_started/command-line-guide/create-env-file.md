# ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ *.env* ਫਾਇਲ ਬਣਾਓ

ਇਸ ਟਿਊਟੋਰੀਅਲ ਵਿੱਚ, ਅਸੀਂ ਤੁਹਾਨੂੰ Azure ਸੇਵਾਵਾਂ ਲਈ ਆਪਣੇ ਵਾਤਾਵਰਣ ਚਲਕਾਂ ਨੂੰ *.env* ਫਾਇਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਸੈਟਅੱਪ ਕਰਨ ਵਿੱਚ ਗਾਈਡ ਕਰਾਂਗੇ। ਵਾਤਾਵਰਣ ਚਲਕਾਂ ਤੁਹਾਨੂੰ ਸੰਵੇਦਨਸ਼ੀਲ ਪ੍ਰਮਾਣ ਪੱਤਰਾਂ, ਜਿਵੇਂ ਕਿ API ਕੁੰਜੀਆਂ, ਨੂੰ ਸੁਰੱਖਿਅਤ ਤਰੀਕੇ ਨਾਲ ਪ੍ਰਬੰਧਿਤ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ, ਬਿਨਾਂ ਉਹਨਾਂ ਨੂੰ ਆਪਣੇ ਕੋਡਬੇਸ ਵਿੱਚ ਹਾਰਡ-ਕੋਡ ਕੀਤੇ।

> [!IMPORTANT]
> - ਸਿਰਫ਼ ਇੱਕ ਭਾਸ਼ਾ ਮਾਡਲ ਸੇਵਾ (Azure OpenAI ਜਾਂ OpenAI) ਨੂੰ ਸੰਰਚਿਤ ਕਰਨ ਦੀ ਲੋੜ ਹੈ। ਆਪਣੀ ਪਸंदीਦਾ ਸੇਵਾ ਲਈ ਵਾਤਾਵਰਣ ਚਲਕਾਂ ਭਰੋ। ਜੇਕਰ ਕਈ ਭਾਸ਼ਾ ਮਾਡਲਾਂ ਦੇ ਵਾਤਾਵਰਣ ਚਲਕ ਸੈੱਟ ਕੀਤੇ ਜਾਂਦੇ ਹਨ, ਤਾਂ co-op translator ਪ੍ਰਾਥਮਿਕਤਾ ਦੇ ਆਧਾਰ 'ਤੇ ਇੱਕ ਚੁਣੇਗਾ।  
> - ਜੇਕਰ Computer Vision ਵਾਤਾਵਰਣ ਚਲਕ ਸੈੱਟ ਨਹੀਂ ਕੀਤੇ ਜਾਂਦੇ, ਤਾਂ translator ਆਪੇ ਹੀ [Markdown-only mode](./markdown-only-mode.md) ਵਿੱਚ ਬਦਲ ਜਾਵੇਗਾ।

> [!NOTE]  
> ਇਹ ਗਾਈਡ ਮੁੱਖ ਤੌਰ 'ਤੇ Azure ਸੇਵਾਵਾਂ 'ਤੇ ਧਿਆਨ ਕੇਂਦ੍ਰਿਤ ਕਰਦੀ ਹੈ, ਪਰ ਤੁਸੀਂ [supported models and services list](../README.md#-supported-models-and-services) ਵਿਚੋਂ ਕਿਸੇ ਵੀ ਸਮਰਥਿਤ ਭਾਸ਼ਾ ਮਾਡਲ ਨੂੰ ਚੁਣ ਸਕਦੇ ਹੋ।

## *.env* ਫਾਇਲ ਬਣਾਓ

ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ, ਇੱਕ *.env* ਨਾਂ ਦੀ ਫਾਇਲ ਬਣਾਓ। ਇਹ ਫਾਇਲ ਸਾਰੇ ਵਾਤਾਵਰਣ ਚਲਕ ਇੱਕ ਸਧਾਰਨ ਫਾਰਮੈਟ ਵਿੱਚ ਸਟੋਰ ਕਰੇਗੀ।

> [!WARNING]
> ਆਪਣੀ *.env* ਫਾਇਲ ਨੂੰ Git ਵਰਗੇ ਵਰਜਨ ਕੰਟਰੋਲ ਸਿਸਟਮਾਂ ਵਿੱਚ ਕੰਮਿਟ ਨਾ ਕਰੋ। ਅਕਸਮਾਤ ਕੰਮਿਟ ਤੋਂ ਬਚਣ ਲਈ *.env* ਨੂੰ ਆਪਣੇ .gitignore ਫਾਇਲ ਵਿੱਚ ਸ਼ਾਮਿਲ ਕਰੋ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਜਾਓ।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੀ ਮੂਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਇੱਕ *.env* ਫਾਇਲ ਬਣਾਓ।

1. *.env* ਫਾਇਲ ਖੋਲ੍ਹੋ ਅਤੇ ਹੇਠਾਂ ਦਿੱਤਾ ਟੈਂਪਲੇਟ ਚਿਪਕਾਓ:

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
> ਜੇਕਰ ਤੁਸੀਂ ਆਪਣੀਆਂ API ਕੁੰਜੀਆਂ ਅਤੇ ਏਂਡਪੌਇੰਟ ਖੋਜਣੀ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ਤੁਸੀਂ [set-up-azure-ai.md](../set-up-azure-ai.md) ਤੋਂ ਸੰਦਰਭ ਲੈ ਸਕਦੇ ਹੋ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏ.ਆਈ. ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸ਼ੁੱਧਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੇ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸੂਤਰ ਵਜੋਂ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਸੰਵੇਦਨਸ਼ੀਲ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਉਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->