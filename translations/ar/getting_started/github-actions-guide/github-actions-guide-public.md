# استخدام إجراء Co-op Translator في GitHub (إعداد عام)

**الجمهور المستهدف:** هذا الدليل موجه للمستخدمين في معظم المستودعات العامة أو الخاصة حيث تكون أذونات GitHub Actions القياسية كافية. يعتمد على الرمز المدمج `GITHUB_TOKEN`.

قم بأتمتة ترجمة توثيق مستودعك بسهولة باستخدام إجراء Co-op Translator في GitHub. يشرح هذا الدليل كيفية إعداد الإجراء لإنشاء طلبات سحب تلقائية مع الترجمات المحدثة كلما تغيرت ملفات Markdown المصدر أو الصور.

> [!IMPORTANT]
>
> **اختيار الدليل المناسب:**
>
> يشرح هذا الدليل **الإعداد الأبسط باستخدام الرمز القياسي `GITHUB_TOKEN`**. هذه الطريقة موصى بها لمعظم المستخدمين لأنها لا تتطلب إدارة مفاتيح خاصة لتطبيق GitHub.
>

## المتطلبات الأساسية

قبل ضبط إجراء GitHub، تأكد من توفر بيانات اعتماد خدمة الذكاء الاصطناعي المطلوبة لديك.

**1. مطلوب: بيانات اعتماد نموذج اللغة الذكي**
ستحتاج إلى بيانات اعتماد لنموذج لغة مدعوم واحد على الأقل:

- **Azure OpenAI**: يتطلب نقطة النهاية، مفتاح API، أسماء النماذج/النشر، إصدار API.
- **OpenAI**: يتطلب مفتاح API، (اختياري: معرف المنظمة، عنوان URL الأساسي، معرف النموذج).
- راجع [النماذج والخدمات المدعومة](../../../../README.md) للمزيد من التفاصيل.

**2. اختياري: بيانات اعتماد الرؤية الذكية (لترجمة الصور)**

- مطلوبة فقط إذا كنت بحاجة لترجمة النصوص داخل الصور.
- **Azure AI Vision**: يتطلب نقطة النهاية ومفتاح الاشتراك.
- إذا لم يتم توفيرها، سيعمل الإجراء في [وضع Markdown فقط](../markdown-only-mode.md).

## الإعداد والتهيئة

اتبع الخطوات التالية لضبط إجراء Co-op Translator في مستودعك باستخدام الرمز القياسي `GITHUB_TOKEN`.

### الخطوة 1: فهم المصادقة (باستخدام `GITHUB_TOKEN`)

يستخدم هذا المسار الرمز المدمج `GITHUB_TOKEN` الذي توفره GitHub Actions. يمنح هذا الرمز تلقائيًا الأذونات اللازمة للمسار للتفاعل مع مستودعك بناءً على الإعدادات التي تم ضبطها في **الخطوة 3**.

### الخطوة 2: ضبط أسرار المستودع

كل ما عليك هو إضافة **بيانات اعتماد خدمة الذكاء الاصطناعي** كأسرار مشفرة في إعدادات المستودع.

1.  انتقل إلى مستودع GitHub المستهدف.
2.  اذهب إلى **الإعدادات** > **الأسرار والمتغيرات** > **الإجراءات**.
3.  ضمن **أسرار المستودع**، اضغط على **سر مستودع جديد** لكل سر مطلوب من أسرار خدمات الذكاء الاصطناعي المدرجة أدناه.

    ![اختيار إعداد الإجراء](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ar.png) *(مرجع الصورة: يوضح مكان إضافة الأسرار)*

**أسرار خدمات الذكاء الاصطناعي المطلوبة (أضف كل ما ينطبق حسب متطلباتك):**

