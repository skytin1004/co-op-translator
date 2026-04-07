# Loo juurkataloogi *.env* fail

Selles õppeülesandes juhendame sind Azure'i teenuste keskkonnamuutujate seadistamisel kasutades *.env* faili. Keskkonnamuutujad võimaldavad turvaliselt hallata tundlikke mandaate, näiteks API-võtmeid, ilma et neid otse koodibaasi kõvakodeeritaks.

> [!IMPORTANT]
> - Konfigureerida tuleb vaid üks keeltemudelite teenus (Azure OpenAI või OpenAI). Täida keskkonnamuutujad eelistatud teenuse jaoks. Kui mitmele keeltemudelile on keskkonnamuutujad seadistatud, valib Co-op Translator välja ühe prioriteedi alusel.
> - Kui Computer Vision keskkonnamuutujad puuduvad, lülitub tõlk automaatselt [ainult Markdown-režiimile](./markdown-only-mode.md).

> [!NOTE]
> Käesolev juhend keskendub peamiselt Azure'i teenustele, kuid võid valida mis tahes toetatud keeltemudeli [toetatud mudelite ja teenuste nimekirjast](../README.md#-supported-models-and-services).

## Loo *.env* fail

Loo oma projekti juurkataloogi fail nimega *.env*. See fail salvestab kõik sinu keskkonnamuutujad lihtsas formaadis.

> [!WARNING]
> Ära pane oma *.env* faili versioonihaldusesse nagu Git. Lisa *.env* oma .gitignore failile, et vältida tahtmatuid commite.

1. Liigu oma projekti juurkataloogi.

1. Loo oma projekti juurkataloogi *.env* fail.

1. Ava *.env* fail ja kleebi järgmine mall:

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
> Kui soovid oma API võtmeid ja lõpp-punkte leida, võid vaadata [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutühendus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->