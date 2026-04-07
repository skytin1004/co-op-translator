# Ställ in Azure AI för Co-op Translator (Azure OpneAI & Azure AI Vision)

Den här guiden hjälper dig att ställa in Azure OpenAI för språköversättning och Azure Computer Vision för bildinnehållsanalys (vilket sedan kan användas för bildbaserad översättning) inom Azure AI Foundry.

**Förutsättningar:**
- Ett Azure-konto med en aktiv prenumeration.
- Tillräckliga behörigheter för att skapa resurser och distributioner i din Azure-prenumeration.

## Skapa ett Azure AI-projekt

Du börjar med att skapa ett Azure AI-projekt, som fungerar som en central plats för att hantera dina AI-resurser.

1. Navigera till [https://ai.azure.com](https://ai.azure.com) och logga in med ditt Azure-konto.

1. Välj **+Create** för att skapa ett nytt projekt.

1. Utför följande uppgifter:
   - Ange ett **Projektnamn** (t.ex. `CoopTranslator-Project`).
   - Välj **AI-hubben** (t.ex. `CoopTranslator-Hub`) (Skapa en ny om det behövs).

1. Klicka på "**Review and Create**" för att sätta upp ditt projekt. Du kommer att tas till projektets översiktssida.

## Ställ in Azure OpenAI för språköversättning

Inom ditt projekt distribuerar du en Azure OpenAI-modell som fungerar som backend för textöversättning.

### Navigera till ditt projekt

Om du inte redan är där, öppna ditt nyligen skapade projekt (t.ex. `CoopTranslator-Project`) i Azure AI Foundry.

### Distribuera en OpenAI-modell

1. Från projektets vänstermeny, under "My assets", välj "**Models + endpoints**".

1. Välj **+ Deploy model**.

1. Välj **Deploy Base Model**.

1. Du kommer att få upp en lista med tillgängliga modeller. Filtrera eller sök efter en lämplig GPT-modell. Vi rekommenderar `gpt-4o`.

1. Välj önskad modell och klicka på **Confirm**.

1. Välj **Deploy**.

### Azure OpenAI-konfiguration

När modellen är distribuerad kan du välja distributionen från sidan "**Models + endpoints**" för att hitta dess **REST-endpoint-URL**, **Nyckel**, **Distributionsnamn**, **Modellnamn** och **API-version**. Dessa kommer att behövas för att integrera översättningsmodellen i din applikation.

> [!NOTE]
> Du kan välja API-versioner från sidan [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) baserat på dina behov. Var medveten om att **API-versionen** skiljer sig från **Modellversionen** som visas på sidan **Models + endpoints** i Azure AI Foundry.

## Ställ in Azure Computer Vision för bildöversättning

För att möjliggöra översättning av text i bilder behöver du hitta API-nyckeln och endpoint för Azure AI-tjänsten.

1. Navigera till ditt Azure AI-projekt (t.ex. `CoopTranslator-Project`). Säkerställ att du är på projektets översiktssida.

### Azure AI-tjänstkonfiguration

Hitta API-nyckeln och endpoint från Azure AI-tjänsten.

1. Navigera till ditt Azure AI-projekt (t.ex. `CoopTranslator-Project`). Säkerställ att du är på projektets översiktssida.

1. Hitta **API Key** och **Endpoint** under fliken Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Denna anslutning gör kapaciteterna hos den länkade Azure AI Services-resursen (inklusive bildanalys) tillgängliga för ditt AI Foundry-projekt. Du kan sedan använda denna anslutning i dina notebooks eller applikationer för att extrahera text från bilder, vilket därefter kan skickas till Azure OpenAI-modellen för översättning.

## Sammanställ dina autentiseringsuppgifter

Vid det här laget bör du ha samlat följande:

**För Azure OpenAI (Textöversättning):**
- Azure OpenAI Endpoint
- Azure OpenAI API-nyckel
- Azure OpenAI Modellnamn (t.ex. `gpt-4o`)
- Azure OpenAI Distributionsnamn (t.ex. `cooptranslator-gpt4o`)
- Azure OpenAI API-version

**För Azure AI Services (Textutdrag från bilder via Vision):**
- Azure AI Service Endpoint
- Azure AI Service API-nyckel

### Exempel: Konfiguration av miljövariabler (Preview)

Senare, när du bygger din applikation, kommer du sannolikt att konfigurera den med dessa insamlade autentiseringsuppgifter. Till exempel kan du ange dem som miljövariabler på följande sätt:

```bash
# Azure AI-tjänstuppgifter (krävs för bildöversättning)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # t.ex., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Valfria reservuppsättningar: duplicera variabler med suffix _1/_2 (samma index för alla variabler i uppsättningen)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI-uppgifter (krävs för textöversättning)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # t.ex., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # t.ex., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # t.ex., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # t.ex., 2024-12-01-preview

# Valfria reservuppsättningar: duplicera hela AZURE_OPENAI_*-uppsättningen med suffix _1/_2 (samma index för alla variabler)
```

---

### Vidare läsning

- [Hur man skapar ett projekt i Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Hur man skapar Azure AI-resurser](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Hur man distribuerar OpenAI-modeller i Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->