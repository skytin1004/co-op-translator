# Crie o arquivo *.env* no diretório raiz

Neste tutorial, vamos guiá-lo na configuração das suas variáveis de ambiente para os serviços Azure usando um arquivo *.env*. As variáveis de ambiente permitem que você gerencie com segurança credenciais sensíveis, como chaves de API, sem incorporá-las diretamente no seu código.

> [!IMPORTANT]
> - Apenas um serviço de modelo de linguagem (Azure OpenAI ou OpenAI) precisa ser configurado. Preencha as variáveis de ambiente para o serviço que você preferir. Se as variáveis de ambiente para múltiplos modelos de linguagem estiverem definidas, o co-op translator selecionará uma com base na prioridade.
> - Se as variáveis de ambiente para Computer Vision não estiverem definidas, o tradutor automaticamente mudará para o [modo apenas Markdown](./markdown-only-mode.md).

> [!NOTE]
> Este guia foca principalmente nos serviços Azure, mas você pode escolher qualquer modelo de linguagem suportado da [lista de modelos e serviços suportados](../README.md#-supported-models-and-services).

## Crie o arquivo *.env*

No diretório raiz do seu projeto, crie um arquivo chamado *.env*. Este arquivo armazenará todas as suas variáveis de ambiente em um formato simples.

> [!WARNING]
> Não comite seu arquivo *.env* em sistemas de controle de versão como Git. Adicione *.env* ao seu arquivo .gitignore para evitar commits acidentais.

1. Navegue até o diretório raiz do seu projeto.

1. Crie um arquivo *.env* no diretório raiz do seu projeto.

1. Abra o arquivo *.env* e cole o seguinte modelo:

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
> Se quiser encontrar suas chaves de API e endpoints, você pode consultar [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->