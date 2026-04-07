# Co-op Translator

_সহজেই আপনার শিক্ষামূলক GitHub সামগ্রী প্রকল্পের বহুভাষিকতার সাথে সাথে স্বয়ংক্রিয়করণ এবং রক্ষণাবেক্ষণ করুন।_

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

### 🌐 বহুভাষিক সমর্থন

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) দ্বারা সমর্থিত

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **অনলাইনে ক্লোন করতে চান?**
>
> এই রেপোজিটরিতে ৫০+ ভাষার অনুবাদ অন্তর্ভুক্ত রয়েছে যা ডাউনলোডের আকার উল্লেখযোগ্যভাবে বৃদ্ধি করে। অনুবাদ ছাড়া ক্লোন করতে sparse checkout ব্যবহার করুন:
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
> এটি আপনাকে দ্রুত ডাউনলোডের মাধ্যমে কোর্স সম্পন্ন করার জন্য প্রয়োজনীয় সবকিছু দেয়।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ওভারভিউ

**Co-op Translator** আপনার শিক্ষামূলক GitHub সামগ্রী বহুভাষায় অনায়াসে স্থানীয়করণ করতে সহায়তা করে।  
যখন আপনি আপনার Markdown ফাইল, ছবি, বা নোটবুকগুলো আপডেট করেন, তখন অনুবাদগুলো স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ থাকে, যা নিশ্চিত করে যে বিশ্বব্যাপী শিক্ষার্থীদের জন্য আপনার সামগ্রী সঠিক এবং সর্বদা আপডেটেড থাকবে।

অনুবাদিত বিষয়বস্তু কিভাবে সংগঠিত হয় তার উদাহরণ:

![Example](../../imgs/translation-ex.png)

## কিভাবে অনুবাদের অবস্থা পরিচালিত হয়

Co-op Translator অনুবাদিত বিষয়বস্তু **সংস্করণযুক্ত সফটওয়্যার আর্টিফ্যাক্ট** হিসেবে পরিচালনা করে,  
স্থির ফাইল হিসেবে নয়।

যন্ত্রটি অনুবাদিত Markdown, ছবি এবং নোটবুকের অবস্থা ট্র্যাক করে  
**ভাষাভিত্তিক মেটাডেটা ব্যবহার করে**।

এই ডিজাইন Co-op Translator কে অনুমতি দেয়:

- পুরানো অনুবাদ নির্ভরযোগ্যভাবে চিহ্নিত করতে  
- Markdown, ছবি এবং নোটবুককে সঙ্গতিপূর্ণভাবে পরিচালনা করতে  
- বড়, দ্রুত গতির, বহুভাষিক রেপোজিটরিতে নিরাপদভাবে স্কেল করতে

অনুবাদগুলোকে পরিচালিত আর্টিফ্যাক্ট হিসেবে মডেলিং করে,  
অনুবাদ কর্মপ্রবাহ আধুনিক সফটওয়্যার নির্ভরতা ও আর্টিফ্যাক্ট ব্যবস্থাপনার সাথে প্রাকৃতিকভাবে সামঞ্জস্যপূর্ণ হয়।

