# Co-op Translator साठी Azure AI सेट अप करा (Azure OpenAI आणि Azure AI Vision)

हा मार्गदर्शक तुम्हाला Azure AI Foundry मध्ये भाषांतरासाठी Azure OpenAI आणि प्रतिमा-आधारित भाषांतरासाठी प्रतिमा सामग्री विश्लेषणासाठी Azure Computer Vision कसे सेट करायचे हे दाखवतो.

**आवश्यक अटी:**
- सक्रिय सदस्यत्व असलेले Azure खाते.
- तुमच्या Azure सदस्यत्वामध्ये संसाधने आणि तैनाती तयार करण्याचे पुरेसे परवानगी.

## Azure AI प्रोजेक्ट तयार करा

तुम्ही Azure AI प्रोजेक्ट तयार करून सुरू कराल, जे तुमच्या AI संसाधनांचे व्यवस्थापन करण्यासाठी केंद्रस्थानी कार्य करते.

1. [https://ai.azure.com](https://ai.azure.com) वर जा आणि तुमच्या Azure खात्याने साइन इन करा.

1. नवीन प्रोजेक्ट तयार करण्यासाठी **+Create** निवडा.

1. पुढील कार्ये करा:
   - **Project name** टाका (उदा., `CoopTranslator-Project`).
   - **AI hub** निवडा (उदा., `CoopTranslator-Hub`) (आवश्यक असल्यास नवीन तयार करा).

1. तुमचा प्रोजेक्ट सेट अप करण्यासाठी "**Review and Create**" वर क्लिक करा. तुम्हाला तुमच्या प्रोजेक्टच्या आढावा पृष्ठावर नेले जाईल.

## भाषांतरासाठी Azure OpenAI सेट अप करा

तुमच्या प्रोजेक्टमध्ये, तुम्ही मजकूर भाषांतरासाठी बॅकएंड म्हणून कार्य करेल अशा Azure OpenAI मॉडेलची तैनात कराल.

### तुमच्या प्रोजेक्टवर जा

जर आधीच अस्तित्त्वात नसेल तर, तुमचा नव्याने तयार केलेला प्रोजेक्ट (उदा., `CoopTranslator-Project`) Azure AI Foundry मध्ये उघडा.

### OpenAI मॉडेल तैनात करा

1. तुमच्या प्रोजेक्टच्या डाव्या मेनूमध्ये, "My assets" अंतर्गत, "**Models + endpoints**" निवडा.

1. **+ Deploy model** निवडा.

1. **Deploy Base Model** निवडा.

1. उपलब्ध मॉडेल्सची यादी तुम्हाला दाखवली जाईल. योग्य GPT मॉडेल शोधा किंवा फिल्टर करा. आम्ही `gpt-4o` शिफारस करतो.

1. इच्छित मॉडेल निवडा आणि **Confirm** वर क्लिक करा.

1. **Deploy** निवडा.

### Azure OpenAI कॉन्फिगरेशन

तैनात केल्यावर, तुम्ही "**Models + endpoints**" पृष्ठावर तैनाती निवडून त्याचा **REST endpoint URL**, **Key**, **Deployment name**, **Model name** आणि **API version** पाहू शकता. हे भाषांतर मॉडेलचे एकत्रीकरण करण्यासाठी गरजेचे असतील.

> [!NOTE]
> तुम्ही तुमच्या गरजेनुसार [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) पृष्ठावरून API आवृत्त्या निवडू शकता. लक्षात ठेवा की **API version** हे Azure AI Foundry मधील "**Models + endpoints**" पृष्ठावर दर्शविलेल्या **Model version** पेक्षा भिन्न आहे.

## प्रतिमा भाषांतरासाठी Azure Computer Vision सेट अप करा

प्रतिमांमधील मजकूराचे भाषांतर सक्षम करण्यासाठी, तुम्हाला Azure AI सेवा API Key आणि Endpoint शोधायचे आहे.

1. तुमच्या Azure AI प्रोजेक्टवर जा (उदा., `CoopTranslator-Project`). प्रोजेक्टच्या आढावा पृष्ठावर असण्याची खात्री करा.

### Azure AI सेवा कॉन्फिगरेशन

Azure AI सेवेतून API Key आणि Endpoint शोधा.

1. तुमच्या Azure AI प्रोजेक्टवर जा (उदा., `CoopTranslator-Project`). प्रोजेक्टच्या आढावा पृष्ठावर असण्याची खात्री करा.

1. Azure AI सेवा टॅबमधून **API Key** आणि **Endpoint** शोधा.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ही कनेक्शन लिंक केलेल्या Azure AI सेवा संसाधनाच्या क्षमता (प्रतिमा विश्लेषणासहित) तुमच्या AI Foundry प्रोजेक्टसाठी उपलब्ध करून देते. तुम्ही नंतर या कनेक्शनचा वापर तुमच्या नोटबुक्स किंवा अनुप्रयोगांमध्ये करून प्रतिमांमधून मजकूर काढू शकता, जो नंतर भाषांतरासाठी Azure OpenAI मॉडेलकडे पाठवता येईल.

## तुमचे क्रेडेन्शियल्स एकत्रित करणे

आता पर्यंत, तुम्ही खालील गोष्टी एकत्र केल्या असाव्यात:

**Azure OpenAI (मजकूर भाषांतरासाठी):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI मॉडेल नाव (उदा., `gpt-4o`)
- Azure OpenAI तैनातीचे नाव (उदा., `cooptranslator-gpt4o`)
- Azure OpenAI API आवृत्ती

**Azure AI सेवा (Vision द्वारे प्रतिमा मजकूर काढणे):**
- Azure AI सेवा Endpoint
- Azure AI सेवा API Key

### उदाहरण: पर्यावरण चल कॉन्फिगरेशन (पूर्वावलोकन)

नंतर, तुमचा अनुप्रयोग तयार करताना तुम्ही या संकलित क्रेडेन्शियल्सचा वापर पर्यावरण चल म्हणून सेट करू शकता.

```bash
# Azure AI सेवा क्रेडेंशियल्स (प्रतिमा भाषांतरासाठी आवश्यक)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # उदा., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# पर्यायी फॉलबॅक सेट: _1/_2 उपसर्गासह पुनरावृत्ती वेरिएबल्स (सर्व वेरिएबल्ससाठी समान अनुक्रमणिका)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI क्रेडेंशियल्स (टेक्स्ट भाषांतरासाठी आवश्यक)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # उदा., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # उदा., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # उदा., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # उदा., 2024-12-01-preview

# पर्यायी फॉलबॅक सेट: संपूर्ण AZURE_OPENAI_* सेटची पुनरावृत्ती _1/_2 उपसर्गासह (सर्व वेरिएबल्ससाठी समान अनुक्रमणिका)
```

---

### पुढील वाचन

- [Azure AI Foundry मध्ये प्रोजेक्ट कसे तयार करावे](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI संसाधने कशी तयार करावीत](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry मध्ये OpenAI मॉडेल तैनात कसे करावे](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असूनही, कृपया ध्यानात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकता नसलेली माहिती असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाची माहिती बाबत व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाचा वापर केल्यामुळे होणाऱ्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थाने घेतल्याबद्दल आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->