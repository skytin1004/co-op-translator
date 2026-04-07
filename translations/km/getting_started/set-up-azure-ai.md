# កំណត់ Azure AI សម្រាប់ Co-op Translator (Azure OpneAI & Azure AI Vision)

មគ្គុទេសក៍នេះនាំអ្នកឆ្លងកាត់ការកំណត់ Azure OpenAI សម្រាប់ការប្រែភាសា និង Azure Computer Vision សម្រាប់វិភាគមាតិការូបភាព (ដែលអាចប្រើសម្រាប់ការប្រែប្រួលដោយផ្អែកលើរូបភាព) នៅក្នុង Azure AI Foundry។

**តម្រូវការមុន:**
- គណនី Azure ជាមួយការជាវសកម្ម។
- សិទ្ធិគ្រប់គ្រាន់ក្នុងការបង្កើតធនធាន និងការចែកចាយក្នុងការជាវ Azure របស់អ្នក។

## បង្កើតគម្រោង Azure AI

អ្នកនឹងចាប់ផ្តើមដោយបង្កើតគម្រោង Azure AI ដែលធ្វើតួនាទីជាទីតាំងកណ្តាលសម្រាប់គ្រប់គ្រងធនធាន AI របស់អ្នក។

1. ទៅកាន់ [https://ai.azure.com](https://ai.azure.com) ហើយចូលដោយគណនី Azure របស់អ្នក។

1. ជ្រើសរើស **+Create** ដើម្បីបង្កើតគម្រោងថ្មី។

1. អនុវត្តតួនាទីខាងក្រោម:
   - បញ្ចូល **Project name** (ឧ. `CoopTranslator-Project`)។
   - ជ្រើសរើស **AI hub**  (ឧ. `CoopTranslator-Hub`) (បង្កើតថ្មីប្រសិនបើចាំបាច់)។

1. ចុច "**Review and Create**" ដើម្បីតាំងពាណិជ្ជកម្មគម្រោងរបស់អ្នក។ អ្នកនឹងត្រូវបានយកទៅទំព័រពិពណ៌នាគម្រោងរបស់អ្នក។

## កំណត់ Azure OpenAI សម្រាប់ការប្រែភាសា

នៅក្នុងគម្រោងរបស់អ្នក អ្នកនឹងចេញផ្សាយម៉ូដែល Azure OpenAI ដើម្បីដំណើរការជាក្រោយការប្រែអត្ថបទ។

### ទៅកាន់គម្រោងរបស់អ្នក

ប្រសិនបើមិនទាន់មាន នៅពេលនេះ បើកគម្រោងថ្មីដែលបានបង្កើត (ឧ. `CoopTranslator-Project`) ក្នុង Azure AI Foundry។

### ចេញផ្សាយម៉ូដែល OpenAI

1. ពីម៉ឺនុយខាងឆ្វេងគម្រោង អ្នកនៅក្រោម "My assets" ជ្រើសរើស "**Models + endpoints**"។

1. ជ្រើសរើស **+ Deploy model**។

1. ជ្រើសរើស **Deploy Base Model**។

1. អ្នកនឹងបានបង្ហាញជាចំណងជញ្ជាំងម៉ូដែលដែលអាចប្រើបាន។ ស្រោចស្រង់ ឬ ស្វែងរកម៉ូដែល GPT សមរម្យ។ យើងផ្តល់អនុសាសន៍ `gpt-4o`។

1. ជ្រើសរើសម៉ូដែលដែលអ្នកចង់បាន ហើយចុច **Confirm**។

1. ជ្រើសរើស **Deploy**។

### កំណត់រចនាសម្ព័ន្ធ Azure OpenAI

បន្ទាប់ពីបានចេញផ្សាយ អ្នកអាចជ្រើសរើសការចេញផ្សាយពីទំព័រ "**Models + endpoints**" ដើម្បីរក **REST endpoint URL**, **Key**, **Deployment name**, **Model name** និង **API version** ។ អ្នកនឹងត្រូវការព័ត៌មានទាំងនេះសម្រាប់ការរួមបញ្ចូលម៉ូដែលប្រែភាសាចូលទៅកម្មវិធីរបស់អ្នក។

> [!NOTE]
> អ្នកអាចជ្រើសរើសកំណែ API ពីទំព័រ [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ដោយផ្អែកលើតម្រូវការរបស់អ្នក។ សូមចងចាំថា **API version** ខុសគ្នាពី **Model version** ដែលបង្ហាញនៅលើទំព័រ **Models + endpoints** ក្នុង Azure AI Foundry។

## កំណត់ Azure Computer Vision សម្រាប់ការប្រែរូបភាព

ដើម្បីអនុញ្ញាតការប្រែអត្ថបទនៅក្នុងរូបភាព អ្នកត្រូវរក Key API និង Endpoint របស់ Azure AI Service។

1. ទៅកាន់គម្រោង Azure AI របស់អ្នក (ឧ. `CoopTranslator-Project`)។ ដូច្នេះ សូមប្រាកដថាអ្នកនៅលើទំព័រពិពណ៌នាគម្រោង។

### កំណត់រចនាសម្ព័ន្ធ Azure AI Service

ស្វែងរក Key API នឹង Endpoint ពី Azure AI Service។

1. ទៅកាន់គម្រោង Azure AI របស់អ្នក (ឧ. `CoopTranslator-Project`)។ ប្រាកដថាអ្នកនៅលើទំព័រពិពណ៌នាគម្រោង។

1. ស្វែងរក **API Key** និង **Endpoint** ពីផ្ទាំង Azure AI Service។

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ការតភ្ជាប់នេះធ្វើឲ្យមុខងាររបស់ធនធាន Azure AI Services ដែលបានភ្ជាប់ (រួមទាំងវិភាគរូបភាព) មានភាពអាចប្រើបានក្នុងគម្រោង AI Foundry របស់អ្នក។ បន្ទាប់មក អ្នកអាចប្រើការតភ្ជាប់នេះក្នុងកំណត់ត្រា ឬកម្មវិធីរបស់អ្នក ដើម្បីចេញអត្ថបទពីរូបភាព ដែលបន្ទាប់មកអាចផ្ញើទៅម៉ូដែល Azure OpenAI សម្រាប់ការប្រើប្រែភាសា។

## សម្រួលព័ត៌មានសម្គាល់របស់អ្នក

ឥឡូវនេះ អ្នកគួរតែបានប្រមូលព័ត៌មានដូចខាងក្រោម៖

**សម្រាប់ Azure OpenAI (ការប្រែអត្ថបទ):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ឧ. `gpt-4o`)
- Azure OpenAI Deployment Name (ឧ. `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**សម្រាប់ Azure AI Services (ការដកអត្ថបទពីរូបភាពតាមរយៈ Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ឧទាហរណ៍៖ កំណត់បរិញ្ញាបថបរិស្ថាន (មើលជាមុន)

នៅពេលក្រោយ ពេលដែលអ្នកកំពុងបង្កើតកម្មវិធីរបស់អ្នក អ្នកប្រហែលជានឹងកំណត់វាដោយប្រើព័ត៌មានសម្គាល់ដែលបានប្រមូល។ ឧទាហរណ៍ អ្នកអាចកំណត់ជាបរិញ្ញាបថបរិស្ថាន ដូចខាងក្រោម៖

```bash
# អ៊ីឌីអេនសម្រាប់សេវា Azure AI (ចាំបាច់សម្រាប់ការបំលែងរូបភាព)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ឧទាហរណ៍ 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ការដាក់ជំនួសជាជម្រើស៖ បង្កើនអថេរដដែលជាប់ដោយពាក្យបញ្ចប់ _1/_2 (លេខវិស័យដូចគ្នាសម្រាប់អថេរទាំងអស់នៅក្នុងកំណត់)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# អ៊ីឌីអេនសម្រាប់ Azure OpenAI (ចាំបាច់សម្រាប់ការបំលែងអត្ថបទ)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ឧទាហរណ៍ 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ឧទាហរណ៍ gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ឧទាហរណ៍ cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ឧទាហរណ៍ 2024-12-01-preview

# ការដាក់ជំនួសជាជម្រើស៖ បង្កើនជុំវិញចំណុច AZURE_OPENAI_* ពេញលេញជាមួយពាក្យបញ្ចប់ _1/_2 (លេខវិស័យដូចគ្នាសម្រាប់អថេរទាំងអស់)
```

---

### អានបន្ថែម

- [របៀបបង្កើតគម្រោងក្នុង Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [របៀបបង្កើតធនធាន Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [របៀបចេញផ្សាយម៉ូដែល OpenAI ក្នុង Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការផ្តល់ការព្រមាន**៖  
ឯកសារនេះត្រូវបានបកប្រែទៅជាភាសាខ្មែរ ដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីទទួលបានភាពត្រឹមត្រូវ សូមយល់អំពីថាការបកប្រែដោយស្វ័យប្រវត្តិសាច់អាចមានកំហុស ឬភាពមិនត្រឹមត្រូវប្រែផ្សេងៗ។ ឯកសារដើមនៅក្នុងភាសា​ដើមរបស់វាគួរត្រូវបានយកជាឯកសារ​ដែលមានអំណាចសិទ្ធិ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សដែលមានជំនាញគឺគួរត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនិងការបកស្រាយខុសៗណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->