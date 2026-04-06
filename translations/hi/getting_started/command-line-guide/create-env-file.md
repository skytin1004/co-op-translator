# रूट डायरेक्टरी में *.env* फ़ाइल बनाएं

इस ट्यूटोरियल में, हम आपको Azure सेवाओं के लिए अपना वातावरण चर सेट करने के लिए मार्गदर्शन करेंगे, जिसमें एक *.env* फ़ाइल का उपयोग किया गया है। वातावरण चर आपको संवेदनशील क्रेडेंशियल, जैसे API कुंजियाँ, को सुरक्षित रूप से प्रबंधित करने की अनुमति देते हैं, बिना उन्हें अपने कोडबेस में हार्ड-कोड किए।

> [!IMPORTANT]
> - केवल एक भाषा मॉडल सेवा (Azure OpenAI या OpenAI) को कॉन्फ़िगर करना आवश्यक है। अपनी पसंदीदा सेवा के लिए वातावरण चर भरें। यदि कई भाषा मॉडलों के लिए वातावरण चर सेट किए गए हैं, तो को-ऑप ट्रांसलेटर प्राथमिकता के आधार पर एक चयन करेगा।
> - यदि कंप्यूटर विज़न के वातावरण चर सेट नहीं किए गए हैं, तो ट्रांसलेटर स्वचालित रूप से [Markdown-only mode](./markdown-only-mode.md) में स्विच कर देगा।

> [!NOTE]
> यह गाइड मुख्य रूप से Azure सेवाओं पर केंद्रित है, लेकिन आप [supported models and services list](../README.md#-supported-models-and-services) से किसी भी समर्थित भाषा मॉडल को चुन सकते हैं।

## *.env* फ़ाइल बनाएं

अपने प्रोजेक्ट की रूट डायरेक्टरी में, एक *.env* नाम की फ़ाइल बनाएं। इस फ़ाइल में आपके सभी वातावरण चर एक सरल प्रारूप में संग्रहित होंगे।

> [!WARNING]
> अपनी *.env* फ़ाइल को Git जैसे संस्करण नियंत्रण सिस्टम में कमिट न करें। आकस्मिक कमिट से बचने के लिए *.env* को अपनी .gitignore फ़ाइल में जोड़ें।

1. अपने प्रोजेक्ट की रूट डायरेक्टरी में जाएं।

1. अपने प्रोजेक्ट की रूट डायरेक्टरी में एक *.env* फ़ाइल बनाएं।

1. *.env* फ़ाइल खोलें और निम्न टेम्पलेट पेस्ट करें:

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
> यदि आप अपनी API कुंजियाँ और एंडपॉइंट ढूंढना चाहते हैं, तो आप [set-up-azure-ai.md](../set-up-azure-ai.md) को संदर्भित कर सकते हैं।

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियां या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->