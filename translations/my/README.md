<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:18:32+00:00",
  "source_file": "README.md",
  "language_code": "my"
}
-->
# Co-op Translator

_သင်၏ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများကို အလွယ်တကူ ဘာသာစကားအမျိုးမျိုးသို့ အလိုအလျောက်ဘာသာပြန်နိုင်ပြီး ကမ္ဘာတစ်ဝှမ်းလုံးမှ ပရိသတ်များထံသို့ ရောက်ရှိစေပါသည်။_

### 🌐 ဘာသာစကားအမျိုးမျိုးအတွက် ထောက်ပံ့မှု

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) မှ ထောက်ပံ့ထားသည်

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## အနှစ်ချုပ်

**Co-op Translator** သည် သင်၏ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများကို ဘာသာစကားအမျိုးမျိုးသို့ အလျင်အမြန် ဘာသာပြန်နိုင်စေပြီး ကမ္ဘာတစ်ဝှမ်းလုံးမှ ပရိသတ်များထံသို့ လွယ်ကူစွာ ရောက်ရှိစေပါသည်။ သင်၏ Markdown ဖိုင်များ၊ ပုံများ သို့မဟုတ် Jupyter notebooks များကို ပြင်ဆင်သည့်အခါ ဘာသာပြန်ချက်များကို အလိုအလျောက် တစ်ပြိုင်နက်တည်း အပ်ဒိတ်လုပ်ပေးသဖြင့် သင်၏ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများသည် နိုင်ငံတကာအသုံးပြုသူများအတွက် အမြဲတမ်း အသစ်နဲ့ သက်ဆိုင်မှုရှိနေစေပါသည်။

Co-op Translator သည် ဘာသာပြန်ထားသော ပညာရေးဆိုင်ရာ GitHub အကြောင်းအရာများကို မည်သို့ စီမံခန့်ခွဲထားသည်ကို ကြည့်ပါ။

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.my.png)

## အလွယ်တကူ စတင်အသုံးပြုရန်

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

## အနည်းဆုံးလိုအပ်ချက်များ

- `.env` ဖိုင်ကို ဒီ template ကို အသုံးပြုပြီး ဖန်တီးပါ - [.env.template](../../.env.template)
- LLM provider တစ်ခု (Azure OpenAI သို့မဟုတ် OpenAI) ကို ပြင်ဆင်ပါ
- ပုံများကို ဘာသာပြန်လိုပါက (`-img`), Azure AI Vision ကိုလည်း ပြင်ဆင်ပါ
- အကြံပြုချက် - အခြား tool များဖြင့် ဖန်တီးထားသော ဘာသာပြန်ချက်များရှိပါက ပထမဦးဆုံး သန့်ရှင်းအောင် ဖျက်ပါ (ဥပမာ - `translations/`).
- အကြံပြုချက် - README တွင် ဘာသာပြန်ချက်များအတွက် [README languages template](./README_languages_template.md) ကို အသုံးပြု၍ အပိုင်းတစ်ခု ထည့်ပါ
- ကြည့်ရန် - [Azure AI ကို ပြင်ဆင်ခြင်း](./getting_started/set-up-azure-ai.md)

## အသုံးပြုနည်း

ထောက်ပံ့ထားသော အမျိုးအစားအားလုံးကို ဘာသာပြန်ရန် -

```bash
translate -l "ko ja"
```

Markdown သာသာ -

```bash
translate -l "de" -md
```

Markdown + ပုံများ -

```bash
translate -l "pt" -md -img
```

Notebooks သာသာ -

```bash
translate -l "zh" -nb
```

နောက်ထပ် flag များ - [Command reference](./getting_started/command-reference.md)

## အင်္ဂါရပ်များ

- Markdown, notebook, ပုံများအတွက် အလိုအလျောက် ဘာသာပြန်ခြင်း
- မူရင်းအကြောင်းအရာ ပြောင်းလဲသည့်အခါ ဘာသာပြန်ချက်များကို တစ်ပြိုင်နက်တည်း ထိန်းသိမ်းပေးခြင်း
- ဒေသတွင်း (CLI) သို့မဟုတ် CI (GitHub Actions) မှ အသုံးပြုနိုင်ခြင်း
- Azure OpenAI သို့မဟုတ် OpenAI ကို အသုံးပြုသည်၊ ပုံများအတွက် Azure AI Vision ကို ရွေးချယ်အသုံးပြုနိုင်သည်
- Markdown format နှင့် ဖွဲ့စည်းပုံကို ထိန်းသိမ်းပေးသည်

## စာရွက်စာတမ်းများ

