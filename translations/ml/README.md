# Co-op Translator

_നിങ്ങളുടെ വിദ്യാഭ്യാസ GitHub ഉള്ളടക്കം ബഹുഭാഷകളിലായി എളുപ്പത്തിൽ ഓട്ടോമേറ്റ് ചെയ്യുകയും സംരക്ഷിക്കുകയും ചെയ്യുക, നിങ്ങളുടെ പ്രോജക്ട് വളരുന്നതിനൊപ്പം._

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

### 🌐 ബഹുഭാഷാ പിന്തുണ

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) വഴി പിന്തുണയ്ക്കുന്നു

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](./README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **പ്രാദേശികമായി ക്ലോൺ ചെയ്യാനാണോ ഇഷ്ടമുള്ളത്?**
>
> ഈ റിപ്പോസിറ്ററിയിൽ 50+ ഭാഷാ പരിഭാഷകൾ ഉൾക്കൊള്ളുന്നു, ഇത് ഡൗൺലോഡ് വലുപ്പം സിഗ്നിഫിക്കന്റ് ആയി വർദ്ധിപ്പിക്കുന്നു. പരിഭാഷകൾ ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ sparse checkout ഉപയോഗിക്കുക:
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
> ഇതോടെ കോഴ്സ് പൂർത്തിയാക്കാൻ ആവശ്യമുള്ള എല്ലാ കാര്യങ്ങളും വേഗതയേറിയ ഡൗൺലോഡോടെ ലഭിക്കും.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## അവലോകനം

**Co-op Translator** നിങ്ങളുടെ വിദ്യാഭ്യാസ GitHub ഉള്ളടക്കം എളുപ്പത്തിൽ പലഭാഷകളിലേക്കും ലൊക്കലൈസ് ചെയ്യാൻ സഹായിക്കുന്നു.  
Markdown ഫയലുകൾ, ചിത്രങ്ങൾ, അല്ലെങ്കിൽ നോട്ട്ബുക്കുകൾ അപ്‌ഡേറ്റ് ചെയ്തപ്പോൾ, പരിഭാഷകൾ ഓട്ടോം ശ്രദ്ധയിൽ പെടുത്തപ്പെടുകയും, ലോകമാകെയുള്ള പഠനാർത്ഥികൾക്ക് ഉള്ളടക്കം ശരിയായി, ഏറ്റവും പുതിയത് ആയി നിലനിൽക്കുകയും ചെയ്യും.

പരിഭാഷപ്പെട്ട ഉള്ളടക്കം എങ്ങനെ ക്രമീകരിച്ചിരിക്കുന്നതിന്റെ ഉദാഹരണം:

![Example](../../imgs/translation-ex.png)

## പരിഭാഷാ നില എങ്ങനെ മാനേജ് ചെയ്യുന്നു

Co-op Translator പരിഭാഷപ്പെട്ട ഉള്ളടക്കത്തെ **വേഴ്സൻ ചെയ്ത സോഫ്റ്റ്‌വെയർ ആർട്ടിഫാക്ടുകളായി** മാനേജ് ചെയ്യുന്നു,  
സ്ഥിരമായ ഫയലുകളെന്ന നിലയിൽ അല്ല.

ഈ ടൂൾ ഭാഷ പരിമിതമായ മെറ്റാഡേറ്റ ഉപയോഗിച്ച്   
പരിഭാഷിച്ച Markdown, ചിത്രങ്ങൾ, നോട്ട്ബുക്കുകളുടെ നില പിന്തുടരുന്നു.

ഈ രൂപകല്‍പ്പന Co-op Translatorന്:

- പഴയാതായി പോയ പരിഭാഷകൾ വിശ്വസനീയമായി കണ്ടെത്താൻ
- Markdown, ചിത്രങ്ങൾ, നോട്ട്ബുക്കുകൾ ഒന്നുപോലെ കൈകാര്യം ചെയ്യാൻ
- വേഗത്തിൽ развивается ചെയ്യുന്ന വലുതും ബഹുഭാഷാ റിപ്പോസിറ്ററികൾക്ക് സുരക്ഷിതമായി സ്കെയിൽ ചെയ്യാൻ

സോഫ്റ്റ്‌വെയർ ആശ്രിതത്വവും ആർട്ടിഫാക്ട് മാനേജ്‌മെന്റും പോലുള്ള ആധുനിക പാരമ്പര്യങ്ങളുമായി സ്വാഭാവികമായി സുഹൃദ്ബന്ധം പുലർത്തുന്നതിന് പരിഭാഷകൾ മാനേജ് ചെയ്യുന്ന ആർട്ടിഫാക്ടുകളായി മോഡൽ ചെയ്യുന്നു.

→ [പരിഭാഷ സ്ഥിതിവിവരം എങ്ങനെ മാനേജ് ചെയ്യുന്നു](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## വേഗത്തിലുള്ള തുടക്കം

```bash
# ഒരു വെർച്ച്വൽ എന്വയുമായിരിക്കണം സൃഷ്‌ടിച്ച് സജീവമാക്കുക (ശുപാർശ ചെയ്യപ്പെടുന്നു)
python -m venv .venv
# വിംഡോസ്
.venv\Scripts\activate
# മാക്ഒഎസ്/ലിനക്സ്
source .venv/bin/activate
# പാക്കേജ് ഇൻസ്റ്റാൾ ചെയ്യുക
pip install co-op-translator
# വിവർത്തനം ചെയ്യുക
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR-ൽ നിന്ന് പബ്ലിക് ഇമേജ് പുൽ ചെയ്യുക
docker pull ghcr.io/azure/co-op-translator:latest
# നിലവിലെ ഫോൾഡർ മൗണ്ട് ചെയ്തും .env നൽകിയുമായുള്ള റൺ (ബാഷ്/ഷെൽ)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## മിനിമൽ ക്രമീകരണം

1. നിങ്ങളുടെ Python പതിപ്പ് പിന്തുണയ്ക്കപ്പെടുന്നുവെന്ന് സ്ഥിരീകരിക്കുക (ഇപ്പോൾ 3.10-3.12). poetry (pyproject.toml) ഇത് സ്വയം കൈകാര്യം ചെയ്യും.  
2. .env ഫയൽ സൃഷ്ടിക്കാൻ ടെമ്പ്ലേറ്റ് ഉപയോഗിക്കുക: [.env.template](../../.env.template)  
3. ഒരു LLM പ്രൊവൈഡർ കോൺഫിഗർ ചെയ്യുക (Azure OpenAI അല്ലെങ്കിൽ OpenAI)  
4. (ഐച്ഛികം) ഇമേജ് പരിഭാഷയ്ക്കായി (`-img`), Azure AI Vision കോൺഫിഗർ ചെയ്യുക  
5. (ഐച്ഛികം) `_1`, `_2` പോലെയുള്ള പൂർകങ്ങളുടെ വൈവിധ്യത്തോടെ പല ക്രെഡൻഷ്യൽ സെറ്റുകൾ കോൺഫിഗർ ചെയ്യാം. ഒരു സെറ്റിലെ എല്ലാ വേരിയബിളുകളും ഒരേ പൂർകം പങ്കുവെക്കണം.  
6. (ശിപാർശ) മുൻ പരിഭാഷകൾ ക്ലീൻ ചെയ്യുക, സംഘർഷം ഒഴിവാക്കാൻ (ഉദാ: `translations/`)  
7. (ശിപാർശ) നിങ്ങളുടെ READMEയിൽ പരിഭാഷാ വിഭാഗം ചേർക്കുക [README languages template](./getting_started/README_languages_template.md) ഉപയോഗിച്ച്  
8. കാണുക: [Azure AI ക്രമീകരിക്കൽ](./getting_started/set-up-azure-ai.md)

## ഉപയോഗം

മേൽ പറഞ്ഞ എല്ലാ പിന്തുണയുള്ള തരം ഫയലുകളും പരിഭാഷ ചെയ്യുക:

```bash
translate -l "ko ja"
```
  
Markdown മാത്രം:

```bash
translate -l "de" -md
```
  
Markdown + ചിത്രങ്ങൾ:

```bash
translate -l "pt" -md -img
```
  
നോട്ട്ബുക്കുകൾ മാത്രം:

```bash
translate -l "zh" -nb
```
  
കൂടുതൽ ഫ്ലാഗുകൾ: [കമാൻഡ് റഫറൻസ്](./getting_started/command-reference.md)

## സവിശേഷതകൾ

- Markdown, നോട്ട്ബുക്കുകൾ, ചിത്രങ്ങൾ എന്നിവയ്ക്കുള്ള ഓട്ടോമേറ്റഡ് പരിഭാഷ  
- സ്രോതസ്സ് മാറ്റങ്ങളോടൊപ്പം പരിഭാഷകൾ സമനം നിലനിർ‍ത്തുന്നു  
- ലോക്കലിലും (CLI) CI-ലും (GitHub Actions) പ്രവർത്തിക്കുന്നു  
- Azure OpenAI അല്ലെങ്കിൽ OpenAI ഉപയോഗിക്കുന്നു; ഇമേജുകൾക്കായി ഐച്ഛികമായി Azure AI Vision  
- Markdown ഫോർമാറ്റും ഘടനയും സംരക്ഷിക്കുന്നു

## ഡോക്യൂമെന്റേഷൻ

- [കമാൻഡ്-ലൈൻ ഗൈഡ്](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions ഗൈഡ് (പബ്ലിക് റിപ്പോസിറ്ററികളും സ്റ്റാൻഡേർഡ് സീക്രറ്റുകളുമാണ്)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions ഗൈഡ് (Microsoft ഓർഗനൈസേഷൻ റിപ്പോസിറ്ററികളും ഓർഗനൈസേഷൻ-ലവൽ ക്രമീകരണങ്ങളും)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README ഭാഷാ ടെമ്പ്ലേറ്റ്](./getting_started/README_languages_template.md)  
- [പിന്തുണയുള്ള ഭാഷകൾ](./getting_started/supported-languages.md)  
- [കൊള്ളുവാൻ](./CONTRIBUTING.md)  
- [പ്രശ്നപരിഹാരം](./getting_started/troubleshooting.md)

### Microsoft-നിഷ്ഠ ഗൈഡ്
> [!NOTE]
> Microsoft “For Beginners” റിപ്പോസിറ്ററികളുടെ മാത്രം പരിപാലകർക്ക്.

- [“മറ്റ് കോഴ്സുകൾ” പട്ടിക അപ്‌ഡേറ്റ് ചെയ്യൽ (MS Beginners റിപ്പോസിറ്ററികൾക്ക് മാത്രം)](./getting_started/update-other-courses.md)

## ഞങ്ങളെ പിന്തുണച്ച് ആഗോള പഠനം വളർത്തുക

വിദ്യാഭ്യാസ ഉള്ളടക്കം ആഗോള തലത്തിൽ പങ്കുവെക്കുന്നതിന് വിപ്ലവം സൃഷ്ടിക്കുന്നതിന് ഞങ്ങളോടൊപ്പം ചേരൂ! GitHub-ൽ [Co-op Translator](https://github.com/azure/co-op-translator) ന് ⭐ തരുക, പഠനത്തിലും സാങ്കേതിക മേഖലയിലും ഭാഷാ തടസ്സങ്ങൾ മറികടക്കാനുള്ള നമ്മുടെ ദൗത്യം പിന്തുണയ്ക്കൂ. നിങ്ങളുടെ താല്പര്യവും സംഭാവനകളും വലിയ സ്വാധീനം ചെലുത്തുന്നു! കോഡ് സംഭാവനകളും ഫീചർ നിർദ്ദേശങ്ങളും എപ്പോഴും സ്വാഗതം ചെയ്യപ്പെടുന്നു.

### Microsoft വിദ്യാഭ്യാസ ഉള്ളടക്കം നിങ്ങളുടെ ഭാഷയിൽ അന്വേഷിക്കുക

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

## വീഡിയോ പ്രദർശനങ്ങൾ

👉 താഴെ ചിത്രത്തിൽ ക്ലിക്ക് ചെയ്ത് YouTube-ൽ കാണുക.

- **Open at Microsoft**: Co-op Translator ഉപയോഗിക്കാൻ ഒരു സിനിമാറ്റ് 18 മിനിറ്റ് മുൻപറിയിപ്പും ഷോർട്ട് ഗൈഡും.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## സംഭാവനകൾക്ക് സ്വാഗതം

ഈ പ്രോജക്റ്റ് സംഭാവനകൾക്കും നിർദ്ദേശങ്ങൾക്കും തുറന്നതാണ്. Azure Co-op Translator-നു സംഭാവന ചെയ്യാൻ താൽപ്പര്യമുണ്ടോ? Co-op Translator മികവ് നന്നാക്കുന്നതിന് സഹായിക്കുന്നതിനുള്ള മാർഗ്ഗങ്ങൾക്കായി ഞങ്ങളുടെ [CONTRIBUTING.md](./CONTRIBUTING.md) കാണുക.

## സംഭാവകര്‍
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## കോഡിന്റെ പെരുമാറ്റം

ഈ പദ്ധതി [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) സ്വീകരിച്ചിട്ടുണ്ട്. കൂടുതൽ വിവരംക്കായി [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) കാണുക അല്ലെങ്കിൽ
ഏതെങ്കിലും അധിക ചോദ്യങ്ങൾക്കോ അഭിപ്രായങ്ങളിക്കോ [opencode@microsoft.com](mailto:opencode@microsoft.com) എന്ന വിലാസത്തിൽ ബന്ധപ്പെടുക.

## ഉത്തരവാദിത്വമുള്ള AI

Microsoft നമ്മുടെ ഉപഭോക്താക്കളെ അവരുടെ AI ഉൽപ്പന്നങ്ങൾ ഉത്തരവാദിത്വത്തോടെ ഉപയോഗിക്കാൻ സഹായിക്കാൻ, നമ്മുടെ പഠനങ്ങൾ പങ്കിടാൻ, Transparency Notes, Impact Assessments പോലുള്ള ഉപകരണങ്ങളുടെ സഹായത്തോടെ വിശ്വാസംപുറത്തൻ കൂട്ടാളിത്തങ്ങൾ നിർമ്മിക്കാൻ പ്രതിജ്ഞാബദ്ധമാണ്. [https://aka.ms/RAI](https://aka.ms/RAI) എന്ന ലിങ്കിൽ ഈ വിഭവങ്ങളിൽ പലതും ലഭ്യമാണ്.  
Microsoftന്റെ ഉത്തരവാദിത്വമുള്ള AI സമീപനം, നീതിമാനം, വിശ്വാസ്യതയും സുരക്ഷയും, സ്വകാര്യതയും സംരക്ഷണം, ഉൾക്കൊള്ളൽ, ഉദ്‌വേഗത, ഉത്തരവാദിത്വം തുടങ്ങിയ AI സിദ്ധാന്തങ്ങളിൽ ആടിസ്ഥാനമാണ്.

ഈ ഉദാഹരണത്തിൽ ഉപയോഗിക്കുന്നവ പോലുള്ള വൻതോതിലുള്ള പ്രകൃതി ഭാഷ, ചിത്രം, സംസാരം മോഡലുകൾ അസമതുല്യത, വിശ്വാസരഹിതം, അപമാനകരമാകുന്ന രീതിയിൽ പ്രവർത്തിക്കാൻ സാധ്യതയുള്ളവയാണ്, അതേവിധം ഹാനികരമായ സാഹചര്യങ്ങൾ സൃഷ്ടിക്കാം. ദയവായി [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) സന്ദർശിച്ചു അപകടങ്ങളും പരിധികളും സംബന്ധിച്ച വിവരം അറിയുക.

ഈ അപകടങ്ങളെ കുറയ്ക്കാൻ ശിപാർശ ചെയ്യുന്ന സമീപനം നിങ്ങളുടെ രൂപകൽപ്പനയിൽ സുരക്ഷാ സിസ്റ്റം ഉൾപ്പെടുത്തലാണ്, ഇത് ഹാനികരമായ പെരുമാറ്റം കണ്ടെത്താനും തടയാനുമാകും. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) സ്വതന്ത്ര സംരക്ഷണ പാളി നൽകുന്നു, ഇത് ആപ്ലിക്കേഷനുകളിലും സേവനങ്ങളിലും ഹാനികരമായ ഉപയോക്തൃ-സൃഷ്ടിയും AI-സൃഷ്ടിയുമായ ഉള്ളടക്കം കണ്ടെത്താൻ കഴിയും. Azure AI Content Safetyയുടെ ഭാഗമായിട്ടുള്ള ടെക്സ്റ്റും ചിത്രം APIകളും ഹാനികരമായ ഉള്ളടക്കം കണ്ടെത്താൻ സഹായിക്കുന്നു. ഇപ്പോൾ ലഭ്യമായ Content Safety Studio വഴി നിങ്ങൾ ഹാനികരമായ ഉള്ളടക്കം വിവിധ അവതരണങ്ങളിലൂടെ കണ്ടെത്താൻ സാമ്പിൾ കോഡ് കാണുകയും പരീക്ഷിക്കുകയും ചെയ്യാം. ഈ [quickstart ഡോക്യുമെന്റേഷൻ](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) സേവനത്തിലേക്ക് അഭ്യർത്ഥനകൾ എങ്ങനെ അയയ്ക്കാമെന്ന് മാർഗനിര്ദേശിക്കുന്നു.

മറ്റൊരു കാര്യം പരിഗണിക്കേണ്ടത് ആപ്ലിക്കേഷൻ общей പ്രകടനമാണ്. മൾട്ടി-മൊഡൽ, മൾട്ടി-മോഡലുകൾ ഉള്ള ആപ്ലിക്കേഷനുകളിലായി, പ്രകടനം എന്നത് നിങ്ങൾക്കും നിങ്ങളുടെ ഉപയോക്താക്കൾക്കും പ്രതീക്ഷിക്കുന്നതുപോലെ സിസ്റ്റം പ്രവർത്തിക്കുന്നതും ഹാനികരമായ ഫലം സൃഷ്ടിക്കാതെ നടക്കുന്നതുമായതിനെയാണ് സൂചിപ്പിക്കുന്നത്. നിങ്ങളുടെ ആപ്ലിക്കേഷന്റെ പ്രത്യക്ഷ പ്രകടനം [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ഉപയോഗിച്ച് വിലയിരുത്തുന്നത് പ്രധാനമാണ്.

നിങ്ങളുടെ AI ആപ്ലിക്കേഷൻ വികസനപരിസരത്ത് [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ഉപയോഗിച്ചു വിലയിരുത്താം. ഒരു ടെസ്റ്റ് ഡാറ്റാസെറ്റ് അല്ലെങ്കിൽ ലക്ഷ്യം നൽകിയാൽ, നിങ്ങളുടെ ജനറേറ്റീവ് AI ആപ്ലിക്കേഷന്റെ ജനറേഷനുകൾ ഉൾപ്പെടുത്തിയിരിക്കുന്ന ഒരു വിലയിരുത്തൽ ഉപകരണത്തിലൂടെയോ നിങ്ങൾ തെരഞ്ഞെടുത്ത ഇനിപ്പറയുന്ന കസ്റ്റം വിലയിരുത്തൽ ഉപകരണത്തിലൂടെയോ സംഖ്യാ ഗണിതപരമായി അളക്കപ്പെടുന്നു. prompt flow sdk ഉപയോഗിച്ച് നിങ്ങളുടെ സിസ്റ്റം വിലയിരുത്താൻ തുടങ്ങാൻ, [quickstart ഗൈഡ്](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) പിന്തുടരാം. വിലയിരുത്തൽ നടത്തിയ ശേഷം, [Azure AI Studio-യിൽ ഫലം ദൃശ്യമാക്കാം](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ട്രേഡ്‌മാർക്കുകൾ

ഈ പദ്ധതി പദ്ധതികൾ, ഉൽപ്പന്നങ്ങൾ അല്ലെങ്കിൽ സേവനങ്ങൾ സംബന്ധിച്ച ട്രേഡ്‌മാർക്ക്‌മോ ലോഗോ മോഡലുകളോ ഉൾക്കൊള്ളാം. Microsoft ട്രേഡ്‌മാർക്കും ലോഗോകൾക്കും അനുവാദപത്രം നൽകുന്ന ഉപയോഗം [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) പാലിക്കണം.  
ഈ പദ്ധതിയുടെ പരിഷ്കൃത പതിപ്പുകളിൽ Microsoft ട്രേഡ്‌മാർക്കും ലോഗോകൾക്കും ഉപയോഗം Microsoft സംരംഭത്തോടുള്ള സംഗതിയെ വഴങ്ങിയതിന്‍റെയോ ആശയം സൃഷ്ടിച്ചതായിരിക്കരുത്.  
മൂന്ന്-പക്ഷ തകർത്തുവെച്ച ട്രേഡ്‌മാർക്ക്/ലോഗോകളുടെ ഉപയോഗം ആ മൂന്നാം-പക്ഷ നയങ്ങളുടെ വിധേയമാണ്.

## സഹായം നേടുക

AI ആപ്പുകൾ നിർമ്മിക്കുന്നതിൽ നിങ്ങൾ തടസ്സപ്പെട്ടു അല്ലെങ്കിൽ ചോദ്യങ്ങൾ ഉണ്ടെങ്കിൽ ഇവിടെ ചേർക്കുക:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ഉൽപ്പന്ന പ്രതികരണം നൽകാനോ നിർമ്മാണത്തിൽ പാളികൾ ഉണ്ടെങ്കിൽ സന്ദർശിക്കുക:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**പരാമർശം**:  
ഈ ദസ്താവേജ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്‌തതാണ്. നിജസാധ്യതക്ക് നാം പരിശ്രമിക്കുന്നെങ്കിലും, സാങ്കേതിക വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തർക്കങ്ങൾ ഉണ്ടായേക്കാമെന്നാണ് ശ്രദ്ധിക്കുക. തദ്ദേശീയ ഭാഷയിലുള്ള മ原文 ദസ്താവേജ് ഔദ്യോഗിക ഉറവിടമായി പരിഗണിക്കപ്പെടണം. അത്യാവശ്യവിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യൻമാർ ആയ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നുണ്ടാകുന്ന ഏതൊരു അനർത്ഥങ്ങളും തെറ്റൃതികളും വേണ്ടി നാം ഉത്തരവാദിത്തം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->