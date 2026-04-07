# ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ರಚಿಸಿ

ಈ ಪಾಠಕ್ರಮದಲ್ಲಿ, ನಾವು ನಿಮಗೆ *.env* ಫೈಲ್ ಬಳಸಿ Azure ಸೇವೆಗಳಿಗಾಗಿ ನಿಮ್ಮ ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿಸುವುದನ್ನು ಮಾರ್ಗದರ್ಶನ ಮಾಡಲಿದ್ದೇವೆ. ಪರಿಸರ ಚರಗಳು ನಿಮ್ಮ ಕೋಡ್ ಬೇಸ್‌ನಲ್ಲಿ ಹಾರ್ಡ್-ಕೋಡ್ ಮಾಡದೆ API ಕೀಗಳು ಸೇರಿದಂತೆ ಸಂವೇದನಾಶೀಲ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ಭದ್ರವಾಗಿ ನಿರ್ವಹಿಸಲು ಸಹಕಾರಿಯಾಗಿದೆ.

> [!IMPORTANT]
> - ಒಬ್ಬ ಭಾಷಾ ಮಾದರಿ ಸೇವೆ (Azure OpenAI ಅಥವಾ OpenAI) ಮಾತ್ರ ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕಿದೆ. ನಿಮ್ಮ ಇಷ್ಟದ ಸೇವೆಗಾಗಿ ಪರಿಸರ ಚರಗಳನ್ನು ತುಂಬಿ. ಬಾಹ್ಯ ಭಾಷಾ ಮಾದರಿಗಳಿಗೆ ಪರಿಸರ ಚರಗಳು ಸಿದ್ಧಪಟ್ಟಿದ್ದಲ್ಲಿ, co-op translator ಆದ್ಯತೆಯ ಆಧಾರದಲ್ಲಿ ಒಂದನ್ನು ಆಯ್ಕೆಮಾಡುತ್ತದೆ.
> - Computer Vision ಪರಿಸರ ಚರಗಳನ್ನು ಹೊಂದಿಸದಿದ್ದರೆ, translator ಸ್ವಯಂಚಾಲಿತವಾಗಿ [Markdown-only mode](./markdown-only-mode.md) ಗೆ ಬದಲಾಯಿಸುತ್ತದೆ.

> [!NOTE]
> ಈ ಮಾರ್ಗದರ್ಶಿ ಮುಖ್ಯವಾಗಿ Azure ಸೇವೆಗಳ ಮೇಲೆ ಕೇಂದ್ರೀಕೃತವಾಗಿದೆ, ಆದರೆ ನೀವು [supported models and services list](../README.md#-supported-models-and-services) ನಿಂದ ಯಾವುದೇ ಬೆಂಬಲಿತ ಭಾಷಾ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಬಹುದು.

## *.env* ಫೈಲ್ ರಚಿಸಿ

ನಿಮ್ಮ ಯೋಜನೆಯ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಎಂಬ ಫೈಲ್ ರಚಿಸಿ. ಈ ಫೈಲ್ ಎಲ್ಲಾ ನಿಮ್ಮ ಪರಿಸರ ಚರಗಳನ್ನು ಸರಳ ಸ್ವರೂಪದಲ್ಲಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

> [!WARNING]
> ನಿಮ್ಮ *.env* ಫೈಲ್ ಅನ್ನು Git ಮುಂತಾದ ಸಂಚಿಕೆ ನಿಯಂತ್ರಣ ವ್ಯವಸ್ಥೆಗಳಿಗೆ ಕಮಿಟ್ ಮಾಡಬೇಡಿ. ಹಲವು ತಪ್ಪು ಕಮಿಟ್ ಗಳಾಗದಂತೆ *.env* ಅನ್ನು ನಿಮ್ಮ .gitignore ಫೈಲ್‌ಗೆ ಸೇರಿಸಿ.

1. ನಿಮ್ಮ ಯೋಜನೆಯ ಮೂಲ ಡೈರೆಕ್ಟರಿಗೆ ಹಾದಿ ಮಾಡಿ.

1. ನಿಮ್ಮ ಯೋಜನೆಯ ಮೂಲ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ರಚಿಸಿ.

1. *.env* ಫೈಲ್ ತೆರೆಯಿರಿ ಮತ್ತು ಕೆಳಗಿನ ಟೆಂಪ್ಲೇಟ್ನ್ನು ಅಂಟಿಸಿ:

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
> ನಿಮ್ಮ API ಕೀಯುಗಳು ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯಲು, ನೀವು [set-up-azure-ai.md](../set-up-azure-ai.md) ಅನ್ನು ಗಮನಿಸಬಹುದು.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ವಿಮರ್ಶೆಯ ನಿರಾಕರಣೆ**:  
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಅನುವಾದಕ್ಕಾಗಿ ಪ್ರಯತ್ನ ಮಾಡುತ್ತಿದ್ದೇವೆ ಆದರೆ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸೂಯಿತತೆಗಳು ಇರಬಹುದಾಗಿದೆ ಎಂಬುದನ್ನು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಇರುವ ಮೂಲ ದಾಖಲೆ ಸರಿಯಾದ ಮೂಲವಾಗಿರುತ್ತದೆ. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅಸ್ಪಷ್ಟತೆಗಳು ಅಥವಾ ತಪ್ಪು ವ್ಯಾಖ್ಯಾನಗಳಿಗೆ ನಾವು ಜವಾಬ್ದಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->