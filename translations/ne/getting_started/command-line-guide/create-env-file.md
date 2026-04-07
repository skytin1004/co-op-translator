# मूल निर्देशिकामा *.env* फाइल सिर्जना गर्ने

यस ट्यूटोरियलमा, हामी तपाईंलाई Azure सेवाहरूको लागि वातावरण चरहरू सेटअप गर्ने तरिका देखाउनेछौं जुन *.env* फाइल प्रयोग गरेर गरिन्छ। वातावरण चरहरूले तपाईंलाई संवेदनशील प्रमाणपत्रहरू, जस्तै API कुञ्जीहरू, सुरक्षित रूपमा व्यवस्थापन गर्न अनुमति दिन्छन्, जसलाई तपाईंको कोडबेसमा हार्ड-कोड नगर्नुहोस्।

> [!IMPORTANT]
> - केवल एउटा भाषा मोडेल सेवा (Azure OpenAI वा OpenAI) कन्फिगर गर्न आवश्यक छ। तपाईंले आफ्नो प्राथमिक सेवाका लागि वातावरण चरहरू भर्नुहोस्। यदि धेरै भाषा मोडेलका लागि वातावरण चरहरू सेट गरिएका छन् भने, co-op translator प्राथमिकताको आधारमा एउटा छान्नेछ।
> - यदि कम्प्युटर भिजन वातावरण चरहरू सेट गरिएको छैन भने, अनुवादकले स्वतः [Markdown-केवल मोड](./markdown-only-mode.md) मा स्विच गर्नेछ।

> [!NOTE]
> यो मार्गनिर्देशन मुख्य रूपमा Azure सेवाहरूमा केन्द्रित छ, तर तपाईंले [समर्थित मोडेल र सेवाहरूको सूची](../README.md#-supported-models-and-services)बाट कुनै पनि समर्थित भाषा मोडेल छनोट गर्न सक्नुहुन्छ।

## *.env* फाइल सिर्जना गर्ने

तपाईंको प्रोजेक्टको मूल निर्देशिकामा, *.env* नामक फाइल सिर्जना गर्नुहोस्। यो फाइलले सबै वातावरण चरहरूलाई सरल फर्म्याटमा सङ्ग्रह गर्नेछ।

> [!WARNING]
> आफ्नो *.env* फाइललाई Git जस्ता भर्सन कन्ट्रोल प्रणालीमा कमिट नगर्नुहोस्। अप्रत्याशित कमिटहरू रोक्न *.env* लाई तपाईंको .gitignore फाइलमा थप्नुहोस्।

1. तपाईंको प्रोजेक्टको मूल निर्देशिकामा जानुहोस्।

1. मूल निर्देशिकामा *.env* फाइल सिर्जना गर्नुहोस्।

1. *.env* फाइल खोल्नुहोस् र तलको टेम्प्लेट टाँस्नुहोस्:

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
> यदि तपाईं आफ्नो API कुञ्जीहरू र अन्त बिन्दुहरू फेला पार्न चाहनुहुन्छ भने, तपाईं [set-up-azure-ai.md](../set-up-azure-ai.md) सन्दर्भ गर्न सक्नुहुन्छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। यद्यपि हामी शुद्धताको लागि प्रयास गर्दछौं, कृपया जान्नुस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्दछन्। मूल दस्तावेज यसको मूल भाषामा प्रामाणिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट कुनै गलतफहमी वा मिसअर्थिङ्गका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->