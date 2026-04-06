# Co-op Translator

_به‌راحتی ترجمه‌های محتوای آموزشی GitHub خود را به چند زبان و در طول تکامل پروژه خود، خودکار و نگهداری کنید._

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

### 🌐 پشتیبانی چندزبانه

#### پشتیبانی شده توسط [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](./README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ترجیح می‌دهید به صورت محلی کلون کنید؟**
>
> این مخزن شامل ترجمه‌های بیش از ۵۰ زبان است که اندازه دانلود را به طور قابل توجهی افزایش می‌دهد. برای کلون بدون ترجمه‌ها، از sparse checkout استفاده کنید:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> این به شما همه چیز مورد نیاز برای تکمیل دوره را با دانلود بسیار سریع‌تر می‌دهد.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## بررسی اجمالی

**Co-op Translator** به شما کمک می‌کند محتوای آموزشی GitHub خود را به‌سادگی به زبان‌های مختلف محلی‌سازی کنید.
هنگامی که فایل‌های Markdown، تصاویر یا دفترچه‌های یادداشت خود را به‌روزرسانی می‌کنید، ترجمه‌ها به‌صورت خودکار همگام‌سازی می‌شوند تا مطمئن شوید محتوای شما برای یادگیرندگان سراسر جهان دقیق و به‌روز باقی می‌ماند.

نمونه‌ای از نحوه سازماندهی محتوای ترجمه شده:

![Example](../../translated_images/fa/translation-ex.0c8aa6a7ee0aad2b.webp)

## مدیریت وضعیت ترجمه چگونه است

Co-op Translator محتوای ترجمه شده را به عنوان **آثار نرم‌افزاری نسخه‌بندی شده** مدیریت می‌کند،  
نه به صورت فایل‌های ایستا.

این ابزار وضعیت ترجمه‌های Markdown، تصاویر و دفترچه‌های یادداشت را با استفاده از **فراداده مخصوص زبان** پیگیری می‌کند.

این طراحی به Co-op Translator امکان می‌دهد:

- به‌طور مطمئن ترجمه‌های منسوخ را شناسایی کند
- رفتار یکسانی برای Markdown، تصاویر و دفترچه‌های یادداشت داشته باشد
- به‌طور ایمن در مخازن بزرگ، با چند زبان و سریع حرکت، مقیاس‌پذیر باشد

با مدل‌سازی ترجمه‌ها به عنوان آثار مدیریتی،  
گردش‌کارهای ترجمه به صورت طبیعی با مدیریت وابستگی‌ها و آثار نرم‌افزاری مدرن هماهنگ می‌شوند.

