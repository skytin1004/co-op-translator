# עדכון סעיף "קורסים אחרים" (מאגרי Microsoft Beginners)

מדריך זה מסביר כיצד לגרום לסעיף "קורסים אחרים" להתעדכן באופן אוטומטי באמצעות Co‑op Translator, וכיצד לעדכן את התבנית הגלובלית לכל המאגר.

- חל על: מאגרי Microsoft Beginners בלבד
- עובד עם: Co‑op Translator CLI ו-GitHub Actions
- מקור התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## התחלה מהירה: הפעל סינכרון אוטומטי במאגר שלך

הוסף את הסימנים הבאים סביב סעיף "קורסים אחרים" ב-README שלך. Co‑op Translator יחליף את כל מה שבין הסימנים האלה בכל הפעלה.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

בכל פעם ש-Co‑op Translator פועל — דרך CLI (למשל, `translate -l "<language codes>"`) או GitHub Actions — הוא מעדכן אוטומטית את סעיף "קורסים אחרים" שכלול בין סימנים אלו.

> [!NOTE]
> אם יש לך רשימה קיימת, פשוט עטוף אותה באותם סימנים. ההפעלה הבאה תחליף אותה בתוכן הסטנדרטי העדכני ביותר.

---

## כיצד לשנות את התוכן הגלובלי

אם ברצונך לעדכן את התוכן הסטנדרטי המופיע בכל מאגרי Beginners:

1. ערוך את התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. פתח pull request למאגר Co-op Translator עם השינויים שלך
3. לאחר שה-PR מאוחזר, גרסת Co‑op Translator תעודכן
4. בפעם הבאה ש-Co‑op Translator ירוץ (ב-CLI או GitHub Action) במאגר היעד, הסעיף המעודכן יסונכרן אוטומטית

כך מובטח מקור אחיד של אמת לתוכן "קורסים אחרים" בכל מאגרי Beginners.


## גדלי מאגרים

המאגרים עלולים להיות גדולים עקב מספר השפות המתורגמות כדי לסייע למשתמשי קצה להשתמש ב-clone - sparse ולשכפל רק את השפות הנחוצות ולא את כל המאגר

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
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בעוד שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. עבור מידע קריטי, מומלץ תרגום מקצועי על ידי בני אדם. איננו אחראים לכל אי הבנה או פרשנות שגויה הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->