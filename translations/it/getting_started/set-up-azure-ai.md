# Configurare Azure AI per Co-op Translator (Azure OpneAI e Azure AI Vision)

Questa guida ti accompagna nella configurazione di Azure OpenAI per la traduzione linguistica e Azure Computer Vision per l'analisi del contenuto delle immagini (che può poi essere utilizzata per la traduzione basata sulle immagini) all'interno di Azure AI Foundry.

**Prerequisiti:**
- Un account Azure con una sottoscrizione attiva.
- Permessi sufficienti per creare risorse e distribuzioni nella tua sottoscrizione Azure.

## Crea un Progetto Azure AI

Inizierai creando un Progetto Azure AI, che funge da punto centrale per gestire le tue risorse AI.

1. Vai su [https://ai.azure.com](https://ai.azure.com) e accedi con il tuo account Azure.

1. Seleziona **+Create** per creare un nuovo progetto.

1. Esegui le seguenti operazioni:
   - Inserisci un **Nome progetto** (es. `CoopTranslator-Project`).
   - Seleziona il **AI hub**  (es. `CoopTranslator-Hub`) (creane uno nuovo se necessario).

1. Clicca su "**Review and Create**" per configurare il tuo progetto. Verrai indirizzato alla pagina panoramica del progetto.

## Configura Azure OpenAI per la Traduzione Linguistica

All'interno del tuo progetto, distribuirai un modello Azure OpenAI che funzionerà come backend per la traduzione del testo.

### Naviga al tuo Progetto

Se non sei già lì, apri il progetto appena creato (es. `CoopTranslator-Project`) in Azure AI Foundry.

### Distribuisci un Modello OpenAI

1. Dal menu a sinistra del tuo progetto, sotto "My assets", seleziona "**Models + endpoints**".

1. Seleziona **+ Deploy model**.

1. Seleziona **Deploy Base Model**.

1. Ti verrà mostrata una lista di modelli disponibili. Filtra o cerca un modello GPT adatto. Consigliamo `gpt-4o`.

1. Seleziona il modello desiderato e clicca su **Confirm**.

1. Seleziona **Deploy**.

### Configurazione Azure OpenAI

Una volta distribuito, puoi selezionare la distribuzione dalla pagina "**Models + endpoints**" per trovare il suo **URL endpoint REST**, **Chiave**, **Nome distribuzione**, **Nome modello** e **Versione API**. Questi saranno necessari per integrare il modello di traduzione nella tua applicazione.

> [!NOTE]
> Puoi selezionare la versione API dalla pagina [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) in base alle tue esigenze. Sappi che la **versione API** è diversa dalla **versione del Modello** mostrata nella pagina **Models + endpoints** in Azure AI Foundry.

## Configura Azure Computer Vision per la Traduzione delle Immagini

Per abilitare la traduzione del testo contenuto nelle immagini, devi trovare la Chiave API e l'Endpoint del servizio Azure AI.

1. Vai al tuo Progetto Azure AI (es. `CoopTranslator-Project`). Assicurati di essere nella pagina panoramica del progetto.

### Configurazione del Servizio Azure AI

Trova la Chiave API e l'Endpoint dal servizio Azure AI.

1. Vai al tuo Progetto Azure AI (es. `CoopTranslator-Project`). Assicurati di essere nella pagina panoramica del progetto.

1. Trova la **Chiave API** e l'**Endpoint** nella scheda del servizio Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Questa connessione rende le capacità della risorsa Azure AI Services collegata (inclusa l'analisi delle immagini) disponibili al tuo progetto AI Foundry. Potrai poi utilizzare questa connessione nei tuoi notebook o applicazioni per estrarre testo dalle immagini, che potrà successivamente essere inviato al modello Azure OpenAI per la traduzione.

## Consolidamento delle tue Credenziali

A questo punto dovresti aver raccolto quanto segue:

**Per Azure OpenAI (Traduzione Testuale):**
- Endpoint Azure OpenAI
- Chiave API Azure OpenAI
- Nome Modello Azure OpenAI (es. `gpt-4o`)
- Nome Distribuzione Azure OpenAI (es. `cooptranslator-gpt4o`)
- Versione API Azure OpenAI

**Per Azure AI Services (Estrazione Testo da Immagini tramite Vision):**
- Endpoint Servizio Azure AI
- Chiave API Servizio Azure AI

### Esempio: Configurazione Variabili d’Ambiente (Anteprima)

Successivamente, durante lo sviluppo della tua applicazione, molto probabilmente la configurerai usando queste credenziali raccolte. Ad esempio, potresti impostarle come variabili d’ambiente così:

```bash
# Credenziali del servizio Azure AI (Richieste per la traduzione delle immagini)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # es., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Set di riserva opzionali: duplicare le variabili con il suffisso _1/_2 (stesso indice per tutte le variabili del set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Credenziali Azure OpenAI (Richieste per la traduzione del testo)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # es., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # es., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # es., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # es., 2024-12-01-preview

# Set di riserva opzionali: duplicare l'intero set AZURE_OPENAI_* con suffisso _1/_2 (stesso indice per tutte le variabili)
```

---

### Letture Consigliate

- [Come creare un progetto in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Come creare risorse Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Come distribuire modelli OpenAI in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Esclusione di responsabilità**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->