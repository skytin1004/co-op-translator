# Co-op Translator

_سهّل عملية أتمتة وصيانة الترجمات لمحتوى GitHub التعليمي الخاص بك عبر عدة لغات مع تطور مشروعك._

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

### 🌐 دعم متعدد اللغات

#### مدعوم بواسطة [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **تفضل استنساخ المستودع محليًا؟**
>
> يشمل هذا المستودع أكثر من 50 ترجمة للغات مما يزيد بشكل كبير من حجم التنزيل. لاستنساخ المستودع بدون الترجمات، استخدم checkout الجزئي:
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
> هذا يمنحك كل ما تحتاجه لإتمام الدورة مع تنزيل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## نظرة عامة

يساعدك **Co-op Translator** على تعريب محتوى GitHub التعليمي الخاص بك إلى عدة لغات بسهولة.  
عندما تقوم بتحديث ملفات Markdown أو الصور أو دفاتر الملاحظات، تبقى الترجمات متزامنة تلقائيًا، مما يضمن بقاء محتواك دقيقًا ومحدثًا للمتعلمين في جميع أنحاء العالم.

مثال على كيفية تنظيم المحتوى المترجم:

![Example](../../imgs/translation-ex.png)

## كيف يتم إدارة حالة الترجمة

يدير Co-op Translator المحتوى المترجم كـ **قطع برامج ذات إصدارات**،  
وليس كملفات ثابتة.

يتتبع الأداة حالة Markdown المترجم، الصور، ودفاتر الملاحظات  
باستخدام **بيانات وصفية خاصة باللغات**.

هذا التصميم يسمح لـ Co-op Translator بـ:

- اكتشاف الترجمات القديمة بشكل موثوق  
- معاملة Markdown، الصور، ودفاتر الملاحظات بشكل متسق  
- التوسع بأمان عبر مستودعات ضخمة متعددة اللغات وسريعة الحركة

من خلال نمذجة الترجمات كقطع مدارّة،  
تتماشى سير العمل الخاص بالترجمة بشكل طبيعي مع  
ممارسات إدارة الاعتمادات والقطع البرمجية الحديثة.