→ [কিভাবে অনুবাদের অবস্থা পরিচালিত হয়](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## দ্রুত শুরু

```bash
# একটি ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন এবং সক্রিয় করুন (সফারিশকৃত)
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

Docker:

```bash
# GHCR থেকে পাবলিক ইমেজটি টেনে আনুন
docker pull ghcr.io/azure/co-op-translator:latest
# বর্তমান ফোল্ডার মাউন্ট করে এবং .env সরবরাহ করে চালান (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## নূন্যতম সেটআপ

1. নিশ্চিত করুন যে আপনার কাছে সমর্থিত Python সংস্করণ আছে (বর্তমানে ৩.১০-৩.১২)। poetry (pyproject.toml) এ এটি স্বয়ংক্রিয়ভাবে পরিচালিত হয়।  
2. টেমপ্লেট ব্যবহার করে একটি `.env` ফাইল তৈরি করুন: [.env.template](../../.env.template)  
3. একটি LLM প্রদানকারী কনফিগার করুন (Azure OpenAI বা OpenAI)  
4. (ঐচ্ছিক) ছবি অনুবাদের জন্য (`-img`), Azure AI Vision কনফিগার করুন  
5. (ঐচ্ছিক) আপনি বহুসংখ্যক ক্রেডেনশিয়াল সেট কনফিগার করতে পারেন `_1`, `_2` ইত্যাদি সাফিক্স দিয়ে ভেরিয়েবলগুলো ডুপ্লিকেট করে। একটি সেটের সমস্ত ভেরিয়েবল একই সাফিক্স থাকতে হবে।  
6. (প্রস্তাবিত) পূর্ববর্তী অনুবাদসমূহ ক্লিন করুন যাতে দ্বন্দ্ব না হয় (যেমন `translations/`)  
7. (প্রস্তাবিত) আপনার README তে অনুবাদ বিভাগ যোগ করুন [README languages template](./getting_started/README_languages_template.md) ব্যবহার করে  
8. দেখুন: [Azure AI সেট আপ করুন](./getting_started/set-up-azure-ai.md)

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

অধিক পতাকা: [Command reference](./getting_started/command-reference.md)

## বৈশিষ্ট্যসমূহ

- Markdown, নোটবুক, এবং ছবির জন্য স্বয়ংক্রিয় অনুবাদ  
- উৎস পরিবর্তনের সাথে অনুবাদ সামঞ্জস্য বজায় রাখে  
- লোকালি (CLI) বা CI (GitHub Actions) এ কাজ করে  
- Azure OpenAI অথবা OpenAI ব্যবহার করে; ছবির জন্য ঐচ্ছিক Azure AI Vision  
- Markdown বিন্যাস এবং কাঠামো সংরক্ষণ করে

## ডকুমেন্টেশন

- [কমান্ড-লাইন গাইড](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions গাইড (পাবলিক রেপোজিটরি ও স্ট্যান্ডার্ড সিক্রেট)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions গাইড (Microsoft অর্গানাইজেশন রেপোজিটরি ও অর্গ-লেভেল সেটআপ)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README ভাষার টেমপ্লেট](./getting_started/README_languages_template.md)  
- [সমর্থিত ভাষাসমূহ](./getting_started/supported-languages.md)  
- [অবদান](./CONTRIBUTING.md)  
- [সমস্যা সমাধান](./getting_started/troubleshooting.md)

### Microsoft-নির্দিষ্ট গাইড
> [!NOTE]
> শুধুমাত্র Microsoft “For Beginners” রেপোজিটরির রক্ষণাবেক্ষকদের জন্য।

- [“অন্যান্য কোর্স” তালিকা আপডেট করা (শুধুমাত্র MS Beginners রেপোজিটরির জন্য)](./getting_started/update-other-courses.md)

## আমাদের সমর্থন করুন এবং বিশ্বব্যাপী শেখাকে উষ্ণ করুন

বিশ্বব্যাপী শিক্ষামূলক সামগ্রী শেয়ার করার বিপ্লবের অংশ হোন! GitHub এ [Co-op Translator](https://github.com/azure/co-op-translator) কে ⭐ দিন এবং শেখা ও প্রযুক্তিতে ভাষাগত বাধা ভেদ করার আমাদের মিশনকে সমর্থন করুন। আপনার আগ্রহ ও অবদান গুরুত্বপূর্ণ প্রভাব ফেলে! কোড অবদান এবং বৈশিষ্ট্য প্রস্তাব সবসময় স্বাগত।

### আপনার ভাষায় Microsoft শিক্ষামূলক সামগ্রী অন্বেষণ করুন

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

## ভিডিও উপস্থাপন

👉 YouTube এ দেখার জন্য নিচের ছবিতে ক্লিক করুন।

- **Microsoft এ ওপেন**: Co-op Translator ব্যবহার করার একটি সংক্ষিপ্ত ১৮ মিনিটের প্রস্তাবনা ও দ্রুত গাইড।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## অবদান

এই প্রকল্প অবদান এবং প্রস্তাব বহন করে। Azure Co-op Translator এ অবদান রাখতে আগ্রহী? অনুগ্রহ করে আমাদের [CONTRIBUTING.md](./CONTRIBUTING.md) দেখুন যা নির্দেশনা প্রদান করে কিভাবে আপনি Co-op Translator কে আরও প্রবেশযোগ্য করতে সাহায্য করতে পারেন।

## অবদানকারীরা
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## আচরণ বিধি

এই প্রকল্পটি গ্রহণ করেছে [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)।
অতিরিক্ত তথ্যের জন্য দেখুন [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) অথবা
যেকোনো প্রশ্ন বা মন্তব্যের জন্য যোগাযোগ করুন [opencode@microsoft.com](mailto:opencode@microsoft.com) ঠিকানায়।

## দায়িত্বশীল AI

Microsoft আমাদের গ্রাহকদের আমাদের AI পণ্যগুলি দায়িত্বশীলভাবে ব্যবহার করতে সাহায্য করার, আমাদের শেখাগুলো শেয়ার করার, এবং Transparency Notes ও Impact Assessments এর মতো সরঞ্জামের মাধ্যমে বিশ্বাসভিত্তিক অংশীদারিত্ব নির্মাণে প্রতিশ্রুতিবদ্ধ। এই সংস্থানগুলোর অনেকগুলি পাওয়া যেতে পারে [https://aka.ms/RAI](https://aka.ms/RAI)।
Microsoft এর দায়িত্বশীল AI এপ্রোচ আমাদের AI নীতিমালা অনুযায়ী যেমন ন্যায্যতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা এবং জবাবদিহিতার উপর ভিত্তি করে গড়ে উঠেছে।

বৃহৎ পরিসরের প্রাকৃতিক ভাষা, ছবি, এবং ভাষণ মডেল - যেমন এই নমুনায় ব্যবহৃত - সম্ভাব্যভাবে এমন আচরণ করতে পারে যা ন্যায্য নয়, নির্ভরযোগ্য নয়, বা আক্রমণাত্মক, এবং এর ফলে ক্ষতি হতে পারে। অনুগ্রহ করে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) দেখুন যাতে ঝুঁকি এবং সীমাবদ্ধতাগুলি সম্পর্কে অবহিত হওয়া যায়।

এই ঝুঁকিগুলো কমানোর জন্য সুপারিশ করা পদ্ধতি হল আপনার আর্কিটেকচারে একটি নিরাপত্তা ব্যবস্থা অন্তর্ভুক্ত করা যা ক্ষতিকর আচরণ সনাক্ত ও প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর প্রদান করে, যা অ্যাপ্লিকেশন ও সেবাগুলিতে ব্যবহারকারী-তৈরি ও AI-তৈরি ক্ষতিকর বিষয়বস্তু সনাক্ত করতে সক্ষম। Azure AI Content Safety টেক্সট এবং চিত্র API অন্তর্ভুক্ত করে যা আপনাকে ক্ষতিকর উপাদান সনাক্ত করতে দেয়। আমাদের একটি ইন্টারেক্টিভ Content Safety Studio ও আছে যা আপনাকে বিভিন্ন মোডালিটির মধ্যে ক্ষতিকর বিষয়বস্তু সনাক্ত করার নমুনা কোড দেখার, অন্বেষণ করার এবং চেষ্টা করার সুযোগ দেয়। নিম্নলিখিত [দ্রুত শুরু ডকুমেন্টেশন](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সেবাটিতে অনুরোধ পাঠানোর প্রক্রিয়ায় সহায়তা করে।

আরেকটি বিষয় যা বিবেচনা করা দরকার তা হলো সামগ্রিক অ্যাপ্লিকেশন পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনগুলোর ক্ষেত্রে, পারফরম্যান্স বলতে বুঝায় যে সিস্টেমটি আপনি ও আপনার ব্যবহারকারীরা প্রত্যাশা করা অনুযায়ী কাজ করে, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাটাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনটির পারফরম্যান্স মূল্যায়ন করা গুরুত্বপূর্ণ, যা [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে করা যেতে পারে।

আপনি আপনার AI অ্যাপ্লিকেশনটি আপনার উন্নয়ন পরিবেশে [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে মূল্যায়ন করতে পারেন। একটি পরীক্ষার ডেটাসেট বা লক্ষ্য দেওয়ার মাধ্যমে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের উৎপাদনগুলি সংখ্যাগতভাবে অন্তর্নির্মিত মূল্যায়ক অথবা আপনার পছন্দের কাস্টম মূল্যায়ক দ্বারা মাপা হয়। prompt flow sdk ব্যবহার করে আপনার সিস্টেম মূল্যায়ন শুরু করতে [দ্রুত শুরু গাইড](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। মূল্যায়ন চালানোর পর, আপনি [Azure AI Studio তে ফলাফল ভিজ্যুয়ালাইজ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) করতে পারেন।

## ট্রেডমার্ক

এই প্রকল্পে প্রকল্প, পণ্য বা সেবার জন্য ট্রেডমার্ক বা লোগোগুলি থাকতে পারে। Microsoft ট্রেডমার্ক বা লোগোর অনুমোদিত ব্যবহার [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে এবং তার নিয়মাবলী অনুসারে হতে হবে।
এই প্রকল্পের সংশোধিত সংস্করণে Microsoft ট্রেডমার্ক বা লোগো ব্যবহারে বিভ্রান্তি করা বা Microsoft স্পনসরশিপ বোঝানো যাবে না।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগোর যেকোনো ব্যবহার সেই পক্ষের নীতিমালা অনুযায়ী হতে হবে।

## সাহায্য নেওয়া

যদি আটকে যান বা AI অ্যাপ তৈরি সম্পর্কে কোনো প্রশ্ন থাকে, যোগ দিন:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

যদি পণ্য প্রতিক্রিয়া বা ত্রুটি থাকে, বিকাশের সময় পরিদর্শন করুন:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) এর মাধ্যমে অনূদিত হয়েছে। যদিও আমরা সঠিকতার জন্য চেষ্টা করি, অনুগ্রহ করে জানুুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষের অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->