# שימוש ב-GitHub Action של Co-op Translator (הגדרה ציבורית)

**קהל יעד:** מדריך זה מיועד למשתמשים ברוב הריפוזיטוריות הציבוריות או הפרטיות שבהן הרשאות GitHub Actions הסטנדרטיות מספיקות. הוא עושה שימוש ב-`GITHUB_TOKEN` המובנה.

הפכו את תהליך תרגום התיעוד בריפוזיטורי שלכם לאוטומטי ופשוט בעזרת Co-op Translator GitHub Action. מדריך זה יסביר לכם כיצד להגדיר את הפעולה כך שתיצור Pull Requests עם תרגומים מעודכנים בכל פעם שמסמכי Markdown או תמונות מקור משתנים.

> [!IMPORTANT]
>
> **בחירת המדריך הנכון:**
>
> מדריך זה מפרט את **ההגדרה הפשוטה באמצעות `GITHUB_TOKEN` הסטנדרטי**. זוהי השיטה המומלצת לרוב המשתמשים, כיוון שאין צורך לנהל מפתחות פרטיים רגישים של GitHub App.
>

## דרישות מוקדמות

לפני הגדרת ה-GitHub Action, ודאו שיש לכם את פרטי הגישה לשירות ה-AI הדרוש.

**1. חובה: פרטי גישה למודל שפה מבוסס AI**
יש צורך בפרטי גישה לפחות לאחד מהמודלים הנתמכים:

- **Azure OpenAI**: דורש Endpoint, API Key, שמות מודל/פריסה, גרסת API.
- **OpenAI**: דורש API Key, (אופציונלי: Org ID, Base URL, Model ID).
- ראו [מודלים ושירותים נתמכים](../../../../README.md) לפרטים נוספים.

**2. אופציונלי: פרטי גישה ל-AI Vision (לתרגום טקסט בתמונות)**

- דרוש רק אם יש צורך לתרגם טקסט מתוך תמונות.
- **Azure AI Vision**: דורש Endpoint ו-Subscription Key.
- אם לא תספקו אותם, הפעולה תעבוד במצב [Markdown בלבד](../markdown-only-mode.md).

## הגדרה וקונפיגורציה

בצעו את השלבים הבאים כדי להגדיר את Co-op Translator GitHub Action בריפוזיטורי שלכם באמצעות `GITHUB_TOKEN` הסטנדרטי.

### שלב 1: הבנת האימות (שימוש ב-`GITHUB_TOKEN`)

ה-Workflow משתמש ב-`GITHUB_TOKEN` המובנה שמספק GitHub Actions. הטוקן הזה מעניק אוטומטית הרשאות ל-Workflow לפעול מול הריפוזיטורי בהתאם להגדרות שתגדירו ב**שלב 3**.

### שלב 2: הגדרת Secrets בריפוזיטורי

כל מה שצריך זה להוסיף את **פרטי הגישה לשירותי ה-AI** כ-Secrets מוצפנים בהגדרות הריפוזיטורי.

1.  עברו לריפוזיטורי היעד שלכם ב-GitHub.
2.  גשו ל-**Settings** > **Secrets and variables** > **Actions**.
3.  תחת **Repository secrets**, לחצו על **New repository secret** עבור כל Secret נדרש מהרשימה למטה.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.he.png) *(הפניה לתמונה: מראה איפה להוסיף Secrets)*

**Secrets נדרשים לשירותי AI (הוסיפו את כל מה שרלוונטי לפי הדרישות המוקדמות):**

