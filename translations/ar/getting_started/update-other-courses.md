# تحديث قسم "الدورات الأخرى" (مستودعات Microsoft Beginners)

تشرح هذه الإرشادات كيفية جعل قسم "الدورات الأخرى" يتم المزامنة التلقائية باستخدام Co‑op Translator، وكيفية تحديث القالب العالمي لكل المستودعات.

- ينطبق على: مستودعات Microsoft Beginners فقط
- يعمل مع: واجهة سطر الأوامر Co‑op Translator و GitHub Actions
- مصدر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## بداية سريعة: تمكين المزامنة التلقائية في المستودع الخاص بك

أضف العلامات التالية حول قسم "الدورات الأخرى" في ملف README الخاص بك. سيقوم Co‑op Translator باستبدال كل شيء بين هذه العلامات في كل تشغيل.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

في كل مرة يتم فيها تشغيل Co‑op Translator - سواء من خلال واجهة سطر الأوامر (مثلاً `translate -l "<language codes>"`) أو GitHub Actions - فإنه يقوم تلقائيًا بتحديث قسم "الدورات الأخرى" المحاط بهذه العلامات.

> [!NOTE]
> إذا كان لديك قائمة موجودة مسبقًا، فقط قم بتغليفها بنفس العلامات. التشغيل التالي سيستبدلها بالمحتوى القياسي الأحدث.

---

## كيفية تغيير المحتوى العالمي

إذا كنت تريد تحديث المحتوى المعياري الذي يظهر في جميع مستودعات Beginners:

1. حرر القالب: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. افتح طلب سحب (pull request) إلى مستودع Co-op Translator مع التغييرات الخاصة بك
3. بعد دمج طلب السحب، سيتم تحديث نسخة Co‑op Translator
4. في المرة التالية التي يتم فيها تشغيل Co‑op Translator (عبر CLI أو GitHub Action) في مستودع الهدف، سيتم مزامنة القسم المحدث تلقائيًا

هذا يضمن مصدرًا موحدًا للمحتوى الخاص بـ "الدورات الأخرى" عبر جميع مستودعات Beginners.

## أحجام المستودعات

يمكن أن تصبح المستودعات كبيرة بسبب عدد اللغات المترجمة لمساعدة المستخدمين النهائيين على تقديم إرشادات حول كيفية استخدام clone - sparse لاستنساخ اللغات الضرورية فقط وعدم استنساخ المستودع بأكمله

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
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->