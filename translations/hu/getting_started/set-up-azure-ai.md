# Azure AI beállítása a Co-op Translatorhoz (Azure OpneAI és Azure AI Vision)

Ez az útmutató végigvezet az Azure OpenAI nyelvi fordításhoz és az Azure Computer Vision képtartalom elemzéshez (amit később képalapú fordításra lehet használni) Azure AI Foundry-n belül történő beállításán.

**Előkészületek:**
- Egy aktív előfizetéssel rendelkező Azure fiók.
- Megfelelő jogosultságok az erőforrások és telepítések létrehozásához az Azure előfizetésben.

## Azure AI projekt létrehozása

Az Azure AI projekt létrehozásával kezded, amely központi helyként szolgál az AI erőforrásaid kezelésére.

1. Lépj a [https://ai.azure.com](https://ai.azure.com) oldalra és jelentkezz be az Azure fiókodba.

1. Válaszd a **+Create** lehetőséget egy új projekt létrehozásához.

1. Teljesítsd a következő feladatokat:
   - Írj be egy **Project name**-t (pl. `CoopTranslator-Project`).
   - Válaszd ki az **AI hub**-ot (pl. `CoopTranslator-Hub`) (Ha szükséges, hozz létre újat).

1. Kattints a "**Review and Create**" gombra a projekt létrehozásához. Ezt követően a projekt áttekintő oldalára jutsz.

## Azure OpenAI beállítása nyelvi fordításhoz

A projektben egy Azure OpenAI modellt telepítesz, amely a szövegfordítás backendjeként fog szolgálni.

### Navigálj a projektedhez

Ha még nem vagy ott, nyisd meg az újonnan létrehozott projektedet (pl. `CoopTranslator-Project`) az Azure AI Foundry-ban.

### OpenAI modell telepítése

1. A projekted bal oldali menüjében, a "My assets" alatt válaszd a "**Models + endpoints**" lehetőséget.

1. Válaszd a **+ Deploy model**-t.

1. Válaszd a **Deploy Base Model** opciót.

1. Ekkor megjelenik a rendelkezésre álló modellek listája. Szűrj vagy keress egy megfelelő GPT modellt. Ajánljuk a `gpt-4o` modellt.

1. Válaszd ki a kívánt modellt, majd kattints a **Confirm** gombra.

1. Válaszd a **Deploy**-ot.

### Azure OpenAI konfiguráció

A telepítést követően az "**Models + endpoints**" oldalon kiválaszthatod a telepítést, ahol megtalálod a **REST endpoint URL**-jét, a **Kulcsot** (Key), a **Telepítés nevét** (Deployment name), a **Modell nevét** és az **API verziót**. Ezekre lesz szükséged a fordító modell alkalmazásba való integrálásához.

> [!NOTE]
> Az API verziókat az [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) oldalon választhatod az igényeidnek megfelelően. Légy tudatában, hogy az **API verzió** különbözik a **Modell verziótól**, amely az Azure AI Foundry "**Models + endpoints**" oldalán látható.

## Azure Computer Vision beállítása képfelirat fordításhoz

Ahhoz, hogy az képeken belüli szöveget fordítani tudd, meg kell szerezned az Azure AI Service API kulcsát és végpontját.

1. Navigálj az Azure AI Projektedhez (pl. `CoopTranslator-Project`). Győződj meg róla, hogy a projekt áttekintő oldalán vagy.

### Azure AI Service konfiguráció

Szerezd meg az Azure AI Service API kulcsát és végpontját.

1. Navigálj az Azure AI Projektedhez (pl. `CoopTranslator-Project`). Figyelj rá, hogy a projekt áttekintő oldalán tartózkodj.

1. Keresd meg az **API Key**-t és az **Endpoint**-ot az Azure AI Service fül alatt.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Ez a kapcsolat lehetővé teszi, hogy a kapcsolt Azure AI Services erőforrás képességei (beleértve a képelemzést is) elérhetők legyenek az AI Foundry projekted számára. Ezt követően ezt a kapcsolatot használhatod jegyzetfüzeteidben vagy alkalmazásaidban, hogy kivonj szöveget képekből, melyeket aztán az Azure OpenAI modellnek küldhetsz el fordítás céljából.

## Hitelesítő adatok összesítése

Eddigre a következő adatokat kell összegyűjtened:

**Azure OpenAI (szövegfordításhoz):**
- Azure OpenAI végpont
- Azure OpenAI API kulcs
- Azure OpenAI modellnév (pl. `gpt-4o`)
- Azure OpenAI telepítés neve (pl. `cooptranslator-gpt4o`)
- Azure OpenAI API verzió

**Azure AI Services (képszöveg kinyerés Vision segítségével):**
- Azure AI Service végpont
- Azure AI Service API kulcs

### Példa: Környezeti változó konfiguráció (Előzetes)

Amikor később az alkalmazást építed, valószínűleg ezeket a hitelesítő adatokat környezeti változókként fogod beállítani így:

```bash
# Azure AI szolgáltatás hitelesítő adatok (kötelező képfordításhoz)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # pl. 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Opcionális tartalék készletek: duplikált változók _1/_2 utótaggal (ugyanaz az index az összes változóhoz a készletben)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI hitelesítő adatok (kötelező szövegfordításhoz)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # pl. 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # pl. gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # pl. cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # pl. 2024-12-01-preview

# Opcionális tartalék készletek: duplikáld a teljes AZURE_OPENAI_* készletet _1/_2 utótaggal (ugyanaz az index az összes változóhoz)
```

---

### További olvasnivaló

- [Hogyan hozzunk létre projektet Azure AI Foundry-ban](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Hogyan hozzunk létre Azure AI erőforrásokat](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Hogyan telepítsünk OpenAI modelleket Azure AI Foundry-ban](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti, anyanyelvi dokumentum tekinthető a hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítás ajánlott. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->