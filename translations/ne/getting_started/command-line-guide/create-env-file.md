# मूल फोल्डरमा *.env* फाइल सिर्जना गर्नुहोस्

यस ट्यूटोरियलमा, हामी तपाईंलाई Azure सेवाहरूको लागि वातावरण चरहरू सेटअप गर्ने तरिका देखाउनेछौं जुन *.env* फाइल प्रयोग गरेर गरिन्छ। वातावरण चरहरूले तपाईंलाई संवेदनशील प्रमाणपत्रहरू, जस्तो कि API कुञ्जीहरू, सुरक्षित रूपमा व्यवस्थापन गर्न अनुमति दिन्छ, जसलाई तपाईंको कोडबेसमा हार्ड-कोड नगरी।

> [!IMPORTANT]
> - केवल एउटा भाषा मोडल सेवा (Azure OpenAI वा OpenAI) कन्फिगर गर्न आवश्यक छ। तपाईंको मनपर्ने सेवाको लागि वातावरण चरहरू भर्नुहोस्। यदि धेरै भाषा मोडलहरूको वातावरण चरहरू सेट गरिएको छ भने, co-op translator ले प्राथमिकताका आधारमा एउटा चयन गर्नेछ।
> - यदि Computer Vision को वातावरण चरहरू सेट गरिएको छैन भने, translator 自动 रूपमा [Markdown-only mode](./markdown-only-mode.md) मा स्विच हुनेछ।

> [!NOTE]
> यो गाइड मुख्य रूपमा Azure सेवाहरूमा ध्यान केन्द्रित छ, तर तपाईं [supported models and services list](../README.md#-supported-models-and-services) बाट कुनै पनि समर्थित भाषा मोडल पनि चयन गर्न सक्नुहुन्छ।

## *.env* फाइल सिर्जना गर्नुहोस्

तपाईंको परियोजनाको मूल फोल्डरमा *.env* नामक फाइल सिर्जना गर्नुहोस्। यो फाइलले सबै वातावरण चरहरूलाई सरल स्वरूपमा भण्डारण गर्नेछ।

> [!WARNING]
> आफ्नो *.env* फाइललाई Git जस्ता संस्करण नियन्त्रण प्रणालीहरूमा कमिट नगर्नुहोस्। आकस्मिक कमिटबाट रोक्न *.env* लाई तपाईंको .gitignore फाइलमा थप्नुहोस्।

1. तपाईंको परियोजनाको मूल फोल्डरमा जानुहोस्।

1. परियोजनाको मूल फोल्डरमा *.env* फाइल सिर्जना गर्नुहोस्।

1. *.env* फाइल खोल्नुहोस् र तलको टेम्प्लेट पेस्ट गर्नुहोस्:

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
> यदि तपाईं आफ्नो API कुञ्जीहरू र endpoints फेला पार्न चाहनुहुन्छ भने, तपाईं [set-up-azure-ai.md](../set-up-azure-ai.md) लाई हेर्न सक्नुहुन्छ।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज [Co-op Translator](https://github.com/Azure/co-op-translator) को AI अनुवाद सेवा प्रयोग गरेर अनुवाद गरिएको हो। यद्यपि हामी शुद्धताका लागि प्रयास गर्छौं, कृपया सम्झनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। यसको मूल भाषा मा रहेको दस्तावेजलाई अधिकृत स्रोतको रूपमा लिनु पर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। हामी यस अनुवाद प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->