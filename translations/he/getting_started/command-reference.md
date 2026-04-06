# הפניה לפקודות

שורת הפקודה של **Co-op Translator** מציעה מספר אפשרויות להתאמת תהליך התרגום:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | מתרגם את הפרויקט לשפות שצוינו. לדוגמה: translate -l "es fr de" מתרגם לספרדית, צרפתית, וגרמנית. השתמש ב-translate -l "all" לתרגום לכל השפות הנתמכות.
translate -l "language_codes" -u              | מעדכן את התרגומים על ידי מחיקת התרגומים הקיימים ויצירתם מחדש. אזהרה: פעולה זו תמחק את כל תרגומי השפות שצוינו.
translate -l "language_codes" -img            | מתרגם רק קבצי תמונות.
translate -l "language_codes" -md             | מתרגם רק קבצי Markdown.
translate -l "language_codes" -nb             | מתרגם רק קבצי מחברת Jupyter (.ipynb).
translate -l "language_codes" --fix           | מתרגם מחדש קבצים עם ציוני ביטחון נמוכים על סמך תוצאות הערכה קודמת.
translate -l "language_codes" -d              | מפעיל מצב דיבאג לרישום מפורט.
translate -l "language_codes" --save-logs, -s | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/ (הקונסול נשלט על ידי -d)
translate -l "language_codes" -r "root_dir"   | מציין את תיקיית השורש של הפרויקט
translate -l "language_codes" -f              | משתמש במצב מהיר לתרגום תמונות (עד פי 3 מהיר יותר עם מחיר קל באיכות וביישור).
translate -l "language_codes" -y              | מאשר אוטומטית את כל ההנחיות (שימושי לצינורות CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | מאפשר או מבטל הוספת קטע ויתור תרגום מכונה לקבצי Markdown ו-Notebook המתורגמים (ברירת מחדל: מופעל).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | מתאים אישית את קטע שפות ה-README עם כתובת המאגר שלך.
translate -l "language_codes" --help          | פרטים על עזרה בתוך ה-CLI המציג פקודות זמינות
evaluate -l "language_code"                  | מעריך את איכות התרגום לשפה ספציפית ומספק ציוני ביטחון
evaluate -l "language_code" -c 0.8           | מעריך תרגומים עם סף ביטחון מותאם אישית
evaluate -l "language_code" -f               | מצב הערכה מהיר (מבוסס חוקים בלבד, ללא LLM)
evaluate -l "language_code" -D               | מצב הערכה מעמיקה (מבוסס LLM בלבד, יותר יסודי אך איטי יותר)
evaluate -l "language_code" --save-logs, -s  | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "language_codes"             | מעבד מחדש קבצי Markdown מתורגמים לעדכון קישורים למחברות (.ipynb). מעדיף מחברות מתורגמות כאשר זמינות; אחרת יכול לחזור למחברות המקוריות.
migrate-links -l "language_codes" -r          | מציין את תיקיית השורש של הפרויקט (ברירת מחדל: התיקייה הנוכחית).
migrate-links -l "language_codes" --dry-run   | מציג אילו קבצים ישתנו ללא כתיבת שינויים.
migrate-links -l "language_codes" --no-fallback-to-original | לא מחדש קישורים למחברות מקוריות כאשר חסרות מקבילות מתורגמות (מעדכן רק כאשר קיימות מתורגמות).
migrate-links -l "language_codes" -d          | מפעיל מצב דיבאג לרישום מפורט.
migrate-links -l "language_codes" --save-logs, -s | שומר יומני DEBUG לקבצים תחת <root_dir>/logs/
migrate-links -l "all" -y                      | מעבד את כל השפות ומאשר אוטומטית את ההנחיה.

## דוגמאות לשימוש

  1. התנהגות ברירת המחדל (הוסף תרגומים חדשים מבלי למחוק תרגומים קיימים):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. הוסף רק תרגומי תמונות חדשים בקוריאנית (לא מוחקים תרגומים קיימים):    translate -l "ko" -img

  3. עדכן את כל התרגומים בקוריאנית (אזהרה: פעולה זו תמחק את כל תרגומי הקוריאנית הקיימים לפני תרגום מחודש):    translate -l "ko" -u

  4. עדכן רק תמונות בקוריאנית (אזהרה: פעולה זו תמחק את כל תמונות הקוריאנית הקיימות לפני תרגום מחודש):    translate -l "ko" -img -u

  5. הוסף תרגומי Markdown חדשים לקוריאנית מבלי להשפיע על שאר התרגומים:    translate -l "ko" -md

  6. תקן תרגומים עם ביטחון נמוך על בסיס תוצאות הערכה קודמות: translate -l "ko" --fix

  7. תקן תרגומים עם ביטחון נמוך עבור קבצים ספציפיים בלבד (Markdown): translate -l "ko" --fix -md

  8. תקן תרגומים עם ביטחון נמוך עבור קבצים ספציפיים בלבד (תמונות): translate -l "ko" --fix -img

  9. השתמש במצב מהיר לתרגום תמונות:    translate -l "ko" -img -f

  10. תקן תרגומים עם ביטחון נמוך עם סף מותאם אישית: translate -l "ko" --fix -c 0.8

  11. דוגמת מצב דיבאג: - translate -l "ko" -d: אפשר רישום דיבאג.
  12. שמירת יומנים לקבצים: translate -l "ko" -s
  13. DEBUG בקונסול ו-DEBUG בקובץ: translate -l "ko" -d -s
  14. תרגום מבלי להוסיף ויתורי תרגום מכונה לתוצאות: translate -l "ko" --no-disclaimer

  15. העבר קישורים למחברות עבור תרגומים בקוריאנית (עדכן קישורים למחברות מתורגמות כאשר זמינות):    migrate-links -l "ko"

  15. העבר קישורים עם הרצה יבשה (ללא כתיבת קבצים):    migrate-links -l "ko" --dry-run

  16. עדכן רק קישורים כאשר יש מחברות מתורגמות (לא לחזור למחברות המקוריות):    migrate-links -l "ko" --no-fallback-to-original

  17. עיבוד כל השפות עם הנחיית אישור:    migrate-links -l "all"

  18. עיבוד כל השפות ואישור אוטומטי:    migrate-links -l "all" -y
  19. שמירת יומנים לקבצים עבור migrate-links:    migrate-links -l "ko ja" -s

  20. התאם אישית את הנחיית השפות ב-README עם כתובת המאגר שלך:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### דוגמאות להערכה

> [!WARNING]  
> **תכונה בגרסת בטא**: פונקציונליות ההערכה נמצאת כרגע בגרסת בטא. תכונה זו שוחררה להערכת מסמכים מתורגמים, ושיטות ההערכה ומימוש מפורט עדיין בפיתוח ועשויות להשתנות.

  1. הערכת תרגומים בקוריאנית: evaluate -l "ko"

  2. הערכה עם סף ביטחון מותאם אישית: evaluate -l "ko" -c 0.8

  3. הערכה מהירה (מבוססת חוקים בלבד): evaluate -l "ko" -f

  4. הערכה מעמיקה (מבוססת LLM בלבד): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו כאל המקור הסמכותי. למידע קריטי מומלץ תרגום מקצועי על ידי אדם. איננו נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->