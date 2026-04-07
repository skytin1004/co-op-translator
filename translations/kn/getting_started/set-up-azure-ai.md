# Co-op Translator ಗಾಗಿ Azure AI ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ (Azure OpenAI & Azure AI Vision)

ಈ ಮಾರ್ಗದರ್ಶಿಕೆಯಲ್ಲಿ ನೀವು Azure AI Foundryಯಲ್ಲಿ ಭಾಷಾಂತರಕ್ಕಾಗಿ Azure OpenAI ಮತ್ತು ಚಿತ್ರ ವಿಷಯ ವಿಶ್ಲೇಷಣೆಗೆ (ಅದನ್ನು ಚಿತ್ರಾಧಾರಿತ ಭಾಷಾಂತರಕ್ಕಾಗಿ ಬಳಸಬಹುದು) Azure Computer Vision ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡುವ ಕುರಿತು ತಿಳಿಸುವುದು.

**ಆಗತ್ಯಗಳು:**
- ಒಂದು ಸಕ್ರಿಯ ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್ ಹೊಂದಿರುವ Azure ಖಾತೆ.
- ನಿಮ್ಮ Azure ಸಬ್ಸ್ಕ್ರಿಪ್ಷನ್‌ನಲ್ಲಿ ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ನಿಯೋಜನೆಗಳನ್ನು ರಚಿಸಲು ಸಾಕ್ಷಮತೆ.

## Azure AI ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಿ

ನೀವು ಪ್ರಾರಂಭಿಸುವಿರಿ Azure AI ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವ ಮೂಲಕ, ಇದು ನಿಮ್ಮ AI ಸಂಪನ್ಮೂಲಗಳನ್ನು ನಿರ್ವಹಿಸಲು ಕೇಂದ್ರಸ್ಥಾನವಾಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

1. [https://ai.azure.com](https://ai.azure.com) ಗೆ ತೆರಳಿ ಮತ್ತು ನಿಮ್ಮ Azure ಖಾತೆಯಿಂದ ಸೈನ್ ಇನ್ ಆಗಿ.

1. ಹೊಸ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸಲು **+Create** ಆಯ್ಕೆಮಾಡಿ.

1. ಕೆಳಗಿನ ಕಾರ್ಯಗಳನ್ನು ಮಾಡಿ:
   - **Project name** ನಮೂದಿಸಿ (ಉದಾ: `CoopTranslator-Project`).
   - **AI hub** ಆಯ್ಕೆಮಾಡಿ (ಉದಾ: `CoopTranslator-Hub`) (ಅವಶ್ಯಕತೆ ಇದ್ದರೆ ಹೊಸದಾಗಿ ರಚಿಸಿ).

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಸೆಟ್ ಅಪ್ ಮಾಡಲು "**Review and Create**" ಕ್ಲಿಕ್ ಮಾಡಿ. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಓವerview ಪುಟಕ್ಕೆ ಕರೆತರುವರು.

## ಭಾಷಾಂತರಕ್ಕಾಗಿ Azure OpenAI ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ

ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ನಡುವೆ, ಪಠ್ಯ ಭಾಷಾಂತರದ ಬ್ಯಾಕ್‌ಎಂಡ್ ಆಗಿ ಕಾರ್ಯನಿರ್ವಹಿಸಲು ನೀವು ಒಂದು Azure OpenAI ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸುವಿರಿ.

### ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಗೆ ನೀವಿಗೊಳ್ಳಿ

ಇಲ್ಲಿರಲಿಲ್ಲೆ, ನಿಮ್ಮ ಹೊಸ ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ: `CoopTranslator-Project`) ಅನ್ನು Azure AI Foundryಯಲ್ಲಿ ತೆರೆಯಿರಿ.

### OpenAI ಮಾದರಿಯನ್ನು ನಿಯೋಜಿಸಿ

1. ನಿಮ್ಮ ಪ್ರಾಜೆಕ್ಟ್ ಎಡ ಬದಿಯ ಮೆನುದಿಂದ, "My assets" ಕೆಳಗೆ "**Models + endpoints**" ಆಯ್ಕೆಮಾಡಿ.

1. **+ Deploy model** ಆಯ್ಕೆಮಾಡಿ.

1. **Deploy Base Model** ಆಯ್ಕೆಮಾಡಿ.

1. ಲಭ್ಯವಿರುವ ಮಾದರಿಗಳ ಪಟ್ಟಿ ನಿಮಗೆ ತೋರಿಸಲಾಗುತ್ತದೆ. ಸೂಕ್ತವಾದ GPT ಮಾದರಿಯನ್ನು ಹುಡುಕಿ ಅಥವಾ ಫಿಲ್ಟರ್ ಮಾಡಿ. ನಾವು `gpt-4o` ಅನ್ನು ಶಿಫಾರಸು ಮಾಡುತ್ತೇವೆ.

