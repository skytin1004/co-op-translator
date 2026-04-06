# రూట్ డైరెక్టరీలో *.env* ఫైల్ సృష్టించండి

ఈ ట్యుటోరియల్‌లో, Azure సేవల కోసం మీ ఎన్‌విరాన్‌మెంట్ వేరియబుల్‌లను *.env* ఫైల్ ఉపయోగించి సెటప్ చేయడం గూర్చి మేము మీకు మార్గనిర్దేశనం చేస్తాము. ఎన్‌విరాన్‌మెంట్ వేరియబుల్‌లు మీ కోడ్‌బేస్‌లో హార్డ్‌కోడ్ చేయకుండా సురక్షితమైన వివరాలు, ఉదాహరణకు API కీలను నిర్వహించడానికి అవకాశం ఇస్తాయి.

> [!IMPORTANT]
> - ఒక్క భాషా మోడల్ సేవ (Azure OpenAI లేదా OpenAI) మాత్రమే కాన్ఫిగర్ చేయాలి. మీరు ప్రాధాన్యతనిచ్చే సేవ కోసం ఎన్‌విరాన్‌మెంట్ వేరియబుల్‌లను పూరించండి. బహుళ భాషా మోడల్స్ కోసం వేరియబుల్‌లు సెట్ అయితే, co-op translator ప్రాధాన్యత ఆధారంగా ఒకదాన్ని ఎంచుకుంటుంది.
> - Computer Vision ఎన్‌విరాన్‌మెంట్ వేరియబుల్‌లు సెట్ కాని పక్షంలో, అనువాదకుడు ఆటోమేటిక్‌గా [Markdown-only mode](./markdown-only-mode.md) కు మారుతుంది.

> [!NOTE]
> ఈ గైడ్ ప్రధానంగా Azure సేవలపై దృష్టి సారిస్తుంది, కాని మీరు [supported models and services list](../README.md#-supported-models-and-services) నుండి ఏదైనా మద్దతు ఉన్న భాషా మోడల్‌ని ఎంచుకోవచ్చు.

## *.env* ఫైల్ సృష్టించండి

మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీలో *.env* అనే ఫైల్‌ని సృష్టించండి. ఈ ఫైల్ మీ అన్ని ఎన్‌వరాన్‌మెంట్ వేరియబుల్‌లను సరళమైన ఫార్మాట్‌లో నిల్వ చేస్తుంది.

> [!WARNING]
> *.env* ఫైల్‌ను Git వంటి వెర్షన్ కంట్రోల్ సిస్టమ్స్‌కు కమిట్ చేయొద్దు. అనుకోని కమిట్‌లను నివారించడానికి *.env* ను మీ .gitignore ఫైల్‌లో చేర్చండి.

1. మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీకి వెళ్ళండి.

1. రూట్ డైరెక్టరీలో ఒక *.env* ఫైల్ సృష్టించండి.

1. *.env* ఫైల్‌ను తెరిచి, క్రింది టెంప్లేట్‌ను పేస్ట్ చేయండి:

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
> మీ API కీలను మరియు ఎండ్‌పాయింట్లను కనుగొనాలనుకుంటే, మీరు [set-up-azure-ai.md](../set-up-azure-ai.md) గైడ్‌ని చూడవచ్చు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్ AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో పొరపాట్లు లేదా అప_STEPె ప్రధానతలు ఉండవచ్చు. మౌలిక భాషలో ఉన్న అసలు డాక్యుమెంట్‌ను అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి నిపుణుల చేత మానవ అనువాదం సిఫార్సు చేయబడింది. ఈ అనువాదాన్ని ఉపయోగించడంలో వచ్చిన ఏవైనా అపార్థాలు లేదా తప్పు వ్యాఖ్యానాలకు మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->