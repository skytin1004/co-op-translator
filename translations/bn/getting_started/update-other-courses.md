# "অন্যান্য কোর্স" বিভাগ আপডেট করুন (Microsoft Beginners রিপোজিটোরি)

এই গাইডটি ব্যাখ্যা করে কিভাবে Co‑op Translator ব্যবহার করে "অন্যান্য কোর্স" বিভাগটি স্বয়ংক্রিয়ভাবে সিঙ্ক্রোনাইজ করা যায়, এবং কিভাবে সব রিপোজিটোরির জন্য গ্লোবাল টেম্পলেট আপডেট করতে হয়।

- প্রযোজ্য: শুধুমাত্র Microsoft Beginners রিপোজিটোরিগুলিতে
- কাজ করে: Co‑op Translator CLI এবং GitHub Actions এর সাথে
- টেম্পলেট উৎস: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## দ্রুত শুরু: আপনার রিপোতে অটো-সিঙ্ক সক্ষম করুন

আপনার README এর "অন্যান্য কোর্স" বিভাগের চারপাশে নিম্নলিখিত মার্কারগুলি যোগ করুন। Co‑op Translator প্রতি রান পর এই মার্কারের মধ্যে থাকা সবকিছু প্রতিস্থাপন করবে।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

প্রতি বার Co‑op Translator চালানো হয়—CLI (যেমন, `translate -l "<language codes>"`) অথবা GitHub Actions এর মাধ্যমে—এটি স্বয়ংক্রিয়ভাবে এই মার্কার দ্বারা আবৃত "অন্যান্য কোর্স" বিভাগ আপডেট করে।

> [!NOTE]
> যদি আপনার একটি বিদ্যমান তালিকা থাকে, শুধু একই মার্কার দিয়ে এটি আবৃত করুন। পরবর্তী রান এটি সর্বশেষ মানকৃত বিষয়বস্তু দিয়ে প্রতিস্থাপন করবে।

---

## গ্লোবাল বিষয়বস্তু কিভাবে পরিবর্তন করবেন

যদি আপনি সব Beginners রিপোজিটোরিতে প্রদর্শিত মানকৃত বিষয়বস্তু আপডেট করতে চান:

1. টেম্পলেটটি সম্পাদনা করুন: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. আপনার পরিবর্তন সহ Co-op Translator রিপোজিটোরিতে একটি pull request খুলুন
3. PR মার্জ হওয়ার পর Co‑op Translator এর সংস্করণ আপডেট হবে
4. পরবর্তীবার Co‑op Translator (CLI বা GitHub Action) একটি লক্ষ্য রিপোতে চালালে, এটি স্বয়ংক্রিয়ভাবে আপডেট হওয়া বিভাগ সিঙ্ক করবে

এটি নিশ্চিত করে যে "অন্যান্য কোর্স" বিষয়বস্তু সব Beginners রিপোজিটোরিতে একটি একক সত্যের উৎস হিসেবে থাকবে।

## রিপো সাইজ

অনুবাদের ধরণের ভাষার সংখ্যার কারণে রিপোগুলো বড় হতে পারে, যা শেষ ব্যবহারকারীদের নির্দেশনার জন্য সাহায্য করতে পারে কিভাবে clone - sparse ব্যবহার করে শুধুমাত্র প্রয়োজনীয় ভাষাগুলো ক্লোন করতে হয় এবং পুরো রিপো নয়

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
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। যদিও আমরা নির্ভুলতার চেষ্টা করি, অনুগ্রহ করে বুঝতে হবে যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অস্পষ্টতা থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায় কর্তৃত্বপূর্ণ উৎস হিসাবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানবিক অনুবাদ প্রয়োজন। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->