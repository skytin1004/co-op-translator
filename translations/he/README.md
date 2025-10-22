<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:56:55+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# מתרגם Co-op

_הפכו את התרגום של התוכן החינוכי שלכם ב-GitHub לאוטומטי, ותגיעו לקהל עולמי בקלות._

תמיכה בשפות רבות

#### נתמך על ידי <a href="https://github.com/Azure/Co-op-Translator">Co-op Translator</a>

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
<a href="./translations/ar/README.md">ערבית</a> | <a href="./translations/bn/README.md">בנגלית</a> | <a href="./translations/bg/README.md">בולגרית</a> | <a href="./translations/my/README.md">בורמזית (מיאנמר)</a> | <a href="./translations/zh/README.md">סינית (פשוטה)</a> | <a href="./translations/hk/README.md">סינית (מסורתית, הונג קונג)</a> | <a href="./translations/mo/README.md">סינית (מסורתית, מקאו)</a> | <a href="./translations/tw/README.md">סינית (מסורתית, טייוואן)</a> | <a href="./translations/hr/README.md">קרואטית</a> | <a href="./translations/cs/README.md">צ'כית</a> | <a href="./translations/da/README.md">דנית</a> | <a href="./translations/nl/README.md">הולנדית</a> | <a href="./translations/et/README.md">אסטונית</a> | <a href="./translations/fi/README.md">פינית</a> | <a href="./translations/fr/README.md">צרפתית</a> | <a href="./translations/de/README.md">גרמנית</a> | <a href="./translations/el/README.md">יוונית</a> | <a href="./translations/he/README.md">עברית</a> | <a href="./translations/hi/README.md">הינדית</a> | <a href="./translations/hu/README.md">הונגרית</a> | <a href="./translations/id/README.md">אינדונזית</a> | <a href="./translations/it/README.md">איטלקית</a> | <a href="./translations/ja/README.md">יפנית</a> | <a href="./translations/ko/README.md">קוריאנית</a> | <a href="./translations/lt/README.md">ליטאית</a> | <a href="./translations/ms/README.md">מלאית</a> | <a href="./translations/mr/README.md">מרטהי</a> | <a href="./translations/ne/README.md">נפאלית</a> | <a href="./translations/pcm/README.md">ניגרית פידג'ין</a> | <a href="./translations/no/README.md">נורווגית</a> | <a href="./translations/fa/README.md">פרסית (פארסי)</a> | <a href="./translations/pl/README.md">פולנית</a> | <a href="./translations/br/README.md">פורטוגזית (ברזיל)</a> | <a href="./translations/pt/README.md">פורטוגזית (פורטוגל)</a> | <a href="./translations/pa/README.md">פנג'בית (גורמוקי)</a> | <a href="./translations/ro/README.md">רומנית</a> | <a href="./translations/ru/README.md">רוסית</a> | <a href="./translations/sr/README.md">סרבית (קירילית)</a> | <a href="./translations/sk/README.md">סלובקית</a> | <a href="./translations/sl/README.md">סלובנית</a> | <a href="./translations/es/README.md">ספרדית</a> | <a href="./translations/sw/README.md">סווהילית</a> | <a href="./translations/sv/README.md">שוודית</a> | <a href="./translations/tl/README.md">טאגאלוג (פיליפינית)</a> | <a href="./translations/ta/README.md">טמילית</a> | <a href="./translations/th/README.md">תאית</a> | <a href="./translations/tr/README.md">טורקית</a> | <a href="./translations/uk/README.md">אוקראינית</a> | <a href="./translations/ur/README.md">אורדו</a> | <a href="./translations/vi/README.md">וייטנאמית</a>
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## סקירה כללית

**Co-op Translator** מאפשר לכם לתרגם במהירות את התוכן החינוכי שלכם ב-GitHub לשפות רבות, ולהגיע לקהל עולמי בלי מאמץ. כאשר אתם מעדכנים קבצי Markdown, תמונות או מחברות Jupyter, התרגומים מסתנכרנים אוטומטית כדי שהתוכן שלכם יישאר עדכני ורלוונטי למשתמשים מכל העולם.

ראו כיצד Co-op Translator מארגן את התוכן החינוכי המתורגם ב-GitHub:

