# Ustvarite datoteko *.env* v osnovni mapi

V tem vodiču vas bomo vodili skozi nastavitev okolijskih spremenljivk za storitve Azure z uporabo datoteke *.env*. Okolijske spremenljivke vam omogočajo varno upravljanje občutljivih poverilnic, kot so API ključi, brez da bi jih vdelali neposredno v vašo kodo.

> [!IMPORTANT]
> - Potrebno je konfigurirati samo eno storitev jezikovnega modela (Azure OpenAI ali OpenAI). Izpolnite okoljske spremenljivke za vašo izbrano storitev. Če so nastavljene okoljske spremenljivke za več jezikovnih modelov, bo co-op prevajalec izbral enega glede na prioriteto.
> - Če okoljske spremenljivke za Computer Vision niso nastavljene, se bo prevajalec samodejno preklopil na [način samo Markdown](./markdown-only-mode.md).

> [!NOTE]
> Ta vodič je osredotočen predvsem na storitve Azure, vendar lahko izberete katerikoli podprt jezikovni model s seznama [podprtih modelov in storitev](../README.md#-supported-models-and-services).

## Ustvarite datoteko *.env*

V osnovni mapi vašega projekta ustvarite datoteko z imenom *.env*. V tej datoteki bodo shranjene vse vaše okoljske spremenljivke v preprostem formatu.

> [!WARNING]
> Ne dodajajte datoteke *.env* v sisteme za nadzor verzij, kot je Git. Dodajte *.env* v vašo datoteko .gitignore, da preprečite nenamerne commite.

1. Pomaknite se v osnovno mapo vašega projekta.

1. Ustvarite datoteko *.env* v osnovni mapi vašega projekta.

1. Odprite datoteko *.env* in prilepite naslednjo predlogo:

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
> Če želite najti vaše API ključe in končne točke, lahko uporabite [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Za kakršne koli napačne razlage ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->