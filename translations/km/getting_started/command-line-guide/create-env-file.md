# បង្កើតឯកសារ *.env* នៅក្នុងថតដើម

ក្នុងមេរៀននេះ យើងនឹងណែនាំអ្នកក្នុងការកំណត់អថេរបរិយាកាសសម្រាប់សេវាកម្ម Azure ដោយប្រើឯកសារ *.env*។ អថេរបរិយាកាសអនុញ្ញាតឱ្យអ្នកគ្រប់គ្រងសម្ងាត់យ៉ាងសុវត្ថិភាព ដូចជាសោ API ដោយមិនត្រូវបញ្ចូលពួកវាក្នុងកូដផ្ទាល់។

> [!IMPORTANT]
> - មានតែសេវាកម្មម៉ូដែលភាសាមួយតែប៉ុណ្ណោះ (Azure OpenAI ឬ OpenAI) ត្រូវបានកំណត់។ សូមបំពេញអថេរបរិយាកាសសម្រាប់សេវាកម្មដែលអ្នកចូលចិត្ត។ ប្រសិនបើមានការកំណត់អថេរបរិយាកាសសម្រាប់ម៉ូដែលភាសាច្រើន Co-op Translator នឹងជ្រើសរើសមួយដោយផ្អែកលើអាទិភាព។
> - ប្រសិនបើអថេរបរិយាកាស Computer Vision មិនត្រូវបានកំណត់ ទំព័រ مترجم នឹងប្ដូរទៅជារបៀប [Markdown-only mode](./markdown-only-mode.md) ដោយស្វ័យប្រវត្តិ។

> [!NOTE]
> មេរៀននេះផ្តោតជាចម្បងលើសេវាកម្ម Azure ប៉ុន្តែអ្នកអាចជ្រើសម៉ូដែលភាសាណាមួយដែលគាំទ្រពីបញ្ជី [supported models and services](../README.md#-supported-models-and-services)។

## បង្កើតឯកសារ *.env*

នៅក្នុងថតដើមនៃគម្រោងរបស់អ្នក សូមបង្កើតឯកសារជាឈ្មោះ *.env*។ ឯកសារនេះនឹងរក្សាទុកអថេរបរិយាកាសទាំងអស់របស់អ្នកនៅក្នុងទ្រង់ទ្រាយសាមញ្ញ។

> [!WARNING]
> សូមកុំបញ្ជូនឯកសារ *.env* របស់អ្នកទៅប្រព័ន្ធគ្រប់គ្រងកំណែដូចជា Git។ សូមបន្ថែម *.env* ទៅក្នុងឯកសារ .gitignore របស់អ្នកដើម្បីចៀសវាងការបញ្ជូនដោយចៃដន្យ។

1. ទៅកាន់ថតដើមនៃគម្រោងរបស់អ្នក។

1. បង្កើតឯកសារ *.env* នៅក្នុងថតដើមនៃគម្រោងរបស់អ្នក។

1. បើកឯកសារ *.env* និងបិទបញ្ចូលគំរូខាងក្រោម៖

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
> ប្រសិនបើអ្នកចង់ស្វែងរកសោ API និងចំណុចចូលរបស់អ្នក អ្នកអាចយោងទៅកាន់ [set-up-azure-ai.md](../set-up-azure-ai.md)។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការព្យាយាម**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងព្យាយាមឱ្យបានត្រឹមត្រូវកម្រិតខ្ពស់ ក៏សូមយល់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការខ្វះឆ្ពោះត្រូវ។ ឯកសារដើមនៅភាសារបស់ខ្លួនគួរត្រូវបានពិចារណាថាជាទូទៅដើម។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សគឺពេញលេញជាង។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសខាតណាមួយដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->