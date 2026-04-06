# Unda faili ya *.env* katika saraka ya mzizi

Katika mafunzo haya, tutakuongoza jinsi ya kuweka mabadiliko ya mazingira kwa huduma za Azure kwa kutumia faili ya *.env*. Mabadiliko ya mazingira huruhusu kusimamia kwa usalama taarifa za siri, kama vile funguo za API, bila kuzichoma moja kwa moja kwenye msimbo wako.

> [!IMPORTANT]
> - Huduma moja tu ya mfano wa lugha (Azure OpenAI au OpenAI) inapaswa kusanidiwa. Jaza mabadiliko ya mazingira kwa huduma unayotaka. Ikiwa mabadiliko ya mazingira kwa baadhi ya mifano ya lugha yamesanidiwa, mtafsiri wa ushirikiano ataamua moja kulingana na kipaumbele.
> - Ikiwa mabadiliko ya mazingira ya Computer Vision hayajasetwa, mtafsiri atabadilisha moja kwa moja hadi [hali ya Markdown pekee](./markdown-only-mode.md).

> [!NOTE]
> Mwongozo huu unazingatia hasa huduma za Azure, lakini unaweza kuchagua mfano wowote wa lugha unaoungwa mkono kutoka [orodha ya mifano na huduma zinazoungwa mkono](../README.md#-supported-models-and-services).

## Unda faili ya *.env*

Katika saraka ya mzizi ya mradi wako, unda faili liitwalo *.env*. Faili hili litahifadhi mabadiliko yote ya mazingira kwa muundo rahisi.

> [!WARNING]
> Usifanye commit faili yako ya *.env* katika mifumo ya kudhibiti toleo kama Git. Ongeza *.env* kwenye faili lako la .gitignore ili kuzuia kufanya commit kwa bahati mbaya.

1. Tembelea saraka ya mzizi ya mradi wako.

1. Unda faili ya *.env* katika saraka ya mzizi ya mradi wako.

1. Fungua faili ya *.env* na ubandike kiolezo kilichofuata:

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
> Ikiwa ungependa kupata funguo zako za API na vituo, unaweza rejelea [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyo**:  
Hati hii imetafsiriwa kwa kutumia huduma ya utafsiri wa AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kufikia usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au kasoro. Hati ya asili katika lugha yake ya mama inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inashauriwa. Hatubebei dhamana kwa kutoelewana au tafsiri zilizotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->