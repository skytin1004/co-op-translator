# रूट निर्देशिकेत *.env* फाइल तयार करा

या ट्यूटोरियलमध्ये, आम्ही तुम्हाला Azure सेवांसाठी तुमचे वातावरणीय चल सेट करण्याच्या प्रक्रियेत मार्गदर्शन करू. वातावरणीय चल तुम्हाला API की सारख्या संवेदनशील प्रमाणीकरणांची सुरक्षितपणे हाताळणी करण्याची परवानगी देतात, जे थेट कोडबेसमध्ये हार्ड-कोड न करता वापरले जातात.

> [!IMPORTANT]
> - फक्त एक भाषा मॉडेल सेवा (Azure OpenAI किंवा OpenAI) कॉन्फिगर करणे आवश्यक आहे. तुमच्या आवडत्या सेवेच्या वातावरणीय चलांची नोंद करा. जर अनेक भाषा मॉडेलसाठी वातावरणीय चल सेट केले असतील, तर को-ऑप ट्रान्सलेटर प्राधान्यक्रमानुसार एक निवडेल.
> - जर Computer Vision चे वातावरणीय चल सेट केलेले नसेल, तर ट्रान्सलेटर आपोआप [Markdown-only mode](./markdown-only-mode.md) मोडमध्ये बदलेल.

> [!NOTE]
> हा मार्गदर्शक प्रामुख्याने Azure सेवांवर लक्ष केंद्रित करतो, परंतु तुम्ही [supported models and services list](../README.md#-supported-models-and-services) मधून कुठलेही समर्थित भाषा मॉडेल निवडू शकता.

## *.env* फाइल तयार करा

तुमच्या प्रोजेक्टच्या रूट निर्देशिकेत *.env* नावाने एक फाइल तयार करा. ही फाइल तुमची सर्व वातावरणीय चल सोप्या स्वरूपात साठवेल.

> [!WARNING]
> तुमची *.env* फाइल Git सारख्या व्हर्शन कंट्रोल सिस्टममध्ये कमिट करू नका. अनपेक्षित कमिट पासून बचाव करण्यासाठी *.env* फाइलचा समावेश तुमच्या .gitignore फाइलमध्ये करा.

1. तुमच्या प्रोजेक्टच्या रूट निर्देशिकेत जा.

1. प्रोजेक्टच्या रूट निर्देशिकेत *.env* फाइल तयार करा.

1. *.env* फाइल उघडा आणि खालील टेम्प्लेट पेस्ट करा:

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
> जर तुम्हाला तुमच्या API की आणि एंडपॉइंट्स शोधायचे असतील, तर तुम्ही [set-up-azure-ai.md](../set-up-azure-ai.md) पहात राहू शकता.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सूचना**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारस केला जातो. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थसंग्रहणासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->