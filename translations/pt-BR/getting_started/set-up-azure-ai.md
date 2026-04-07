# Configurar Azure AI para Co-op Translator (Azure OpneAI & Azure AI Vision)

Este guia orienta você na configuração do Azure OpenAI para tradução de idiomas e Azure Computer Vision para análise de conteúdo de imagens (que pode ser usado para tradução baseada em imagens) dentro do Azure AI Foundry.

**Pré-requisitos:**
- Uma conta Azure com uma assinatura ativa.
- Permissões suficientes para criar recursos e implantações em sua assinatura Azure.

## Criar um Projeto Azure AI

Você começará criando um Projeto Azure AI, que atua como um local central para gerenciar seus recursos de IA.

1. Navegue até [https://ai.azure.com](https://ai.azure.com) e faça login com sua conta Azure.

1. Selecione **+Create** para criar um novo projeto.

1. Execute as seguintes tarefas:
   - Insira um **Nome do projeto** (exemplo: `CoopTranslator-Project`).
   - Selecione o **AI hub** (exemplo: `CoopTranslator-Hub`) (Crie um novo, se necessário).

1. Clique em "**Review and Create**" para configurar seu projeto. Você será levado para a página de visão geral do seu projeto.

## Configurar Azure OpenAI para Tradução de Idiomas

Dentro do seu projeto, você implantará um modelo Azure OpenAI para servir como backend para tradução de texto.

### Navegar para Seu Projeto

Se ainda não estiver lá, abra seu projeto recém-criado (exemplo: `CoopTranslator-Project`) no Azure AI Foundry.

### Implantar um Modelo OpenAI

1. No menu lateral do seu projeto, em "My assets", selecione "**Models + endpoints**".

1. Selecione **+ Deploy model**.

1. Selecione **Deploy Base Model**.

1. Será apresentada uma lista de modelos disponíveis. Filtre ou pesquise por um modelo GPT adequado. Recomendamos o `gpt-4o`.

1. Selecione seu modelo desejado e clique em **Confirm**.

1. Selecione **Deploy**.

### Configuração do Azure OpenAI

Após a implantação, você pode selecionar a implantação na página "**Models + endpoints**" para encontrar sua **URL do endpoint REST**, **Chave**, **Nome da implantação**, **Nome do modelo** e **Versão da API**. Estes serão necessários para integrar o modelo de tradução em sua aplicação.

> [!NOTE]
> Você pode selecionar versões da API na página [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) conforme suas necessidades. Esteja ciente de que a **versão da API** é diferente da **versão do modelo** exibida na página **Models + endpoints** no Azure AI Foundry.

## Configurar Azure Computer Vision para Tradução de Imagens

Para habilitar a tradução de texto dentro de imagens, você precisa localizar a Chave da API e o Endpoint do Azure AI Service.

1. Navegue até seu Projeto Azure AI (exemplo: `CoopTranslator-Project`). Certifique-se de estar na página de visão geral do projeto.

### Configuração do Azure AI Service

Encontre a Chave da API e o Endpoint do Azure AI Service.

1. Navegue até seu Projeto Azure AI (exemplo: `CoopTranslator-Project`). Certifique-se de estar na página de visão geral do projeto.

1. Encontre a **Chave da API** e o **Endpoint** na aba do Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Esta conexão torna as capacidades do recurso vinculado Azure AI Services (incluindo análise de imagens) disponíveis para seu projeto AI Foundry. Você poderá então usar essa conexão em seus notebooks ou aplicações para extrair texto de imagens, o qual pode ser enviado em seguida ao modelo Azure OpenAI para tradução.

## Consolidando Suas Credenciais

Até aqui, você deve ter coletado o seguinte:

**Para Azure OpenAI (Tradução de Texto):**
- Endpoint Azure OpenAI
- Chave da API Azure OpenAI
- Nome do Modelo Azure OpenAI (exemplo: `gpt-4o`)
- Nome da Implantação Azure OpenAI (exemplo: `cooptranslator-gpt4o`)
- Versão da API Azure OpenAI

**Para Azure AI Services (Extração de Texto de Imagem via Vision):**
- Endpoint Azure AI Service
- Chave da API Azure AI Service

### Exemplo: Configuração de Variáveis de Ambiente (Prévia)

Mais adiante, ao construir sua aplicação, você provavelmente a configurará usando essas credenciais coletadas. Por exemplo, você pode configurá-las como variáveis de ambiente assim:

```bash
# Credenciais do Serviço Azure AI (Obrigatório para tradução de imagens)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # Exemplo, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Conjuntos opcionais de fallback: variáveis duplicadas com sufixo _1/_2 (mesmo índice para todas as variáveis do conjunto)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Credenciais do Azure OpenAI (Obrigatório para tradução de texto)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # Exemplo, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # Exemplo, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # Exemplo, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # Exemplo, 2024-12-01-preview

# Conjuntos opcionais de fallback: duplicar o conjunto completo AZURE_OPENAI_* com sufixo _1/_2 (mesmo índice para todas as variáveis)
```

---

### Leitura Adicional

- [Como Criar um projeto no Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Como Criar recursos Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Como Implantar modelos OpenAI no Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->