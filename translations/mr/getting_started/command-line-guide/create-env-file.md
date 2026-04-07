# रुट डिरेक्टरीमध्ये *.env* फाइल तयार करा

या ट्यूटोरियलमध्ये, आम्ही तुम्हाला *.env* फाइल वापरून Azure सेवांसाठी तुमच्या पर्यावरण चल (environment variables) सेट करण्यासाठी मार्गदर्शन करू. पर्यावरण चल तुम्हाला संवेदनशील क्रेडेन्शियल्स जसे की API कीज सुरक्षितपणे व्यवस्थापित करण्याची परवानगी देतात, ज्यामुळे तुम्हाला तुमच्या कोडबेसमध्ये त्यांना हार्ड-कोड करण्याची गरज नाही.

> [!IMPORTANT]
> - फक्त एका भाषा मॉडेल सेवेला (Azure OpenAI किंवा OpenAI) कॉन्फिगर करणे आवश्यक आहे. तुमच्या प्राधान्य सेवा साठी पर्यावरण चल भरा. जर अनेक भाषा मॉडेलसाठी पर्यावरण चल सेट केले गेले तर सह-ऑप भाषांतरक प्राधान्यानुसार एक निवडेल.
> - जर कंप्यूटर विजन पर्यावरण चल सेट नसतील, तर भाषांतरक आपोआप [Markdown-only मोड](./markdown-only-mode.md) वर स्विच करेल.

> [!NOTE]
> हा मार्गदर्शक मुख्यत्वे Azure सेवांवर लक्ष केंद्रित करतो, पण तुम्ही [supported models and services list](../README.md#-supported-models-and-services) मधील कोणतेही समर्थित भाषा मॉडेल निवडू शकता.

## *.env* फाइल तयार करा

तुमच्या प्रकल्पाच्या रुट डिरेक्टरीमध्ये, *.env* नावाची फाइल तयार करा. ही फाइल सर्व पर्यावरण चल एका सोप्या स्वरूपात साठवेल.

> [!WARNING]
> तुमची *.env* फाइल Git सारख्या आवृत्ती नियंत्रण प्रणालींमध्ये कमिट करू नका. आकस्मिक कमिट होण्यापासून टाळण्यासाठी *.env* तुमच्या .gitignore फाइलमध्ये जोडा.

1. तुमच्या प्रकल्पाच्या रुट डिरेक्टरीकडे जा.

1. प्रकल्पाच्या रुट डिरेक्टरीमध्ये *.env* फाइल तयार करा.

1. *.env* फाइल उघडा आणि पुढील साचा कॉपी करा:

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
> तुमच्या API कीज आणि एंडपॉइंट शोधण्यासाठी, तुम्ही [set-up-azure-ai.md](../set-up-azure-ai.md) या लेखाकडे पाहू शकता.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकारपूर्वक सूचना**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित केला आहे. जरी आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत समजावा. महत्त्वाची माहिती साठी व्यावसायिक मानवी अनुवादाची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवणाऱ्या कोणत्याही गैरसमजुतींसाठी किंवा गैरव्याख्यांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->