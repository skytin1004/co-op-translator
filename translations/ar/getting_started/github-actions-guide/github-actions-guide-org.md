# استخدام إجراء Co-op Translator في GitHub (دليل المؤسسات)

**الجمهور المستهدف:** هذا الدليل مخصص **لموظفي Microsoft الداخليين** أو **الفرق التي لديها صلاحية الوصول إلى بيانات اعتماد تطبيق Co-op Translator GitHub الجاهز** أو يمكنهم إنشاء تطبيق GitHub مخصص خاص بهم.

قم بأتمتة ترجمة توثيق مستودعك بسهولة باستخدام إجراء Co-op Translator في GitHub. سيرشدك هذا الدليل خلال إعداد الإجراء لإنشاء طلبات سحب تلقائيًا مع الترجمات المحدثة كلما تم تغيير ملفات Markdown المصدرية أو الصور.

> [!IMPORTANT]
>
> **اختيار الدليل المناسب:**
>
> يشرح هذا الدليل الإعداد باستخدام **معرّف تطبيق GitHub ومفتاح خاص**. عادةً ما تحتاج إلى طريقة "دليل المؤسسات" هذه إذا: **`GITHUB_TOKEN` لديه صلاحيات محدودة:** إعدادات مؤسستك أو مستودعك تقيد الصلاحيات الافتراضية الممنوحة لـ `GITHUB_TOKEN` القياسي. تحديدًا، إذا لم يُسمح لـ `GITHUB_TOKEN` بالصلاحيات اللازمة للكتابة (مثل `contents: write` أو `pull-requests: write`)، فسيفشل سير العمل في [دليل الإعداد العام](./github-actions-guide-public.md) بسبب عدم كفاية الصلاحيات. استخدام تطبيق GitHub مخصص مع صلاحيات محددة يتجاوز هذا القيد.
>
> **إذا لم ينطبق عليك ما سبق:**
>
> إذا كان لدى `GITHUB_TOKEN` القياسي الصلاحيات الكافية في مستودعك (أي أنك لست مقيدًا بقيود تنظيمية)، يرجى استخدام **[دليل الإعداد العام باستخدام GITHUB_TOKEN](./github-actions-guide-public.md)**. الدليل العام لا يتطلب الحصول على معرفات تطبيق أو مفاتيح خاصة ويعتمد فقط على `GITHUB_TOKEN` القياسي وصلاحيات المستودع.

## المتطلبات الأساسية

قبل إعداد إجراء GitHub، تأكد من توفر بيانات اعتماد خدمة الذكاء الاصطناعي اللازمة لديك.

**1. مطلوب: بيانات اعتماد نموذج اللغة الذكي**
تحتاج إلى بيانات اعتماد لنموذج لغة مدعوم واحد على الأقل:

- **Azure OpenAI**: يتطلب نقطة النهاية، مفتاح API، أسماء النماذج/النشر، إصدار API.
- **OpenAI**: يتطلب مفتاح API، (اختياري: معرف المنظمة، عنوان قاعدة API، معرف النموذج).
- راجع [النماذج والخدمات المدعومة](../../../../README.md) للمزيد من التفاصيل.
- دليل الإعداد: [إعداد Azure OpenAI](../set-up-resources/set-up-azure-openai.md).

**2. اختياري: بيانات اعتماد الرؤية الحاسوبية (لترجمة الصور)**

- مطلوبة فقط إذا كنت بحاجة لترجمة النصوص داخل الصور.
- **Azure Computer Vision**: يتطلب نقطة النهاية ومفتاح الاشتراك.
- إذا لم يتم توفيرها، سيعمل الإجراء في [وضع Markdown فقط](../markdown-only-mode.md).
- دليل الإعداد: [إعداد Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md).

## الإعداد والتهيئة

اتبع الخطوات التالية لإعداد إجراء Co-op Translator في مستودعك:

### الخطوة 1: تثبيت وتكوين مصادقة تطبيق GitHub

