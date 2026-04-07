# Postavljanje Azure AI za Co-op Translator (Azure OpneAI & Azure AI Vision)

Ovaj vodič vodi vas kroz postavljanje Azure OpenAI za jezični prijevod i Azure Computer Vision za analizu sadržaja slika (koji se zatim može koristiti za prijevod temeljen na slikama) unutar Azure AI Foundry.

**Preduvjeti:**
- Azure račun s aktivnom pretplatom.
- Dovoljne dozvole za stvaranje resursa i implementacija u vašoj Azure pretplati.

## Kreiranje Azure AI Projekta

Počet ćete s kreiranjem Azure AI Projekta, koji služi kao središnje mjesto za upravljanje vašim AI resursima.

1. Idite na [https://ai.azure.com](https://ai.azure.com) i prijavite se svojim Azure računom.

1. Odaberite **+Create** za kreiranje novog projekta.

1. Obavite sljedeće zadatke:
   - Unesite **Naziv projekta** (npr. `CoopTranslator-Project`).
   - Odaberite **AI hub** (npr. `CoopTranslator-Hub`) (Ako treba, kreirajte novi).

1. Kliknite "**Review and Create**" za postavljanje projekta. Bit ćete preusmjereni na stranicu pregleda vašeg projekta.

## Postavljanje Azure OpenAI za jezični prijevod

Unutar vašeg projekta, implementirat ćete Azure OpenAI model koji će služiti kao backend za prijevod teksta.

### Otvorite svoj Projekt

Ako već niste tamo, otvorite nedavno kreirani projekt (npr. `CoopTranslator-Project`) u Azure AI Foundry.

### Implementirajte OpenAI Model

1. U lijevom izborniku vašeg projekta, pod "My assets", odaberite "**Models + endpoints**".

1. Odaberite **+ Deploy model**.

1. Odaberite **Deploy Base Model**.

1. Prikazat će vam se popis dostupnih modela. Filtrirajte ili pretražite za odgovarajući GPT model. Preporučamo `gpt-4o`.

1. Odaberite željeni model i kliknite **Confirm**.

1. Odaberite **Deploy**.

### Konfiguracija Azure OpenAI

Nakon implementacije, možete odabrati deployment sa stranice "**Models + endpoints**" da biste pronašli njegov **REST endpoint URL**, **Key**, **Deployment name**, **Model name** i **API version**. To će vam trebati za integraciju modela prijevoda u vašu aplikaciju.

> [!NOTE]
> API verzije možete odabrati s [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) stranice prema vašim zahtjevima. Imajte na umu da se **API verzija** razlikuje od **Model verzije** prikazane na stranici **Models + endpoints** u Azure AI Foundry.

## Postavljanje Azure Computer Vision za prijevod slika

Da biste omogućili prijevod teksta unutar slika, trebate pronaći Azure AI Service API Key i Endpoint.

1. Idite na svoj Azure AI Projekt (npr. `CoopTranslator-Project`). Provjerite jeste li na stranici pregleda projekta.

### Konfiguracija Azure AI Service

Pronađite API Key i Endpoint iz Azure AI Service.

1. Idite na svoj Azure AI Projekt (npr. `CoopTranslator-Project`). Provjerite jeste li na stranici pregleda projekta.

1. Pronađite **API Key** i **Endpoint** na kartici Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Ova veza omogućava mogućnosti povezanog Azure AI Services resursa (uključujući analizu slike) dostupnima vašem AI Foundry projektu. Zatim ovu vezu možete koristiti u svojim bilježnicama ili aplikacijama za izvlačenje teksta iz slika, koji se potom može poslati Azure OpenAI modelu na prijevod.

## Konsolidacija Vaših Podataka za Pristup

Do sada biste trebali imati sljedeće podatke:

**Za Azure OpenAI (Prijevod teksta):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Naziv modela (npr. `gpt-4o`)
- Azure OpenAI Naziv deploymenta (npr. `cooptranslator-gpt4o`)
- Azure OpenAI API Verzija

**Za Azure AI Services (Izvlačenje teksta iz slike putem Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Primjer: Konfiguracija Varijabli Okoline (Preview)

Kasnije, prilikom izrade vaše aplikacije, najvjerojatnije ćete ih konfigurirati koristeći prikupljene podatke ovako:

```bash
# Azure AI vjerodajnice servisa (potrebno za prijevod slika)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # npr., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Opcionalni sigurnosni setovi: duplicirajte varijable sa sufiksom _1/_2 (isti indeks za sve varijable u setu)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI vjerodajnice (potrebno za prijevod teksta)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # npr., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # npr., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # npr., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # npr., 2024-12-01-preview

# Opcionalni sigurnosni setovi: duplicirajte cijeli AZURE_OPENAI_* set sa sufiksom _1/_2 (isti indeks za sve varijable)
```

---

### Daljnje čitanje

- [Kako kreirati projekt u Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kako kreirati Azure AI resurse](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kako implementirati OpenAI modele u Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument je preveden koristeći AI uslugu za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->