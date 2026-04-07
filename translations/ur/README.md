# Co-op Translator

_تعلیمی GitHub مواد کے لیے ترجموں کو بآسانی خودکار بنائیں اور متعدد زبانوں میں اپنے پروجیکٹ کی ترقی کے ساتھ ترجمے برقرار رکھیں۔_

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

### 🌐 کثیراللسانی حمایت

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) کی حمایت یافتہ

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](./README.md) | [Vietnamese](../vi/README.md)

> **کیا آپ مقامی طور پر کلون کرنا پسند کریں گے؟**
>
> اس ذخیرے میں 50+ زبانوں کے ترجمے شامل ہیں جو ڈاؤن لوڈ کے حجم کو کافی بڑھا دیتے ہیں۔ ترجموں کے بغیر کلون کرنے کے لیے sparse checkout استعمال کریں:
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
> اس سے آپ کو کورس مکمل کرنے کے لیے ہر چیز بہترین اور تیز تر ڈاؤن لوڈ کے ساتھ حاصل ہو جاتی ہے۔
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## جائزہ

**Co-op Translator** آپ کو آپ کے تعلیمی GitHub مواد کو بآسانی متعدد زبانوں میں مقامی نوعیت دینے میں مدد دیتا ہے۔
جب آپ اپنے Markdown فائلوں، تصاویر، یا نوٹ بکس کو اپ ڈیٹ کرتے ہیں، تو ترجمے خودکار طور پر ہم آہنگ رہتے ہیں، اس بات کو یقینی بناتے ہوئے کہ آپ کا مواد عالمی طلباء کے لیے درست اور اپ ٹو ڈیٹ رہے۔

ترجمہ شدہ مواد کی تنظیم کی مثال:

![Example](../../imgs/translation-ex.png)

## ترجمے کی حالت کا انتظام کیسے کیا جاتا ہے

Co-op Translator ترجمہ شدہ مواد کو **ورژن شدہ سوفٹ ویئر آرٹیفیکٹس** کی صورت میں انتظام دیتا ہے،  
نہ کہ حیثیت میں ساکن فائلوں کی طرح۔

یہ آلہ ترجمہ شدہ Markdown، تصاویر، اور نوٹ بکس کی حالت کو  
**زبان کے دائرہ اختیار metadata** کے ذریعے ٹریک کرتا ہے۔

یہ ڈیزائن Co-op Translator کو اجازت دیتا ہے:

- پرانے ترجموں کا مؤثر پتہ لگانا
- Markdown، تصاویر، اور نوٹ بکس کے ساتھ یکساں سلوک کرنا
- بڑے، تیزی سے بڑھتے ہوئے، کثیراللسانی ذخائر پر محفوظ پیمانے پر کام کرنا

ترجموں کو منظم شدہ آرٹیفیکٹس کے طور پر ماڈل بنا کر، ترجمہ ورک فلو جدید سوفٹ ویئر  
انحصار اور آرٹیفیکٹ مینجمنٹ کی مشقوں کے ساتھ قدرتی طور پر مطابقت رکھتا ہے۔

