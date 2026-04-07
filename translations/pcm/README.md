# Co-op Translator

_Ezily automatet an maintain transléshon dem for your educational GitHub content for plenti language dem as your project dey grow._

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

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Prefer to Clone Locally?**
>
> Dis repozitori get 50+ language translations wey make di download size plenty. To clone without translations, use sparse checkout:
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
> Dis one go give you everything you need to complete di course quick quick.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overview

**Co-op Translator** dey help you localize your educational GitHub content into plenti language dem without wahala.
When you update your Markdown files, images, or notebooks, translations go dey automatically synchronized, make sure say your content still dey correct and up to date for learners all over di world.

Example of how translated content dey organized:

![Example](../../imgs/translation-ex.png)

## How translation state is managed

Co-op Translator dey manage translated content as **versioned software artifacts**,  
no be like static files.

Di tool dey track di state of translated Markdown, images, and notebooks
using **language-scoped metadata**.

Dis design make Co-op Translator fit:

- Sure sure detect outdated translations
- Treat Markdown, images, and notebooks one kain
- Scale safely across big, fast-moving, multi-language repositories

By modeling translations as managed artifacts,
translation workflows follow modern
software dependency and artifact management style.

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Quick start

```bash
# Make and activate one virtual environment (wey dem recommend)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Comot di public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run wit di current folder mount and .env provide (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal setup

1. Make sure say you get Python version wey dem support (now na 3.10-3.12). For poetry (pyproject.toml) dis one dey automatic.
2. Create one `.env` file using di template: [.env.template](../../.env.template)
3. Configure one LLM provider (Azure OpenAI or OpenAI)
4. (Optional) For image translation (`-img`), configure Azure AI Vision
5. (Optional) You fit configure many credential sets by copying variables with suffixes like `_1`, `_2`, etc. All variables for one set must carry di same suffix.
6. (Recommended) Clear any old translations to avoid wahala (eg, `translations/`)
7. (Recommended) Add translation section inside your README using di [README languages template](./getting_started/README_languages_template.md)
8. See: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## Usage

Translate all supported types:

```bash
translate -l "ko ja"
```

Only Markdown:

```bash
translate -l "de" -md
```

Markdown + images:

```bash
translate -l "pt" -md -img
```

Only notebooks:

```bash
translate -l "zh" -nb
```

More flags: [Command reference](./getting_started/command-reference.md)

## Features

- Automated translation for Markdown, notebooks, and images
- Keeps translations dey inline with source changes
- Works locally (CLI) or for CI (GitHub Actions)
- Use Azure OpenAI or OpenAI; optional Azure AI Vision for images dem
- Preserve Markdown format and structure

## Docs

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Supported languages](./getting_started/supported-languages.md)
- [Contributing](./CONTRIBUTING.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> Only for maintainers of Microsoft “For Beginners” repositories.

- [Updating the “other courses” list (for MS Beginners repositories only)](./getting_started/update-other-courses.md)

## Support us and foster global learning

Make you join us revolutionize how educational content dey shared worldwide! Give [Co-op Translator](https://github.com/azure/co-op-translator) one ⭐ for GitHub and support our mission to break language wall for learning and technology. Your interest and contributions fit make big impact! Code contributions and feature suggestions always dey welcomed.

### Explore Microsoft educational content in your language

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

## Video presentations

👉 Click di image below to watch on YouTube.

- **Open at Microsoft**: One short 18-minute intro and quick guide on how to take use Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contributing

Dis project dey welcome contributions and suggestions. If you wan contribute to Azure Co-op Translator, abeg check our [CONTRIBUTING.md](./CONTRIBUTING.md) for how you fit help make Co-op Translator easy to use.

## Contributors
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Dis project don adopt di [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more info, see di [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any oda questions or comments.

## Responsible AI

Microsoft don commit to help our customers use our AI products responsibly, share our learnings, and build trust-based partnerships through tools like Transparency Notes and Impact Assessments. Plenti of dis resources dey find for [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft approach to responsible AI base for our AI principles of fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Large-scale natural language, image, and speech models - like di ones wey dem use for dis sample - fit fit behave in ways wey no fair, no reliable, or dey offensive, we fit cause harm. Abeg check di [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) to know about risks and wahala dem.

Di way wey dem recommend to reduce dis kind risk na to put safety system for your architecture wey fit detect and stop bad behavior. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) dey provide independent protection layer, wey fit detect harmful user-generated and AI-generated content for apps and services dem. Azure AI Content Safety get text and image APIs wey go allow you detect bad material. We still get interactive Content Safety Studio wey allow you view, explore and try sample code for detecting harmful content for different modalities. Dis [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) go guide you how to dey make requests to di service.

Another tin wey you suppose consider na di overall application performance. For multi-modal and multi-models apps, we mean say di system go do as you and your users expect, including say e no go generate harmful outputs. E important to check di performance for your overall app using [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You fit evaluate your AI application inside your development environment using [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Whether na test dataset or target, your generative AI application generations go dey quantitatively measured with built-in evaluators or custom evaluators wey you choose. To start to dey use prompt flow sdk for evaluating your system, you fit follow di [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Once you run evaluation, you fit [visualize di results inside Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Dis project fit get trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos dey follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
If you use Microsoft trademarks or logos for modified versions of dis project, make sure e no confuse people or make dem think say Microsoft sponsor am.
Any use of third-party trademarks or logos go follow di third-party policies.

## Getting Help

If you jam wahala or get any questions about building AI apps, make you join:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

If you get product feedback or error wen you dey build, go visit:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg sabi say automated translations fit get error or no too correct. Di original document for e own language na di correct source. For important info, e better make professional human translation do am. We no go responsible for any misunderstanding or wrong meaning wey fit come from dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->