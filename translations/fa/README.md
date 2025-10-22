<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T11:52:24+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# مترجم Co-op

_به راحتی ترجمه محتوای آموزشی خود در گیت‌هاب را به زبان‌های مختلف خودکار کنید تا به مخاطبان جهانی دسترسی پیدا کنید._

### 🌐 پشتیبانی از چند زبان

#### پشتیبانی شده توسط <a href="https://github.com/Azure/Co-op-Translator">Co-op Translator</a>

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
<a href="./translations/ar/README.md">عربی</a> | <a href="./translations/bn/README.md">بنگالی</a> | <a href="./translations/bg/README.md">بلغاری</a> | <a href="./translations/my/README.md">برمه‌ای (میانمار)</a> | <a href="./translations/zh/README.md">چینی (ساده)</a> | <a href="./translations/hk/README.md">چینی (سنتی، هنگ‌کنگ)</a> | <a href="./translations/mo/README.md">چینی (سنتی، ماکائو)</a> | <a href="./translations/tw/README.md">چینی (سنتی، تایوان)</a> | <a href="./translations/hr/README.md">کروات</a> | <a href="./translations/cs/README.md">چکی</a> | <a href="./translations/da/README.md">دانمارکی</a> | <a href="./translations/nl/README.md">هلندی</a> | <a href="./translations/et/README.md">استونیایی</a> | <a href="./translations/fi/README.md">فنلاندی</a> | <a href="./translations/fr/README.md">فرانسوی</a> | <a href="./translations/de/README.md">آلمانی</a> | <a href="./translations/el/README.md">یونانی</a> | <a href="./translations/he/README.md">عبری</a> | <a href="./translations/hi/README.md">هندی</a> | <a href="./translations/hu/README.md">مجارستانی</a> | <a href="./translations/id/README.md">اندونزیایی</a> | <a href="./translations/it/README.md">ایتالیایی</a> | <a href="./translations/ja/README.md">ژاپنی</a> | <a href="./translations/ko/README.md">کره‌ای</a> | <a href="./translations/lt/README.md">لیتوانیایی</a> | <a href="./translations/ms/README.md">مالایی</a> | <a href="./translations/mr/README.md">مراتی</a> | <a href="./translations/ne/README.md">نپالی</a> | <a href="./translations/pcm/README.md">پیدجین نیجریه‌ای</a> | <a href="./translations/no/README.md">نروژی</a> | <a href="./translations/fa/README.md">فارسی</a> | <a href="./translations/pl/README.md">لهستانی</a> | <a href="./translations/br/README.md">پرتغالی (برزیل)</a> | <a href="./translations/pt/README.md">پرتغالی (پرتغال)</a> | <a href="./translations/pa/README.md">پنجابی (گورموخی)</a> | <a href="./translations/ro/README.md">رومانیایی</a> | <a href="./translations/ru/README.md">روسی</a> | <a href="./translations/sr/README.md">صربی (سیریلیک)</a> | <a href="./translations/sk/README.md">اسلواکی</a> | <a href="./translations/sl/README.md">اسلوونیایی</a> | <a href="./translations/es/README.md">اسپانیایی</a> | <a href="./translations/sw/README.md">سواحیلی</a> | <a href="./translations/sv/README.md">سوئدی</a> | <a href="./translations/tl/README.md">تاگالوگ (فیلیپینی)</a> | <a href="./translations/ta/README.md">تامیلی</a> | <a href="./translations/th/README.md">تایلندی</a> | <a href="./translations/tr/README.md">ترکی</a> | <a href="./translations/uk/README.md">اوکراینی</a> | <a href="./translations/ur/README.md">اردو</a> | <a href="./translations/vi/README.md">ویتنامی</a>
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## معرفی

**Co-op Translator** به شما کمک می‌کند تا محتوای آموزشی گیت‌هاب خود را به سرعت به زبان‌های مختلف ترجمه کنید و به راحتی به مخاطبان جهانی دسترسی پیدا کنید. هر زمان که فایل‌های Markdown، تصاویر یا نوت‌بوک‌های Jupyter خود را به‌روزرسانی کنید، ترجمه‌ها به طور خودکار همگام می‌شوند تا محتوای آموزشی شما برای کاربران بین‌المللی همیشه تازه و مرتبط باقی بماند.

نحوه سازماندهی محتوای آموزشی ترجمه‌شده توسط Co-op Translator را ببینید:

<img src="../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fa.png" alt="نمونه">

## شروع سریع

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

داکر:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## راه‌اندازی ساده

