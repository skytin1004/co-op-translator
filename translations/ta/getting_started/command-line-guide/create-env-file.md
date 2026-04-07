# Root கோப்பகத்தில் *.env* கோப்பை உருவாக்குக

இந்த பாடத்தில், Azure சேவைகளுக்கான உங்கள் சுற்றுப்புற மாறிகளைக் *.env* கோப்பைப் பயன்படுத்தி அமைப்பதற்கான வழிமுறைகளை நாம் 안내 செய்வோம். சுற்றுப்புற மாறிகள் API முக்கியங்கள் போன்ற சென்சிடிவ் சான்றுகளை உங்கள் குறியீட்டு அடிப்படையில் நேரடியாக எழுதாமல் பாதுகாப்பாக நிர்வகிக்க உதவுகிறது.

> [!IMPORTANT]
> - ஒரே ஒரு மொழி மாதிரி சேவையையே (Azure OpenAI அல்லது OpenAI) அமைக்க வேண்டும். உங்கள் விருப்ப சேவைக்கான சுற்றுப்புற மாறிகளை நிரப்பவும். பல மொழி மாதிரிகளுக்கான சுற்றுப்புற மாறிகள் அமைக்கப்பட்டால், co-op translator முன்னுரிமைப் புகுந்து ஒன்று தேர்ந்தெடுக்கும்.
> - கணினி பார்வை சுற்றுப்புற மாறிகள் அமைக்கப்படாவிட்டால், பிடிப்பான் தானாகவே [Markdown-only mode](./markdown-only-mode.md)க்கு மாறும்.

> [!NOTE]
> இந்த வழிகாட்டி பெரும்பாலும் Azure சேவைகளுக்கு முக்கியமாக உள்ளது, ஆனால் நீங்கள் [supported models and services list](../README.md#-supported-models-and-services)இல் இருந்த ஏதாவது ஆதரவு பெற்ற மொழி மாதிரியையும் தேர்வு செய்யலாம்.

## *.env* கோப்பை உருவாக்குக

உங்கள் திட்டத்தின் root கோப்பகத்தில் *.env* என்ற கோப்பை உருவாக்குங்கள். இந்த கோப்பு உங்கள் சுற்றுப்புற மாறிகளை எளிய வடிவில் சேமிக்கும்.

> [!WARNING]
> உங்கள் *.env* கோப்பை Git போன்ற பதிப்பு கட்டுப்பாட்டு அமைப்புகளில் commit செய்ய வேண்டாம். தவறுதலாக commit ஆகாமல் தடுப்பதற்காக *.env*ஐ உங்கள் .gitignore கோப்பில் சேர்க்கவும்.

1. உங்கள் திட்டத்தின் root கோப்பகத்துக்கு செல்லவும்.

1. திட்டத்தின் root கோப்பகத்தில் *.env* கோப்பை உருவாக்கவும்.

1. *.env* கோப்பைத் திறந்து கீழ்காணும் வார்ப்புருவை ஒட்டவும்:

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
> உங்கள் API முக்கியங்கள் மற்றும் endpoints எங்கே என்பதை கண்டுபிடிக்க விரும்பினால், [set-up-azure-ai.md](../set-up-azure-ai.md) ஐப் பார்க்கலாம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**உறுதிப்பத்திரம்**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானாக செய்யப்பட்ட மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அசல் ஆவணம் அதன் இயல்புமொழியில் அங்கீகாரமான மூலம் ஆகக் கணக்கிடப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதிலிருந்து ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான பொருளீடுகளுக்கும் நாம் பொறுப்பாக இல்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->