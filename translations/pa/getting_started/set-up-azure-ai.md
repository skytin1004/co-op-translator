# Co-op Translator ਲਈ Azure AI ਸੈਟਅਪ ਕਰੋ (Azure OpneAI & Azure AI Vision)

ਇਹ ਮਾਰਗਦਰਸ਼ਕ ਤੁਹਾਨੂੰ Azure AI Foundry ਵਿੱਚ ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਲਈ Azure OpenAI ਅਤੇ ਚਿੱਤਰ ਸਮੱਗਰੀ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ Azure Computer Vision (ਜੋ ਤਦ ਉੱਪਰ ਅਧਾਰਿਤ ਅਨੁਵਾਦ ਲਈ ਵਰਤਿਆ ਜਾ ਸਕਦਾ ਹੈ) ਸੈਟਅਪ ਕਰਨ ਚਲਾਉਂਦਾ ਹੈ।

**ਜਰੂਰੀ ਸ਼ਰਤਾਂ:**
- ਇੱਕ Azure ਖਾਤਾ ਜਿਸ ਵਿੱਚ ਸਰਗਰਮ ਸਭਸਕ੍ਰਿਪਸ਼ਨ ਹੋਵੇ।
- ਆਪਣੇ Azure ਸਭਸਕ੍ਰਿਪਸ਼ਨ ਵਿੱਚ ਸਰੋਤ ਤੇ ਤੈਨਾਤੀਆਂ ਸਿਰਜਣ ਲਈ ਕਾਫੀ ਅਧਿਕਾਰ।

## ਇੱਕ Azure AI ਪ੍ਰੋਜੈਕਟ ਬਣਾਓ

ਤੁਸੀਂ ਇੱਕ Azure AI ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਨਾਲ ਸ਼ੁਰੂ ਕਰੋਗੇ, ਜੋ ਤੁਹਾਡੇ AI ਸਰੋਤਾਂ ਦੀ ਪ੍ਰਬੰਧਕੀ ਲਈ ਕੇਂਦਰੀ ਸਥਾਨ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ।

