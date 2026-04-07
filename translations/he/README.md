# Co-op Translator

_אוטומציה ותחזוקה קלים של תרגומים לתוכן החינוכי שלך ב-GitHub במגוון שפות ככל שהפרויקט שלך מתפתח._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 תמיכה ברב שפות

#### נתמך על ידי [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](./README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **מעדיפים לשכפל מקומי?**
>
> מאגר זה כולל למעלה מ-50 תרגומים לשפות, מה שמגדיל משמעותית את גודל ההורדה. כדי לשכפל ללא התרגומים, השתמשו ב-sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> זה נותן לכם את כל מה שצריך כדי להשלים את הקורס עם הורדה מהירה משמעותית.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## סקירה כללית

**Co-op Translator** עוזר לכם לאזור את התוכן החינוכי שלכם ב-GitHub למספר שפות בקלות.
כשאתם מעדכנים את קבצי Markdown, תמונות או יומנים, התרגומים מתעדכנים באופן אוטומטי, ומבטיחים שהתוכן שלכם נשאר מדויק ומעודכן ללומדים בכל רחבי העולם.

דוגמה לאופן ארגון התוכן המתורגם:

![Example](../../imgs/translation-ex.png)

## איך מנוהל מצב התרגום

Co-op Translator מנהל את התוכן המתורגם כ**ארטיפקטים של תוכנה בגרסאות**,  
ולא כקבצים סטטיים.

הכלי עוקב אחר מצב Markdown, תמונות ויומנים מתורגמים
באמצעות **מטא-דאטה ברמת שפה**.

עיצוב זה מאפשר ל-Co-op Translator:

- לזהות תרגומים מיושנים בצורה אמינה
- להתייחס אל Markdown, תמונות ויומנים באופן עקבי
- להתרחב בבטחה במאגרים גדולים, מהירים ורב-שפתיים

על ידי מודלינג של תרגומים כארטיפקטים מנוהלים,
זרימות עבודה של תרגום מתיישרות באופן טבעי עם שיטות ניהול
תלויות ותהליכי גרסאות של תוכנה מודרנית.

