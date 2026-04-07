# Azure AI nustatymas Co-op Translator (Azure OpneAI & Azure AI Vision)

Šiame vadove pateikiama, kaip nustatyti Azure OpenAI kalbų vertimui ir Azure Computer Vision vaizdų turinio analizei (kuria vėliau galima naudoti vaizdų pagrindu atliekamam vertimui) Azure AI Foundry aplinkoje.

**Reikalavimai:**
- Azure paskyra su aktyvia prenumerata.
- Pakankamos teisės kurti išteklius ir diegimus jūsų Azure prenumeratoje.

## Sukurkite Azure AI projektą

Pradėsite nuo Azure AI projekto kūrimo, kuris bus centrinė vieta jūsų AI išteklių valdymui.

1. Eikite į [https://ai.azure.com](https://ai.azure.com) ir prisijunkite savo Azure paskyra.

1. Pasirinkite **+Create**, kad sukurtumėte naują projektą.

1. Atlikite šiuos veiksmus:
   - Įveskite **Projekto pavadinimą** (pvz., `CoopTranslator-Project`).
   - Pasirinkite **AI hub** (pvz., `CoopTranslator-Hub`) (jei reikia, sukurkite naują).

1. Spustelėkite "**Review and Create**", kad sukurtumėte projektą. Būsite nukreipti į savo projekto apžvalgos puslapį.

## Azure OpenAI nustatymas kalbų vertimui

Jūsų projekte diegsite Azure OpenAI modelį, kuris tarnaus kaip teksto vertimo paslauga.

### Eikite į savo projektą

Jei dar nesate, atidarykite ką tik sukurtą projektą (pvz., `CoopTranslator-Project`) Azure AI Foundry.

### Diegti OpenAI modelį

1. Iš kairiojo projekto meniu, skiltyje "My assets", pasirinkite "**Models + endpoints**".

1. Paspauskite **+ Deploy model**.

1. Pasirinkite **Deploy Base Model**.

1. Pasirodys sąrašas galimų modelių. Filtruokite arba ieškokite tinkamo GPT modelio. Rekomenduojame `gpt-4o`.

1. Pasirinkite norimą modelį ir spustelėkite **Confirm**.

1. Pasirinkite **Deploy**.

### Azure OpenAI konfigūracija

Įdiegus modelį, galite pasirinkti diegimą iš "**Models + endpoints**" puslapio ir rasti jo **REST endpoint URL**, **Key**, **Diegimo pavadinimą**, **Modelio pavadinimą** ir **API versiją**. Šie duomenys reikalingi vertimo modelio integravimui į jūsų aplikaciją.

> [!NOTE]
> API versijas galite rinktis pagal savo poreikius iš [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) puslapio. Atminkite, kad **API versija** skiriasi nuo **Modelio versijos**, parodytos "**Models + endpoints**" puslapyje Azure AI Foundry.

## Azure Computer Vision nustatymas vaizdų vertimui

Norėdami leisti vertimą iš vaizduose esančio teksto, turite rasti Azure AI Service API raktą ir galinį tašką (endpoint).

1. Eikite į savo Azure AI projektą (pvz., `CoopTranslator-Project`). Įsitikinkite, kad esate projekto apžvalgos puslapyje.

### Azure AI Service konfigūracija

Raskite API raktą ir Galinį tašką iš Azure AI Service.

1. Eikite į savo Azure AI Projektą (pvz., `CoopTranslator-Project`). Įsitikinkite, kad esate projekto apžvalgos puslapyje.

1. Raskite **API Key** ir **Endpoint** Azure AI Service skiltyje.

    ![Raskite API Key ir Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Šis ryšys suteikia jūsų AI Foundry projektui prieigą prie susieto Azure AI Services ištekliaus galimybių (įskaitant vaizdų analizę). Vėliau galite naudoti šį ryšį savo užrašų knygelėse ar programose, kad ištrauktumėte tekstą iš vaizdų ir perduotumėte jį Azure OpenAI modeliui vertimui.

## Jūsų paskyrų duomenų suvienodinimas

Šiuo metu turėtumėte turėti šią informaciją:

**Azure OpenAI (teksto vertimui):**
- Azure OpenAI galinis taškas (Endpoint)
- Azure OpenAI API raktas
- Azure OpenAI modelio pavadinimas (pvz., `gpt-4o`)
- Azure OpenAI diegimo pavadinimas (pvz., `cooptranslator-gpt4o`)
- Azure OpenAI API versija

**Azure AI Services (vaizdų teksto ištraukimas per Vision):**
- Azure AI Service galinis taškas (Endpoint)
- Azure AI Service API raktas

### Pavyzdys: Aplinkos kintamųjų konfigūracija (Peržiūra)

Vėliau, kūrimo metu, greičiausiai konfigūruosite savo aplikaciją naudodami surinktus duomenis. Pavyzdžiui, galite juos nustatyti kaip aplinkos kintamuosius taip:

```bash
# Azure AI paslaugų kredencialai (reikalinga vaizdų vertimui)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # pvz., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Pasirinktiniai atsarginiai rinkiniai: sudublikavus kintamuosius su priesaga _1/_2 (tas pats indeksas visiems rinkinio kintamiesiems)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI kredencialai (reikalinga tekstų vertimui)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # pvz., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # pvz., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # pvz., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # pvz., 2024-12-01-preview

# Pasirinktiniai atsarginiai rinkiniai: sudublikavus visą AZURE_OPENAI_* rinkinį su priesaga _1/_2 (tas pats indeksas visiems kintamiesiems)
```

---

### Tolimesnė literatūra

- [Kaip sukurti projektą Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Kaip sukurti Azure AI išteklius](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Kaip diegti OpenAI modelius Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, atkreipkite dėmesį, kad automatizuotos vertimų paslaugos gali turėti klaidų arba netikslumų. Pradinė dokumento versija gimtąja kalba laikoma autoritetingu šaltiniu. Svarbiai informacijai rekomenduojame naudoti profesionalų žmogaus vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingas interpretacijas, kilusias naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->