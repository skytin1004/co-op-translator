# Azure AI instellen voor Co-op Translator (Azure OpneAI & Azure AI Vision)

Deze handleiding begeleidt je bij het instellen van Azure OpenAI voor vertaaldiensten en Azure Computer Vision voor analyse van beeldinhoud (die vervolgens gebruikt kan worden voor beeldgebaseerde vertaling) binnen Azure AI Foundry.

**Vereisten:**
- Een Azure-account met een actieve abonnement.
- Voldoende machtigingen om resources en implementaties aan te maken binnen je Azure-abonnement.

## Maak een Azure AI-project aan

Je begint met het aanmaken van een Azure AI-project, dat fungeert als een centrale plek voor het beheren van je AI-resources.

1. Ga naar [https://ai.azure.com](https://ai.azure.com) en meld je aan met je Azure-account.

1. Selecteer **+Create** om een nieuw project aan te maken.

1. Voer de volgende taken uit:
   - Voer een **Projectnaam** in (bijv. `CoopTranslator-Project`).
   - Selecteer de **AI-hub** (bijv. `CoopTranslator-Hub`) (maak een nieuwe aan indien nodig).

1. Klik op "**Review and Create**" om je project op te zetten. Je wordt naar de overzichtspagina van je project gebracht.

## Azure OpenAI instellen voor taalvertaling

Binnen je project ga je een Azure OpenAI-model implementeren dat dient als backend voor tekstvertaling.

### Navigeer naar je project

Als je er nog niet bent, open je zojuist aangemaakte project (bijv. `CoopTranslator-Project`) in Azure AI Foundry.

### Implementeer een OpenAI-model

1. Selecteer in het linkermenu van je project onder "My assets" de optie "**Models + endpoints**".

1. Selecteer **+ Deploy model**.

1. Selecteer **Deploy Base Model**.

1. Je krijgt een lijst met beschikbare modellen te zien. Filter of zoek naar een geschikt GPT-model. We raden `gpt-4o` aan.

1. Selecteer het gewenste model en klik op **Confirm**.

1. Selecteer **Deploy**.

### Azure OpenAI-configuratie

Nadat het model is geïmplementeerd, kun je de deployment selecteren op de "**Models + endpoints**" pagina om de **REST endpoint URL**, **Key**, **Deployment name**, **Model name** en **API version** te vinden. Deze heb je nodig om het vertaalmodel in je applicatie te integreren.

> [!NOTE]
> Je kunt API-versies selecteren vanaf de [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) pagina op basis van je vereisten. Houd er rekening mee dat de **API version** verschilt van de **Model version** die wordt weergegeven op de **Models + endpoints** pagina in Azure AI Foundry.

## Azure Computer Vision instellen voor beeldvertaling

Om vertaling van tekst in afbeeldingen mogelijk te maken, moet je de Azure AI Service API-sleutel en Endpoint vinden.

1. Navigeer naar je Azure AI-project (bijv. `CoopTranslator-Project`). Zorg dat je op de overzichtspagina van het project bent.

### Azure AI Service-configuratie

Vind de API-sleutel en Endpoint bij de Azure AI Service.

1. Navigeer naar je Azure AI-project (bijv. `CoopTranslator-Project`). Zorg dat je op de overzichtspagina van het project bent.

1. Zoek de **API Key** en **Endpoint** via het tabblad Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Deze verbinding maakt de mogelijkheden van de gekoppelde Azure AI Services-resource (inclusief beeldanalyse) beschikbaar voor je AI Foundry-project. Je kunt deze verbinding gebruiken in je notebooks of applicaties om tekst uit afbeeldingen te extraheren, die vervolgens naar het Azure OpenAI-model kan worden gestuurd voor vertaling.

## Je inloggegevens consolideren

Je zou nu de volgende gegevens verzameld moeten hebben:

**Voor Azure OpenAI (Tekstvertaling):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (bijv. `gpt-4o`)
- Azure OpenAI Deployment Name (bijv. `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Voor Azure AI Services (Extractie van tekst uit afbeeldingen via Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Voorbeeld: Configuratie van omgevingsvariabelen (Preview)

Later, bij het bouwen van je applicatie configureer je deze waarschijnlijk met behulp van de verzamelde inloggegevens. Bijvoorbeeld, je zou ze als omgevingsvariabelen kunnen instellen zoals hieronder:

```bash
# Azure AI-servicegegevens (vereist voor beeldvertaling)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # bijv., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Optionele fallback-sets: dupliceer variabelen met achtervoegsel _1/_2 (zelfde index voor alle variabelen in de set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI-gegevens (vereist voor tekstvertaling)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # bijv., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # bijv., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # bijv., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # bijv., 2024-12-01-preview

# Optionele fallback-sets: dupliceer de volledige AZURE_OPENAI_* set met achtervoegsel _1/_2 (zelfde index voor alle variabelen)
```

---

### Verdere Lectuur

- [Hoe maak je een project aan in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Hoe maak je Azure AI-resources aan](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Hoe implementeer je OpenAI-modellen in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal dient als de gezaghebbende bron te worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij aanvaarden geen aansprakelijkheid voor eventuele misverstanden of verkeerde interpretaties voortvloeiend uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->