- [Command-line လမ်းညွှန်](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions လမ်းညွှန် (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions လမ်းညွှန် (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [ထောက်ပံ့ထားသော ဘာသာစကားများ](./getting_started/supported-languages.md)
- [ပြဿနာဖြေရှင်းနည်း](./getting_started/troubleshooting.md)

## ကျွန်ုပ်တို့ကို ထောက်ပံ့ပြီး ကမ္ဘာလုံးဆိုင်ရာ ပညာရေးကို တိုးတက်စေပါ

ပညာရေးအကြောင်းအရာများကို ကမ္ဘာတစ်ဝှမ်းလုံးတွင် မျှဝေရန် လှုပ်ရှားမှုတွင် ပါဝင်ပါ! [Co-op Translator](https://github.com/azure/co-op-translator) ကို GitHub တွင် ⭐ ပေးပြီး သင်ယူခြင်းနှင့် နည်းပညာအတွက် ဘာသာစကားအတားအဆီးများကို ချိုးဖျက်ရန် ကျွန်ုပ်တို့၏ ရည်ရွယ်ချက်ကို ထောက်ပံ့ပါ။ သင်၏စိတ်ဝင်စားမှုနှင့် ပါဝင်ဆောင်ရွက်မှုများသည် အရေးပါသော သက်ရောက်မှုရှိစေပါသည်။ ကုဒ်ပံ့ပိုးမှုများနှင့် အင်္ဂါရပ်အကြံပြုမှုများကို အမြဲကြိုဆိုပါသည်။

### သင်၏ဘာသာစကားဖြင့် Microsoft ပညာရေးအကြောင်းအရာများကို ရှာဖွေပါ

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

Co-op Translator အကြောင်း ပိုမိုသိရှိလိုပါက ကျွန်ုပ်တို့၏ တင်ဆက်ချက်များကို ကြည့်ရှုနိုင်ပါသည် _(အောက်ပါပုံကို နှိပ်၍ YouTube တွင် ကြည့်ရှုနိုင်သည်)_:

- **Open at Microsoft**: မိနစ် ၁၈ ခန့် ကြာသော အကျဉ်းချုပ်နဲ့ Co-op Translator ကို မည်သို့ အသုံးပြုရမည်ကို လမ်းညွှန်ပေးထားသည်။

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.my.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ပံ့ပိုးမှုနှင့် ပါဝင်ဆောင်ရွက်ခြင်း

ဤပရောဂျက်သည် ပါဝင်ဆောင်ရွက်မှုများနှင့် အကြံပြုချက်များကို ကြိုဆိုပါသည်။ Azure Co-op Translator တွင် ပါဝင်လိုပါက [CONTRIBUTING.md](./CONTRIBUTING.md) ကို ဖတ်ရှု၍ မည်သို့ ကူညီနိုင်သည်ကို လေ့လာပါ။

## ပါဝင်သူများ

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ကျင့်ဝတ်စည်းကမ်း

ဤပရောဂျက်သည် [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ကို လိုက်နာသည်။
အသေးစိတ်အချက်အလက်များအတွက် [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ကို ကြည့်ပါ သို့မဟုတ်
မေးခွန်းများရှိပါက [opencode@microsoft.com](mailto:opencode@microsoft.com) သို့ ဆက်သွယ်နိုင်ပါသည်။

## တာဝန်ရှိသော AI

Microsoft သည် ကျွန်ုပ်တို့၏ AI ထုတ်ကုန်များကို တာဝန်ရှိစွာ အသုံးပြုနိုင်ရန် ကူညီပေးခြင်း၊ ကျွန်ုပ်တို့၏ အတွေ့အကြုံများကို မျှဝေခြင်းနှင့် Transparency Notes နှင့် Impact Assessments ကဲ့သို့သော ကိရိယာများဖြင့် ယုံကြည်မှုအပေါ် အခြေခံသော မိတ်ဖက်ဆက်ဆံရေးများ တည်ဆောက်ခြင်းတို့ကို ကတိပြုထားပါသည်။ ဤအရင်းအမြစ်များအနက် အများစုကို [https://aka.ms/RAI](https://aka.ms/RAI) တွင် ရှာဖွေနိုင်ပါသည်။
Microsoft ၏ တာဝန်ရှိသော AI အပေါ် သဘောထားသည် တရားမျှတမှု၊ ယုံကြည်စိတ်ချရမှုနှင့် လုံခြုံမှု၊ ကိုယ်ရေးအချက်အလက်နှင့် လုံခြုံရေး၊ ပါဝင်နိုင်မှု၊ ပွင့်လင်းမြင်သာမှုနှင့် တာဝန်ယူမှုတို့ကို အခြေခံထားပါသည်။

ဤနမူနာတွင် အသုံးပြုထားသည့် အကြီးစား သဘာဝဘာသာစကား၊ ပုံနှင့် အသံမော်ဒယ်များသည် တရားမျှတမှုမရှိခြင်း၊ ယုံကြည်စိတ်ချရမှုမရှိခြင်း သို့မဟုတ် စိတ်ထိခိုက်စေသော အပြုအမူများ ပြုလုပ်နိုင်သဖြင့် အန္တရာယ်များ ဖြစ်ပေါ်နိုင်ပါသည်။ အန္တရာယ်များနှင့် ကန့်သတ်ချက်များအကြောင်း သိရှိရန် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ဖတ်ရှုပါ။

ဤအန္တရာယ်များကို လျှော့ချရန် အကြံပြုချက်မှာ သင့်စနစ်အတွင်း အန္တရာယ်ရှိသော အပြုအမူများကို ရှာဖွေနိုင်ပြီး တားဆီးနိုင်သော လုံခြုံရေးစနစ်တစ်ခု ထည့်သွင်းပါ။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) သည် လွတ်လပ်သော ကာကွယ်ရေးအလွှာတစ်ခုဖြစ်ပြီး အသုံးပြုသူများဖန်တီးသောအကြောင်းအရာနှင့် AI ဖန်တီးသောအကြောင်းအရာများအနက် အန္တရာယ်ရှိသောအရာများကို ရှာဖွေနိုင်ပါသည်။ Azure AI Content Safety တွင် စာသားနှင့် ပုံ API များပါဝင်ပြီး အန္တရာယ်ရှိသောအကြောင်းအရာများကို ရှာဖွေနိုင်ပါသည်။ Content Safety Studio ကိုလည်း အသုံးပြု၍ modality များစွာအတွက် အန္တရာယ်ရှိသောအကြောင်းအရာများကို ကြည့်ရှု၊ စမ်းသပ်နိုင်ပါသည်။ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) တွင် ဝန်ဆောင်မှုသို့ တောင်းဆိုမှုများ ပြုလုပ်နည်းကို လမ်းညွှန်ပေးထားပါသည်။
တစ်ခုထပ်ပြီးစဉ်းစားရမယ့်အချက်ကတော့ အပလီကေးရှင်းရဲ့ စုစုပေါင်းလုပ်ဆောင်ရည်ပါ။ မူလတန်းအမျိုးမျိုးနဲ့ မော်ဒယ်အမျိုးမျိုးပါဝင်တဲ့အပလီကေးရှင်းတွေမှာ လုပ်ဆောင်ရည်ဆိုတာ သင်နဲ့ သုံးစွဲသူတွေ မျှော်လင့်ထားသလို စနစ်က အလုပ်လုပ်ပေးတာ၊ အန္တရာယ်ရှိတဲ့ output မထုတ်ပေးတာပါ။ သင့်အပလီကေးရှင်းရဲ့ စုစုပေါင်းလုပ်ဆောင်ရည်ကို [generation quality နဲ့ risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) တွေနဲ့ တိုင်းတာသုံးသပ်ဖို့ အရေးကြီးပါတယ်။

သင့်ရဲ့ AI အပလီကေးရှင်းကို development environment မှာ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ကိုသုံးပြီး တိုင်းတာနိုင်ပါတယ်။ Test dataset တစ်ခုဖြစ်စေ၊ target တစ်ခုဖြစ်စေ၊ သင့်ရဲ့ generative AI application ရဲ့ output တွေကို built-in evaluators သို့မဟုတ် သင်ရွေးချယ်ထားတဲ့ custom evaluators တွေနဲ့ တိုင်းတာနိုင်ပါတယ်။ prompt flow sdk ကိုသုံးပြီး စနစ်ကို တိုင်းတာချင်ရင် [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကိုလိုက်နာနိုင်ပါတယ်။ Evaluation run တစ်ခုလုပ်ပြီးရင် [Azure AI Studio မှာ ရလဒ်တွေကို မြင်နိုင်ပါတယ်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## မှတ်ပုံတင်အမှတ်တံဆိပ်များ

ဒီ project မှာ project, product, service တွေအတွက် မှတ်ပုံတင်အမှတ်တံဆိပ် သို့မဟုတ် logo တွေပါဝင်နိုင်ပါတယ်။ Microsoft မှတ်ပုံတင်အမှတ်တံဆိပ် သို့မဟုတ် logo တွေကို သုံးခွင့်ရဖို့ [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ကိုလိုက်နာရပါမယ်။
ဒီ project ကို ပြင်ဆင်ပြီး Microsoft မှတ်ပုံတင်အမှတ်တံဆိပ် သို့မဟုတ် logo တွေသုံးတဲ့အခါ Microsoft sponsorship ဖြစ်တယ်လို့ ရှုပ်ထွေးမှုမဖြစ်စေဖို့လိုပါတယ်။
Third-party မှတ်ပုံတင်အမှတ်တံဆိပ် သို့မဟုတ် logo တွေသုံးတဲ့အခါတော့ သူတို့ရဲ့ policy ကိုလိုက်နာရပါမယ်။

## အကူအညီရယူခြင်း

AI app တွေ တည်ဆောက်တဲ့အခါ မသိတာ၊ မဖြေရှင်းနိုင်တာရှိရင် ဒီမှာ ပါဝင်ဆွေးနွေးနိုင်ပါတယ် -

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Product feedback ပေးချင်တာ၊ error တွေကြုံတွေ့ရင်တော့ ဒီမှာ ဝင်ကြည့်နိုင်ပါတယ် -

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**ဝေဖန်ချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။