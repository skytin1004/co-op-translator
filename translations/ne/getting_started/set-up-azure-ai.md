# Co-op Translator का लागि Azure AI सेटअप गर्नुहोस् (Azure OpneAI र Azure AI Vision)

यस मार्गदर्शनले तपाईंलाई Azure AI Foundry भित्र भाषा अनुवादको लागि Azure OpenAI र छविमा आधारित अनुवादका लागि छवि सामग्री विश्लेषणका लागि Azure Computer Vision सेटअप गर्ने तरीका देखाउँछ।

**आवश्यकताहरू:**
- सक्रिय सदस्यता भएको Azure खाता।
- Azure सदस्यतामा स्रोत र तैनातीहरू सिर्जना गर्ने पर्याप्त अनुमतिहरू।

## Azure AI परियोजना सिर्जना गर्नुहोस्

तपाईंले Azure AI स्रोतहरू व्यवस्थापन गर्नको लागि केन्द्रिय स्थानको रूपमा Azure AI परियोजना सिर्जना गरेर सुरु गर्नुहुनेछ।

1. जानुहोस् [https://ai.azure.com](https://ai.azure.com) र आफ्नो Azure खातासँग साइन इन गर्नुहोस्।

1. नयाँ परियोजना सिर्जना गर्न **+Create** छनौट गर्नुहोस्।

1. तलका कार्यहरू गर्नुहोस्:
   - **Project name** प्रविष्टि गर्नुहोस् (जस्तै, `CoopTranslator-Project`)।
   - **AI hub** छान्नुहोस् (जस्तै, `CoopTranslator-Hub`) (आवश्यक परे नयाँ सिर्जना गर्नुहोस्)।

1. आफ्नो परियोजना सेटअप गर्न "**Review and Create**" क्लिक गर्नुहोस्। तपाईंलाई आफ्नो परियोजनाको अवलोकन पृष्ठमा लगिनेछ।

## भाषा अनुवादका लागि Azure OpenAI सेटअप गर्नुहोस्

तपाईंको परियोजनामा, तपाईंले पाठ अनुवादको ब्याकएन्डको रूपमा Azure OpenAI मोडेल तैनाथ गर्नु हुनेछ।

### आफ्नो परियोजनामा जानुहोस्

यदि पहिले गएको छैन भने, Azure AI Foundry मा आफ्नो नयाँ सिर्जना गरेको परियोजना (जस्तै, `CoopTranslator-Project`) खोल्नुहोस्।

### OpenAI मोडेल तैनाथ गर्नुहोस्

1. आफ्नो परियोजनाको बाँया मेनुबाट, "My assets" अन्तर्गत "**Models + endpoints**" चयन गर्नुहोस्।

1. **+ Deploy model** चयन गर्नुहोस्।

1. **Deploy Base Model** चयन गर्नुहोस्।

1. उपलब्ध मोडेलहरूको सूची देखाइनेछ। उपयुक्त GPT मोडेल खोज्नुहोस् अथवा फिल्टर गर्नुहोस्। हामी `gpt-4o` सिफारिस गर्छौं।

1. आफ्नो रोजेको मोडेल चयन गरी **Confirm** क्लिक गर्नुहोस्।

1. **Deploy** चयन गर्नुहोस्।

### Azure OpenAI कन्फिगरेसन

तैनाथ भएपछि, "**Models + endpoints**" पृष्ठबाट तैनाती चयन गरी यसको **REST endpoint URL**, **Key**, **Deployment name**, **Model name** र **API version** पत्ता लगाउन सक्नुहुन्छ। यी तपाईंको अनुप्रयोगमा अनुवाद मोडेल इंटीग्रेट गर्न आवश्यक पर्नेछन्।

> [!NOTE]
> तपाईं आफ्नो आवश्यकताअनुसार [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) पृष्ठबाट API संस्करणहरू छनौट गर्न सक्नुहुन्छ। ध्यान दिनुहोस् कि **API version** Azure AI Foundry को "**Models + endpoints**" पृष्ठमा देखाइने **Model version** भन्दा भिन्न हुन्छ।

## छवि अनुवादका लागि Azure Computer Vision सेटअप गर्नुहोस्

छविहरू भित्रको पाठ अनुवाद सक्षम गर्न, तपाईंले Azure AI Service को API Key र Endpoint खोज्न आवश्यक छ।

1. आफ्नो Azure AI परियोजनामा जानुहोस् (जस्तै, `CoopTranslator-Project`)। परियोजना अवलोकन पृष्ठमा हुनुहोस्।

### Azure AI Service कन्फिगरेसन

Azure AI Service बाट API Key र Endpoint खोज्नुहोस्।

1. आफ्नो Azure AI परियोजनामा जानुहोस् (जस्तै, `CoopTranslator-Project`)। परियोजना अवलोकन पृष्ठमा हुनुहोस्।

1. Azure AI Service ट्याबबाट **API Key** र **Endpoint** खोज्नुहोस्।

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

यस कनेक्शनले सम्बन्धित Azure AI Services स्रोत (छवि विश्लेषण सहित) को क्षमता तपाईंको AI Foundry परियोजनामा उपलब्ध गराउँछ। तपाईंले यो कनेक्शन आफ्ना नोटबुक वा अनुप्रयोगहरूमा प्रयोग गरी छविबाट पाठ निकाल्न सक्नुहुन्छ, जुन पछि अनुवादका लागि Azure OpenAI मोडेलमा पठाउन सकिन्छ।

## तपाईंका प्रमाणपत्रहरू एकीकृत गर्दै

अबसम्म तपाईंले यी संकलन गर्नुभयो:

**Azure OpenAI (पाठ अनुवाद) का लागि:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (जस्तै, `gpt-4o`)
- Azure OpenAI Deployment Name (जस्तै, `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (छवि पाठ निकाल्ने Vision मार्फत) का लागि:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### उदाहरण: वातावरण भेरिएबल कन्फिगरेसन (प्रिभ्यू)

पछि, जब तपाईं आफ्नो अनुप्रयोग बनाउनुहुन्छ, तपाईं सम्भवतः यी प्रमाणपत्रहरू वातावरण भेरिएबलको रूपमा कन्फिगर गर्नुहुनेछ। उदाहरणका लागि:

```bash
# Azure AI सेवा प्रमाणपत्रहरू (छवि अनुवादका लागि आवश्यक)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # जस्तै, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# वैकल्पिक फेलब्याक सेटहरू: उपसर्ग _1/_2 सहित दोहो¥याइएको भेरिएबलहरू (सेटका सबै भेरिएबलहरूको लागि उस्तै इन्डेक्स)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI प्रमाणपत्रहरू (पाठ अनुवादका लागि आवश्यक)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # जस्तै, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # जस्तै, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # जस्तै, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # जस्तै, 2024-12-01-preview

# वैकल्पिक फेलब्याक सेटहरू: उपसर्ग _1/_2 सहित पूर्ण AZURE_OPENAI_* सेट दोहो¥याउनुहोस् (सबै भेरिएबलहरूको लागि उस्तै इन्डेक्स)
```

---

### थप पढ्न

- [Azure AI Foundry मा परियोजना कसरी सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI स्रोतहरू कसरी सिर्जना गर्ने](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry मा OpenAI मोडेलहरू कसरी तैनाथ गर्ने](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो कागजात AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी सटीकताको प्रयास गर्छौं भनेपनि, कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्दछन्। मूल कागजात यसको स्थानीय भाषामा नै आधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानवीय अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी उत्तरदायी छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->