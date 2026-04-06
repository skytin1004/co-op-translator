# Maak het *.env*-bestand aan in de hoofdmap

In deze tutorial begeleiden we je bij het instellen van je omgevingsvariabelen voor Azure-diensten met behulp van een *.env*-bestand. Omgevingsvariabelen maken het mogelijk om gevoelige inloggegevens, zoals API-sleutels, veilig te beheren zonder ze in je codebasis hard te coderen.

> [!IMPORTANT]
> - Er hoeft slechts één taalmodelservice (Azure OpenAI of OpenAI) geconfigureerd te worden. Vul de omgevingsvariabelen in voor je voorkeursservice. Als omgevingsvariabelen voor meerdere taalmodellen zijn ingesteld, zal de Co-op Translator er één selecteren op basis van prioriteit.
> - Als de omgevingsvariabelen voor Computer Vision niet zijn ingesteld, schakelt de vertaler automatisch over naar de [Markdown-only-modus](./markdown-only-mode.md).

> [!NOTE]
> Deze gids richt zich vooral op Azure-diensten, maar je kunt elk ondersteund taalmodel kiezen uit de [lijst met ondersteunde modellen en diensten](../README.md#-supported-models-and-services).

## Maak het *.env*-bestand aan

Maak in de hoofdmap van je project een bestand aan met de naam *.env*. Dit bestand slaat al je omgevingsvariabelen op in een eenvoudig formaat.

> [!WARNING]
> Voeg je *.env*-bestand niet toe aan versiebeheersystemen zoals Git. Voeg *.env* toe aan je .gitignore-bestand om onbedoelde commits te voorkomen.

1. Navigeer naar de hoofdmap van je project.

1. Maak een *.env*-bestand aan in de hoofdmap van je project.

1. Open het *.env*-bestand en plak de volgende sjabloon:

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
> Als je je API-sleutels en endpoints wilt vinden, kun je verwijzen naar [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor belangrijke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->