# Co-op Translator

_ਆਸਾਨੀ ਨਾਲ ਆਪਣੇ ਸਿੱਖਿਆਸਬੰਧੀ GitHub ਸਮੱਗਰੀ ਲਈ ਕਈ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਨੁਵਾਦਾਂ ਨੂੰ ਸੰਗਠਿਤ ਅਤੇ ਅਪਡੇਟ ਰੱਖੋ ਜਿਵੇਂ ਤੁਹਾਡਾ ਪ੍ਰੋਜੈਕਟ ਵਿਕਸਿਤ ਹੁੰਦਾ ਹੈ।_

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

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਮਰਥਨ

#### ਦੇ ਖ਼ਾਤਿਰ [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਕੀ ਤੁਹਾਨੂੰ ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਪਸੰਦ ਹੈ?**
>
> ਇਹ ਰੇਪੋਜ਼ਟਰੀ 50+ ਭਾਸ਼ਾ ਅਨੁਵਾਦਾਂ ਨੂੰ ਸ਼ਾਮਿਲ ਕਰਦੀ ਹੈ ਜੋ ਡਾਊਨਲੋਡ ਆਕਾਰ ਨੂੰ ਕਾਫ਼ੀ ਵਧਾਉਂਦਾ ਹੈ। ਬਿਨਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਕਲੋਨ ਕਰਨ ਲਈ, sparse checkout ਵਰਤੋ:
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
> ਇਹ ਤੁਹਾਨੂੰ ਕੋਰਸ ਮੁਕੰਮਲ ਕਰਨ ਲਈ ਜ਼ਰੂਰੀ ਸਾਰਾ ਕੁਝ ਤੇਜ਼ ਡਾਊਨਲੋਡ ਨਾਲ ਦਿੰਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ਜਾਇਜ਼ਾ

**Co-op Translator** ਤੁਹਾਡੇ ਸਿੱਖਿਆਸਬੰਧੀ GitHub ਸਮੱਗਰੀ ਨੂੰ ਬਿਨਾਂ ਕਿਸੇ ਔਖਏ ਮਿਹਨਤ ਦੇ ਕਈ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਢਾਲਣ ਵਿਚ ਮਦਦ ਕਰਦਾ ਹੈ।  
ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ Markdown ਫਾਈਲਾਂ, ਚਿੱਤਰਾਂ ਜਾਂ ਨੋਟਬੁੱਕ ਨੂੰ ਅਪਡੇਟ ਕਰਦੇ ਹੋ, ਤਦ ਅਨੁਵਾਦ ਆਟੋਮੈਟਿਕ ਤੌਰ 'ਤੇ ਸਮਕਾਲੀ ਬਣੇ ਰਹਿੰਦੇ ਹਨ, ਇਸ ਤਰ੍ਹਾਂ ਤੁਹਾਡੀ ਸਮੱਗਰੀ ਵਿਸ਼ਵ ਭਰ ਦੇ ਸਿੱਖਣ ਵਾਲਿਆਂ ਲਈ ਸਹੀ ਅਤੇ ਅਜਮਾਇਸ਼ਯੋਗ ਰਹਿੰਦੀ ਹੈ।

ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਕਿਵੇਂ ਸੰਗਠਿਤ ਹੁੰਦੀ ਹੈ ਇਸਦਾ ਉਦਾਹਰਣ:

![Example](../../imgs/translation-ex.png)

## ਅਨੁਵਾਦ ਸਥਿਤੀ ਕਿਵੇਂ ਪ੍ਰਬੰਧਿਤ ਕੀਤੀ ਜਾਂਦੀ ਹੈ

Co-op Translator ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਨੂੰ **ਵਰਜ਼ਨ ਕੀਤੀਆਂ ਸਾਫਟਵੇਅਰ ਕਮਾਈਆਂ ਵਜੋਂ** ਪ੍ਰਬੰਧਿਤ ਕਰਦਾ ਹੈ,  
ਨਾ ਕਿ ਸਥਿਰ ਫਾਈਲਾਂ ਵਜੋਂ।

ਇਹ ਸੰਦ ਅਨੁਵਾਦ ਕੀਤੇ Markdown, ਚਿੱਤਰ, ਅਤੇ ਨੋਟਬੁੱਕ ਦੀ ਸਥਿਤੀ ਦੀ ਨਿਗਰਾਨੀ  
**ਭਾਸ਼ਾ-ਸੀਮਤ ਮੈਟਾਡੇਟਾ** ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕਰਦਾ ਹੈ।

