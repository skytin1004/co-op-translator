# Co-op Translator

_Automacione e mantenha facilmente traduções para o seu conteúdo educativo no GitHub em múltiplos idiomas à medida que o seu projeto evolui._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Suporte Multilíngue

#### Suportado por [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Árabe](../ar/README.md) | [Bengali](../bn/README.md) | [Búlgaro](../bg/README.md) | [Birmanês (Myanmar)](../my/README.md) | [Chinês (Simplificado)](../zh-CN/README.md) | [Chinês (Tradicional, Hong Kong)](../zh-HK/README.md) | [Chinês (Tradicional, Macau)](../zh-MO/README.md) | [Chinês (Tradicional, Taiwan)](../zh-TW/README.md) | [Croata](../hr/README.md) | [Checo](../cs/README.md) | [Dinamarquês](../da/README.md) | [Holandês](../nl/README.md) | [Estónio](../et/README.md) | [Finlandês](../fi/README.md) | [Francês](../fr/README.md) | [Alemão](../de/README.md) | [Grego](../el/README.md) | [Hebraico](../he/README.md) | [Hindi](../hi/README.md) | [Húngaro](../hu/README.md) | [Indonésio](../id/README.md) | [Italiano](../it/README.md) | [Japonês](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Coreano](../ko/README.md) | [Lituano](../lt/README.md) | [Malaio](../ms/README.md) | [Malaiala](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalês](../ne/README.md) | [Pidgin Nigeriano](../pcm/README.md) | [Norueguês](../no/README.md) | [Persa (Farsi)](../fa/README.md) | [Polaco](../pl/README.md) | [Português (Brasil)](../pt-BR/README.md) | [Português (Portugal)](./README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romeno](../ro/README.md) | [Russo](../ru/README.md) | [Sérvio (Cirílico)](../sr/README.md) | [Eslovaco](../sk/README.md) | [Esloveno](../sl/README.md) | [Espanhol](../es/README.md) | [Suaíli](../sw/README.md) | [Sueco](../sv/README.md) | [Tagalo (Filipino)](../tl/README.md) | [Tâmil](../ta/README.md) | [Telugu](../te/README.md) | [Tailandês](../th/README.md) | [Turco](../tr/README.md) | [Ucraniano](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Prefere clonar localmente?**
>
> Este repositório inclui traduções em mais de 50 idiomas, o que aumenta significativamente o tamanho do download. Para clonar sem traduções, use sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Isto oferece-lhe tudo o que precisa para completar o curso com um download muito mais rápido.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Visão Geral

**Co-op Translator** ajuda-o a localizar o seu conteúdo educativo no GitHub em múltiplos idiomas sem esforço.  
Quando atualiza os seus ficheiros Markdown, imagens ou notebooks, as traduções permanecem automaticamente sincronizadas, garantindo que o seu conteúdo se mantém preciso e atualizado para aprendizes em todo o mundo.

Exemplo de como o conteúdo traduzido é organizado:

![Example](../../translated_images/pt-PT/translation-ex.0c8aa6a7ee0aad2b.webp)

## Como o estado da tradução é gerido

O Co-op Translator gere o conteúdo traduzido como **artefactos de software versionados**,  
não como ficheiros estáticos.

A ferramenta acompanha o estado do Markdown traduzido, imagens e notebooks  
usando **metadados específicos por idioma**.

Este design permite ao Co-op Translator:

- Detetar fiavelmente traduções desatualizadas
- Tratar Markdown, imagens e notebooks de forma consistente
- Escalar com segurança em repositórios grandes, rápidos e multilíngues

Ao modelar as traduções como artefactos geridos,  
os fluxos de trabalho de tradução alinham-se naturalmente com as modernas  
práticas de gestão de dependências e artefactos de software.