1. ਜਾਓ [https://ai.azure.com](https://ai.azure.com) ਅਤੇ ਆਪਣੇ Azure ਖਾਤੇ ਨਾਲ ਸਾਈਨ ਇਨ ਕਰੋ।

1. ਨਵਾਂ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਲਈ **+Create** ਚੁਣੋ।

1. ਹੇਠ ਲਿਖੇ ਕੰਮ ਕਰੋ:
   - ਇੱਕ **ਪ੍ਰੋਜੈਕਟ ਨਾਮ** ਦਰਜ ਕਰੋ (ਜਿਵੇਂ, `CoopTranslator-Project`)।
   - **AI hub** ਚੁਣੋ (ਉਦਾਹਰਨ ਵਜੋਂ, `CoopTranslator-Hub`) (ਜਰੂਰਤ ਹੋਣ ‘ਤੇ ਨਵਾਂ ਬਣਾਉ)।

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਨੂੰ ਸੈਟਅਪ ਕਰਨ ਲਈ "**Review and Create**" ‘ਤੇ ਕਲਿੱਕ ਕਰੋ। ਤੁਹਾਨੂੰ ਤੁਹਾਡੇ ਪ੍ਰੋਜੈਕਟ ਦੇ ਓਵਰਵਿਊ ਪੰਨੇ ‘ਤੇ ਲਿਜਾਇਆ ਜਾਵੇਗਾ।

## ਭਾਸ਼ਾ ਅਨੁਵਾਦ ਲਈ Azure OpenAI ਸੈਟਅਪ ਕਰੋ

ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ, ਤੁਸੀਂ ਟੈਕਸਟ ਅਨੁਵਾਦ ਦੀ ਪਿਛੋਕੜ ਦੇ ਤੌਰ 'ਤੇ ਇੱਕ Azure OpenAI ਮਾਡਲ ਤੈਨात ਕਰੋਗੇ।

### ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਜਾਓ

ਜੇ ਪਹਿਲਾਂ ਨਹੀਂ ਕੀਤਾ ਹੈ, ਆਪਣਾ ਨਵਾਂ ਬਣਾਇਆ ਪ੍ਰੋਜੈਕਟ (ਉਦਾਹਰਨ ਵਜੋਂ, `CoopTranslator-Project`) Azure AI Foundry ਵਿੱਚ ਖੋਲ੍ਹੋ।

### ਇੱਕ OpenAI ਮਾਡਲ Deploy ਕਰੋ

1. ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੇ ਖੱਬੇ ਮੇਨੂ ਤੋਂ, "My assets" ਹੇਠਾਂ, "**Models + endpoints**" ਚੁਣੋ।

1. **+ Deploy model** ਚੁਣੋ।

1. **Deploy Base Model** ਚੁਣੋ।

1. ਤੁਹਾਨੂੰ ਉਪਲੱਬਧ ਮਾਡਲਾਂ ਦੀ ਸੂਚੀ ਦਿੱਤੀ ਜਾਵੇਗੀ। ਇੱਕ ਉਚਿਤ GPT ਮਾਡਲ ਖੋਜੋ ਜਾਂ ਛਾਂਟੋ। ਅਸੀਂ `gpt-4o` ਦੀ ਸਿਫਾਰਸ਼ ਕਰਦੇ ਹਾਂ।

1. ਆਪਣਾ ਚਾਹੀਦਾ ਮਾਡਲ ਚੁਣੋ ਅਤੇ **Confirm** ‘ਤੇ ਕਲਿੱਕ ਕਰੋ।

1. **Deploy** ਚੁਣੋ।

### Azure OpenAI ਸੰਰਚਨਾ

ਇੱਕ ਵਾਰ ਤੈਨਾਤ ਹੋ ਜਾਣ ‘ਤੇ, ਤੁਸੀਂ "**Models + endpoints**" ਪੰਨੇ ਤੋਂ ਤੈਨਾਤ ਨੂੰ ਚੁਣ ਕੇ ਇਸ ਦਾ **REST endpoint URL**, **Key**, **Deployment name**, **Model name** ਅਤੇ **API version** ਲੱਭ ਸਕਦੇ ਹੋ। ਇਹਨਾਂ ਦੀ ਲੋੜ ਤੁਹਾਡੇ ਅਨੁਵਾਦ ਮਾਡਲ ਨੂੰ ਆਪਣੇ ਐਪਲੀਕੇਸ਼ਨ ਨਾਲ ਜੋੜਨ ਲਈ ਪਵੇਗੀ।

> [!NOTE]
> ਤੁਸੀਂ ਆਪਣੀਆਂ ਲੋੜਾਂ ਅਨੁਸਾਰ [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ਪੰਨੇ ਤੋਂ API ਵਰਜਨ ਚੁਣ ਸਕਦੇ ਹੋ। ਧਿਆਨ ਰੱਖੋ ਕਿ **API version** ਭਿੰਨ ਹੈ ਉਸ **Model version** ਤੋਂ ਜੋ Azure AI Foundry ਵਿੱਚ "**Models + endpoints**" ਪੰਨੇ ‘ਤੇ ਦਿਖਾਇਆ ਜਾਂਦਾ ਹੈ।

## ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ Azure Computer Vision ਸੈਟਅਪ ਕਰੋ

ਚਿੱਤਰਾਂ ਵਿੱਚ ਲਿਖਤ ਦੇ ਅਨੁਵਾਦ ਨੂੰ ਯੋਗ ਕਰਨ ਲਈ, ਤੁਹਾਨੂੰ Azure AI Service ਦਾ API Key ਅਤੇ Endpoint ਲੱਭਣੇ ਹੋਣਗੇ।

1. ਆਪਣੇ Azure AI ਪ੍ਰੋਜੈਕਟ (ਜਿਵੇਂ `CoopTranslator-Project`) ‘ਤੇ ਜਾਓ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਪ੍ਰੋਜੈਕਟ ਓਵਰਵਿਊ ਪੰਨੇ ‘ਤੇ ਹੋ।

### Azure AI Service ਸੰਰਚਨਾ

Azure AI Service ਤੋਂ API Key ਅਤੇ Endpoint ਲੱਭੋ।

1. ਆਪਣੇ Azure AI ਪ੍ਰੋਜੈਕਟ (ਜਿਵੇਂ `CoopTranslator-Project`) ‘ਤੇ ਜਾਓ। ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਪ੍ਰੋਜੈਕਟ ਓਵਰਵਿਊ ਪੰਨੇ ‘ਤੇ ਹੋ।

1. Azure AI Service ਟੈਬ ਤੋਂ **API Key** ਅਤੇ **Endpoint** ਲੱਭੋ।

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ਇਹ ਕਨੈਕਸ਼ਨ ਜੋੜੇ ਗਏ Azure AI Services ਸਰੋਤ (ਜਿਸ ਵਿੱਚ ਚਿੱਤਰ ਵਿਸ਼ਲੇਸ਼ਣ ਵੀ ਸ਼ਾਮਲ ਹੈ) ਦੀਆਂ ਸਮਰੱਥਾਵਾਂ ਨੂੰ ਤੁਹਾਡੇ AI Foundry ਪ੍ਰੋਜੈਕਟ ਲਈ ਉਪਲੱਬਧ ਕਰਵਾਉਂਦਾ ਹੈ। ਫਿਰ ਤੁਸੀਂ ਆਪਣੇ ਨੋਟਬੁੱਕਾਂ ਜਾਂ ਐਪਲੀਕੇਸ਼ਨਾਂ ਵਿੱਚ ਇਸ ਕਨੈਕਸ਼ਨ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਚਿੱਤਰਾਂ ਵਿੱਚੋਂ ਲਿਖਤ ਕੱਢ ਸਕਦੇ ਹੋ, ਜਿਸਨੂੰ ਬਾਅਦ ਵਿੱਚ ਅਨੁਵਾਦ ਲਈ Azure OpenAI ਮਾਡਲ ਨੂੰ ਭੇਜਿਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਆਪਣੇ ਕਰੈਡੈਂਸ਼ਲ ਇੱਕਠੇ ਕਰੋ

ਹੁਣ ਤੱਕ, ਤੁਹਾਡੇ ਕੋਲ ਹੇਠ ਲਿਖੀਆਂ ਜਾਣਕਾਰੀਆਂ ਇਕੱਠੀਆਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ:

**Azure OpenAI (ਟੈਕਸਟ ਅਨੁਵਾਦ) ਲਈ:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI ਮਾਡਲ ਦਾ ਨਾਮ (ਜਿਵੇਂ, `gpt-4o`)
- Azure OpenAI Deployment ਨਾਮ (ਜਿਵੇਂ, `cooptranslator-gpt4o`)
- Azure OpenAI API ਵਰਜਨ

**Azure AI Services (ਦ੍ਰਿਸ਼ ਟੈਕਸਟ ਨਿਕਾਸ ਵਿਜ਼ਨ ਰਾਹੀਂ) ਲਈ:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ਉਦਾਹਰਨ: ਵਾਤਾਵਰਨ ਚਲਾਇਤੀ ਕੌਨਫਿਗਰੇਸ਼ਨ (ਪ੍ਰੀਵੀਅੂ)

ਬਾਅਦ ਵਿੱਚ, ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੀ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਓਗੇ, ਤਾਂ ਤੁਸੀਂ ਸੰਭਵ ਹੈ ਕਿ ਇਹਨਾਂ ਇੱਕੱਠੀਆਂ ਕੀਤੀਆਂ ਜਾਣਕਾਰੀਆਂ ਨੂੰ ਵਾਤਾਵਰਨ ਚਲਾਇਤੀ (environment variables) ਵਜੋਂ ਸੈੱਟ ਕਰੋਗੇ, ਉਦਾਹਰਨ ਵਜੋਂ:

```bash
# ਏਜ਼ੂਰ ਏਆਈ ਸੇਵਾ ਦੀਆਂ ਪ੍ਰਮਾਣਿਕਤਾ (ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ ਲੋੜੀਂਦਾ)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ਜਿਵੇਂ, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ਵਿਕਲਪਿਕ ਫਾਲਬੈਕ ਸੈਟ: ਸੂਫਿਕਸ _1/_2 ਨਾਲ ਨਕਲ ਕੀਤੀਆਂ ਵਾਰੀਏਬਲਾਂ (ਸੈੱਟ ਦੇ ਸਾਰੇ ਵਾਰੀਏਬਲਾਂ ਲਈ ਇੱਕੋ ਜਿਹਾ ਇੰਡੈਕਸ)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# ਏਜ਼ੂਰ ਓਪਨਏਆਈ ਪ੍ਰਮਾਣਿਕਤਾ (ਟੈਕਸਟ ਅਨੁਵਾਦ ਲਈ ਲੋੜੀਂਦਾ)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ਜਿਵੇਂ, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ਜਿਵੇਂ, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ਜਿਵੇਂ, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ਜਿਵੇਂ, 2024-12-01-preview

# ਵਿਕਲਪਿਕ ਫਾਲਬੈਕ ਸੈਟ: ਸੂਫਿਕਸ _1/_2 ਨਾਲ ਪੂਰਾ AZURE_OPENAI_* ਸੈੱਟ ਨਕਲ ਕਰੋ (ਸਾਰੇ ਵਾਰੀਏਬਲਾਂ ਲਈ ਇੱਕੋ ਜਿਹਾ ਇੰਡੈਕਸ)
```

---

### ਹੋਰ ਪੜ੍ਹਾਈ

- [Azure AI Foundry ਵਿੱਚ ਪ੍ਰੋਜੈਕਟ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI ਸਰੋਤ ਬਣਾਉਣ ਦਾ ਤਰੀਕਾ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry ਵਿੱਚ OpenAI ਮਾਡਲ ਤੈਨਾਤ ਕਰਨ ਦਾ ਤਰੀਕਾ](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਜਾਣੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਪਸ਼ਟਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਸਰਵੋਤਮ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਅਹੰਕਾਰਮਈ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਅਰਥ ਲੱਗਣ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->