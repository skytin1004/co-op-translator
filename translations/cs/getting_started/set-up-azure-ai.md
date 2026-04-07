# Nastavení Azure AI pro Co-op Translator (Azure OpneAI & Azure AI Vision)

Tento průvodce vás provede nastavením Azure OpenAI pro jazykový překlad a Azure Computer Vision pro analýzu obsahu obrázků (které pak lze použít pro překlad založený na obrázcích) v rámci Azure AI Foundry.

**Požadavky:**
- Účet Azure s aktivním předplatným.
- Dostatečná oprávnění k vytváření zdrojů a implementací ve vašem předplatném Azure.

## Vytvoření projektu Azure AI

Začnete vytvořením projektu Azure AI, který slouží jako centrální místo pro správu vašich AI zdrojů.

1. Přejděte na [https://ai.azure.com](https://ai.azure.com) a přihlaste se pomocí vašeho účtu Azure.

1. Vyberte **+Create** pro vytvoření nového projektu.

1. Proveďte následující úkoly:
   - Zadejte **Jméno projektu** (např. `CoopTranslator-Project`).
   - Vyberte **AI hub**  (např. `CoopTranslator-Hub`) (vytvořte nový, pokud je potřeba).

1. Klikněte na "**Review and Create**" pro nastavení vašeho projektu. Budete přesměrováni na přehledovou stránku vašeho projektu.

## Nastavení Azure OpenAI pro jazykový překlad

V rámci vašeho projektu nasadíte model Azure OpenAI, který bude sloužit jako backend pro překlad textu.

### Navigace do vašeho projektu

Pokud již nejste v projektu, otevřete svůj nově vytvořený projekt (např. `CoopTranslator-Project`) v Azure AI Foundry.

### Nasazení modelu OpenAI

1. V levém menu projektu, pod "My assets", vyberte "**Models + endpoints**".

1. Vyberte **+ Deploy model**.

1. Vyberte **Deploy Base Model**.

1. Zobrazí se seznam dostupných modelů. Filtrovat nebo vyhledejte vhodný GPT model. Doporučujeme `gpt-4o`.

1. Vyberte požadovaný model a klikněte na **Confirm**.

1. Vyberte **Deploy**.

### Konfigurace Azure OpenAI

Po nasazení můžete na stránce "**Models + endpoints**" vybrat implementaci, kde najdete **REST endpoint URL**, **Klíč**, **Jméno implementace**, **Jméno modelu** a **Verzi API**. Tyto údaje budete potřebovat pro integraci překladového modelu do vaší aplikace.

> [!NOTE]
> Verze API můžete vybírat na stránce [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) podle vašich požadavků. Mějte na paměti, že **verze API** se liší od **verze modelu**, která je zobrazena na stránce **Models + endpoints** v Azure AI Foundry.

## Nastavení Azure Computer Vision pro překlad obrázků

Pro povolení překladu textu v obrázcích je potřeba získat Azure AI Service API Key a Endpoint.

1. Přejděte do vašeho projektu Azure AI (např. `CoopTranslator-Project`). Ujistěte se, že jste na přehledové stránce projektu.

### Konfigurace Azure AI Service

Získejte API Key a Endpoint z Azure AI Service.

1. Přejděte do vašeho projektu Azure AI (např. `CoopTranslator-Project`). Ujistěte se, že jste na přehledové stránce projektu.

1. Získejte **API Key** a **Endpoint** z karty Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Toto propojení zpřístupňuje funkce přidruženého zdroje Azure AI Services (včetně analýzy obrázků) ve vašem projektu AI Foundry. Poté můžete toto propojení používat ve svých poznámkových blocích nebo aplikacích k extrakci textu z obrázků, který následně může být odeslán do modelu Azure OpenAI k překladu.

## Konsolidace vašich přihlašovacích údajů

Nyní byste měli mít shromážděné následující údaje:

**Pro Azure OpenAI (překlad textu):**
- Endpoint Azure OpenAI
- API klíč Azure OpenAI
- Jméno modelu Azure OpenAI (např. `gpt-4o`)
- Jméno implementace Azure OpenAI (např. `cooptranslator-gpt4o`)
- Verze API Azure OpenAI

**Pro Azure AI Services (extrakce textu z obrázků přes Vision):**
- Endpoint Azure AI Service
- API klíč Azure AI Service

### Příklad: Konfigurace prostředí proměnných (Preview)

Později při tvorbě vaší aplikace pravděpodobně nastavíte tyto shromážděné údaje jako proměnné prostředí následovně:

```bash
# Azure AI přihlašovací údaje (vyžadováno pro překlad obrázků)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # např., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Volitelné náhradní sady: duplikujte proměnné s příponou _1/_2 (stejné indexy pro všechny proměnné v sadě)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI přihlašovací údaje (vyžadováno pro překlad textu)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # např., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # např., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # např., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # např., 2024-12-01-preview

# Volitelné náhradní sady: duplikujte celou sadu AZURE_OPENAI_* s příponou _1/_2 (stejné indexy pro všechny proměnné)
```

---

### Další čtení

- [Jak vytvořit projekt v Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Jak vytvořit Azure AI zdroje](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Jak nasadit modely OpenAI v Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí služby AI pro překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nezodpovídáme za jakákoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->