<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T14:13:16+00:00",
  "source_file": "README.md",
  "language_code": "my"
}
-->
# Co-op Translator

_သင့်ရဲ့ပညာရေးဆိုင် GitHub အကြောင်းအရာတွေကို အလွယ်တကူ ဘာသာစကားအမျိုးမျိုးသို့ အလိုအလျောက်ဘာသာပြန်ပေးနိုင်တဲ့အတွက် ကမ္ဘာတစ်ဝှမ်းလူထုကို ရောက်ရှိနိုင်ပါတယ်။_

### 🌐 ဘာသာစကားအမျိုးမျိုးကို ထောက်ပံ့ပေးထားပါတယ်

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) မှ ထောက်ပံ့ပေးထားသော ဘာသာစကားများ

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## အကျဉ်းချုပ်

**Co-op Translator** က သင့်ရဲ့ပညာရေးဆိုင် GitHub အကြောင်းအရာတွေကို ဘာသာစကားအမျိုးမျိုးသို့ အလျင်အမြန် ဘာသာပြန်ပေးနိုင်ပါတယ်။ သင့် Markdown ဖိုင်တွေ၊ ပုံတွေ၊ Jupyter notebook တွေကို update လုပ်တိုင်း ဘာသာပြန်ချက်တွေကို အလိုအလျောက် sync လုပ်ပေးလို့ ကမ္ဘာတစ်ဝှမ်းအသုံးပြုသူတွေအတွက် အကြောင်းအရာအသစ်နဲ့ သက်ဆိုင်မှုရှိနေစေပါတယ်။

Co-op Translator က ဘာသာပြန်ထားတဲ့ ပညာရေးဆိုင် GitHub အကြောင်းအရာတွေကို ဘယ်လိုစီမံထားသလဲဆိုတာကြည့်ပါ။

![ဥပမာ](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.my.png)

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

- `.env` ဖိုင်ကို template: [.env.template](../../.env.template) ကိုသုံးပြီး ဖန်တီးပါ
- LLM provider တစ်ခု (Azure OpenAI သို့မဟုတ် OpenAI) ကို configure လုပ်ပါ
- ပုံတွေကို ဘာသာပြန်ချင်ရင် (`-img`) Azure AI Vision ကိုလည်း သတ်မှတ်ပါ
- အကြံပြုချက်: အခြား tool တွေက ဘာသာပြန်ထားတဲ့ translation တွေရှိရင် ပထမဆုံး သန့်ရှင်းရေးလုပ်ပါ (ဥပမာ: `translations/`)
- အကြံပြုချက်: README မှာ ဘာသာပြန်ချက် section ထည့်ပါ [README languages template](./README_languages_template.md) ကိုသုံးပါ
- ကြည့်ရန်: [Azure AI ကို စတင်သုံးရန်](./getting_started/set-up-azure-ai.md)

## အသုံးပြုနည်း

ထောက်ပံ့ထားတဲ့ အမျိုးအစားအားလုံးကို ဘာသာပြန်ရန်:

```bash
translate -l "ko ja"
```

Markdown သာ:

```bash
translate -l "de" -md
```

Markdown + ပုံများ:

```bash
translate -l "pt" -md -img
```

Notebook သာ:

```bash
translate -l "zh" -nb
```

နောက်ထပ် flag တွေ: [Command reference](./getting_started/command-reference.md)

## လက္ခဏာများ

- Markdown, notebook, ပုံများအတွက် အလိုအလျောက် ဘာသာပြန်ပေးနိုင်ခြင်း
- Source ပြောင်းလဲမှုနဲ့ translation တွေကို အမြဲ sync လုပ်ပေးခြင်း
- Local (CLI) သို့မဟုတ် CI (GitHub Actions) မှာ အသုံးပြုနိုင်ခြင်း
- Azure OpenAI သို့မဟုတ် OpenAI ကိုသုံးပြီး ပုံအတွက် Azure AI Vision ကို optional သုံးနိုင်ခြင်း
- Markdown formatting နဲ့ structure ကို ထိန်းသိမ်းပေးခြင်း

## လမ်းညွှန်စာအုပ်များ

