# Azure AI:n käyttöönotto Co-op Translatorille (Azure OpneAI & Azure AI Vision)

Tässä ohjeessa käydään läpi, kuinka asetat Azure OpenAI:n kielenkääntämiseen ja Azure Computer Visionin kuvasisällön analysointiin (jota voidaan käyttää kuvapohjaiseen käännökseen) Azure AI Foundryn sisällä.

**Esivaatimukset:**
- Azure-tili, jossa on aktiivinen tilaus.
- Riittävät oikeudet luoda resursseja ja käyttöönottoja Azure-tilauksessasi.

## Luo Azure AI -projekti

Aloitat luomalla Azure AI -projektin, joka toimii keskeisenä paikkana AI-resurssiesi hallintaan.

1. Siirry osoitteeseen [https://ai.azure.com](https://ai.azure.com) ja kirjaudu sisään Azure-tililläsi.

1. Valitse **+Create** luodaksesi uuden projektin.

1. Suorita seuraavat tehtävät:
   - Syötä **Projektin nimi** (esim. `CoopTranslator-Project`).
   - Valitse **AI hub** (esim. `CoopTranslator-Hub`) (Luo uusi tarvittaessa).

1. Napsauta "**Review and Create**" asettaaksesi projektisi. Sinut ohjataan projektisi yleiskatsaus-sivulle.

## Aseta Azure OpenAI kielenkäännökseen

Projektissasi otat käyttöön Azure OpenAI -mallin tekstin käännöstä varten taustapalvelimena.

### Siirry projektiisi

Jos et ole jo siellä, avaa juuri luomasi projekti (esim. `CoopTranslator-Project`) Azure AI Foundrysta.

### Ota käyttöön OpenAI-malli

1. Valitse projektisi vasemmasta valikosta "My assets" -kohdan alta "**Models + endpoints**".

1. Valitse **+ Deploy model**.

1. Valitse **Deploy Base Model**.

1. Näet luettelon käytettävissä olevista malleista. Suodata tai etsi sopivaa GPT-mallia. Suosittelemme `gpt-4o`:ta.

1. Valitse haluamasi malli ja napsauta **Confirm**.

1. Valitse **Deploy**.

### Azure OpenAI:n asetukset

Kun malli on käyttöön otettu, voit valita käyttöönoton "**Models + endpoints**" -sivulta löytääksesi sen **REST-päätepisteen URL:n**, **avaimen**, **käyttöönoton nimen**, **mallin nimen** ja **API-version**. Näitä tarvitaan käännösmallin integroimiseksi sovellukseesi.

> [!NOTE]
> Voit valita API-versioita osoitteesta [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) tarpeidesi mukaan. Huomaa, että **API-versio** eroaa **Malliversiosta**, joka näkyy **Models + endpoints** -sivulla Azure AI Foundryssa.

## Aseta Azure Computer Vision kuvakäännökseen

Tekstin kääntämisen mahdollistamiseksi kuvista sinun täytyy löytää Azure AI Service API Key ja Endpoint.

1. Siirry Azure AI -projektiisi (esim. `CoopTranslator-Project`). Varmista, että olet projektin yleiskatsaus-sivulla.

### Azure AI Service -asetukset

Löydä API Key ja Endpoint Azure AI Service -välilehdeltä.

1. Siirry Azure AI -projektiisi (esim. `CoopTranslator-Project`). Varmista, että olet projektin yleiskatsaus-sivulla.

1. Etsi **API Key** ja **Endpoint** Azure AI Service -välilehdeltä.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Tämä yhteys tekee linkitetyn Azure AI Services -resurssin mahdollisuudet (mukaan lukien kuvan analysointi) käytettäväksi AI Foundry -projektissasi. Voit käyttää tätä yhteyttä muistioissasi tai sovelluksissasi kuvan tekstin purkamiseen, jonka voi sitten lähettää Azure OpenAI -mallille käännettäväksi.

## Todennustietojen kokoaminen

Nyt sinulla pitäisi olla koossa seuraavat tiedot:

**Azure OpenAI:lle (teksti käännökseen):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Mallin nimi (esim. `gpt-4o`)
- Azure OpenAI Käyttöönoton nimi (esim. `cooptranslator-gpt4o`)
- Azure OpenAI API-versio

**Azure AI Services:lle (kuvatekstin purku Visionin kautta):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Esimerkki: Ympäristömuuttujien määrittely (esikatselu)

Myöhemmin, rakentaessasi sovellustasi, todennäköisesti määrittelet nämä kerätyt tunnistetiedot ympäristömuuttujina seuraavan esimerkin mukaisesti:

```bash
# Azure AI -palvelun tunnistetiedot (vaaditaan kuvakäännöksessä)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # esim., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Valinnaiset varasetit: kopioi muuttujat sufiksilla _1/_2 (sama indeksi kaikille kyseiselle joukolle kuuluville muuttujille)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI -tunnistetiedot (vaaditaan tekstikäännöksessä)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # esim., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # esim., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # esim., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # esim., 2024-12-01-preview

# Valinnaiset varasetit: kopioi koko AZURE_OPENAI_* joukko sufiksilla _1/_2 (sama indeksi kaikille muuttujille)
```

---

### Lisälukemista

- [Kuinka luoda projekti Azure AI Foundryssa](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kuinka luoda Azure AI -resursseja](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kuinka ottaa OpenAI-malleja käyttöön Azure AI Foundryssa](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on aina määräävä lähde. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->