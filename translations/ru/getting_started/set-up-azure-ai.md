# Настройка Azure AI для Co-op Translator (Azure OpneAI и Azure AI Vision)

Это руководство проведет вас по настройке Azure OpenAI для языкового перевода и Azure Computer Vision для анализа содержимого изображений (которое затем можно использовать для перевода на основе изображения) в Azure AI Foundry.

**Требования:**
- Учетная запись Azure с активной подпиской.
- Достаточные разрешения для создания ресурсов и развертываний в вашей подписке Azure.

## Создание проекта Azure AI

Начните с создания проекта Azure AI, который служит центральным местом для управления вашими AI-ресурсами.

1. Перейдите на [https://ai.azure.com](https://ai.azure.com) и войдите в систему с вашей учетной записью Azure.

1. Выберите **+Create**, чтобы создать новый проект.

1. Выполните следующие действия:
   - Введите **Имя проекта** (например, `CoopTranslator-Project`).
   - Выберите **AI hub** (например, `CoopTranslator-Hub`) (создайте новый, если нужно).

1. Нажмите "**Review and Create**", чтобы создать проект. Вы перейдете на страницу обзора вашего проекта.

## Настройка Azure OpenAI для языкового перевода

В вашем проекте вы развернете модель Azure OpenAI, которая будет служить бэкендом для перевода текста.

### Перейдите в ваш проект

Если вы еще не там, откройте ваш недавно созданный проект (например, `CoopTranslator-Project`) в Azure AI Foundry.

### Развертывание модели OpenAI

1. В левом меню проекта, в разделе "My assets", выберите "**Models + endpoints**".

1. Выберите **+ Deploy model**.

1. Выберите **Deploy Base Model**.

1. Вам будет представлен список доступных моделей. Отфильтруйте или найдите подходящую модель GPT. Мы рекомендуем `gpt-4o`.

1. Выберите желаемую модель и нажмите **Confirm**.

1. Нажмите **Deploy**.

### Конфигурация Azure OpenAI

После развертывания вы можете выбрать развертывание на странице "**Models + endpoints**", чтобы найти его **REST endpoint URL**, **Key**, **Deployment name**, **Model name** и **API version**. Они понадобятся для интеграции модели перевода в ваше приложение.

> [!NOTE]
> Вы можете выбрать версии API на странице [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) в зависимости от ваших требований. Обратите внимание, что **версия API** отличается от **версии модели**, отображаемой на странице **Models + endpoints** в Azure AI Foundry.

## Настройка Azure Computer Vision для перевода изображений

Чтобы включить перевод текста внутри изображений, вам нужно получить ключ API и endpoint сервиса Azure AI.

1. Перейдите в ваш проект Azure AI (например, `CoopTranslator-Project`). Убедитесь, что вы находитесь на странице обзора проекта.

### Конфигурация Azure AI Service

Найдите ключ API и endpoint сервиса Azure AI.

1. Перейдите в ваш проект Azure AI (например, `CoopTranslator-Project`). Убедитесь, что вы находитесь на странице обзора проекта.

1. Найдите **API Key** и **Endpoint** на вкладке Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Это подключение делает возможности связанного ресурса Azure AI Services (включая анализ изображений) доступными в вашем проекте AI Foundry. Затем вы можете использовать это подключение в ваших блокнотах или приложениях для извлечения текста из изображений, который впоследствии можно отправлять в модель Azure OpenAI для перевода.

## Консолидация ваших учетных данных

На данный момент вы должны иметь следующие данные:

**Для Azure OpenAI (перевод текста):**
- Endpoint Azure OpenAI
- API Key Azure OpenAI
- Имя модели Azure OpenAI (например, `gpt-4o`)
- Имя развертывания Azure OpenAI (например, `cooptranslator-gpt4o`)
- Версия API Azure OpenAI

**Для Azure AI Services (извлечение текста из изображений с помощью Vision):**
- Endpoint Azure AI Service
- API Key Azure AI Service

### Пример: конфигурация переменных окружения (предварительный просмотр)

Позже, при создании вашего приложения, вы, вероятно, настроите его с помощью этих собранных учетных данных. Например, вы можете установить их в виде переменных окружения следующим образом:

```bash
# Учетные данные Azure AI Service (требуются для перевода изображений)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # например, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Необязательные запасные наборы: дублируйте переменные с суффиксами _1/_2 (одинаковый индекс для всех переменных в наборе)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Учетные данные Azure OpenAI (требуются для перевода текста)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # например, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # например, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # например, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # например, 2024-12-01-preview

# Необязательные запасные наборы: дублируйте полный набор AZURE_OPENAI_* с суффиксами _1/_2 (одинаковый индекс для всех переменных)
```

---

### Дополнительная литература

- [Как создать проект в Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Как создать ресурсы Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Как развернуть модели OpenAI в Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматического сервиса перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->