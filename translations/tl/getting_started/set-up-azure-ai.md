# Itakda ang Azure AI para sa Co-op Translator (Azure OpneAI & Azure AI Vision)

Ang gabay na ito ay naglalakad sa iyo sa pag-set up ng Azure OpenAI para sa pagsasalin ng wika at Azure Computer Vision para sa pagsusuri ng nilalaman ng imahe (na maaaring magamit para sa pagsasaling batay sa imahe) sa loob ng Azure AI Foundry.

**Mga Kinakailangan:**
- Isang Azure account na may aktibong subscription.
- Sapat na mga pahintulot upang lumikha ng mga resources at deployment sa iyong Azure subscription.

## Lumikha ng Azure AI Project

Magsisimula ka sa pamamagitan ng paglikha ng Azure AI Project, na nagsisilbing sentrong lugar para sa pamamahala ng iyong mga AI resources.

1. Pumunta sa [https://ai.azure.com](https://ai.azure.com) at mag-sign in gamit ang iyong Azure account.

1. Piliin ang **+Create** upang lumikha ng bagong proyekto.

1. Gawin ang mga sumusunod na hakbang:
   - Ilagay ang **Project name** (hal. `CoopTranslator-Project`).
   - Piliin ang **AI hub** (hal. `CoopTranslator-Hub`) (Lumikha ng bago kung kinakailangan).

1. I-click ang "**Review and Create**" upang itakda ang iyong proyekto. Dadalhin ka sa overview page ng iyong proyekto.

## Itakda ang Azure OpenAI para sa Pagsasalin ng Wika

Sa loob ng iyong proyekto, magde-deploy ka ng Azure OpenAI model na magsisilbing backend para sa pagsasalin ng teksto.

### Pumunta sa Iyong Proyekto

Kung hindi ka pa naroroon, buksan ang bagong likha mong proyekto (hal. `CoopTranslator-Project`) sa Azure AI Foundry.

### Mag-deploy ng OpenAI Model

1. Mula sa kaliwang menu ng iyong proyekto, sa ilalim ng "My assets", piliin ang "**Models + endpoints**".

1. Piliin ang **+ Deploy model**.

1. Piliin ang **Deploy Base Model**.

1. Ipapakita sa iyo ang listahan ng mga available na modelo. I-filter o hanapin ang angkop na GPT model. Inirerekomenda namin ang `gpt-4o`.

1. Piliin ang nais mong modelo at i-click ang **Confirm**.

1. Piliin ang **Deploy**.

### Konfigurasyon ng Azure OpenAI

Kapag na-deploy na, maaari mong piliin ang deployment mula sa page na "**Models + endpoints**" para makita ang **REST endpoint URL**, **Key**, **Deployment name**, **Model name** at **API version** nito. Kakailanganin ang mga ito upang isama ang translation model sa iyong aplikasyon.

> [!NOTE]
> Maaari kang pumili ng API versions mula sa [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) na pahina base sa iyong mga pangangailangan. Tandaan na ang **API version** ay iba sa **Model version** na ipinapakita sa page na **Models + endpoints** sa Azure AI Foundry.

## Itakda ang Azure Computer Vision para sa Pagsasalin ng Imahe

Para mapagana ang pagsasalin ng teksto sa loob ng mga imahe, kailangan mong hanapin ang Azure AI Service API Key at Endpoint.

1. Pumunta sa iyong Azure AI Project (hal. `CoopTranslator-Project`). Siguraduhing nasa project overview page ka.

### Konfigurasyon ng Azure AI Service

Hanapin ang API Key at Endpoint mula sa Azure AI Service.

1. Pumunta sa iyong Azure AI Project (hal. `CoopTranslator-Project`). Siguraduhing nasa project overview page ka.

1. Hanapin ang **API Key** at **Endpoint** mula sa Azure AI Service tab.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Ginagawa nitong available sa iyong AI Foundry project ang kakayahan ng naka-link na Azure AI Services resource (kabilang ang pagsusuri ng imahe). Maaari mo itong gamitin sa iyong mga notebook o aplikasyon upang kumuha ng teksto mula sa mga imahe, na maaari naman ipadala sa Azure OpenAI model para sa pagsasalin.

## Pagsasama-sama ng Iyong Mga Kredensyal

Sa puntong ito, dapat ay nakalap mo na ang mga sumusunod:

**Para sa Azure OpenAI (Pagsasalin ng Teksto):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (hal. `gpt-4o`)
- Azure OpenAI Deployment Name (hal. `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Para sa Azure AI Services (Pagkuha ng Teksto mula sa Imahe gamit ang Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Halimbawa: Pagkonfigura ng Environment Variable (Preview)

Sa susunod, kapag bumubuo ka ng iyong aplikasyon, malamang na iko-configure mo ito gamit ang mga nakalap mong kredensyal. Halimbawa, maaari mo silang itakda bilang mga environment variable nang ganito:

```bash
# Mga Kredensyal ng Azure AI Service (Kailangan para sa pagsasalin ng larawan)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # hal., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Mga opsyonal na fallback na set: kopyahin ang mga variable na may suffix na _1/_2 (parehong index para sa lahat ng variable sa set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Mga Kredensyal ng Azure OpenAI (Kailangan para sa pagsasalin ng teksto)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # hal., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # hal., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # hal., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # hal., 2024-12-01-preview

# Mga opsyonal na fallback na set: kopyahin ang buong AZURE_OPENAI_* set na may suffix na _1/_2 (parehong index para sa lahat ng variable)
```

---

### Karagdagang Babasahin

- [Paano Lumikha ng proyekto sa Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Paano Lumikha ng Azure AI resources](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Paano Mag-deploy ng OpenAI models sa Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat aming nilalayon ang katumpakan, mangyaring tandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->