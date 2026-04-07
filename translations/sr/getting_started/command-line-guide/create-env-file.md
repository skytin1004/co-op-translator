# Креирање *.env* фајла у коренском директоријуму

У овом туторијалу водићемо вас кроз подешавање ваших окружењских променљивих за Azure сервисе користећи *.env* фајл. Окружењске променљиве вам омогућавају безбедно управљање осетљивим акредитивима, као што су API кључеви, без њиховог уметања директно у ваш код.

> [!IMPORTANT]
> - Само један сервис језичког модела (Azure OpenAI или OpenAI) треба да буде конфигурисан. Попуните окружењске променљиве за сервис који више волите. Ако су окружењске променљиве подешене за више језичких модела, co-op translator ће одабрати један на основу приоритета.
> - Ако окружењске променљиве за Computer Vision нису подешене, преводилац ће аутоматски прећи у [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Овај водич је углавном усмерен на Azure сервисе, али можете изабрати било који подржани језички модел са [листе подржаних модела и сервиса](../README.md#-supported-models-and-services).

## Креирање *.env* фајла

У коренском директоријуму вашег пројекта, креирајте фајл по имену *.env*. Овај фајл ће чувати све ваше окружењске променљиве у једноставном формату.

> [!WARNING]
> Не шаљите ваш *.env* фајл у системе за контролу верзија као што је Git. Додајте *.env* у ваш .gitignore фајл како бисте спречили случајне слањања.

1. Идите у коренски директоријум вашег пројекта.

1. Креирајте *.env* фајл у коренском директоријуму вашег пројекта.

1. Отворите *.env* фајл и налепите следећи шаблон:

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
> Уколико желите да пронађете ваше API кључеве и крајње тачке, можете погледати [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање одговорности**:  
Овај документ је преведен помоћу услуге за аутоматски превод [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, имајте на уму да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->