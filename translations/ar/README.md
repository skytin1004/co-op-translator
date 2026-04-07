# Co-op Translator

_قم بتسهيل أتمتة وصيانة الترجمات لمحتوى GitHub التعليمي الخاص بك عبر لغات متعددة مع تطور مشروعك._

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

#### مدعوم من [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](./README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **تفضل الاستنساخ محليًا؟**
>
> يتضمن هذا المستودع أكثر من 50 ترجمة لغة مما يزيد حجم التنزيل بشكل كبير. للاستنساخ بدون الترجمات، استخدم السحب الضيق:
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
> يمنحك هذا كل ما تحتاجه لإكمال الدورة بتنزيل أسرع بكثير.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## نظرة عامة

يساعدك **Co-op Translator** على تعريب محتوى GitHub التعليمي الخاص بك إلى لغات متعددة بسهولة.  
عند تحديث ملفات Markdown أو الصور أو دفاتر الملاحظات، تبقى الترجمات متزامنة تلقائيًا، مما يضمن بقاء المحتوى دقيقًا ومحدثًا للمتعلمين في جميع أنحاء العالم.

مثال على كيفية تنظيم المحتوى المترجم:

![Example](../../translated_images/ar/translation-ex.0c8aa6a7ee0aad2b.webp)

## كيفية إدارة حالة الترجمة

يدير Co-op Translator المحتوى المترجم كـ **مخلفات برمجية ذات إصدارات**،  
وليس كملفات ثابتة.

يتتبع الأداة حالة Markdown المترجمة، والصور، ودفاتر الملاحظات  
باستخدام **بيانات وصفية مخصصة للغة**.

يسمح هذا التصميم لـ Co-op Translator بـ:

- اكتشاف الترجمات القديمة بشكل موثوق
- التعامل مع Markdown، والصور، ودفاتر الملاحظات بشكل متناسق
- التوسع بأمان عبر مستودعات كبيرة وسريعة الحركة ومتعددة اللغات

من خلال نمذجة الترجمات كمخلفات مُدارة،  
تتوافق سير عمل الترجمة بشكل طبيعي مع ممارسات  
إدارة التبعية والمخلفات البرمجية الحديثة.

