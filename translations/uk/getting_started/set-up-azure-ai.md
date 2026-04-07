# Налаштування Azure AI для Co-op Translator (Azure OpneAI та Azure AI Vision)

Цей посібник проведе вас крок за кроком через налаштування Azure OpenAI для перекладу мов та Azure Computer Vision для аналізу вмісту зображень (який потім можна використовувати для перекладу зображень) у межах Azure AI Foundry.

**Вимоги:**
- Обліковий запис Azure з активною підпискою.
- Достатні права для створення ресурсів та розгортання у вашій підписці Azure.

## Створення проекту Azure AI

Почніть зі створення проекту Azure AI, який слугуватиме центральним місцем для керування вашими AI ресурсами.

1. Перейдіть на [https://ai.azure.com](https://ai.azure.com) і увійдіть зі своїм обліковим записом Azure.

1. Оберіть **+Create** для створення нового проекту.

1. Виконайте такі дії:
   - Введіть **Назву проекту** (наприклад, `CoopTranslator-Project`).
   - Виберіть **AI hub** (наприклад, `CoopTranslator-Hub`) (створіть новий, якщо потрібно).

1. Натисніть "**Review and Create**", щоб налаштувати свій проект. Вас буде перенаправлено на сторінку огляду проекту.

## Налаштування Azure OpenAI для перекладу мов

У межах свого проекту ви розгорнете модель Azure OpenAI, щоб вона слугувала backend для текстового перекладу.

### Перехід до вашого проекту

Якщо ви ще не в ньому, відкрийте ваш новостворений проект (наприклад, `CoopTranslator-Project`) в Azure AI Foundry.

### Розгортання моделі OpenAI

1. У лівому меню вашого проекту, в розділі "My assets", оберіть "**Models + endpoints**".

1. Оберіть **+ Deploy model**.

1. Оберіть **Deploy Base Model**.

1. Вам буде показано список доступних моделей. Відфільтруйте або знайдіть відповідну модель GPT. Ми рекомендуємо `gpt-4o`.

1. Виберіть потрібну модель і натисніть **Confirm**.

1. Натисніть **Deploy**.

### Конфігурація Azure OpenAI

Після розгортання ви можете обрати розгортання на сторінці "**Models + endpoints**", щоб знайти його **REST endpoint URL**, **Key**, **Deployment name**, **Model name** та **API version**. Вони знадобляться для інтеграції моделі перекладу у вашу програму.

> [!NOTE]
> Ви можете вибрати версії API на сторінці [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) відповідно до ваших потреб. Зверніть увагу, що **API version** відрізняється від **Model version**, яка показана на сторінці **Models + endpoints** в Azure AI Foundry.

## Налаштування Azure Computer Vision для перекладу зображень

Щоб мати змогу перекладати текст на зображеннях, потрібно знайти ключ API та кінцеву точку (Endpoint) сервісу Azure AI.

1. Перейдіть до вашого проекту Azure AI (наприклад, `CoopTranslator-Project`). Переконайтеся, що ви на сторінці огляду проекту.

### Конфігурація Azure AI Service

Знайдіть API Key та Endpoint на вкладці Azure AI Service.

1. Перейдіть до вашого проекту Azure AI (наприклад, `CoopTranslator-Project`). Переконайтеся, що ви на сторінці огляду проекту.

1. Знайдіть **API Key** та **Endpoint** на вкладці Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Це підключення робить можливості ресурсу Azure AI Services, що пов’язаний (включно з аналізом зображень), доступними для вашого проєкту AI Foundry. Далі ви можете використовувати це підключення у своїх ноутбуках або застосунках для вилучення тексту з зображень, який потім можна надіслати на модель Azure OpenAI для перекладу.

## Об’єднання ваших облікових даних

На цей момент ви повинні мати такі дані:

**Для Azure OpenAI (текстовий переклад):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (наприклад, `gpt-4o`)
- Azure OpenAI Deployment Name (наприклад, `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Для Azure AI Services (вилучення тексту з зображень через Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Приклад: Конфігурація змінних середовища (огляд)

Пізніше, під час розробки вашого додатка, ви ймовірно налаштуєте його, використовуючи ці зібрані облікові дані. Наприклад, ви можете встановити їх у змінні середовища ось так:

```bash
# Облікові дані служби Azure AI (потрібні для перекладу зображень)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # наприклад, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Необов’язкові запасні набори: дублюйте змінні з суфіксом _1/_2 (однаковий індекс для всіх змінних у наборі)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Облікові дані Azure OpenAI (потрібні для перекладу тексту)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # наприклад, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # наприклад, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # наприклад, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # наприклад, 2024-12-01-preview

# Необов’язкові запасні набори: дублюйте повний набір AZURE_OPENAI_* з суфіксом _1/_2 (однаковий індекс для всіх змінних)
```

---

### Додаткове читання

- [Як створити проект в Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Як створити ресурси Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Як розгортати моделі OpenAI в Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння чи неправильне тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->