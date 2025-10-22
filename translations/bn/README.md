<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:37:23+00:00",
  "source_file": "README.md",
  "language_code": "bn"
}
-->
# কো-অপ ট্রান্সলেটর

_সহজেই আপনার শিক্ষামূলক GitHub কনটেন্টকে একাধিক ভাষায় অনুবাদ করুন, যাতে বিশ্বজুড়ে পাঠকদের কাছে পৌঁছাতে পারেন।_

### 🌐 একাধিক ভাষার সমর্থন

#### [কো-অপ ট্রান্সলেটর](https://github.com/Azure/Co-op-Translator) দ্বারা সমর্থিত

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[আরবি](../ar/README.md) | [বাংলা](./README.md) | [বুলগেরিয়ান](../bg/README.md) | [বর্মী (মিয়ানমার)](../my/README.md) | [চাইনিজ (সরলীকৃত)](../zh/README.md) | [চাইনিজ (প্রথাগত, হংকং)](../hk/README.md) | [চাইনিজ (প্রথাগত, ম্যাকাও)](../mo/README.md) | [চাইনিজ (প্রথাগত, তাইওয়ান)](../tw/README.md) | [ক্রোয়েশিয়ান](../hr/README.md) | [চেক](../cs/README.md) | [ড্যানিশ](../da/README.md) | [ডাচ](../nl/README.md) | [এস্তোনিয়ান](../et/README.md) | [ফিনিশ](../fi/README.md) | [ফরাসি](../fr/README.md) | [জার্মান](../de/README.md) | [গ্রিক](../el/README.md) | [হিব্রু](../he/README.md) | [হিন্দি](../hi/README.md) | [হাঙ্গেরিয়ান](../hu/README.md) | [ইন্দোনেশিয়ান](../id/README.md) | [ইতালিয়ান](../it/README.md) | [জাপানি](../ja/README.md) | [কোরিয়ান](../ko/README.md) | [লিথুয়ানিয়ান](../lt/README.md) | [মালয়](../ms/README.md) | [মারাঠি](../mr/README.md) | [নেপালি](../ne/README.md) | [নাইজেরিয়ান পিজিন](../pcm/README.md) | [নরওয়েজিয়ান](../no/README.md) | [পার্সিয়ান (ফার্সি)](../fa/README.md) | [পোলিশ](../pl/README.md) | [পর্তুগিজ (ব্রাজিল)](../br/README.md) | [পর্তুগিজ (পর্তুগাল)](../pt/README.md) | [পাঞ্জাবি (গুরুমুখি)](../pa/README.md) | [রোমানিয়ান](../ro/README.md) | [রাশিয়ান](../ru/README.md) | [সার্বিয়ান (সিরিলিক)](../sr/README.md) | [স্লোভাক](../sk/README.md) | [স্লোভেনিয়ান](../sl/README.md) | [স্প্যানিশ](../es/README.md) | [সোয়াহিলি](../sw/README.md) | [সুইডিশ](../sv/README.md) | [তাগালোগ (ফিলিপিনো)](../tl/README.md) | [তামিল](../ta/README.md) | [থাই](../th/README.md) | [তুর্কি](../tr/README.md) | [ইউক্রেনিয়ান](../uk/README.md) | [উর্দু](../ur/README.md) | [ভিয়েতনামিজ](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## সংক্ষিপ্ত বিবরণ

**কো-অপ ট্রান্সলেটর** আপনাকে দ্রুত আপনার শিক্ষামূলক GitHub কনটেন্টকে একাধিক ভাষায় অনুবাদ করতে সাহায্য করে, যাতে সহজেই বিশ্বজুড়ে পাঠকদের কাছে পৌঁছাতে পারেন। আপনি যখন আপনার Markdown ফাইল, ছবি, বা Jupyter নোটবুক আপডেট করেন, অনুবাদগুলো স্বয়ংক্রিয়ভাবে সিঙ্ক হয়, যাতে আপনার শিক্ষামূলক GitHub কনটেন্ট আন্তর্জাতিক ব্যবহারকারীদের জন্য সর্বদা নতুন ও প্রাসঙ্গিক থাকে।

কো-অপ ট্রান্সলেটর কীভাবে অনুবাদিত শিক্ষামূলক GitHub কনটেন্ট সংগঠিত করে দেখুন:

![উদাহরণ](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.bn.png)

## দ্রুত শুরু

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

ডকার:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## ন্যূনতম সেটআপ

- একটি `.env` তৈরি করুন এই টেমপ্লেট ব্যবহার করে: [.env.template](../../.env.template)
- একটি LLM প্রদানকারী কনফিগার করুন (Azure OpenAI বা OpenAI)
- ছবি অনুবাদের জন্য (`-img`), Azure AI Vision-ও সেট করুন
- সুপারিশ: যদি অন্য টুল দিয়ে অনুবাদ করা ফাইল থাকে, আগে সেগুলো পরিষ্কার করুন যাতে দ্বন্দ্ব না হয় (যেমন: `translations/`)
- সুপারিশ: আপনার README-তে একটি অনুবাদ বিভাগ যোগ করুন [README ভাষা টেমপ্লেট](./README_languages_template.md) ব্যবহার করে
- দেখুন: [Azure AI সেটআপ করুন](./getting_started/set-up-azure-ai.md)

## ব্যবহার

সব ধরনের সমর্থিত ফাইল অনুবাদ করুন:

```bash
translate -l "ko ja"
```

শুধু Markdown:

```bash
translate -l "de" -md
```

Markdown + ছবি:

```bash
translate -l "pt" -md -img
```

শুধু নোটবুক:

```bash
translate -l "zh" -nb
```

আরও ফ্ল্যাগ: [কমান্ড রেফারেন্স](./getting_started/command-reference.md)

## বৈশিষ্ট্য

- Markdown, নোটবুক, এবং ছবির জন্য স্বয়ংক্রিয় অনুবাদ
- সোর্স পরিবর্তনের সাথে অনুবাদ সিঙ্ক রাখে
- লোকাল (CLI) বা CI (GitHub Actions)-এ কাজ করে
- Azure OpenAI বা OpenAI ব্যবহার করে; ছবির জন্য ঐচ্ছিক Azure AI Vision
- Markdown ফরম্যাটিং ও গঠন ঠিক রাখে

## ডকুমেন্টেশন

- [কমান্ড-লাইন গাইড](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions গাইড (পাবলিক রিপোজিটরি ও স্ট্যান্ডার্ড সিক্রেট)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions গাইড (Microsoft অর্গানাইজেশন রিপোজিটরি ও অর্গ-লেভেল সেটআপ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [সমর্থিত ভাষাসমূহ](./getting_started/supported-languages.md)
- [সমস্যা সমাধান](./getting_started/troubleshooting.md)

## আমাদের সমর্থন করুন এবং বিশ্বব্যাপী শিক্ষার প্রসার ঘটান

বিশ্বজুড়ে শিক্ষামূলক কনটেন্ট ভাগাভাগি করার পদ্ধতিতে পরিবর্তন আনতে আমাদের সঙ্গে যোগ দিন! [কো-অপ ট্রান্সলেটর](https://github.com/azure/co-op-translator)-কে GitHub-এ ⭐ দিন এবং শেখা ও প্রযুক্তিতে ভাষার বাধা দূর করার আমাদের মিশনকে সমর্থন করুন। আপনার আগ্রহ ও অবদান গুরুত্বপূর্ণ! কোড অবদান ও ফিচার সাজেশন সবসময় স্বাগত।

### আপনার ভাষায় Microsoft-এর শিক্ষামূলক কনটেন্ট দেখুন

- [AZD ফর বিগিনারস](https://github.com/microsoft/AZD-for-beginners)
- [এজ AI ফর বিগিনারস](https://github.com/microsoft/edgeai-for-beginners)
- [মডেল কনটেক্সট প্রোটোকল (MCP) ফর বিগিনারস](https://github.com/microsoft/mcp-for-beginners)
- [AI এজেন্টস ফর বিগিনারস](https://github.com/microsoft/ai-agents-for-beginners)
- [.NET ব্যবহার করে জেনারেটিভ AI ফর বিগিনারস](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [জেনারেটিভ AI ফর বিগিনারস](https://github.com/microsoft/generative-ai-for-beginners)
- [জেনারেটিভ AI ফর বিগিনারস (জাভা)](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML ফর বিগিনারস](https://aka.ms/ml-beginners)
- [ডেটা সায়েন্স ফর বিগিনারস](https://aka.ms/datascience-beginners)
- [AI ফর বিগিনারস](https://aka.ms/ai-beginners)
- [সাইবারসিকিউরিটি ফর বিগিনারস](https://github.com/microsoft/Security-101)
- [ওয়েব ডেভ ফর বিগিনারস](https://aka.ms/webdev-beginners)
- [IoT ফর বিগিনারস](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## ভিডিও উপস্থাপনা

কো-অপ ট্রান্সলেটর সম্পর্কে আরও জানতে আমাদের উপস্থাপনা দেখুন _(নিচের ছবিতে ক্লিক করুন YouTube-এ দেখতে)_:

- **Open at Microsoft**: ১৮ মিনিটের সংক্ষিপ্ত পরিচিতি ও দ্রুত গাইড, কীভাবে কো-অপ ট্রান্সলেটর ব্যবহার করবেন।

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.bn.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## অবদান রাখুন

এই প্রকল্পে অবদান ও সাজেশন স্বাগত। Azure Co-op Translator-এ অবদান রাখতে আগ্রহী? [CONTRIBUTING.md](./CONTRIBUTING.md) দেখুন, কীভাবে কো-অপ ট্রান্সলেটরকে আরও সহজলভ্য করতে সাহায্য করতে পারেন।

## অবদানকারীরা

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## আচরণবিধি

এই প্রকল্পে [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) গ্রহণ করা হয়েছে।
আরও তথ্যের জন্য [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) দেখুন অথবা
[opencode@microsoft.com](mailto:opencode@microsoft.com)-এ অতিরিক্ত প্রশ্ন বা মন্তব্য পাঠান।

## দায়িত্বশীল AI

Microsoft আমাদের AI পণ্যগুলো দায়িত্বশীলভাবে ব্যবহার করতে গ্রাহকদের সহায়তা করতে, আমাদের শেখা শেয়ার করতে, এবং বিশ্বাসভিত্তিক অংশীদারিত্ব গড়ে তুলতে প্রতিশ্রুতিবদ্ধ। Transparency Notes ও Impact Assessments-এর মতো টুলের মাধ্যমে আমরা এই কাজ করি। এসব রিসোর্সের অনেক কিছুই পাওয়া যাবে [https://aka.ms/RAI](https://aka.ms/RAI)।
Microsoft-এর দায়িত্বশীল AI-এর পদ্ধতি আমাদের AI নীতিমালার উপর ভিত্তি করে: ন্যায্যতা, নির্ভরযোগ্যতা ও নিরাপত্তা, গোপনীয়তা ও সুরক্ষা, অন্তর্ভুক্তি, স্বচ্ছতা, এবং জবাবদিহিতা।

বড় আকারের ভাষা, ছবি, ও বক্তৃতা মডেল—যেমন এই স্যাম্পলে ব্যবহৃত—অন্যায্য, অবিশ্বস্ত, বা আপত্তিকর আচরণ করতে পারে, যা ক্ষতির কারণ হতে পারে। অনুগ্রহ করে [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) পড়ে ঝুঁকি ও সীমাবদ্ধতা সম্পর্কে জানুন।

এই ঝুঁকি কমানোর জন্য সুপারিশকৃত পদ্ধতি হলো আপনার আর্কিটেকচারে একটি নিরাপত্তা ব্যবস্থা অন্তর্ভুক্ত করা, যা ক্ষতিকর আচরণ শনাক্ত ও প্রতিরোধ করতে পারে। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) একটি স্বাধীন সুরক্ষা স্তর দেয়, যা অ্যাপ ও সার্ভিসে ক্ষতিকর ব্যবহারকারী-জেনারেটেড ও AI-জেনারেটেড কনটেন্ট শনাক্ত করতে পারে। Azure AI Content Safety-তে টেক্সট ও ছবি API আছে, যা ক্ষতিকর উপাদান শনাক্ত করতে সাহায্য করে। আমাদের ইন্টারেক্টিভ Content Safety Studio-ও আছে, যেখানে বিভিন্ন ধরনের ক্ষতিকর কনটেন্ট শনাক্ত করার নমুনা কোড দেখতে, পরীক্ষা করতে পারেন। [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) আপনাকে সার্ভিসে অনুরোধ পাঠানোর ধাপ দেখায়।
আরেকটি গুরুত্বপূর্ণ বিষয় হলো সামগ্রিক অ্যাপ্লিকেশনের পারফরম্যান্স। মাল্টি-মোডাল এবং মাল্টি-মডেল অ্যাপ্লিকেশনের ক্ষেত্রে, পারফরম্যান্স বলতে বোঝায় যে সিস্টেমটি আপনি এবং আপনার ব্যবহারকারীদের প্রত্যাশা অনুযায়ী কাজ করছে কিনা, যার মধ্যে ক্ষতিকর আউটপুট তৈরি না করাও অন্তর্ভুক্ত। আপনার সামগ্রিক অ্যাপ্লিকেশনের পারফরম্যান্স মূল্যায়ন করা জরুরি, যা করতে পারেন [generation quality এবং risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ব্যবহার করে।

আপনি আপনার ডেভেলপমেন্ট এনভায়রনমেন্টে [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ব্যবহার করে আপনার AI অ্যাপ্লিকেশন মূল্যায়ন করতে পারেন। টেস্ট ডেটাসেট বা নির্দিষ্ট টার্গেটের ভিত্তিতে, আপনার জেনারেটিভ AI অ্যাপ্লিকেশনের আউটপুটগুলো বিল্ট-ইন ইভ্যালুয়েটর বা আপনার পছন্দের কাস্টম ইভ্যালুয়েটর দিয়ে পরিমাপ করা হয়। সিস্টেম মূল্যায়নের জন্য prompt flow sdk দিয়ে শুরু করতে চাইলে, আপনি [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) অনুসরণ করতে পারেন। একবার আপনি ইভ্যালুয়েশন রান সম্পন্ন করলে, আপনি [Azure AI Studio-তে ফলাফল ভিজুয়ালাইজ করতে পারেন](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ট্রেডমার্ক

এই প্রকল্পে বিভিন্ন প্রকল্প, পণ্য, বা পরিষেবার ট্রেডমার্ক বা লোগো থাকতে পারে। Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহারের অনুমোদিত নিয়মাবলী [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) অনুসরণ করতে হবে।
এই প্রকল্পের পরিবর্তিত সংস্করণে Microsoft-এর ট্রেডমার্ক বা লোগো ব্যবহার করলে যেন বিভ্রান্তি না হয় বা Microsoft-এর স্পনসরশিপ বোঝায় না, তা নিশ্চিত করতে হবে।
তৃতীয় পক্ষের ট্রেডমার্ক বা লোগো ব্যবহারের ক্ষেত্রে সংশ্লিষ্ট তৃতীয় পক্ষের নীতিমালা প্রযোজ্য।

## সহায়তা পাওয়া

যদি আপনি কোনো সমস্যায় পড়েন বা AI অ্যাপ তৈরি নিয়ে কোনো প্রশ্ন থাকে, তাহলে যোগ দিন:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

যদি আপনার কোনো প্রোডাক্ট ফিডব্যাক থাকে বা অ্যাপ তৈরি করতে গিয়ে কোনো ত্রুটি পান, তাহলে দেখুন:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**অস্বীকৃতি**:
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতা বজায় রাখার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসঙ্গতি থাকতে পারে। মূল ভাষায় লেখা নথিটিই চূড়ান্ত ও কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হবে। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।