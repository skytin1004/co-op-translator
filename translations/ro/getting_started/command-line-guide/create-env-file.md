# Creează fișierul *.env* în directorul rădăcină

În acest tutorial, te vom ghida prin configurarea variabilelor de mediu pentru serviciile Azure folosind un fișier *.env*. Variabilele de mediu îți permit să gestionezi în siguranță acreditările sensibile, cum ar fi cheile API, fără a le include direct în codul tău.

> [!IMPORTANT]
> - Doar un singur serviciu de model lingvistic (Azure OpenAI sau OpenAI) trebuie configurat. Completează variabilele de mediu pentru serviciul preferat. Dacă variabilele de mediu pentru mai multe modele lingvistice sunt setate, translatorul co-op va selecta unul pe baza priorității.
> - Dacă variabilele de mediu pentru Computer Vision nu sunt setate, translatorul va comuta automat în [modul doar Markdown](./markdown-only-mode.md).

> [!NOTE]
> Acest ghid se concentrează în principal pe serviciile Azure, dar poți alege orice model lingvistic suportat din [lista modelelor și serviciilor suportate](../README.md#-supported-models-and-services).

## Creează fișierul *.env*

În directorul rădăcină al proiectului tău, creează un fișier numit *.env*. Acest fișier va stoca toate variabilele tale de mediu într-un format simplu.

> [!WARNING]
> Nu adăuga fișierul *.env* în sistemele de control al versiunilor, cum ar fi Git. Adaugă *.env* în fișierul tău .gitignore pentru a preveni commit-urile accidentale.

1. Navighează către directorul rădăcină al proiectului tău.

1. Creează un fișier *.env* în directorul rădăcină al proiectului tău.

1. Deschide fișierul *.env* și lipește următorul șablon:

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
> Dacă vrei să găsești cheile API și punctele finale, poți consulta [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertisment**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->