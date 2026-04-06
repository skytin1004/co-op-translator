# "অন্যান্য কোর্স" বিভাগ আপডেট করুন (Microsoft Beginners রিপোজ)

এই নির্দেশিকাটি ব্যাখ্যা করে কীভাবে Co-op Translator ব্যবহার করে "অন্যান্য কোর্স" বিভাগটি স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ করতে হয়, এবং কীভাবে সমস্ত রিপোজের জন্য গ্লোবাল টেমপ্লেট আপডেট করতে হয়।

- প্রযোজ্য: শুধুমাত্র Microsoft Beginners রিপোজিটোরিগুলোর জন্য
- কাজ করে: Co-op Translator CLI এবং GitHub Actions-এর সাথে
- টেমপ্লেট উৎস: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## দ্রুত শুরু: আপনার রিপোতে অটো-সিঙ্ক চালু করুন

আপনার README-র "অন্যান্য কোর্স" বিভাগের চারপাশে নিচের মার্কারগুলি যোগ করুন। Co-op Translator প্রতিবার এই মার্কারগুলির মধ্যে সবকিছু প্রতিস্থাপন করবে।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator যখনই চলে—CLI (যেমন, `translate -l "<language codes>"`) বা GitHub Actions-এর মাধ্যমে—এটি স্বয়ংক্রিয়ভাবে এই মার্কার দ্বারা মোড়ানো "অন্যান্য কোর্স" বিভাগ আপডেট করবে।

> [!NOTE]
> আপনার যদি ইতিমধ্যে একটি তালিকা থাকে, তাহলে শুধু এটি একই মার্কার দিয়ে মোড়ান। পরবর্তী রান এটিকে সর্বশেষ মানসম্পন্ন বিষয়বস্তুর মাধ্যমে প্রতিস্থাপন করবে।

---

## গ্লোবাল কন্টেন্ট কীভাবে পরিবর্তন করবেন

আপনি যদি সমস্ত Beginners রিপোজে প্রদর্শিত মানসম্পন্ন বিষয়বস্তু আপডেট করতে চান:

1. টেমপ্লেটটি সম্পাদনা করুন: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. আপনার পরিবর্তনগুলি সহ Co-op Translator রিপোতে একটি pull request খুলুন
3. PR মিশ্রিত হওয়ার পরে, Co-op Translator সংস্করণ আপডেট হবে
4. পরবর্তীবার যখন Co-op Translator (CLI বা GitHub Action) একটি টার্গেট রিপোতে চালানো হবে, এটি সংশোধিত বিভাগটি স্বয়ংক্রিয়ভাবে সিঙ্ক করবে

এটি সমস্ত Beginners রিপোজিটোরিগুলোর "অন্যান্য কোর্স" বিষয়বস্তুর জন্য একটি একক সত্যিকার উৎস নিশ্চিত করে।


## রিপো আকারসমূহ

অনুবাদকৃত ভাষার সংখ্যার কারণে রিপোগুলো বড় হয়ে যেতে পারে যাতে শেষ ব্যবহারকারীদের নির্দেশনা দেওয়া যায় কিভাবে clone - sparse ব্যবহার করে শুধুমাত্র প্রয়োজনীয় ভাষাগুলো ক্লোন করতে হবে, সম্পূর্ণ রিপো নয়।

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই নথিটি AI অনূদিত সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা সঠিকতার জন্য চেষ্টা করি, দয়া করে মনে রাখুন যে স্বয়ংক্রিয় অনুবাদে ভুল বা অসম্পূর্ণতা থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানুষের অনুবাদ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নয়।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->