- یک فایل `.env` با استفاده از قالب بسازید: <a href="./.env.template">.env.template</a>
- یک ارائه‌دهنده LLM (Azure OpenAI یا OpenAI) را پیکربندی کنید
- برای ترجمه تصویر (`-img`)، Azure AI Vision را نیز تنظیم کنید
- توصیه می‌شود: اگر ترجمه‌هایی توسط ابزارهای دیگر دارید، ابتدا آن‌ها را پاک کنید تا تداخل ایجاد نشود (مثلاً: `translations/`)
- توصیه می‌شود: یک بخش ترجمه به README خود اضافه کنید با استفاده از <a href="./README_languages_template.md">قالب زبان‌های README</a>
- ببینید: <a href="./getting_started/set-up-azure-ai.md">راه‌اندازی Azure AI</a>

## نحوه استفاده

ترجمه همه انواع پشتیبانی‌شده:

```bash
translate -l "ko ja"
```

فقط Markdown:

```bash
translate -l "de" -md
```

Markdown + تصاویر:

```bash
translate -l "pt" -md -img
```

فقط نوت‌بوک‌ها:

```bash
translate -l "zh" -nb
```

پرچم‌های بیشتر: <a href="./getting_started/command-reference.md">مرجع دستورات</a>

## قابلیت‌ها

- ترجمه خودکار برای Markdown، نوت‌بوک‌ها و تصاویر
- ترجمه‌ها را با تغییرات منبع همگام نگه می‌دارد
- به صورت محلی (CLI) یا در CI (GitHub Actions) کار می‌کند
- از Azure OpenAI یا OpenAI استفاده می‌کند؛ Azure AI Vision برای تصاویر اختیاری است
- قالب‌بندی و ساختار Markdown را حفظ می‌کند

## مستندات

- <a href="./getting_started/command-line-guide/command-line-guide.md">راهنمای خط فرمان</a>
- <a href="./getting_started/github-actions-guide/github-actions-guide-public.md">راهنمای GitHub Actions (مخازن عمومی و رمزهای استاندارد)</a>
- <a href="./getting_started/github-actions-guide/github-actions-guide-org.md">راهنمای GitHub Actions (مخازن سازمانی مایکروسافت و تنظیمات سطح سازمان)</a>
- <a href="./getting_started/supported-languages.md">زبان‌های پشتیبانی‌شده</a>
- <a href="./getting_started/troubleshooting.md">رفع اشکال</a>

## از ما حمایت کنید و یادگیری جهانی را گسترش دهید

با ما همراه شوید تا نحوه اشتراک‌گذاری محتوای آموزشی در سراسر جهان را متحول کنیم! به <a href="https://github.com/azure/co-op-translator">Co-op Translator</a> در گیت‌هاب یک ⭐ بدهید و از ماموریت ما برای رفع موانع زبانی در یادگیری و فناوری حمایت کنید. علاقه و مشارکت شما تاثیر بزرگی دارد! مشارکت در کد و پیشنهاد ویژگی‌ها همیشه خوش‌آمد است.

### محتوای آموزشی مایکروسافت را به زبان خودتان کشف کنید

- <a href="https://github.com/microsoft/AZD-for-beginners">AZD برای مبتدیان</a>
- <a href="https://github.com/microsoft/edgeai-for-beginners">Edge AI برای مبتدیان</a>
- <a href="https://github.com/microsoft/mcp-for-beginners">پروتکل Model Context (MCP) برای مبتدیان</a>
- <a href="https://github.com/microsoft/ai-agents-for-beginners">عامل‌های هوش مصنوعی برای مبتدیان</a>
- <a href="https://github.com/microsoft/Generative-AI-for-beginners-dotnet">هوش مصنوعی مولد برای مبتدیان با .NET</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners">هوش مصنوعی مولد برای مبتدیان</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners-java">هوش مصنوعی مولد برای مبتدیان با جاوا</a>
- <a href="https://aka.ms/ml-beginners">یادگیری ماشین برای مبتدیان</a>
- <a href="https://aka.ms/datascience-beginners">علم داده برای مبتدیان</a>
- <a href="https://aka.ms/ai-beginners">هوش مصنوعی برای مبتدیان</a>
- <a href="https://github.com/microsoft/Security-101">امنیت سایبری برای مبتدیان</a>
- <a href="https://aka.ms/webdev-beginners">توسعه وب برای مبتدیان</a>
- <a href="https://aka.ms/iot-beginners">اینترنت اشیا برای مبتدیان</a>
- <a href="https://github.com/microsoft/PhiCookBook">PhiCookBook</a>

## ارائه‌های ویدیویی

برای آشنایی بیشتر با Co-op Translator ارائه‌های ما را ببینید _(روی تصویر زیر کلیک کنید تا در یوتیوب ببینید.)_:

