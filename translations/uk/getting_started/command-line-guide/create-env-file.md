# Створіть файл *.env* у кореневій теці

У цьому підручнику ми проведемо вас через налаштування ваших змінних оточення для сервісів Azure за допомогою файлу *.env*. Змінні оточення дозволяють безпечно керувати конфіденційними обліковими даними, такими як API-ключі, без жорсткого кодування їх у вашій кодовій базі.

> [!IMPORTANT]
> - Потрібно налаштувати лише один сервіс мовних моделей (Azure OpenAI або OpenAI). Заповніть змінні оточення для обраного вами сервісу. Якщо встановлено змінні оточення для декількох мовних моделей, Co-op Translator вибере одну відповідно до пріоритету.
> - Якщо змінні оточення для Computer Vision не налаштовані, перекладач автоматично переключиться в [режим лише Markdown](./markdown-only-mode.md).

> [!NOTE]
> Цей посібник переважно орієнтований на сервіси Azure, але ви можете обрати будь-яку підтримувану мовну модель зі [списку підтримуваних моделей і сервісів](../README.md#-supported-models-and-services).

## Створіть файл *.env*

У кореневій теці вашого проєкту створіть файл з іменем *.env*. Цей файл зберігатиме всі ваші змінні оточення у простому форматі.

> [!WARNING]
> Не додавайте файл *.env* до систем контролю версій, таких як Git. Додайте *.env* до вашого файлу .gitignore, щоб уникнути випадкових комітів.

1. Перейдіть до кореневої теки вашого проєкту.

1. Створіть файл *.env* у кореневій теці вашого проєкту.

1. Відкрийте файл *.env* і вставте наступний шаблон:

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
> Якщо ви хочете знайти свої API-ключі та кінцеві точки, ви можете звернутися до [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ його рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->