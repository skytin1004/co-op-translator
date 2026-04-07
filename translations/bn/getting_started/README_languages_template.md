# 🌐 বহু-ভাষা সমর্থন (টেমপ্লেট)

রক্ষণাবেক্ষক: নিচের ব্লকটি একটি "সমস্ত ভাষা" উদাহরণ যা Co-op Translator দ্বারা পরিচালিত।

- আপনি যদি চান Co-op Translator এই তালিকাটি সম্পূর্ণ স্বয়ংক্রিয়ভাবে আপ-টু-ডেট রাখতে `translate` চালানোর সময় (যেকোনো ভাষা নির্বাচন), তাহলে দুইটি মন্তব্য চিহ্ন অপরিবর্তিত রাখুন।
- আপনি যদি শুধুমাত্র একটি ভাষার উপসেট দেখাতে চান, তাহলে দুইটি মন্তব্য চিহ্ন মুছে ফেলুন এবং যেসকল ভাষা তালিকাভুক্ত করতে চান না সেগুলো মুছে দিন। মন্তব্য চিহ্নগুলো মুছে ফেলার পর Co-op Translator আর এই অংশটি স্বয়ংক্রিয়ভাবে প্রতিস্থাপন করবে না।

- এখন এই অংশে একটি "স্থানীয়ভাবে ক্লোন করতে আগ্রহী?" পরামর্শ অন্তর্ভুক্ত আছে, যা ব্যবহারকারীদের বড় অনুবাদের পে-লোড ছাড়া ক্লোন করতে সাহায্য করবে। আপনি আপনার রিপোজিটোরির URL দিয়ে পরামর্শটি ব্যক্তিগতকৃত করতে পারেন, উদাহরণস্বরূপ চালিয়ে:
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](./README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকারোক্তি**:  
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা সঠিকতার জন্য চেষ্টা করি, অনুগ্রহ করে মনোযোগ দিন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসত্যতা থাকতে পারে। মূল ভাষায় থাকা ডকুমেন্টটিই প্রামাণিক উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানুষের অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল ধারণা বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->