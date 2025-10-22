<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:56:35+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "he"
}
-->
# תרומה ל-Co-op Translator

הפרויקט הזה מזמין תרומות והצעות. רוב התרומות דורשות שתאשר הסכם רישיון תורם (CLA) שמצהיר שיש לך את הזכות, ואתה אכן מעניק לנו את הזכויות להשתמש בתרומה שלך. לפרטים, בקר ב-https://cla.opensource.microsoft.com.

כשאתה מגיש Pull Request, בוט ה-CLA יבדוק אוטומטית אם אתה צריך לספק CLA ויעטר את ה-PR בהתאם (למשל, בדיקת סטטוס, תגובה). פשוט עקוב אחרי ההוראות של הבוט. תצטרך לעשות זאת רק פעם אחת בכל הרפוז שמשתמשים ב-CLA שלנו.

## הגדרת סביבת פיתוח

להגדרת סביבת הפיתוח לפרויקט הזה, מומלץ להשתמש ב-Poetry לניהול התלויות. אנחנו משתמשים ב-`pyproject.toml` לניהול התלויות, ולכן להתקנת התלויות יש להשתמש ב-Poetry.

### יצירת סביבת עבודה וירטואלית

#### באמצעות pip

```bash
python -m venv .venv
```

#### באמצעות Poetry

```bash
poetry init
```

### הפעלת סביבת העבודה הווירטואלית

#### עבור pip ו-Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### באמצעות Poetry

```bash
poetry shell
```

### התקנת החבילה והחבילות הנדרשות

#### באמצעות Poetry (מה- pyproject.toml)

```bash
poetry install
```

### בדיקות ידניות

לפני הגשת PR, חשוב לבדוק את פונקציית התרגום עם תיעוד אמיתי:

1. צור תיקיית בדיקה בתיקיית השורש:
    ```bash
    mkdir test_docs
    ```

2. העתק מסמכי Markdown ותמונות שתרצה לתרגם לתיקיית הבדיקה. לדוגמה:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. התקן את החבילה מקומית:
    ```bash
    pip install -e .
    ```

4. הרץ את Co-op Translator על מסמכי הבדיקה שלך:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. בדוק את הקבצים המתורגמים ב-`test_docs/translations` וב-`test_docs/translated_images` כדי לוודא:
   - איכות התרגום
   - ההערות במטא-דאטה נכונות
   - מבנה ה-Markdown המקורי נשמר
   - קישורים ותמונות עובדים כמו שצריך

הבדיקה הידנית הזו עוזרת לוודא שהשינויים שלך עובדים טוב בתרחישים אמיתיים.

### משתני סביבה

1. צור קובץ `.env` בתיקיית השורש על ידי העתקת הקובץ `.env.template` שסופק.
1. מלא את משתני הסביבה לפי ההנחיות.

