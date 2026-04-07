# Co-op Translator

_ನಿಮ್ಮ ಶಿಕ್ಷಣ ಗಿithub ವಿಷಯದ ಅನುವಾದಗಳನ್ನು ಬಹು ಭಾಷೆಗಳಲ್ಲಿ ಸುಲಭವಾಗಿ ಸ್ವಯಂಚಾಲಿತಗೊಳಿಸಿ ಮತ್ತು ಉಳಿಸಿಕೊಳ್ಳಿ ನಿಮ್ಮ ಯೋಜನೆ ಬೆಳೆಯುತ್ತಿರುವಂತೆ._

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

### 🌐 ಬಹು-ಭಾಷಾ ಬೆಂಬಲ

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) ಮೂಲಕ ಬೆಂಬಲಿಸಲಾಗಿದೆ

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](./README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ಸ್ಥಳೀಯವಾಗಿ ಕ್ಲೋನ್ ಮಾಡಲು ಇಚ್ಛಿಸುವಿರಾ?**
>
> ಈ ಸಂಗ್ರಹದಲ್ಲಿ 50+ ಭಾಷೆಗಳ ಅನುವಾದಗಳು ಇದೆ, ಇದು ಡೌನ್ಲೋಡ್ ಗಾತ್ರವನ್ನು ಬಹಳಷ್ಟು ಹೆಚ್ಚಿಸುತ್ತದೆ. ಅನುವಾದಗಳಿಲ್ಲದೆ ಕ್ಲೋನ್ ಮಾಡಲು sparse checkout ಅನ್ನು ಬಳಸಿ:
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
> ಇದರಿಂದ ನೀವು ಕೋರ್ಸ್ ಅನ್ನು ಬಹಳ ವೇಗವಾಗಿ ಪೂರ್ಣಗೊಳಿಸಲು ಬೇಕಾದ ಎಲ್ಲಾ ಅನ್ನು ಪಡೆಯುತ್ತೀರಿ.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ಅವಲೋಕನ

**Co-op Translator** ಸಹಾಯ ಮಾಡುತ್ತದೆ ನಿಮ್ಮ ಶಿಕ್ಷಣ GitHub ವಿಷಯವನ್ನು ಬಹು ಭಾಷೆಗಳಲ್ಲಿ ಸುಲಭವಾಗಿ ಸ್ಥಳೀಯಗೊಳಿಸಲು.
ನೀವು ನಿಮ್ಮ Markdown ಫೈಲ್‌ಗಳು, ಚಿತ್ರಗಳು ಅಥವಾ ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಅಪ್ಡೇಟ್ ಮಾಡಿದಾಗ, ಅನುವಾದಗಳು ಸ್ವಯಂಚಾಲಿತವಾಗಿ đồngಿನವಾಗುತ್ತವೆ, ಜಾಗತಿಕವಾಗಿ ಕಲಿಯುವವರಿಗೆ ನಿಮ್ಮ ವಿಷಯವು ಇರಲು ನಿಖರ ಮತ್ತು ನವೀನವಾಗಿರುತ್ತದೆ.

ಅನುವಾದಿತ ವಿಷಯ ಹೇಗೆ ಸಂಘಟಿತವಾಗಿದೆ ಎಂಬ ಉದಾಹರಣೆ:

![Example](../../imgs/translation-ex.png)

## ಅನುವಾದ ಸ್ಥಿತಿಯನ್ನು ಹೇಗೆ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ

Co-op Translator ಅನುವಾದಿತ ವಿಷಯವನ್ನು **ಆವೃತ್ತಿಯ ಸಾಫ್ಟ್‌ವೇರ್ ಕಲೆಗಳಾಗಿ**  
ನಿರ್ವಹಿಸುತ್ತದೆ,  
ಸ್ಥಿರ ಫೈಲ್‌ಗಳಾಗಿ ಅಲ್ಲ.

ಈ ಸಾಧನವು ಅನುವಾದಿತ Markdown, ಚಿತ್ರಗಳು ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳ ಸ್ಥಿತಿಯನ್ನು  
**ಭಾಷಾ-ವಿಸ್ತೃತ ಮೆಟಾಡೇಟಾ** ಬಳಸಿ ಟ್ರ್ಯಾಕ್ ಮಾಡುತ್ತದೆ.

ಈ ವಿನ್ಯಾಸವು Co-op Translatorಗೆ ಅನುಮತಿಸುತ್ತದೆ:

- ಹಳೆಯದಾದ ಅನುವಾದಗಳನ್ನು ವಿಶ್ವಾಸಾರ್ಹವಾಗಿ ಪತ್ತೆ ಮಾಡುವುದು
- Markdown, ಚಿತ್ರಗಳು ಮತ್ತು ನೋಟ್ಬುಕ್‌ಗಳನ್ನು ಸಮಾನ ವಿಧಾನದಂತೆ ನಿಭಾಯಿಸುವುದು
- ದೊಡ್ಡ, ವೇಗವಾಗಿ ಸರಿಯುತ್ತಿರುವ, ಬಹು ಭಾಷಾ ಸಂಗ್ರಹಣೆಗಳಲ್ಲಿ ಸುರಕ್ಷಿತವಾಗಿ ಮಾಪಿಸುವುದು

ಅನುವಾದಗಳನ್ನು ನಿರ್ವಹಿತ ಕಲೆಗಳಾಗಿ ಮಾದರೀಕರಿಸುವ ಮೂಲಕ,  
ಅನುವಾದ ಕಾರ್ಯಪಟುಗಳು ಸಹಜವಾಗಿ ಇತ್ತೀಚಿನ ಸಾಫ್ಟ್‌ವೇರ್ ನಿರ್ಬಂಧ ಮತ್ತು ಕಲೆ ನಿರ್ವಹಣೆ ಪಧ್ಧತಿಗಳೊಂದಿಗೆ ಹೊಂದಿಕೊಳ್ಳುತ್ತವೆ.

→ [ಅನುವಾದ ಸ್ಥಿತಿಯನ್ನು ಹೇಗೆ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## ತ್ವರಿತ ಪ್ರಾರಂಭ

```bash
# ಒಂದು ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ ಮತ್ತು ಸಕ್ರಿಯಗೊಳಿಸಿ (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ)
python -m venv .venv
# ವಿಂಡೋಸ್
.venv\Scripts\activate
# ಮ್ಯಾಕ್‌ಒಎಸ್/ಲಿನಕ್ಸ್ನು
source .venv/bin/activate
# ಪ್ಯಾಕೇಜ್ ಅನ್ನು ಸ್ಥಾಪಿಸಿ
pip install co-op-translator
# ಅನುವಾದಿಸಿ
translate -l "ko ja fr" -md
```

ಡೋಕರ್:

```bash
# GHCR ನಿಂದ ಸಾರ್ವಜನಿಕ ಚಿತ್ರವನ್ನು ಎಳೆಯಿರಿ
docker pull ghcr.io/azure/co-op-translator:latest
# ಪ್ರಸ್ತುತ ಫೋಲ್ಡರ್ ಸ್ಪರ್ಧಿಸಲಾಗಿದ್ದು .env ಒದಗಿಸಲಾಗಿದೆ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ಕನಿಷ್ಠ ಸೆಟ್ ಅಪ್

1. ನೀವು ಬೆಂಬಲಿತ Python ಆವೃತ್ತಿಯನ್ನು (ವೇತನ 3.10-3.12) ಹೊಂದಿದ್ದೀರಿ ಎಂದು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ. ಪಾಯ್ತ್ರೀನಲ್ಲಿ (pyproject.toml) ಇದು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ.
2. `.env` ಫೈಲ್ ಅನ್ನು ಟೆಂಪ್ಲೇಟ್ನಿಂದ ರಚಿಸಿ: [.env.template](../../.env.template)
3. ಒಂದು LLM ಸರಬರಾಜುದಾರರನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ (Azure OpenAI ಅಥವಾ OpenAI)
4. (ಐಚ್ಛಿಕ) ಚಿತ್ರಗಳ ಅನುವಾದಕ್ಕೆ (`-img`), Azure AI Vision ಅನ್ನು ಕಾನ್ಫಿಗರ್ ಮಾಡಿ
5. (ಐಚ್ಛಿಕ) ನೀವು ಬಹು ಪ್ರಮಾಣಪತ್ರ ಸೆಟ್‌ಗಳನ್ನು ನಕಲಿಸುವ ಮೂಲಕ, ಮುಂದೆ `_1`, `_2` ಮುಂತಾದ ಸೂಫಿಕ್ಸ್‌ಗಳನ್ನು ಬಳಸಿ ಕಾನ್ಫಿಗರ್ ಮಾಡಬಹುದು. ಒಂದು ಸೆಟ್‌ನ ಎಲ್ಲಾ ಕ್ರಮಾಂಕಗಳು ಒಂದೇ ಸೂಫಿಕ್ಸ್ ಹಂಚಿಕೊಳ್ಳಬೇಕು.
6. (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ) ಹಿಂದಿನ ಯಾವುದೇ ಅನುವಾದಗಳನ್ನು ಸ್ವಚ್ಛಮಾಡಿ ಸಂಘರ್ಷಗಳನ್ನು ತಡೆಯಲು (ಉದಾ: `translations/`)
7. (ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ) ನಿಮ್ಮ READMEಗೆ ಒಂದು ಅನುವಾದ ವಿಭಾಗವನ್ನು ಸೇರಿಸಿ [README languages template](./getting_started/README_languages_template.md) ಬಳಸಿ
8. ನೋಡಿ: [Azure AI ಸೆಟ್ ಅಪ್](./getting_started/set-up-azure-ai.md)

## ಬಳಕೆ

ಎಲ್ಲಾ ಬೆಂಬಲಿತ ಪ್ರಕಾರಗಳನ್ನು ಅನುವಾದಿಸಿ:

```bash
translate -l "ko ja"
```

ಕೆವಲ Markdown:

```bash
translate -l "de" -md
```

Markdown + ಚಿತ್ರಗಳು:

```bash
translate -l "pt" -md -img
```

ಕೆವಲ ನೋಟ್ಬುಕ್‌ಗಳು:

```bash
translate -l "zh" -nb
```

ಹೆಚ್ಚಿನ ಧ್ವಜಗಳು: [ಆಜ್ಞಾ ಉಲ್ಲೇಖ](./getting_started/command-reference.md)

## ಲಕ್ಷಣಗಳು

- Markdown, ನೋಟ್ಬುಕ್ ಮತ್ತು ಚಿತ್ರಗಳ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದ
- ಮೂಲ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ ಅನುವಾದಗಳನ್ನು đồngಿನಗೊಳಿಸುತ್ತದೆ
- ಸ್ಥಳೀಯವಾಗಿ (CLI) ಅಥವಾ CI (GitHub Actions) ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ
- Azure OpenAI ಅಥವಾ OpenAI ಬಳಸುತ್ತದೆ; ಚಿತ್ರಗಳಿಗೆ ಐಚ್ಛಿಕವಾಗಿ Azure AI Vision
- Markdown ವಿನ್ಯಾಸ ಮತ್ತು ರಚನೆಯನ್ನು ಉಳಿಸುತ್ತದೆ

## ಡಾಕ್ಸ್

- [ಆಜ್ಞಾ ರೇಖಾ ಮಾರ್ಗದರ್ಶಿ](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions ಮಾರ್ಗದರ್ಶಿ (ಸಾರ್ವಜನಿಕ ಸಂಗ್ರಹಣೆಗಳು & ಮಾನದಂಡ ರಹಸ್ಯಗಳು)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions ಮಾರ್ಗದರ್ಶಿ (Microsoft ಸಂಸ್ಥಾನ ಸಂಗ್ರಹಣೆಗಳು & ಸಂಸ್ಥೆ ಮಟ್ಟದ ಸೆಟ್‌ಅಪ್‌ಗಳು)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README ಭಾಷೆಗಳ ಟೆಂಪ್ಲೇಟ್](./getting_started/README_languages_template.md)
- [ಬೆಂಬಲಿತ ಭಾಷೆಗಳು](./getting_started/supported-languages.md)
- [ಹಾಳುಮುರುವುಗಳ ನಿರ್ವಹಣೆ](./getting_started/troubleshooting.md)

### Microsoft-ವಿಶಿಷ್ಟ ಮಾರ್ಗದರ್ಶಿ
> [!NOTE]
> Microsoft “For Beginners” ಸಂಗ್ರಹಣೆಗಳ ನಿರ್ವಾಹಕರಿಗೆ ಮಾತ್ರ.

- [“ಇತರ ಕೋರ್ಸ್‌ಗಳು” ಪಟ್ಟಿಯನ್ನು ನವೀಕರಿಸುವುದು (MS Beginners ಸಂಗ್ರಹಣೆಗಳಿಗಾಗಿ ಮಾತ್ರ)](./getting_started/update-other-courses.md)

## ನಮ್ಮನ್ನು ಬೆಂಬಲಿಸಿ ಮತ್ತು ಜಾಗತಿಕ ಅಧ್ಯಯನವನ್ನು ಉತ್ತೇಜಿಸಿ

ಶಿಕ್ಷಣ ವಿಷಯವನ್ನು ಜಾಗತಿಕವಾಗಿ ಹಂಚಿಕೊಳ್ಳುವ ವಿಧಾನವನ್ನು ಪರಿವರ್ತಿಸಲು ನಮ್ಮೊಡನೆ ಸೇರಿ! [Co-op Translator](https://github.com/azure/co-op-translator) ಗೆ GitHub ಮೇಲೆ ⭐ ಕೊಡಿ ಮತ್ತು ಕಲಿಕೆ ಮತ್ತು ತಂತ್ರಜ್ಞಾನದಲ್ಲಿ ಭಾಷಾ ಅಡೆತಡೆಗಳನ್ನು ಮುರಿಯಲು ನಮ್ಮ ಗುರಿಯನ್ನು ಬೆಂಬಲಿಸಿ. ನಿಮ್ಮ ಆಸಕ್ತಿ ಮತ್ತು ಕೊಡುಗೆಗಳು ಮಹತ್ವದ ಪ್ರಭಾವವನ್ನು ಹೊಂದಿವೆ! ಕೋಡ್ ಕೊಡುಗೆಗಳು ಮತ್ತು ವೈಶಿಷ್ಟ್ಯ ಸೂಚನೆಗಳು ಸದಾ ಸ್ವಾಗತತಗೊಂಡಿವೆ.

### ನಿಮ್ಮ ಭಾಷೆಯಲ್ಲಿ Microsoft ಶಿಕ್ಷಣ ವಿಷಯ ಅನ್ವೇಷಿಸಿ

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

## ವಿಡಿಯೋ ಪ್ರಸ್ತುತಪಡಣೆಗಳು

👉 YouTube ನಲ್ಲಿ ನೋಡುವುದಕ್ಕಾಗಿ ಕೆಳಗಿನ ಚಿತ್ರವನ್ನು ಕ್ಲಿಕ್ ಮಾಡಿ.

- **Open at Microsoft**: Co-op Translator ಅನ್ನು ಹೇಗೆ ಬಳಸುವುದು ಎಂಬ 18 ನಿಮಿಷದ ಸಂಕ್ಷಿಪ್ತ ಪರಿಚಯ ಮತ್ತು ವೇಗದ ಮಾರ್ಗದರ್ಶಿ.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ಕೊಡುಗೆ ಸಲ್ಲಿಸುವುದು

ಈ ಯೋಜನೆ ಕೊಡುಗೆ ಮತ್ತು ಸೂಚನೆಗಳಿಗೆ ಸ್ವಾಗತವಿರುತ್ತದೆ. Azure Co-op Translatorಗೆ ಕೊಡುಗೆ ಮಾಡಲು ಆಸಕ್ತರಿದ್ದರೆ, ದಯವಿಟ್ಟು ನಮ್ಮ [CONTRIBUTING.md](./CONTRIBUTING.md) ನೋಡಿ, Co-op Translator ಅನ್ನು ಇನ್ನಷ್ಟು ಲಭ್ಯವಾಗುವುದಕ್ಕಾಗಿ ನೀವು ಹೇಗೆ ಸಹಾಯ ಮಾಡಬಹುದು ಎಂದು ತಿಳಿಯಿರಿ.

## ಕೊಡುಗೆದಾರರು
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ವರ್ತನೆಯ ನಿಯಮಾವಳಿ

ಈ ಯೋಜನೆ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ಅನ್ನು ಅನುಸರಿಸಿದೆ.  
ಹೆಚ್ಚಿನ ಮಾಹಿತಿಗೆ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ಅನ್ನು ನೋಡಿ ಅಥವಾ  
ಯಾವುದೇ ಹೆಚ್ಚುವರಿ ಪ್ರಶ್ನೆಗಳು ಅಥವಾ ಪ್ರತಿಕ್ರಿಯೆಗಳಿಗಾಗಿ [opencode@microsoft.com](mailto:opencode@microsoft.com) ಅನ್ನು ಸಂಪರ್ಕಿಸಿ.

## ಹೊಣೆಗಾರಿಕೆಯ AI

Microsoft ನಮ್ಮ ಗ್ರಾಹಕರು ನಮ್ಮ AI ಉತ್ಪನ್ನಗಳನ್ನು ಹೊಣೆಗಾರಿಕೆಯೊಂದಿಗೆ ಬಳಸಲು ಸಹಾಯ ಮಾಡಲು ಬದ್ಧವಾಗಿದೆ, ನಮ್ಮ ಅಸ್ತಿತ್ವಗಳನ್ನು ಹಂಚಿಕೊಳ್ಳುತ್ತಾ ಮತ್ತು Transparency Notes ಮತ್ತು Impact Assessments ಮುಂತಾದ ಸಲಕರಣೆಗಳ ಮೂಲಕ ನಂಬಿಕೆ ಆಧಾರಿತ ಸಹಭಾಗಿತ್ವಗಳನ್ನು ಮಾಡುತ್ತಿರುವುದು. ಇವುಗಳ ಬಹುಪಾಲು ಸಂಪನ್ಮೂಲಗಳನ್ನು [https://aka.ms/RAI](https://aka.ms/RAI) ನಲ್ಲಿ ಕಾಣಬಹುದು.  
ಹೊಣೆಗಾರಿಕೆಯ AI ಗೆ Microsoft ನ ದೃಷ್ಟಿಕೋನವು ನ್ಯಾಯ, ನಂಬಿಕೆ ಮತ್ತು ಸುರಕ್ಷತೆ, ಗೌಪ್ಯತೆ ಮತ್ತು ಭದ್ರತೆ, ಸಮಾವೇಶ, ಪಾರದರ್ಶನತೆ ಮತ್ತು ಹೊಣೆಗಾರಿಕೆ ಎಂಬ AI ತತ್ವಗಳ ಮೇಲೆ ಆಧಾರಿತವಾಗಿದೆ.

ಈ ಉದಾಹರಣೆಯಲ್ಲಿ ಬಳಸಿದಂತೆ ಭಾರೀ ಪ್ರಮಾಣದ ಪ್ರಕೃತಿ ಭಾಷೆ, ಚಿತ್ರ ಮತ್ತು ಧ್ವನಿ ಮಾದರಿಗಳು - ಅನ್ಯಾಯಕರ, ಅಚರ್ಯಕರ, ಅಥವಾ ಅಸ್ವೀಕಾರ್ಯವಾಗಿ ವರ್ತಿಸ ಬಹುದು, ಇದರಿಂದ ಹಾನಿ ಸಂಭವಿಸಬಹುದು. ಅಪಾಯಗಳು ಮತ್ತು ನಿಯಂತ್ರಣಗಳ ಬಗ್ಗೆ ಮಾಹಿತಿ ಪಡೆಯಲು ದಯವಿಟ್ಟು [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ಅನ್ನು ಪರಿಶೀಲಿಸಿ.

ಈ ಅಪಾಯಗಳನ್ನು ತಿಳಿದುಕೊಂಡು ತಡೆಯಲು ಶಿಫಾರಸು ಮಾಡಲಾದ ವಿಧಾನವು ನಿಮ್ಮ ವಾಸ್ತುಶಿಲ್ಪದಲ್ಲಿ ಹಾನಿಕರ ವರ್ತನೆಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಿ ತಡೆಯುವ ಸುರಕ್ಷತಾ ವ್ಯವಸ್ಥೆಯನ್ನು ಸೇರಿಸುವುದು. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ಸ್ವತಂತ್ರ ರಕ್ಷಣೆ ಸರ್ತಿಯಾಗಿದ್ದು, ಅಪ್ಲಿಕೇಶನ್‌ಗಳು ಮತ್ತು ಸೇವೆಗಳಲ್ಲಿ ಹಾನಿಕರ ಬಳಕೆದಾರ-ರೂಪಿಸಿದ ಮತ್ತು AI-ರೂಪಿಸಿದ ವಿಷಯಗಳನ್ನು ಪತ್ತೆಹಚ್ಚಲು ಸಾಮರ್ಥ್ಯ ಹೊಂದಿದೆ. Azure AI Content Safety ಪಠ್ಯ ಮತ್ತು ಚಿತ್ರ API ಗಳನ್ನು ಒಳಗೊಂಡಿದೆ, ಇದು ನಿಮಗೆ ಹಾನಿಕರ ವಸ್ತುಗಳ ಪತ್ತೆಯನ್ನು ನೆರವು ನೀಡುತ್ತದೆ. ನಾವು ಇತರ ರೀತಿಯ ಮಾದರಿಗಳಲ್ಲಿ ಹಾನಿಕರ ವಿಷಯವನ್ನು ಪತ್ತೆಯಾಗಿಸಲು, ಅನ್ವೇಷಿಸಲು ಮತ್ತು ಮಾದರಿ ಕೋಡ್ ಅನ್ನು ಪ್ರಯೋಗಿಸಲು ಅನುಮತಿಸುವ Content Safety Studio ಯನ್ನು ಸಹ ಹೊಂದಿದ್ದೇವೆ. ಕೆಳಗಿನ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ನಿಮ್ಮನ್ನು ಸೇವೆಗೆ ವಿನಂತಿ ಸಲ್ಲಿಸುವ ಮೂಲಕ ಮಾರ್ಗದರ್ಶಿಸುತ್ತದೆ.

ಮತ್ತೊಂದು ಪರಿಗಣಿಸುವ ವಿಷಯವೆಂದರೆ ಈ ಅಪ್ಲಿಕೇಶನ್‌ನ ಒಟ್ಟು ಪ್ರದರ್ಶನ. ಬಹು-ಮಾರ್ಗದ ಮತ್ತು ಬಹು-ಮಾದರಿಗಳ ಅಪ್ಲಿಕೇಶನ್‌ಗಳಲ್ಲಿ, ಪ್ರದರ್ಶನ ಎಂದರೆ ನೀವು ಮತ್ತು ನಿಮ್ಮ ಬಳಕೆದಾರರು ನಿರೀಕ್ಷಿಸುವಂಥೆಯೇ ವ್ಯವಸ್ಥೆ ಕಾರ್ಯನಿರ್ವಹಿಸುವುದು, ಹಾನಿಕರ ಔಟ್ಪುಟ್‌ಗಳನ್ನು ಸೃಷ್ಟಿಸದಿರಲು ಒಳಗೊಂಡಿದೆ. ನಿಮ್ಮ ಒಟ್ಟು ಅಪ್ಲಿಕೇಶನ್ ಪ್ರದರ್ಶನವನ್ನು [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ಬಳಸಿ ಮೌಲ್ಯಮಾಪನ ಮಾಡುವುದು ಮಹತ್ವಪೂರ್ಣ.

ನಿಮ್ಮ AI ಅಪ್ಲಿಕೇಶನ್ ಅನ್ನು ನಿಮ್ಮ ಅಭಿವೃದ್ಧಿ ವಾತಾವರಣದಲ್ಲಿ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ಬಳಸಿ ಮೌಲ್ಯಮಾಡಬಹುದು. ಪರೀಕ್ಷಾ ಡೇಟಾಸೆಟ್ ಅಥವಾ ಗುರಿ ಇವುಗಳಿಗೆ ಅನುಸಾರವಾಗಿ, ನಿಮ್ಮ ಜನರೇಟಿವ್ AI ಅಪ್ಲಿಕೇಶನ್ ಸೃಷ್ಟಿಗಳನ್ನು ನಿರ್ಮಿತ ಮುಲ್ಯಮಾಪಕರು ಅಥವಾ ನಿಮ್ಮ ಆಯ್ಕೆಯ ಕಸ್ಟಮ್ ಮೌಲ್ಯಮಾಪಕರ ಸಹಾಯದಿಂದ ಪ್ರಮಾಣಿತವಾಗಿ ಅಳತೆ ಮಾಡಲಾಗುತ್ತದೆ. prompt flow sdk ಯೊಂದಿಗೆ ನಿಮ್ಮ ವ್ಯವಸ್ಥೆಯನ್ನು ಮೌಲ್ಯಮಾಪನ ಮಾಡಲು ಪ್ರಾರಂಭಿಸಲು, [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ಅನ್ನು ಅನುಸರಿಸಿ. ಮೌಲ್ಯಮಾಪನ ರನ್ ನಡಿಸುವ ನಂತರ, ನೀವು [Azure AI Studio ಯಲ್ಲಿ ಫಲಿತಾಂಶಗಳನ್ನು ದೃಷ್ಯಮಾಡಬಹುದು](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ವ್ಯಾಪಾರಕ ಸಂಕೇತಗಳು

ಈ ಯೋಜನೆಲ್ಲಿ ವೈಯಕ್ತಿಕ ಹೆಸರುಗಳು ಅಥವಾ ಲೋಗೋಗಳು ಇರಬಹುದು, ಉತ್ಪನ್ನಗಳು ಅಥವಾ ಸೇವೆಗಳ. Microsoft ವ್ಯಾಪಾರಕ ಸಂಕೇತಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಉತ್ತೀರ್ಣ ಬಳಕೆ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ಅನುಸರಿಸಬೇಕು ಮತ್ತು ಅದರೊಳಗೆ ಇರಬೇಕು.  
ಈ ಯೋಜನೆಯ ಬದಲಾಯಿಸಿದ ರೂಪಗಳಲ್ಲಿ Microsoft ವ್ಯಾಪಾರಕ ಸಂಕೇತಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಬಳಕೆ Microsoft ಪ್ರಾಯೋಜಕತ್ವವನ್ನು ಗೊಂದಲಕ್ಕೆ ಅಥವಾ ಸೂಚನಕ್ಕೆ ಕಾರಣವಾಗಬಾರದು.  
ಮೂರನೇ ಪಕ್ಷದ ವ್ಯಾಪಾರಕ ಸಂಕೇತಗಳು ಅಥವಾ ಲೋಗೋಗಳ ಯಾವುದೇ ಬಳಕೆ ಆ ಪಕ್ಷದ ನೀತಿಗಳ ಅಧೀನವಾಗಿರುತ್ತದೆ.

## ಸಹಾಯ ಪಡೆಯುವುದು

ನೀವು ಅಡ್ಡಪಡೆಯುತ್ತಿದ್ದರೆ ಅಥವಾ AI ಅಪ್ಲಿಕೇಶನ್‌ಗಳನ್ನು ನಿರ್ಮಿಸುವ ಕುರಿತು ಯಾವುದೇ ಪ್ರಶ್ನೆಗಳಿದ್ದರೆ, ಸೇರಿ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ಉತ್ಪನ್ನ ಪ್ರತಿಕ್ರಿಯೆ ಅಥವಾ ನಿರ್ಮಾಣದ ವೇಳೆ ತೊಂದರೆ ಇದ್ದರೆ ಭೇಟಿ ನೀಡಿರಿ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತೊಡಕೆ**:  
ಈ ದಸ್ತಾವೇಜು AI ಭಾಷಾಂತರ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಭಾಷಾಂತರಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯತ್ತ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಭಾಷಾಂತರಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂದು कृಪया ಗಮನಿಸಿ. ಮೂಲ ದಸ್ತಾವೇಜಿನ ಸ್ವರಾಜ್ಯದ ಭಾಷೆಯು ಪ್ರಾಧಿಕಾರಿತ ಮೂಲವೆಂಬುದಾಗಿ ಪರಿಗಣಿಸಬೇಕಾಗಿದೆ. ಮಹತ್ತರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಭಾಷಾಂತರವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಭಾಷಾಂತರ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ误理解 ಅಥವಾ ತಪ್ಪಾಗಿ ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವುದಕ್ಕೆ ನಾವು ಹೊಣೆಗಾರರಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->