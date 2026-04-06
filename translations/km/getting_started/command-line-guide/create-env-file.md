# បង្កើតឯកសារ *.env* ក្នុងដើមថត

នៅក្នុងមេរៀននេះ យើងនឹងណែនាំអ្នកពីវិធីកំណត់អថេរបរិស្ថានសម្រាប់សេវាកម្ម Azure ដោយប្រើឯកសារ *.env*។ អថេរបរិស្ថានអនុញ្ញាតឲ្យអ្នកគ្រប់គ្រងសម្ងាត់យ៉ាងសុវត្ថិភាព ដូចជាកូនសោ API ដោយមិនចាំបាច់ដាក់ពួកវាចូលក្នុងកូដ។

> [!IMPORTANT]
> - ត្រូវកំណត់សេវាកម្មមួយតែម្ដងសម្រាប់ម៉ូដែលភាសា (Azure OpenAI ឬ OpenAI)។ បំពេញអថេរបរិស្ថានសម្រាប់សេវាកម្មដែលអ្នកចង់ប្រើ។ ប្រសិនបើមានការកំណត់អថេរបរិស្ថានរបស់ម៉ូដែលភាសាច្រើន អ្នកបកប្រែរួមគ្នានឹងជ្រើសរើសមួយអាស្រ័យលើអាទិភាព។
> - ប្រសិនបើអថេរបរិស្ថាន Computer Vision មិនត្រូវបានកំណត់ អ្នកបកប្រែគឺនឹងប្តូរទៅ [របៀប Markdown តែប៉ុណ្ណោះ](./markdown-only-mode.md) ដោយស្វ័យប្រវត្តិ។

> [!NOTE]
> មគ្គុទេសក៍នេះផ្តោតជាសំខាន់លើយករណ៍សេវាកម្ម Azure ប៉ុណ្ណោះ ប៉ុន្តែអ្នកអាចជ្រើសម៉ូដែលភាសាណាមួយដែលគាំទ្រពី [បណ្តុំម៉ូដែលនិងសេវាកម្មគាំទ្រ](../README.md#-supported-models-and-services)។

## បង្កើតឯកសារ *.env*

នៅក្នុងថតដើមនៃគម្រោងរបស់អ្នក បង្កើតឯកសារដោយមានឈ្មោះ *.env*។ ឯកសារនេះនឹងផ្ទុកអថេរបរិស្ថានទាំងអស់របស់អ្នកក្នុងទ្រង់ទ្រាយសាមញ្ញ។

> [!WARNING]
> កុំប្រគល់ឯកសារ *.env* របស់អ្នកទៅប្រព័ន្ធគ្រប់គ្រងកំណែដូចជា Git។ បន្ថែម *.env* ទៅក្នុងឯកសារ .gitignore របស់អ្នក ដើម្បីការពារការបញ្ចូលច្រឡំ។

1. ទៅកាន់ថតដើមនៃគម្រោងរបស់អ្នក។

1. បង្កើតឯកសារ *.env* នៅក្នុងថតដើមនៃគម្រោងរបស់អ្នក។

1. បើកឯកសារ *.env* ហើយបិទស្រង់ពុម្ពតាងខាងក្រោម៖

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
> ប្រសិនបើអ្នកចង់ស្វែងរកកូនសោ API និងចំណុចចេញ អ្នកអាចយោងទៅ [set-up-azure-ai.md](../set-up-azure-ai.md)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ បើយើងខិតខំរកការត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិសម្រង់អាចមានកំហុសឬការខុសគ្នា។ ឯកសារប្រភពដើមនៅក្នុងភាសាមូលដ្ឋានគួរត្រូវបានយកចិត្តទុកដាក់ជាផ្លូវការជាទីបំផុត។ សម្រាប់ព័ត៌មានដាច់ខាត ការបកប្រែមនុស្សជំនាញត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->