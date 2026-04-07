# Nastavenie Azure AI pre Co-op Translator (Azure OpneAI a Azure AI Vision)

Tento návod vás prevedie nastavením Azure OpenAI pre preklad jazykov a Azure Computer Vision pre analýzu obsahu obrázkov (ktoré sa potom môžu použiť na preklad na základe obrázkov) v rámci Azure AI Foundry.

**Požiadavky:**
- Účet Azure s aktívnym predplatným.
- Dostatočné povolenia na vytváranie zdrojov a nasadení vo vašom Azure predplatnom.

## Vytvorenie Azure AI projektu

Začnete vytvorením Azure AI projektu, ktorý slúži ako centrálny bod na správu vašich AI zdrojov.

1. Prejdite na [https://ai.azure.com](https://ai.azure.com) a prihláste sa so svojim Azure účtom.

1. Vyberte **+Create** pre vytvorenie nového projektu.

1. Vykonajte nasledujúce kroky:
   - Zadajte **Názov projektu** (napr. `CoopTranslator-Project`).
   - Vyberte **AI hub** (napr. `CoopTranslator-Hub`) (v prípade potreby vytvorte nový).

1. Kliknite na "**Review and Create**" pre nastavenie projektu. Budete presmerovaní na prehľadovú stránku svojho projektu.

## Nastavenie Azure OpenAI pre preklad jazyka

Vo vašom projekte nasadíte model Azure OpenAI, ktorý bude slúžiť ako backend pre preklad textu.

### Prejdite do svojho projektu

Ak ešte nie ste v ňom, otvorte svoj novo vytvorený projekt (napr. `CoopTranslator-Project`) v Azure AI Foundry.

### Nasadenie OpenAI modelu

1. V ľavom menu projektu, pod "My assets", vyberte "**Models + endpoints**".

1. Vyberte **+ Deploy model**.

1. Vyberte **Deploy Base Model**.

1. Zobrazí sa vám zoznam dostupných modelov. Filtrovať alebo vyhľadať vhodný GPT model. Odporúčame `gpt-4o`.

1. Vyberte požadovaný model a kliknite na **Confirm**.

1. Vyberte **Deploy**.

### Konfigurácia Azure OpenAI

Po nasadení môžete vybrať nasadenie na stránke "**Models + endpoints**" a nájsť jeho **REST endpoint URL**, **Kľúč**, **Názov nasadenia**, **Názov modelu** a **Verziu API**. Tieto údaje budete potrebovať na integráciu prekladového modelu do vašej aplikácie.

> [!NOTE]
> API verzie si môžete vybrať na stránke [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) podľa vašich požiadaviek. Majte na pamäti, že **verzia API** sa líši od **verzie modelu** zobrazenej na stránke **Models + endpoints** v Azure AI Foundry.

## Nastavenie Azure Computer Vision pre preklad obrázkov

Na umožnenie prekladu textu v obrázkoch je potrebné získať API kľúč a endpoint Azure AI Service.

1. Prejdite do svojho Azure AI projektu (napr. `CoopTranslator-Project`). Uistite sa, že ste na prehľadovej stránke projektu.

### Konfigurácia Azure AI služby

Nájdite API kľúč a endpoint z Azure AI Service.

1. Prejdite do svojho Azure AI projektu (napr. `CoopTranslator-Project`). Uistite sa, že ste na prehľadovej stránke projektu.

1. Nájdite **API Key** a **Endpoint** na záložke Azure AI Service.

    ![Nájdite API Key a Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Toto prepojenie sprístupňuje schopnosti prepojeného zdroja Azure AI Services (vrátane analýzy obrázkov) vo vašom AI Foundry projekte. Túto konekciu potom môžete použiť vo svojich notebookoch alebo aplikáciách na extrakciu textu z obrázkov, ktorý sa následne môže odoslať na Azure OpenAI model na preklad.

## Konsolidácia vašich prihlasovacích údajov

V tomto kroku by ste mali mať nasledovné údaje:

**Pre Azure OpenAI (preklad textu):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Názov modelu Azure OpenAI (napr. `gpt-4o`)
- Názov nasadenia Azure OpenAI (napr. `cooptranslator-gpt4o`)
- Verzia API Azure OpenAI

**Pre Azure AI Services (extrakcia textu z obrázkov cez Vision):**
- Endpoint Azure AI Service
- API Key Azure AI Service

### Príklad: Konfigurácia premenných prostredia (náhľad)

Neskôr pri vývoji vašej aplikácie pravdepodobne tieto zozbierané kredenciály nastavíte ako premenné prostredia napríklad takto:

```bash
# Azure AI prihlasovacie údaje (povinné pre preklad obrázkov)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # napr., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Nepovinné náhradné sady: duplikujte premenné s príponou _1/_2 (rovnaký index pre všetky premenné v sade)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI prihlasovacie údaje (povinné pre preklad textu)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # napr., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # napr., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # napr., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # napr., 2024-12-01-preview

# Nepovinné náhradné sady: duplikujte celú sadu AZURE_OPENAI_* s príponou _1/_2 (rovnaký index pre všetky premenné)
```

---

### Ďalšie čítanie

- [Ako vytvoriť projekt v Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Ako vytvoriť Azure AI zdroje](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Ako nasadiť OpenAI modely v Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o odmietnutí zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím vezmite na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->