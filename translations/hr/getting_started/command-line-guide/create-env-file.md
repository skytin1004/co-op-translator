# Kreirajte *.env* datoteku u korijenskom direktoriju

U ovom vodiču ćemo vas provesti kroz postavljanje vaših varijabli okoline za Azure usluge koristeći *.env* datoteku. Varijable okoline omogućuju vam sigurno upravljanje osjetljivim vjerodajnicama, poput API ključeva, bez da ih unosite direktno u vaš kod.

> [!IMPORTANT]
> - Potrebno je konfigurirati samo jednu uslugu jezičnog modela (Azure OpenAI ili OpenAI). Ispunite varijable okoline za vašu preferiranu uslugu. Ako su varijable okoline postavljene za više jezičnih modela, co-op translator će odabrati jedan na temelju prioriteta.
> - Ako varijable okoline za Computer Vision nisu postavljene, prevoditelj će se automatski prebaciti u [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Ovaj vodič se prvenstveno fokusira na Azure usluge, ali možete odabrati bilo koji podržani jezični model s popisa [supported models and services](../README.md#-supported-models-and-services).

## Kreirajte *.env* datoteku

U korijenskom direktoriju vašeg projekta, kreirajte datoteku pod nazivom *.env*. Ova datoteka će pohraniti sve vaše varijable okoline u jednostavnom formatu.

> [!WARNING]
> Nemojte slati vašu *.env* datoteku u sustave za kontrolu verzija poput Gita. Dodajte *.env* u vašu .gitignore datoteku kako biste spriječili slučajne commitove.

1. Navigirajte do korijenskog direktorija vašeg projekta.

1. Kreirajte *.env* datoteku u korijenskom direktoriju vašeg projekta.

1. Otvorite *.env* datoteku i zalijepite sljedeći predložak:

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
> Ako želite pronaći vaše API ključeve i završne točke, možete se referirati na [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj je dokument preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešne tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->