> [!TIP]
>
> ### אפשרויות נוספות לסביבת פיתוח
>
> בנוסף להרצת הפרויקט מקומית, אפשר גם להשתמש ב-GitHub Codespaces או ב-VS Code Dev Containers כאפשרות חלופית להגדרת סביבת פיתוח.
>
> #### GitHub Codespaces
>
> אפשר להריץ את הדוגמאות האלה באופן וירטואלי באמצעות GitHub Codespaces וללא הגדרות או התקנות נוספות.
>
> הכפתור יפתח VS Code מבוסס דפדפן:
>
> 1. פתח את התבנית (זה עשוי לקחת כמה דקות):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### הרצה מקומית עם VS Code Dev Containers
>
> ⚠️ אפשרות זו תעבוד רק אם Docker Desktop שלך מוקצה לפחות 16GB RAM. אם יש לך פחות, אפשר לנסות את [אפשרות GitHub Codespaces](../..) או [להגדיר מקומית](../..).
>
> אפשרות קשורה היא VS Code Dev Containers, שפותחת את הפרויקט ב-VS Code המקומי שלך עם [הרחבת Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. הפעל את Docker Desktop (התקן אם לא מותקן)
> 2. פתח את הפרויקט:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### סגנון קוד

אנחנו משתמשים ב-[Black](https://github.com/psf/black) כפורמטור קוד Python כדי לשמור על אחידות הסגנון בפרויקט. Black הוא פורמטור קוד בלתי מתפשר שמסדר אוטומטית את הקוד לפי הסגנון של Black.

#### הגדרות

ההגדרות של Black נמצאות ב-`pyproject.toml` שלנו:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### התקנת Black

אפשר להתקין את Black עם Poetry (מומלץ) או pip:

##### עם Poetry

Black מותקן אוטומטית כשאתה מגדיר את סביבת הפיתוח:
```bash
poetry install
```

##### עם pip

אם אתה משתמש ב-pip, אפשר להתקין את Black ישירות:
```bash
pip install black
```

#### שימוש ב-Black

##### עם Poetry

1. עיצוב כל קבצי ה-Python בפרויקט:
    ```bash
    poetry run black .
    ```

2. עיצוב קובץ או תיקייה מסוימים:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### עם pip

1. עיצוב כל קבצי ה-Python בפרויקט:
    ```bash
    black .
    ```

2. עיצוב קובץ או תיקייה מסוימים:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> מומלץ להגדיר את העורך שלך לעצב אוטומטית קוד עם Black בשמירה. רוב העורכים המודרניים תומכים בזה דרך הרחבות או תוספים.

## הרצת Co-op Translator

להרצת Co-op Translator עם Poetry בסביבה שלך, בצע את השלבים הבאים:

1. עבור לתיקייה שבה תרצה לבצע בדיקות תרגום או צור תיקייה זמנית לבדיקה.

2. הרץ את הפקודה הבאה. החלף את `-l ko` בקוד השפה שאליה תרצה לתרגם. הדגל `-d` מפעיל מצב דיבאג.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ודא שסביבת Poetry שלך מופעלת (poetry shell) לפני הרצת הפקודה.

## תרומה לשפה חדשה

נשמח לקבל תרומות שמוסיפות תמיכה בשפות חדשות. לפני פתיחת PR, השלם את השלבים הבאים כדי להבטיח בדיקה חלקה.

1. הוסף את השפה למיפוי הפונטים
   - ערוך את `src/co_op_translator/fonts/font_language_mappings.yml`
   - הוסף ערך עם:
     - `code`: קוד שפה בסגנון ISO (למשל, `vi`)
     - `name`: שם תצוגה קריא
     - `font`: פונט שנמצא ב-`src/co_op_translator/fonts/` שתומך בכתב
     - `rtl`: `true` אם מימין לשמאל, אחרת `false`

2. כלול קבצי פונט נדרשים (אם צריך)
   - אם נדרש פונט חדש, בדוק התאמת רישיון להפצה בקוד פתוח
   - הוסף את קובץ הפונט ל-`src/co_op_translator/fonts/`

3. בדיקה מקומית
   - הרץ תרגומים לדוגמה קטנה (Markdown, תמונות, ו-notebooks לפי הצורך)
   - ודא שהתוצאה מוצגת נכון, כולל פונטים וכל פריסת RTL אם רלוונטי

4. עדכן תיעוד
   - ודא שהשפה מופיעה ב-`getting_started/supported-languages.md`
   - אין צורך לשנות את `README_languages_template.md`; הוא נוצר אוטומטית מהרשימה הנתמכת

5. פתח PR
   - תאר את השפה שנוספה וכל שיקולי פונט/רישוי
   - צרף צילומי מסך של התוצאות אם אפשר

דוגמה לערך YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### בדיקת השפה החדשה

אפשר לבדוק את השפה החדשה על ידי הרצת הפקודה הבאה:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## מתחזקים

### פורמט הודעת Commit ואסטרטגיית מיזוג

כדי לשמור על אחידות ובהירות בהיסטוריית ה-commit של הפרויקט, אנחנו משתמשים בפורמט הודעת commit מסוים **להודעת ה-commit הסופית** כשמשתמשים באסטרטגיית **Squash and Merge**.

כש-Pull Request (PR) מתמזג, ה-commits הבודדים יאוחדו ל-commit אחד. הודעת ה-commit הסופית צריכה להיות לפי הפורמט הבא כדי לשמור על היסטוריה נקייה ואחידה.

#### פורמט הודעת Commit (ל-squash and merge)

אנחנו משתמשים בפורמט הבא להודעות commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: מציין את קטגוריית ה-commit. אנחנו משתמשים בסוגים הבאים:
  - `Docs`: לעדכוני תיעוד.
  - `Build`: לשינויים שקשורים למערכת הבנייה או לתלויות, כולל עדכוני קבצי קונפיגורציה, CI, או Dockerfile.
  - `Core`: לשינויים בפונקציונליות הליבה של הפרויקט, במיוחד בקבצים שב-`src/co_op_translator/core`.

- **description**: סיכום קצר של השינוי.
- **PR number**: מספר ה-Pull Request שקשור ל-commit.

**דוגמאות**:

- `Docs: עדכון הוראות התקנה להבהרה (#50)`
- `Core: שיפור טיפול בתרגום תמונות (#60)`

> [!NOTE]
> כרגע, הקידומות **`Docs`**, **`Core`**, ו-**`Build`** מתווספות אוטומטית לכותרות PR לפי התוויות שמוחלות על קוד המקור ששונה. כל עוד התווית הנכונה מוחלת, בדרך כלל אין צורך לעדכן ידנית את כותרת ה-PR. רק צריך לוודא שהכול נכון והקידומת נוצרה כראוי.

#### אסטרטגיית מיזוג

אנחנו משתמשים ב-**Squash and Merge** כאסטרטגיית ברירת מחדל ל-Pull Requests. אסטרטגיה זו מבטיחה שהודעות ה-commit יהיו לפי הפורמט שלנו, גם אם ה-commits הבודדים לא.

**סיבות**:

- היסטוריה נקייה וליניארית של הפרויקט.
- אחידות בהודעות commit.
- פחות רעש מ-commits קטנים (למשל, "fix typo").

בעת המיזוג, ודא שהודעת ה-commit הסופית היא לפי הפורמט שתואר למעלה.

**דוגמה ל-Squash and Merge**
אם PR מכיל את ה-commits הבאים:

- `fix typo`
- `update README`
- `adjust formatting`

הם צריכים להיות מאוחדים ל:
`Docs: שיפור בהירות התיעוד והפורמט (#65)`

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.