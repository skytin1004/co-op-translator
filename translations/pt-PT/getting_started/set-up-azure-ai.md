# Configurar Azure AI para Co-op Translator (Azure OpneAI & Azure AI Vision)

Este guia orienta-o na configuração do Azure OpenAI para tradução linguística e do Azure Computer Vision para análise de conteúdo de imagem (que pode depois ser usado para tradução baseada em imagens) dentro do Azure AI Foundry.

**Pré-requisitos:**
- Uma conta Azure com uma subscrição ativa.
- Permissões suficientes para criar recursos e implementações na sua subscrição Azure.

## Criar um Projeto Azure AI

Começará por criar um Projeto Azure AI, que atua como um local central para gerir os seus recursos de IA.

1. Navegue para [https://ai.azure.com](https://ai.azure.com) e inicie sessão com a sua conta Azure.

1. Selecione **+Create** para criar um novo projeto.

1. Realize as seguintes tarefas:
   - Introduza um **Nome do projeto** (ex., `CoopTranslator-Project`).
   - Selecione o **AI hub** (ex., `CoopTranslator-Hub`) (Crie um novo se necessário).

1. Clique em "**Review and Create**" para configurar o seu projeto. Será direcionado para a página de visão geral do seu projeto.

## Configurar Azure OpenAI para Tradução Linguística

Dentro do seu projeto, irá implementar um modelo Azure OpenAI para servir como backend para a tradução de texto.

### Navegar para o Seu Projeto

Se ainda não o fez, abra o seu projeto recém-criado (ex., `CoopTranslator-Project`) no Azure AI Foundry.

### Implementar um Modelo OpenAI

1. No menu à esquerda do seu projeto, em "My assets", selecione "**Models + endpoints**".

1. Selecione **+ Deploy model**.

1. Selecione **Deploy Base Model**.

1. Será apresentada uma lista de modelos disponíveis. Filtre ou procure um modelo GPT adequado. Recomendamos o `gpt-4o`.

1. Selecione o modelo desejado e clique em **Confirm**.

1. Selecione **Deploy**.

### Configuração do Azure OpenAI

Depois de implementado, pode selecionar a implementação na página "**Models + endpoints**" para encontrar o seu **URL do ponto de extremidade REST**, **Chave**, **Nome da implementação**, **Nome do modelo** e **Versão da API**. Estes serão necessários para integrar o modelo de tradução na sua aplicação.

> [!NOTE]
> Pode selecionar versões da API a partir da página [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) consoante as suas necessidades. Tenha em atenção que a **versão da API** é diferente da **versão do Modelo** apresentada na página **Models + endpoints** no Azure AI Foundry.

## Configurar Azure Computer Vision para Tradução de Imagem

Para permitir a tradução de texto dentro de imagens, precisa de encontrar a Chave de API e o Ponto de Extremidade do Serviço Azure AI.

1. Navegue até ao seu Projeto Azure AI (ex., `CoopTranslator-Project`). Certifique-se de que está na página de visão geral do projeto.

### Configuração do Serviço Azure AI

Encontre a Chave de API e o Ponto de Extremidade a partir do Serviço Azure AI.

1. Navegue até ao seu Projeto Azure AI (ex., `CoopTranslator-Project`). Certifique-se de que está na página de visão geral do projeto.

1. Encontre a **Chave de API** e o **Ponto de Extremidade** na aba do Serviço Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Esta ligação torna as capacidades do recurso Azure AI Services ligado (incluindo análise de imagem) disponíveis para o seu projeto AI Foundry. Pode depois usar esta ligação nos seus notebooks ou aplicações para extrair texto de imagens, que pode posteriormente ser enviado para o modelo Azure OpenAI para tradução.

## Consolidação das Suas Credenciais

A esta altura, deverá ter recolhido o seguinte:

**Para Azure OpenAI (Tradução de Texto):**
- Ponto de Extremidade Azure OpenAI
- Chave API Azure OpenAI
- Nome do Modelo Azure OpenAI (ex., `gpt-4o`)
- Nome da Implementação Azure OpenAI (ex., `cooptranslator-gpt4o`)
- Versão da API Azure OpenAI

**Para Serviços Azure AI (Extração de Texto de Imagem via Vision):**
- Ponto de Extremidade Serviço Azure AI
- Chave API Serviço Azure AI

### Exemplo: Configuração de Variáveis de Ambiente (Pré-visualização)

Mais tarde, ao construir a sua aplicação, provavelmente irá configurá-la usando estas credenciais recolhidas. Por exemplo, poderá defini-las como variáveis de ambiente assim:

```bash
# Credenciais do Serviço Azure AI (Obrigatório para tradução de imagens)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ex., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Conjuntos de fallback opcionais: variáveis duplicadas com o sufixo _1/_2 (mesmo índice para todas as variáveis do conjunto)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Credenciais Azure OpenAI (Obrigatório para tradução de texto)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ex., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ex., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ex., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ex., 2024-12-01-preview

# Conjuntos de fallback opcionais: duplicar o conjunto completo AZURE_OPENAI_* com sufixo _1/_2 (mesmo índice para todas as variáveis)
```

---

### Leitura Adicional

- [Como criar um projeto no Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Como criar recursos Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Como implementar modelos OpenAI no Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->