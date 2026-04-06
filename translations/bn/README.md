# Co-op Translator

_আপনার শিক্ষামূলক GitHub বিষয়বস্তু বিভিন্ন ভাষায় সহজেই স্বয়ংক্রিয় অনুবাদ এবং রক্ষণাবেক্ষণ করুন যেমন আপনার প্রকল্প বিকাশ লাভ করে।_

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

### 🌐 একাধিক ভাষার সমর্থন

#### সমর্থিত [Co-op Translator](https://github.com/Azure/Co-op-Translator) দ্বারা

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **স্থানীয়ভাবে ক্লোন করতে চান?**
>
> এই রিপোজিটরিতে ৫০+ ভাষার অনুবাদ রয়েছে যা ডাউনলোড আকার উল্লেখযোগ্যভাবে বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> এটি আপনাকে দ্রুত ডাউনলোড সহ কোর্স সম্পন্ন করার জন্য সবকিছু প্রদান করবে।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ওভারভিউ

**Co-op Translator** আপনাকে সহজে আপনার শিক্ষামূলক GitHub বিষয়বস্তু বিভিন্ন ভাষায় স্থানীয়করণ করতে সাহায্য করে।  
যখন আপনি আপনার Markdown ফাইল, ছবি, বা নোটবুক আপডেট করেন, অনুবাদগুলো স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ থাকে, নিশ্চিত করে যে আপনার বিষয়বস্তু বিশ্বব্যাপী শিক্ষার্থীদের জন্য সঠিক এবং হালনাগাদ থাকে।

অনুবাদকৃত বিষয়বস্তু কিভাবে সংগঠিত তা উদাহরণ:

![Example](../../translated_images/bn/translation-ex.0c8aa6a7ee0aad2b.webp)

## অনুবাদ অবস্থা কিভাবে পরিচালিত হয়

Co-op Translator অনুবাদকৃত বিষয়বস্তু **ভার্সনকৃত সফটওয়্যার আর্টিফ্যাক্ট** হিসেবে পরিচালনা করে,  
স্থির ফাইল হিসেবে নয়।

টুলটি অনুবাদকৃত Markdown, ছবি, এবং নোটবুকের অবস্থা ট্র্যাক করে 
**ভাষা-সং scoped metadata** ব্যবহার করে।

এই নকশার মাধ্যমে Co-op Translator পারে:

- নির্ভরযোগ্যভাবে পুরানো অনুবাদ চিহ্নিত করা
- Markdown, ছবি, এবং নোটবুক সামঞ্জস্যপূর্ণভাবে পরিচালনা করা
- বড়, দ্রুত-গামী, বহুভাষিক রিপোজিটরিগুলো নিরাপদে স্কেল করা

অনুবাদগুলোকে পরিচালিত আর্টিফ্যাক্ট হিসেবে মডেল করায়,
অনুবাদ ওয়ার্কফ্লোগুলো আধুনিক  
সফটওয়্যার ডিপেন্ডেন্সি এবং আর্টিফ্যাক্ট ব্যবস্থাপনার অনুশীলনের সাথে স্বতঃসিদ্ধভাবে খাপ খায়।

