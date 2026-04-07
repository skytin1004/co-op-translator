# Gumawa ng *.env* na file sa root directory

Sa tutorial na ito, gagabayan ka namin sa pag-set up ng iyong environment variables para sa mga Azure services gamit ang *.env* na file. Pinapayagan ng environment variables na ligtas mong pamahalaan ang mga sensitibong kredensyal, tulad ng mga API key, nang hindi ini-embed nang diretso sa iyong codebase.

> [!IMPORTANT]
> - Isang language model service lang (Azure OpenAI o OpenAI) ang kailangang i-configure. Punan ang environment variables para sa iyong preferred na serbisyo. Kung maraming environment variables para sa iba't ibang language model ang naka-set, pipiliin ng co-op translator ang isa base sa prayoridad.
> - Kung hindi naka-set ang Computer Vision environment variables, awtomatikong lilipat ang translator sa [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> Nakatuon ang gabay na ito sa mga Azure services, ngunit maaari kang pumili ng anumang suportadong language model mula sa [supported models and services list](../README.md#-supported-models-and-services).

## Gumawa ng *.env* na file

Sa root directory ng iyong proyekto, gumawa ng file na pinangalanang *.env*. Sa file na ito ilalagay ang lahat ng iyong environment variables sa isang simpleng format.

> [!WARNING]
> Huwag i-commit ang iyong *.env* file sa mga version control system tulad ng Git. Idagdag ang *.env* sa iyong .gitignore file upang maiwasan ang aksidenteng commits.

1. Pumunta sa root directory ng iyong proyekto.

1. Gumawa ng *.env* na file sa root directory ng iyong proyekto.

1. Buksan ang *.env* file at i-paste ang sumusunod na template:

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
> Kung nais mong hanapin ang iyong mga API key at endpoints, maaari kang sumangguni sa [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang di pagkakaunawaan o maling interpretasyon na bunga ng paggamit ng salin na ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->