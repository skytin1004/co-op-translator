# Utilizar a GitHub Action Co-op Translator (Configuração Pública)

**Destinatários:** Este guia destina-se a utilizadores na maioria dos repositórios públicos ou privados onde as permissões padrão do GitHub Actions são suficientes. Utiliza o `GITHUB_TOKEN` incorporado.

Automatize a tradução da documentação do seu repositório de forma simples com a GitHub Action Co-op Translator. Este guia explica como configurar a action para criar automaticamente pull requests com traduções atualizadas sempre que os seus ficheiros Markdown de origem ou imagens forem alterados.

> [!IMPORTANT]
>
> **Escolher o Guia Certo:**
>
> Este guia detalha a **configuração mais simples usando o `GITHUB_TOKEN` padrão**. Este é o método recomendado para a maioria dos utilizadores, pois não requer a gestão de Chaves Privadas sensíveis de GitHub App.
>

## Pré-requisitos

Antes de configurar a GitHub Action, certifique-se de que tem as credenciais do serviço de IA necessárias.

**1. Obrigatório: Credenciais do Modelo de Linguagem de IA**
Precisa de credenciais para pelo menos um dos Modelos de Linguagem suportados:

- **Azure OpenAI**: Requer Endpoint, Chave API, Nomes de Modelo/Deployment, Versão da API.
- **OpenAI**: Requer Chave API, (Opcional: Org ID, Base URL, Model ID).
- Consulte [Modelos e Serviços Suportados](../../../../README.md) para mais detalhes.

**2. Opcional: Credenciais de IA de Visão (para Tradução de Imagens)**

- Só é necessário se precisar de traduzir texto dentro de imagens.
- **Azure AI Vision**: Requer Endpoint e Chave de Subscrição.
- Se não fornecer, a action funciona em [modo só-Markdown](../markdown-only-mode.md).

## Configuração

Siga estes passos para configurar a GitHub Action Co-op Translator no seu repositório usando o `GITHUB_TOKEN` padrão.

### Passo 1: Compreender a Autenticação (Usar `GITHUB_TOKEN`)

Este workflow utiliza o `GITHUB_TOKEN` incorporado fornecido pelo GitHub Actions. Este token concede automaticamente permissões ao workflow para interagir com o seu repositório, de acordo com as definições configuradas no **Passo 3**.

### Passo 2: Configurar Segredos do Repositório

Só precisa de adicionar as **credenciais do serviço de IA** como segredos encriptados nas definições do seu repositório.

1.  Aceda ao seu repositório de destino no GitHub.
2.  Vá a **Settings** > **Secrets and variables** > **Actions**.
3.  Em **Repository secrets**, clique em **New repository secret** para cada segredo de serviço de IA necessário listado abaixo.

    <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.pt.png" alt="Selecionar ação de definições"> *(Referência de Imagem: Mostra onde adicionar segredos)*

**Segredos de Serviço de IA Necessários (Adicione TODOS os que se aplicam consoante os seus Pré-requisitos):**

| Nome do Segredo                         | Descrição                                 | Fonte do Valor                     |
| :-------------------------------------- | :---------------------------------------- | :--------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`              | Chave para Azure AI Service (Computer Vision)  | O seu Azure AI Foundry             |
| `AZURE_AI_SERVICE_ENDPOINT`             | Endpoint para Azure AI Service (Computer Vision) | O seu Azure AI Foundry             |
| `AZURE_OPENAI_API_KEY`                  | Chave para Azure OpenAI                   | O seu Azure AI Foundry             |
| `AZURE_OPENAI_ENDPOINT`                 | Endpoint para Azure OpenAI                | O seu Azure AI Foundry             |
| `AZURE_OPENAI_MODEL_NAME`               | Nome do Modelo Azure OpenAI               | O seu Azure AI Foundry             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`     | Nome do Deployment Azure OpenAI           | O seu Azure AI Foundry             |
| `AZURE_OPENAI_API_VERSION`              | Versão da API para Azure OpenAI           | O seu Azure AI Foundry             |
| `OPENAI_API_KEY`                        | Chave API para OpenAI                     | A sua plataforma OpenAI            |
| `OPENAI_ORG_ID`                         | ID da Organização OpenAI (Opcional)       | A sua plataforma OpenAI            |
| `OPENAI_CHAT_MODEL_ID`                  | ID específico do modelo OpenAI (Opcional) | A sua plataforma OpenAI            |
| `OPENAI_BASE_URL`                       | Base URL personalizada da API OpenAI (Opcional) | A sua plataforma OpenAI      |

### Passo 3: Configurar Permissões do Workflow

A GitHub Action precisa de permissões concedidas via `GITHUB_TOKEN` para fazer checkout do código e criar pull requests.

1.  No seu repositório, vá a **Settings** > **Actions** > **General**.
2.  Desça até à secção **Workflow permissions**.
3.  Selecione **Read and write permissions**. Isto concede ao `GITHUB_TOKEN` as permissões necessárias de `contents: write` e `pull-requests: write` para este workflow.
4.  Certifique-se de que a caixa **Allow GitHub Actions to create and approve pull requests** está **selecionada**.
5.  Clique em **Save**.

<img src="../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.pt.png" alt="Definição de permissões">

### Passo 4: Criar o Ficheiro de Workflow

Por fim, crie o ficheiro YAML que define o workflow automatizado usando o `GITHUB_TOKEN`.

1.  No diretório raiz do seu repositório, crie o diretório `.github/workflows/` se ainda não existir.
2.  Dentro de `.github/workflows/`, crie um ficheiro chamado `co-op-translator.yml`.
3.  Cole o seguinte conteúdo em `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Personalize o Workflow:**
  - **[!IMPORTANT] Línguas de Destino:** No passo `Run Co-op Translator`, **DEVE rever e modificar a lista de códigos de línguas** no comando `translate -l "..." -y` para corresponder aos requisitos do seu projeto. A lista de exemplo (`ar de es...`) deve ser substituída ou ajustada.
  - **Trigger (`on:`):** O trigger atual executa em cada push para `main`. Para repositórios grandes, considere adicionar um filtro `paths:` (veja o exemplo comentado no YAML) para executar o workflow apenas quando ficheiros relevantes (ex: documentação de origem) forem alterados, poupando minutos de execução.
  - **Detalhes do PR:** Personalize a `commit-message`, `title`, `body`, nome da `branch` e `labels` no passo `Create Pull Request` se necessário.

## Execução do Workflow

> [!WARNING]  
> **Limite de Tempo dos Runners Hospedados pelo GitHub:**  
> Os runners hospedados pelo GitHub, como `ubuntu-latest`, têm um **limite máximo de execução de 6 horas**.  
> Para repositórios de documentação grandes, se o processo de tradução exceder as 6 horas, o workflow será automaticamente terminado.  
> Para evitar isto, considere:  
> - Utilizar um **runner auto-hospedado** (sem limite de tempo)  
> - Reduzir o número de línguas de destino por execução

Assim que o ficheiro `co-op-translator.yml` for integrado na sua branch principal (ou na branch especificada no trigger `on:`), o workflow será executado automaticamente sempre que forem feitas alterações nessa branch (e corresponder ao filtro `paths`, se configurado).

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.