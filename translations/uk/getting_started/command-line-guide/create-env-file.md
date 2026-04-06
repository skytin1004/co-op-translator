# Створіть файл *.env* у кореневій директорії

У цьому посібнику ми проведемо вас через налаштування змінних середовища для сервісів Azure за допомогою файлу *.env*. Змінні середовища дозволяють безпечно керувати конфіденційними даними, такими як API-ключі, не вбудовуючи їх у кодову базу.

> [!IMPORTANT]
> - Потрібно налаштувати лише один сервіс мовної моделі (Azure OpenAI або OpenAI). Заповніть змінні середовища для обраного сервісу. Якщо встановлено змінні середовища для кількох мовних моделей, co-op translator вибере одну на основі пріоритету.
> - Якщо змінні середовища для Computer Vision не встановлені, перекладач автоматично перейде в [режим лише Markdown](./markdown-only-mode.md).

> [!NOTE]
> Цей посібник переважно орієнтований на сервіси Azure, але ви можете обрати будь-яку підтримувану мовну модель зі [списку підтримуваних моделей і сервісів](../README.md#-supported-models-and-services).

## Створення файлу *.env*

У кореневій директорії вашого проєкту створіть файл з назвою *.env*. У цьому файлі зберігатимуться всі ваші змінні середовища у простому форматі.

> [!WARNING]
> Не комітьте файл *.env* у системи керування версіями, як-от Git. Додайте *.env* до вашого .gitignore, щоб уникнути випадкових комітів.

1. Перейдіть у кореневу директорію вашого проєкту.

1. Створіть файл *.env* у кореневій директорії вашого проєкту.

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
> Якщо ви хочете знайти свої API-ключі та кінцеві точки, зверніться до [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоч ми й прагнемо до точності, будь ласка, майте на увазі, що автоматизований переклад може містити помилки або неточності. Оригінальний документ на рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується звертатися до професійного перекладу, виконаного людиною. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->