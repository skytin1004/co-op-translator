<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:09:03+00:00",
  "source_file": "README.md",
  "language_code": "he"
}
-->
# מתרגם Co-op

_הפכו את התרגום של התוכן החינוכי שלכם ב-GitHub לאוטומטי, ותגיעו לקהל עולמי בקלות._

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
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](./README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## סקירה כללית

**Co-op Translator** מאפשר לכם לתרגם במהירות את התוכן החינוכי שלכם ב-GitHub למגוון שפות, ולהגיע בקלות לקהל עולמי. כאשר אתם מעדכנים קבצי Markdown, תמונות או מחברות Jupyter, התרגומים מסתנכרנים אוטומטית כדי לשמור על התוכן שלכם עדכני ורלוונטי למשתמשים מכל העולם.

ראו כיצד Co-op Translator מארגן את התוכן החינוכי המתורגם ב-GitHub:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.he.png)

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
- מומלץ: אם יש לכם תרגומים שנוצרו בכלים אחרים, נקו אותם קודם כדי למנוע התנגשויות (למשל: `translations/`).
- מומלץ: הוסיפו סעיף תרגומים ל-README שלכם בעזרת [תבנית שפות ל-README](./README_languages_template.md)
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

## תיעוד

- [מדריך שורת פקודה](./getting_started/command-line-guide/command-line-guide.md)
- [מדריך GitHub Actions (ריפוזיטוריים ציבוריים וסודות סטנדרטיים)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [מדריך GitHub Actions (ריפוזיטוריים של ארגון Microsoft והגדרות ברמת ארגון)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [שפות נתמכות](./getting_started/supported-languages.md)
- [פתרון תקלות](./getting_started/troubleshooting.md)

## תמכו בנו וקידמו למידה גלובלית

הצטרפו אלינו למהפכה בדרך בה תוכן חינוכי משותף ברחבי העולם! תנו ל-[Co-op Translator](https://github.com/azure/co-op-translator) ⭐ ב-GitHub ותמכו במשימה שלנו לשבור את מחסומי השפה בלמידה ובטכנולוגיה. ההתעניינות והתרומה שלכם משפיעות מאוד! נשמח לקבל תרומות קוד והצעות לפיצ'רים.

### גלו תוכן חינוכי של Microsoft בשפה שלכם

- [AZD למתחילים](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI למתחילים](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) למתחילים](https://github.com/microsoft/mcp-for-beginners)
- [סוכני AI למתחילים](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI למתחילים ב-.NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI למתחילים](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI למתחילים ב-Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML למתחילים](https://aka.ms/ml-beginners)
- [Data Science למתחילים](https://aka.ms/datascience-beginners)
- [AI למתחילים](https://aka.ms/ai-beginners)
- [סייבר למתחילים](https://github.com/microsoft/Security-101)
- [פיתוח אתרים למתחילים](https://aka.ms/webdev-beginners)
- [IoT למתחילים](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## הרצאות וידאו

למדו עוד על Co-op Translator דרך ההרצאות שלנו _(לחצו על התמונה לצפייה ב-YouTube.)_:

- **Open at Microsoft**: היכרות קצרה של 18 דקות ומדריך מהיר לשימוש ב-Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.he.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## תרומה לפרויקט

הפרויקט הזה מזמין תרומות והצעות. רוצים לתרום ל-Azure Co-op Translator? ראו את [CONTRIBUTING.md](./CONTRIBUTING.md) להנחיות כיצד תוכלו לעזור להפוך את Co-op Translator לנגיש יותר.

## תורמים

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## קוד אתי

הפרויקט הזה אימץ את [קוד ההתנהגות של קוד פתוח של Microsoft](https://opensource.microsoft.com/codeofconduct/).
למידע נוסף ראו את [שאלות ותשובות על קוד ההתנהגות](https://opensource.microsoft.com/codeofconduct/faq/) או
פנו ל-[opencode@microsoft.com](mailto:opencode@microsoft.com) עם שאלות או הערות נוספות.

## בינה מלאכותית אחראית

Microsoft מחויבת לעזור ללקוחות להשתמש במוצרי הבינה המלאכותית שלנו באחריות, לשתף את הלקחים שלנו ולבנות שותפויות מבוססות אמון באמצעות כלים כמו Transparency Notes ו-Impact Assessments. משאבים רבים זמינים ב-[https://aka.ms/RAI](https://aka.ms/RAI).
הגישה של Microsoft לבינה מלאכותית אחראית מבוססת על עקרונות של הוגנות, אמינות ובטיחות, פרטיות ואבטחה, הכלה, שקיפות ואחריות.

מודלים גדולים לשפה, תמונה ודיבור – כמו אלו שבדוגמה הזו – עלולים לפעול בדרכים לא הוגנות, לא אמינות או פוגעניות, ולגרום לנזק. אנא עיינו ב-[הערת השקיפות של Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) כדי להכיר את הסיכונים והמגבלות.

הדרך המומלצת לצמצום סיכונים היא לכלול מערכת בטיחות בארכיטקטורה שלכם שיכולה לזהות ולמנוע התנהגות מזיקה. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) מספקת שכבת הגנה עצמאית, שמסוגלת לזהות תוכן מזיק שנוצר על ידי משתמשים או בינה מלאכותית. השירות כולל APIs לטקסט ולתמונה שמאפשרים לזהות חומר מזיק. יש גם Content Safety Studio אינטראקטיבי שמאפשר לצפות, לחקור ולנסות דוגמאות קוד לזיהוי תוכן מזיק במגוון פורמטים. [מדריך ההתחלה המהירה](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ילווה אתכם בביצוע בקשות לשירות.


היבט נוסף שיש לקחת בחשבון הוא ביצועי האפליקציה הכלליים. באפליקציות מרובות מודלים ומרובות מצבים, ביצועים משמעותם שהמערכת פועלת כפי שאתה והמשתמשים שלך מצפים, כולל הימנעות מהפקת תוצרים מזיקים. חשוב להעריך את ביצועי האפליקציה שלך באמצעות <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in">מדדי איכות יצירה, סיכון ובטיחות</a>.

ניתן להעריך את אפליקציית הבינה המלאכותית שלך בסביבת הפיתוח באמצעות <a href="https://microsoft.github.io/promptflow/index.html">prompt flow SDK</a>. בעזרת מערך נתונים לבדיקה או יעד מסוים, תוצרי האפליקציה שלך נמדדים באופן כמותי בעזרת מעריכי איכות מובנים או מותאמים אישית לבחירתך. כדי להתחיל לעבוד עם prompt flow sdk ולהעריך את המערכת שלך, אפשר לעקוב אחר <a href="https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk">מדריך ההתחלה המהירה</a>. לאחר ביצוע הערכה, ניתן <a href="https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results">לראות את התוצאות ב-Azure AI Studio</a>.

## סימני מסחר

הפרויקט הזה עשוי לכלול סימני מסחר או לוגואים של פרויקטים, מוצרים או שירותים. שימוש מורשה בסימני מסחר או לוגואים של Microsoft כפוף ל- ועליו לעמוד ב- <a href="https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general">הנחיות סימני המסחר והמותג של Microsoft</a>. שימוש בסימני מסחר או לוגואים של Microsoft בגרסאות ערוכות של הפרויקט הזה לא יגרום לבלבול או לרמוז על חסות של Microsoft. כל שימוש בסימני מסחר או לוגואים של צד שלישי כפוף למדיניות של אותו צד שלישי.

## קבלת עזרה

אם נתקעת או יש לך שאלות לגבי בניית אפליקציות בינה מלאכותית, הצטרף ל:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

אם יש לך משוב על המוצר או נתקלת בשגיאות במהלך הבנייה, בקר ב:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**הצהרת אחריות**:
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עשויים להכיל טעויות או אי-דיוקים. יש לראות במסמך המקורי בשפתו המקורית כמקור הסמכותי. למידע קריטי, מומלץ לפנות לתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנה או פירוש שגוי הנובעים מהשימוש בתרגום זה.