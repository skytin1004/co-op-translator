# Co-op Translator के लिए Azure AI सेट अप करें (Azure OpenAI और Azure AI Vision)

यह गाइड आपको Azure AI Foundry के भीतर भाषा अनुवाद के लिए Azure OpenAI और छवि सामग्री विश्लेषण के लिए Azure Computer Vision (जिसका उपयोग बाद में छवि-आधारित अनुवाद के लिए किया जा सकता है) सेट अप करने के लिए मार्गदर्शन करता है।

**पूर्व आवश्यकताएँ:**
- सक्रिय सब्सक्रिप्शन के साथ एक Azure खाता।
- आपके Azure सब्सक्रिप्शन में संसाधन और डिप्लॉयमेंट बनाने के लिए पर्याप्त अनुमतियाँ।

## एक Azure AI प्रोजेक्ट बनाएं

आप एक Azure AI प्रोजेक्ट बनाकर शुरू करेंगे, जो आपके AI संसाधनों का प्रबंधन करने के लिए एक केंद्रीय स्थान के रूप में कार्य करता है।

1. [https://ai.azure.com](https://ai.azure.com) पर जाएं और अपने Azure खाते से साइन इन करें।

1. नया प्रोजेक्ट बनाने के लिए **+Create** चुनें।

1. निम्नलिखित कार्य करें:
   - एक **Project name** दर्ज करें (जैसे, `CoopTranslator-Project`)।
   - **AI hub** चुनें (जैसे, `CoopTranslator-Hub`) (यदि आवश्यक हो तो नया बनाएं)।

1. अपने प्रोजेक्ट को सेट अप करने के लिए "**Review and Create**" पर क्लिक करें। आपको आपके प्रोजेक्ट के अवलोकन पृष्ठ पर ले जाया जाएगा।

## भाषा अनुवाद के लिए Azure OpenAI सेट अप करें

अपने प्रोजेक्ट के भीतर, आप टेक्स्ट अनुवाद के लिए बैकएंड के रूप में सेवा देने हेतु Azure OpenAI मॉडल डिप्लॉय करेंगे।

### अपने प्रोजेक्ट पर जाएं

यदि आप पहले से वहां नहीं हैं, तो अपने हाल ही में बनाए गए प्रोजेक्ट (जैसे `CoopTranslator-Project`) को Azure AI Foundry में खोलें।

### एक OpenAI मॉडल डिप्लॉय करें

1. अपने प्रोजेक्ट के बाएँ मेनू में, "My assets" के अंतर्गत, "**Models + endpoints**" चुनें।

1. **+ Deploy model** चुनें।

1. **Deploy Base Model** चुनें।

1. उपलब्ध मॉडलों की एक सूची प्रस्तुत की जाएगी। एक उपयुक्त GPT मॉडल के लिए फ़िल्टर करें या खोजें। हम `gpt-4o` की सिफारिश करते हैं।

1. अपनी पसंदीदा मॉडल चुनें और **Confirm** पर क्लिक करें।

1. **Deploy** चुनें।

### Azure OpenAI कॉन्फ़िगरेशन

एक बार डिप्लॉय हो जाने पर, आप "**Models + endpoints**" पृष्ठ से डिप्लॉयमेंट चुन सकते हैं ताकि उसका **REST endpoint URL**, **Key**, **Deployment name**, **Model name** और **API version** देखा जा सके। ये आपके एप्लिकेशन में अनुवाद मॉडल को इंटीग्रेट करने के लिए आवश्यक होंगे।

> [!NOTE]
> आप अपनी आवश्यकताओं के आधार पर [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) पृष्ठ से API संस्करण चुन सकते हैं। ध्यान दें कि **API version** Azure AI Foundry के **Models + endpoints** पृष्ठ पर दिखाए गए **Model version** से अलग है।

## छवि अनुवाद के लिए Azure Computer Vision सेट अप करें

छवियों के भीतर टेक्स्ट के अनुवाद को सक्षम करने के लिए, आपको Azure AI सेवा का API Key और Endpoint खोजना होगा।

1. अपने Azure AI प्रोजेक्ट (जैसे, `CoopTranslator-Project`) पर जाएं। सुनिश्चित करें कि आप प्रोजेक्ट अवलोकन पृष्ठ पर हैं।

### Azure AI सेवा कॉन्फ़िगरेशन

Azure AI सेवा से API Key और Endpoint खोजें।

1. अपने Azure AI प्रोजेक्ट (जैसे, `CoopTranslator-Project`) पर जाएं। सुनिश्चित करें कि आप प्रोजेक्ट अवलोकन पृष्ठ पर हैं।

1. Azure AI सेवा टैब से **API Key** और **Endpoint** खोजें।

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

यह कनेक्शन लिंक्ड Azure AI सेवाओं के संसाधन (जिसमें छवि विश्लेषण शामिल है) की क्षमताओं को आपके AI Foundry प्रोजेक्ट के लिए उपलब्ध बनाता है। आप इस कनेक्शन का उपयोग अपनी नोटबुक्स या एप्लिकेशन में छवियों से टेक्स्ट निकालने के लिए कर सकते हैं, जिसे बाद में अनुवाद के लिए Azure OpenAI मॉडल को भेजा जा सकता है।

## अपनी प्रमाण-पत्रों का समेकन

अब तक, आपको निम्नलिखित इकट्ठा कर लेना चाहिए:

**Azure OpenAI (टेक्स्ट अनुवाद) के लिए:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (जैसे, `gpt-4o`)
- Azure OpenAI Deployment Name (जैसे, `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI सेवाओं (दृष्टि के माध्यम से छवि टेक्स्ट निष्कर्षण) के लिए:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### उदाहरण: पर्यावरण चर कॉन्फ़िग्रेशन (पूर्वावलोकन)

बाद में, जब आप अपना एप्लिकेशन बनाएंगे, तो आप इन्हें शायद पर्यावरण चर के रूप में कॉन्फ़िगर करेंगे, जैसे:

```bash
# Azure AI सेवा क्रेडेंशियल्स (छवि अनुवाद के लिए आवश्यक)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # उदाहरण के लिए, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# वैकल्पिक फालबैक सेट: प्रत्यय _1/_2 के साथ डुप्लिकेट चर (सेट के सभी चर के लिए समान सूचकांक)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI क्रेडेंशियल्स (पाठ अनुवाद के लिए आवश्यक)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # उदाहरण के लिए, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # उदाहरण के लिए, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # उदाहरण के लिए, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # उदाहरण के लिए, 2024-12-01-preview

# वैकल्पिक फालबैक सेट: प्रत्यय _1/_2 के साथ पूर्ण AZURE_OPENAI_* सेट की नकल करें (सभी चर के लिए समान सूचकांक)
```

---

### आगे पढ़ें

- [Azure AI Foundry में प्रोजेक्ट कैसे बनाएं](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI संसाधन कैसे बनाएं](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry में OpenAI मॉडल कैसे डिप्लॉय करें](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल भाषा में मूल दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->