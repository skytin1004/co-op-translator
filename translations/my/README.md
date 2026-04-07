# Co-op Translator

_သင်၏ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများကို စီမံခန့်ခွဲရာတွင်၊ စီမံကိန်းတိုးတက်လာသည့်အချိန်အတွင်း မျိုးစုံဘာသာစကားဖြင့် အလွယ်တကူအလိုအလျောက် ဘာသာပြန်နိုင်စေရန်နှင့် ပြုစုထိန်းသိမ်းနိုင်ရန်။_

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

### 🌐 မျိုးစုံဘာသာစကား အထောက်အပံ့

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) မှထောက်ပံ့သည်

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ဒေသခံအဖြစ် Clone လုပ်လိုပါသလား?**
>
> ဤအထောက်အထားတွင် ဘာသာပြန်ဆိုချက် ၅၀ ကျော် ပါဝင်သောကြောင့် ဒေါင်းလုဒ်အရွယ်အစား ပြင်းထန်စွာ တိုးလာပါတယ်။ ဘာသာပြန်ချက်များ မပါသော မူရင်းအတိုင်း clone လုပ်လိုလျှင် sparse checkout ကို သုံးပါ။
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
> ဤနည်းဖြင့် သင်လိုအပ်သည့် အကျဉ်းချုပ်သင်တန်း အားလုံးကို ပိုမိုအမြန် ဒေါင်းလုဒ်နိုင်မည်ဖြစ်သည်။
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## အနှိုင်းအယှက်

**Co-op Translator** သည် သင်၏ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာကို မျိုးစုံဘာသာစကားဖြင့် အလွယ်တကူ ပြောင်းလဲနိုင်စေသည်။
Markdown ဖိုင်များ၊ ပုံများ၊ သို့မဟုတ် notebook များကို update လုပ်သည်နှင့်အမျှ ဘာသာပြန်ဆိုမှုများ သွားလာ အလိုအလျောက် ညှိနှိုင်းထားသည့်အတွက် ကမာပတ်တလွှားရှိ သင်ယူသူများအတွက် တိကျမှန်ကန်ပြီး နောက်ဆုံးသတင်းအချက်အလက်များကို ထိန်းသိမ်းထားပေးသည်။

ဘာသာပြန်ဆိုထားသော အကြောင်းအရာများ ပြသပုံ ဥပမာ:

![Example](../../imgs/translation-ex.png)

## ဘာသာပြန်နေရပ်ကို မည်သို့ စီမံခန့်ခွဲသည်

Co-op Translator သည် ဘာသာပြန်ဆိုထားသော အကြောင်းအရာများကို **ဗားရှင်းထုတ်လမ်း software နည်းပညာ ပစ္စည်းများ**အဖြစ် စီမံခန့်ခွဲသည်၊  
အတည်မပြုထားသော ဖိုင်များအဖြစ် မဟုတ်ပါ။

ဤကိရိယာသည် ဘာသာပြန်ဆိုထားသော Markdown, ပုံများ နှင့် notebook များ၏ အခြေအနေကို  
**ဘာသာစကား-ခွဲ Metadata** ဖြင့် ထိန်းသိမ်းထားသည်။

ဒီဒီဇိုင်းသည် Co-op Translator ကို အောက်ဖော်ပြပါအရာများ ပြုလုပ်နိုင်စေသည် -

- ဘာသာပြန်ဟောင်းပျက်များကို ယုံကြည်စိတ်ချစွာ ရှာဖွေနိုင်ခြင်း
- Markdown, ပုံများ နှင့် notebook များကို တူညီတည်ကြပ်စွာ ဆက်ဆံနိုင်ခြင်း
- မျိုးစုံဘာသာစကားများပါ အသစ်မြန်ဆန်စွာ လှုပ်ရှားနေသော ကြီးမားသော repository များတွင် လုံခြုံစိတ်ချစွာ အတိုင်းအတာချထားနိုင်ခြင်း