1. ನಿಮ್ಮ ಇಚ್ಛಿತ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಿಸಿ **Confirm** ಕ್ಲಿಕ್ ಮಾಡಿ.

1. **Deploy** ಕ್ಲಿಕ್ ಮಾಡಿ.

### Azure OpenAI ಸಂರಚನೆ

ನಿಯೋಜನೆ ನಂತರ, ನೀವು "**Models + endpoints**" ಪುಟದಿಂದ ನಿಯೋಜನೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ ಅದರ **REST endpoint URL**, **Key**, **Deployment name**, **Model name** ಮತ್ತು **API version** ಅನ್ನು ಕಂಡುಹಿಡಿಯಬಹುದು. ಈ ಗಳು ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್‌ನಲ್ಲಿ ಭಾಷಾಂತರ ಮಾದರಿಯನ್ನು ಸಂಯೋಜಿಸಲು ಅಗತ್ಯವಿರುತ್ತವೆ.

> [!NOTE]
> ನಿಮ್ಮ ಅಗತ್ಯಗಳಿಗೆ ತಕ್ಕಂತೆ [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ಪುಟದಿಂದ API ಆವೃತ್ತಿಗಳನ್ನು ಆಯ್ಕೆಮಾಡಬಹುದು. ಗಮನಿಸಿ, **API version** ಹಿಂದಿನ Azure AI Foundryಯ "**Models + endpoints**" ಪುಟದ **Model version**ನಿಂದ ವಿಭಿನ್ನವಾಗಿದೆ.

## ಚಿತ್ರ ಭಾಷಾಂತರಕ್ಕಾಗಿ Azure Computer Vision ಅನ್ನು ಸೆಟ್ ಅಪ್ ಮಾಡಿ

ಚಿತ್ರಗಳೊಳಗಿನ ಪಠ್ಯದ ಭಾಷಾಂತರಕ್ಕೆ ಸಧ್ಯ ದಪ್ಪ ಡಾಯಲಾಗಿಂ, ನೀವು Azure AI Service API ಕೀ ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್ ಅನ್ನು ಹುಡುಕಬೇಕು.

1. ನಿಮ್ಮ Azure AI ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಹಾದುಹೋಗಿ (ಉದಾ: `CoopTranslator-Project`). ನೀವು ಪ್ರಾಜೆಕ್ಟ್ ಓವerview ಪುಟದಲ್ಲಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ.

### Azure AI Service ಸಂರಚನೆ

Azure AI Service ನಿಂದ API ಕೀ ಮತ್ತು ಎಂಡ್ಪಾಯಿಂಟ್ ಕಂಡುಹಿಡಿಯಿರಿ.

1. ನಿಮ್ಮ Azure AI ಪ್ರಾಜೆಕ್ಟ್ (ಉದಾ: `CoopTranslator-Project`) ಗೆ ಹೋಗಿ. ಪ್ರಾಜೆಕ್ಟ್ ಓವerview ಪುಟದಲ್ಲಿರಲಿ.

1. Azure AI Service ಟ್ಯಾಬ್ ನಿಂದ **API Key** ಮತ್ತು **Endpoint** ಕಂಡುಹಿಡಿಯಿರಿ.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ಈ ಸಂಪರ್ಕವು ಲಿಂಕ್ ಮಾಡಿದ Azure AI Services ಸಂಪನ್ಮೂಲಗಳ ಸಾಮರ್ಥ್ಯಗಳನ್ನು (ಚಿತ್ರ ವಿಶ್ಲೇಷಣೆಯನ್ನು ಒಳಗೊಂಡಂತೆ) ನಿಮ್ಮ AI Foundry ಪ್ರಾಜೆಕ್ಟ್‌ಗೆ ಲಭ್ಯವಿಡುತ್ತದೆ. ಇದನ್ನು ನಿಮ್ಮ ನೋಟ್ಬುಕ್ಸ್ ಅಥವಾ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ ಬಳಸಿ ಚಿತ್ರಗಳೊಳಗಿನ ಪಠ್ಯವನ್ನು ತೆಗೆದುಕೊಂಡು ಅದನ್ನು ನಂತರ ಭಾಷಾಂತರಕ್ಕಾಗಿ Azure OpenAI ಮಾದರಿಗೆ ಕಳುಹಿಸಬಹುದು.

## ನಿಮ್ಮ ಪ್ರಮಾಣಪತ್ರಗಳ ಸಂಕ್ಷೇಪಣ

ಈಗಾಗಲೇ ನೀವು ಕೆಳಕಂಡವುಗಳನ್ನು ಸಂಗ್ರಹಿಸಿರಬೇಕು:

**Azure OpenAI (ಪಠ್ಯ ಭಾಷಾಂತರ) ಗಾಗಿ:**
- Azure OpenAI ಎಂಡ್ಪಾಯಿಂಟ್
- Azure OpenAI API ಕೀ
- Azure OpenAI ಮಾದರಿ ಹೆಸರು (ಉದಾ: `gpt-4o`)
- Azure OpenAI ನಿಯೋಜನೆ ಹೆಸರು (ಉದಾ: `cooptranslator-gpt4o`)
- Azure OpenAI API ಆವೃತ್ತಿ

**Azure AI ಸೇವೆಗಳು (ಚಿತ್ರ ಪಠ್ಯದ ನೇಮಕಾತಿ Vision ಮೂಲಕ) ಗಾಗಿ:**
- Azure AI Service ಎಂಡ್ಪಾಯಿಂಟ್
- Azure AI Service API ಕೀ

### ಉದಾಹರಣೆ: ಪರಿಸರ ವ್ಯತ್ಯಾಸ ಸಂರಚನೆ (ಪ್ರಿವ್ಯೂ)

ನಂತರ, ನಿಮ್ಮ ಅಪ್ಲಿಕೇಶನ್ ನಿರ್ಮಿಸುವಾಗ, ನೀವು ಈ ಸಂಗ್ರಹಿಸಿದ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಬಳಸಿಕೊಂಡು ನಿಯೋಜಿಸಬಹುದು. ಉದಾಹರಣೆಗೆ, ನೀವು ಅವುಗಳನ್ನು ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳಾಗಿ ಕಾನ್ಫಿಗರ್ ಮಾಡಬಹುದು:

```bash
# ಆಜೂರ್ AI ಸೇವೆ ಕ್ರೆಡೆನ್ಷಿಯಲ್ಸ್ (ಚಿತ್ರ ಅನುವಾದಕ್ಕೆ ಅಗತ್ಯ)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ಉದಾ., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ಐಚ್ಛಿಕ ಬ್ಯಾಕಪ್ ಸೆಟ್‌ಗಳು: ಅನುಕ್ರಮಾಂಕ _1/_2 ಸಮಾನವಾದ ಅಂಶಗಳೊಂದಿಗೆ ನಕಲಿ ಚರಗಳು (ಸೆಟ್‌ನ ಎಲ್ಲಾ ಚರಗಳಿಗೆ ಒಂದೇ ಸೂಚ್ಯಂಕ)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# ಆಜೂರ್ ಓಪನ್‌ಎಐ ಕ್ರೆಡೆನ್ಷಿಯಲ್ಸ್ (ಪಠ್ಯ ಅನುವಾದಕ್ಕೆ ಅಗತ್ಯ)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ಉದಾ., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ಉದಾ., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ಉದಾ., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ಉದಾ., 2024-12-01-preview

# ಐಚ್ಛಿಕ ಬ್ಯಾಕಪ್ ಸೆಟ್‌ಗಳು: AZURE_OPENAI_* ಸಂಪೂರ್ಣ ಸೆಟ್ ಅನ್ನು ಸೂಚ್ಯಂಕ _1/_2 ಜೊತೆ ನಕಲಿಸಿ (ಎಲ್ಲಾ ಚರಗಳಿಗೆ ಒಂದೇ ಸೂಚ್ಯಂಕ)
```

---

### ಹೆಚ್ಚುವರಿ ಓದು

- [Azure AI Foundryಯಲ್ಲಿ ಪ್ರಾಜೆಕ್ಟ್ ರಚಿಸುವ ವಿಧಗಳು](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI ಸಂಪನ್ಮೂಲಗಳನ್ನು ರಚಿಸುವ ವಿಧಾನ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundryಯಲ್ಲಿ OpenAI ಮಾದರಿಗಳನ್ನು ನಿಯೋಜಿಸುವ ವಿಧಾನ](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ವಿಮുക്തಿ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಉಪಯೋಗಿಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಅನುವಾದದಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂಬ ನುಡಿಯೋತ್ಸವ ವಹಿಸಲು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯ ಮೂಲ ದಾಖಲೆ ಪ್ರಾಮಾಣಿಕ ಮಾಧ್ಯಮವಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದದ ಸಲಹೆ ನೀಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಬೇಧನೆಗಳು ಅಥವಾ ದುರ್ವುವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->