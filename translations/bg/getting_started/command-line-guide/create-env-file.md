# Създайте файла *.env* в коренната директория

В това ръководство ще ви преведем през настройката на променливите на средата за услугите на Azure, използвайки файл *.env*. Променливите на средата ви позволяват сигурно да управлявате чувствителни идентификационни данни, като API ключове, без да ги вграждате директно в кода си.

> [!IMPORTANT]
> - Трябва да бъде конфигурирана само една от услугите за езиков модел (Azure OpenAI или OpenAI). Попълнете променливите на средата за предпочитаната от вас услуга. Ако са зададени променливи за няколко езикови модела, кооперативният преводач ще избере един според приоритета.
> - Ако променливите на средата за Computer Vision не са зададени, преводачът автоматично ще премине в [режим само с Markdown](./markdown-only-mode.md).

> [!NOTE]
> Това ръководство се фокусира основно върху услугите на Azure, но можете да изберете всеки поддържан езиков модел от [списъка с поддържани модели и услуги](../README.md#-supported-models-and-services).

## Създайте файла *.env*

В коренната директория на вашия проект създайте файл с име *.env*. Този файл ще съхранява всички ваши променливи на средата в прост формат.

> [!WARNING]
> Не комитвайте файла *.env* в системи за контрол на версиите като Git. Добавете *.env* във файла си .gitignore, за да предотвратите случайни комити.

1. Отидете в коренната директория на вашия проект.

1. Създайте файл *.env* в коренната директория на вашия проект.

1. Отворете файла *.env* и поставете следния шаблон:

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
> Ако искате да намерите вашите API ключове и крайни точки, можете да се обърнете към [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни интерпретации, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->