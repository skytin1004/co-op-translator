# Készítse el a *.env* fájlt a gyökérkönyvtárban

Ebben az útmutatóban végigvezetjük Önt az Azure szolgáltatásokhoz szükséges környezeti változók beállításán egy *.env* fájl segítségével. A környezeti változók lehetővé teszik az érzékeny hitelesítő adatok, például az API kulcsok biztonságos kezelését anélkül, hogy azokat közvetlenül a kódbázisba kellene illeszteni.

> [!IMPORTANT]
> - Csak egy nyelvi modell szolgáltatást (Azure OpenAI vagy OpenAI) kell konfigurálni. Töltse ki a környezeti változókat a preferált szolgáltatáshoz. Ha több nyelvi modell környezeti változói is meg vannak adva, a co-op translator a prioritás alapján választ egyet.
> - Ha a Computer Vision környezeti változók nincsenek beállítva, a fordító automatikusan átvált a [csak Markdown módra](./markdown-only-mode.md).

> [!NOTE]
> Ez az útmutató elsősorban az Azure szolgáltatásokra fókuszál, de bármely támogatott nyelvi modellt választhat a [támogatott modellek és szolgáltatások listájából](../README.md#-supported-models-and-services).

## Készítse el a *.env* fájlt

A projekt gyökérkönyvtárában hozzon létre egy *.env* nevű fájlt. Ebben a fájlban egyszerű formátumban tárolhatja az összes környezeti változót.

> [!WARNING]
> Ne kövesse el a *.env* fájlt verziókezelő rendszerekbe, mint például Git. Adja hozzá a *.env* fájlt a .gitignore fájlhoz az esetleges véletlen feltöltések elkerülése érdekében.

1. Navigáljon a projekt gyökérkönyvtárába.

1. Hozzon létre egy *.env* fájlt a projekt gyökérkönyvtárában.

1. Nyissa meg a *.env* fájlt, és illessze be a következő sablont:

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
> Ha meg akarja találni az API kulcsait és végpontjait, hivatkozhat a [set-up-azure-ai.md](../set-up-azure-ai.md) dokumentumra.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) használatával készült. Bár igyekszünk pontos fordítást biztosítani, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő hiteles forrásnak. Kritikus információk esetén javasolt szakmai emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy félreértelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->