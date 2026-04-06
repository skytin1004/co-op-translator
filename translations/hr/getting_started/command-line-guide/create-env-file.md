# Kreirajte datoteku *.env* u korijenskom direktoriju

U ovom vodiču ćemo vas provesti kroz postavljanje vaših varijabli okoline za Azure usluge koristeći datoteku *.env*. Varijable okoline omogućuju vam sigurno upravljanje osjetljivim vjerodajnicama, poput API ključeva, bez njihovog ugrađivanja u vaš kod.

> [!IMPORTANT]
> - Potrebno je konfigurirati samo jednu uslugu modela jezika (Azure OpenAI ili OpenAI). Ispunite varijable okoline za željenu uslugu. Ako su varijable okoline postavljene za više modela jezika, co-op translator će odabrati jedan prema prioritetu.
> - Ako varijable okoline za Computer Vision nisu postavljene, prevoditelj će se automatski prebaciti u [Markdown-samo način rada](./markdown-only-mode.md).

> [!NOTE]
> Ovaj vodič se prvenstveno fokusira na Azure usluge, ali možete odabrati bilo koji podržani model jezika sa [popisa podržanih modela i usluga](../README.md#-supported-models-and-services).

## Kreirajte datoteku *.env*

U korijenskom direktoriju vašeg projekta, kreirajte datoteku nazvanu *.env*. Ova datoteka će spremati sve vaše varijable okoline u jednostavnom formatu.

> [!WARNING]
> Nemojte izvršiti commit vaše *.env* datoteke u sustave za kontrolu verzija poput Gita. Dodajte *.env* u vašu .gitignore datoteku kako biste spriječili slučajne commitove.

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
> Ako želite pronaći vaše API ključeve i krajnje točke, možete pogledati [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, molimo imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku smatra se službenim i autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili kriva tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->