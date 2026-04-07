# Crea il file *.env* nella directory radice

In questo tutorial, ti guideremo nella configurazione delle variabili d'ambiente per i servizi Azure utilizzando un file *.env*. Le variabili d'ambiente ti permettono di gestire in modo sicuro le credenziali sensibili, come le chiavi API, senza inserirle direttamente nel tuo codice.

> [!IMPORTANT]
> - Deve essere configurato solo un servizio di modello linguistico (Azure OpenAI o OpenAI). Compila le variabili d'ambiente per il servizio che preferisci. Se vengono impostate variabili d'ambiente per più modelli linguistici, il co-op translator ne selezionerà uno in base alla priorità.
> - Se le variabili d'ambiente di Computer Vision non sono impostate, il traduttore passerà automaticamente alla [modalità solo Markdown](./markdown-only-mode.md).

> [!NOTE]
> Questa guida si concentra principalmente sui servizi Azure, ma puoi scegliere qualsiasi modello linguistico supportato dalla [lista di modelli e servizi supportati](../README.md#-supported-models-and-services).

## Crea il file *.env*

Nella directory radice del tuo progetto, crea un file chiamato *.env*. Questo file conterrà tutte le tue variabili d'ambiente in un formato semplice.

> [!WARNING]
> Non commettere il file *.env* nei sistemi di controllo versione come Git. Aggiungi *.env* al tuo file .gitignore per evitare commit accidentali.

1. Vai nella directory radice del tuo progetto.

1. Crea un file *.env* nella directory radice del tuo progetto.

1. Apri il file *.env* e incolla il seguente modello:

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
> Se vuoi trovare le tue chiavi API e gli endpoint, puoi fare riferimento a [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->