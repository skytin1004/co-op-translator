# റൂട്ട് ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക

ഈ ട്യൂട്ടോറിയലിൽ, Azure സേവനങ്ങൾക്ക് വേണ്ടിയുള്ള പരിസ്ഥിതി വ്യത്യാസങ്ങൾ നിങ്ങൾ എങ്ങനെ സജ്ജീകരിക്കാമെന്ന് വിശദീകരിക്കും. പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സുരക്ഷിതമായി API കീകൾ പോലുള്ള സേനസെറ്റീവ് ക്രെഡൻഷ്യലുകൾ നിർകോഡ് ചെയാതെ കൈകാര്യം ചെയ്യുന്നതിനുള്ള മാർഗ്ഗമാണ്.

> [!IMPORTANT]
> - ഒരു ഭാഷ മോഡൽ സേവനം മാത്രം (Azure OpenAI അല്ലെങ്കിൽ OpenAI) സജ്ജീകരിക്കേണ്ടതുണ്ട്. നിങ്ങളുടെ ഇഷ്ടാനുസൃത സേവനത്തിനുള്ള പരിസ്ഥിതി വ്യത്യാസങ്ങൾ പൂരിപ്പിക്കുക. ഒന്നിലധികം ഭാഷാ മോഡലുകൾക്കായി പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സജ്ജീകരിച്ചാൽ, co-op translator മുൻഗണന പ്രകാരം ഓരൊന്ന് തിരഞ്ഞെടുക്കും.
> - Computer Vision പരിസ്ഥിതി വ്യത്യാസങ്ങൾ സജ്ജീകരിക്കപ്പെടാത്ത പക്ഷം, translator സ്വയം [Markdown-only mode](./markdown-only-mode.md) തുറക്കും.

> [!NOTE]
> ഈ ഗൈഡ് പ്രധാനമായി Azure സേവനങ്ങളെ കേന്ദ്രീകരിച്ചിരിക്കുന്നുവെങ്കിലും, [supported models and services list](../README.md#-supported-models-and-services) ൽ നിന്നും മറ്റ് പിന്തുണയുള്ള ഭാഷ മോഡലുകളും തിരഞ്ഞെടുക്കാം.

## *.env* ഫയൽ സൃഷ്ടിക്കുക

നിങ്ങളുടെ പ്രോജക്റ്റ് റൂട്ട് ഡയറക്ടറിയിൽ *.env* എന്ന പേരിൽ ഒരു ഫയൽ സൃഷ്ടിക്കുക. ഈ ഫയലിൽ നിങ്ങളുടെ എല്ലാ പരിസ്ഥിതി വ്യത്യാസങ്ങളും എളുപ്പമുള്ള ഫോർമാറ്റിൽ സൂക്ഷിക്കും.

> [!WARNING]
> നിങ്ങളുടെ *.env* ഫയൽ Git പോലുള്ള വേർഷൻ കൺട്രോൾ സിസ്റ്റങ്ങളിലും കമ്മിറ്റ് ചെയ്യരുത്. അവമുടക്കാതിരിക്കാനായി *.env* നെ .gitignore ലിസ്റ്റിൽ ചേർക്കുക.

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ റൂട്ട് ഡയറക്ടറിയിലേക്ക് പോവുക.

1. റൂട്ട് ഡയറക്ടറിയിൽ *.env* ഫയൽ സൃഷ്ടിക്കുക.

1. *.env* ഫയൽ തുറന്ന് ചുവടെയുള്ള ടെംപ്ലേറ്റ് പകർത്തി ചേർക്കുക:

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
> നിങ്ങളുടെ API കീകളും എന്റ്പോയിന്റുകളും കണ്ടെത്താൻ, [set-up-azure-ai.md](../set-up-azure-ai.md) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസ്പഷ്ടീകരണം**:  
ഈ പ്രമാണം AI ഭാഷാന്തർ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്കായി ശ്രമിച്ചുവെങ്കിലും, ഓട്ടോമേറ്റഡ് ഭാഷാന്തരങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാമെന്ന് ദയവായി മനസിലാക്കുക. സ്വദേശഭാഷയിൽ ഉള്ള ഓർജിനൽ പ്രമാണം അധികാരപരമായ ഉറവിടമായി പരിഗണിക്കപ്പെടmalıdır. നിർണ്ണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യഭാഷാന്തരം ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ ഉണ്ടാകുന്ന ഏതൊരു തെറ്റിനും അല്ലെങ്കിൽ തെറ്റിദ്ധാരണകൾക്കും ഞങ്ങൾ ഉത്തരവാദിത്വം വരുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->