![דוגמה](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.he.png)

## התחלה מהירה

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## הגדרה מינימלית

- צרו קובץ `.env` לפי התבנית: [.env.template](../../.env.template)
- הגדירו ספק LLM אחד (Azure OpenAI או OpenAI)
- לתרגום תמונות (`-img`), הגדירו גם Azure AI Vision
- מומלץ: אם יש לכם תרגומים שנוצרו בכלים אחרים, נקו אותם קודם כדי למנוע התנגשות (למשל: `translations/`).
- מומלץ: הוסיפו מקטע תרגומים ל-README שלכם בעזרת [תבנית שפות ל-README](./README_languages_template.md)
- ראו: [הגדרת Azure AI](./getting_started/set-up-azure-ai.md)

## שימוש

תרגום כל הסוגים הנתמכים:

```bash
translate -l "ko ja"
```

רק Markdown:

```bash
translate -l "de" -md
```

Markdown + תמונות:

```bash
translate -l "pt" -md -img
```

רק מחברות:

```bash
translate -l "zh" -nb
```

עוד דגלים: [מדריך פקודות](./getting_started/command-reference.md)

## תכונות

- תרגום אוטומטי ל-Markdown, מחברות ותמונות
- שומר על סנכרון התרגומים עם שינויים במקור
- עובד מקומית (CLI) או ב-CI (GitHub Actions)
- משתמש ב-Azure OpenAI או OpenAI; אפשרות ל-Azure AI Vision לתמונות
- שומר על מבנה ופורמט Markdown

## מסמכים

