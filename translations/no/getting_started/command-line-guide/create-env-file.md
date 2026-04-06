# Opprett *.env*-filen i rotkatalogen

I denne veiledningen vil vi hjelpe deg med å sette opp miljøvariablene dine for Azure-tjenester ved hjelp av en *.env*-fil. Miljøvariabler lar deg sikkert håndtere sensitive legitimasjoner, som API-nøkler, uten å hardkode dem i kodebasen din.

> [!IMPORTANT]
> - Bare én språkmodelltjeneste (Azure OpenAI eller OpenAI) trenger å konfigureres. Fyll ut miljøvariablene for din foretrukne tjeneste. Hvis miljøvariabler for flere språkmodeller er satt, vil co-op translator velge en basert på prioritet.
> - Hvis miljøvariabler for Computer Vision ikke er satt, vil oversetteren automatisk bytte til [kun Markdown-modus](./markdown-only-mode.md).

> [!NOTE]
> Denne guiden fokuserer primært på Azure-tjenester, men du kan velge hvilken som helst støttet språkmodell fra [listen over støttede modeller og tjenester](../README.md#-supported-models-and-services).

## Opprett *.env*-filen

I rotkatalogen til prosjektet ditt oppretter du en fil som heter *.env*. Denne filen vil lagre alle miljøvariablene dine i et enkelt format.

> [!WARNING]
> Ikke legg *.env*-filen din til versjonskontrollsystemer som Git. Legg til *.env* i .gitignore-filen din for å unngå utilsiktede commits.

1. Naviger til rotkatalogen til prosjektet ditt.

1. Opprett en *.env*-fil i rotkatalogen til prosjektet ditt.

1. Åpne *.env*-filen og lim inn følgende mal:

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
> Hvis du vil finne API-nøklene og endepunktene dine, kan du se [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på dets opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for noen misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->