- [Command-line လမ်းညွှန်](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions လမ်းညွှန် (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions လမ်းညွှန် (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [ထောက်ပံ့ထားသော ဘာသာစကားများ](./getting_started/supported-languages.md)
- [ပြဿနာဖြေရှင်းနည်း](./getting_started/troubleshooting.md)

## ကျွန်ုပ်တို့ကို ထောက်ပံ့ပြီး ကမ္ဘာလုံးဆိုင် ပညာရေးကို တိုးတက်အောင်လုပ်ပါ

ပညာရေးအကြောင်းအရာတွေကို ကမ္ဘာတစ်ဝှမ်းမျှဝေဖို့ ပြောင်းလဲရေးမှာ ပါဝင်ပါ။ [Co-op Translator](https://github.com/azure/co-op-translator) ကို GitHub မှာ ⭐ ပေးပြီး သင်ယူရေးနဲ့ နည်းပညာမှာ ဘာသာစကားအတားအဆီးတွေကို ချိုးဖျက်ဖို့ ကျွန်ုပ်တို့ရဲ့ ရည်ရွယ်ချက်ကို ထောက်ပံ့ပါ။ သင့်ရဲ့စိတ်ဝင်စားမှုနဲ့ ပါဝင်မှုတွေက အရေးကြီးတဲ့ သက်ရောက်မှုရှိပါတယ်။ Code ပေးပို့ခြင်းနဲ့ feature အကြံပြုချက်တွေကို အမြဲလက်ခံပါတယ်။

### Microsoft ပညာရေးအကြောင်းအရာတွေကို သင့်ဘာသာစကားနဲ့ လေ့လာပါ

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

## ဗီဒီယို တင်ဆက်ချက်များ

Co-op Translator အကြောင်းကို ဗီဒီယိုတင်ဆက်ချက်များမှ ပိုမိုလေ့လာနိုင်ပါတယ် _(အောက်ပါပုံကိုနှိပ်ပြီး YouTube မှာကြည့်ပါ)_:

- **Open at Microsoft**: Co-op Translator ကို အသုံးပြုနည်းနဲ့ အကျဉ်းချုပ် ၁၈ မိနစ်စာ တင်ဆက်ချက်။

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.my.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## ပါဝင်ပေးနိုင်ခြင်း

ဒီ project က ပါဝင်ပေးမှုနဲ့ အကြံပြုချက်တွေကို ကြိုဆိုပါတယ်။ Azure Co-op Translator မှာ ပါဝင်ချင်ပါသလား? [CONTRIBUTING.md](./CONTRIBUTING.md) ကိုကြည့်ပြီး Co-op Translator ကို ပိုမိုလွယ်ကူစေဖို့ ဘယ်လိုကူညီနိုင်မလဲ သိနိုင်ပါတယ်။

## ပါဝင်သူများ

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## အပြုသဘောဆောင် အကျင့်စည်းကမ်း

ဒီ project မှာ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ကို လိုက်နာထားပါတယ်။
နောက်ထပ်သိချင်တာရှိရင် [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ကိုကြည့်ပါ သို့မဟုတ်
[opencode@microsoft.com](mailto:opencode@microsoft.com) ကို ဆက်သွယ်မေးမြန်းနိုင်ပါတယ်။

## တာဝန်ရှိသော AI

Microsoft က AI ထုတ်ကုန်တွေကို တာဝန်ရှိစွာ အသုံးပြုနိုင်ဖို့ ကူညီပေးနေပြီး၊ ကျွန်ုပ်တို့ရဲ့ အတွေ့အကြုံတွေကို မျှဝေသလို၊ Transparency Notes နဲ့ Impact Assessments တို့လို tools တွေဖြင့် ယုံကြည်မှုအခြေပြု မိတ်ဖက်ရေးကို တည်ဆောက်နေပါတယ်။ ဒီ resource တွေထဲက အများစုကို [https://aka.ms/RAI](https://aka.ms/RAI) မှာ ရှာနိုင်ပါတယ်။
Microsoft ရဲ့ တာဝန်ရှိသော AI အနုပညာတွေက တရားမျှတမှု၊ ယုံကြည်စိတ်ချမှုနဲ့ လုံခြုံရေး၊ ကိုယ်ရေးကိုယ်တာနှင့် လုံခြုံရေး၊ ပါဝင်မှု၊ ပွင့်လင်းမှု၊ တာဝန်ယူမှုတို့ကို အခြေခံထားပါတယ်။

သဘာဝဘာသာစကား၊ ပုံ၊ အသံ စတဲ့ မော်ဒယ်ကြီးတွေ - ဒီ sample မှာသုံးထားတဲ့အတိုင်း - တစ်ခါတစ်ရံ မျှတမှုမရှိ၊ ယုံကြည်စိတ်ချမှုမရှိ၊ သို့မဟုတ် စိတ်မဝင်စားစရာ ဖြစ်နိုင်ပါတယ်။ ဒါကြောင့် [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ကို ဖတ်ရှုပါ။

ဒီအန္တရာယ်တွေကို လျှော့ချဖို့ အကြံပြုချက်က သင့် architecture မှာ safety system တစ်ခု ထည့်သွင်းပါ။ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) က သီးခြားကာကွယ်မှုအလွှာတစ်ခုဖြစ်ပြီး၊ အသုံးပြုသူ/AI-generated အန္တရာယ်ရှိတဲ့အကြောင်းအရာတွေကို ရှာဖွေနိုင်ပါတယ်။ Azure AI Content Safety မှာ text နဲ့ image API တွေပါဝင်ပြီး အန္တရာယ်ရှိတဲ့အကြောင်းအရာတွေကို ရှာဖွေနိုင်ပါတယ်။ Content Safety Studio မှာလည်း modality အမျိုးမျိုးအတွက် harmful content ကို sample code နဲ့ စမ်းသပ်ကြည့်နိုင်ပါတယ်။ အောက်ပါ [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) မှာ service ကို request လုပ်နည်းကို လမ်းညွှန်ပေးထားပါတယ်။
တစ်ခြားစဉ်းစားစရာအချက်တစ်ခုကတော့ အပလီကေးရှင်းရဲ့ စွမ်းဆောင်ရည်ပေါင်းစုံပါ။ မျိုးစုံမော်ဒယ်နဲ့ မျိုးစုံမီဒီယာအပလီကေးရှင်းတွေအတွက် စွမ်းဆောင်ရည်ဆိုတာ သင်နဲ့ သုံးစွဲသူတွေ မျှော်လင့်သလို စနစ်က အလုပ်လုပ်နိုင်ဖို့၊ အန္တရာယ်ရှိတဲ့ output မထုတ်ပေးဖို့ပါဝင်ပါတယ်။ သင့်အပလီကေးရှင်းရဲ့ စွမ်းဆောင်ရည်ကို [generation quality နဲ့ risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) တွေနဲ့ တိုင်းတာသုံးသပ်ဖို့ အရေးကြီးပါတယ်။

သင့်ရဲ့ AI အပလီကေးရှင်းကို သင့် development environment မှာ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ကိုသုံးပြီး တိုင်းတာနိုင်ပါတယ်။ Test dataset တစ်ခုဖြစ်စေ၊ target တစ်ခုဖြစ်စေ၊ သင့်ရဲ့ generative AI application output တွေကို built-in evaluators သို့မဟုတ် သင်ရွေးချယ်ထားတဲ့ custom evaluators တွေနဲ့ တိကျစွာ တိုင်းတာနိုင်ပါတယ်။ သင့်စနစ်ကို prompt flow sdk နဲ့ စတင်တန့်သပ်ချင်ရင် [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ကိုလိုက်နာနိုင်ပါတယ်။ Evaluation run တစ်ခုလုပ်ပြီးရင် [Azure AI Studio မှာ ရလဒ်တွေကို မြင်နိုင်ပါတယ်](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)။

## ကုန်အမှတ်တံဆိပ်များ

ဒီ project မှာ project, product, service တွေအတွက် အမှတ်တံဆိပ် သို့မဟုတ် logo တွေ ပါဝင်နိုင်ပါတယ်။ Microsoft အမှတ်တံဆိပ် သို့မဟုတ် logo တွေကို ခွင့်ပြုသုံးစွဲချင်ရင် [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) ကိုလိုက်နာရပါမယ်။
ဒီ project ကို ပြင်ဆင်ထားတဲ့ version တွေမှာ Microsoft အမှတ်တံဆိပ် သို့မဟုတ် logo တွေကို သုံးစွဲတဲ့အခါ Microsoft က ပံ့ပိုးပေးတယ်လို့ သံသယမဖြစ်စေဖို့၊ သို့မဟုတ် ရှုပ်ထွေးမှုမဖြစ်စေဖို့ လိုအပ်ပါတယ်။
တတိယပါတီအမှတ်တံဆိပ် သို့မဟုတ် logo တွေကို သုံးစွဲတဲ့အခါတော့ အဲ့ဒီ တတိယပါတီရဲ့ မူဝါဒတွေကိုလိုက်နာရပါမယ်။

## အကူအညီရယူခြင်း

AI app တွေ တည်ဆောက်ရာမှာ အခက်အခဲရှိတယ်၊ မေးခွန်းရှိတယ်ဆိုရင် ဒီနေရာမှာ ပါဝင်ဆွေးနွေးနိုင်ပါတယ်-

<kbd>![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)</kbd>(https://aka.ms/foundry/discord)

Product feedback ပေးချင်တယ်၊ သို့မဟုတ် တည်ဆောက်ရာမှာ error တွေကြုံရတယ်ဆိုရင် ဒီနေရာကို သွားလေ့လာနိုင်ပါတယ်-

<kbd>![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)</kbd>(https://aka.ms/foundry/forum)

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသော ရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သော နားလည်မှုမှားများ သို့မဟုတ် အနားလည်မှုမှားများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။