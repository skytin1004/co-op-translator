<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:22:44+00:00",
  "source_file": "README.md",
  "language_code": "pcm"
}
-->
# Co-op Translator

_Easy way wey you fit use automate to translate your educational GitHub content go plenti language so people for everywhere fit sabi wetin you dey talk._

### 🌐 Multi-Language Support

#### Co-op Translator dey support all dis language

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## Overview

**Co-op Translator** go help you quick quick translate your educational GitHub content go plenti language, so people for everywhere fit understand am without wahala. If you update your Markdown files, images, or Jupyter notebooks, the translation go dey update by itself so your educational GitHub content go always dey fresh and correct for people wey dey different country.

See as Co-op Translator dey arrange translated educational GitHub content:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.pcm.png)

## How you fit start

```bash
# Create and activate a virtual environment (recommended)
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
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## How to set am simple

- Make `.env` file with the template: [.env.template](../../.env.template)
- Set one LLM provider (Azure OpenAI or OpenAI)
- If you wan translate image (`-img`), set Azure AI Vision join
- E good make you clean any translation wey other tool don do before, so wahala no go dey (like: `translations/`).
- E good make you add translations section for your README with [README languages template](./README_languages_template.md)
- Check: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## How to use am

Translate everything wey e support:

```bash
translate -l "ko ja"
```

Only Markdown:

```bash
translate -l "de" -md
```

Markdown plus images:

```bash
translate -l "pt" -md -img
```

Only notebooks:

```bash
translate -l "zh" -nb
```

See more flags: [Command reference](./getting_started/command-reference.md)

## Wetin e fit do

- E dey translate Markdown, notebooks, and images by itself
- E dey make sure translation dey follow source anytime you change am
- E fit run for your computer (CLI) or for CI (GitHub Actions)
- E dey use Azure OpenAI or OpenAI; if na image, you fit use Azure AI Vision join
- E dey keep Markdown formatting and arrangement as e be

## Docs

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Supported languages](./getting_started/supported-languages.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

## Support Us and Help People Learn Everywhere

Abeg join body make we change how people dey share educational content for everywhere! Give [Co-op Translator](https://github.com/azure/co-op-translator) one ⭐ for GitHub and help our work wey dey break language wahala for learning and technology. As you show interest and contribute, e dey make big difference! If you sabi code or get idea for new feature, abeg bring am.

### See Microsoft educational content for your language

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

## Video Presentations

You fit learn more about Co-op Translator from our presentations _(Click the image below to watch am for YouTube.)_:

- **Open at Microsoft**: Na short 18-minute intro and quick guide on how you fit use Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.pcm.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## How you fit contribute

This project dey welcome anybody wey wan help or get idea. If you wan join body for Azure Co-op Translator, check our [CONTRIBUTING.md](./CONTRIBUTING.md) to see how you fit make Co-op Translator easy for everybody.

## People wey don contribute

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

This project dey follow [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
If you wan know more, check [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
send mail to [opencode@microsoft.com](mailto:opencode@microsoft.com) if you get any question or talk.

## Responsible AI

Microsoft dey try make sure say people dey use our AI products well, dey share wetin we learn, and dey build trust with tools like Transparency Notes and Impact Assessments. You fit see many of these things for [https://aka.ms/RAI](https://aka.ms/RAI).
How Microsoft dey do responsible AI na based on our AI principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability.

Big AI models wey dey do language, image, and speech - like the ones wey this sample dey use - fit sometimes do things wey no good, wey fit cause wahala. Abeg check [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) so you go sabi the risk and limitation.

The best way to avoid wahala na to add safety system for your setup wey fit see and stop bad behaviour. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) fit help you as extra protection, e fit see bad content wey people or AI generate for your app or service. Azure AI Content Safety get text and image APIs wey fit help you see bad things. We still get Content Safety Studio wey you fit use test and try code wey dey detect bad content for different type. This [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) go show you how to send request to the service.
Another thing wey you suppose reason na how the whole app dey perform. For apps wey get plenty mode and plenty model, when we talk performance, e mean say the system dey do wetin you and your users dey expect, plus e no dey produce wahala output. E good make you check how your whole app dey perform with [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

You fit test your AI app for where you dey build am with the [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). If you get test dataset or target, your generative AI app go dey measure with built-in evaluators or any custom evaluator wey you like. To start with prompt flow sdk to test your system, just follow the [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). After you run the evaluation, you fit [see the results for Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

This project fit get trademarks or logos for projects, products, or services. If you wan use Microsoft
trademarks or logos, you gats follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
If you use Microsoft trademarks or logos for any version wey you change, e no suppose confuse people or make e look like say na Microsoft sponsor am.
Any use of third-party trademarks or logos na the third-party policy go guide am.

## How to Get Help

If wahala hold you or you get question about how to build AI apps, join:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

If you wan drop feedback or you dey see error as you dey build, go:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Disclaimer**:
Na AI translation service wey dem dey call [Co-op Translator](https://github.com/Azure/co-op-translator) we use take translate this document. Even though we try make the translation correct, abeg make you sabi say machine translation fit get mistake or no too correct. Na the original document for the main language be the correct one wey you suppose follow. If the information dey important, abeg use professional human translation. We no go fit hold any responsibility for any wahala or misunderstanding wey fit happen because of this translation.