# Co-op Translator

_ਆਸਾਨੀ ਨਾਲ ਆਪਣੇ ਸਿੱਖਿਆਤਮਕ GitHub ਸਮੱਗਰੀ ਦੇ ਅਨੁਵਾਦਾਂ ਨੂੰ ਕਈ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਦੇ ਵਿਕਾਸ ਨਾਲ ਢਾਲੋ ਅਤੇ ਸੰਭਾਲੋ।_

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

### 🌐 ਬਹੁ-ਭਾਸ਼ਾਈ ਸਹਾਇਤਾ

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) ਵੱਲੋਂ ਸਮਰਥਿਤ

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](./README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ਕੀ ਤੁਸੀਂ ਲੋਕਲ ਤੌਰ 'ਤੇ ਕਲੋਨ ਕਰਨਾ ਪਸੰਦ ਕਰਦੇ ਹੋ?**
>
> ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ ਵਿੱਚ 50+ ਭਾਸ਼ਾਵਾਂ ਦੇ ਅਨੁਵਾਦ ਸ਼ਾਮਲ ਹਨ ਜੋ ਡਾਊਨਲੋਡ ਆਕਾਰ ਨੂੰ ਕਾਫੀ ਵਧਾਉਂਦੇ ਹਨ। ਬਿਨਾਂ ਅਨੁਵਾਦਾਂ ਦੇ ਕਲੋਨ ਕਰਨ ਲਈ sparse checkout ਦੀ ਵਰਤੋਂ ਕਰੋ:
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
> ਇਸ ਤਰ੍ਹਾਂ ਤੁਹਾਡੇ ਕੋਲ ਕੋਰਸ ਪੂਰਾ ਕਰਨ ਲਈ ਸਾਰੀਆਂ ਚੀਜ਼ਾਂ ਮਿਲਦੀਆਂ ਹਨ ਤੇ ਡਾਊਨਲੋਡ ਵੀ ਬਹੁਤ ਤੇਜ਼ ਹੁੰਦਾ ਹੈ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ਓਵਰਵਿਊ

**Co-op Translator** ਤੁਹਾਡੇ ਸਿੱਖਿਆਤਮਕ GitHub ਸਮੱਗਰੀ ਨੂੰ ਬਹੁ-ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਬਿਨਾ ਕਿਸੇ ਔਖੜਾਈ ਦੇ ਸਥਾਨਕ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।  
ਜਦੋਂ ਤੁਸੀਂ ਆਪਣੇ Markdown ਫਾਈਲਾਂ, ਚਿੱਤਰਾਂ ਜਾਂ ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਅਪਡੇਟ ਕਰਦੇ ਹੋ, ਅਨੁਵਾਦ ਆਪੋ-ਆਪ ਜੁੜੇ ਰਹਿੰਦੇ ਹਨ, ਇਸ ਨਾਲ ਇਹ ਯਕੀਨੀ ਬਣਦਾ ਹੈ ਕਿ ਤੁਹਾਡਾ ਸਮੱਗਰੀ ਦੁਨੀਆ ਭਰ ਦੇ ਵਿਦਿਆਰਥੀਆਂ ਲਈ ਸਹੀ ਅਤੇ ਅਪ-ਟੂ-ਡੇਟ ਰਹਿੰਦਾ ਹੈ।

ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਦੇ ਕਿਵੇਂ ਸੰਗਠਿਤ ਕੀਤੇ ਜਾਣ ਦਾ ਉਦਾਹਰਨ:

![Example](../../translated_images/pa/translation-ex.0c8aa6a7ee0aad2b.webp)

## ਅਨੁਵਾਦ ਦੀ ਸਥਿਤੀ ਕਿਵੇਂ ਸੰਭਾਲੀ ਜਾਂਦੀ ਹੈ

Co-op Translator ਅਨੁਵਾਦਿਤ ਸਮੱਗਰੀ ਨੂੰ **ਵਰਜਨਡ ਸੌਫਟਵੇਅਰ ਆਰਟੀਫੈਕਟਸ** ਵਜੋਂ ਸੰਭਾਲਦਾ ਹੈ,  
ਨਾਮਾਤਰ ਸਥਿਰ ਫਾਈਲਾਂ ਵਜ਼ੋਂ ਨਹੀਂ।

ਇਹ ਸੰਦ ਅਨੁਵਾਦਿਤ Markdown, ਚਿੱਤਰ ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਦੀ ਸਥਿਤੀ  
**ਭਾਸ਼ਾ-ਵਿਕੇਂਦ੍ਰਤ ਮੈਟਾਡਾਟਾ** ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਟ੍ਰੈਕ ਕਰਦਾ ਹੈ।

ਇਹ ਡਿਜ਼ਾਈਨ Co-op Translator ਨੂੰ ਯੋਗ ਬਣਾਉਂਦਾ ਹੈ ਕਿ:

- ਬਿਨਾ ਕਿਸੇ ਗਲਤੀ ਦੇ ਪੁਰਾਣੇ ਅਨੁਵਾਦਾਂ ਦਾ ਪਤਾ ਲਗਾਏ  
- Markdown, ਚਿੱਤਰ ਅਤੇ ਨੋਟਬੁੱਕਾਂ ਨੂੰ ਸਮਾਨ ਤਰੀਕੇ ਨਾਲ ਸਾਂਭੇ  
- ਵੱਡੇ ਅਤੇ ਤੇਜ਼-ਗਤੀ ਵਾਲੇ ਬਹੁ-ਭਾਸ਼ਾਈ ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਵਿੱਚ ਸੁਰੱਖਿਅਤ ਢੰਗ ਨਾਲ ਫੈਲੇ

ਅਨੁਵਾਦਾਂ ਨੂੰ ਪ੍ਰਬੰਧਤ ਆਰਟੀਫੈਕਟ ਵਜੋਂ ਮਾਡਲਿੰਗ ਕਰਕੇ,  
ਅਨੁਵਾਦ ਕਾਰਜ ਪ੍ਰਵਾਹ प्राकृतिक ਤੌਰ 'ਤੇ ਆਧੁਨਿਕ  
ਸੌਫਟਵੇਅਰ ਡੀਪੈਂਡੈਂਸੀ ਅਤੇ ਆਰਟੀਫੈਕਟ ਪ੍ਰਬੰਧਨ ਅਮਲਾਂ ਨਾਲ ਮੇਲ ਖਾਂਦੇ ਹਨ।

→ [ਅਨੁਵਾਦ ਦੀ ਸਥਿਤੀ ਕਿਵੇਂ ਸੰਭਾਲੀ ਜਾਂਦੀ ਹੈ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## ਤੁਰੰਤ ਸ਼ੁਰੂਆਤ

```bash
# ਵਰਚੁਅਲ ਵਾਤਾਵਰਣ ਬਣਾਓ ਅਤੇ ਸਰਗਰਮ ਕਰੋ (ਸਿਫਾਰਸ਼ ਕੀਤੀ ਗਈ)
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

Docker:

```bash
# GHCR ਤੋਂ ਜਨਤਕ ਛਵੀ ਨੂੰ ਖਿੱਚੋ
docker pull ghcr.io/azure/co-op-translator:latest
# ਮੌਜੂਦਾ ਫੋਲਡਰ ਮਾਊਂਟ ਕੀਤਾ ਗਿਆ ਹੈ ਅਤੇ .env ਪ੍ਰਦਾਨ ਕੀਤਾ ਗਿਆ ਹੈ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ਘੱਟੋ ਘੱਟ ਸੈਟਅੱਪ

1. ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਸਮਰਥ ਪਾਇਥਨ ਵਰਜਨ ਹੈ (ਹੁਣ ਲਈ 3.10-3.12)। poetry (pyproject.toml) ਵਿੱਚ ਇਹ ਆਪਣੇ ਆਪ ਸੰਭਾਲਿਆ ਜਾਂਦਾ ਹੈ।  
2. .env ਫਾਈਲ ਬਣਾਓ ਇਸ ਟੈਮਪਲੇਟ ਦੀ ਵਰਤੋਂ ਨਾਲ: [.env.template](../../.env.template)  
3. ਇੱਕ LLM ਪ੍ਰਦਾਤਾ ਕਨਫਿਗਰ ਕਰੋ (Azure OpenAI ਜਾਂ OpenAI)  
4. (ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ) ਚਿੱਤਰਾਂ ਦੇ ਅਨੁਵਾਦ ਲਈ (`-img`), Azure AI Vision ਕਨਫਿਗਰ ਕਰੋ  
5. (ਇੱਛਾ ਅਨੁਸਾਰ) ਕਈ ਕ੍ਰੈਡੇਂਸ਼ੀਅਲ ਸੈੱਟ ਕਨਫਿਗਰ ਕਰਨ ਲਈ ਵਰਿਆਬਲਜ਼ ਨੂੰ _1, _2 ਆਦਿ ਨਾਲ ਨਕਲ ਕਰੋ। ਇੱਕ ਸੈੱਟ ਵਿਚ ਸਾਰੇ ਵਰਿਆਬਲਜ਼ ਨੂੰ ਸਮਾਨ ਸਫ਼ਿਕਸ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।  
6. (ਸਿਫਾਰਸ਼਼ੀ) ਕਿਸੇ ਵੀ ਪਹਿਲਾਂ ਦੇ ਅਨੁਵਾਦਾਂ ਨੂੰ ਸਾਫ ਕਰੋ ਤਾਂ ਜੋ ਟਕਰਾਅ ਨਾ ਹੋਵੇ (ਜਿਵੇਂ, `translations/`)  
7. (ਸਿਫਾਰਸ਼਼ੀ) ਆਪਣੇ README ਵਿੱਚ ਅਨੁਵਾਦ ਸੈਕਸ਼ਨ ਸ਼ਾਮਲ ਕਰੋ [README ਭਾਸ਼ਾਵਾਂ ਟੈਮਪਲੇਟ](./getting_started/README_languages_template.md) ਨੂੰ ਵਰਤ ਕੇ  
8. ਵੇਖੋ: [Azure AI ਸੈਟਅੱਪ](./getting_started/set-up-azure-ai.md)

## ਵਰਤੋਂ

ਸਾਰੇ ਸਮਰਥਿਤ ਕਿਸਮਾਂ ਦਾ ਅਨੁਵਾਦ ਕਰੋ:

```bash
translate -l "ko ja"
```

ਕੇਵਲ Markdown:

```bash
translate -l "de" -md
```

Markdown + ਚਿੱਤਰ:

```bash
translate -l "pt" -md -img
```

ਕੇਵਲ ਨੋਟਬੁੱਕ:

```bash
translate -l "zh" -nb
```

ਹੋਰ ਝੰਡੇ: [ਕਮਾਂਡ ਰੈਫਰੈਂਸ](./getting_started/command-reference.md)

## ਵਿਸ਼ੇਸ਼ਤਾਵਾਂ

- Markdown, ਨੋਟਬੁੱਕਾਂ ਅਤੇ ਚਿੱਤਰਾਂ ਲਈ ਸਵੈਚਲਿਤ ਅਨੁਵਾਦ  
- ਸੋਰਸ ਬਦਲਾਵਾਂ ਨਾਲ ਅਨੁਵਾਦਾਂ ਨੂੰ ਸਥਿਰ ਰੱਖਦਾ ਹੈ  
- ਸਥਾਨਕ (CLI) ਜਾਂ CI (GitHub Actions) ਵਿੱਚ ਕੰਮ ਕਰਦਾ ਹੈ  
- Azure OpenAI ਜਾਂ OpenAI ਵਰਤਦਾ ਹੈ; ਚਿੱਤਰਾਂ ਲਈ ਵਿਕਲਪਕ Azure AI Vision  
- Markdown ਦੇ ਫਾਰਮੈਟਿੰਗ ਅਤੇ ਢਾਂਚੇ ਨੂੰ ਬਚਾਉਂਦਾ ਹੈ

## ਦਸਤਾਵੇਜ਼

- [ਕਮਾਂਡ-ਲਾਈਨ ਗਾਈਡ](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions ਗਾਈਡ (ਪਬਲਿਕ ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਅਤੇ ਸਧਾਰਣ ਸੱਤਰਾਂ)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions ਗਾਈਡ (Microsoft ਸੰਸਥਾ ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਅਤੇ ਓਰਗ-ਪੱਧਰੀ ਸੈਟਅੱਪ)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README ਭਾਸ਼ਾਵਾਂ ਟੈਮਪਲੇਟ](./getting_started/README_languages_template.md)  
- [ਸਮਰਥਿਤ ਭਾਸ਼ਾਵਾਂ](./getting_started/supported-languages.md)  
- [ਯੋਗਦਾਨ](./CONTRIBUTING.md)  
- [ਮਸਲੇ ਹੱਲ ਕਰਨ](./getting_started/troubleshooting.md)

### ਮਾਇਕਰੋਸੌਫਟ ਖ਼ਾਸ ਗਾਈਡ
> [!NOTE]
> ਸਿਰਫ ਮਾਇਕਰੋਸੌਫਟ “ਨਵਾਂ ਸਿੱਖਣ ਵਾਲਿਆਂ ਲਈ” ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਦੇ ਮੇਨਟੇਨਰਾਂ ਲਈ।

- [“ਹੋਰ ਕੋਰਸਾਂ” ਦੀ ਸੂਚੀ ਅਪਡੇਟ ਕਰਨਾ (ਸਿਰਫ MS Beginners ਰਿਪੋਜ਼ਿਟਰੀਜ਼ ਲਈ)](./getting_started/update-other-courses.md)

## ਸਾਨੂੰ ਸਹਾਇਤਾ ਕਰੋ ਅਤੇ ਵਿਸ਼ਵ ਪੱਧਰੀ ਸਿੱਖਿਆ ਨੂੰ فروغ ਦਿਓ

ਸਾਡੇ ਨਾਲ ਜੁੜੋ ਅਤੇ ਸਿੱਖਿਆਤਮਕ ਸਮੱਗਰੀ ਦੇ ਸੰਸਾਰ ਭਰ ਵਿੱਚ ਵੰਡਣ ਦੇ ਤਰੀਕੇ ਨੂੰ ਬਦਲੋ! GitHub ਤੇ [Co-op Translator](https://github.com/azure/co-op-translator) ਨੂੰ ⭐ ਦਿਓ ਅਤੇ ਸਿੱਖਣ ਅਤੇ ਟੈਕਨੋਲੋਜੀ ਵਿੱਚ ਭਾਸ਼ਾਈ ਬਾਧਾਵਾਂ ਨੂੰ ਮੁਕਤ ਕਰਨ ਲਈ ਸਾਡੀ ਮিছਨ ਦੀ ਸਹਾਇਤਾ ਕਰੋ। ਤੁਹਾਡਾ ਰੁਚੀ ਅਤੇ ਯੋਗਦਾਨ ਮਹੱਤਵਪੂਰਨ ਅਸਰ ਪਾਂਉਂਦੇ ਹਨ! ਕੋਡ ਯੋਗਦਾਨ ਅਤੇ ਫੀਚਰ ਸੁਝਾਵ ਹਮੇਸ਼ਾ ਸੁਆਗਤ ਹਨ।

### ਆਪਣੀ ਭਾਸ਼ਾ ਵਿੱਚ Microsoft ਸਿੱਖਿਆਤਮਕ ਸਮੱਗਰੀ ਵੇਖੋ

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

## ਵੀਡੀਓ ਪ੍ਰस्तੁਤੀਆਂ

👉 YouTube ਤੇ ਦੇਖਣ ਲਈ ਹੇਠਾਂ ਦੀ ਚਿੱਤਰ 'ਤੇ ਕਲਿੱਕ ਕਰੋ।

- **Microsoft 'ਤੇ ਖੋਲ੍ਹੋ**: Co-op Translator ਨੂੰ ਕਿਵੇਂ ਵਰਤਣਾ ਹੈ ਉੱਤੇ ਇੱਕ ਛੋਟੀ ਜਿਹੀ 18 ਮਿੰਟ ਦੀ ਪਰੀਚਿਆ ਅਤੇ ਤੇਜ਼ ਗਾਈਡ।

  [![Open at Microsoft](../../translated_images/pa/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ਯੋਗਦਾਨ

ਇਹ ਪ੍ਰੋਜੈਕਟ ਯੋਗਦਾਨ ਅਤੇ ਸੁਝਾਵਾਂ ਦਾ ਸਵਾਗਤ ਕਰਦਾ ਹੈ। ਤੁਹਾਡੀ ਰੁਚੀ Azure Co-op Translator ਵਿੱਚ ਯੋਗਦਾਨ ਦੇਣ ਵਿੱਚ ਹੈ? ਕਿਰਪਾ ਕਰਕੇ ਸਾਡਾ [CONTRIBUTING.md](./CONTRIBUTING.md) ਵੇਖੋ ਤਾਂ ਜੋ ਤੁਸੀਂ ਜਾਣ ਸਕੋ ਕਿ ਕਿਵੇਂ Co-op Translator ਨੂੰ ਹੋਰ ਸਮਝਦਾਰ ਅਤੇ ਸੌਖਾ ਬਣਾਇਆ ਜਾ ਸਕਦਾ ਹੈ।

## ਯੋਗਦਾਨਦਾਤਾ
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ਕੋਡ ਆਫ ਕੰਡਕਟ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਨੇ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ਨੂੰ ਅਪਣਾਇਆ ਹੈ।  
ਵਧੂ ਜਾਣਕਾਰੀ ਲਈ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ਵੇਖੋ ਜਾਂ ਕਿਸੇ ਵੀ ਹੋਰ ਸਵਾਲ ਜਾਂ ਟਿੱਪਣੀਆਂ ਲਈ [opencode@microsoft.com](mailto:opencode@microsoft.com) ਨਾਲ ਸੰਪਰਕ ਕਰੋ।

## ਜ਼ਿੰਮੇਵਾਰ AI

Microsoft ਸਾਡੇ ਗਾਹਕਾਂ ਨੂੰ ਸਾਡੇ AI ਉਤਪਾਦਾਂ ਨੂੰ ਜ਼ਿੰਮੇਵਾਰੀ ਨਾਲ ਵਰਤਣ ਵਿੱਚ ਮਦਦ ਕਰਨ, ਸਾਡੇ ਸਿੱਖਿਆਈਆਂ ਸਾਂਝੀਆਂ ਕਰਨ ਅਤੇ Transparency Notes ਅਤੇ Impact Assessments ਵਰਗੇ ਟੂਲਾਂ ਰਾਹੀਂ ਭਰੋਸੇਮੰਦ ਭਾਈਚਾਰਿਆਂ ਦਾ ਨਿਰਮਾਣ ਕਰਨ ਲਈ ਵਚਨਬੱਧ ਹੈ। ਇਹਨਾਂ ਵਿੱਚੋਂ ਬਹੁਤ ਸਾਰੇ ਸਾਧਨ [https://aka.ms/RAI](https://aka.ms/RAI) 'ਤੇ ਉਪਲੱਬਧ ਹਨ।  
Microsoft ਦੇ ਜ਼ਿੰਮੇਵਾਰ AI ਲਈ ਦ੍ਰਿਸ਼ਟਿਕੋਣ ਸਾਡੇ AI ਦੇ ਸਿਧਾਂਤਾਂ 'ਤੇ ਆਧਾਰਿਤ ਹੈ ਜੋ ਨਿਆਂਸਪੱਦਤਾ, ਭਰੋਸੇਯੋਗਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਗੁਪਤਤਾ ਅਤੇ ਸੁਰੱਖਿਆ, ਸਾਮਿਲ ਹੋਣ, ਪਾਰਦਰਸ਼ੀਤਾ ਅਤੇ ਜਵਾਬਦੇਹੀ ਦਾ ਹੁੰਦਾ ਹੈ।

ਵੱਡੇ ਪੈਮਾਨੇ ਤੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ, ਚਿੱਤਰ ਅਤੇ ਸਪੀਚ ਮਾਡਲ - ਜਿਵੇਂ ਕਿ ਇਸ ਨਮੂਨੇ ਵਿੱਚ ਵਰਤੇ ਗਏ - ਸੰਭਾਵਿਤ ਤੌਰ 'ਤੇ ਅਣਨਿਆਂਸਪੱਦ, ਅਭਰਾਮਣीय ਜਾਂ ਅਪਮਾਨਜਨਕ ਤਰੀਕਿਆਂ ਨਾਲ ਵਰਤਾਰ ਕਰ ਸਕਦੇ ਹਨ, ਜਿਸ ਨਾਲ ਨੁਕਸਾਨ ਹੋ ਸਕਦਾ ਹੈ। ਕਿਰਪਾ ਕਰਕੇ ਖਤਰੇ ਅਤੇ ਸੀਮਾਵਾਂ ਬਾਰੇ ਜਾਣਕਾਰੀ ਲਈ [Azure OpenAI ਸੇਵਾ Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ਨੂੰ ਵੇਖੋ।

ਇਨ੍ਹਾਂ ਖਤਰਨਾਂ ਨੂੰ ਘਟਾਉਣ ਦਾ ਸਿਫਾਰਸ਼ੀ ਤਰੀਕਾ ਤੁਹਾਡੇ ਆਰਕੀਟੈਕਚਰ ਵਿੱਚ ਇੱਕ ਸੁਰੱਖਿਆ ਪ੍ਰਣਾਲੀ ਸ਼ਾਮਲ ਕਰਨਾ ਹੈ, ਜੋ ਨੁਕਸਾਨਦਾਇਕ ਵਿਹਾਰ ਦਾ ਪਤਾ ਲਗਾ ਸਕੇ ਅਤੇ ਰੋਕ ਸਕੇ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ਇੱਕ ਸੁਤੰਤਰ ਪਰਤ ਸੁਰੱਖਿਆ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ, ਜੋ ਐਪਲੀਕੇਸ਼ਨ ਅਤੇ ਸੇਵਾਵਾਂ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਉਪਭੋਗਤਾ ਅਤੇ AI ਦੁਆਰਾ ਬਣਾਇਆ ਸਮੱਗਰੀ ਪਛਾਣ ਸਕਦਾ ਹੈ। Azure AI Content Safety ਵਿੱਚ ਟੈਕਸਟ ਅਤੇ ਚਿੱਤਰ API ਸ਼ਾਮਲ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦਾ ਪਤਾ ਲਗਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦੇ ਹਨ। ਸਾਡੇ ਕੋਲ ਇੱਕ ਇੰਟਰਐਕਟਿਵ Content Safety Studio ਵੀ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਵਿਕਲਪ, ਖੋਜ ਅਤੇ ਵੱਖ-ਵੱਖ ਮਾਡਾਲਿਟੀਆਂ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਸਮੱਗਰੀ ਦੀ ਪਛਾਣ ਲਈ ਨਮੂਨਾ ਕੋਡ ਦੇਖਣ ਅਤੇ ਕੋਸ਼ਿਸ਼ ਕਰਨ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ। ਹੇਠਾਂ ਦਿੱਤੀ [quickstart ਦਸਤਾਵੇਜ਼ੀ] (https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ਤੁਹਾਨੂੰ ਸੇਵਾ ਨੂੰ ਬੇਨਤੀ ਭੇਜਣ ਲਈ ਰਾਹ ਪਰ ਦਿਖਾਉਂਦੀ ਹੈ।

ਇੱਕ ਹੋਰ ਪੱਖ ਜੋ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਚਾਹੀਦਾ ਹੈ ਉਹ ਹੈ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ। ਬਹੁ-ਮਾਡਾਲ ਅਤੇ ਬਹੁ-ਮਾਡਲ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨਾਲ, ਅਸੀਂ ਕਾਰਗੁਜ਼ਾਰੀ ਦਾ ਅਰਥ ਲੈਂਦੇ ਹਾਂ ਕਿ ਪ੍ਰਣਾਲੀ ਤੁਹਾਡੇ ਅਤੇ ਤੁਹਾਡੇ ਯੂਜ਼ਰਾਂ ਦੀ ਉਮੀਦਾਂ ਮੁਤਾਬਕ ਕੰਮ ਕਰਦੀ ਹੈ, ਜਿਸ ਵਿੱਚ ਨੁਕਸਾਨਦਾਇਕ ਨਤੀਜੇ ਨਾ ਬਣਾਉਣਾ ਵੀ ਸ਼ਾਮਲ ਹੈ। ਤੁਹਾਡੇ ਸਮੁੱਚੇ ਐਪਲੀਕੇਸ਼ਨ ਦੀ ਕਾਰਗੁਜ਼ਾਰੀ ਮੁਲਾਂਕਣ ਲਈ [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ਦਾ ਇਸਤੇਮਾਲ ਕਰਨਾ ਜ਼ਰੂਰੀ ਹੈ।

ਤੁਸੀਂ ਆਪਣੇ ਵਿਕਾਸ ਮਾਹੌਲ ਵਿੱਚ ਆਪਣੀ AI ਐਪਲੀਕੇਸ਼ਨ ਦਾ ਮੁਲਾਂਕਣ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ਨੂੰ ਵਰਤ ਕੇ ਕਰ ਸਕਦੇ ਹੋ। ਜਾਂ ਤਾਂ ਕਿਸੇ ਟੈਸਟ ਡੇਟਾ ਸੈੱਟ ਜਾਂ ਟਾਰਗਟ ਦੇ ਨਾਲ, ਤੁਹਾਡੇ ਜੇਨੇਰੇਟਿਵ AI ਐਪਲੀਕੇਸ਼ਨ ਦੀਆਂ ਜੇਨੇਰੇਸ਼ਨਾਂ ਨੂੰ ਬਿਲਟ-ਇਨ ਜਾਂ ਤੁਹਾਡੇ ਚੋਣ ਦੇ ਕਸਟਮ ਮੁਲਾਂਕਣਕਾਰਾਂ ਨਾਲ ਮਾਤਰਾਤਮਕ ਤੌਰ 'ਤੇ ਮਾਪਿਆ ਜਾਂਦਾ ਹੈ। ਪ੍ਰਣਾਲੀ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਲਈ prompt flow sdk ਨਾਲ ਸ਼ੁਰੂ ਕਰਨ ਲਈ, ਤੁਸੀਂ [quickstart ਗਾਈਡ](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ਬਰਤ ਸਕਦੇ ਹੋ। ਇੱਕ ਵਾਰੀ ਮੁਲਾਂਕਣ ਚੱਲਾਉਣ ਤੋਂ ਬਾਅਦ, ਤੁਸੀਂ ਨਤੀਜੇ [Azure AI Studio ਵਿੱਚ ਵੇਖ ਸਕਦੇ ਹੋ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ਟਰੇਡਮਾਰਕ

ਇਸ ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ ਹੋ ਸਕਦਾ ਹੈ ਕਿਸੇ ਪ੍ਰੋਜੈਕਟ, ਉਤਪਾਦ ਜਾਂ ਸੇਵਾਵਾਂ ਲਈ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਸ਼ਾਮਲ ਹੋਣ। Microsoft ਦੀ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦੇ ਅਧਿਕਾਰਤ ਇਸਤੇਮਾਲ ਨੂੰ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ਅਨੁਸਾਰ ਕਰਨਾ ਜਰੂਰੀ ਹੈ।  
ਇਸ ਪ੍ਰੋਜੈਕਟ ਦੇ ਸੰਸ਼ੋਧਿਤ ਸੰਸਕਰਣਾਂ ਵਿੱਚ Microsoft ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦਾ ਇਸਤੇਮਾਲ Microsoft ਦੇ ਪ੍ਰਿਯੋਜਕਤਾ ਜਾਂ ਸਹਿਯੋਗ ਨੂੰ ਧੋਖਾ ਨਹੀਂ ਦੇਣਾ ਚਾਹੀਦਾ।  
ਤੀਜਿਆਂ ਪੱਖ ਦੇ ਟਰੇਡਮਾਰਕ ਜਾਂ ਲੋਗੋ ਦਾ ਇਸਤੇਮਾਲ ਉਨ੍ਹਾਂ ਦੀਆਂ ਨੀਤੀਆਂ ਅਨੁਸਾਰ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।

## ਮਦਦ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ

ਜੇ ਤੁਸੀਂ ਫਸੇ ਹੋ ਜਾਂ AI ਐਪ ਬਣਾਉਣ ਬਾਰੇ ਕੋਈ ਸਵਾਲ ਹੈ, ਤਾਂ ਜੁੜੋ:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਉਤਪਾਦ ਦੇ ਫੀਡਬੈਕ ਜਾਂ ਗਲਤੀਆਂ ਹਨ ਤਾਂ ਦਰਜ ਕਰੋ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ਅਸਵੀਕਾਰ ਕਰਨਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਡ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਟਰਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸ੍ਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਾਨਵ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਮੀ ਜਾਂ ਭ੍ਰਮ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->