# Sukurkite *.env* failą pagrindiniame kataloge

Šiame vadove mes jums paaiškinsime, kaip sukonfigūruoti savo aplinkos kintamuosius Azure paslaugoms naudojant *.env* failą. Aplinkos kintamieji leidžia saugiai valdyti jautrius prisijungimo duomenis, tokius kaip API raktai, be jų tiesioginio įrašymo į kodo bazę.

> [!IMPORTANT]
> - Reikia sukonfigūruoti tik vieną kalbos modelio paslaugą (Azure OpenAI arba OpenAI). Užpildykite aplinkos kintamuosius pagal savo pageidaujamą paslaugą. Jei nustatyti keli kalbos modelių aplinkos kintamieji, co-op translator pasirinks vieną pagal prioriteto tvarką.
> - Jei nėra nustatyti Computer Vision aplinkos kintamieji, vertėjas automatiškai perjungs į [tik Markdown režimą](./markdown-only-mode.md).

> [!NOTE]
> Šiame vadove daugiausia dėmesio skiriama Azure paslaugoms, tačiau galite pasirinkti bet kurį palaikomą kalbos modelį iš [palaikomų modelių ir paslaugų sąrašo](../README.md#-supported-models-and-services).

## Sukurkite *.env* failą

Projekto pagrindiniame kataloge sukurkite failą pavadinimu *.env*. Šiame faile bus saugomi visi jūsų aplinkos kintamieji paprastu formatu.

> [!WARNING]
> Neskelbkite savo *.env* failo versijų kontrolės sistemose, tokiuose kaip Git. Pridėkite *.env* prie savo .gitignore failo, kad išvengtumėte atsitiktinių įsipareigojimų.

1. Eikite į projekto pagrindinį katalogą.

1. Sukurkite *.env* failą projekto pagrindiniame kataloge.

1. Atidarykite *.env* failą ir įklijuokite šabloną:

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
> Jei norite rasti savo API raktus ir galinius taškus, galite kreiptis į [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už jokius nesusipratimus ar neteisingus aiškinimus, kylančius naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->