يستخدم سير العمل مصادقة تطبيق GitHub للتفاعل الآمن مع مستودعك (مثل إنشاء طلبات السحب) نيابة عنك. اختر أحد الخيارين:

#### **الخيار أ: تثبيت تطبيق Co-op Translator الجاهز (للاستخدام الداخلي في Microsoft)**

1. انتقل إلى صفحة [تطبيق Co-op Translator في GitHub](https://github.com/apps/co-op-translator).

1. اختر **تثبيت** وحدد الحساب أو المؤسسة التي يوجد بها مستودعك المستهدف.

    ![تثبيت التطبيق](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ar.png)

1. اختر **تحديد مستودعات فقط** وحدد مستودعك المستهدف (مثلاً: `PhiCookBook`). اضغط **تثبيت**. قد يُطلب منك المصادقة.

    ![تثبيت التفويض](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ar.png)

1. **الحصول على بيانات اعتماد التطبيق (يتطلب إجراء داخلي):** للسماح لسير العمل بالمصادقة كتطبيق، تحتاج إلى معلومتين توفرهما لك فريق Co-op Translator:
  - **معرّف التطبيق (App ID):** المعرف الفريد لتطبيق Co-op Translator. معرّف التطبيق هو: `1164076`.
  - **المفتاح الخاص:** يجب أن تحصل على **المحتوى الكامل** لملف المفتاح الخاص `.pem` من جهة الاتصال المسؤولة عن الصيانة. **تعامل مع هذا المفتاح ككلمة مرور واحتفظ به بأمان.**

1. انتقل إلى الخطوة 2.

#### **الخيار ب: استخدام تطبيق GitHub مخصص خاص بك**

- إذا رغبت، يمكنك إنشاء وتكوين تطبيق GitHub خاص بك. تأكد من منحه صلاحية القراءة والكتابة للمحتوى وطلبات السحب. ستحتاج إلى معرّف التطبيق والمفتاح الخاص الذي تم إنشاؤه.

### الخطوة 2: إعداد أسرار المستودع

تحتاج إلى إضافة بيانات اعتماد تطبيق GitHub وبيانات اعتماد خدمة الذكاء الاصطناعي كأسرار مشفرة في إعدادات مستودعك.

1. انتقل إلى مستودع GitHub المستهدف (مثلاً: `PhiCookBook`).

1. اذهب إلى **الإعدادات** > **الأسرار والمتغيرات** > **الإجراءات**.

1. ضمن **أسرار المستودع**، اضغط **سر مستودع جديد** لكل سر من الأسرار المدرجة أدناه.

   ![تحديد إعداد الإجراء](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ar.png)

**الأسرار المطلوبة (لمصادقة تطبيق GitHub):**

| اسم السر              | الوصف                                              | مصدر القيمة                                     |
| :------------------- | :------------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | معرّف تطبيق GitHub (من الخطوة 1).                  | إعدادات تطبيق GitHub                            |
| `GH_APP_PRIVATE_KEY` | **المحتوى الكامل** لملف `.pem` الذي تم تحميله.     | ملف `.pem` (من الخطوة 1)                        |

**أسرار خدمة الذكاء الاصطناعي (أضف جميع ما ينطبق حسب متطلباتك):**

| اسم السر                             | الوصف                                         | مصدر القيمة                     |
| :---------------------------------- | :-------------------------------------------- | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | مفتاح خدمة Azure AI (الرؤية الحاسوبية)         | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`         | نقطة نهاية خدمة Azure AI (الرؤية الحاسوبية)    | Azure AI Foundry                |
| `AZURE_OPENAI_API_KEY`              | مفتاح خدمة Azure OpenAI                        | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`             | نقطة نهاية خدمة Azure OpenAI                   | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`           | اسم نموذج Azure OpenAI الخاص بك                | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | اسم نشر Azure OpenAI الخاص بك                  | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`          | إصدار API لـ Azure OpenAI                      | Azure AI Foundry                |
| `OPENAI_API_KEY`                    | مفتاح API لـ OpenAI                            | منصة OpenAI                     |
| `OPENAI_ORG_ID`                     | معرف منظمة OpenAI                              | منصة OpenAI                     |
| `OPENAI_CHAT_MODEL_ID`              | معرف نموذج OpenAI المحدد                       | منصة OpenAI                     |
| `OPENAI_BASE_URL`                   | عنوان قاعدة API مخصص لـ OpenAI                 | منصة OpenAI                     |

![إدخال اسم متغير البيئة](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ar.png)

### الخطوة 3: إنشاء ملف سير العمل

أخيرًا، أنشئ ملف YAML الذي يعرّف سير العمل المؤتمت.

1. في الدليل الجذري لمستودعك، أنشئ مجلد `.github/workflows/` إذا لم يكن موجودًا.

1. داخل `.github/workflows/`، أنشئ ملفًا باسم `co-op-translator.yml`.

1. الصق المحتوى التالي في ملف co-op-translator.yml.

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

4.  **تخصيص سير العمل:**
  - **[!IMPORTANT] اللغات المستهدفة:** في خطوة `Run Co-op Translator`، **يجب عليك مراجعة وتعديل قائمة رموز اللغات** داخل أمر `translate -l "..." -y` لتناسب متطلبات مشروعك. القائمة الموجودة كمثال (`ar de es...`) يجب استبدالها أو تعديلها.
  - **المشغل (`on:`):** المشغل الحالي يعمل عند كل دفع إلى `main`. للمستودعات الكبيرة، فكر في إضافة فلتر `paths:` (انظر المثال المعلق في ملف YAML) لتشغيل سير العمل فقط عند تغيير الملفات ذات الصلة (مثل التوثيق المصدري)، لتوفير دقائق تشغيل runner.
  - **تفاصيل طلب السحب:** يمكنك تخصيص `commit-message`، `title`، `body`، اسم الفرع، و`labels` في خطوة `Create Pull Request` إذا لزم الأمر.

## إدارة بيانات الاعتماد والتجديد

- **الأمان:** احفظ دائمًا بيانات الاعتماد الحساسة (مفاتيح API، المفاتيح الخاصة) كأسرار في GitHub Actions. لا تعرضها أبدًا في ملف سير العمل أو كود المستودع.
- **[!IMPORTANT] تجديد المفاتيح (لمستخدمي Microsoft الداخليين):** كن على علم بأن مفتاح Azure OpenAI المستخدم داخل Microsoft قد يكون له سياسة تجديد إلزامية (مثلاً: كل 5 أشهر). تأكد من تحديث أسرار GitHub المقابلة (`AZURE_OPENAI_...`) **قبل انتهاء صلاحيتها** لتجنب فشل سير العمل.

## تشغيل سير العمل

> [!WARNING]  
> **حد أقصى لمدة تشغيل runner المستضاف من GitHub:**  
> runners المستضافة من GitHub مثل `ubuntu-latest` لديها **حد أقصى لمدة التنفيذ وهو 6 ساعات**.  
> بالنسبة لمستودعات التوثيق الكبيرة، إذا تجاوزت عملية الترجمة 6 ساعات، سيتم إنهاء سير العمل تلقائيًا.  
> لتجنب ذلك، فكر في:  
> - استخدام **runner مستضاف ذاتيًا** (بدون حد زمني)  
> - تقليل عدد اللغات المستهدفة في كل تشغيل

بمجرد دمج ملف `co-op-translator.yml` في الفرع الرئيسي (أو الفرع المحدد في مشغل `on:`)، سيعمل سير العمل تلقائيًا عند دفع تغييرات إلى ذلك الفرع (ومطابقة فلتر `paths` إذا تم تكوينه).

إذا تم إنشاء أو تحديث ترجمات، سيقوم الإجراء تلقائيًا بإنشاء طلب سحب يحتوي على التغييرات، ليكون جاهزًا للمراجعة والدمج.

---

**إخلاء المسؤولية**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ينشأ عن استخدام هذه الترجمة.