→ [How translation state is managed](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## দ্রুত শুরু

```bash
# একটি ভার্চুয়াল পরিবেশ তৈরি করুন এবং সক্রিয় করুন (প্রস্তাবিত)
python -m venv .venv
# উইন্ডোজ
.venv\Scripts\activate
# ম্যাকওএস/লিনাক্স
source .venv/bin/activate
# প্যাকেজ ইনস্টল করুন
pip install co-op-translator
# অনুবাদ করুন
translate -l "ko ja fr" -md
```

ডকার:

```bash
# GHCR থেকে পাবলিক ইমেজ টানা
docker pull ghcr.io/azure/co-op-translator:latest
# বর্তমান ফোল্ডার মাউন্ট করে এবং .env সরবরাহ করে চালানো (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ন্যূনতম সেটআপ

1. নিশ্চিত করুন যে আপনার একটি সমর্থিত Python সংস্করণ রয়েছে (বর্তমানে ৩.১০-৩.১২)। poetry (pyproject.toml) এ এটি স্বয়ংক্রিয়ভাবে পরিচালিত হয়।
2. টেমপ্লেট ব্যবহার করে একটি `.env` ফাইল তৈরি করুন: [.env.template](../../.env.template)
3. একটি LLM প্রদানকারী কনফিগার করুন (Azure OpenAI অথবা OpenAI)
4. (ঐচ্ছিক) ছবি অনুবাদের জন্য (`-img`), Azure AI Vision কনফিগার করুন
5. (ঐচ্ছিক) বহু সার্টিফিকেট সেট কনফিগার করতে আপনি `_1`, `_2` ইত্যাদি সারফেক্স সহ ভেরিয়েবলগুলি পুনরাবৃত্তি করতে পারেন। একটি সেটের সব ভেরিয়েবল একই সারফেক্স ভাগ করতে হবে।
6. (প্রস্তাবিত) পূর্বের অনুবাদগুলি পরিষ্কার করুন যাতে সংঘর্ষ এড়ানো যায় (যেমন, `translations/`)
7. (প্রস্তাবিত) আপনার README তে অনুবাদের সেকশন যুক্ত করুন [README languages template](./getting_started/README_languages_template.md) ব্যবহার করে
8. দেখুন: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## ব্যবহার

সমস্ত সমর্থিত টাইপ অনুবাদ করুন:

```bash
translate -l "ko ja"
```

শুধুমাত্র Markdown:

```bash
translate -l "de" -md
```

Markdown + ছবি:

```bash
translate -l "pt" -md -img
```

শুধুমাত্র নোটবুক:

```bash
translate -l "zh" -nb
```

আরো ফ্ল্যাগ: [Command reference](./getting_started/command-reference.md)

## বৈশিষ্ট্য

- Markdown, নোটবুক, এবং ছবি জন্য স্বয়ংক্রিয় অনুবাদ
- উৎস পরিবর্তনের সাথে অনুবাদ সিঙ্ক রাখা হয়
- লোকালি (CLI) অথবা CI (GitHub Actions) এ কাজ করে
- Azure OpenAI অথবা OpenAI ব্যবহার করে; ছবি জন্য ঐচ্ছিক Azure AI Vision
- Markdown বিন্যাস এবং কাঠামো বজায় রাখে

## ডকুমেন্টেশন

- [Command-line guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Supported languages](./getting_started/supported-languages.md)
- [Contributing](./CONTRIBUTING.md)
- [Troubleshooting](./getting_started/troubleshooting.md)

### Microsoft-নির্দিষ্ট গাইড
> [!NOTE]
> শুধুমাত্র Microsoft “For Beginners” রিপোজিটরি রক্ষণাবেক্ষকদের জন্য।

- [“অন্যান্য কোর্স” তালিকা আপডেট করা (শুধুমাত্র MS Beginners রিপোজিটরি জন্য)](./getting_started/update-other-courses.md)

## আমাদের সাহায্য করুন এবং বৈশ্বিক শিক্ষা উন্নত করুন

গ্লোবালি শিক্ষামূলক বিষয়বস্তু ভাগাভাগির ধরণ বিপ্লব করার আমাদের সাথে যোগ দিন! [Co-op Translator](https://github.com/azure/co-op-translator) কে GitHub এ ⭐ দিন এবং শেখা ও প্রযুক্তিতে ভাষাগত প্রতিবন্ধকতা দূর করার আমাদের মিশনকে সমর্থন করুন। আপনার আগ্রহ এবং অবদান গুরুত্বপূর্ণ প্রভাব ফেলে! কোড অবদান এবং বৈশিষ্ট্য প্রস্তাব সবসময় স্বাগত।

### আপনার ভাষায় Microsoft শিক্ষামূলক বিষয়বস্তু অন্বেষণ করুন

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

## ভিডিও উপস্থাপনা

👉 YouTube এ দেখতে নীচের ছবিটি ক্লিক করুন।

- **Open at Microsoft**: Co-op Translator ব্যবহারের একটি সংক্ষিপ্ত ১৮-মিনিটের পরিচিতি এবং দ্রুত গাইড।

  [![Open at Microsoft](../../translated_images/bn/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## অবদান রাখা

এই প্রকল্পে অবদান এবং পরামর্শ স্বাগত। Azure Co-op Translator এ অবদান রাখতে আগ্রহী? দয়া করে আমাদের [CONTRIBUTING.md](./CONTRIBUTING.md) দেখুন যেখানে Co-op Translator কে আরও অ্যাক্সেসযোগ্য করার জন্য নির্দেশাবলী রয়েছে।

## অবদানকারী সবাই
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## আচরণবিধি

এই প্রকল্পটি [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করেছে। আরও তথ্যের জন্য দেখুন [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা
যেকোনো অতিরিক্ত প্রশ্ন বা মন্তব্যের জন্য যোগাযোগ করুন [opencode@microsoft.com](mailto:opencode@microsoft.com) এ।

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের আমাদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহারের ক্ষেত্রে সহায়তা করতে প্রতিশ্রুতিবদ্ধ, আমাদের শেখানো শেয়ার করে, এবং Transparency Notes এবং Impact Assessments-এর মতো টুলের মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তোলে। এই ধরনের অনেক রিসোর্স পাওয়া যায় [https://aka.ms/RAI](https://aka.ms/RAI) এ।
Microsoft-এর দায়িত্বশীল AI-এর দৃষ্টিভঙ্গি আমাদের AI নীতিমালা যেমন ন্যায়পরায়ণতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং দায়িত্বশীলতার ভিত্তিতে স্থাপিত।

বড় পরিসরের প্রাকৃতিক ভাষা, ছবি এবং বক্তৃতা মডেল - যেমন এই নমুনায় ব্যবহৃত হয় - সম্ভাব্য এমনভাবে আচরণ করতে পারে যা অন্যায়, অবিশ্বস্ত, বা আপত্তিকর, যার ফলে ক্ষতি হতে পারে। অনুগ্রহ করে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পরামর্শ করুন ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে অবগত থাকার জন্য।

এই ঝুঁকিগুলি কমানোর জন্য সুপারিশ করা পন্থা হল আপনার স্থাপত্যে একটি সুরক্ষা পদ্ধতি যুক্ত করা যা ক্ষতিকারক আচরণ সনাক্ত এবং প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বতন্ত্র সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন ও পরিষেবায় ক্ষতিকর ব্যবহারকারী-উত্পাদিত এবং AI-উত্পাদিত উপাদান সনাক্ত করতে সক্ষম। Azure AI Content Safety-এ টেক্সট এবং ইমেজ API রয়েছে যা আপনাকে ক্ষতিকর উপাদান সনাক্ত করতে দেয়। এছাড়াও একটি ইন্টারেক্টিভ Content Safety Studio রয়েছে যা আপনাকে বিভিন্ন মোডালিটিতে ক্ষতিকর উপাদান সনাক্তকরণের জন্য নমুনা কোড দেখার, অনুসন্ধান এবং চেষ্টা করার সুবিধা দেয়। নিম্নোক্ত [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে পরিষেবায় রিকোয়েস্ট পাঠানোর নির্দেশিকা দেয়।

আরেকটি বিষয় যা বিবেচনা করতে হবে তা হল সামগ্রিক অ্যাপ্লিকেশন কর্মক্ষমতা। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলির ক্ষেত্রে, কর্মক্ষমতা মানে হলো সিস্টেমটি আপনি এবং আপনার ব্যবহারকারীরা প্রত্যাশা করা অনুযায়ী কাজ করে, যার মধ্যে রয়েছে ক্ষতিকর আউটপুট তৈরি না করা। [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে আপনার সামগ্রিক অ্যাপ্লিকেশনের কর্মক্ষমতা মূল্যায়ন করা গুরুত্বপূর্ণ।

আপনি আপনার AI অ্যাপ্লিকেশনটি আপনার উন্নয়ন পরিবেশে [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে মূল্যায়ন করতে পারেন। একটি টেস্ট ডেটাসেট বা লক্ষ্য নিয়ে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশন জেনারেশনগুলি পরিমাণগতভাবে আপনি বেছে নেওয়া বিল্ট-ইন বা কাস্টম ইভ্যালুয়েটরের মাধ্যমে পরিমাপিত হয়। prompt flow sdk দিয়ে আপনার সিস্টেমটি মূল্যায়নের জন্য শুরু করতে, আপনি [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি মূল্যায়ন চালালে, আপনি [Azure AI Studio-তে ফলাফল ভিজ্যুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য, বা পরিষেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার অবশ্যই [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।
এই প্রকল্পের সংশোধিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগোর ব্যবহার বিভ্রান্তি সৃষ্টি করা বা Microsoft স্পন্সরশিপ নির্দেশ করা যাবে না।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর যেকোনো ব্যবহার ঐ পক্ষের নীতিমালা অনুসারে হবেই।

## সহায়তা পান

যদি আপনি আটকে যান বা AI অ্যাপ গড়ার বিষয়ে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

আপনার যদি পণ্য সংক্রান্ত মতামত বা ত্রুটি থাকে, তাহলে যান:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে জেনে রাখুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই authoritative উৎস হিসেবে বিবেচিত হওয়া উচিত। জরুরি তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে কোনো ভুল ধারণা বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->