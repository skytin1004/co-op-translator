# Vytvorte súbor *.env* v koreňovom adresári

V tomto návode vás prevedieme nastavením vašich environmentálnych premenných pre služby Azure pomocou súboru *.env*. Environmentálne premenné vám umožňujú bezpečne spravovať citlivé prihlasovacie údaje, ako sú kľúče API, bez toho, aby ste ich tvrdo zakódovali do vášho kódu.

> [!IMPORTANT]
> - Je potrebné nakonfigurovať len jednu službu jazykového modelu (Azure OpenAI alebo OpenAI). Vyplňte environmentálne premenné pre preferovanú službu. Ak sú nastavené environmentálne premenné pre viacero jazykových modelov, co-op translator vyberie jeden na základe priority.
> - Ak nie sú nastavené environmentálne premenné pre Computer Vision, prekladateľ sa automaticky prepne do [režimu iba Markdown](./markdown-only-mode.md).

> [!NOTE]
> Tento návod sa zameriava prevažne na služby Azure, ale môžete si vybrať akýkoľvek podporovaný jazykový model zo zoznamu [podporovaných modelov a služieb](../README.md#-supported-models-and-services).

## Vytvorte súbor *.env*

V koreňovom adresári vášho projektu vytvorte súbor s názvom *.env*. Tento súbor bude uchovávať všetky vaše environmentálne premenné v jednoduchom formáte.

> [!WARNING]
> Nesnažte sa commitnúť váš súbor *.env* do systémov na správu verzií, ako je Git. Pridajte *.env* do vášho súboru .gitignore, aby ste predišli nechceným commitom.

1. Prejdite do koreňového adresára vášho projektu.

1. Vytvorte súbor *.env* v koreňovom adresári vášho projektu.

1. Otvorte súbor *.env* a vložte nasledujúcu šablónu:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> Ak chcete nájsť svoje kľúče API a koncové body, môžete sa odvolať na [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, vezmite prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne výklady vzniknuté použitím tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->