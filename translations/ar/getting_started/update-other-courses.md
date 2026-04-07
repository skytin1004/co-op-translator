# تحديث قسم "الدورات الأخرى" (مستودعات Microsoft للمبتدئين)

يوضح هذا الدليل كيفية جعل قسم "الدورات الأخرى" يتزامن تلقائيًا باستخدام Co‑op Translator، وكيفية تحديث القالب العام لجميع المستودعات.

- ينطبق على: مستودعات Microsoft للمبتدئين فقط  
- يعمل مع: Co‑op Translator CLI و GitHub Actions  
- مصدر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## بدء سريع: تفعيل التزامن التلقائي في المستودع الخاص بك

أضف العلامات التالية حول قسم "الدورات الأخرى" في ملف README الخاص بك. سيقوم Co‑op Translator باستبدال كل شيء بين هذه العلامات في كل مرة يتم التشغيل فيها.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
في كل مرة يعمل فيها Co‑op Translator — عبر CLI (مثلاً، `translate -l "<language codes>"`) أو GitHub Actions — فإنه يقوم تلقائيًا بتحديث قسم "الدورات الأخرى" المحاط بهذه العلامات.

> [!NOTE]  
> إذا كان لديك قائمة حالية، فقط قم بتغليفها بنفس العلامات. في التشغيل التالي سيتم استبدالها بالمحتوى القياسي المحدث.

---

## كيفية تغيير المحتوى العام

إذا كنت تريد تحديث المحتوى القياسي الذي يظهر في جميع مستودعات المبتدئين:

1. حرر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. افتح طلب سحب (pull request) إلى مستودع Co-op Translator مع تغييراتك  
3. بعد دمج طلب السحب، سيتم تحديث نسخة Co‑op Translator  
4. في المرة القادمة التي يعمل فيها Co‑op Translator (CLI أو GitHub Action) في مستودع الهدف، سيقوم بمزامنة القسم المحدث تلقائيًا

هذا يضمن وجود مصدر واحد للحقيقة لمحتوى "الدورات الأخرى" عبر جميع مستودعات المبتدئين.

## أحجام المستودعات

يمكن أن تصبح المستودعات كبيرة بسبب عدد اللغات التي تُترجم إليها لمساعدة المستخدمين النهائيين في تقديم إرشادات حول كيفية استخدام clone - sparse لاستنساخ اللغات الضرورية فقط وليس المستودع بأكمله

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاستعانة بترجمة احترافية بشرية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->