→ [چگونه وضعیت ترجمه مدیریت می‌شود](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## شروع سریع

```bash
# ایجاد و فعال‌سازی یک محیط مجازی (توصیه‌شده)
python -m venv .venv
# ویندوز
.venv\Scripts\activate
# مک‌اواس/لینوکس
source .venv/bin/activate
# نصب بسته
pip install co-op-translator
# ترجمه
translate -l "ko ja fr" -md
```

Docker:

```bash
# کشیدن تصویر عمومی از GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# اجرای با پوشه جاری نصب شده و فایل .env ارائه شده (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## پیکربندی حداقلی

1. اطمینان حاصل کنید که نسخه پایتون پشتیبانی شده دارید (فعلاً 3.10-3.12). در poetry (pyproject.toml) این به طور خودکار مدیریت می‌شود.
2. یک فایل `.env` بسازید با استفاده از الگو: [.env.template](../../.env.template)
3. یک ارائه‌دهنده LLM را پیکربندی کنید (Azure OpenAI یا OpenAI)
4. (اختیاری) برای ترجمه تصویر (`-img`)، Azure AI Vision را پیکربندی کنید
5. (اختیاری) می‌توانید چند مجموعه اعتبارنامه را با تکرار متغیرها با پسوندهایی مانند `_1`، `_2` و غیره پیکربندی کنید. همه متغیرها در یک مجموعه باید همان پسوند را داشته باشند.
6. (توصیه‌شده) هر ترجمه قبلی را برای جلوگیری از تداخل پاک کنید (مثلاً `translations/`)
7. (توصیه‌شده) یک بخش ترجمه به README خود اضافه کنید با استفاده از [الگوی زبان‌های README](./getting_started/README_languages_template.md)
8. مشاهده کنید: [راه‌اندازی Azure AI](./getting_started/set-up-azure-ai.md)

## نحوه استفاده

ترجمه تمام نوع‌های پشتیبانی شده:

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

فقط دفترچه یادداشت:

```bash
translate -l "zh" -nb
```

گزینه‌های بیشتر: [مرجع دستورات](./getting_started/command-reference.md)

## امکانات

- ترجمه خودکار برای Markdown، دفترچه‌های یادداشت و تصاویر
- نگهداری همگام ترجمه‌ها با تغییرات منبع
- کار به صورت محلی (CLI) یا در CI (GitHub Actions)
- استفاده از Azure OpenAI یا OpenAI؛ Azure AI Vision اختیاری برای تصاویر
- حفظ قالب‌بندی و ساختار Markdown

## مستندات

- [راهنمای خط فرمان](./getting_started/command-line-guide/command-line-guide.md)
- [راهنمای GitHub Actions (مخازن عمومی و اسرار استاندارد)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [راهنمای GitHub Actions (مخازن سازمان مایکروسافت و تنظیمات سازمانی)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [الگوی زبان‌های README](./getting_started/README_languages_template.md)
- [زبان‌های پشتیبانی شده](./getting_started/supported-languages.md)
- [همکاری](./CONTRIBUTING.md)
- [رفع اشکال](./getting_started/troubleshooting.md)

### راهنمای مخصوص مایکروسافت
> [!NOTE]
> فقط برای نگهدارندگان مخازن «برای مبتدیان» مایکروسافت.

- [به‌روزرسانی فهرست «دوره‌های دیگر» (فقط برای مخازن مبتدیان مایکروسافت)](./getting_started/update-other-courses.md)

## حمایت از ما و توسعه یادگیری جهانی

به ما در انقلاب نحوه اشتراک‌گذاری محتوای آموزشی در سراسر جهان بپیوندید! به [Co-op Translator](https://github.com/azure/co-op-translator) در GitHub یک ستاره بدهید و از ماموریت ما برای شکستن موانع زبانی در یادگیری و فناوری حمایت کنید. علاقه و مشارکت‌های شما تاثیر بسزایی دارد! مشارکت‌های کد و پیشنهاد امکانات همیشه استقبال می‌شود.

### محتوای آموزشی مایکروسافت را به زبان خود کاوش کنید

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

## ارائه‌های ویدئویی

👉 روی تصویر زیر کلیک کنید تا در یوتیوب مشاهده کنید.

- **Open at Microsoft**: معرفی کوتاه ۱۸ دقیقه‌ای و راهنمای سریع نحوه استفاده از Co-op Translator.

  [![Open at Microsoft](../../translated_images/fa/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## همکاری

این پروژه پذیرای مشارکت‌ها و پیشنهادات است. علاقه‌مند به همکاری در Azure Co-op Translator هستید؟ لطفاً راهنمای [CONTRIBUTING.md](./CONTRIBUTING.md) ما را جهت اطلاع از چگونگی کمک به در دسترس‌تر کردن Co-op Translator ببینید.

## مشارکت‌کنندگان
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## کد رفتاری

این پروژه کد رفتار متن‌باز مایکروسافت [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) را پذیرفته است.
برای اطلاعات بیشتر به [سوالات متداول کد رفتار](https://opensource.microsoft.com/codeofconduct/faq/) مراجعه کنید یا
با [opencode@microsoft.com](mailto:opencode@microsoft.com) جهت هر گونه سوال یا نظر اضافی تماس بگیرید.

## هوش مصنوعی مسئولانه

مایکروسافت متعهد است که به مشتریان خود کمک کند تا محصولات هوش مصنوعی ما را به طور مسئولانه استفاده کنند، تجربیات خود را به اشتراک بگذارند و از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی‌های تأثیر، شراکت‌های مبتنی بر اعتماد بسازند. بسیاری از این منابع را می‌توان در [https://aka.ms/RAI](https://aka.ms/RAI) یافت.
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول هوش مصنوعی ما شامل عدالت، قابلیت اطمینان و ایمنی، حریم خصوصی و امنیت، شمول، شفافیت و پاسخگویی استوار است.

مدل‌های بزرگ زبان طبیعی، تصویر و گفتار - مانند مدل‌های استفاده شده در این نمونه - ممکن است رفتاری داشته باشند که ناعادلانه، غیرقابل اعتماد یا توهین‌آمیز باشد، که در نتیجه می‌تواند آسیب رسان باشد. لطفاً برای اطلاع از ریسک‌ها و محدودیت‌ها به [یادداشت شفافیت سرویس Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) مراجعه کنید.

روش پیشنهادی برای کاهش این ریسک‌ها، افزودن یک سیستم ایمنی در معماری شما است که بتواند رفتارهای مضر را تشخیص داده و جلوگیری کند. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) لایه‌ای مستقل از حفاظت فراهم می‌کند که قادر به شناسایی محتواهای آسیب‌رسان تولید شده توسط کاربر و هوش مصنوعی در برنامه‌ها و سرویس‌ها است. Azure AI Content Safety شامل API های متن و تصویر است که به شما امکان تشخیص محتوای آسیب‌رسان را می‌دهند. همچنین ما یک استودیوی تعاملی Content Safety داریم که به شما امکان می‌دهد کد نمونه تشخیص محتوای مضر در حالت‌های مختلف را مشاهده، بررسی و آزمایش کنید. مستندات شروع سریع زیر [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) شما را برای ارسال درخواست‌ها به این سرویس هدایت می‌کند.

جنبه دیگری که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندحالتی و چندمدلی، عملکرد به معنی این است که سیستم همان‌طور که انتظار شما و کاربران است عمل کند، از جمله تولید نکردن خروجی‌های مضر. ارزیابی عملکرد کلی برنامه شما با استفاده از [معیارهای کیفیت تولید و ریسک و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) مهم است.

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه خود با استفاده از [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با داشتن مجموعه داده تست یا هدف، تولیدات برنامه هوش مصنوعی شما به صورت کمی با ارزیاب‌های داخلی یا ارزیاب‌های سفارشی انتخابی سنجیده می‌شود. برای شروع کار با prompt flow sdk جهت ارزیابی سیستم خود، می‌توانید از [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) استفاده کنید. پس از اجرای ارزیابی، می‌توانید [نتایج را در Azure AI Studio مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت باید مطابق با [راهنمای علامت تجاری و برند مایکروسافت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) باشد.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید موجب سردرگمی شده یا حمایت مایکروسافت را القا کند.
استفاده از علائم تجاری یا لوگوهای شخص ثالث نیز تابع سیاست‌های همان شخص ثالث است.

## دریافت کمک

اگر به مشکل برخورد کردید یا سوالی درباره ساخت برنامه‌های هوش مصنوعی داشتید، به اینجا بپیوندید:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر بازخورد محصول یا خطاهایی هنگام ساختن داشتید به اینجا مراجعه کنید:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از خدمت ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا عدم دقت‌هایی باشد. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->