→ [كيف تتم إدارة حالة الترجمة](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## البداية السريعة

```bash
# إنشاء وتفعيل بيئة افتراضية (موصى به)
python -m venv .venv
# ويندوز
.venv\Scripts\activate
# ماك أو إس / لينكس
source .venv/bin/activate
# تثبيت الحزمة
pip install co-op-translator
# ترجم
translate -l "ko ja fr" -md
```

دُكر:

```bash
# سحب الصورة العامة من GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# التشغيل مع تركيب المجلد الحالي وتوفير ملف .env (باش/زِش)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## الإعداد الأدنى

1. تأكد من أن لديك نسخة Python مدعومة (حاليًا 3.10-3.12). يتم التعامل مع هذا تلقائيًا في poetry (pyproject.toml).
2. أنشئ ملف `.env` باستخدام القالب: [.env.template](../../.env.template)
3. قم بتكوين مزود LLM واحد (Azure OpenAI أو OpenAI)
4. (اختياري) لترجمة الصور (`-img`)، قم بتكوين Azure AI Vision
5. (اختياري) يمكنك تكوين مجموعات بيانات اعتماد متعددة عن طريق تكرار المتغيرات مع لاحقات مثل `_1`, `_2`، إلخ. يجب أن تشترك جميع المتغيرات في مجموعة واحدة بنفس اللاحقة.
6. (موصى به) قم بتنظيف أي ترجمات سابقة لتجنب التعارضات (مثل `translations/`)
7. (موصى به) أضف قسم ترجمة إلى ملف README الخاص بك باستخدام [قالب لغات README](./getting_started/README_languages_template.md)
8. انظر: [إعداد Azure AI](./getting_started/set-up-azure-ai.md)

## الاستخدام

ترجم جميع الأنواع المدعومة:

```bash
translate -l "ko ja"
```

فقط Markdown:

```bash
translate -l "de" -md
```

Markdown + صور:

```bash
translate -l "pt" -md -img
```

فقط دفاتر الملاحظات:

```bash
translate -l "zh" -nb
```

مزيد من الأعلام: [مرجع الأوامر](./getting_started/command-reference.md)

## الميزات

- الترجمة الآلية لملفات Markdown ودفاتر الملاحظات والصور
- الحفاظ على تزامن الترجمات مع تغييرات المصدر
- يعمل محليًا (CLI) أو في CI (GitHub Actions)
- يستخدم Azure OpenAI أو OpenAI؛ مع خيار Azure AI Vision للصور
- يحافظ على تنسيق وهيكل Markdown

## الوثائق

- [دليل سطر الأوامر](./getting_started/command-line-guide/command-line-guide.md)
- [دليل GitHub Actions (المستودعات العامة والأسرار القياسية)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [دليل GitHub Actions (مستودعات منظمة Microsoft وإعدادات على مستوى المنظمة)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [قالب لغات README](./getting_started/README_languages_template.md)
- [اللغات المدعومة](./getting_started/supported-languages.md)
- [المساهمة](./CONTRIBUTING.md)
- [استكشاف الأخطاء وإصلاحها](./getting_started/troubleshooting.md)

### دليل خاص بـ Microsoft
> [!NOTE]
> للمشرفين على مستودعات Microsoft "للمبتدئين" فقط.

- [تحديث قائمة "الدورات الأخرى" (لمستودعات MS Beginners فقط)](./getting_started/update-other-courses.md)

## دعمنا وتعزيز التعلم العالمي

انضم إلينا في إحداث ثورة في كيفية مشاركة المحتوى التعليمي عالميًا! امنح [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ على GitHub وادعم مهمتنا في كسر الحواجز اللغوية في التعلم والتقنية. يترك اهتمامك ومساهماتك أثرًا كبيرًا! مساهمات الشفرات المقترحة وطلبات الميزات مرحب بها دائمًا.

### استكشف المحتوى التعليمي لـ Microsoft بلغتك

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

👉 اضغط على الصورة أدناه للمشاهدة على يوتيوب.

- **Open at Microsoft**: مقدمة سريعة مدتها 18 دقيقة ودليل سريع حول كيفية استخدام Co-op Translator.

  [![Open at Microsoft](../../translated_images/ar/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## المساهمة

يرحب هذا المشروع بالمساهمات والاقتراحات. هل تهتم بالمساهمة في Azure Co-op Translator؟ يرجى الاطلاع على [CONTRIBUTING.md](./CONTRIBUTING.md) لإرشادات حول كيفية المساعدة في جعل Co-op Translator أكثر سهولة في الوصول.

## المساهمون
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## مدونة السلوك

لقد اعتمد هذا المشروع [مدونة السلوك المفتوح المصدر لمايكروسوفت](https://opensource.microsoft.com/codeofconduct/).
لمزيد من المعلومات، يرجى مراجعة [الأسئلة المتكررة حول مدونة السلوك](https://opensource.microsoft.com/codeofconduct/faq/) أو
التواصل عبر البريد الإلكتروني [opencode@microsoft.com](mailto:opencode@microsoft.com) لأي أسئلة أو تعليقات إضافية.

## الذكاء الاصطناعي المسؤول

تلتزم مايكروسوفت بمساعدة عملائنا على استخدام منتجات الذكاء الاصطناعي لدينا بمسؤولية، ومشاركة معارفنا، وبناء شراكات قائمة على الثقة من خلال أدوات مثل ملاحظات الشفافية وتقييمات التأثير. يمكن العثور على العديد من هذه الموارد في [https://aka.ms/RAI](https://aka.ms/RAI).
يرتكز نهج مايكروسوفت في الذكاء الاصطناعي المسؤول على مبادئ الذكاء الاصطناعي لدينا مثل العدالة، والموثوقية والسلامة، والخصوصية والأمان، والشمولية، والشفافية، والمساءلة.

يمكن أن تتصرف نماذج كبيرة النطاق في اللغة الطبيعية والصورة والكلام - مثل تلك المستخدمة في هذا المثال - بطرق قد تكون غير عادلة أو غير موثوقة أو مسيئة، مما قد يسبب أضراراً. يرجى الاطلاع على [ملاحظة الشفافية لخدمة Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) لمعرفة المخاطر والقيود.

النهج الموصى به للتقليل من هذه المخاطر هو تضمين نظام أمان في البنية التحتية الخاصة بك يمكنه اكتشاف ومنع السلوك الضار. توفر [سلامة المحتوى في Azure AI](https://learn.microsoft.com/azure/ai-services/content-safety/overview) طبقة حماية مستقلة، قادرة على اكتشاف المحتوى الضار الناتج عن المستخدم والذكاء الاصطناعي في التطبيقات والخدمات. تتضمن سلامة المحتوى في Azure AI واجهات برمجة التطبيقات للنص والصورة التي تتيح لك اكتشاف المواد الضارة. كما لدينا استوديو تفاعلي لسلامة المحتوى يسمح لك بعرض واستكشاف وتجربة كود عينة لاكتشاف المحتوى الضار عبر وسائط مختلفة. يوجهك مستند [الدليل السريع](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) خلال كيفية تقديم الطلبات إلى الخدمة.

جانب آخر يجب مراعاته هو أداء التطبيق بشكل عام. مع التطبيقات متعددة الوسائط والنماذج، نعني بالأداء أن النظام يعمل كما تتوقع أنت ومستخدموك، بما في ذلك عدم توليد مخرجات ضارة. من المهم تقييم أداء تطبيقك العام باستخدام [مقاييس جودة التوليد والمخاطر والسلامة](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

يمكنك تقييم تطبيق الذكاء الاصطناعي الخاص بك في بيئة التطوير باستخدام [مجموع أدوات prompt flow SDK](https://microsoft.github.io/promptflow/index.html). باستخدام بيانات اختبار أو هدف معين، يتم قياس التوليدات التطبيقية للذكاء الاصطناعي الكمي باستخدام مقيمين مدمجين أو مقيمين مخصصين من اختيارك. للبدء باستخدام مجموع أدوات prompt flow SDK لتقييم نظامك، يمكنك اتباع [دليل البدء السريع](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). بمجرد تنفيذ تقييم، يمكنك [عرض النتائج في Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## العلامات التجارية

قد يحتوي هذا المشروع على علامات تجارية أو شعارات لمشاريع أو منتجات أو خدمات. يخضع الاستخدام المصرح به لعلامات تجارية أو شعارات مايكروسوفت 
لـ و يجب أن يتبع 
[إرشادات العلامات التجارية والهوية لمايكروسوفت](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
يجب ألا يتسبب استخدام علامات تجارية أو شعارات مايكروسوفت في نسخ معدلة لهذا المشروع في إحداث ارتباك أو إيهام برعاية مايكروسوفت.
أي استخدام لعلامات تجارية أو شعارات لأطراف ثالثة يخضع لسياسات تلك الأطراف الثالثة.

## الحصول على المساعدة

إذا واجهت صعوبة أو كان لديك أي أسئلة حول بناء تطبيقات الذكاء الاصطناعي، انضم إلى:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

إذا كان لديك ملاحظات عن المنتج أو أخطاء أثناء البناء، قم بزيارة:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). على الرغم من أننا نسعى للدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحيوية، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->