<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:40:37+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "ar"
}
-->
# ترجمة مشروعك باستخدام Co-op Translator

أداة **Co-op Translator** هي أداة واجهة سطر أوامر (CLI) تساعدك على ترجمة ملفات الماركدوان والصور في مشروعك إلى عدة لغات. يشرح هذا القسم كيفية استخدام الأداة، ويغطي خيارات سطر الأوامر المختلفة، ويقدم أمثلة لحالات استخدام متعددة.

> [!NOTE]
> للحصول على قائمة كاملة بالأوامر ووصفها التفصيلي، يرجى الرجوع إلى [مرجع الأوامر](./command-reference.md).

---

## سيناريوهات وأوامر نموذجية

فيما يلي بعض حالات الاستخدام الشائعة لأداة **Co-op Translator**، مع الأوامر المناسبة لتشغيلها.

### 1. الترجمة الأساسية (لغة واحدة)

لترجمة مشروعك بالكامل (ملفات الماركدوان والصور) إلى لغة واحدة، مثل الكورية، استخدم الأمر التالي:

```bash
translate -l "ko"
```

سيقوم هذا الأمر بترجمة جميع ملفات الماركدوان والصور إلى الكورية، مع إضافة الترجمات الجديدة دون حذف أي ترجمات موجودة.

