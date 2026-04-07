# Co-op Translator க்கான Azure AI அமைக்கவும் (Azure OpenAI & Azure AI Vision)

இந்த வழிகாட்டி, Azure AI Foundry உள்ளே மொழி மொழிபெயர்க்க Azure OpenAI மற்றும் பட உள்ளடக்க বিশ্লেষণের জন্য Azure Computer Vision (பின்னர் படத்தின் அடிப்படையிலான மொழிபெயர்ப்புக்கு பயன்படக்கூடியது) அமைக்கும் முறையை விளக்குகின்றது.

**முன்னோட்டங்கள்:**
- செயல்பாட்டில் உள்ள Azure கணக்கு.
- உங்கள் Azure சந்தாவில் வளங்கள் மற்றும் அமர்வுகளை உருவாக்க உரிமைகள்.

## Azure AI திட்டத்தை உருவாக்கவும்

நீங்கள் Azure AI திட்டம் உருவாக்குவதில் தொடங்குவீர்கள், இது உங்கள் AI வளங்களை நிர்வகிக்க நடுவண் இடமாக செயல்படும்.

1. [https://ai.azure.com](https://ai.azure.com) செல்லுங்கள் மற்றும் உங்கள் Azure கணக்கில் உள்நுழையவும்.

1. புதிய திட்டம் உருவாக்க **+Create** தேர்வு செய்யவும்.

1. பின்வரும் பணிகளை செய்யவும்:
   - **Project name** உள்ளிடவும் (உதா., `CoopTranslator-Project`).
   - **AI hub** தேர்வு செய்யவும் (உதா., `CoopTranslator-Hub`) (தேவைப்படும் பட்சத்தில் புதிய ஒன்றை உருவாக்கவும்).

1. உங்கள் திட்டத்தை அமைக்க "**Review and Create**" கிளிக் செய்யவும். உங்களது திட்டம் சார்ந்த பார்வைப் பக்கம் திறக்கப்படும்.

## மொழி மொழிபெயர்க்க Azure OpenAI அமைக்கவும்

உங்கள் திட்டத்தின் உள்ளே, உரை மொழிபெயர்ப்புக்கு பின்னணி பணியாற்ற Azure OpenAI மாதிரியை அமர்த்துவீர்கள்.

### உங்கள் திட்டத்துக்கு செல்லவும்

இன்னும் திறக்கப்படவில்லை என்றால், உங்கள் புதிய திட்டத்தை (உதா., `CoopTranslator-Project`) Azure AI Foundry இல் திறக்கவும்.

### OpenAI மாதிரியை அமர்த்தவும்

1. உங்கள் திட்டத்தின் இடது மெனுவில் "My assets" கீழ் "**Models + endpoints**" தேர்வு செய்யவும்.

1. **+ Deploy model** தேர்வு செய்யவும்.

1. **Deploy Base Model** தேர்வு செய்யவும்.

1. கிடைக்கும் மாதிரிகள் பட்டியலைப்பாருங்கள். ஏற்ற மாதிரியை தேடவும் அல்லது வடிகட்டவும். நாம் பரிந்துரைக்கிறோம் `gpt-4o`.

1. நீங்கள் விரும்பும் மாதிரியை தேர்வு செய்து **Confirm** கிளிக் செய்யவும்.

1. **Deploy** தேர்வு செய்யவும்.

### Azure OpenAI கட்டமைப்பு

அமைக்கப்பட்டவுடன், "**Models + endpoints**" பக்கத்தில் இருந்து அமர்வு தொடர்பான **REST endpoint URL**, **Key**, **Deployment name**, **Model name** மற்றும் **API version** ஐ பெற்றுக்கொள்ளலாம். இவை உங்கள் பயன்பாட்டில் மொழிபெயர்ப்பு மாதிரியை இணைக்க தேவையாகும்.

> [!NOTE]
> தேவைகளின் அடிப்படையில் [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) பக்கத்தில் இருந்து API பதிப்புகளை தேர்வு செய்யலாம். Azure AI Foundry இல் "**Models + endpoints**" பக்கத்தில் காணப்படும் **Model version** உடன் **API version** வித்தியாசம் உள்ளது என்பதைக் கவனிக்கவும்.

## பட மொழிபெயர்க்க Azure Computer Vision அமைக்கவும்

படங்களில் உள்ள உரையை மொழிபெயர்க்க Azure AI Service API Key மற்றும் Endpoint ஐ கண்டறிய வேண்டும்.

1. உங்கள் Azure AI திட்டத்துக்குச் செல்லவும் (உதா., `CoopTranslator-Project`). திட்டத்தின் மேலோட்டப் பக்கத்தில் இருப்பதை உறுதிப்படுத்தவும்.

### Azure AI Service கட்டமைப்பு

Azure AI சேவை மூலம் API Key மற்றும் Endpoint கண்டறிந்து கொள்ளவும்.

1. உங்கள் Azure AI திட்டத்துக்குச் செல்லவும் (உதா., `CoopTranslator-Project`). திட்ட மேலோட்டப் பக்கத்தில் இருப்பதை உறுதி செய்யவும்.

1. Azure AI Service தாவலைப் பயன்படுத்தி **API Key** மற்றும் **Endpoint** ஐ கண்டறியவும்.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

இந்த இணைப்பு, இணைக்கப்பட்ட Azure AI சேவை வளத்தின் (படம் விசாரணை உட்பட) திறன்களை உங்கள் AI Foundry திட்டத்துக்கு கிடைக்கும் வகையில் செய்யும். இதன் பிறகு, உங்கள் நோட்டுபுக்களில் அல்லது பயன்பாடுகளில் படத்திலிருந்து உரையை பெற இந்த இணைப்பைப் பயன்படுத்தி, அதை பின்னர் மொழிபெயர்க்க Azure OpenAI மாதிரிக்கு அனுப்பலாம்.

## உங்கள் அங்கீகாரத் தகவல்களை ஒருங்கிணைத்தல்

 இதுவரை, நீங்கள் பின்வருவனவற்றை சேகரித்து இருக்க வேண்டும்:

**Azure OpenAI (உரை மொழிபெயர்ப்பு) க்கான:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (உதா., `gpt-4o`)
- Azure OpenAI Deployment Name (உதா., `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI சேவைகள் (Vision மூலம் பட உரை தேடும்) க்கான:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### எடுத்துக்காட்டு: சுற்றுப்புற மாறி கட்டமைப்பு (पूर्वावलோகம்)

பின்னர் உங்கள் பயன்பாட்டை உருவாக்கும் போது, இந்த சேகரிக்கப்பட்ட அங்கீகாரத் தகவல்களை சுற்றுப்புற மாறிகளாக அமைக்கும் வாய்ப்புள்ளது:

```bash
# Azure AI சேவைச் சான்றுகள் (படத் மொழிபெயர்ப்பிற்கு தேவையானவை)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # உதாரணமாக, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# விருப்பத் தத்ரூபச் செட்: _1/_2 என்ற இறுதியொட்டை கொண்ட நகல் மாறிலிகள் (அனைத்து மாறிலிகளுக்கும் ஒரே இடை)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI சான்றுகள் (எழுத்துத் மொழிபெயர்ப்பிற்கு தேவையானவை)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # உதாரணமாக, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # உதாரணமாக, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # உதாரணமாக, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # உதாரணமாக, 2024-12-01-preview

# விருப்பத் தத்ரூபச் செட்: முழு AZURE_OPENAI_* செட்டை _1/_2 இறுதியொட்டை கொண்டு நகலெடுக்கவும் (அனைத்து மாறிலிகளுக்கும் ஒரே இடை)
```

---

### மேலதிக வாசிப்பு

- [Azure AI Foundry இல் திட்டம் உருவாக்குவது எப்படி](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI வளங்களை உருவாக்குவது எப்படி](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry இல் OpenAI மாதிரிகளை அமர்த்துவது எப்படி](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**தயவு குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) எனும் AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டது. துல்லியத்திற்காக முயற்சி செய்தாலும், தானாக மொழிபெயர்ப்பு செய்யப்பட்டதில் பிழைகள் அல்லது தவறுகள் இருக்க வாய்ப்பு உள்ளது. அந்த ஆவணத்தின் அசல் மொழியில் உள்ளமைதையே அதிகாரப்பூர்வமான மூலமாக கருத வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்நுட்பமான மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்படுத்துவதால் ஏற்படும் தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் жауапளிக்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->