| اسم السر                         | الوصف                               | مصدر القيمة                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | مفتاح خدمة Azure AI (الرؤية الحاسوبية)  | منصة Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | نقطة نهاية خدمة Azure AI (الرؤية الحاسوبية) | منصة Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | مفتاح خدمة Azure OpenAI              | منصة Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | نقطة نهاية خدمة Azure OpenAI         | منصة Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | اسم نموذج Azure OpenAI              | منصة Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | اسم نشر Azure OpenAI                 | منصة Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | إصدار API لـ Azure OpenAI              | منصة Azure AI Foundry               |
| `OPENAI_API_KEY`                    | مفتاح API لـ OpenAI                        | منصة OpenAI              |
| `OPENAI_ORG_ID`                     | معرف منظمة OpenAI (اختياري)         | منصة OpenAI              |
| `OPENAI_CHAT_MODEL_ID`              | معرف نموذج OpenAI محدد (اختياري)       | منصة OpenAI              |
| `OPENAI_BASE_URL`                   | عنوان URL أساسي مخصص لـ OpenAI (اختياري)     | منصة OpenAI              |

### الخطوة 3: ضبط أذونات المسار

يحتاج إجراء GitHub إلى أذونات تمنحها عبر `GITHUB_TOKEN` لفحص الكود وإنشاء طلبات السحب.

1.  في مستودعك، اذهب إلى **الإعدادات** > **الإجراءات** > **عام**.
2.  مرر للأسفل إلى قسم **أذونات المسار**.
3.  اختر **أذونات القراءة والكتابة**. هذا يمنح `GITHUB_TOKEN` أذونات `contents: write` و `pull-requests: write` اللازمة لهذا المسار.
4.  تأكد من تفعيل خيار **السماح لـ GitHub Actions بإنشاء والموافقة على طلبات السحب**.
5.  اضغط على **حفظ**.

![إعداد الأذونات](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.ar.png)

### الخطوة 4: إنشاء ملف المسار

أخيرًا، أنشئ ملف YAML الذي يحدد المسار المؤتمت باستخدام `GITHUB_TOKEN`.

1.  في الدليل الجذري لمستودعك، أنشئ مجلد `.github/workflows/` إذا لم يكن موجودًا.
2.  داخل `.github/workflows/`، أنشئ ملفًا باسم `co-op-translator.yml`.
3.  الصق المحتوى التالي في ملف `co-op-translator.yml`.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **تخصيص المسار:**
  - **[!IMPORTANT] اللغات المستهدفة:** في خطوة `Run Co-op Translator`، **يجب عليك مراجعة وتعديل قائمة رموز اللغات** داخل أمر `translate -l "..." -y` لتناسب متطلبات مشروعك. القائمة الموجودة كمثال (`ar de es...`) يجب استبدالها أو تعديلها.
  - **المشغل (`on:`):** المشغل الحالي يعمل عند كل دفع إلى `main`. للمستودعات الكبيرة، يمكنك إضافة عامل تصفية `paths:` (انظر المثال المعلق في ملف YAML) لتشغيل المسار فقط عند تغيير الملفات ذات الصلة (مثل التوثيق المصدر)، مما يوفر وقت تشغيل الخادم.
  - **تفاصيل طلب السحب:** يمكنك تخصيص `commit-message`، `title`، `body`، اسم الفرع، و`labels` في خطوة `Create Pull Request` إذا رغبت.

## تشغيل المسار

> [!WARNING]  
> **حد وقت تشغيل الخادم المستضاف من GitHub:**  
> الخوادم المستضافة مثل `ubuntu-latest` لديها **حد أقصى لمدة التنفيذ وهو 6 ساعات**.  
> إذا تجاوزت عملية الترجمة هذا الحد في مستودعات التوثيق الكبيرة، سيتم إيقاف المسار تلقائيًا.  
> لتجنب ذلك، يمكنك:  
> - استخدام **خادم مستضاف ذاتيًا** (بدون حد زمني)  
> - تقليل عدد اللغات المستهدفة في كل تشغيل

بمجرد دمج ملف `co-op-translator.yml` في الفرع الرئيسي (أو الفرع المحدد في المشغل `on:`)، سيعمل المسار تلقائيًا عند دفع تغييرات إلى ذلك الفرع (ومطابقة عامل تصفية `paths` إذا تم ضبطه).

---

**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.