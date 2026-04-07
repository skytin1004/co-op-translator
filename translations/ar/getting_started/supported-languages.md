# اللغات المدعومة

تدرج الجدول أدناه اللغات المدعومة حالياً بواسطة **Co-op Translator**. يشمل رموز اللغات، وأسماء اللغات، وأي مشاكل معروفة مرتبطة بكل لغة. إذا كنت ترغب في إضافة دعم للغة جديدة، يرجى إضافة رمز اللغة المقابل، واسم اللغة، والخط المناسب في ملف `font_language_mappings.yml` الموجود في `src/co_op_translator/fonts/` وتقديم طلب سحب بعد الاختبار.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | الإنجليزية           | NotoSans-Medium.ttf               | No          | No           |
| fr            | الفرنسية             | NotoSans-Medium.ttf               | No          | No           |
| es            | الإسبانية            | NotoSans-Medium.ttf               | No          | No           |
| de            | الألمانية            | NotoSans-Medium.ttf               | No          | No           |
| ru            | الروسية              | NotoSans-Medium.ttf               | No          | No           |
| ar            | العربية              | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | الفارسية             | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | الأردية              | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh-CN         | الصينية (مبسطة)      | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-MO         | الصينية (تقليدية، ماكاو) | NotoSansCJK-Medium.ttc       | No          | No           |
| zh-HK         | الصينية (تقليدية، هونغ كونغ) | NotoSansCJK-Medium.ttc   | No          | No           |
| zh-TW         | الصينية (تقليدية، تايوان) | NotoSansCJK-Medium.ttc      | No          | No           |
| ja            | اليابانية            | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | الكورية              | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | الهندية              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | البنغالية            | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | الماراثية            | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | النيبالية            | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | البنجابية (جورموخية)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt-PT         | البرتغالية (البرتغال)| NotoSans-Medium.ttf               | No          | No           |
| pt-BR         | البرتغالية (البرازيل) | NotoSans-Medium.ttf               | No          | No           |
| it            | الإيطالية            | NotoSans-Medium.ttf               | No          | No           |
| lt            | الليتوانية           | NotoSans-Medium.ttf               | No          | No           |
| pl            | البولندية            | NotoSans-Medium.ttf               | No          | No           |
| tr            | التركية              | NotoSans-Medium.ttf               | No          | No           |
| el            | اليونانية            | NotoSans-Medium.ttf               | No          | No           |
| th            | التايلاندية          | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | السويدية             | NotoSans-Medium.ttf               | No          | No           |
| da            | الدنماركية           | NotoSans-Medium.ttf               | No          | No           |
| no            | النرويجية            | NotoSans-Medium.ttf               | No          | No           |
| fi            | الفنلندية            | NotoSans-Medium.ttf               | No          | No           |
| nl            | الهولندية            | NotoSans-Medium.ttf               | No          | No           |
| he            | العبرية              | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | الفيتنامية           | NotoSans-Medium.ttf               | No          | No           |
| id            | الإندونيسية          | NotoSans-Medium.ttf               | No          | No           |
| ms            | الملايوية            | NotoSans-Medium.ttf               | No          | No           |
| tl            | التاغالوغية (الفلبينية) | NotoSans-Medium.ttf           | No          | No           |
| sw            | السواحلية            | NotoSans-Medium.ttf               | No          | No           |
| hu            | الهنغارية            | NotoSans-Medium.ttf               | No          | No           |
| cs            | التشيكية             | NotoSans-Medium.ttf               | No          | No           |
| sk            | السلوفاكية           | NotoSans-Medium.ttf               | No          | No           |
| ro            | الرومانية            | NotoSans-Medium.ttf               | No          | No           |
| bg            | البلغارية            | NotoSans-Medium.ttf               | No          | No           |
| sr            | الصربية (السيريلية)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | الكرواتية            | NotoSans-Medium.ttf               | No          | No           |
| sl            | السلوفينية           | NotoSans-Medium.ttf               | No          | No           |
| uk            | الأوكرانية           | NotoSans-Medium.ttf               | No          | No           |
| my            | البورمية (ميانمار)   | NotoSansMyanmar-Medium.ttf        | No          | No           |
| ta            | التاميلية            | NotoSansTamil-Medium.ttf          | No          | No           |
| et            | الإستونية            | NotoSans-Medium.ttf               | No          | No           |
| pcm           | النيجيرية بيدجين     | NotoSans-Medium.ttf               | No          | No           |
| te            | التيلجو              | NotoSans-Medium.ttf               | No          | No           |
| ml            | المالايالامية         | NotoSans-Medium.ttf               | No          | No           |
| kn            | الكنادية             | NotoSans-Medium.ttf               | No          | No           |
| km            | الخميرية             | NotoSansKhmer-Medium.ttf          | No          | No           |

## إضافة لغة جديدة

مهتم بإضافة لغة جديدة؟ يرجى اتباع دليل المساهمة:

- انظر المساهمة: [قم بالمساهمة بلغة جديدة](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الحساسة أو الهامة، يُنصح بالاعتماد على ترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->