→ [كيف يتم إدارة حالة الترجمة](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## بداية سريعة

```bash
# إنشاء وتفعيل بيئة افتراضية (موصى به)
python -m venv .venv
# ويندوز
.venv\Scripts\activate
# ماك أو إس/لينكس
source .venv/bin/activate
# تثبيت الحزمة
pip install co-op-translator
# ترجم
translate -l "ko ja fr" -md
```

دوكر:

```bash
# سحب الصورة العامة من GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# التشغيل مع تثبيت المجلد الحالي وتوفير ملف .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## إعدادات أساسية

1. تأكد من وجود إصدار بايثون مدعوم (حاليًا 3.10-3.12). في poetry (pyproject.toml) يتم التعامل مع هذا تلقائيًا.  
2. أنشئ ملف `.env` باستخدام النموذج: [.env.template](../../.env.template)  
3. قم بتكوين مزود LLM واحد (Azure OpenAI أو OpenAI)  
4. (اختياري) لترجمة الصور (`-img`)، قم بتكوين Azure AI Vision  
5. (اختياري) يمكنك تكوين مجموعات اعتماد متعددة عن طريق تكرار المتغيرات مع لاحقة مثل `_1`، `_2`، إلخ. يجب أن تشترك جميع المتغيرات ضمن مجموعة في نفس اللاحقة.  
6. (موصى به) نظف أية ترجمات سابقة لتجنب التعارضات (مثلاً، `translations/`)  
7. (موصى به) أضف قسم الترجمة إلى README الخاص بك باستخدام [نموذج لغات README](./getting_started/README_languages_template.md)  
8. انظر: [إعداد Azure AI](./getting_started/set-up-azure-ai.md)

## الاستخدام

ترجم جميع الأنواع المدعومة:

```bash
translate -l "ko ja"
```

Markdown فقط:

```bash
translate -l "de" -md
```

Markdown + صور:

```bash
translate -l "pt" -md -img
```

دفاتر ملاحظات فقط:

```bash
translate -l "zh" -nb
```

المزيد من الأعلام: [مرجع الأوامر](./getting_started/command-reference.md)

## الميزات

- الترجمة الآلية لـ Markdown، دفاتر الملاحظات، والصور  
- الحفاظ على تزامن الترجمات مع تغييرات المصدر  
- يعمل محليًا (CLI) أو في تنفيذات CI (GitHub Actions)  
- يستخدم Azure OpenAI أو OpenAI؛ Azure AI Vision اختياري للصور  
- يحافظ على تنسيق وهيكل Markdown

## الوثائق

- [دليل سطر الأوامر](./getting_started/command-line-guide/command-line-guide.md)  
- [دليل GitHub Actions (للمستودعات العامة والأسرار القياسية)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [دليل GitHub Actions (لمستودعات منظمة Microsoft وإعدادات على مستوى المنظمة)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [نموذج لغات README](./getting_started/README_languages_template.md)  
- [اللغات المدعومة](./getting_started/supported-languages.md)  
- [المساهمة](./CONTRIBUTING.md)  
- [استكشاف الأخطاء وإصلاحها](./getting_started/troubleshooting.md)

### دليل خاص بـ Microsoft
> [!NOTE]
> موجه فقط لمشرفي مستودعات Microsoft التعليمية "للمبتدئين".

- [تحديث قائمة "الدورات الأخرى" (لمستودعات MS Beginners فقط)](./getting_started/update-other-courses.md)

## ادعمنا وعزز التعليم العالمي

انضم إلينا في ثورة كيفية مشاركة المحتوى التعليمي عالميًا! امنح [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ على GitHub وادعم مهمتنا لكسر الحواجز اللغوية في التعلم والتكنولوجيا. مساهماتك واهتمامك تحدث فرقًا كبيرًا! مساهمات الكود واقتراحات الميزات دائماً مرحب بها.

### استكشف محتوى Microsoft التعليمي بلغتك

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

## عروض الفيديو

👉 انقر على الصورة أدناه للمشاهدة على يوتيوب.

- **Open at Microsoft**: مقدمة سريعة مدتها 18 دقيقة ودليل سريع عن كيفية استخدام Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## المساهمة

يرحب هذا المشروع بالمساهمات والاقتراحات. هل ترغب في المساهمة في Azure Co-op Translator؟ يرجى مراجعة [CONTRIBUTING.md](./CONTRIBUTING.md) لدينا للحصول على إرشادات حول كيفية المساعدة في جعل Co-op Translator أكثر سهولة في الوصول.

## المساهمون
[![مساهمو co-op-translator](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## قواعد السلوك

لقد تبنى هذا المشروع [قواعد السلوك مفتوحة المصدر من مايكروسوفت](https://opensource.microsoft.com/codeofconduct/).
لمزيد من المعلومات، راجع [الأسئلة الشائعة حول قواعد السلوك](https://opensource.microsoft.com/codeofconduct/faq/) أو
تواصل مع [opencode@microsoft.com](mailto:opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## الذكاء الاصطناعي المسؤول

تلتزم مايكروسوفت بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بمسؤولية، ومشاركة ما تعلمناه، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات الأثر. يمكن العثور على العديد من هذه الموارد على [https://aka.ms/RAI](https://aka.ms/RAI).
تستند مقاربة مايكروسوفت للذكاء الاصطناعي المسؤول إلى مبادئ الذكاء الاصطناعي لدينا المتعلقة بالإنصاف، والموثوقية والسلامة، والخصوصية والأمان، والشمولية، والشفافية، والمساءلة.

يمكن أن تتصرف نماذج اللغة الطبيعية والصورة والصوت واسعة النطاق - مثل تلك المستخدمة في هذا المثال - بطرق غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضرارًا. يرجى الرجوع إلى [مذكرة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) لتكون على علم بالمخاطر والقيود.

النهج الموصى به لتخفيف هذه المخاطر هو تضمين نظام أمان في بنيتك يمكنه اكتشاف ومنع السلوك الضار. يوفر [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الذي يولده المستخدم أو الذكاء الاصطناعي في التطبيقات والخدمات. تتضمن خدمة Azure AI Content Safety واجهات برمجة تطبيقات للنص والصورة تسمح لك بالكشف عن المواد الضارة. كما لدينا استوديو تفاعلي لـ Content Safety يسمح لك بعرض واستكشاف وتجربة رمز برمجي نموذجي لاكتشاف المحتوى الضار عبر أوضاع مختلفة. يوجهك [وثائق البدء السريع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) التالية للقيام بالطلبات إلى الخدمة.

هناك جانب آخر يجب أخذه في الاعتبار وهو أداء التطبيق العام. مع التطبيقات متعددة الأوضاع والنماذج، نعتبر الأداء يعني أن النظام يعمل كما تتوقع أنت والمستخدمون، بما في ذلك عدم إنتاج مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [مقاييس جودة التوليد والمخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير الخاصة بك باستخدام [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). سواء كان لديك مجموعة بيانات اختبار أو هدف معين، يتم قياس توليدات تطبيق الذكاء الاصطناعي التوليدي الخاص بك كميًا باستخدام مقيمين مدمجين أو مقيمين مخصصين تختارهم. للبدء باستخدام prompt flow sdk لتقييم نظامك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تشغيل التقييم، يمكنك [عرض النتائج في Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. يخضع الاستخدام المصرح به لعلامات مايكروسوفت التجارية أو شعاراتها إلى
ويجب أن يتبع [إرشادات العلامات التجارية والعلامات التجارية لمايكروسوفت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
لا يجب أن يسبب استخدام علامات مايكروسوفت التجارية أو شعاراتها في نسخ معدلة من هذا المشروع لبسًا أو يوحي برعاية مايكروسوفت.
أي استخدام لعلامات تجارية أو شعارات لأطراف ثالثة يخضع لسياسات تلك الجهات.

## الحصول على المساعدة

إذا واجهتك مشكلة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

إذا كان لديك ملاحظات على المنتج أو أخطاء أثناء البناء قم بزيارة:

[![منتدى مطوري Microsoft Foundry](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى جاهدين لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاستعانة بالترجمة البشرية المحترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->