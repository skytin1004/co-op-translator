# עדכון סעיף "קורסים אחרים" (מאגרי Microsoft Beginners)

מדריך זה מסביר כיצד לגרום לסעיף "קורסים אחרים" לסנכרן אוטומטית באמצעות Co-op Translator, וכיצד לעדכן את התבנית הגלובלית לכל המאגר.

- חל על: מאגרי Microsoft Beginners בלבד  
- פועל עם: Co-op Translator CLI ו-GitHub Actions  
- מקור התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## התחלה מהירה: הפעלת סנכרון אוטומטי במאגר שלך

הוסף את הסימנים הבאים סביב סעיף "קורסים אחרים" בקובץ ה-README שלך. Co-op Translator יחליף הכל בין סימנים אלה בכל ריצה.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
בכל פעם ש-Co-op Translator רץ — דרך CLI (למשל, `translate -l "<language codes>"`) או GitHub Actions — הוא יעדכן אוטומטית את סעיף "קורסים אחרים" העטוף בסימנים אלה.

> [!NOTE]  
> אם יש לך רשימה קיימת, פשוט עטוף אותה באותם סימנים. הריצה הבאה תחליף אותה בתוכן המוסדר העדכני ביותר.

---

## כיצד לשנות את התוכן הגלובלי

אם ברצונך לעדכן את התוכן המוסדר שמופיע בכל מאגרי Beginners:

1. ערוך את התבנית: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. פתח בקשת משיכה למאגר Co-op Translator עם השינויים שלך  
3. לאחר שהבקשה משולבת, גרסת ה-Co-op Translator תעודכן  
4. בפעם הבאה ש-Co-op Translator ירוץ (CLI או GitHub Action) במאגר יעד, הוא יסנכרן אוטומטית את הסעיף המעודכן

זה מבטיח מקור אמת יחיד לתוכן "קורסים אחרים" בכל מאגרי Beginners.

## גדלי מאגר 

המאגרים עלולים להיות גדולים עקב כמות השפות המתורגמות כדי לסייע למשתמשי הקצה לספק הדרכה כיצד להשתמש ב-clone - sparse כדי לשכפל רק את השפות הנחוצות ולא את כל המאגר

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
**כתב ויתור אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי אנושי. אנו לא אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->