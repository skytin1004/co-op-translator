# ರೂಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ರಚಿಸಿ

ಈ ತರಬೇತಿನಲ್ಲಿ, Azure ಸೇವೆಗಳಿಗಾಗಿ ನಿಮ್ಮ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳ ನಿರ್ವಹಣೆಯನ್ನು *.env* ಫೈಲ್ ಬಳಸಿ ಹೇಗೆ ಮಾಡಿಕೊಳ್ಳುವುದು ಎಂಬುದನ್ನು ನಾವು ಮಾರ್ಗದರ್ಶಿಸುತ್ತೇವೆ. ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳು API ಕಿಗಳಂತಹ ಸున్నಿತ ಪ್ರಮಾಣಪತ್ರಗಳನ್ನು ನಿಮ್ಮ ಕೋಡ್‌ಬೇಸ್‌ನಲ್ಲಿ ಹಾರ್ಡ್-ಕೋಡಿಂಗ್ ಮಾಡದೆ ಸುರಕ್ಷಿತವಾಗಿ ನಿರ್ವಹಿಸುವ ಅವಕಾಶ ನೀಡುತ್ತವೆ.

> [!IMPORTANT]
> - ಒಂದೇ ಭಾಷಾ ಮಾದರಿ ಸೇವೆಯನ್ನು (Azure OpenAI ಅಥವಾ OpenAI) ಕಾನ್ಫಿಗರ್ ಮಾಡಬೇಕು. ನಿಮ್ಮ ಆಯ್ಕೆಮಾಡಿದ ಸೇವೆಯ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ. ಹಲವು ಭಾಷಾ ಮಾದರಿಗಳಿಗೆ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳು ಸಿದ್ಧವಾಗಿದ್ದರೆ, ಕೋ-ಆಪ್ ಟ್ರಾನ್ಸ್‌ಲೇಟರ್ ಆದ್ಯತೆಯ ಆಧಾರದ ಮೇಲೆ ಒಂದನ್ನು ಆಯ್ಕೆ ಮಾಡಲಾಗುತ್ತದೆ.
> - Computer Vision ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳು ಇಲ್ಲದಿದ್ದರೆ, ಟ್ರಾನ್ಸ್‌ಲೇಟರ್ ಸ್ವಯಂಚಾಲಿತವಾಗಿ [Markdown-only ಮೋಡ್](./markdown-only-mode.md) ಗೆ ತಿರುಗುತ್ತದೆ.

> [!NOTE]
> ಈ ಗೈಡ್ ಪ್ರಮುಖವಾಗಿ Azure ಸೇವೆಗಳ ಮೇಲೆ ಕೈಗೊಳ್ಳುತ್ತದೆ, ಆದರೆ ನೀವು [ಸ್ಪೋರ್ಟ್ ಮಾಡಲಾದ ಮಾದರಿಗಳು ಮತ್ತು ಸೇವೆಗಳ ಪಟ್ಟಿ](../README.md#-supported-models-and-services) ಯಿಂದ ಯಾವುದೇ ಬೆಂಬಲಿತ ಭಾಷಾ ಮಾದರಿಯನ್ನು ಆಯ್ಕೆ ಮಾಡಬಹುದು.

## *.env* ಫೈಲ್ ಸೃಷ್ಟಿಸಿ

ನಿಮ್ಮ ಯೋಜನೆಯಲ್ಲಿ ರೂಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಎಂಬ ಫೈಲ್ ರಚಿಸಿ. ಈ ಫೈಲ್ ಎಲ್ಲಾ ನಿಮ್ಮ ಪರಿಸರ ವ್ಯತ್ಯಾಸಗಳನ್ನು ಸರಳ ಫಾರ್ಮ್ಯಾಟ್‌ನಲ್ಲಿ ಸಂಗ್ರಹಿಸುತ್ತದೆ.

> [!WARNING]
> ನಿಮ್ಮ *.env* ಫೈಲ್ ಅನ್ನು Git ಮುಂತಾದ ಆವೃತ್ತಿ ನಿಯಂತ್ರಣ ವ್ಯವಸ್ಥೆಗಳಿಗೆ ಕಮಿಟ್ ಮಾಡಬೇಡಿ. ಅಸಾವಧಾನ ಕಮಿಟ್ಗಳು ತಪ್ಪಿಸಲು *.env* ಅನ್ನು ನಿಮ್ಮ .gitignore ಫೈಲ್‌ಗೆ ಸೇರ್ಪಡೆ ಮಾಡಿ.

1. ನಿಮ್ಮ ಯೋಜನೆಯ ರೂಟ್ ಡೈರೆಕ್ಟರಿಗೆ ನವಿಗೇಟ್ ಮಾಡಿ.

1. ನಿಮ್ಮ ಯೋಜನೆಯ ರೂಟ್ ಡೈರೆಕ್ಟರಿಯಲ್ಲಿ *.env* ಫೈಲ್ ರಚಿಸಿ.

1. *.env* ಫೈಲ್ ತೆರೆದು ಕೆಳಗಿನ ಟೆಂಪ್ಲೇಟನ್ನು ಪೇಸ್ಟ್ ಮಾಡಿ:

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
> ನಿಮ್ಮ API ಕಿಗಳು ಮತ್ತು ಎಂಡ್‌ಪಾಯಿಂಟ್‌ಗಳನ್ನು ಕಂಡುಹಿಡಿಯಬೇಕಾದರೆ, ನೀವು [set-up-azure-ai.md](../set-up-azure-ai.md) ಅನ್ನು ನೋಡಿ.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಜವಾಬ್ದಾರಿ ನಿರಾಕರಣೆ**:  
ಈ ಡಾಕ್ಯುಮೆಂಟ್ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯನ್ನು ಸಾಧಿಸಲು ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷ್ಟಗಳು ಅಥವಾ ತಪ್ಪು ಮಾಹಿತಿ থাকতে ಸಾಧ್ಯತೆ ಇದೆ. ಮೂಲ ಡಾಕ್ಯುಮೆಂಟ್ ಅದರ ಸ್ಥಳೀಯ ಭಾಷೆಯಲ್ಲಿ ಅನುಮೋದಿತ ಮೂಲವನ್ನಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗೆ, ವೃತ್ತಿಪರ ಮಾನವನ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದವನ್ನು ಬಳಸಿದ ಹಿನ್ನೆಲೆಯಲ್ಲಿ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗ್ರಹಣ ಅಥವಾ ದುರ್ಭಾಷೆಯನ್ನು ಕುರಿತು ನಾವು ಜವಾಬ್ದಾರಿಯಾಗಿದ್ದೇವೆ ಎಂದು ಮನಗಾಣಿಸುವುದು ತಪ್ಪು.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->