→ [כיצד ניהול מצב התרגום מתבצע](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## התחלה מהירה

```bash
# צור והפעל סביבה וירטואלית (מומלץ)
python -m venv .venv
# חלונות
.venv\Scripts\activate
# מק או לינוקס
source .venv/bin/activate
# התקן את החבילה
pip install co-op-translator
# תרגם
translate -l "ko ja fr" -md
```

Docker:

```bash
# משוך את התמונה הציבורית מ-GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# הפעל עם התיקייה הנוכחית מותקנת וקובץ .env מסופק (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## התקנה מינימלית

1. וודא שיש לך גרסת Python נתמכת (כרגע 3.10-3.12). ב-poetry (pyproject.toml) זה מטופל אוטומטית.
2. צור קובץ `.env` באמצעות התבנית: [.env.template](../../.env.template)
3. הגדר ספק LLM אחד (Azure OpenAI או OpenAI)
4. (אופציונלי) לתרגום תמונות (`-img`), הגדר Azure AI Vision
5. (אופציונלי) ניתן להגדיר מספר מערכי הרשאות על ידי שכפול משתנים עם סיומות כמו `_1`, `_2`, וכו'. כל המשתנים במערך חייבים לחלוק את אותה סיומת.
6. (מומלץ) נקה תרגומים קודמים כדי למנוע התנגשויות (לדוגמה, `translations/`)
7. (מומלץ) הוסף קטע תרגום ל-README שלך באמצעות [תבנית שפות ל-README](./getting_started/README_languages_template.md)
8. ראה: [הגדרת Azure AI](./getting_started/set-up-azure-ai.md)

## שימוש

תרגם את כל הסוגים הנתמכים:

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

רק יומנים:

```bash
translate -l "zh" -nb
```

עוד דגלים: [הפנייה לפקודות](./getting_started/command-reference.md)

## תכונות

- תרגום אוטומטי ל-Markdown, יומנים ותמונות
- שומר על סנכרון התרגומים עם שינויים במקור
- עובד באופן מקומי (CLI) או ב-CI (GitHub Actions)
- משתמש ב-Azure OpenAI או OpenAI; בינה מלאכותית Azure AI Vision אופציונלית לתמונות
- שומר על מבנה ופורמט Markdown

## תיעוד

- [מדריך שורת פקודה](./getting_started/command-line-guide/command-line-guide.md)
- [מדריך GitHub Actions (מאגרי ציבוריים וסודות סטנדרטיים)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [מדריך GitHub Actions (מאגרי ארגון Microsoft והגדרות ארגוניות)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [תבנית שפות ל-README](./getting_started/README_languages_template.md)
- [שפות נתמכות](./getting_started/supported-languages.md)
- [תורמים](./CONTRIBUTING.md)
- [פתרון תקלות](./getting_started/troubleshooting.md)

### מדריך ספציפי למיקרוסופט
> [!NOTE]
> מיועד למתחזקים של מאגרי Microsoft “למתחילים” בלבד.

- [עדכון רשימת "קורסים אחרים" (למאגרי MS למתחילים בלבד)](./getting_started/update-other-courses.md)

## תמכו בנו וקידמו למידה גלובלית

הצטרפו אלינו במהפכה של שיתוף תוכן חינוכי גלובלי! העניקו ל-[Co-op Translator](https://github.com/azure/co-op-translator) ⭐ ב-GitHub ותמכו במשימה שלנו לפרוץ מחסומי שפה בלמידה וטכנולוגיה. העניין והתרומות שלכם משנים במידה משמעותית! תרומות קוד והצעות תכונות תמיד מתקבלות בברכה.

### חקרו תוכן חינוכי של מיקרוסופט בשפה שלכם

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## מצגות וידאו

👉 לחצו על התמונה למטה לצפייה ביוטיוב.

- **Open at Microsoft**: הקדמה ותדריך קצר של 18 דקות על איך להשתמש ב-Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## תרומה

פרויקט זה מקבל ברצון תרומות והצעות. מעוניינים לתרום ל-Azure Co-op Translator? ראו את [CONTRIBUTING.md](./CONTRIBUTING.md) שלנו לקבלת הנחיות כיצד תוכלו לעזור להפוך את Co-op Translator לנגיש יותר.

## תורמים
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## קוד ההתנהגות

הפרויקט הזה אימץ את [קוד ההתנהגות בקוד פתוח של Microsoft](https://opensource.microsoft.com/codeofconduct/).
למידע נוסף ראה את ה-[שאלות נפוצות על קוד ההתנהגות](https://opensource.microsoft.com/codeofconduct/faq/) או פנה ל-[opencode@microsoft.com](mailto:opencode@microsoft.com) עם שאלות או הערות נוספות.

## בינה מלאכותית אחראית

Microsoft מחויבת לעזור ללקוחותינו להשתמש במוצרי ה-AI שלנו באחריות, לשתף את הלמידות שלנו, ולבנות שותפויות מבוססות אמון באמצעות כלים כמו הערות שקיפות והערכות השפעה. משאבים רבים ניתן למצוא ב-[https://aka.ms/RAI](https://aka.ms/RAI).
הגישות של Microsoft לבינה מלאכותית אחראית מבוססות על עקרונות AI של הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

מודלים רחבי היקף של שפה טבעית, תמונה ודיבור — כמו אלה שבהם משתמשים בדוגמה זו — עלולים להתנהג בצורה לא הוגנת, לא אמינה או פוגענית, דבר שיכול לגרום לנזקים. אנא התייעצו ב-[הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להתעדכן בסיכונים ומגבלות.

הגישה המומלצת להפחתת סיכונים אלה היא לכלול מערכת בטיחות בארכיטקטורה שלך שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או בינה מלאכותית באפליקציות ושירותים. Azure AI Content Safety כוללת APIs לטקסט ותמונה שמאפשרים לזהות חומר מזיק. בנוסף, יש לנו סטודיו אינטראקטיבי של Content Safety שמאפשר לך לצפות, לחקור ולנסות קוד לדוגמה לזיהוי תוכן מזיק במגוון מודאליות. התיעוד הבא [מהיר ההתחלה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ינחה אותך כיצד לבצע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכוללים. עם יישומים מרובי מודאליות ומודלים, אנו מתייחסים לביצועים כאל מערכת שמתפקדת כפי שאתה והמשתמשים שלך מצפים, כולל אי יצירת פלטים מזיקים. חשוב להעריך את ביצועי האפליקציה הכוללים שלך באמצעות [מדדי איכות יצירה, סיכון ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

ניתן להעריך את אפליקציית הבינה המלאכותית שלך בסביבת הפיתוח שלך באמצעות ה-[prompt flow SDK](https://microsoft.github.io/promptflow/index.html). בין אם מדובר בערכת נתוני בדיקה או ביעד, דורות הבינה המלאכותית שלך נמדדים בכמות באמצעות מעריכי ביצועים מובנים או מעריכים מותאמים אישית שתבחר. כדי להתחיל עם prompt flow sdk להערכת המערכת שלך, ניתן לעקוב אחרי ה-[מדריך מהיר ההתחלה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר הפעלת ריצת הערכה, ניתן [להציג את התוצאות ב-Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימני מסחר

הפרויקט הזה עשוי לכלול סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסימני המסחר או בלוגואים של Microsoft כפוף ומחויב ל-[הנחיות סימני המסחר והמותגים של Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
שימוש בסימני המסחר או בלוגואים של Microsoft בגרסאות מתוקנות של פרויקט זה אסור שיגרום לבלבול או לרמוז על חסות של Microsoft.
שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות אותם צדדים שלישיים.

## קבלת עזרה

אם נתקלת בקשיים או יש לך שאלות בנוגע לבניית אפליקציות בינה מלאכותית, הצטרף/י ל:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

אם יש לך משוב על המוצר או שגיאות בעת הבנייה, בקר/י ב:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו הטבעית נחשב למקור הסמכותי. עבור מידע קריטי, מומלץ שימוש בתרגום מקצועי על ידי אנשים. אנו לא אחראים לכל אי הבנה או פרשנות שגויה הנובעים משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->