ਇਸ ਡਿਜ਼ਾਈਨ ਨਾਲ Co-op Translator ਸਕਦਾ ਹੈ:

- ਪੁਰਾਣੇ ਅਨੁਵਾਦਾਂ ਦਾ ਯਕੀਨੀ ਪਤਾ ਲਗਾਏ
- Markdown, ਚਿੱਤਰ, ਅਤੇ ਨੋਟਬੁੱਕ ਨੂੰ ਇਕਸਾਰ ਤਰੀਕੇ ਨਾਲ ਸਾਬਤ ਕਰੇ
- ਵੱਡੀਆਂ ਤੇਜ਼ੀ ਨਾਲ ਬਦਲਦੀਆਂ ਕਈ-ਭਾਸ਼ਾਈ ਰੇਪੋਜ਼ਟਰੀਜ਼ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਪੱਧਰ 'ਤੇ ਵੱਧੇ

ਅਨੁਵਾਦਾਂ ਨੂੰ ਪ੍ਰਬੰਧਿਤ ਕਮਾਈਆਂ ਵਜੋਂ ਮਾਡਲ ਕਰਕੇ,  
ਅਨੁਵਾਦ ਕਾਰਜ-ਪ੍ਰਵਾਹ ਆਧੁਨਿਕ  
ਸਾਫਟਵੇਅਰ ਡਿਪੇਂਡੇਸੀ ਅਤੇ ਕਮਾਈ ਪ੍ਰਬੰਧਨ ਅਭਿਆਸਾਂ ਨਾਲ ਕੁਦਰਤੀ ਤੌਰ 'ਤੇ ਮਿਲਦੇ ਹਨ।

