# Azure AI seadistamine Co-op Translatori jaoks (Azure OpneAI & Azure AI Vision)

See juhend viib teid läbi Azure OpenAI seadistamise keele tõlkimiseks ja Azure Computer Visioni seadistamise pildisisu analüüsiks (mida saab seejärel kasutada pildi põhjal tõlkimiseks) Azure AI Foundrys.

**Eeltingimused:**
- Azure konto aktiivse tellimusega.
- Piisavad õigused ressursside ja juurutuste loomiseks oma Azure tellimuses.

## Loo Azure AI projekt

Alustage Azure AI projekti loomisega, mis toimib keskse halduskohana teie AI ressursside jaoks.

1. Minge aadressile [https://ai.azure.com](https://ai.azure.com) ja logige sisse oma Azure kontoga.

1. Valige **+Create**, et luua uus projekt.

1. Tehke järgmised toimingud:
   - Sisestage **projekti nimi** (nt `CoopTranslator-Project`).
   - Valige **AI keskust** (nt `CoopTranslator-Hub`) (loo vajadusel uus).

1. Klõpsake "**Review and Create**", et projekt seadistada. Te suunatakse oma projekti ülevaate lehele.

## Azure OpenAI seadistamine keele tõlkimiseks

Sisemiselt projektis juurutate Azure OpenAI mudeli, mis toimib teksti tõlkimise taustsüsteemina.

### Mine oma projekti

Kui pole veel oma uude loodud projekti (nt `CoopTranslator-Project`) Azure AI Foundrys avatud, avage see nüüd.

### OpenAI mudeli juurutamine

1. Oma projekti vasakpoolsest menüüst valige jaotisest "My assets" "**Models + endpoints**".

1. Valige **+ Deploy model**.

1. Valige **Deploy Base Model**.

1. Teile kuvatakse saadaolevate mudelite nimekiri. Filtreerige või otsige sobivat GPT mudelit. Soovitame `gpt-4o`.

1. Valige soovitud mudel ja klõpsake **Confirm**.

1. Valige **Deploy**.

### Azure OpenAI konfiguratsioon

Pärast juurutamist saate valida juurutuse lehelt "**Models + endpoints**", et leida selle **REST endpoint URL**, **Key**, **Juurutuse nimi**, **Mudeli nimi** ja **API versioon**. Neid on vaja tõlkemudeli integreerimiseks teie rakendusse.

> [!NOTE]
> API versioone saate valida vastavalt oma vajadustele lehelt [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation). Olge teadlik, et **API versioon** erineb **Mudeli versioonist**, mis kuvatakse Azure AI Foundry lehel **Models + endpoints**.

## Azure Computer Visioni seadistamine pilditõlkeks

Teksti tõlkimise võimaldamiseks piltidel peate leidma Azure AI Service API Key ja Endpoint.

1. Minge oma Azure AI projekti (nt `CoopTranslator-Project`). Veenduge, et olete projekti ülevaatelehel.

### Azure AI Service konfiguratsioon

Leidke Azure AI Service kaardilt API Key ja Endpoint.

1. Minge oma Azure AI projekti (nt `CoopTranslator-Project`). Veenduge, et olete projekti ülevaatelehel.

1. Leidke Azure AI Service vahekaardilt **API Key** ja **Endpoint**.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

See ühendus võimaldab seotud Azure AI Services ressursi (sealhulgas pildi analüüsimise) võimekust kasutada teie AI Foundry projektis. Seejärel saate seda ühendust kasutada oma märkmikes või rakendustes tekstide eraldamiseks piltidelt, mis saab seejärel saata Azure OpenAI mudelile tõlkimiseks.

## Oma volituste koondamine

Seni peaksite olema kogunud järgmised andmed:

**Azure OpenAI jaoks (teksti tõlkimiseks):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI mudeli nimi (nt `gpt-4o`)
- Azure OpenAI juurutuse nimi (nt `cooptranslator-gpt4o`)
- Azure OpenAI API versioon

**Azure AI teenuste jaoks (teksti eraldamiseks piltidelt Visioni kaudu):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Näide: keskkonnamuutuja konfiguratsioon (eelvaade)

Hiljem, kui hakkate oma rakendust ehitama, tõenäoliselt seadistate seda nende kogutud volitustega. Näiteks võite need määrata keskkonnamuutujatena järgmiselt:

```bash
# Azure AI teenuse mandaadid (nõutud pilditõlke jaoks)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # nt 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Valikulised varuvõimalused: dubleeri muutujad sufiksiga _1/_2 (kõikide komplekti muutujate sama indeks)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI mandaadid (nõutud tekstide tõlkimiseks)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # nt 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # nt gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # nt cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # nt 2024-12-01-preview

# Valikulised varuvõimalused: dubleeri kogu AZURE_OPENAI_* komplekt sufiksiga _1/_2 (kõikide muutujate sama indeks)
```

---

### Täiendav lugemine

- [Kuidas luua projekt Azure AI Foundrys](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kuidas luua Azure AI ressursse](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kuidas juurutada OpenAI mudeleid Azure AI Foundrys](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud AI-tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüdleme täpsuse poole, tuleks arvestada, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->