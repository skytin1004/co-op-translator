# Unda faili la *.env* kwenye saraka kuu

Katika mafunzo haya, tutakuongoza jinsi ya kuweka vigezo vya mazingira kwa huduma za Azure kutumia faili la *.env*. Vigezo vya mazingira vinakuwezesha kusimamia kwa usalama taarifa nyeti, kama vile funguo za API, bila kuzichora moja kwa moja kwenye msimbo wako.

> [!IMPORTANT]
> - Huduma moja tu ya mfano wa lugha (Azure OpenAI au OpenAI) inahitaji kusanidiwa. Jaza vigezo vya mazingira kwa huduma unayopendelea. Ikiwa vigezo vya mazingira kwa mifano mingi ya lugha vimewekwa, tafsiri ya ushirikiano itachagua moja kulingana na kipaumbele.
> - Ikiwa vigezo vya mazingira vya Computer Vision havijatolewa, mtafsiri atabadilisha moja kwa moja kuwa [hali ya Markdown pekee](./markdown-only-mode.md).

> [!NOTE]
> Mwongozo huu unahusu hasa huduma za Azure, lakini unaweza kuchagua mfano wowote wa lugha unaoungwa mkono kutoka kwa [orodha ya mifano na huduma zinazoungwa mkono](../README.md#-supported-models-and-services).

## Unda faili la *.env*

Kwenye saraka kuu ya mradi wako, unda faili lenye jina *.env*. Faili hili litaweka vigezo vyote vya mazingira kwa muundo rahisi.

> [!WARNING]
> Usitoe faili lako la *.env* kwenye mifumo ya udhibiti wa toleo kama Git. Ongeza *.env* kwenye faili lako la .gitignore ili kuzuia utoaji wa bahati mbaya.

1. Nenda kwenye saraka kuu ya mradi wako.

1. Unda faili la *.env* kwenye saraka kuu ya mradi wako.

1. Fungua faili la *.env* na weka mfano ufuatao:

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
> Ikiwa unataka kupata funguo zako za API na vituo, unaweza rejelea [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kauli ya Kukataa**:
Nyaraka hii imetatuliwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Nyaraka ya asili katika lugha yake inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri za kitaalamu na za binadamu zinapendekezwa. Hatubebei wajibu wowote kwa kutoelewana au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->