# Opret filen *.env* i roddirectory

I denne vejledning vil vi guide dig gennem opsætning af dine miljøvariabler til Azure-tjenester ved hjælp af en *.env* fil. Miljøvariabler gør det muligt at administrere følsomme legitimationsoplysninger som API-nøgler sikkert uden at hardkode dem i din kodebase.

> [!IMPORTANT]
> - Der skal kun konfigureres én sprogmodeltjeneste (Azure OpenAI eller OpenAI). Udfyld miljøvariablerne for din foretrukne tjeneste. Hvis miljøvariabler for flere sprogmodeller er sat, vælger co-op translator én baseret på prioritet.
> - Hvis Computer Vision miljøvariabler ikke er sat, skifter oversætteren automatisk til [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Denne vejledning fokuserer primært på Azure-tjenester, men du kan vælge enhver understøttet sprogmodel fra [listen over understøttede modeller og tjenester](../README.md#-supported-models-and-services).

## Opret filen *.env*

I roddirectory for dit projekt, opret en fil med navnet *.env*. Denne fil vil gemme alle dine miljøvariabler i et enkelt format.

> [!WARNING]
> Committ ikke din *.env* fil til versionsstyringssystemer som Git. Tilføj *.env* til din .gitignore fil for at undgå utilsigtede commits.

1. Naviger til roddirectory for dit projekt.

1. Opret en *.env* fil i roddirectory for dit projekt.

1. Åbn *.env* filen og indsæt følgende skabelon:

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
> Hvis du vil finde dine API-nøgler og endpoints, kan du se [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->