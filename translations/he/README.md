# Co-op Translator

_אוטומציה ותחזוקה קלה של תרגומים לתוכן החינוכי שלך ב-GitHub במספר שפות ככל שהפרויקט שלך מתפתח._

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

### 🌐 תמיכה בריבוי שפות

#### נתמך על ידי [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[ערבית](../ar/README.md) | [בנגלית](../bn/README.md) | [בולגרית](../bg/README.md) | [בורמזית (מיאנמר)](../my/README.md) | [סינית (מפושטת)](../zh-CN/README.md) | [סינית (מסורתית, הונג קונג)](../zh-HK/README.md) | [סינית (מסורתית, מקאו)](../zh-MO/README.md) | [סינית (מסורתית, טאיוואן)](../zh-TW/README.md) | [קרואטית](../hr/README.md) | [צ'כית](../cs/README.md) | [דנית](../da/README.md) | [הולנדית](../nl/README.md) | [אסטונית](../et/README.md) | [פינית](../fi/README.md) | [צרפתית](../fr/README.md) | [גרמנית](../de/README.md) | [יוונית](../el/README.md) | [עברית](./README.md) | [הינדי](../hi/README.md) | [הונגרית](../hu/README.md) | [אינדונזית](../id/README.md) | [איטלקית](../it/README.md) | [יפנית](../ja/README.md) | [קנאדה](../kn/README.md) | [קמרית](../km/README.md) | [קוריאנית](../ko/README.md) | [ליטאית](../lt/README.md) | [מלאית](../ms/README.md) | [מלאיאלאם](../ml/README.md) | [מרטהית](../mr/README.md) | [נפאלית](../ne/README.md) | [פידג'ין ניגרי](../pcm/README.md) | [נורווגית](../no/README.md) | [פרסית (פארסי)](../fa/README.md) | [פולנית](../pl/README.md) | [פורטוגזית (ברזיל)](../pt-BR/README.md) | [פורטוגזית (פורטוגל)](../pt-PT/README.md) | [פונג'אבית (גורמוכי)](../pa/README.md) | [רומנית](../ro/README.md) | [רוסית](../ru/README.md) | [סרבית (קירילית)](../sr/README.md) | [סלובקית](../sk/README.md) | [סלובנית](../sl/README.md) | [ספרדית](../es/README.md) | [סווהילית](../sw/README.md) | [שוודית](../sv/README.md) | [טגלוג (פיליפינית)](../tl/README.md) | [טמילית](../ta/README.md) | [טלוגו](../te/README.md) | [תאית](../th/README.md) | [טורקית](../tr/README.md) | [אוקראינית](../uk/README.md) | [אורדו](../ur/README.md) | [וייטנאמית](../vi/README.md)

> **מעדיפים לשכפל מקומית?**
>
> מאגר זה כולל יותר מ-50 תרגומים לשפות שמגדילים משמעותית את גודל ההורדה. כדי לשכפל ללא התרגומים, השתמש ב-sparse checkout:
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
> זה מספק לך את כל מה שאתה צריך כדי להשלים את הקורס בהורדה מהירה הרבה יותר.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## סקירה כללית

**Co-op Translator** עוזר לך ללוקלזציה של התוכן החינוכי שלך ב-GitHub למספר שפות בקלות.
כאשר אתה מעדכן את קבצי Markdown, תמונות או מחברות, התרגומים נשארים מסונכרנים אוטומטית, ומבטיחים שהתוכן שלך יהיה מדויק ועדכני ללומדים בכל העולם.

דוגמה לאופן שבו התוכן המתורגם מאורגן:

![Example](../../translated_images/he/translation-ex.0c8aa6a7ee0aad2b.webp)

## איך מצב התרגום מנוהל

Co-op Translator מנהל את התוכן המתורגם כ-**ארטיפקטים תוכנתיים בגרסאות**,  
ולא כקבצים סטטיים.

הכלי עוקב אחר מצב תרגום ה-Markdown, התמונות והמחברות
באמצעות **מטא-דאטה בהיקף שפה**.

עיצוב זה מאפשר ל-Co-op Translator:

- לזהות באופן אמין תרגומים מיושנים
- להתייחס ל-Markdown, תמונות ומחברות בצורה עקבית
- להתרחב בצורה בטוחה ברחבי מאגרים גדולים, מהירים ובריבוי שפות

