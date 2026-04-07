# Co-op Translator

_به‌راحتی ترجمه‌های محتوای آموزشی GitHub خود را در چندین زبان به‌طور خودکار مدیریت و بروزرسانی کنید، همان طور که پروژه شما پیشرفت می‌کند._

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

### 🌐 پشتیبانی چندزبانگی

#### پشتیبانی‌شده توسط [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](./README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ترجیح می‌دهید به‌صورت محلی کلون کنید؟**
>
> این مخزن بیش از ۵۰ ترجمه زبان را شامل می‌شود که اندازه دانلود را به‌طور قابل توجهی افزایش می‌دهد. برای کلون بدون ترجمه‌ها از sparse checkout استفاده کنید:
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
> این به شما همه چیز مورد نیاز برای اتمام دوره با سرعت دانلود بسیار بیشتر می‌دهد.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## مرور کلی

**Co-op Translator** به شما کمک می‌کند تا محتوای آموزشی GitHub خود را به‌سادگی به چند زبان مختلف بومی‌سازی کنید. هنگامی که فایل‌های Markdown، تصاویر یا دفترچه‌های یادداشت (notebooks) خود را به‌روزرسانی می‌کنید، ترجمه‌ها به‌طور خودکار همگام‌سازی می‌شوند و اطمینان حاصل می‌شود که محتوای شما برای یادگیرندگان در سراسر جهان دقیق و به‌روز باقی بماند.

نمونه‌ای از چگونه محتوای ترجمه شده سازماندهی شده است:

![Example](../../imgs/translation-ex.png)

## چگونه وضعیت ترجمه مدیریت می‌شود

Co-op Translator محتوای ترجمه شده را به‌صورت **آثار نرم‌افزاری نسخه‌بندی‌شده** مدیریت می‌کند،  
نه به صورت فایل‌های ایستا.

این ابزار با استفاده از **متاداده‌های محدود به زبان**، وضعیت ترجمه شده Markdown، تصاویر و نوت‌بوک‌ها را ردیابی می‌کند.

این طراحی به Co-op Translator اجازه می‌دهد تا:

- به‌طور قابل اعتماد ترجمه‌های منسوخ را تشخیص دهد
- برخورد یکنواخت با Markdown، تصاویر و دفترچه‌های یادداشت داشته باشد
- به‌صورت امن در مخازن چندزبانه بزرگ و سریع‌التحول مقیاس بپذیرد

با مدل‌سازی ترجمه‌ها به‌عنوان آرتیفکت‌های مدیریت شده،  
فرآیندهای کاری ترجمه به‌طور طبیعی با مدیریت وابستگی‌ها و آثار نرم‌افزاری مدرن هماهنگ می‌گردد.

