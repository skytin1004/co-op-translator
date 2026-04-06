# Utwórz plik *.env* w katalogu głównym

W tym samouczku przeprowadzimy Cię przez proces konfigurowania zmiennych środowiskowych dla usług Azure za pomocą pliku *.env*. Zmienne środowiskowe pozwalają na bezpieczne zarządzanie poufnymi danymi, takimi jak klucze API, bez konieczności umieszczania ich bezpośrednio w kodzie.

> [!IMPORTANT]
> - Należy skonfigurować tylko jedną usługę modelu językowego (Azure OpenAI lub OpenAI). Wypełnij zmienne środowiskowe dla wybranej usługi. Jeśli zostaną ustawione zmienne dla kilku modeli językowych, co-op translator wybierze jeden na podstawie priorytetu.
> - Jeśli zmienne środowiskowe dla Computer Vision nie są ustawione, translator automatycznie przełączy się na [tryb tylko Markdown](./markdown-only-mode.md).

> [!NOTE]
> Ten przewodnik koncentruje się głównie na usługach Azure, ale możesz wybrać dowolny obsługiwany model językowy z listy [obsługiwanych modeli i usług](../README.md#-supported-models-and-services).

## Utwórz plik *.env*

W katalogu głównym projektu utwórz plik o nazwie *.env*. Ten plik będzie przechowywał wszystkie Twoje zmienne środowiskowe w prostym formacie.

> [!WARNING]
> Nie dodawaj pliku *.env* do systemów kontroli wersji, takich jak Git. Dodaj plik *.env* do swojego pliku .gitignore, aby zapobiec przypadkowym commitom.

1. Przejdź do katalogu głównego swojego projektu.

1. Utwórz plik *.env* w katalogu głównym swojego projektu.

1. Otwórz plik *.env* i wklej poniższy szablon:

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
> Jeśli chcesz znaleźć swoje klucze API i końcówki, możesz odwołać się do [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było jak najbardziej poprawne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uważany za wiarygodne źródło. W przypadku istotnych informacji zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->