# "دیگر کورسز" سیکشن کو اپ ڈیٹ کریں (Microsoft Beginners repositories)

یہ گائیڈ بتاتی ہے کہ "دیگر کورسز" سیکشن کو Co-op Translator کے ذریعے خودکار مطابقت پذیری کیسے بنائیں، اور تمام repositories کے لیے عالمی ٹیمپلیٹ کو کیسے اپ ڈیٹ کریں۔

- قابل اطلاق: صرف Microsoft Beginners repositories
- کام کرتا ہے: Co-op Translator CLI اور GitHub Actions کے ساتھ
- ٹیمپلیٹ ماخذ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## فوری آغاز: آپ کی repository میں خودکار مطابقت پذیری کو فعال کریں

اپنے README میں "دیگر کورسز" سیکشن کے ارد گرد درج ذیل مارکرز شامل کریں۔ Co-op Translator ہر رن پر ان مارکرز کے درمیان موجود تمام مواد کو تبدیل کر دے گا۔

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

جب بھی Co-op Translator چلتا ہے — CLI کے ذریعے (مثلاً `translate -l "<language codes>"`) یا GitHub Actions کے ذریعہ — یہ خودکار طور پر ان مارکرز کے اندر موجود "دیگر کورسز" سیکشن کو اپ ڈیٹ کر دیتا ہے۔

> [!NOTE]
> اگر آپ کے پاس پہلے سے موجود فہرست ہے، تو بس اس کے ارد گرد وہی مارکرز لگا دیں۔ اگلا رن اسے تازہ ترین معیاری مواد سے بدل دے گا۔

---

## عالمی مواد کو کیسے تبدیل کریں

اگر آپ وہ معیاری مواد اپ ڈیٹ کرنا چاہتے ہیں جو تمام Beginners repositories میں ظاہر ہوتا ہے:

1. ٹیمپلیٹ کو ایڈٹ کریں: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. اپنے تبدیلیوں کے ساتھ Co-op Translator repository کے لیے pull request کھولیں
3. PR کے مرج ہونے کے بعد، Co-op Translator کا ورژن اپ ڈیٹ ہو جائے گا
4. جب اگلی بار Co-op Translator چلایا جائے گا (CLI یا GitHub Action کے ذریعے) کسی ہدف repository میں، تو یہ خودکار طور پر اپ ڈیٹ شدہ سیکشن کو مطابقت دے گا

اس سے "دیگر کورسز" کے مواد کے لیے تمام Beginners repositories میں ایک واحد حقیقی ماخذ کی ضمانت ملتی ہے۔

## repository کے سائز

زیادہ زبانوں میں ترجمہ کیے جانے کی وجہ سے repositories بڑے ہو سکتے ہیں تاکہ اختتامی صارفین کو clone - sparse استعمال کرنے کی رہنمائی دی جا سکے تاکہ صرف ضروری زبانوں کو کلون کیا جائے اور پورے repository کو نہیں۔

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
**ڈس کلیمر**:  
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھا جائے گا۔ اہم معلومات کے لئے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریحات کی ہم ذمہ دار نہیں ہوں گے۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->