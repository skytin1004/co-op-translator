# Креирајте *.env* фајл у коренском директоријуму

У овом туторијалу ћемо вас провести кроз подешавање ваших променљивих окружења за Azure сервисе користећи *.env* фајл. Променљиве окружења вам омогућавају да безбедно управљате осетљивим акредитивима, као што су API кључеви, без да их убацујете директно у ваш код.

> [!IMPORTANT]
> - Потребно је конфигурисати само један сервис за језички модел (Azure OpenAI или OpenAI). Попуните променљиве окружења за ваш омиљени сервис. Уколико су променљиве окружења за више језичких модела постављене, co-op translator ће изабрати један на основу приоритетa.
> - Ако се променљиве окружења за Computer Vision не подесе, преводилац ће аутоматски прелазити у [Markdown-only режим](./markdown-only-mode.md).

> [!NOTE]
> Овај водич је првенствено фокусиран на Azure сервисе, али можете изабрати било који подржани језички модел са [листе подржаних модела и сервиса](../README.md#-supported-models-and-services).

## Креирајте *.env* фајл

У коренском директоријуму вашег пројекта направите фајл под називом *.env*. Овај фајл ће чувати све ваше променљиве окружења у једноставном формату.

> [!WARNING]
> Не додајте ваш *.env* фајл у системе за контролу верзија као што је Git. Додајте *.env* у ваш .gitignore фајл како бисте спречили случајне комите.

1. Идите у коренски директоријум вашег пројекта.

1. Направите *.env* фајл у коренском директоријуму вашег пројекта.

1. Отворите *.env* фајл и залепите следећи шаблон:

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
> Ако желите да пронађете ваше API кључеве и крајње тачке, можете погледати [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ограничење одговорности**:  
Овај документ је преведен уз помоћ АИ сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, молимо имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->