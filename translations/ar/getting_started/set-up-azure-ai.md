# إعداد Azure AI لـ Co-op Translator (Azure OpneAI و Azure AI Vision)

يوضح هذا الدليل كيفية إعداد Azure OpenAI لترجمة اللغات و Azure Computer Vision لتحليل محتوى الصور (والذي يمكن استخدامه بعد ذلك للترجمة القائمة على الصور) ضمن Azure AI Foundry.

**المتطلبات الأساسية:**
- حساب Azure مع اشتراك نشط.
- أذونات كافية لإنشاء الموارد والنشر في اشتراك Azure الخاص بك.

## إنشاء مشروع Azure AI

ابدأ بإنشاء مشروع Azure AI، والذي يعمل كمكان مركزي لإدارة موارد الذكاء الاصطناعي الخاصة بك.

1. انتقل إلى [https://ai.azure.com](https://ai.azure.com) وقم بتسجيل الدخول باستخدام حساب Azure الخاص بك.

1. اختر **+Create** لإنشاء مشروع جديد.

1. قم بالمهام التالية:
   - أدخل **اسم المشروع** (مثلاً `CoopTranslator-Project`).
   - اختر **AI hub**  (مثلاً `CoopTranslator-Hub`) (أنشئ جديدًا إذا لزم الأمر).

1. انقر على "**Review and Create**" لإعداد مشروعك. سيتم توجيهك إلى صفحة نظرة عامة على مشروعك.

## إعداد Azure OpenAI لترجمة اللغات

داخل مشروعك، ستقوم بنشر نموذج Azure OpenAI ليعمل كواجهة خلفية لترجمة النصوص.

### انتقل إلى مشروعك

إذا لم تكن في المكان المناسب، افتح مشروعك الجديد (مثلاً `CoopTranslator-Project`) في Azure AI Foundry.

### نشر نموذج OpenAI

1. من القائمة اليسرى لمشروعك، تحت "My assets"، اختر "**Models + endpoints**".

1. اختر **+ Deploy model**.

1. اختر **Deploy Base Model**.

1. ستُعرض عليك قائمة بالنماذج المتاحة. قم بتصفية أو البحث عن نموذج GPT مناسب. نوصي بـ `gpt-4o`.

1. اختر النموذج المطلوب وانقر على **Confirm**.

1. اختر **Deploy**.

### إعداد Azure OpenAI

بمجرد النشر، يمكنك اختيار النشر من صفحة "**Models + endpoints**" للعثور على **رابط REST endpoint**، و**المفتاح**، و**اسم النشر**، و**اسم النموذج**، و**إصدار API**. ستحتاج هذه المعلومات لاستخدام نموذج الترجمة في تطبيقك.

> [!NOTE]
> يمكنك اختيار إصدارات API من صفحة [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) بناءً على متطلباتك. لاحظ أن **إصدار API** يختلف عن **إصدار النموذج** الظاهر في صفحة **Models + endpoints** في Azure AI Foundry.

## إعداد Azure Computer Vision لترجمة الصور

لتمكين ترجمة النصوص داخل الصور، تحتاج إلى الحصول على مفتاح API ونقطة نهاية Azure AI Service.

1. انتقل إلى مشروع Azure AI الخاص بك (مثلاً `CoopTranslator-Project`). تأكد من أنك في صفحة نظرة عامة على المشروع.

### إعداد خدمة Azure AI

ابحث عن مفتاح API ونقطة النهاية من خدمة Azure AI.

1. انتقل إلى مشروع Azure AI الخاص بك (مثلاً `CoopTranslator-Project`). تأكد من أنك في صفحة نظرة عامة على المشروع.

1. ابحث عن **مفتاح API** و**نقطة النهاية** من علامة تبويب خدمة Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

يتيح هذا الاتصال إمكانية استخدام موارد خدمة Azure AI المرتبطة (بما في ذلك تحليل الصور) في مشروع AI Foundry الخاص بك. يمكنك بعد ذلك استخدام هذا الاتصال في دفاتر الملاحظات أو التطبيقات الخاصة بك لاستخراج النص من الصور، والذي يمكن إرساله بعد ذلك إلى نموذج Azure OpenAI للترجمة.

## تجميع بيانات الاعتماد الخاصة بك

حتى الآن، يجب أن تكون قد جمعت ما يلي:

**لـ Azure OpenAI (ترجمة النصوص):**
- نقطة نهاية Azure OpenAI
- مفتاح API الخاص بـ Azure OpenAI
- اسم نموذج Azure OpenAI (مثلاً `gpt-4o`)
- اسم نشر Azure OpenAI (مثلاً `cooptranslator-gpt4o`)
- إصدار API الخاص بـ Azure OpenAI

**لـ Azure AI Services (استخراج نص الصورة عبر الرؤية):**
- نقطة نهاية خدمة Azure AI
- مفتاح API الخاص بخدمة Azure AI

### مثال: تكوين متغيرات البيئة (معاينة)

لاحقًا، عند بناء تطبيقك، من المحتمل أن تقوم بتكوينه باستخدام بيانات الاعتماد التي جمعتها. على سبيل المثال، قد تقوم بتعيينها كمتغيرات بيئة على النحو التالي:

```bash
# بيانات اعتماد خدمة Azure AI (مطلوبة لترجمة الصور)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # على سبيل المثال، 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# مجموعات احتياطية اختيارية: تكرار المتغيرات مع اللاحقة _1/_2 (نفس الفهرس لجميع المتغيرات في المجموعة)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# بيانات اعتماد Azure OpenAI (مطلوبة لترجمة النص)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # على سبيل المثال، 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # على سبيل المثال، gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # على سبيل المثال، cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # على سبيل المثال، 2024-12-01-preview

# مجموعات احتياطية اختيارية: تكرار مجموعة AZURE_OPENAI_* كاملة مع اللاحقة _1/_2 (نفس الفهرس لجميع المتغيرات)
```

---

### مزيد من القراءة

- [كيفية إنشاء مشروع في Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [كيفية إنشاء موارد Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [كيفية نشر نماذج OpenAI في Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار النسخة الأصلية من المستند بلغتها الأصلية المصدر الرسمي والمعتمد. بالنسبة للمعلومات الحساسة أو الحيوية، يُنصح بالترجمة المهنية التي يقوم بها بشر. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->