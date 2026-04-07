# Konfiguracja Azure AI dla Co-op Translator (Azure OpneAI i Azure AI Vision)

Ten przewodnik przeprowadzi Cię przez proces konfiguracji Azure OpenAI do tłumaczenia języków oraz Azure Computer Vision do analizy zawartości obrazów (które mogą być następnie wykorzystane do tłumaczenia opartego na obrazach) w ramach Azure AI Foundry.

**Wymagania wstępne:**
- Konto Azure z aktywną subskrypcją.
- Wystarczające uprawnienia do tworzenia zasobów i wdrożeń w subskrypcji Azure.

## Utwórz projekt Azure AI

Zaczniesz od utworzenia projektu Azure AI, który będzie centralnym miejscem do zarządzania Twoimi zasobami AI.

1. Przejdź do [https://ai.azure.com](https://ai.azure.com) i zaloguj się na konto Azure.

1. Wybierz **+Create**, aby utworzyć nowy projekt.

1. Wykonaj następujące czynności:
   - Wprowadź **Nazwa projektu** (np. `CoopTranslator-Project`).
   - Wybierz **AI hub** (np. `CoopTranslator-Hub`) (Utwórz nowy, jeśli to konieczne).

1. Kliknij "**Review and Create**", aby utworzyć projekt. Zostaniesz przeniesiony do strony przeglądu projektu.

## Konfiguracja Azure OpenAI do tłumaczenia języka

W ramach swojego projektu wdrożysz model Azure OpenAI, który będzie służył jako zaplecze do tłumaczenia tekstu.

### Przejdź do swojego projektu

Jeśli jeszcze tego nie zrobiłeś, otwórz swój nowo utworzony projekt (np. `CoopTranslator-Project`) w Azure AI Foundry.

### Wdróż model OpenAI

1. Z menu po lewej stronie projektu, w sekcji "My assets", wybierz "**Models + endpoints**".

1. Wybierz **+ Deploy model**.

1. Wybierz **Deploy Base Model**.

1. Zostanie wyświetlona lista dostępnych modeli. Przefiltruj lub wyszukaj odpowiedni model GPT. Zalecamy model `gpt-4o`.

1. Wybierz żądany model i kliknij **Confirm**.

1. Wybierz **Deploy**.

### Konfiguracja Azure OpenAI

Po wdrożeniu możesz wybrać wdrożenie na stronie "**Models + endpoints**", aby znaleźć jego **adres REST endpoint**, **klucz**, **nazwę wdrożenia**, **nazwę modelu** oraz **wersję API**. Będą one potrzebne do integracji modelu tłumaczeniowego z Twoją aplikacją.

> [!NOTE]
> Możesz wybrać wersje API na stronie [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) w zależności od swoich potrzeb. Pamiętaj, że **wersja API** różni się od **wersji modelu** wyświetlanej na stronie **Models + endpoints** w Azure AI Foundry.

## Konfiguracja Azure Computer Vision do tłumaczenia obrazów

Aby umożliwić tłumaczenie tekstu w obrazach, musisz znaleźć klucz API i punkt końcowy usługi Azure AI.

1. Przejdź do swojego projektu Azure AI (np. `CoopTranslator-Project`). Upewnij się, że jesteś na stronie przeglądu projektu.

### Konfiguracja usługi Azure AI

Znajdź klucz API i punkt końcowy w usłudze Azure AI.

1. Przejdź do swojego projektu Azure AI (np. `CoopTranslator-Project`). Upewnij się, że jesteś na stronie przeglądu projektu.

1. Znajdź **API Key** i **Endpoint** na karcie usługi Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

To połączenie umożliwia korzystanie z funkcji powiązanego zasobu Azure AI Services (w tym analizy obrazów) w projekcie AI Foundry. Możesz następnie używać tego połączenia w swoich notatnikach lub aplikacjach do ekstrakcji tekstu z obrazów, który może być następnie przesłany do modelu Azure OpenAI w celu przetłumaczenia.

## Konsolidacja poświadczeń

Do tego momentu powinieneś zebrać następujące dane:

**Dla Azure OpenAI (Tłumaczenie tekstu):**
- Punkt końcowy Azure OpenAI
- Klucz API Azure OpenAI
- Nazwa modelu Azure OpenAI (np. `gpt-4o`)
- Nazwa wdrożenia Azure OpenAI (np. `cooptranslator-gpt4o`)
- Wersja API Azure OpenAI

**Dla usług Azure AI (Ekstrakcja tekstu z obrazu przez Vision):**
- Punkt końcowy usługi Azure AI
- Klucz API usługi Azure AI

### Przykład: Konfiguracja zmiennych środowiskowych (Podgląd)

Później, podczas budowania aplikacji, prawdopodobnie skonfigurujesz ją, używając tych zebranych poświadczeń. Na przykład możesz ustawić je jako zmienne środowiskowe w następujący sposób:

```bash
# Poświadczenia usługi Azure AI (wymagane do tłumaczenia obrazów)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # np. 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Opcjonalne zestawy zapasowe: duplikuj zmienne z przyrostkiem _1/_2 (ten sam indeks dla wszystkich zmiennych w zestawie)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Poświadczenia Azure OpenAI (wymagane do tłumaczenia tekstu)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # np. 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # np. gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # np. cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # np. 2024-12-01-preview

# Opcjonalne zestawy zapasowe: duplikuj cały zestaw AZURE_OPENAI_* z przyrostkiem _1/_2 (ten sam indeks dla wszystkich zmiennych)
```

---

### Dalsze lektury

- [Jak utworzyć projekt w Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Jak tworzyć zasoby Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Jak wdrażać modele OpenAI w Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się o dokładność, prosimy o świadomość, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być traktowany jako źródło wiarygodne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->