> [!TIP]
>
> هل تريد معرفة رموز اللغات المتوفرة في **Co-op Translator**؟ قم بزيارة قسم [اللغات المدعومة](https://github.com/Azure/co-op-translator#supported-languages) في المستودع لمزيد من التفاصيل.

#### مثال على Phi-3 CookBook

في **Phi-3 CookBook**، استخدمت الطريقة التالية لإضافة الترجمة الكورية لملفات الماركدوان والصور الموجودة.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. ترجمة عدة لغات

لترجمة مشروعك إلى عدة لغات (مثل الإسبانية، الفرنسية، والألمانية)، استخدم هذا الأمر:

```bash
translate -l "es fr de"
```

سيقوم هذا الأمر بترجمة المشروع إلى الإسبانية، الفرنسية، والألمانية، مع إضافة الترجمات الجديدة دون الكتابة فوق الترجمات الموجودة.

#### مثال على Phi-3 CookBook

في **Phi-3 CookBook**، بعد سحب أحدث التغييرات لتعكس آخر الالتزامات، استخدمت الطريقة التالية لترجمة ملفات الماركدوان والصور التي تمت إضافتها حديثًا.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> بالرغم من أنه يُنصح عادةً بترجمة لغة واحدة في كل مرة، في حالات مثل هذه حيث تحتاج إلى إضافة تغييرات محددة، يمكن أن يكون ترجمة عدة لغات دفعة واحدة أكثر كفاءة.

### 3. تحديث الترجمات (يحذف الترجمات الموجودة)

لتحديث الترجمات الموجودة (أي حذف الترجمات الحالية واستبدالها بأخرى جديدة)، استخدم الخيار `-u`. سيؤدي هذا إلى حذف كل الترجمات الموجودة للغات المحددة وإعادة ترجمتها.

```bash
translate -l "ko" -u
```

تحذير: سيطلب منك هذا الأمر التأكيد قبل المضي قدمًا في حذف الترجمات الحالية.

#### مثال على Phi-3 CookBook

في **Phi-3 CookBook**، استخدمت الطريقة التالية لتحديث جميع الملفات المترجمة إلى الإسبانية. أنصح باستخدام هذه الطريقة عندما يكون هناك تغييرات كبيرة في المحتوى الأصلي عبر عدة مستندات ماركدوان. إذا كان هناك عدد قليل فقط من ملفات الماركدوان المترجمة لتحديثها، فمن الأفضل حذف تلك الملفات يدويًا ثم استخدام طريقة `-a` لإضافة الترجمات المحدثة.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. ترجمة الصور فقط

لترجمة ملفات الصور فقط في مشروعك، استخدم الخيار `-img`:

```bash
translate -l "ko" -img
```

سيقوم هذا الأمر بترجمة الصور فقط إلى الكورية، دون التأثير على ملفات الماركدوان.

### 6. ترجمة ملفات الماركدوان فقط

لترجمة ملفات الماركدوان فقط في مشروعك، استخدم الخيار `-md`:

```bash
translate -l "ko" -md
```

### 7. التحقق من الأخطاء في الملفات المترجمة

إذا أردت فحص الملفات المترجمة بحثًا عن أخطاء وإعادة محاولة الترجمة إذا لزم الأمر، استخدم الخيار `-chk`:

```bash
translate -l "ko" -chk
```

سيقوم هذا الأمر بمسح ملفات الماركدوان المترجمة وإعادة محاولة الترجمة لأي ملفات بها أخطاء.

#### مثال على Phi-3 CookBook

في **Phi-3 CookBook**، استخدمت الطريقة التالية للتحقق من أخطاء الترجمة في الملفات الكورية وإعادة محاولة الترجمة تلقائيًا لأي ملفات تم اكتشاف مشاكل بها.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

هذا الخيار يتحقق من أخطاء الترجمة. حاليًا، إذا كان الفرق في فواصل الأسطر بين الملف الأصلي والمترجم أكثر من ستة، يتم اعتبار الملف به خطأ في الترجمة. أخطط لتحسين هذا المعيار ليكون أكثر مرونة في المستقبل.

على سبيل المثال، هذه الطريقة مفيدة لاكتشاف الأجزاء المفقودة أو الترجمات التالفة، وستقوم تلقائيًا بإعادة محاولة الترجمة لتلك الملفات.

ومع ذلك، إذا كنت تعرف مسبقًا الملفات التي بها مشاكل، فمن الأفضل حذف تلك الملفات يدويًا ثم استخدام خيار `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d`:

```bash
translate -l "ko" -d
```

سيشغل هذا الأمر الترجمة في وضع التصحيح، مما يوفر معلومات تسجيل إضافية تساعدك في تحديد المشكلات أثناء عملية الترجمة.

#### مثال على Phi-3 CookBook

في **Phi-3 CookBook**، واجهت مشكلة حيث تسببت الترجمات التي تحتوي على روابط كثيرة في ملفات الماركدوان في أخطاء تنسيق، مثل الترجمات المعطوبة وتجاهل فواصل الأسطر. لتشخيص هذه المشكلة، استخدمت الخيار `-d` لرؤية كيفية عمل عملية الترجمة.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. ترجمة جميع اللغات

إذا أردت ترجمة المشروع إلى كل اللغات المدعومة، استخدم الكلمة المفتاحية all.

> [!WARNING]
> ترجمة جميع اللغات دفعة واحدة قد تستغرق وقتًا طويلًا حسب حجم المشروع. على سبيل المثال، استغرقت ترجمة **Phi-3 CookBook** إلى الإسبانية حوالي ساعتين. وبالنظر إلى الحجم، ليس من العملي لشخص واحد التعامل مع 20 لغة. يُنصح بتقسيم العمل بين عدة مساهمين، كل منهم يدير لغة أو لغتين، وتحديث الترجمات تدريجيًا.

```bash
translate -l "all"
```

سيقوم هذا الأمر بترجمة المشروع إلى كل اللغات المتاحة. إذا قررت المتابعة، قد تستغرق الترجمة وقتًا طويلًا حسب حجم المشروع.

> [!TIP]
>
> ### حذف الملفات المترجمة يدويًا (اختياري)
> يتم الآن اكتشاف الملفات المترجمة وتنظيفها تلقائيًا عند تحديث ملف المصدر.
>
> مع ذلك، إذا أردت تحديث ترجمة يدويًا - على سبيل المثال، لإعادة ترجمة ملف معين أو تجاوز سلوك النظام - يمكنك استخدام الأمر التالي لحذف كل نسخ الملف عبر مجلدات اللغات.
>
> ### على ويندوز:
> 1. **باستخدام موجه الأوامر (Command Prompt)**:
>    - افتح موجه الأوامر.
>    - انتقل إلى المجلد الذي توجد فيه الملفات باستخدام أمر `cd`.
>    - استخدم الأمر التالي لحذف الملفات:
>      ```
>      del /s *filename*
>      ```
>      خيار `/s` يبحث أيضًا في المجلدات الفرعية.
>
> 2. **باستخدام PowerShell**:
>    - افتح PowerShell.
>    - نفذ هذا الأمر:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      استبدل `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` بالأمر المناسب.
>
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     استبدل `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` بالأمر لتحديث أحدث تغييرات الملفات.

**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الحساسة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.