- **Open at Microsoft**: معرفی کوتاه ۱۸ دقیقه‌ای و راهنمای سریع استفاده از Co-op Translator.

  <a href="https://www.youtube.com/watch?v=jX_swfH_KNU"><img src="../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fa.jpg" alt="Open at Microsoft"></a>

## مشارکت

این پروژه از مشارکت و پیشنهادات استقبال می‌کند. علاقه‌مند به همکاری در Azure Co-op Translator هستید؟ لطفاً <a href="./CONTRIBUTING.md">CONTRIBUTING.md</a> را برای راهنمایی نحوه کمک به دسترس‌پذیرتر شدن Co-op Translator ببینید.

## مشارکت‌کنندگان

<a href="https://github.com/Azure/co-op-translator/graphs/contributors"><img src="https://contrib.rocks/image?repo=Azure/co-op-translator" alt="مشارکت‌کنندگان co-op-translator"></a>

## منشور رفتاری

این پروژه از <a href="https://opensource.microsoft.com/codeofconduct/">منشور رفتاری متن‌باز مایکروسافت</a> پیروی می‌کند.
برای اطلاعات بیشتر <a href="https://opensource.microsoft.com/codeofconduct/faq/">سوالات متداول منشور رفتاری</a> را ببینید یا
با <a href="mailto:opencode@microsoft.com">opencode@microsoft.com</a> تماس بگیرید.

## هوش مصنوعی مسئولانه

مایکروسافت متعهد است که به مشتریان خود کمک کند تا محصولات هوش مصنوعی را به شکل مسئولانه استفاده کنند، تجربیات خود را به اشتراک بگذارد و با ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی تاثیر، اعتمادسازی کند. بسیاری از این منابع را می‌توانید در <a href="https://aka.ms/RAI">https://aka.ms/RAI</a> پیدا کنید.
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول انصاف، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، فراگیری، شفافیت و پاسخگویی استوار است.

مدل‌های بزرگ زبان طبیعی، تصویر و گفتار - مانند مدل‌هایی که در این نمونه استفاده شده‌اند - ممکن است رفتارهای ناعادلانه، غیرقابل اعتماد یا توهین‌آمیز داشته باشند که می‌تواند آسیب‌هایی ایجاد کند. لطفاً <a href="https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text">یادداشت شفافیت سرویس Azure OpenAI</a> را مطالعه کنید تا از ریسک‌ها و محدودیت‌ها آگاه شوید.

رویکرد پیشنهادی برای کاهش این ریسک‌ها، افزودن یک سیستم ایمنی به معماری شماست که بتواند رفتارهای مضر را شناسایی و جلوگیری کند. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> یک لایه محافظتی مستقل فراهم می‌کند که قادر است محتوای مضر تولیدشده توسط کاربر یا هوش مصنوعی را در برنامه‌ها و سرویس‌ها شناسایی کند. Azure AI Content Safety شامل APIهای متن و تصویر است که به شما امکان می‌دهد محتوای مضر را شناسایی کنید. همچنین یک Content Safety Studio تعاملی داریم که می‌توانید کد نمونه را برای شناسایی محتوای مضر در حالت‌های مختلف مشاهده و امتحان کنید. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">مستندات شروع سریع</a> شما را در ارسال درخواست به سرویس راهنمایی می‌کند.

یک جنبه‌ی دیگر که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندمدلی و چندحالته، منظور از عملکرد این است که سیستم همان‌طور که شما و کاربران‌تان انتظار دارید عمل کند، از جمله اینکه خروجی‌های مضر تولید نکند. ارزیابی عملکرد کلی برنامه با استفاده از [شاخص‌های کیفیت تولید و معیارهای ریسک و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) اهمیت دارد.

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه با استفاده از [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با داشتن یک مجموعه داده آزمایشی یا هدف مشخص، تولیدات برنامه هوش مصنوعی شما به صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی مورد سنجش قرار می‌گیرند. برای شروع ارزیابی سیستم با prompt flow sdk می‌توانید [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) را دنبال کنید. پس از اجرای یک ارزیابی، می‌توانید [نتایج را در Azure AI Studio مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت تابع و باید مطابق با [راهنمای علائم تجاری و برند مایکروسافت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) باشد.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید باعث سردرگمی یا القای حمایت مایکروسافت شود.
هرگونه استفاده از علائم تجاری یا لوگوهای شخص ثالث تابع سیاست‌های آن‌هاست.

## دریافت کمک

اگر در ساخت برنامه‌های هوش مصنوعی به مشکل برخوردید یا سوالی داشتید، به این انجمن بپیوندید:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

اگر بازخورد محصولی دارید یا هنگام ساخت با خطا مواجه شدید، به این انجمن مراجعه کنید:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادقتی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.