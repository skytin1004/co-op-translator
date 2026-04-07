# Skapa filen *.env* i rotkatalogen

I denna handledning guidar vi dig genom att ställa in dina miljövariabler för Azure-tjänster med hjälp av en *.env*-fil. Miljövariabler gör att du säkert kan hantera känsliga autentiseringsuppgifter, såsom API-nycklar, utan att hårdkoda dem i din kodbas.

> [!IMPORTANT]
> - Endast en språkmodelltjänst (Azure OpenAI eller OpenAI) behöver konfigureras. Fyll i miljövariablerna för din föredragna tjänst. Om miljövariabler för flera språkmodeller är satta, kommer co-op translator att välja en baserat på prioritet.
> - Om miljövariabler för Computer Vision inte är satta, kommer översättaren automatiskt att byta till [endast Markdown-läge](./markdown-only-mode.md).

> [!NOTE]
> Denna guide fokuserar främst på Azure-tjänster, men du kan välja vilken som helst av de stödda språkmodellerna från [listan över stödda modeller och tjänster](../README.md#-supported-models-and-services).

## Skapa *.env*-filen

I rotkatalogen för ditt projekt, skapa en fil med namnet *.env*. Denna fil kommer att lagra alla dina miljövariabler i ett enkelt format.

> [!WARNING]
> Lägg inte upp din *.env*-fil i versionshanteringssystem som Git. Lägg till *.env* i din .gitignore-fil för att förhindra oavsiktliga commits.

1. Navigera till rotkatalogen för ditt projekt.

1. Skapa en *.env*-fil i rotkatalogen för ditt projekt.

1. Öppna *.env*-filen och klistra in följande mall:

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
> Om du vill hitta dina API-nycklar och endpoints kan du hänvisa till [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår genom användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->