- [מדריך שורת פקודה](./getting_started/command-line-guide/command-line-guide.md)
- [מדריך GitHub Actions (ריפוזיטוריים ציבוריים וסודות סטנדרטיים)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [מדריך GitHub Actions (ריפוזיטוריים של ארגון Microsoft והגדרות ברמת ארגון)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [שפות נתמכות](./getting_started/supported-languages.md)
- [פתרון בעיות](./getting_started/troubleshooting.md)

## תמכו בנו וקידמו למידה עולמית

הצטרפו אלינו למהפכה בשיתוף תוכן חינוכי ברחבי העולם! תנו ל-<a href="https://github.com/azure/co-op-translator">Co-op Translator</a> ⭐ ב-GitHub ותמכו במשימה שלנו לשבור את מחסומי השפה בלמידה ובטכנולוגיה. ההתעניינות והתרומה שלכם משפיעות מאוד! נשמח לקבל תרומות קוד והצעות לפיצ'רים.

### גלו תוכן חינוכי של Microsoft בשפה שלכם

- <a href="https://github.com/microsoft/AZD-for-beginners">AZD למתחילים</a>
- <a href="https://github.com/microsoft/edgeai-for-beginners">Edge AI למתחילים</a>
- <a href="https://github.com/microsoft/mcp-for-beginners">Model Context Protocol (MCP) למתחילים</a>
- <a href="https://github.com/microsoft/ai-agents-for-beginners">סוכני AI למתחילים</a>
- <a href="https://github.com/microsoft/Generative-AI-for-beginners-dotnet">Generative AI למתחילים ב-.NET</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners">Generative AI למתחילים</a>
- <a href="https://github.com/microsoft/generative-ai-for-beginners-java">Generative AI למתחילים ב-Java</a>
- <a href="https://aka.ms/ml-beginners">למידת מכונה למתחילים</a>
- <a href="https://aka.ms/datascience-beginners">מדעי הנתונים למתחילים</a>
- <a href="https://aka.ms/ai-beginners">AI למתחילים</a>
- <a href="https://github.com/microsoft/Security-101">סייבר למתחילים</a>
- <a href="https://aka.ms/webdev-beginners">פיתוח אתרים למתחילים</a>
- <a href="https://aka.ms/iot-beginners">IoT למתחילים</a>
- <a href="https://github.com/microsoft/PhiCookBook">PhiCookBook</a>

## מצגות וידאו

למדו עוד על Co-op Translator דרך המצגות שלנו _(לחצו על התמונה לצפייה ב-YouTube.)_:

- **Open at Microsoft**: היכרות קצרה של 18 דקות ומדריך מהיר לשימוש ב-Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.he.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## תרומה לפרויקט

הפרויקט הזה מזמין תרומות והצעות. רוצים לתרום ל-Azure Co-op Translator? ראו את [CONTRIBUTING.md](./CONTRIBUTING.md) להנחיות כיצד תוכלו לעזור להפוך את Co-op Translator לנגיש יותר.

## תורמים

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## קוד אתי

הפרויקט הזה אימץ את <a href="https://opensource.microsoft.com/codeofconduct/">קוד האתי של Microsoft לקוד פתוח</a>.
למידע נוסף ראו את <a href="https://opensource.microsoft.com/codeofconduct/faq/">שאלות ותשובות על קוד האתי</a> או
פנו ל-<a href="mailto:opencode@microsoft.com">opencode@microsoft.com</a> עם שאלות או הערות נוספות.

## AI אחראי

Microsoft מחויבת לעזור ללקוחות להשתמש במוצרי AI שלנו באחריות, לשתף את הידע שלנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו Transparency Notes ו-Impact Assessments. משאבים רבים זמינים ב-<a href="https://aka.ms/RAI">https://aka.ms/RAI</a>.
הגישה של Microsoft ל-AI אחראי מבוססת על עקרונות של הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכלה, שקיפות ואחריות.

מודלים גדולים לשפה, תמונה ודיבור – כמו אלו שבדוגמה הזו – עלולים לפעול באופן לא הוגן, לא אמין או פוגעני, ולגרום לנזק. קראו את <a href="https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text">הערת השקיפות של Azure OpenAI</a> כדי להכיר את הסיכונים והמגבלות.

הדרך המומלצת לצמצום סיכונים היא לכלול מערכת בטיחות בארכיטקטורה שלכם שיכולה לזהות ולמנוע התנהגות מזיקה. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview">Azure AI Content Safety</a> מספקת שכבת הגנה עצמאית, שמסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או AI. השירות כולל APIs לטקסט ולתמונה שמאפשרים לזהות חומרים מזיקים. יש גם Content Safety Studio אינטראקטיבי שמאפשר לצפות, לחקור ולנסות דוגמאות קוד לזיהוי תוכן מזיק במגוון סוגי מדיה. <a href="https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest">מדריך ההתחלה המהירה</a> יסייע לכם לבצע בקשות לשירות.


היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכלליים. באפליקציות מרובות מודלים ומרובות מצבים, ביצועים משמעותם שהמערכת פועלת כפי שאתה והמשתמשים שלך מצפים, כולל הימנעות מהפקת תוצרים מזיקים. חשוב להעריך את ביצועי האפליקציה שלך באמצעות <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">מדדי איכות יצירה, סיכון ובטיחות</a>.

ניתן להעריך את אפליקציית הבינה המלאכותית שלך בסביבת הפיתוח באמצעות <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. בעזרת מערך נתונים לבדיקה או יעד מסוים, תוצרי האפליקציה שלך נמדדים באופן כמותי בעזרת מעריכי ביצועים מובנים או מותאמים אישית לבחירתך. כדי להתחיל לעבוד עם prompt flow sdk ולהעריך את המערכת שלך, אפשר לעקוב אחר <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">מדריך ההתחלה המהירה</a>. לאחר ביצוע הערכה, ניתן <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">לראות את התוצאות ב-Azure AI Studio</a>.

## סימני מסחר

הפרויקט הזה עשוי לכלול סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסימני מסחר או לוגואים של Microsoft כפוף ל- ועליו לעמוד ב- <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">הנחיות סימני המסחר והמותג של Microsoft</a>. שימוש בסימני מסחר או לוגואים של Microsoft בגרסאות ערוכות של הפרויקט הזה לא יגרום לבלבול או לרמוז על חסות של Microsoft. כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותו צד שלישי.

## קבלת עזרה

אם נתקעת או שיש לך שאלות לגבי בניית אפליקציות בינה מלאכותית, הצטרף ל:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

אם יש לך משוב על המוצר או נתקלת בשגיאות במהלך הבנייה, בקר ב:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. המסמך המקורי בשפתו המקורית הוא המקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.