<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:25:28+00:00",
  "source_file": "README.md",
  "language_code": "fa"
}
-->
# مترجم Co-op

_به راحتی ترجمه محتوای آموزشی گیت‌هاب خود را به چندین زبان مختلف خودکار کنید تا به مخاطبان جهانی دسترسی پیدا کنید._

### 🌐 پشتیبانی از چند زبان

#### پشتیبانی شده توسط [Co-op Translator](https://github.com/Azure/Co-op-Translator)

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](./README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## معرفی

**Co-op Translator** به شما این امکان را می‌دهد که محتوای آموزشی گیت‌هاب خود را به سرعت به چندین زبان مختلف ترجمه کنید و به راحتی به مخاطبان جهانی دسترسی پیدا کنید. هر زمان که فایل‌های Markdown، تصاویر یا نوت‌بوک‌های Jupyter خود را به‌روزرسانی کنید، ترجمه‌ها به طور خودکار همگام‌سازی می‌شوند تا محتوای آموزشی شما برای کاربران بین‌المللی همیشه تازه و مرتبط باقی بماند.

نحوه سازماندهی محتوای آموزشی ترجمه‌شده توسط Co-op Translator را ببینید:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fa.png)

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

## راه‌اندازی حداقلی

- یک فایل `.env` با استفاده از قالب [.env.template](../../.env.template) بسازید
- یکی از ارائه‌دهندگان LLM (Azure OpenAI یا OpenAI) را پیکربندی کنید
- برای ترجمه تصویر (`-img`)، Azure AI Vision را نیز تنظیم کنید
- توصیه می‌شود: اگر ترجمه‌هایی توسط ابزارهای دیگر تولید کرده‌اید، ابتدا آن‌ها را پاک کنید تا از تداخل جلوگیری شود (مثلاً: `translations/`).
- توصیه می‌شود: یک بخش ترجمه به README خود اضافه کنید با استفاده از [قالب زبان‌های README](./README_languages_template.md)
- ببینید: [راه‌اندازی Azure AI](./getting_started/set-up-azure-ai.md)

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

پرچم‌های بیشتر: [مرجع دستورات](./getting_started/command-reference.md)

## قابلیت‌ها

- ترجمه خودکار برای Markdown، نوت‌بوک‌ها و تصاویر
- همگام‌سازی ترجمه‌ها با تغییرات منبع
- قابل استفاده به صورت محلی (CLI) یا در CI (GitHub Actions)
- استفاده از Azure OpenAI یا OpenAI؛ Azure AI Vision اختیاری برای تصاویر
- حفظ ساختار و قالب‌بندی Markdown

## مستندات

