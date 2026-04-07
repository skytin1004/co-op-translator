# Sett opp Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

Denne veiledningen tar deg gjennom å sette opp Azure OpenAI for språkoversettelse og Azure Computer Vision for bildeinnholdsanalyse (som deretter kan brukes til bildebasert oversettelse) innen Azure AI Foundry.

**Forutsetninger:**
- En Azure-konto med et aktivt abonnement.
- Tilstrekkelige tillatelser til å opprette ressurser og distribusjoner i ditt Azure-abonnement.

## Opprett et Azure AI-prosjekt

Du starter med å opprette et Azure AI-prosjekt, som fungerer som et sentralt sted for å administrere AI-ressursene dine.

1. Naviger til [https://ai.azure.com](https://ai.azure.com) og logg inn med din Azure-konto.

1. Velg **+Create** for å opprette et nytt prosjekt.

1. Utfør følgende oppgaver:
   - Skriv inn et **Prosjektnavn** (f.eks. `CoopTranslator-Project`).
   - Velg **AI-hubben** (f.eks. `CoopTranslator-Hub`) (Opprett en ny om nødvendig).

1. Klikk "**Review and Create**" for å sette opp prosjektet ditt. Du vil bli tatt til oversiktssiden for prosjektet.

## Sett opp Azure OpenAI for språkoversettelse

Innenfor prosjektet ditt vil du distribuere en Azure OpenAI-modell som skal fungere som backend for tekstoversettelse.

### Naviger til prosjektet ditt

Hvis du ikke allerede er der, åpne ditt nylig opprettede prosjekt (f.eks. `CoopTranslator-Project`) i Azure AI Foundry.

### Distribuer en OpenAI-modell

1. Fra prosjektets venstremeny, under "Mine ressurser", velg "**Models + endpoints**".

1. Velg **+ Deploy model**.

1. Velg **Deploy Base Model**.

1. Du vil få en liste over tilgjengelige modeller. Filtrer eller søk etter en passende GPT-modell. Vi anbefaler `gpt-4o`.

1. Velg ønsket modell og klikk **Confirm**.

1. Velg **Deploy**.

### Azure OpenAI-konfigurasjon

Når modellen er distribuert, kan du velge distribusjonen fra "**Models + endpoints**"-siden for å finne dens **REST-endepunkt-URL**, **Nøkkel**, **Distribusjonsnavn**, **Modellnavn** og **API-versjon**. Disse vil være nødvendige for å integrere oversettelsesmodellen i applikasjonen din.

> [!NOTE]
> Du kan velge API-versjoner fra siden [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) basert på dine behov. Vær oppmerksom på at **API-versjon** er forskjellig fra **Modellversjon** som vises på **Models + endpoints**-siden i Azure AI Foundry.

## Sett opp Azure Computer Vision for bildeoversettelse

For å aktivere oversettelse av tekst i bilder, må du finne Azure AI Service API-nøkkel og endepunkt.

1. Naviger til ditt Azure AI-prosjekt (f.eks. `CoopTranslator-Project`). Sørg for at du er på prosjektets oversiktsside.

### Azure AI Service-konfigurasjon

Finn API-nøkkel og endepunkt fra Azure AI Service.

1. Naviger til ditt Azure AI-prosjekt (f.eks. `CoopTranslator-Project`). Sørg for at du er på prosjektets oversiktsside.

1. Finn **API Key** og **Endpoint** fra fanen for Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Denne tilkoblingen gjør mulighetene tilknyttet den koblede Azure AI Services-ressursen (inkludert bildeanalyse) tilgjengelige for AI Foundry-prosjektet ditt. Du kan deretter bruke denne tilkoblingen i notatbøker eller applikasjoner for å hente ut tekst fra bilder, som deretter kan sendes til Azure OpenAI-modellen for oversettelse.

## Konsolidering av dine legitimasjoner

Nå bør du ha samlet følgende:

**For Azure OpenAI (tekstoversettelse):**
- Azure OpenAI-endepunkt
- Azure OpenAI API-nøkkel
- Azure OpenAI-modellnavn (f.eks. `gpt-4o`)
- Azure OpenAI-distribusjonsnavn (f.eks. `cooptranslator-gpt4o`)
- Azure OpenAI API-versjon

**For Azure AI Services (innhenting av tekst fra bilder via Vision):**
- Azure AI Service-endepunkt
- Azure AI Service API-nøkkel

### Eksempel: Miljøvariabelkonfigurasjon (forhåndsvisning)

Senere, når du bygger applikasjonen din, vil du sannsynligvis konfigurere den med disse innsamlede legitimasjonene. For eksempel kan du sette dem som miljøvariabler slik:

```bash
# Azure AI-tjenestepåloggingsinformasjon (påkrevd for bildetranslasjon)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # f.eks., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Valgfrie reserve-sett: dupliser variabler med suffiks _1/_2 (samme indeks for alle variabler i settet)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI-påloggingsinformasjon (påkrevd for tekstoversettelse)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # f.eks., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # f.eks., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # f.eks., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # f.eks., 2024-12-01-preview

# Valgfrie reserve-sett: dupliser hele AZURE_OPENAI_* settet med suffiks _1/_2 (samme indeks for alle variabler)
```

---

### Videre lesning

- [Hvordan opprette et prosjekt i Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Hvordan opprette Azure AI-ressurser](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Hvordan distribuere OpenAI-modeller i Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på morsmålet skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->