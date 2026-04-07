# "دیگر کورسز" سیکشن کو اپ ڈیٹ کریں (Microsoft Beginners ریپوز)

یہ رہنما بتاتی ہے کہ کیسے "دیگر کورسز" سیکشن کو Co-op Translator کے ذریعے خودکار ہم وقت ساز بنایا جائے، اور تمام ریپوز کے لیے عالمی ٹیمپلیٹ کو کیسے اپ ڈیٹ کیا جائے۔

- لاگو ہوتا ہے: صرف Microsoft Beginners ریپوز پر  
- کام کرتا ہے: Co-op Translator CLI اور GitHub Actions کے ساتھ  
- ٹیمپلیٹ کا ذریعہ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## فوری آغاز: اپنے ریپو میں خودکار ہم وقت سازی کو فعال کریں

اپنے README میں "دیگر کورسز" سیکشن کے گرد درج ذیل مارکر شامل کریں۔ Co-op Translator ہر بار ان مارکرز کے درمیان موجود تمام مواد کو تبدیل کر دے گا۔

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ہر بار جب Co-op Translator چلتا ہے — CLI کے ذریعے (مثلاً `translate -l "<language codes>"`) یا GitHub Actions میں — یہ خودکار طریقے سے ان مارکرز سے گھری ہوئی "دیگر کورسز" سیکشن کو تازہ ترین کر دیتا ہے۔

> [!NOTE]  
> اگر آپ کے پاس پہلے سے موجود فہرست ہے تو اسے بس انہی مارکرز کے ساتھ لپیٹ دیں۔ اگلا رن اسے تازہ ترین معیاری مواد سے تبدیل کر دے گا۔

---

## عالمی مواد کو تبدیل کرنے کا طریقہ

اگر آپ اس معیاری مواد کو اپ ڈیٹ کرنا چاہتے ہیں جو تمام Beginners ریپوز میں دکھائی دیتا ہے:

1. ٹیمپلیٹ کو ایڈٹ کریں: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. اپنے تبدیلیوں کے ساتھ Co-op Translator ریپو میں ایک pull request کھولیں  
3. PR کے مرج ہونے کے بعد، Co-op Translator کا ورژن اپ ڈیٹ ہو جائے گا  
4. جب بھی اگلی بار Co-op Translator (CLI یا GitHub Action) ایک ہدف ریپو میں چلے گا، تو یہ خودکار طور پر اپ ڈیٹ شدہ سیکشن کو ہم وقت ساز کر دے گا

یہ تمام Beginners ریپوز میں "دیگر کورسز" کے مواد کے لیے ایک واحد حقائق کا ذریعہ یقینی بناتا ہے۔

## ریپو سائزز

ریپوز زبانوں کی تعداد کی وجہ سے بڑے ہو سکتے ہیں جن میں ترجمہ کیا گیا ہے تاکہ صارفین کو رہنمائی کرنے میں مدد ملے کہ وہ clone - sparse کا استعمال کیسے کریں تاکہ صرف ضروری زبانیں کلون کی جائیں اور پورا ریپو نہ لیا جائے

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
**ڈسکلیمر**:
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے ضابطگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی اصل زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->