→ [چگونگی مدیریت وضعیت ترجمه](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## شروع سریع

```bash
# ایجاد و فعال‌سازی یک محیط مجازی (توصیه می‌شود)
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

داکر:

```bash
# تصویر عمومی را از GHCR دریافت کنید
docker pull ghcr.io/azure/co-op-translator:latest
# اجرای با پوشه فعلی نصب شده و فایل .env ارائه شده (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## تنظیم حداقلی

1. اطمینان حاصل کنید که نسخه پایتون پشتیبانی شده را دارید (در حال حاضر 3.10-3.12). در poetry (pyproject.toml) این به‌طور خودکار مدیریت می‌شود.
2. یک فایل `.env` با استفاده از قالب: [.env.template](../../.env.template) ایجاد کنید
3. یک ارائه‌دهنده LLM را پیکربندی کنید (Azure OpenAI یا OpenAI)
4. (اختیاری) برای ترجمه تصویر (`-img`)، Azure AI Vision را پیکربندی کنید
5. (اختیاری) می‌توانید چند مجموعه اعتبارنامه با افزودن پسوندهایی مانند `_1`، `_2`، و غیره برای متغیرها پیکربندی کنید. همه متغیرها در یک مجموعه باید پسوند یکسانی داشته باشند.
۶. (توصیه شده) همه ترجمه‌های قبلی را برای جلوگیری از تداخل پاک کنید (مثلاً `translations/`)
7. (توصیه شده) یک بخش ترجمه به README خود اضافه کنید با استفاده از [قالب زبان‌های README](./getting_started/README_languages_template.md)
8. ببینید: [راه‌اندازی Azure AI](./getting_started/set-up-azure-ai.md)

## نحوه استفاده

ترجمه تمام انواع پشتیبانی‌شده:

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

فقط دفترچه‌های یادداشت:

```bash
translate -l "zh" -nb
```

پرچم‌های بیشتر: [مرجع دستور](./getting_started/command-reference.md)

## ویژگی‌ها

- ترجمه خودکار Markdown، دفترچه‌ها و تصاویر
- همگام‌سازی ترجمه‌ها با تغییرات منبع  
- کار به‌صورت محلی (CLI) یا در CI (GitHub Actions)
- استفاده از Azure OpenAI یا OpenAI؛ Azure AI Vision برای تصاویر به صورت اختیاری
- حفظ قالب‌بندی و ساختار Markdown

## مستندات

- [راهنمای خط فرمان](./getting_started/command-line-guide/command-line-guide.md)
- [راهنمای GitHub Actions (مخازن عمومی و اسرار استاندارد)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [راهنمای GitHub Actions (مخازن سازمانی مایکروسافت و تنظیمات سطح سازمان)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [قالب زبان‌های README](./getting_started/README_languages_template.md)
- [زبان‌های پشتیبانی‌شده](./getting_started/supported-languages.md)
- [همکاری در پروژه](./CONTRIBUTING.md)
- [عیب‌یابی](./getting_started/troubleshooting.md)

### راهنمای اختصاصی مایکروسافت
> [!NOTE]
> فقط برای نگهدارندگان مخازن «برای تازه‌کاران» مایکروسافت.

- [بروزرسانی فهرست «دوره‌های دیگر» (فقط برای مخازن MS Beginners)](./getting_started/update-other-courses.md)

## ما را حمایت کنید و یادگیری جهانی را رونق دهید

به ما در تحول نحوه به اشتراک‌گذاری محتوای آموزشی در سطح جهان بپیوندید! به [Co-op Translator](https://github.com/azure/co-op-translator) در GitHub ستاره دهید و از مأموریت ما برای شکستن موانع زبانی در یادگیری و فناوری حمایت کنید. علاقه و مشارکت‌های شما تأثیر بسزایی دارد! مشارکت در کد و پیشنهاد ویژگی‌ها همیشه خوش‌آمد است.

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

## ارائه‌های ویدیویی

👉 برای مشاهده در یوتیوب روی تصویر زیر کلیک کنید.

- **Open at Microsoft**: معرفی مختصر ۱۸ دقیقه‌ای و راهنمای سریع استفاده از Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## همکاری در پروژه

این پروژه پذیرای مشارکت‌ها و پیشنهادات است. علاقمند به همکاری در Azure Co-op Translator هستید؟ لطفاً راهنمای ما را در [CONTRIBUTING.md](./CONTRIBUTING.md) مطالعه کنید تا بدانید چگونه می‌توانید به قابل دسترس‌تر شدن Co-op Translator کمک کنید.

## مشارکت‌کنندگان
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## قوانین رفتار

این پروژه قوانین رفتار متن‌باز مایکروسافت را پذیرفته است [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
برای اطلاعات بیشتر به [پرسش‌های متداول قوانین رفتار](https://opensource.microsoft.com/codeofconduct/faq/) مراجعه کنید یا برای هر سوال یا نظر اضافی با [opencode@microsoft.com](mailto:opencode@microsoft.com) تماس بگیرید.

## هوش مصنوعی مسئولانه

مایکروسافت متعهد به کمک به مشتریان خود برای استفاده مسئولانه از محصولات هوش مصنوعی ما، به اشتراک‌گذاری تجربیاتمان و ساختن مشارکت‌های مبتنی بر اعتماد از طریق ابزارهایی مانند یادداشت‌های شفافیت و ارزیابی تأثیر است. بسیاری از این منابع را می‌توانید در [https://aka.ms/RAI](https://aka.ms/RAI) بیابید.
رویکرد مایکروسافت به هوش مصنوعی مسئولانه بر اصول هوش مصنوعی ما مبتنی است که شامل انصاف، قابلیت اطمینان و ایمنی، حفظ حریم خصوصی و امنیت، فراگیری، شفافیت و پاسخگویی است.

مدل‌های بزرگ زبان طبیعی، تصویر و گفتار - مانند نمونه‌های استفاده شده در این نمونه - ممکن است رفتارهایی ناعادلانه، غیرقابل اطمینان یا توهین‌آمیز داشته باشند که می‌تواند آسیب‌زا باشد. لطفاً برای آگاهی از ریسک‌ها و محدودیت‌ها به [یادداشت شفافیت سرویس Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) مراجعه کنید.

رویکرد پیشنهادی برای کاهش این ریسک‌ها، شامل کردن یک سیستم ایمنی در معماری شماست که بتواند رفتارهای مضر را شناسایی و جلوگیری کند. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) یک لایه محافظت مستقل فراهم می‌کند که قادر به کشف محتوای مضر تولید شده توسط کاربر و هوش مصنوعی در برنامه‌ها و خدمات است. Azure AI Content Safety شامل APIهای متنی و تصویری است که به شما امکان می‌دهد محتوای مضر را شناسایی کنید. همچنین یک استودیو تعاملی Content Safety داریم که به شما امکان می‌دهد نمونه کدهایی برای شناسایی محتوای مضر در حوزه‌های مختلف را مشاهده، بررسی و آزمایش کنید. مستندات شروع سریع [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) شما را در ارسال درخواست به سرویس راهنمایی می‌کند.

یکی دیگر از جنبه‌هایی که باید در نظر گرفته شود، عملکرد کلی برنامه است. در برنامه‌های چندرسانه‌ای و چندمدلی، عملکرد به معنای این است که سیستم همانطور که شما و کاربران انتظار دارید اجرا شود، از جمله عدم تولید خروجی‌های مضر. ارزیابی عملکرد کلی برنامه با استفاده از [معیارهای کیفیت تولید، ریسک و ایمنی](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) اهمیت دارد.

شما می‌توانید برنامه هوش مصنوعی خود را در محیط توسعه خود با استفاده از [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ارزیابی کنید. با یک مجموعه داده آزمایشی یا هدف تعیین شده، تولیدات هوش مصنوعی شما به صورت کمی با ارزیاب‌های داخلی یا سفارشی شما سنجیده می‌شود. برای شروع کار با sdk prompt flow برای ارزیابی سیستم خود، می‌توانید از [راهنمای شروع سریع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) پیروی کنید. پس از اجرای ارزیابی، می‌توانید [نتایج را در Azure AI Studio مشاهده کنید](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## علائم تجاری

این پروژه ممکن است شامل علائم تجاری یا لوگوهایی برای پروژه‌ها، محصولات یا خدمات باشد. استفاده مجاز از علائم تجاری یا لوگوهای مایکروسافت مشروط به و باید از [رهنمودهای علامت تجاری و برند مایکروسافت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) پیروی کند.
استفاده از علائم تجاری یا لوگوهای مایکروسافت در نسخه‌های تغییر یافته این پروژه نباید باعث سردرگمی شود یا دلالت بر حمایت مایکروسافت داشته باشد.
هر گونه استفاده از علائم تجاری یا لوگوهای طرف سوم مشمول سیاست‌های آن سازمان‌ها است.

## دریافت کمک

اگر به مشکلی برخوردید یا سوالی درباره ساخت برنامه‌های هوش مصنوعی داشتید، به موارد زیر بپیوندید:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

اگر بازخورد محصول دارید یا هنگام ساخت برنامه به خطا برخوردید، به موارد زیر مراجعه کنید:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است دارای خطا یا نواقص باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوتفاهم یا تفسیر نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->