→ [ترجمے کی حالت کا انتظام کیسے کیا جاتا ہے](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## فوری آغاز

```bash
# ایک ورچوئل ماحول بنائیں اور اسے فعال کریں (تجویز کردہ)
python -m venv .venv
# ونڈوز
.venv\Scripts\activate
# میک او ایس/لینکس
source .venv/bin/activate
# پیکیج انسٹال کریں
pip install co-op-translator
# ترجمہ کریں
translate -l "ko ja fr" -md
```

ڈوکر:

```bash
# GHCR سے پبلک امیج کھینچیں
docker pull ghcr.io/azure/co-op-translator:latest
# موجودہ فولڈر کے ساتھ چلائیں اور .env فراہم کریں (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## کم از کم سیٹ اپ

1. یقین دہانی کریں کہ آپ کے پاس سپورٹ شدہ Python ورژن ہے (فی الحال 3.10-3.12)۔ poetry (pyproject.toml) میں یہ خودکار طور پر ہینڈل کیا جاتا ہے۔
2. ایک `.env` فائل بنائیں سانچے کا استعمال کرتے ہوئے: [.env.template](../../.env.template)
3. ایک LLM پرووائیڈر کو ترتیب دیں (Azure OpenAI یا OpenAI)
4. (اختیاری) تصویر کے ترجمے کے لیے (`-img`)، Azure AI Vision کو ترتیب دیں
5. (اختیاری) آپ ایک سے زیادہ اسناد سیٹ ترتیب دے سکتے ہیں، متغیرات کو suffixes جیسے `_1`، `_2` وغیرہ کے ساتھ دوہرا کر۔ ایک سیٹ میں تمام متغیرات کا suffix ایک جیسا ہونا چاہیے۔
6. (تجویز کردہ) سابقہ ترجمے صاف کریں تاکہ تصادم سے بچا جا سکے (مثلاً `translations/`)
7. (تجویز کردہ) اپنے README میں ترجمہ سیکشن شامل کریں [README languages template](./getting_started/README_languages_template.md) کا استعمال کرتے ہوئے
8. دیکھیں: [Azure AI سیٹ اپ کریں](./getting_started/set-up-azure-ai.md)

## استعمال

تاکہ تمام حمایت شدہ اقسام کا ترجمہ کریں:

```bash
translate -l "ko ja"
```

صرف Markdown:

```bash
translate -l "de" -md
```

Markdown + تصاویر:

```bash
translate -l "pt" -md -img
```

صرف نوٹ بکس:

```bash
translate -l "zh" -nb
```

مزید فلیگز: [کمانڈ ریفرنس](./getting_started/command-reference.md)

## خصوصیات

- Markdown، نوٹ بکس، اور تصاویر کا خودکار ترجمہ
- ترجموں کو ماخذ کی تبدیلیوں کے ساتھ ہم آہنگ رکھتا ہے
- مقامی (CLI) یا CI (GitHub Actions) میں کام کرتا ہے
- Azure OpenAI یا OpenAI استعمال کرتا ہے؛ تصاویر کے لیے اختیاری Azure AI Vision
- Markdown کی فارمیٹنگ اور ساخت کو برقرار رکھتا ہے

## دستاویزات

- [کمانڈ لائن گائیڈ](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions گائیڈ (عوامی ذخائر اور معیاری راز)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions گائیڈ (Microsoft تنظیمی ذخائر اور تنظیمی سطح پر سیٹ اپ)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README زبانوں کا سانچہ](./getting_started/README_languages_template.md)
- [سپورٹ شدہ زبانیں](./getting_started/supported-languages.md)
- [شراکت داری](./CONTRIBUTING.md)
- [مسائل کا حل](./getting_started/troubleshooting.md)

### Microsoft مخصوص گائیڈ
> [!NOTE]
> صرف Microsoft “For Beginners” ذخیرہ رکھنے والوں کے لیے۔

- [“Other courses” کی فہرست کو اپ ڈیٹ کرنا (صرف MS Beginners ذخائر کے لیے)](./getting_started/update-other-courses.md)

## ہمارے ساتھ تعاون کریں اور عالمی تعلیم کو فروغ دیں

ہمارے ساتھ شامل ہوں اور تعلیماتی مواد کو عالمی سطح پر بانٹنے کے طریقے میں انقلاب لائیں! [Co-op Translator](https://github.com/azure/co-op-translator) کو GitHub پر ⭐ دیں اور زبانوں کی رکاوٹوں کو ختم کرنے کے ہمارے مشن کی حمایت کریں۔ آپ کی دلچسپی اور شراکتیں بہت اہم اثر ڈالتی ہیں! کوڈ تعاون اور خصوصیت کی تجاویز ہمیشہ خوش آئند ہیں۔

### Microsoft تعلیمی مواد کو اپنی زبان میں دریافت کریں

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

## ویڈیو پریزنٹیشنز

👉 یوٹیوب پر دیکھنے کے لیے نیچے تصویر پر کلک کریں۔

- **Open at Microsoft**: Co-op Translator کا مختصر 18 منٹ کا تعارف اور فوری رہنمائی۔

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## تعاون

یہ پروجیکٹ شراکتوں اور تجاویز کا خیرم مقدم کرتا ہے۔ Azure Co-op Translator میں تعاون کرنے میں دلچسپی رکھتے ہیں؟ براہ کرم ہمارے [CONTRIBUTING.md](./CONTRIBUTING.md) ملاحظہ کریں تاکہ معلوم ہو سکے کہ آپ Co-op Translator کو مزید قابل رسائی بنانے میں کیسے مدد کر سکتے ہیں۔

## شراکت داران
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ضابطہ اخلاق

اس پروجیکٹ نے [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) کو اپنایا ہے۔
مزید معلومات کے لئے [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) دیکھیں یا
کسی بھی اضافی سوالات یا تبصروں کے لئے [opencode@microsoft.com](mailto:opencode@microsoft.com) سے رابطہ کریں۔

## ذمہ دار AI

Microsoft اس بات کے لیے پرعزم ہے کہ ہمارے صارفین ہمارے AI مصنوعات کو ذمہ داری سے استعمال کریں، اپنے تجربات شیئر کریں، اور Transparency Notes اور Impact Assessments جیسے ٹولز کے ذریعے اعتماد پر مبنی شراکت داریاں قائم کریں۔ ان وسائل میں سے کئی [https://aka.ms/RAI](https://aka.ms/RAI) پر دستیاب ہیں۔
Microsoft کا ذمہ دار AI کا طریقہ کار ہمارے AI اصولوں پر مبنی ہے جن میں انصاف، اعتبار اور حفاظت، پرائیویسی اور سیکیورٹی، شمولیت، شفافیت، اور جوابدہی شامل ہیں۔

بڑے پیمانے پر قدرتی زبان، تصویر، اور تقریر کے ماڈلز—جیسے کہ اس نمونے میں استعمال ہونے والے—ممکنہ طور پر غیر منصفانہ، غیر معتبر، یا توہین آمیز رویہ اختیار کر سکتے ہیں، جو کہ نقصان دہ ہو سکتے ہیں۔ براہ کرم خطرات اور حدود کے بارے میں معلومات کے لیے [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) سے رجوع کریں۔

ان خطرات کو کم کرنے کا تجویز کردہ طریقہ یہ ہے کہ آپ کی فن تعمیر میں ایک حفاظتی نظام شامل کیا جائے جو نقصان دہ رویے کو شناخت اور روک سکے۔ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ایک آزاد حفاظتی پرت فراہم کرتا ہے، جو ایپلیکیشنز اور خدمات میں نقصان دہ صارف یا AI کے ذریعہ تیار کردہ مواد کو شناخت کر سکتا ہے۔ Azure AI Content Safety میں متن اور تصویر کے API شامل ہیں جو آپ کو نقصان دہ مواد کو شناخت کرنے کی اجازت دیتے ہیں۔ ہمارے پاس ایک interactive Content Safety Studio بھی ہے جو آپ کو مختلف سانچوں میں نقصان دہ مواد کی جانچ کرنے اور نمونہ کوڈ کو دیکھنے اور آزمائش کرنے کی سہولت دیتا ہے۔ درج ذیل [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) آپ کو سروس کے لیے درخواستیں بنانے میں رہنمائی فراہم کرتی ہے۔

ایک اور پہلو جس پر غور کرنا چاہیے وہ مجموعی درخواست کی کارکردگی ہے۔ کثیرالسانی اور کثیرماڈل ایپلیکیشنز کے ساتھ، ہم کارکردگی کا مطلب سمجھتے ہیں کہ نظام آپ اور آپ کے صارفین کی توقعات کے مطابق کام کرے، جس میں نقصان دہ نتائج پیدا نہ ہوں۔ اپنی مجموعی ایپلیکیشن کی کارکردگی کا اندازہ لگانا اہم ہے، [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) کا استعمال کرتے ہوئے۔

آپ اپنے AI ایپلیکیشن کا اپنے ترقیاتی ماحول میں [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) استعمال کرتے ہوئے جائزہ لے سکتے ہیں۔ چاہے کوئی ٹیسٹ ڈیٹا سیٹ ہو یا کوئی ہدف، آپ کی جنیریٹو AI ایپلیکیشن کی تخلیقات خود بخود بلٹ ان یا اپنی مرضی کے مطابق ایویلیویٹرز کے ذریعے مقداری طور پر ماپی جاتی ہیں۔ اپنے نظام کا جائزہ لینے کے لیے prompt flow sdk کے ساتھ شروع کرنے کے لیے، آپ [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پر عمل کر سکتے ہیں۔ جائزہ کی تکمیل کے بعد، آپ [Azure AI Studio میں نتائج دیکھ سکتے ہیں](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)۔

## ٹریڈ مارکس

اس پروجیکٹ میں پروجیکٹس، مصنوعات، یا خدمات کے ٹریڈ مارکس یا لوگوز شامل ہو سکتے ہیں۔ Microsoft کے
ٹریڈ مارکس یا لوگوز کے مجاز استعمال کو [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) کے مطابق ہونا چاہیے۔
Microsoft کے ٹریڈ مارکس یا لوگوز کو اس پروجیکٹ کے ترمیم شدہ ورژن میں استعمال کرنے سے الجھن نہیں ہونی چاہیے اور نہ ہی Microsoft کی سرپرستی کا مطلب ہونا چاہیے۔
تیسرے فریق کے ٹریڈ مارکس یا لوگوز کے تمام استعمال متعلقہ فریق کی پالیسیوں کے تابع ہوں گے۔

## مدد حاصل کریں

اگر آپ پھنس جائیں یا AI ایپس بنانے کے بارے میں کوئی سوال ہو تو شامل ہوں:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر آپ کے پاس پیداوار کے بارے میں آراء یا تعمیر کے دوران غلطیاں ہوں تو ملاحظہ کریں:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دستخط:**  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے استعمال سے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لئے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا بے ضابطگیاں ہو سکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->