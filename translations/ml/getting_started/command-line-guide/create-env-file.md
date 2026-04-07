# റൂട്ട്ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക

ഈ ട്യൂട്ടോറിയലിൽ, Azure സേവനങ്ങൾക്ക് നിങ്ങളുടെ എൻവയൺമെന്റ് വേരിയബിളുകൾ സജ്ജമാക്കുന്നതിനുള്ള മാർഗ്ഗനിർദ്ദേശം നൽകുന്നതാണ്. എൻവയൺമെന്റ് വേരിയബിളുകൾ, API കീകൾ പോലുള്ള സുരക്ഷിതമായ ക്രെഡൻഷ്യലുകൾ നിങ്ങളുടെ കോഡ്‌بേസിൽ ഹാർഡ്കോഡുചെയ്യാതെ സുരക്ഷിതമായി കൈകാര്യം ചെയ്യാൻ സഹായിക്കുന്നു.

> [!IMPORTANT]
> - ഒരൊറ്റ ഭാഷാ മോഡൽ സേവനമേ (Azure OpenAI അല്ലെങ്കിൽ OpenAI) कॉन्फിഗർ ചെയ്യേണ്ടതാണ്. നിങ്ങളുടെ ഇഷ്ടപ്പെട്ട സേവനത്തിനായി എൻവയൺമെന്റ് വേരിയബിളുകൾ പൂരിപ്പിക്കുക. ഒരേസമയം പല ഭാഷാ മോഡലുകളുടെ എൻവയൺമെന്റ് വേരിയബിളുകൾ സജ്ജമാക്കിയാൽ, co-op translator മുൻഗണന അനുസരിച്ച് ഒന്ന് തിരഞ്ഞെടുക്കും.
> - Computer Vision എൻവയൺമെന്റ് വേരിയബിളുകൾ സജ്ജമാക്കിയില്ലെങ്കിൽ, translator സ്വയമേധയാ [Markdown-only mode](./markdown-only-mode.md) ലേക്ക് മാറും.

> [!NOTE]
> ഈ ഗൈഡ് Azure സേവനങ്ങളിൽ പ്രധാനമായി ശ്രദ്ധ കേന്ദ്രീകരിച്ചിരിക്കുന്നു, പക്ഷേ നിങ്ങൾ [supported models and services list](../README.md#-supported-models-and-services) ൽനിന്ന് പിന്തുണയുള്ള ഏതൊരു ഭാഷാ മോഡലും തിരഞ്ഞെടുക്കാവുന്നതാണ്.

## *.env* ഫയൽ സൃഷ്ടിക്കുക

നിങ്ങളുടെ പ്രോജക്ടിന്റെ റൂട്ട്ഡയറക്ടറിയിൽ *.env* എന്ന പേരിൽ ഒരു ഫയൽ സൃഷ്ടിക്കുക. ഈ ഫയലിൽ നിങ്ങളുടെ എല്ലാ എൻവയൺമെന്റ് വേരിയബിളുകളും ലളിതമായ ഫോർമാറ്റിൽ സംഭരിക്കും.

> [!WARNING]
> നിങ്ങളുടെ *.env* ഫയൽ Git പോലുള്ള വേർഷൻ കൺട്രോൾ സിസ്റ്റങ്ങളിൽ കമ്മിറ്റ് ചെയ്യേണ്ടതില്ല. അസാധാരണ കമ്മിറ്റുകൾ തടയാൻ *.env* നിങ്ങളുടെ .gitignore ഫയലിൽ ചേർക്കുക.

1. നിങ്ങളുടെ പ്രോജക്ടിന്റെ റൂട്ട്ഡയറക്ടറിയിലേക്ക് പോകുക.

1. പ്രോജക്ടിന്റെ റൂട്ട്ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക.

1. *.env* ഫയൽ തുറന്ന് താഴെ കൊടുത്ത ടെംപ്ലേറ്റ് പേസ്റ്റ് ചെയ്യുക:

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
> നിങ്ങളുടെ API കീകളും എണ്ട്പോയിന്റുകളും കണ്ടെത്താൻ [set-up-azure-ai.md](../set-up-azure-ai.md) കാണാവുന്നതാണ്.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ഡിസ്‌ക്ലെയിമർ**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്യപ്പെട്ടതാണ്. നാം നിശ്ചിതത്വത്തിന് ശ്രമിക്കുന്നതിനിടയിലും, യാന്ത്രിക വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അച്ചടക്കങ്ങൾ ഉണ്ടാകാവുന്നതാണ്. അതിനാൽ, എന്നാൽ മറ്റുളള ഭാഷയിലെ പ്രമാണം അതിന്റെ ഉറപ്പെടുത്തിയ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദ്ദേശിക്കുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിനാൽ ഉണ്ടാകാവുന്ന ഏതെന്താനും തെറ്റായ വ്യാഖ്യാനത്തിനും വരുത്തിയ തെറ്റിനും ഞങ്ങൾക്ക് ബാധ്യതയില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->