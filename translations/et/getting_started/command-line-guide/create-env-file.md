# Loo juurkausta faili *.env*

Selles juhendis juhendame sind Azure teenuste keskkonnamuutujate seadistamisel kasutades faili *.env*. Keskkonnamuutujad võimaldavad sul turvaliselt hallata tundlikke mandaate, nagu API võtmed, ilma neid koodibaasi kõvaks koodimiseks.

> [!IMPORTANT]
> - Ainult üks keelemudelite teenus (Azure OpenAI või OpenAI) peab olema seadistatud. Täida keskkonnamuutujad oma eelistatud teenuse jaoks. Kui mitme keelemudeli keskkonnamuutujaid on seatud, valib co-op translator ühe prioriteedi alusel.
> - Kui Computer Visioni keskkonnamuutujaid ei ole seatud, lülitub tõlk automaatselt üle [ainult Markdown režiimile](./markdown-only-mode.md).

> [!NOTE]
> See juhend keskendub peamiselt Azure teenustele, kuid võid valida mis tahes toetatud keelemudeli [toetatud mudelite ja teenuste nimekirjast](../README.md#-supported-models-and-services).

## Loo *.env* fail

Loo oma projekti juurkaustas fail nimega *.env*. See fail hoiab kõiki sinu keskkonnamuutujaid lihtsas vormingus.

> [!WARNING]
> Ära lisa oma *.env* faili versioonihaldussüsteemi nagu Git. Lisa *.env* oma .gitignore faili, et vältida juhuslikke commit'e.

1. Liigu oma projekti juurkausta.

1. Loo oma projekti juurkausta fail *.env*.

1. Ava *.env* fail ja kleebi sinna järgmine mall:

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
> Kui soovid leida oma API võtmeid ja lõpp-punkte, võid viidata juhisele [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles peaks olema autoriteetne allikas. Olulise teabe puhul soovitatakse professionaalset inimtõlget. Me ei vastuta tõlke kasutamisest tingitud arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->