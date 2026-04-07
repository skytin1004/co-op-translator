# Nastavitev Azure AI za Co-op Translator (Azure OpneAI & Azure AI Vision)

Ta vodič vas vodi skozi postopek nastavitev Azure OpenAI za prevajanje jezikov in Azure Computer Vision za analizo vsebine slik (ki se lahko nato uporablja za prevajanje na osnovi slik) znotraj Azure AI Foundry.

**Predpogoj:**
- Azure račun z aktivno naročnino.
- Zadostna dovoljenja za ustvarjanje virov in nameščanj v vaši Azure naročnini.

## Ustvarite Azure AI Projekt

Začeli boste z ustvarjanjem Azure AI Projekta, ki deluje kot osrednje mesto za upravljanje vaših AI virov.

1. Pojdite na [https://ai.azure.com](https://ai.azure.com) in se prijavite z vašim Azure računom.

1. Izberite **+Create** za ustvarjanje novega projekta.

1. Izvedite naslednje naloge:
   - Vnesite **Ime projekta** (npr. `CoopTranslator-Project`).
   - Izberite **AI hub**  (npr. `CoopTranslator-Hub`) (po potrebi ustvarite novega).

1. Kliknite "**Review and Create**" za nastavitev vašega projekta. Preusmerjeni boste na pregledno stran vašega projekta.

## Nastavitev Azure OpenAI za prevajanje jezikov

Znotraj vašega projekta boste namestili Azure OpenAI model, ki bo služil kot ozadje za prevajanje besedil.

### Pojdite do svojega projekta

Če še niste, odprite vaš novo ustvarjeni projekt (npr. `CoopTranslator-Project`) v Azure AI Foundry.

### Namestitev OpenAI modela

1. V levem meniju vašega projekta, pod "My assets", izberite "**Models + endpoints**".

1. Izberite **+ Deploy model**.

1. Izberite **Deploy Base Model**.

1. Prikazan bo seznam razpoložljivih modelov. Filtrirajte ali poiščite ustrezen GPT model. Priporočamo `gpt-4o`.

1. Izberite želeni model in kliknite **Confirm**.

1. Izberite **Deploy**.

### Konfiguracija Azure OpenAI

Ko je nameščen, lahko na strani "**Models + endpoints**" izberete nameščanje in si ogledate **REST endpoint URL**, **Ključ**, **Ime nameščanja**, **Ime modela** in **Različico API-ja**. Ti podatki so potrebni za integracijo prevajalskega modela v vašo aplikacijo.

> [!NOTE]
> Izberete lahko različice API-ja na strani [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) glede na vaše potrebe. Upoštevajte, da se **različica API-ja** razlikuje od **različice modela**, prikazane na strani **Models + endpoints** v Azure AI Foundry.

## Nastavitev Azure Computer Vision za prevajanje slik

Za omogočanje prevajanja besedila znotraj slik morate pridobiti Azure AI Service API ključ in Endpoint.

1. Pojdite do vašega Azure AI Projekta (npr. `CoopTranslator-Project`). Prepričajte se, da ste na pregledni strani projekta.

### Konfiguracija Azure AI storitve

Pridobite API ključ in Endpoint iz zavihka Azure AI Service.

1. Pojdite do vašega Azure AI Projekta (npr. `CoopTranslator-Project`). Prepričajte se, da ste na pregledni strani projekta.

1. Najdite **API Key** in **Endpoint** v zavihku Azure AI Service.

    ![Najdite API ključ in Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Ta povezava omogoča vašemu AI Foundry projektu uporabo zmogljivosti povezanega vira Azure AI storitev (vključno z analizo slik). Nato lahko to povezavo uporabite v vaših zapiskih ali aplikacijah za izločanje besedila iz slik, ki ga je mogoče poslati Azure OpenAI modelu za prevajanje.

## Konsolidacija vaših poverilnic

Zdaj bi morali imeti zbirko naslednjih podatkov:

**Za Azure OpenAI (prevajanje besedil):**
- Azure OpenAI Endpoint
- Azure OpenAI API ključ
- Ime Azure OpenAI modela (npr. `gpt-4o`)
- Ime Azure OpenAI nameščanja (npr. `cooptranslator-gpt4o`)
- Različica Azure OpenAI API-ja

**Za Azure AI storitve (izvleček besedila iz slik prek Vision):**
- Endpoint Azure AI storitve
- API ključ Azure AI storitve

### Primer: Konfiguracija okoljskih spremenljivk (predogled)

Kasneje, ko boste gradili vašo aplikacijo, jih boste verjetno konfigurirali z uporabo teh zbranih poverilnic. Na primer, lahko jih nastavite kot okoljske spremenljivke na naslednji način:

```bash
# Azure AI službeni podatki (zahtevani za prevajanje slik)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # npr., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Neobvezni nadomestni nizi: podvojite spremenljivke s pripono _1/_2 (isti indeks za vse spremenljivke v nizu)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI službeni podatki (zahtevani za prevajanje besedila)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # npr., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # npr., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # npr., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # npr., 2024-12-01-preview

# Neobvezni nadomestni nizi: podvojite celoten nabor AZURE_OPENAI_* s pripono _1/_2 (isti indeks za vse spremenljivke)
```

---

### Nadaljnje branje

- [Kako ustvariti projekt v Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kako ustvariti Azure AI vire](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kako namestiti OpenAI modele v Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvorni jeziku je treba šteti za avtoritativni vir. Za ključne informacije je priporočljiv strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->