ဘာသာပြန်ဆိုချက်များကို စီမံထိန်းသိမ်းထားသော ပစ္စည်းများအဖြစ် ဖော်မတ်ချထားခြင်းအားဖြင့်၊  
ဘာသာပြန်လုပ်ငန်းစဉ်များသည် နောက်ဆုံးပေါ် software မူလတန်းမှ သက်ဆိုင်သော မူရေးတမ်းအခြေခံ နှင့် ပစ္စည်း စီမံခန့်ခွဲမှုနည်းလမ်းများနှင့် သဘာဝကျစွာကိုက်ညီသွားသည်။

→ [ဘာသာပြန်နေရာ စီမံခန့်ခွဲခြင်းနည်းလမ်း](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## အလျင်အမြန် စတင်ခြင်း

```bash
# ဗာချွယ်ပတ်ဝန်းကျင်တစ်ခု ဖန်တီးပြီး ဖွင့်ပါ (အကြံပြုပါသည်)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# ပက်ကေ့ဂျ်ကို တပ်ဆင်ပါ
pip install co-op-translator
# ဘာသာပြန်ပါ
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR မှ ဖျော်ဖြေမှုအပေါ်မှ ပြည်သူ့ပုံကို ဆွဲယူပါ
docker pull ghcr.io/azure/co-op-translator:latest
# လက်ရှိဖိုင်တွဲကို တပ်ဆင်ပြီး .env ကို ပေးပြီး ရယူပါ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## အနည်းဆုံး စတင်ဖြည့်စွက်ခြင်း

1. သင့်တွင် ပံ့ပိုးထားသော Python ဗားရှင်း ရှိကြောင်း သေချာစေပါ (လက်ရှိတွင် 3.10-3.12 ဖြစ်သည်)။ poetry (pyproject.toml) တွင် အလိုအလျောက် ကိစ္စယူထားသည်။
2. `.env` ဖိုင်ကို [ဒီ template](../../.env.template) ကို အသုံးပြု၍ ဖန်တီးပါ
3. LLM provider တစ်ခုကို ပြင်ဆင်ပါ (Azure OpenAI သို့မဟုတ် OpenAI)
4. (တောင်းဆိုပါက) ပုံဘာသာပြန်ရန် (`-img`), Azure AI Vision ကို သတ်မှတ်ပါ
5. (တောင်းဆိုပါက) အချက်အလက်များ တူညီသော suffix များဖြင့် တွဲဖက်ကာ မျိုးစုံသော credential အချုပ်များ ပြင်ဆင်နိုင်သည် - `_1`, `_2` စသဖြင့်။ တစ်ခုချင်းစီ အတွင်း ဥပမာအားဖြင့် suffix တွေကို အတူတူရှိရမည်။
6. (အကြံပြုချက်) ယခင်ဘာသာပြန်ချက်များကို ပြင်ဆင်ပြီး အခက်အခဲ မရှိအောင် လိုအပ်ပါက ဖျက်ပါ (ဥပမာ - `translations/`)
7. (အကြံပြုချက်) README တွင် ဘာသာပြန် အပိုင်းတစ်ခု ထည့်ရန် [README languages template](./getting_started/README_languages_template.md) ကို အသုံးပြုပါ
8. ကြည့်ပါ: [Azure AI သတ်မှတ်ခြင်း](./getting_started/set-up-azure-ai.md)

## အသုံးပြုနည်း

ပံ့ပိုးထားသော အမျိုးအစားများအားလုံး ဘာသာပြန်ဆိုပါ -

```bash
translate -l "ko ja"
```

Markdown သာမက -

```bash
translate -l "de" -md
```

Markdown + ပုံများ -

```bash
translate -l "pt" -md -img
```

Notebook သာမက -

```bash
translate -l "zh" -nb
```

အောက်ဖော်ပြပါ Flag များလည်းရှိပါသည်: [Command reference](./getting_started/command-reference.md)

## အင်္ဂါရပ်များ

- Markdown, notebook နှင့် ပုံများအတွက် အလိုအလျောက် ဘာသာပြန်မှု
- မူလအကြောင်းအရာပြောင်းလဲမှုများနှင့် လိုက်ပြီး ဘာသာပြန်ထားမှုများကို ညှိနှိုင်းထားပေးပါသည်
- ဒေသတွင်း (CLI) သို့မဟုတ် CI (GitHub Actions) တွင် အသုံးပြုနိုင်သည်
- Azure OpenAI သို့မဟုတ် OpenAI ကို အသုံးပြုသည်; ပုံများအတွက် Azure AI Vision ကို ရွေးချယ်၍ အသုံးပြုနိုင်သည်
- Markdown ဖော်မတ်နှင့် ဖွဲ့စည်းမှုကို သိမ်းဆည်းကာ ထိန်းသိမ်းထားသည်

## စာတမ်းများ

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (အများနှင့် မျှဝေသော repositories နှင့် အခြေခံ သေချာမှုများ)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft အဖွဲ့အစည်း repositories နှင့် အဖွဲ့အစည်းအဆင့် ဆက်တင်များ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Supported languages](./getting_started/supported-languages.md)
- [Contributing](./CONTRIBUTING.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

### Microsoft အတွက် သီးသန့်လမ်းညွှန်
> [!NOTE]
> Microsoft “For Beginners” repository များအတွက် သာ အသုံးပြုသူများအတွက်။

- [“အခြားသင်တန်းများ” စာရင်း ပြုပြင်ခြင်း (Microsoft Beginners repository များအတွက်သာ)](./getting_started/update-other-courses.md)

## ကျွန်ုပ်တို့အား ထောက်ခံကူညီပါနှင့် ကမ္ဘာတစ်ဝှမ်း ပညာသင်ယူမှုကို မြှင့်တင်ကြပါစို့

ပညာရေးဆိုင်ရာ အကြောင်းအရာ မျှဝေပုံကို အပြောင်းအလဲ ရှိစေဖို့ ကျွန်ုပ်တို့နှင့်ပူးပေါင်းကူညီပါ။ [Co-op Translator](https://github.com/azure/co-op-translator) ကို GitHub ပေါ်တွင် ⭐ ထိုးပြီး ကမ္ဘာတလွှား သင်ယူမှုနှင့် နည်းပညာ ဘာသာစကားကွားနားချက်များကို ဖျက်ဆီးရန် ကျွန်ုပ်တို့ရဲ့ ရည်မှန်းချက်ကို ထောက်ခံပါ။ သင်၏စိတ်ဝင်စားမှု နှင့် အထောက်အပံ့များသည် အတော်လေး အရေးကြီးသည်! စာအုပ်ပေးအပ်မှုများနှင့် အင်္ဂါရပ် အကြံအစည်များ အမြဲမကောင်းပါ။

### သင်၏ဘာသာစကားဖြင့် Microsoft ပညာရေးအကြောင်းအရာများကို ရှာဖွေပါ

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

## ဗီဒီယိုတင်ဆက်ချက်များ

👉 YouTube တွင် ကြည့်ရှုရန် အောက်ပါပုံအား နှိပ်ပါ။

- **Open at Microsoft**: Co-op Translator ကို မည်သို့ အသုံးပြုရမည်ကို အချိန်တို ၁၈ မိနစ်အတွင်း ရှင်းလင်းပြသချက်။

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ပံ့ပိုးကူညီခြင်း

ဤပရောဂျက်တွင် လှုပ်ရှားမှုနှင့် အကြံပေးချက်များကို စိတ်ဝင်စားသူများအား ဖိတ်ခေါ်သည်။ Azure Co-op Translator မှာ ပါဝင်ရန် စိတ်ဝင်စားပါသလား? ကျေးဇူးပြုပြီး ကျွန်ုပ်တို့ရဲ့ [CONTRIBUTING.md](./CONTRIBUTING.md) တွင် ပါသော လမ်းညွှန်ချက်များနှင့်အတူ အသေးစိတ် သိရှိနိုင်ပါသည်။

## ပါဝင်သောသူများ
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ကျင့်ဝတ်စည်းကမ်း

ဤပရောဂျက်သည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ကို အတည်ပြုထားသည်။
 အသေးစိတ်အချက်အလက်များအတွက် [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ကိုကြည့်ရှုပါ၊ သို့မဟုတ် ထပ်မံမေးမြန်းလိုပါက [opencode@microsoft.com](mailto:opencode@microsoft.com) ဆက်သွယ်နိုင်ပါသည်။

## တာဝန်ယူမှု AI

Microsoft သည် ကျွန်ုပ်တို့၏ AI ထုတ်ကုန်များကို တာဝန်ရှိစွာ အသုံးပြုရန်၊ ကျွန်ုပ်တို့၏သင်ခန်းစာများကို မျှဝေရန်နှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော tools များမှတဆင့် ယုံကြည်မှုအခြေစိုက် မိတ်ဖက်ဆက်ဆံရေးများ တည်ဆောက်ရန် စိတ်ဝင်စားပါသည်။ ဤအရင်းအမြစ်များ အများကြီးကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် တွေ့နိုင်သည်။
Microsoft ၏ တာဝန်ရှိသော AI ရဲ့ ရှေ့နောက်မှာ ကျွန်ုပ်တို့၏ AI မူဝါဒများဖြစ်သည့် တရားမျှတမှု၊ ယုံကြည်မှုနှင့်လုံခြုံရေး၊ ကိုယ်ရေးကိုယ်တာနှင့်လုံခြုံမှု၊ ချဲ့ထွင်ခြင်း၊ ထင်ရှားပုံနှင့် တာဝန်ယူမှုတို့အပေါ် မူတည်သည်။

ဤနမူနာတွင် သုံးထားသည့် အကြီးစား သဘာဝဘာသာစကား၊ ပုံနှင့် အသံ မော်ဒယ်များသည် မျှတမှုမရှိခြင်း၊ ယုံကြည်စိတ်ချရမှုမရှိခြင်း သို့မဟုတ် တစေတကြောင်း မကြည်သာမှုများ ဖြစ်စေခြင်းများကြောင့် ထိခိုက်မှုများ ဖြစ်ပေါ်စေနိုင်သည်။ အန္တရာယ်နှင့် ကန့်သတ်ချက်များအကြောင်း သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ကြည့်ရှုပါ။

ဤအန္တရာယ်များ လျော့နည်းစေရန် အကြံပြုနည်းမှာ သင့်၏ ဖွဲ့စည်းတည်ဆောက်မှုတွင် ထိခိုက်မှုရှိသော လုပ်ဆောင်ချက်များကို ရှာဖွေကာ တားဆီးနိုင်သော လုံခြုံရေး စနစ်တစ်ခု ထည့်သွင်းရန် ဖြစ်သည်။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် သီးသန့် အကာအကွယ်အလွှာတစ်ခုဖြစ်ပြီး၊ အသုံးပြုသူများ ထုတ်လုပ်သောနှင့် AI ထုတ်လုပ်သော အကြောင်းအရာ ထိခိုက်မှုရှိမှုများ ကို တွေ့ရှိနိုင်သည်။ Azure AI Content Safety တွင် သက်ဆိုင်ရာ စာသားနှင့် ပုံ API များ ပါဝင်ပြီး ထိခိုက်မှုရှိသော အကြောင်းအရာများ ရှာဖွေရန် အခွင့်အရေး ပေးသည်။ ဤနောက်တစ်ခုမှာ Content Safety Studio ဖြစ်ပြီး ထိခိုက်မှုရှိသော အကြောင်းအရာများကို မိုးစုံပုံစံဖြင့် သုံးသပ်၊ စမ်းသပ်နိုင်ရန် နမူနာကုဒ် များကို ကြည့်ရှုနိုင်သည်။ နောက်ဖော်ပြပါ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) သည် ဝန်ဆောင်မှုသို့ မေးမြန်းမှုများ စတင် ပြုလုပ်ပုံကို လမ်းညွှန်ပေးသည်။

အခြားတစ်ချက်မှာ စုပေါင်း application လုပ်ဆောင်ချက်ဖြစ်ပုံမှန်မှုကို စဉ်းစားရမည်ဖြစ်သည်။ မျိုးစုံဂဏန်းနှင့် မော်ဒယ်များ ပါဝင်သည့် application များတွင် စနစ်သည် သင်နှင့် သင့်အသုံးပြုသူများ ထင်မြင်လိုသောအတိုင်း လုပ်ဆောင်ရမည်မှာ အရေးကြီးသည်၊ ထိခိုက်သော output မထုတ်ပေးခြင်းပါဝင်သည်။ သင့် application တစ်ခုလုံး၏ လုပ်ဆောင်ချက်ကို [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) များဖြင့် သုံးသပ်ဖော်ထုတ်ဖို့ အရေးကြီးသည်။

သင့် AI application ကို သင်၏ ဖွံ့ဖြိုးတိုးတက်မှု ပတ်ဝန်းကျင်တွင် [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) အသုံးပြုပြီး ရှုမြင်သုံးသပ်နိုင်သည်။ စမ်းသပ်ရန် ဒေတာသို့မဟုတ် ပန်းတိုင်တစ်ခုကို အသုံးပြုကာ သင်၏ generative AI application ၏ ထုတ်နေမှုများကို ကွဲပြားသော အကဲဖြတ်သူများနှင့် သဘောတူပြီး အကဲဖြတ်ပြီး တိုင်းတာနိုင်သည်။ prompt flow SDK ဖြင့် သင့်စနစ်ကို စတင် သုံးသပ်ရန် [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကို လိုက်နာနိုင်သည်။ အကဲဖြတ်ခြင်း run တစ်ခု ပြီးဆုံးလျှင် [Azure AI Studio တွင် ရလဒ်များကို ကြည့်ရှု](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ပြုလုပ်နိုင်ပါသည်။

## ပံ့ပိုးရေးအမှတ်တံဆိပ်များ

ဤပရောဂျက်တွင် ပရောဂျက်များ၊ ထုတ်ကုန်များ သို့မဟုတ် ဝန်ဆောင်မှုများအတွက် အမှတ်တံဆိပ်များ သို့မဟုတ် အလံများ ပါဝင်နိုင်သည်။ Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် အလံများကို အသုံးပြုရန် သက်ဆိုင်ရာလိုက်နာရမည့် [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)  ကို လိုက်နာရမည်ဖြစ်သည်။
Microsoft အမှတ်တံဆိပ်များ သို့မဟုတ် အလံများကို ဤပရောဂျက်၏ ပြင်ဆင်ထားသောဗားရှင်းများတွင် အသုံးပြုခြင်းသည် သံသယဖြစ်စေနိုင်ခြင်း သို့မဟုတ် Microsoft မှ ပံ့ပိုးမှုရှိသည့်အကွက်ရှိသည်ဟု ထင်မြင်စေခြင်း မရှိရ။
တတိယ पक्ष၏ အမှတ်တံဆိပ်များ သို့မဟုတ် အလံများကို အသုံးပြုခြင်းမှာ အဆိုပါ တတိယ पक्ष၏ နိုင်ငံရေးများကိုလိုက်နာရမည်ဖြစ်သည်။

## အကူအညီရယူခြင်း

AI apps ဖန်တီးရာတွင် ခက်ခဲမှုတက်လျှင် သို့မဟုတ် မေးခွန်းများ ရှိပါက:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ထုတ်ကုန်တုံ့ပြန်ချက် သို့မဟုတ် ဖန်တီးမှုအမှားများရှိပါက သွားရောက်မြင်ရှုနိုင်ပါသည်-

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပယ်ချခြင်း**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ခြင်းဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျနော်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ စက်တင်စေမှုအရ ဘာသာပြန်ချက်များတွင် မှားယွင်းချက်များ သို့မဟုတ် အမှားများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန်။ မူလစာရွက်စာတမ်းမှာ မိသားစုဘာသာဖြင့် ရေးသားထားသည့် လက်ခံရရှိမှုအလားအလာအတွက် အထောက်အထားဖြစ်သည်ဟု သတ်မှတ်ရမည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက် အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်သော မမှန်ကန်မှုများ သို့မဟုတ် မှားယွင်းသော နားလည်မှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->