| שם ה-Secret                         | תיאור                                   | מקור הערך                     |
| :---------------------------------- | :-------------------------------------- | :---------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | מפתח לשירות Azure AI (Computer Vision)    | Azure AI Foundry שלכם             |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint לשירות Azure AI (Computer Vision) | Azure AI Foundry שלכם             |
| `AZURE_OPENAI_API_KEY`              | מפתח לשירות Azure OpenAI                | Azure AI Foundry שלכם             |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint לשירות Azure OpenAI             | Azure AI Foundry שלכם             |
| `AZURE_OPENAI_MODEL_NAME`           | שם המודל שלכם ב-Azure OpenAI             | Azure AI Foundry שלכם             |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | שם הפריסה שלכם ב-Azure OpenAI            | Azure AI Foundry שלכם             |
| `AZURE_OPENAI_API_VERSION`          | גרסת API ל-Azure OpenAI                  | Azure AI Foundry שלכם             |
| `OPENAI_API_KEY`                    | מפתח API ל-OpenAI                        | פלטפורמת OpenAI שלכם           |
| `OPENAI_ORG_ID`                     | מזהה ארגון OpenAI (אופציונלי)            | פלטפורמת OpenAI שלכם           |
| `OPENAI_CHAT_MODEL_ID`              | מזהה מודל OpenAI מסוים (אופציונלי)       | פלטפורמת OpenAI שלכם           |
| `OPENAI_BASE_URL`                   | כתובת בסיס מותאמת ל-OpenAI API (אופציונלי) | פלטפורמת OpenAI שלכם           |

### שלב 3: הגדרת הרשאות ל-Workflow

ה-GitHub Action צריך הרשאות דרך `GITHUB_TOKEN` כדי לבצע checkout לקוד וליצור Pull Requests.

1.  בריפוזיטורי שלכם, גשו ל-**Settings** > **Actions** > **General**.
2.  גללו עד לקטע **Workflow permissions**.
3.  בחרו ב-**Read and write permissions**. זה מעניק ל-`GITHUB_TOKEN` את ההרשאות הדרושות (`contents: write` ו-`pull-requests: write`) ל-Workflow הזה.
4.  ודאו שהאפשרות **Allow GitHub Actions to create and approve pull requests** מסומנת.
5.  לחצו על **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.he.png)

### שלב 4: יצירת קובץ Workflow

לבסוף, צרו את קובץ ה-YAML שמגדיר את ה-Workflow האוטומטי באמצעות `GITHUB_TOKEN`.

1.  בתיקיית השורש של הריפוזיטורי, צרו את התיקייה `.github/workflows/` אם היא לא קיימת.
2.  בתוך `.github/workflows/`, צרו קובץ בשם `co-op-translator.yml`.
3.  העתיקו את התוכן הבא ל-`co-op-translator.yml`.

```yaml
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
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
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

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
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
4.  **התאמת ה-Workflow:**
  - **[!IMPORTANT] שפות יעד:** בשלב `Run Co-op Translator`, חובה לעבור ולשנות את רשימת קודי השפות בפקודת `translate -l "..." -y` כך שתתאים לצרכי הפרויקט שלכם. הרשימה לדוגמה (`ar de es...`) צריכה להיות מוחלפת או מותאמת.
  - **Trigger (`on:`):** ההגדרה הנוכחית מפעילה את ה-Workflow בכל Push ל-main. בריפוזיטוריות גדולות, מומלץ להוסיף פילטר `paths:` (ראו דוגמה בתגובות ב-YAML) כדי להפעיל את ה-Workflow רק כאשר קבצים רלוונטיים (למשל תיעוד מקור) משתנים, וכך לחסוך זמן ריצה.
  - **פרטי ה-PR:** התאימו את ה-`commit-message`, `title`, `body`, שם ה-`branch` וה-`labels` בשלב יצירת ה-Pull Request לפי הצורך.

## הפעלת ה-Workflow

> [!WARNING]  
> **מגבלת זמן ל-GitHub-hosted Runner:**  
> ל-GitHub-hosted runners כמו `ubuntu-latest` יש **מגבלת זמן ריצה מקסימלית של 6 שעות**.  
> בריפוזיטוריות תיעוד גדולות, אם תהליך התרגום עובר את 6 השעות, ה-Workflow יופסק אוטומטית.  
> כדי למנוע זאת, שקלו:  
> - שימוש ב-**self-hosted runner** (ללא מגבלת זמן)  
> - הפחתת מספר שפות היעד בכל ריצה

לאחר שמיזגתם את קובץ `co-op-translator.yml` ל-main (או לענף שמוגדר ב-`on:`), ה-Workflow ירוץ אוטומטית בכל פעם שמבוצעים שינויים לענף הזה (ובהתאם לפילטר `paths`, אם מוגדר).

---

**הצהרת אחריות**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנות או פירושים שגויים הנובעים מהשימוש בתרגום זה.