→ [Como o estado da tradução é gerido](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Arranque rápido

```bash
# Criar e ativar um ambiente virtual (recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalar o pacote
pip install co-op-translator
# Traduzir
translate -l "ko ja fr" -md
```

Docker:

```bash
# Puxe a imagem pública do GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Execute com a pasta atual montada e .env fornecido (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configuração mínima

1. Certifique-se de que possui uma versão suportada do Python (atualmente 3.10-3.12). No poetry (pyproject.toml) isto é gerido automaticamente.
2. Crie um ficheiro `.env` usando o modelo: [.env.template](../../.env.template)
3. Configure um fornecedor de LLM (Azure OpenAI ou OpenAI)
4. (Opcional) Para tradução de imagens (`-img`), configure o Azure AI Vision
5. (Opcional) Pode configurar múltiplos conjuntos de credenciais duplicando variáveis com sufixos como `_1`, `_2`, etc. Todas as variáveis num conjunto devem partilhar o mesmo sufixo.
6. (Recomendado) Limpe quaisquer traduções anteriores para evitar conflitos (ex., `translations/`)
7. (Recomendado) Adicione uma secção de tradução ao seu README usando o [modelo de idiomas do README](./getting_started/README_languages_template.md)
8. Consulte: [Configurar Azure AI](./getting_started/set-up-azure-ai.md)

## Uso

Traduzir todos os tipos suportados:

```bash
translate -l "ko ja"
```

Apenas Markdown:

```bash
translate -l "de" -md
```

Markdown + imagens:

```bash
translate -l "pt" -md -img
```

Apenas notebooks:

```bash
translate -l "zh" -nb
```

Mais opções: [Referência de comandos](./getting_started/command-reference.md)

## Funcionalidades

- Tradução automatizada para Markdown, notebooks e imagens  
- Mantém traduções sincronizadas com alterações na origem  
- Funciona localmente (CLI) ou em CI (GitHub Actions)  
- Usa Azure OpenAI ou OpenAI; opcionalmente Azure AI Vision para imagens  
- Preserva formatação e estrutura do Markdown  

## Documentação

- [Guia da linha de comando](./getting_started/command-line-guide/command-line-guide.md)
- [Guia GitHub Actions (Repositórios Públicos & segredos padrão)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Guia GitHub Actions (Repositórios da organização Microsoft & configurações a nível de org)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Modelo de idiomas para README](./getting_started/README_languages_template.md)
- [Idiomas suportados](./getting_started/supported-languages.md)
- [Contribuir](./CONTRIBUTING.md)
- [Resolução de problemas](./getting_started/troubleshooting.md)

### Guia específico para Microsoft
> [!NOTE]
> Apenas para mantenedores dos repositórios “For Beginners” da Microsoft.

- [Atualizar a lista de “outros cursos” (apenas para repositórios MS Beginners)](./getting_started/update-other-courses.md)

## Apoie-nos e promova o aprendizado global

Junte-se a nós na revolução de como o conteúdo educativo é partilhado globalmente! Dê uma ⭐ ao [Co-op Translator](https://github.com/azure/co-op-translator) no GitHub e apoie a nossa missão de derrubar barreiras linguísticas no aprendizado e na tecnologia. O seu interesse e contribuições fazem uma grande diferença! Contribuições de código e sugestões de funcionalidades são sempre bem-vindas.

### Explore conteúdo educativo Microsoft no seu idioma

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Apresentações em vídeo

👉 Clique na imagem abaixo para ver no YouTube.

- **Open at Microsoft**: Uma breve introdução de 18 minutos e guia rápido sobre como usar o Co-op Translator.

  [![Open at Microsoft](../../translated_images/pt-PT/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuir

Este projeto acolhe contribuições e sugestões. Interessado em contribuir para o Azure Co-op Translator? Por favor consulte o nosso [CONTRIBUTING.md](./CONTRIBUTING.md) para orientações sobre como pode ajudar a tornar o Co-op Translator mais acessível.

## Contribuidores
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Código de Conduta

Este projeto adotou o [Código de Conduta Open Source da Microsoft](https://opensource.microsoft.com/codeofconduct/).
Para mais informações, consulte as [Perguntas Frequentes sobre o Código de Conduta](https://opensource.microsoft.com/codeofconduct/faq/) ou
contacte [opencode@microsoft.com](mailto:opencode@microsoft.com) para quaisquer perguntas ou comentários adicionais.

## IA Responsável

A Microsoft compromete-se a ajudar os nossos clientes a utilizar os nossos produtos de IA de forma responsável, partilhando as nossas aprendizagens e construindo parcerias baseadas na confiança através de ferramentas como Notas de Transparência e Avaliações de Impacto. Muitos destes recursos podem ser encontrados em [https://aka.ms/RAI](https://aka.ms/RAI).
A abordagem da Microsoft à IA responsável está fundamentada nos nossos princípios de IA que são justiça, fiabilidade e segurança, privacidade e segurança, inclusão, transparência e responsabilidade.

Modelos de linguagem natural, imagem e voz em grande escala - como os usados neste exemplo - podem potencialmente comportar-se de formas injustas, pouco fiáveis ou ofensivas, causando danos. Por favor, consulte a [nota de transparência do serviço Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) para se informar sobre riscos e limitações.

A abordagem recomendada para mitigar estes riscos é incluir um sistema de segurança na sua arquitetura que possa detetar e prevenir comportamentos prejudiciais. O [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fornece uma camada independente de proteção, capaz de detetar conteúdos prejudiciais gerados por utilizadores e por IA em aplicações e serviços. O Azure AI Content Safety inclui APIs de texto e imagem que permitem detetar material prejudicial. Temos também um Content Safety Studio interativo que permite visualizar, explorar e experimentar código de exemplo para detetar conteúdos prejudiciais em diferentes modalidades. A seguinte [documentação de início rápido](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) orienta-o na realização de pedidos ao serviço.

Outro aspeto a considerar é o desempenho geral da aplicação. Em aplicações multimodais e multimodelos, o desempenho significa que o sistema funciona como você e os seus utilizadores esperam, incluindo não gerar saídas prejudiciais. É importante avaliar o desempenho da sua aplicação global usando [métricas de qualidade de geração e de risco e segurança](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Pode avaliar a sua aplicação de IA no seu ambiente de desenvolvimento usando o [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Com um conjunto de dados de teste ou um objetivo, as gerações da sua aplicação de IA generativa são medidas quantitativamente com avaliadores incorporados ou avaliadores personalizados à sua escolha. Para começar com o prompt flow sdk para avaliar o seu sistema, pode seguir o [guia de início rápido](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Depois de executar uma avaliação, pode [visualizar os resultados no Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Marcas Comerciais

Este projeto pode conter marcas comerciais ou logótipos de projetos, produtos ou serviços. O uso autorizado das
marcas comerciais ou logótipos da Microsoft está sujeito e deve seguir as
[Diretrizes de Marcas e Identidade da Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
O uso das marcas comerciais ou logótipos da Microsoft em versões modificadas deste projeto não deve causar confusão nem implicar patrocínio da Microsoft.
Qualquer uso de marcas comerciais ou logótipos de terceiros está sujeito às políticas desses terceiros.

## Obter Ajuda

Se ficar bloqueado ou tiver dúvidas sobre como construir aplicações de IA, junte-se a:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Se tiver feedback sobre produtos ou encontrar erros durante a construção, visite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor note que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->