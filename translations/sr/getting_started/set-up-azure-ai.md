# Подешавање Azure AI за Co-op Translator (Azure OpneAI & Azure AI Vision)

Овај водич вас води кроз подешавање Azure OpenAI за превод језика и Azure Computer Vision за анализу садржаја слике (која се затим може користити за превод заснован на слици) у оквиру Azure AI Foundry.

**Претпоставке:**
- Azure налог са активном претплатом.
- Довољна овлашћења за креирање ресурса и распоређивања у вашој Azure претплати.

## Креирање Azure AI Пројекта

Почећете креирањем Azure AI Пројекта, који служи као централно место за управљање вашим AI ресурсима.

1. Идите на [https://ai.azure.com](https://ai.azure.com) и пријавите се са вашим Azure налогом.

1. Изаберите **+Create** да бисте креирали нови пројекат.

1. Направите следеће:
   - Унесите **Име пројекта** (нпр. `CoopTranslator-Project`).
   - Изаберите **AI hub** (нпр. `CoopTranslator-Hub`) (Креирајте нови ако је потребно).

1. Кликните "**Review and Create**" да подесите ваш пројекат. Бићете преусмерени на страницу прегледа вашег пројекта.

## Подешавање Azure OpenAI за превод језика

Унутар вашег пројекта, распоредите Azure OpenAI модел који ће служити као позадина за превод текста.

### Отварање вашег пројекта

Ако већ нисте тамо, отворите недавно креирани пројекат (нпр. `CoopTranslator-Project`) у Azure AI Foundry.

### Распоређивање OpenAI модела

1. Са левог менија вашег пројекта, у одељку "My assets" изаберите "**Models + endpoints**".

1. Изаберите **+ Deploy model**.

1. Изаберите **Deploy Base Model**.

1. Биће вам приказана листа доступних модела. Филтрирајте или претражите одговарајући GPT модел. Препоручујемо `gpt-4o`.

1. Изаберите жељени модел и кликните **Confirm**.

1. Изаберите **Deploy**.

### Конфигурација Azure OpenAI

Када се распореди, можете из странице "**Models + endpoints**" изабрати распоређивање да бисте пронашли његов **REST endpoint URL**, **Кључ**, **Име распореда**, **Име модела** и **API верзију**. Ово ће бити потребно за интеграцију модела превода у вашу апликацију.

> [!NOTE]
> Можете одабрати верзије API-а са странице [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) у складу са вашим захтевима. Имајте на уму да се **API верзија** разликује од **Верзије модела** која се приказује на страници **Models + endpoints** у Azure AI Foundry.

## Подешавање Azure Computer Vision за превод слика

Да бисте омогућили превод текста унутар слика, потребно је да пронађете Azure AI Service API кључ и Endpoint.

1. Идите на ваш Azure AI Пројекат (нпр. `CoopTranslator-Project`). Уверите се да сте на прегледу пројекта.

### Конфигурација Azure AI Service

Пронађите API кључ и Endpoint из Azure AI Service-а.

1. Идите на ваш Azure AI Пројекат (нпр. `CoopTranslator-Project`). Уверите се да сте на прегледу пројекта.

1. Пронађите **API Key** и **Endpoint** у табу Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Ова веза омогућава капацитете повезаног Azure AI Services ресурса (укључујући анализу слика) доступним вашем AI Foundry пројекту. Затим можете користити ову везу у вашим белешкама или апликацијама за извлачење текста из слика, који се могу послати Azure OpenAI моделу за превод.

## Консолидовање ваших акредитива

До сада бисте требали имати следеће информације:

**За Azure OpenAI (Превод текста):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (нпр. `gpt-4o`)
- Azure OpenAI Deployment Name (нпр. `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**За Azure AI Services (Извлачење текста из слика преко Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Пример: Конфигурација системских променљивих (преглед)

Касније, када будете креирали апликацију, вероватно ћете их конфигурисати користећи сакупљене акредитиве. На пример, можете их поставити као системске променљиве на следећи начин:

```bash
# Акредитиви за Azure AI сервис (потребно за превод слика)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # нпр., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Опциони сетови за резерву: дуплирајте променљиве са наставком _1/_2 (исти индекс за све променљиве у скупу)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Акредитиви за Azure OpenAI (потребно за превод текста)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # нпр., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # нпр., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # нпр., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # нпр., 2024-12-01-preview

# Опциони сетови за резерву: дуплирајте цео AZURE_OPENAI_* сет са наставком _1/_2 (исти индекс за све променљиве)
```

---

### Додатно читање

- [Како креирати пројекат у Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Како креирати Azure AI ресурсе](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Како распоредити OpenAI моделе у Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ограничење одговорности**:  
Овај документ је преведен помоћу AI сервиса за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални превод од стране људског преводиоца. Нисмо одговорни за било каква неспоразума или погрешне тумачења који могу настати коришћењем овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->