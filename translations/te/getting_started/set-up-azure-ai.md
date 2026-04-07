# Co-op Translator కోసం Azure AI సెటప్ చేయడం (Azure OpneAI & Azure AI Vision)

ఈ గైడ్ Azure AI Foundry లో భాషా అనువాదానికి Azure OpenAI మరియు చిత్రం ఆధారిత అనువాదానికి ఉపయోగించే Azure Computer Vision ని సెటప్ చేసే విధానాన్ని మీకు చూపిస్తుంది.

**అవసరాలు:**
- సక్రియమైన సబ్‌స్క్రిప్షన్ ఉన్న Azure ఖాతా.
- మీ Azure సబ్‌స్క్రిప్షన్ లో రిసోర్సులు మరియు డిప్లాయ్‌మెంట్‌లు సృష్టించేందుకు సరిపడిన అనుమతులు.

## Azure AI ప్రాజెక్ట్ క్రియేట్ చేయండి

మీ AI రిసోర్సులను నిర్వహించడానికి కేంద్రంగా పనిచేసే Azure AI ప్రాజెక్ట్ సృష్టించడం మీ ప్రారంభము.

1. [https://ai.azure.com](https://ai.azure.com) కి వెళ్లి మీ Azure ఖాతాతో సైన్ ఇన్ అవ్వండి.

1. కొత్త ప్రాజెక్ట్ సృష్టించడానికి **+Create** ఎంచుకోండి.

1. క్రింది కార్యాలు చేయండి:
   - **Project name** ను నమోదు చేయండి (ఉదా: `CoopTranslator-Project`).
   - **AI hub** ను ఎంచుకోండి (ఉదా: `CoopTranslator-Hub`) (అవసరమైతే కొత్తది సృష్టించండి).

1. మీ ప్రాజెక్ట్ సెట్ అప్ చేయడానికి "**Review and Create**" పై క్లిక్ చేయండి. మీరు మీ ప్రాజెక్ట్ అవలోకన పేజీకి తీసుకెళ్లబడతారు.

## భాషా అనువాదానికి Azure OpenAI సెటప్ చేయండి

మీ ప్రాజెక్ట్ లో, టెక్స్ అనువాదానికి బ్యాక్‌ఎండ్ గా పనిచేసే Azure OpenAI మోడల్ ను మీరు డిప్లాయ్ చేస్తారు.

### మీ ప్రాజెక్ట్ కి వెళ్లండి

ఇప్పటికే లేనే కాకపోతే, మీ సృష్టించిన ప్రాజెక్ట్ (ఉదా: `CoopTranslator-Project`) ను Azure AI Foundry లో తెరవండి.

### OpenAI మోడల్ ను డిప్లాయ్ చేయండి

1. మీ ప్రాజెక్ట్ యొక్క ఎడమ మెనులో "My assets" కింద "**Models + endpoints**" ఎంచుకోండి.

1. **+ Deploy model** ఎంచుకోండి.

1. **Deploy Base Model** ఎంచుకోండి.

1. అందుబాటులో ఉన్న మోడల్స్ జాబితా మీరు చూస్తారు. సరైన GPT మోడల్ కోసం ఫిల్టర్ చేసి లేదా సెర్చ్ చేయండి. మా సిఫార్సు `gpt-4o`.

1. మీ ఇష్టమైన మోడల్ ఎంచుకుని **Confirm** పై క్లిక్ చేయండి.

1. **Deploy** ఎంచుకోండి.

### Azure OpenAI కంఫిగరేషన్

డిప్లాయ్ అయిన తరువాత, మీరు "**Models + endpoints**" పేజీ నుండి డిప్లాయ్‌మెంట్‌ని ఎంచుకుని దాని **REST endpoint URL** , **Key**, **Deployment name**, **Model name** మరియు **API version** వివరాలను పొందవచ్చు. ఈ వివరాలు అనువాద మోడల్ ను మీ అప్లికేషన్ లో అనుసంధానించడానికి అవసరం అవుతాయి.

> [!NOTE]
> మీ అవసరాల ప్రకారం [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) పేజీ నుండి API వెర్షన్లు ఎంపిక చేసుకోవచ్చు. గమనించండి, **API version** అనేది Azure AI Foundry లోని **Models + endpoints** పేజీలో చూపించిన **Model version** కంటే వేరుగా ఉంటుంది.

## చిత్రం అనువాదానికి Azure Computer Vision సెటప్ చేయండి

చిత్రాలలో ఉన్న టెక్స్‍ట్ అనువాదం కోసం, మీరు Azure AI Service API Key మరియు Endpoint ని కనుగొనాల్సి ఉంటుంది.

1. మీ Azure AI ప్రాజెక్ట్ (ఉదా: `CoopTranslator-Project`) కి వెళ్లండి. ప్రాజెక్ట్ అవలోకన పేజీలో ఉండడం నిర్ధారించుకోండి.

### Azure AI Service కంఫిగరేషన్

Azure AI Service నుండి API Key మరియు Endpoint ని కనుగొనండి.

1. మీ Azure AI ప్రాజెక్ట్ (ఉదా: `CoopTranslator-Project`) కి వెళ్లండి. ప్రాజెక్ట్ అవలోకన పేజీలో ఉండండి.

1. Azure AI Service ట్యాబ్ నుండి **API Key** మరియు **Endpoint** ని కనుగొనండి.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ఈ కనెక్షన్ లింక్ అయిన Azure AI Services రిసోర్సు (చిత్ర విశ్లేషణ కలుపుకుని) సామర్థ్యాలను మీ AI Foundry ప్రాజెక్ట్ కు అందుబాటులో ఉంచుతుంది. అనంతరం మీరు ఈ కనెక్షన్ ని మీ నోట్బుక్స్ లేదా అప్లికేషన్లలో ఉపయోగించి చిత్రాల నుంచి టెక్స్‍ట్ తీసి Azure OpenAI మోడల్ కు అనువాదం కోసం పంపవచ్చు.

## మీ సర్టిఫికెట్లు కాంసాలిడేట్ చేయడం

ఈ దాకా, మీరు క్రిందివి సేకరించారనుకుంటున్నాము:

**Azure OpenAI కోసం (టెక్స్ట్ అనువాదం):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ఉదా: `gpt-4o`)
- Azure OpenAI Deployment Name (ఉదా: `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services కోసం (దృష్టి ద్వారా చిత్రం టెక్స్‍ట్ ఎక్స్‌ట్రాక్షన్):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ఉదాహరణ: ఎన్‌విరాన్‌మెంట్ వేరియబుల్ కంఫిగరేషన్ (ప్రివ్యూ)

ఆప్లికేషన్ నిర్మాణ సమయంలో, మీరు ఈ సేకరించిన సర్టిఫికెట్లను ఉపయోగించి అనేక సార్లు ఎన్‌విరాన్‌మెంట్ వేరియబుల్స్ గా సెట్ చేస్తారు.

```bash
# Azure AI సేవా ప్రమాణపత్రాలు (చిత్ర అనువాదానికి అవసరం)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ఉదా., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ఐచ్ఛిక ప్రత్యామ్నాయ సెట్‌లు: సఫిక్స్ _1/_2 తో డూప్లికేట్ వేరియబుల్స్ (సెట్‌లోని అన్ని వేరియబుల్స్‌కు అదే సూచిక)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI ప్రమాణపత్రాలు (పాఠ్య అనువాదానికి అవసరం)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ఉదా., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ఉదా., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ఉదా., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ఉదా., 2024-12-01-preview

# ఐచ్ఛిక ప్రత్యామ్నాయ సెట్‌లు: సఫిక్స్ _1/_2 తో పూర్తి AZURE_OPENAI_* సెట్‌ను నకలు చేయండి (అన్ని వేరియబుల్స్‌కు అదే సూచిక)
```

---

### మరిన్ని చదవండి

- [Azure AI Foundry లో ప్రాజెక్ట్ సృష్టించడం](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI రిసోర్సులు సృష్టించడం](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry లో OpenAI మోడల్స్ ని డిప్లాయ్ చేయడం](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అసాధారణ సమాచారం**:  
ఈ డాక్యుమెంట్ AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడినది. మనం ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటిక్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు. మౌలిక భావాన్ని అర్థం చేసుకోవడానికి, దేశీయ భాషలోని అసలు డాక్యుమెంట్ నమ్మకమైన మూలంగా భావించాలి. ముఖ్యమైన సమాచారానికి, నిపుణుల చేతి అనువాదాన్ని సూచించబడుతుంది. ఈ అనువాదం వాడుకలో ఏర్పడే ఏదైనా తప్పుగా అర్థం చేసుకోవడంవల్ల కలిగే బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->