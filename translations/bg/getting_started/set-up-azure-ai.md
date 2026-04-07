# Настройване на Azure AI за Co-op Translator (Azure OpneAI & Azure AI Vision)

Това ръководство ви превежда през настройването на Azure OpenAI за езиков превод и Azure Computer Vision за анализ на съдържание на изображения (което след това може да се използва за превод на изображения) в Azure AI Foundry.

**Предварителни изисквания:**
- Акаунт в Azure с активен абонамент.
- Достатъчни права за създаване на ресурси и разгръщания във вашия Azure абонамент.

## Създаване на проект в Azure AI

Ще започнете със създаването на проект в Azure AI, който действа като централно място за управление на вашите AI ресурси.

1. Отидете на [https://ai.azure.com](https://ai.azure.com) и влезте с вашия Azure акаунт.

1. Изберете **+Create**, за да създадете нов проект.

1. Изпълнете следните задачи:
   - Въведете **Име на проекта** (например `CoopTranslator-Project`).
   - Изберете **AI hub** (например `CoopTranslator-Hub`) (Създайте нов, ако е необходимо).

1. Кликнете "**Review and Create**", за да настроите вашия проект. Ще бъдете пренасочени към страницата с преглед на вашия проект.

## Настройване на Azure OpenAI за езиков превод

В рамките на вашия проект ще разположите Azure OpenAI модел, който ще служи като бекенд за превод на текст.

### Влезте в проекта си

Ако още не сте там, отворете новосъздадения си проект (например `CoopTranslator-Project`) в Azure AI Foundry.

### Разгръщане на OpenAI модел

1. От лявото меню на вашия проект, под "My assets", изберете "**Models + endpoints**".

1. Изберете **+ Deploy model**.

1. Изберете **Deploy Base Model**.

1. Ще ви бъде показан списък с налични модели. Филтрирайте или потърсете подходящ GPT модел. Препоръчваме `gpt-4o`.

1. Изберете желания модел и кликнете **Confirm**.

1. Изберете **Deploy**.

### Конфигурация на Azure OpenAI

След разгръщането можете да изберете разгръщането от страницата "**Models + endpoints**", за да намерите неговия **REST endpoint URL**, **Key**, **Deployment name**, **Model name** и **API version**. Те ще ви бъдат нужни, за да интегрирате модела за превод във вашето приложение.

> [!NOTE]
> Можете да изберете версии на API от страницата [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) според вашите нужди. Имайте предвид, че **API версията** се различава от **версията на модела**, показвана на страницата **Models + endpoints** в Azure AI Foundry.

## Настройване на Azure Computer Vision за превод на изображения

За да може да превеждате текст в изображения, трябва да намерите API ключа и Endpoint на Azure AI Service.

1. Отидете в проекта си в Azure AI (например `CoopTranslator-Project`). Уверете се, че сте на страницата с преглед на проекта.

### Конфигурация на Azure AI Service

Намерете API ключа и Endpoint от Azure AI Service.

1. Отидете в проекта си в Azure AI (например `CoopTranslator-Project`). Уверете се, че сте на страницата с преглед на проекта.

1. Намерете **API Key** и **Endpoint** от раздела Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Тази връзка прави възможностите на свързания ресурс Azure AI Services (включително анализ на изображения) достъпни за вашия проект в AI Foundry. След това можете да използвате тази връзка в тетрадки или приложения, за да извличате текст от изображения, който след това може да бъде изпращан към модела Azure OpenAI за превод.

## Консолидиране на вашите данни за достъп

До тук би трябвало да сте събрали следното:

**За Azure OpenAI (превод на текст):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Име на Azure OpenAI модел (например `gpt-4o`)
- Име на разгръщане в Azure OpenAI (например `cooptranslator-gpt4o`)
- Версия на Azure OpenAI API

**За Azure AI Services (извличане на текст от изображения чрез Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Пример: Конфигуриране на променливи на средата (Preview)

По-късно, при разработката на вашето приложение, вероятно ще ги конфигурирате като променливи на средата, както следва:

```bash
# Удостоверения за услугата Azure AI (задължителни за превод на изображения)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # например, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# По избор резервни комплекти: дублирайте променливите с наставка _1/_2 (същият индекс за всички променливи в комплекта)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Удостоверения за Azure OpenAI (задължителни за превод на текст)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # например, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # например, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # например, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # например, 2024-12-01-preview

# По избор резервни комплекти: дублирайте пълния комплект AZURE_OPENAI_* с наставка _1/_2 (същият индекс за всички променливи)
```

---

### Допълнително четиво

- [Как да създадете проект в Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Как да създавате Azure AI ресурси](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Как да разгръщате OpenAI модели в Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->