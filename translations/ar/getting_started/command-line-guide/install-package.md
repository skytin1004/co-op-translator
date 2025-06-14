<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b6d85d887d2664539a438dae5d0dfa50",
  "translation_date": "2025-06-12T18:31:19+00:00",
  "source_file": "getting_started/command-line-guide/install-package.md",
  "language_code": "ar"
}
-->
# تثبيت حزمة Co-op Translator

أداة **Co-op Translator** هي أداة سطر أوامر (CLI) مصممة لمساعدتك في ترجمة جميع ملفات الماركدوان والصور في مشروعك إلى عدة لغات. سيرشدك هذا الدليل خلال كيفية إعداد المترجم وتشغيله لمختلف الحالات.

### إنشاء بيئة افتراضية

يمكنك إنشاء بيئة افتراضية باستخدام إما `pip` أو `Poetry`. اكتب أحد الأوامر التالية داخل الطرفية.

#### باستخدام pip

```bash
python -m venv .venv
```

#### باستخدام Poetry

```bash
poetry init
```

### تفعيل البيئة الافتراضية

بعد إنشاء البيئة الافتراضية، ستحتاج إلى تفعيلها. تختلف الخطوات حسب نظام التشغيل الخاص بك. اكتب الأمر التالي داخل الطرفية.

#### لكل من pip وPoetry

- ويندوز:

    ```bash
    .venv\Scripts\activate
    ```

- ماك/لينكس:

    ```bash
    source .venv/bin/activate
    ```

#### باستخدام Poetry

1. إذا أنشأت البيئة باستخدام Poetry، اكتب الأمر التالي داخل الطرفية لتفعيلها.

    ```bash
    poetry shell
    ```

### تثبيت الحزمة والحزم المطلوبة

بمجرد إعداد البيئة الافتراضية وتفعيلها، الخطوة التالية هي تثبيت التبعيات اللازمة.

### التثبيت السريع

التثبيت عبر Co-Op Translator باستخدام pip

```
pip install co-op-translator
```  
أو  

التثبيت عبر Poetry  
```
poetry add co-op-translator
```

#### باستخدام pip (من requirements.txt) إذا قمت باستنساخ هذا المستودع

![NOTE] يرجى عدم القيام بذلك إذا قمت بتثبيت co-op translator عبر التثبيت السريع.

1. إذا كنت تستخدم pip، اكتب الأمر التالي داخل الطرفية. سيقوم تلقائيًا بتثبيت الحزم المطلوبة المحددة في ملف `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

#### باستخدام Poetry (من pyproject.toml)

1. إذا كنت تستخدم Poetry، اكتب الأمر التالي داخل الطرفية. سيقوم تلقائيًا بتثبيت الحزم المطلوبة المحددة في ملف `pyproject.toml`:

    ```bash
    poetry install
    ```

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.