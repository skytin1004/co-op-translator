# 🌐 کثیراللسانی معاونت (سانچہ)

منتظمین: نیچے دیا گیا بلاک Co-op Translator کے زیر انتظام "تمام زبانوں" کی مثال ہے۔

- اگر آپ چاہتے ہیں کہ Co-op Translator اس فہرست کو مکمل طور پر خودکار طریقے سے تازہ رکھے جب بھی آپ `translate` چلائیں (کسی بھی زبان کے انتخاب کے ساتھ)، تو دو کمنٹ مارکرز کو جوں کا توں رکھیں۔
- اگر آپ صرف زبانوں کا ایک ذیلی مجموعہ دکھانا چاہتے ہیں، تو دونوں کمنٹ مارکرز کو حذف کر دیں اور کسی بھی زبان کو ہٹا دیں جسے آپ فہرست میں شامل نہیں کرنا چاہتے۔ مارکرز کو حذف کرنے کے بعد، Co-op Translator اس سیکشن کو خودکار طریقے سے تبدیل نہیں کرے گا۔

- اس سیکشن میں اب "کیا آپ لوکل کلون کرنا ترجیح دیتے ہیں؟" کے مشورے کو شامل کیا گیا ہے تاکہ صارفین کو بڑے ترجمہ بوجھ کے بغیر کلون کرنے میں مدد ملے۔ آپ اپنے مخزن کے URL کے ساتھ اس مشورے کو ذاتی بنا سکتے ہیں، مثلاً:
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](./README.md) | [Vietnamese](../vi/README.md)
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
**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشاں ہیں، تاہم براہ کرم آگاہ رہیں کہ خودکار ترجموں میں غلطیاں یا عدم وضاحت ہوسکتی ہے۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ سمجھا جائے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->