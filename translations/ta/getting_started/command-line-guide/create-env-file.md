# ரூட் அடைவைலில் *.env* கோப்பை உருவாக்கவும்

இந்த பயிற்சியில், Azure சேவைகளுக்கான உங்கள் சூழல் மாறிலிகளை *.env* கோப்பின் மூலம் அமைக்கும் முறையை 안내ப்போறோம். சூழல் மாறிலிகள் உங்கள் கோட்பாத்தியில் நுழையாமல் பாதுகாப்பான முறையில் உணவு விசைகள் போன்ற முக்கிய அம்சங்களை நிர்வகிக்க உதவுகின்றன.

> [!IMPORTANT]
> - ஒரு மொழி மாடல் சேவையே (Azure OpenAI அல்லது OpenAI) கட்டமைக்கப்பட வேண்டும். நீங்கள் விரும்பும் சேவைக்கான சூழல் மாறிலிகளை நிரப்பவும். பல மொழி மாடல்களுக்கான சூழல் மாறிலிகள் அமைக்கப்பட்டால், co-op translator முக்கியத்துவத்தைப் பொருத்து ஒன்று தேர்ந்தெடுக்கப்படும்.
> - கணினி பார்வை சூழல் மாறிலிகள் அமைக்கப்பட்டு இல்லையெனில், translator தானாகவும் [Markdown-only mode](./markdown-only-mode.md) க்கு மாறும்.

> [!NOTE]
> இந்த வழிகாட்டி முதன்மையாக Azure சேவைகளைக் கவனிக்கும், ஆனாலும் [ஆதரவுடன் கூடிய மாடல்களும் சேவைகளும் பட்டியலில்](../README.md#-supported-models-and-services) இருந்து எந்த மொழி மாடலையும் நீங்கள் தேர்ந்தெடுக்கலாம்.

## *.env* கோப்பை உருவாக்கவும்

உங்கள் 프로젝트 ரூட் அடைவிலே *.env* என்ற கோப்பை உருவாக்கவும். இந்தக் கோப்பு உங்கள் அனைத்து சூழல் மாறிலிகளையும் எளிய வடிவத்தில் சேமிக்கும்.

> [!WARNING]
> *.env* கோப்பை Git போன்ற பதிப்பு கட்டுப்பாட்டு அமைப்புகளுக்கு சமர்ப்பிக்க வேண்டாம். தவறுதலாக சமர்ப்பிப்பதைக் குறைக்க *.env* ஐ உங்கள் .gitignore கோப்பில் சேர்க்கவும்.

1. உங்கள் திட்டத்தின் ரூட் அடைவுக்கு சென்று.

1. ரூட் அடைவில் *.env* கோப்பை உருவாக்கவும்.

1. *.env* கோப்பை திறந்து கீழ்காணும் மாதிரியை ஒட்டவும்:

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
> உங்கள் API விசைகள் மற்றும் இடைமுகங்களை கண்டுபிடிக்க [set-up-azure-ai.md](../set-up-azure-ai.md) ஐ கூர்ந்து பார்க்கலாம்.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**பிரதி இணையறிக்கை**:  
இந்தக் கோப்பு AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் சரியானதற்காக முயற்சித்தாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனியுங்கள். மூலக் கோப்பு அதன் தாய்மொழியில் அங்கீகாரம் பெற்ற ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்ப மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டினால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பு கொள்ளமுடியாது.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->