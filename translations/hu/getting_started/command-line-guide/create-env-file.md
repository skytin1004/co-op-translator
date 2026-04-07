# Hozd létre a *.env* fájlt a gyökérkönyvtárban

Ebben az útmutatóban végigvezetünk azon, hogyan állítsd be az Azure szolgáltatások környezeti változóit egy *.env* fájl segítségével. A környezeti változók lehetővé teszik, hogy biztonságosan kezeld az érzékeny hitelesítési adatokat, például API kulcsokat, anélkül, hogy azokat a kódodba kellene beágyaznod.

> [!IMPORTANT]
> - Csak egy nyelvi modell szolgáltatást (Azure OpenAI vagy OpenAI) kell konfigurálni. Töltsd ki a környezeti változókat a preferált szolgáltatásodhoz. Ha több nyelvi modell környezeti változói be vannak állítva, a co-op translator prioritás alapján választ egyet.
> - Ha a Computer Vision környezeti változók nincsenek beállítva, a fordító automatikusan átvált a [csak Markdown módra](./markdown-only-mode.md).

> [!NOTE]
> Ez az útmutató elsősorban az Azure szolgáltatásokra fókuszál, de bármely támogatott nyelvi modell közül választhatsz a [támogatott modellek és szolgáltatások listájából](../README.md#-supported-models-and-services).

## Hozd létre a *.env* fájlt

A projekted gyökérkönyvtárában hozz létre egy *.env* nevű fájlt. Ebben a fájlban egyszerű formátumban tárolhatod az összes környezeti változódat.

> [!WARNING]
> Ne commitáld a *.env* fájlt verziókezelő rendszerekbe, mint a Git. Add hozzá a *.env* fájlt a .gitignore fájlodhoz, hogy elkerüld a véletlen commiteket.

1. Navigálj a projekted gyökérkönyvtárába.

1. Hozz létre egy *.env* fájlt a projekt gyökérkönyvtárában.

1. Nyisd meg a *.env* fájlt, és illeszd be a következő sablont:

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
> Ha meg szeretnéd találni az API kulcsaidat és végpontjaidat, utalhatsz a [set-up-azure-ai.md](../set-up-azure-ai.md) fájlra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár a pontosságra törekszünk, kérjük, legyen tekintettel arra, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum annak anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból adódhat.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->