על ידי מיצוב התרגומים כארטיפקטים מנוהלים,
זרימות עבודה של תרגום מתיישרות באופן טבעי עם
הפרקטיקות המודרניות של ניהול תלות בתוכנה וארטיפקטים.

→ [איך מצב התרגום מנוהל](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## התחלת עבודה מהירה

```bash
# צור והפעל סביבה וירטואלית (מומלץ)
python -m venv .venv
# חלונות
.venv\Scripts\activate
# macOS/לינוקס
source .venv/bin/activate
# התקן את החבילה
pip install co-op-translator
# תתרגם
translate -l "ko ja fr" -md
```

Docker:

```bash
# משוך את התמונה הציבורית מ-GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# הרץ עם התיקייה הנוכחית מותקנת ו-.env מסופק (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## הגדרה מינימלית

1. ודא שברשותך גרסת פייתון נתמכת (כרגע 3.10-3.12). ב-poetry (pyproject.toml) זה מטופל אוטומטית.
2. צור קובץ `.env` באמצעות התבנית: [.env.template](../../.env.template)
3. הגדר ספק LLM אחד (Azure OpenAI או OpenAI)
4. (אופציונלי) לתרגום תמונות (`-img`), הגדר Azure AI Vision
5. (אופציונלי) ניתן להגדיר מערכות קרדנציאל מרובות על ידי שכפול משתנים עם סיומות כמו `_1`, `_2` וכו'. כל המשתנים בקבוצה חייבים לשתף את אותה הסיומת.
6. (מומלץ) נקו את כל התרגומים הקודמים כדי למנוע התנגשויות (למשל, `translations/`)
7. (מומלץ) הוסף קטע תרגום ל-README שלך באמצעות [תבנית שפות README](./getting_started/README_languages_template.md)
8. עיין ב: [הגדרת Azure AI](./getting_started/set-up-azure-ai.md)

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

רק מחברות:

```bash
translate -l "zh" -nb
```

דגלים נוספים: [מדריך פקודות](./getting_started/command-reference.md)

## תכונות

- תרגום אוטומטי ל-Markdown, מחברות ותמונות
- שומר על סנכרון בין התרגומים לשינויים במקור
- פועל מקומית (CLI) או ב-CI (GitHub Actions)
- משתמש ב-Azure OpenAI או OpenAI; אופציונלי Azure AI Vision לתמונות
- שומר על פורמט ומבנה Markdown

## תיעוד

- [מדריך שורת פקודה](./getting_started/command-line-guide/command-line-guide.md)
- [מדריך GitHub Actions (מאגרי קוד ציבוריים וסודות סטנדרטיים)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [מדריך GitHub Actions (מאגרים בארגון Microsoft והגדרות ארגוניות)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [תבנית שפות README](./getting_started/README_languages_template.md)
- [שפות נתמכות](./getting_started/supported-languages.md)
- [תרומה לקוד](./CONTRIBUTING.md)
- [פתרון בעיות](./getting_started/troubleshooting.md)

### מדריך ייחודי ל-Microsoft
> [!NOTE]
> עבור משמרי מאגרי ה-"למתחילים" של Microsoft בלבד.

- [עדכון רשימת "קורסים אחרים" (עבור מאגרי מתחילים בלבד)](./getting_started/update-other-courses.md)

## תמכו בנו וקידמו למידה גלובלית

הצטרפו אלינו במהפכה בתחום שיתוף התוכן החינוכי ברחבי העולם! תנו ל-[Co-op Translator](https://github.com/azure/co-op-translator) ⭐ ב-GitHub ותמכו במשימתנו לשבור מחסומי שפה בלמידה וטכנולוגיה. ההתעניינות והתרומות שלכם יוצרות השפעה משמעותית! תרומות בקוד והצעות לפיצ'רים תמיד מתקבלות בברכה.

### חקרו תוכן חינוכי של Microsoft בשפה שלכם

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

👉 לחץ על התמונה למטה לצפייה ב-YouTube.

- **Open at Microsoft**: הקדמה קצרה של 18 דקות ומדריך מהיר לשימוש ב-Co-op Translator.

  [![Open at Microsoft](../../translated_images/he/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## תרומה

פרויקט זה מקבל בברכה תרומות והצעות. מעוניין לתרום ל-Azure Co-op Translator? נא עיין ב-[CONTRIBUTING.md](./CONTRIBUTING.md) שלנו לקבלת הנחיות כיצד תוכל לעזור להפוך את Co-op Translator לנגיש יותר.

## תורמים
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## קוד התנהגות

פרויקט זה אימץ את [קוד ההתנהגות בקוד הפתוח של מיקרוסופט](https://opensource.microsoft.com/codeofconduct/).
למידע נוסף ראו את [שאלות נפוצות על קוד ההתנהגות](https://opensource.microsoft.com/codeofconduct/faq/) או
צרו קשר בכתובת [opencode@microsoft.com](mailto:opencode@microsoft.com) עם כל שאלה או הערה נוספת.

## בינה מלאכותית אחראית

מיקרוסופט מחויבת לעזור ללקוחותיה להשתמש במוצרי ה-AI שלנו באחריות, לשתף את הלימודים שלנו ולבנות שותפויות מבוססות אמון דרך כלים כמו הערות שקיפות והערכות השפעה. משאבים רבים אלו נמצאים בכתובת [https://aka.ms/RAI](https://aka.ms/RAI).
הגישה של מיקרוסופט לבינה מלאכותית אחראית נשענת על עקרונות ה-AI שלנו: הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכללה, שקיפות ואחריות.

מודלי שפה, תמונה ודיבור בקנה מידה גדול - כמו אלו המשמשים בדוגמה זו - עלולים לפעול בדרכים שאינן הוגנות, אמינות או עלולות להיות פוגעניות, ולגרום נזקים. אנא בדקו את [הערת השקיפות של שירות Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להיות מודעים לסיכונים ולמגבלות.

הגישה המומלצת למתן מענה לסיכונים אלה היא לכלול מערכת בטיחות בארכיטקטורה שלכם שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספק שכבת הגנה עצמאית, המסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או על ידי AI באפליקציות ובשירותים. Azure AI Content Safety כוללת APIs לטקסט ותמונה שמאפשרים לזהות חומר מזיק. יש לנו גם סטודיו אינטראקטיבי לבטיחות תוכן שמאפשר לצפות, לחקור ולנסות קוד לדוגמה לזיהוי תוכן מזיק במודאליות שונות. תיעוד [מהיר להתחלה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) הבא מדריך אתכם כיצד לבצע בקשות לשירות.

היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכוללים. עם אפליקציות רב-מודאליות ורב-מודליות, אנו מחשיבים ביצועים כעובדה שהמערכת מתפקדת כפי שאתם והמשתמשים שלכם מצפים, כולל אי יצירת פלטים מזיקים. חשוב להעריך את ביצועי האפליקציה הכוללים שלכם באמצעות [מדדי איכות יצירה, סיכון ובטיחות](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

ניתן להעריך את אפליקציית ה-AI שלכם בסביבת הפיתוח באמצעות [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). נתון מערך בדיקה או יעד, יצירות האפליקציה הגנרטיבית שלכם נמדדות כמותית עם מעריכים מובנים או מעריכים מותאמים אישית לבחירתכם. כדי להתחיל עם ה-prompt flow sdk להערכת המערכת, ניתן לעקוב אחרי [מדריך התחלה מהירה](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). לאחר ביצוע ריצה להערכה, ניתן [להציג את התוצאות ב-Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## סימני מסחר

פרויקט זה עלול לכלול סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. השימוש המורשה בסימני המסחר או הלוגואים של מיקרוסופט כפוף ל-
[הנחיות לסימני המסחר ומותג של מיקרוסופט](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
שימוש בסימני המסחר או לוגואים של מיקרוסופט בגרסאות מותאמות של פרויקט זה אסור לגרום לבלבול או לרמוז לספונסרשיפ של מיקרוסופט.
שימוש בכל סימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותו צד שלישי.

## קבלת עזרה

אם אתם נתקעים או יש לכם שאלות על בניית אפליקציות AI, הצטרפו ל:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

אם יש לכם משוב על המוצר או שגיאות במהלך הבנייה בקרו ב:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדייק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי, מומלץ להיעזר בתרגום מקצועי על ידי בני אדם. אנו לא נושאים באחריות לכל אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->