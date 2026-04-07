# Configurarea Azure AI pentru Co-op Translator (Azure OpneAI & Azure AI Vision)

Acest ghid te va conduce pas cu pas prin configurarea Azure OpenAI pentru traducerea limbajului și Azure Computer Vision pentru analiza conținutului imaginilor (care poate fi apoi folosită pentru traducerea bazată pe imagini) în cadrul Azure AI Foundry.

**Precondiții:**
- Un cont Azure cu un abonament activ.
- Permisiuni suficiente pentru a crea resurse și implementări în abonamentul tău Azure.

## Crearea unui Proiect Azure AI

Veți începe prin crearea unui Proiect Azure AI, care servește ca un punct central pentru gestionarea resurselor AI.

1. Navighează la [https://ai.azure.com](https://ai.azure.com) și autentifică-te cu contul tău Azure.

1. Selectează **+Create** pentru a crea un proiect nou.

1. Efectuează următoarele sarcini:
   - Introdu un **Nume proiect** (de ex., `CoopTranslator-Project`).
   - Selectează **AI hub** (de ex., `CoopTranslator-Hub`) (creează unul nou dacă este necesar).

1. Apasă pe "**Review and Create**" pentru a configura proiectul. Vei fi dus la pagina de prezentare generală a proiectului.

## Configurarea Azure OpenAI pentru traducerea limbajului

În cadrul proiectului tău, vei implementa un model Azure OpenAI pentru a servi ca backend pentru traducerea textului.

### Navigarea către Proiectul tău

Dacă nu ești deja acolo, deschide noul tău proiect creat (de ex., `CoopTranslator-Project`) în Azure AI Foundry.

### Implementarea unui model OpenAI

1. Din meniul din stânga al proiectului, sub "My assets", selectează "**Models + endpoints**".

1. Selectează **+ Deploy model**.

1. Selectează **Deploy Base Model**.

1. Ți se va afișa o listă a modelelor disponibile. Filtrează sau caută un model GPT potrivit. Recomandăm `gpt-4o`.

1. Selectează modelul dorit și apasă pe **Confirm**.

1. Selectează **Deploy**.

### Configurarea Azure OpenAI

După implementare, poți selecta implementarea din pagina "**Models + endpoints**" pentru a găsi **URL-ul endpoint-ului REST**, **Cheia**, **Numele implementării**, **Numele modelului** și **Versiunea API**. Acestea vor fi necesare pentru integrarea modelului de traducere în aplicația ta.

> [!NOTE]
> Poți selecta versiuni API de pe pagina [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) în funcție de cerințele tale. Reține că **versiunea API** este diferită de **versiunea Modelului** afișată pe pagina **Models + endpoints** în Azure AI Foundry.

## Configurarea Azure Computer Vision pentru traducerea imaginilor

Pentru a permite traducerea textului din imagini, trebuie să găsești cheia API și endpoint-ul Azure AI Service.

1. Navighează la Proiectul tău Azure AI (de ex., `CoopTranslator-Project`). Asigură-te că ești în pagina de prezentare generală a proiectului.

### Configurarea Azure AI Service

Găsește cheia API și endpoint-ul din Azure AI Service.

1. Navighează la Proiectul tău Azure AI (de ex., `CoopTranslator-Project`). Asigură-te că ești în pagina de prezentare generală a proiectului.

1. Găsește **API Key** și **Endpoint** în fila Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Această conexiune face capabilitățile resursei Azure AI Services asociate (inclusiv analiza imaginilor) disponibile proiectului tău AI Foundry. Poți apoi folosi această conexiune în caietele tale de notițe sau aplicații pentru a extrage text din imagini, care poate fi ulterior trimis către modelul Azure OpenAI pentru traducere.

## Consolidarea Credentiațialelor Tale

Până acum, ar trebui să fi adunat următoarele:

**Pentru Azure OpenAI (Traducere text):**
- Endpoint Azure OpenAI
- Cheia API Azure OpenAI
- Numele modelului Azure OpenAI (de ex., `gpt-4o`)
- Numele implementării Azure OpenAI (de ex., `cooptranslator-gpt4o`)
- Versiunea API Azure OpenAI

**Pentru Azure AI Services (Extracția textului din imagini prin Vision):**
- Endpoint Azure AI Service
- Cheia API Azure AI Service

### Exemplu: Configurare variabile de mediu (previzualizare)

Mai târziu, când vei construi aplicația ta, probabil o vei configura folosind aceste credențiale colectate. De exemplu, le-ai putea seta ca variabile de mediu astfel:

```bash
# Credentiale Serviciu Azure AI (Necesar pentru traducerea imaginilor)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # de ex., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Seturi opționale de rezervă: variabile duplicate cu sufixul _1/_2 (același index pentru toate variabilele din set)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Credentiale Azure OpenAI (Necesar pentru traducerea textului)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # de ex., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # de ex., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # de ex., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # de ex., 2024-12-01-preview

# Seturi opționale de rezervă: duplică întregul set AZURE_OPENAI_* cu sufixul _1/_2 (același index pentru toate variabilele)
```

---

### Lecturi suplimentare

- [Cum să creezi un proiect în Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cum să creezi resurse Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cum să implementezi modele OpenAI în Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventuale neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->