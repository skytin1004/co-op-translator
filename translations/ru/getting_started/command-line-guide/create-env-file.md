# Создайте файл *.env* в корневом каталоге

В этом руководстве мы покажем вам, как настроить переменные окружения для служб Azure с помощью файла *.env*. Переменные окружения позволяют безопасно управлять конфиденциальными учетными данными, такими как ключи API, без их жесткого кодирования в вашем коде.

> [!IMPORTANT]
> - Необходимо настроить только один сервис языковой модели (Azure OpenAI или OpenAI). Заполните переменные окружения для предпочитаемого сервиса. Если заданы переменные для нескольких языковых моделей, co-op translator выберет одну на основе приоритета.
> - Если переменные окружения для Computer Vision не установлены, переводчик автоматически переключится в [режим только Markdown](./markdown-only-mode.md).

> [!NOTE]
> Это руководство в основном сосредоточено на сервисах Azure, но вы можете выбрать любую поддерживаемую языковую модель из [списка поддерживаемых моделей и сервисов](../README.md#-supported-models-and-services).

## Создайте файл *.env*

В корневом каталоге вашего проекта создайте файл с именем *.env*. Этот файл будет содержать все ваши переменные окружения в простом формате.

> [!WARNING]
> Не коммитьте файл *.env* в системы контроля версий, такие как Git. Добавьте *.env* в ваш .gitignore, чтобы избежать случайных коммитов.

1. Перейдите в корневой каталог вашего проекта.

1. Создайте файл *.env* в корневом каталоге вашего проекта.

1. Откройте файл *.env* и вставьте следующий шаблон:

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
> Если вы хотите найти свои ключи API и конечные точки, вы можете обратиться к [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматический перевод может содержать ошибки и неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->