→ [ਅਨੁਵਾਦ ਸਥਿਤੀ ਕਿਵੇਂ ਪ੍ਰਬੰਧਿਤ ਕੀਤੀ ਜਾਂਦੀ ਹੈ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## ਜਲਦੀ ਸ਼ੁਰੂਆਤ

```bash
# ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਸક્રਿਯ ਕਰੋ (ਸਿਫਾਰਸ਼ੀ)
python -m venv .venv
# ਵਿੰਡੋਜ਼
.venv\Scripts\activate
# ਮੈਕਓਐਸ/ਲਿਨਕਸ
source .venv/bin/activate
# ਪੈਕੇਜ ਇੰਸਟਾਲ ਕਰੋ
pip install co-op-translator
# ਅਨੁਵਾਦ ਕਰੋ
translate -l "ko ja fr" -md
```

ਡਾਕਰ:

```bash
# ਜੀਐਚਸੀਆਰ ਤੋਂ ਜਨਤਕ ਚਿੱਤਰ ਕੱਸੀਦਾ ਕਰੋ
docker pull ghcr.io/azure/co-op-translator:latest
# ਮੌਜੂਦਾ ਫੋਲਡਰ ਮਾਊਂਟ ਕੀਤੇ ਹੋਏ ਅਤੇ .env ਦਿੱਤਾ ਗਿਆ ਚਲਾਓ (ਬੈਸ਼/ਜ਼ਸ਼)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ਘੱਟੋ-ਘੱਟ ਸੈਟਅਪ

1. ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਮਰਥਿਤ Python ਵਰਜ਼ਨ ਹੈ (ਹੁਣ 3.10-3.12)। poetry (pyproject.toml) ਵਿੱਚ ਇਹ ਆਪਣੇ ਆਪ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ।
2. ਇੱਕ `.env` ਫਾਈਲ ਬਣਾ ਕੇ ਟੈੰਪਲੇਟ ਵਰਤੋਂ: [.env.template](../../.env.template)
3. ਇੱਕ LLM ਪ੍ਰੋਵਾਇਡਰ ਕਾਨਫਿਗਰ ਕਰੋ (Azure OpenAI ਜਾਂ OpenAI)
4. (ਵਿਕਲਪਿਕ) ਚਿੱਤਰ ਅਨੁਵਾਦ ਲਈ (`-img`), Azure AI Vision ਕਾਨਫਿਗਰ ਕਰੋ
5. (ਵਿਕਲਪਿਕ) ਤੁਸੀਂ ਸੰਗ੍ਰਹਿਤ ਅਕਾਉਂਟਾਂ ਦੇ ਲਈ ਕਈ ਕ੍ਰੈਡੈਂਸ਼ਲ ਸੈਟਾਂ ਕਾਪੀ ਕਰਕੇ ਬਣਾ ਸਕਦੇ ਹੋ ਜਿਵੇਂ `_1`, `_2`, ਆਦਿ ਨਾਲ ਸਫਿਕਸ। ਇਕ ਸੈਟ ਦੇ ਸਾਰੇ ਵੈਰੀਏਬਲ ਇੱਕੋ ਸਫਿਕਸ ਵਾਲੇ ਹੋਣੇ ਚਾਹੀਦੇ ਹਨ।
6. (ਸਿਫਾਰਸ਼ੀ) ਪਹਿਲਾਂ ਦੇ ਅਨੁਵਾਦ ਹਟਾ ਕੇ ਟਕਰਾਅ ਤੋਂ ਬਚੋ (ਜਿਵੇਂ `translations/`)
7. (ਸਿਫਾਰਸ਼ੀ) README ਵਿੱਚ ਅਨੁਵਾਦ ਸੈਕਸ਼ਨ ਸ਼ਾਮਿਲ ਕਰੋ [README ਭਾਸ਼ਾਵਾਂ ਟੈੰਪਲੇਟ](./getting_started/README_languages_template.md) ਵਰਤੀ ਕੇ
8. ਵੇਖੋ: [Azure AI ਸੈਟਅਪ](./getting_started/set-up-azure-ai.md)

## ਵਰਤੋਂ

ਸਾਰੇ ਸਮਰਥਿਤ ਕਿਸਮਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```bash
translate -l "ko ja"
```

ਸਿਰਫ Markdown:

```bash
translate -l "de" -md
```

Markdown + ਚਿੱਤਰ:

```bash
translate -l "pt" -md -img
```

ਸਿਰਫ ਨੋਟਬੁੱਕ:

```bash
translate -l "zh" -nb
```

ਹੋਰ ਝੰਡੇ: [ਕਮਾਂਡ ਸੰਦਰਭ](./getting_started/command-reference.md)

## ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

- Markdown, ਨੋਟਬੁੱਕ ਅਤੇ ਚਿੱਤਰਾਂ ਲਈ ਸੁਚਾਰੂ ਅਨੁਵਾਦ
- ਅਨੁਵਾਦਾਂ ਨੂੰ ਸਰੋਤ ਬਦਲਾਅ ਦੇ ਨਾਲ ਸਮਕਾਲੀ ਰੱਖਦਾ ਹੈ
- ਲੋਕਲ (CLI) ਅਤੇ CI (GitHub Actions) ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹੈ
- Azure OpenAI ਜਾਂ OpenAI ਵਰਤਦਾ ਹੈ; ਚਿੱਤਰਾਂ ਲਈ ਵਿਕਲਪਿਕ Azure AI Vision
- Markdown ਫਾਰਮੈਟਿੰਗ ਅਤੇ ਢਾਂਚਾ ਬਰਕਰਾਰ ਰੱਖਦਾ ਹੈ

## ਦਸਤਾਵੇਜ਼

- [ਕਮਾਂਡ-ਲਾਈਨ ਮਾਰਗਦਰਸ਼ਨ](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions ਮਾਰਗਦਰਸ਼ਨ (ਪਬਲਿਕ ਰੇਪੋਜ਼ਟਰੀਜ਼ ਅਤੇ ਸਧਾਰਨ ਸਿਕਰੇਟ)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions ਮਾਰਗਦਰਸ਼ਨ (Microsoft ਸੰਸਥਾ ਰੇਪੋਜ਼ਟਰੀਜ਼ ਅਤੇ ਸੰਸਥਾ-ਪੱਧਰੀ ਸੈਟਅਪ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README ਭਾਸ਼ਾਵਾਂ ਟੈੰਪਲੇਟ](./getting_started/README_languages_template.md)
- [ਸਮਰਥਿਤ ਭਾਸ਼ਾਵਾਂ](./getting_started/supported-languages.md)
- [ਯੋਗਦਾਨ](./CONTRIBUTING.md)
- [ਸਮੱਸਿਆ ਹੱਲ](./getting_started/troubleshooting.md)

### Microsoft ਵਿਸ਼ੇਸ਼ ਮਾਰਗਦਰਸ਼ਨ
> [!NOTE]
> ਸਿਰਫ Microsoft “For Beginners” ਰੇਪੋਜ਼ਟਰੀਜ਼ ਦੇ ਸੰਭਾਲਕਾਂ ਲਈ।

- [“ਹੋਰ ਕੋਰਸ” ਸੂਚੀ ਅੱਪਡੇਟ ਕਰਨਾ (ਸਿਰਫ MS Beginners ਰੇਪੋਜ਼ਟਰੀਜ਼ ਲਈ)](./getting_started/update-other-courses.md)

## ਸਾਡੇ ਸਮਰਥਨ ਕਰੋ ਅਤੇ ਵਿਸ਼ਵ ਵਿਆਪੀ ਸਿੱਖਿਆ ਨੂੰ ਬਹਾਲ ਕਰੋ

ਸਾਡੇ ਨਾਲ ਜੁੜੋ ਅਤੇ ਵਿਸ਼ਵ ਭਰ ਵਿੱਚ ਸਿੱਖਿਆ ਸੰਬੰਧੀ ਸਮੱਗਰੀ ਸਾਂਝਾ ਕਰਨ ਦੇ ਤਰੀਕੇ ਨੂੰ ਬਦਲੋ! [Co-op Translator](https://github.com/azure/co-op-translator) ਨੂੰ GitHub 'ਤੇ ਇੱਕ ⭐ ਦਿਓ ਅਤੇ ਸਿੱਖਿਆ ਅਤੇ ਤਕਨਾਲੋਜੀ ਵਿੱਚ ਭਾਸ਼ਾ ਦੀਆਂ ਰੁਕਾਵਟਾਂ ਤੋੜਨ ਦੇ ਸਾਡੇ ਮਿਸ਼ਨ ਨੂੰ ਸਹਾਇਤਾ ਦਿਓ। ਤੁਹਾਡੀ ਦਿਲਚਸਪੀ ਅਤੇ ਯੋਗਦਾਨ ਮਹੱਤਵਪੂਰਨ ਪ੍ਰਭਾਵ ਪੈਦਾ ਕਰਦੇ ਹਨ! ਕੋਡ ਯੋਗਦਾਨ ਅਤੇ ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ ਲਈ ਸਝਾਵਾਂ ਹਮੇਸ਼ਾ ਸਵਾਗਤ ਹਨ।

### ਆਪਣੀ ਭਾਸ਼ਾ ਵਿੱਚ Microsoft ਦੀ ਸਿੱਖਿਆਸਬੰਧੀ ਸਮੱਗਰੀ ਖੋਜੋ

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

## ਵੀਡੀਓ ਪੇਸ਼ਕਸ਼ਾਂ

👉 ਹੇਠਾਂ ਦਿੱਤੇ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰਕੇ YouTube 'ਤੇ ਦੇਖੋ।

- **Microsoft ਦੇਖੋ**: Co-op Translator ਦੀ ਵਰਤੋਂ ਕਰਨ ਦਾ ਇੱਕ ਛੋਟਾ 18 ਮਿੰਟਾਂ ਦਾ ਪ੍ਰਸਤਾਵ ਅਤੇ ਤੇਜ਼ ਗਾਈਡ।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ਯੋਗਦਾਨ ਪਾਉਣਾ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਯੋਗਦਾਨ ਅਤੇ ਸੁਝਾਵਾਂ ਦਾ ਸਵਾਗਤ ਹੈ। Azure Co-op Translator ਵਿੱਚ ਯੋਗਦਾਨ ਦੇਣ ਵਿੱਚ ਰੁਚੀ ਰੱਖਦੇ ਹੋ? ਕਿਰਪਾ ਕਰਕੇ ਸਾਡੇ [CONTRIBUTING.md](./CONTRIBUTING.md) ਨੂੰ ਦੇਖੋ ਜੋ ਤੁਹਾਨੂੰ Co-op Translator ਨੂੰ ਹੋਰ ਪਹੁੰਚਯੋਗ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਦੇਵੇਗਾ।

## ਯੋਗਦਾਨਕਾਰੀਆਂ
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ਕੋਡ ਆਫ ਕੰਡਕਟ

ਇਸ ਪਰਿਯੋਜਨਾ ਨੇ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ਨੂੰ ਅਪਣਾਇਆ ਹੈ।  
ਵਧੀਕ ਜਾਣਕਾਰੀ ਲਈ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ਵੇਖੋ ਜਾਂ ਕਿਸੇ ਵੀ ਵਾਧੂ ਸਵਾਲਾਂ ਜਾਂ ਟਿੱਪਣੀਆਂ ਲਈ [opencode@microsoft.com](mailto:opencode@microsoft.com) ਨਾਲ ਸੰਪਰਕ ਕਰੋ।

## ਜ਼ਿੰਮੇਵਾਰ AI

Microsoft ਸਾਡੇ ਗਾਹਕਾਂ ਨੂੰ ਸਾਡੇ AI ਉਤਪਾਦਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਡੇ ਸਿੱਖਿਆਨਾਮੇ ਸਾਂਝੇ ਕਰਨ ਅਤੇ Transparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਔਜ਼ਾਰਾਂ ਰਾਹੀਂ ਭਰੋਸੇ-ਆਧਾਰਿਤ ਭਾਈਚਾਰੇ ਵਿਕਸਤ ਕਰਨ ਲਈ ਵਚਨਬੱਧ ਹੈ। ਬਹੁਤ ਸਾਰੇ ਇਹ ਸਰੋਤ [https://aka.ms/RAI](https://aka.ms/RAI) ’ਤੇ ਮਿਲ ਸਕਦੇ ਹਨ।  
Microsoft ਦਾ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਵਤਨਦਾਰੀ ਫੇਅਰਨੈੱਸ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਪ੍ਰਾਈਵੇਸੀ ਅਤੇ ਸੁਰੱਖਿਆ, ਸਮਾਵੇਸ਼ਤਾ, ਪਾਰਦਰਸ਼ਤਾ ਅਤੇ ਜਵਾਬਦੇਹੀ ਦੇ ਅਧਾਰ ’ਤੇ ਹੈ।

ਵੱਡੇ ਪੱਧਰ ਦੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ, ਅਤੇ ਬੋਲਣ ਵਾਲੇ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ ਹਨ - ਸੰਭਵ ਤੌਰ 'ਤੇ ਤਰੀਕੇ ਨਾਲ ਵਿਹਾਰ ਕਰ ਸਕਦੇ ਹਨ ਜੋ ਅਨਿਆਂਸਪਦ, ਅਣਭਰੋਸੇਯੋਗ ਜਾਂ ਆਪਤੀਜਨਕ ਹੋ ਸਕਦੇ ਹਨ, ਜੋ ਕਿ ਨੁਕਸਾਨ ਪਹੁੰਚਾ ਸਕਦੇ ਹਨ। ਕਿਰਪਾ ਕਰਕੇ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਉਦਯੋਗਿਕ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ ਵੇਖੋ।

ਇਨ੍ਹਾਂ ਖਤਰਨਾਂ ਨੂੰ ਘਟਾਉਣ ਲਈ ਸੁਝਾਅ ਦਿੱਤਾ ਗਿਆ ਹੈ ਕਿ ਆਪਣੀ ਭਵਨੀ ਰਚਨਾ ਵਿੱਚ ਇਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਲ ਕਰੋ ਜੋ ਨੁਕਸਾਨਦਾਇਕ ਵਿਹਾਰ ਦੀ ਪਛਾਣ ਅਤੇ ਰੋਕਥਾਮ ਕਰ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇਕ ਸਵਤੰਤਰ ਪਰਤ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨਾਂ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਯੂਜ਼ਰ-ਨਿਰਮਿਤ ਅਤੇ AI-ਨਿਰਮਿਤ ਸਮੱਗਰੀ ਨੂੰ ਪਛਾਣ ਸਕਦਾ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ API ਸ਼ਾਮਲ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। ਸਾਡੇ ਕੋਲ ਇੰਟਰਐਕਟਿਵ Content Safety Studio ਵੀ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਵੱਖ-ਵੱਖ ਮਾਡਿਯਾਲਿਟੀਆਂ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਨੂੰ ਪਛਾਣਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਦੇਖਣ, ਇਸ ਦਾ ਅਧਿਐਨ ਕਰਨ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਬੇਨਤੀ ਕਰਨ ਦੇ ਰਸਤੇ ਪ੍ਰਗਟਦੀ ਹੈ।

ਇੱਕ ਹੋਰ ਪਹਿਲੂ ਜਿਸ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਲਾਜ਼ਮੀ ਹੈ ਉਹ ਹੈ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ। ਮਲਟੀ-ਮੋਡਲ ਅਤੇ ਮਲਟੀ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਦੇ ਅਰਥ ਨੂੰ ਸਮਝਦੇ ਹਾਂ ਕਿ ਸਿਸਟਮ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਯੂਜ਼ਰਾਂ ਦੀ ਉਮੀਦਾਂ ਅਨੁਸਾਰ ਕੰਮ ਕਰਦਾ ਹੈ, ਜਿਸ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਨਤੀਜੇ ਬਣਾਉਣਾ ਸ਼ਾਮਲ ਨਹੀਂ। ਇਸ ਲਈ ਤੁਹਾਡੇ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਰਾਹੀਂ ਮੁਲਾਂਕਣ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।

ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਮਾਹੌਲ ਵਿੱਚ ਆਪਣੇ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ਵਰਤ ਸਕਦੇ ਹੋ। ਪ੍ਰਾਪਤ ਟੈਸਟ ਡੇਟਾ ਸੈੱਟ ਜਾਂ ਟਾਰਗੇਟ ਦੇ ਅਨੁਸਾਰ, ਤੁਹਾਡੇ ਜਨਰਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੇ ਨਤੀਜੇ ਕੁਆੰਟੀਟੀਵ ਤੌਰ 'ਤੇ ਬਿਲਟ-ਇਨ ਜਾਂ ਆਪਣੀ ਚੋਣ ਦੇ ਇਵੈਲਵੇਟਰਾਂ ਨਾਲ ਮਾਪੇ ਜਾਂਦੇ ਹਨ। ਸਿਸਟਮ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ prompt flow sdk ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਦੀ ਪਾਲਣਾ ਕਰ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਤੁਸੀਂ ਮੁਲਾਂਕਣ ਚਲਾਉਂਦੇ ਹੋ, ਤੁਸੀਂ [Azure AI Studio ਵਿੱਚ ਨਤੀਜੇ ਦੇਖ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ਟ੍ਰੇਡਮਾਰਕ

ਇਸ ਪਰਿਯੋਜਨਾ ਵਿੱਚ ਪ੍ਰਾਜੈਕਟਾਂ, ਉਤਪਾਦਾਂ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਹੋ ਸਕਦੇ ਹਨ। Microsoft ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਨੂੰ ਅਧਿਕਾਰਿਤ ਤੌਰ ’ਤੇ ਵਰਤਣਾ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ਦੇ ਅਧੀਨ ਹੈ ਅਤੇ ਇਸ ਦਾ ਪਾਲਣ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।  
Microsoft ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਨੂੰ ਇਸ ਪ੍ਰਾਜੈਕਟ ਦੇ ਤਬਦੀਲ ਵੇਰਜ਼ਨਾਂ ਵਿੱਚ ਵਰਤਣ ਨਾਲ ਗਲਤਫਹਿਮੀ ਜਾਂ Microsoft ਦੀ ਮਾਲਕੀ ਸੰਬੰਧੀ ਗਲਤ ਧਾਰਣਾ ਨਹੀਂ ਹੋਣੀ ਚਾਹੀਦੀ। ਤੀਜੀਆਂ ਪੱਖੀਆਂ ਦੇ ਟ੍ਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੇ ਵਰਤੋਂ ਬਾਰੇ ਉਹਨਾਂ ਦੀਆਂ ਨੀਤੀਆਂ ਲਾਗੂ ਹੁੰਦੀਆਂ ਹਨ।

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰੋ

ਜੇ ਤੁਸੀਂ ਕਿਸੇ ਸਮੱਸਿਆ ਵਿੱਚ ਫਸ ਜਾਂਦੇ ਹੋ ਜਾਂ AI ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ ਤਾਂ ਸ਼ਾਮਿਲ ਹੋਵੋ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਉਤਪਾਦ ਪ੍ਰਤੀਕ੍ਰਿਆ ਜਾਂ ਬਣਾਉਣ ਦੌਰਾਨ ਕੋਈ ਗਲਤੀਆਂ ਹਨ ਤਾਂ ਭੇਟ ਕਰੋ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰਤਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਿਵੇਂ ਕਿ ਅਸੀਂ ਸਹੀਗੀ ਬਰਕਰਾਰ ਰੱਖਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸ਼ੁੱਧਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਉਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਭਾਵੀ ਸ੍ਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਵਿਸ਼ੇਸ਼ਜ੍ਞ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->