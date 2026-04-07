# రూట్ డైరెక్టరీలో *.env* ఫైల్ సృష్టించండి

ఈ ట్యుటోరియల్‌లో, Azure సేవల కోసం మీ వాతావరణ వేరియబుల్స్ సెట్ చేయడంలో നിങ്ങల్ని గైడ్ చేస్తాము, ఇది *.env* ఫైల్ ఉపయోగిస్తుంది. వాతావరణ వేరియబుల్స్ సెన్సిటివ్ క్రెడెన్షియల్స్, ఏపీఐ కీలు వంటివి, మీ కోడ్‌బేస్‌లో హార్డ్-కోడ్ చేయకుండా సురక్షితంగా నిర్వహించడానికి అనుమతిస్తాయి.

> [!IMPORTANT]
> - ఒక్క భాషా మోడల్ సేవ (Azure OpenAI లేదా OpenAI) మాత్రమే కాన్ఫిగర్ చేయాల్సినది. మీ ఇష్టమైన సేవ కోసం వాతావరణ వేరియబుల్స్ పూరించండి. బహుళ భాషా మోడల్స్ కోసం వాతావరణ వేరియబుల్స్ సెట్ చేయడమై ఉంటే, కో-ఆప్ ట్రాన్స్లేటర్ ప్రాధాన్యత ఆధారంగా ఒకదాన్ని ఎంచుకుంటుంది.
> - కంప్యూటర్ విజన్ వాతావరణ వేరియబుల్స్ సెట్ చేయకపోతే, ట్రాన్స్లేటర్ స్వయంచాలకంగా [Markdown-only mode](./markdown-only-mode.md)కి మారుతుంది.

> [!NOTE]
> ఈ గైడ్ ప్రధానంగా Azure సేవల పై దృష్టి సారిస్తుంది, కానీ మీరు [supported models and services list](../README.md#-supported-models-and-services) నుండి మద్దతు పొందిన ఎలాంటి భాషా మోడల్‌ను ఎంచుకోవచ్చు.

## *.env* ఫైల్ సృష్టించండి

మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీలో *.env* అనే ఫైల్ సృష్టించండి. ఈ ఫైల్ మీ వాతావరణ వేరియబుల్స్ సులభమైన ఫార్మాట్‌లో నిల్వ చేస్తుంది.

> [!WARNING]
> *.env* ఫైల్‌ను Git వంటి వెర్షన్ కంట్రోల్ సిస్టమ్స్‌కి కమిట్ చేయవద్దు. అపరాధ కమిట్లను నివారించేలా *.env* ను .gitignore ఫైల్‌లో జోడించండి.

1. మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీకి వెళ్ళండి.

1. మీ ప్రాజెక్ట్ యొక్క రూట్ డైరెక్టరీలో *.env* ఫైల్ సృష్టించండి.

1. *.env* ఫైల్‌ను తెరవండి మరియు క్రింది టెంప్లేట్‌ని పేస్ట్ చేయండి:

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
> మీ API కీలు మరియు ఎండ్పాయింట్‌లు కనుగొనదలచినట్లయితే, మీరు [set-up-azure-ai.md](../set-up-azure-ai.md)ని పరిశీలించవచ్చు.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**డిస్‌క్లైమర్**:  
ఈ డాక్యుమెంట్ [Co-op Translator](https://github.com/Azure/co-op-translator) అనే AI అనువాద సేవను ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి శ్రద్ధ వహించినప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా పొరపాట్లు ఉండవచ్చు гэమనని దయచేసి గమనించండి. మూల డాక్యుమెంట్ native భాషలోనే ప్రామాణిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదం చేయించుకోవడం మంచిది. ఈ అనువాదం ఉపయోగంలో జరిగే ఏవైనా అపార్థాల లేదా తప్పు అర్థాల కోసం మేము బాధ్యులు కాకపోవడం స것.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->