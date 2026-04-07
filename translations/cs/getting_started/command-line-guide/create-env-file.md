# Vytvořte soubor *.env* v kořenovém adresáři

V tomto návodu vás provedeme nastavením vašich proměnných prostředí pro služby Azure pomocí souboru *.env*. Proměnné prostředí vám umožňují bezpečně spravovat citlivé přihlašovací údaje, jako jsou klíče API, aniž byste je museli pevně zakódovat do vašeho kódu.

> [!IMPORTANT]
> - Konfigurovat je třeba pouze jednu službu modelu jazyka (Azure OpenAI nebo OpenAI). Vyplňte proměnné prostředí pro preferovanou službu. Pokud jsou nastaveny proměnné prostředí pro více modelů jazyků, co-op translator vybere jeden podle priority.
> - Pokud nejsou nastaveny proměnné prostředí pro Computer Vision, překladač se automaticky přepne do [režimu pouze Markdown](./markdown-only-mode.md).

> [!NOTE]
> Tento průvodce je zaměřen především na služby Azure, ale můžete si vybrat jakýkoli podporovaný model jazyka ze [seznamu podporovaných modelů a služeb](../README.md#-supported-models-and-services).

## Vytvoření souboru *.env*

V kořenovém adresáři vašeho projektu vytvořte soubor nazvaný *.env*. Tento soubor bude uchovávat všechny vaše proměnné prostředí v jednoduchém formátu.

> [!WARNING]
> Soubor *.env* neukládejte do systémů správy verzí, jako je Git. Přidejte *.env* do svého souboru .gitignore, abyste zabránili nechtěným commity.

1. Přejděte do kořenového adresáře vašeho projektu.

1. Vytvořte soubor *.env* v kořenovém adresáři vašeho projektu.

1. Otevřete soubor *.env* a vložte následující šablonu:

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
> Pokud chcete najít své klíče API a koncové body, můžete se podívat do [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neneseme odpovědnost za jakékoliv nedorozumění nebo nesprávné výklady, které mohou vzniknout z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->