- [راهنمای خط فرمان](./getting_started/command-line-guide/command-line-guide.md)
- [راهنمای GitHub Actions (مخازن عمومی و رمزهای استاندارد)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [راهنمای GitHub Actions (مخازن سازمانی مایکروسافت و تنظیمات سطح سازمان)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [زبان‌های پشتیبانی‌شده](./getting_started/supported-languages.md)
- [رفع اشکال](./getting_started/troubleshooting.md)

## از ما حمایت کنید و یادگیری جهانی را گسترش دهید

به ما بپیوندید تا نحوه به اشتراک‌گذاری محتوای آموزشی در سراسر جهان را متحول کنیم! به [Co-op Translator](https://github.com/azure/co-op-translator) در گیت‌هاب ⭐ بدهید و از مأموریت ما برای رفع موانع زبانی در یادگیری و فناوری حمایت کنید. علاقه و مشارکت شما تأثیر قابل توجهی دارد! مشارکت در کد و پیشنهاد ویژگی‌های جدید همیشه خوش‌آمد است.

### محتوای آموزشی مایکروسافت را به زبان خودتان کشف کنید

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

## ارائه‌های ویدیویی

برای آشنایی بیشتر با Co-op Translator ارائه‌های ما را ببینید _(برای تماشا در یوتیوب روی تصویر زیر کلیک کنید.)_:

- **Open at Microsoft**: معرفی کوتاه ۱۸ دقیقه‌ای و راهنمای سریع برای استفاده از Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fa.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## مشارکت

این پروژه از مشارکت و پیشنهادات استقبال می‌کند. علاقه‌مند به مشارکت در Azure Co-op Translator هستید؟ لطفاً [CONTRIBUTING.md](./CONTRIBUTING.md) ما را برای راهنمایی درباره نحوه کمک به دسترس‌پذیرتر شدن Co-op Translator ببینید.

## مشارکت‌کنندگان

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## منشور رفتاری

این پروژه از [منشور رفتاری متن‌باز مایکروسافت](https://opensource.microsoft.com/codeofconduct/) پیروی می‌کند.
برای اطلاعات بیشتر به [سؤالات متداول منشور رفتاری](https://opensource.microsoft.com/codeofconduct/faq/) مراجعه کنید یا
با [opencode@microsoft.com](mailto:opencode@microsoft.com) برای هرگونه سؤال یا نظر اضافی تماس بگیرید.

## هوش مصنوعی مسئولانه

مایکروسافت متعهد است که به مشتریان خود برای استفاده مسئولانه از محصولات هوش مصنوعی کمک کند، تجربیات خود را به اشتراک بگذارد و از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی تأثیر، مشارکت‌های مبتنی بر اعتماد ایجاد کند. بسیاری از این منابع را می‌توانید در [https://aka.ms/RAI](https://aka.ms/RAI) بیابید.
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول انصاف، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، شمول، شفافیت و پاسخگویی استوار است.

مدل‌های زبان طبیعی، تصویر و گفتار در مقیاس بزرگ - مانند آن‌هایی که در این نمونه استفاده شده‌اند - ممکن است به شیوه‌هایی ناعادلانه، غیرقابل اعتماد یا توهین‌آمیز عمل کنند و در نتیجه آسیب‌هایی ایجاد کنند. لطفاً برای آگاهی از ریسک‌ها و محدودیت‌ها به [یادداشت شفافیت سرویس Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) مراجعه کنید.

رویکرد پیشنهادی برای کاهش این ریسک‌ها، گنجاندن یک سیستم ایمنی در معماری شماست که بتواند رفتارهای مضر را شناسایی و جلوگیری کند. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) یک لایه محافظتی مستقل فراهم می‌کند که قادر است محتوای مضر تولیدشده توسط کاربر یا هوش مصنوعی را در برنامه‌ها و سرویس‌ها شناسایی کند. Azure AI Content Safety شامل APIهای متن و تصویر است که به شما امکان می‌دهد محتوای مضر را شناسایی کنید. همچنین یک Content Safety Studio تعاملی داریم که به شما اجازه می‌دهد کد نمونه برای شناسایی محتوای مضر در حالت‌های مختلف را مشاهده و آزمایش کنید. [مستندات شروع سریع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) شما را در ارسال درخواست به این سرویس راهنمایی می‌کند.
یک جنبه‌ی دیگر که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندمدلی و چندحالته، منظور از عملکرد این است که سیستم همان‌طور که شما و کاربران‌تان انتظار دارید عمل کند، از جمله اینکه خروجی‌های مضر تولید نکند. ارزیابی عملکرد کلی برنامه با استفاده از [شاخص‌های کیفیت تولید و معیارهای ریسک و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) اهمیت دارد.

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه با استفاده از [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با داشتن یک مجموعه داده آزمایشی یا هدف مشخص، تولیدات برنامه هوش مصنوعی شما به صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی مورد سنجش قرار می‌گیرند. برای شروع ارزیابی سیستم با prompt flow sdk می‌توانید [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) را دنبال کنید. پس از اجرای یک ارزیابی، می‌توانید [نتایج را در Azure AI Studio مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت تابع و باید مطابق با [راهنمای علائم تجاری و برند مایکروسافت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) باشد.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید باعث سردرگمی یا القای حمایت مایکروسافت شود.
هرگونه استفاده از علائم تجاری یا لوگوهای شرکت‌های ثالث تابع سیاست‌های آن شرکت‌ها است.

## دریافت کمک

اگر در ساخت برنامه‌های هوش مصنوعی به مشکل برخوردید یا سوالی داشتید، به این انجمن بپیوندید:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

اگر بازخورد محصولی دارید یا هنگام ساخت با خطا مواجه شدید، به این انجمن مراجعه کنید:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**سلب مسئولیت**:
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. اگرچه ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطا یا نادقتی باشند. نسخه اصلی سند به زبان مادری آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه انسانی حرفه‌ای توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نداریم.