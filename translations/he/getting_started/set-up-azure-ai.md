# הגדרת Azure AI עבור Co-op Translator (Azure OpneAI ו-Azure AI Vision)

המדריךนี้ מוביל אותך במהלך הגדרת Azure OpenAI לתרגום שפה ו-Azure Computer Vision לניתוח תוכן תמונה (שניתן להשתמש בו לאחר מכן לתרגום מבוסס תמונה) בתוך Azure AI Foundry.

**דרישות מוקדמות:**
- חשבון Azure עם מנוי פעיל.
- הרשאות מספיקות ליצירת משאבים ופריסות במנוי Azure שלך.

## צור פרויקט Azure AI

תתחיל ביצירת פרויקט Azure AI, המשמש כמקום מרכזי לניהול המשאבים שלך בתחום ה-AI.

1. עבור אל [https://ai.azure.com](https://ai.azure.com) והיכנס עם חשבון Azure שלך.

1. בחר **+Create** כדי ליצור פרויקט חדש.

1. בצע את המשימות הבאות:
   - הזן **שם פרויקט** (למשל, `CoopTranslator-Project`).
   - בחר את **AI hub** (למשל, `CoopTranslator-Hub`) (צור אחד חדש אם צריך).

1. לחץ "**Review and Create**" כדי להקים את הפרויקט שלך. תועבר לדף הסקירה של הפרויקט.

## הגדר Azure OpenAI לתרגום שפה

בתוך הפרויקט שלך, תפרוס דגם Azure OpenAI שישמש כתשתית לתרגום טקסט.

### עבור לפרויקט שלך

אם אינך כבר שם, פתח את הפרויקט החדש שיצרת (למשל, `CoopTranslator-Project`) בתוך Azure AI Foundry.

### פרוס דגם OpenAI

1. מתפריט הצד השמאלי של הפרויקט, תחת "My assets", בחר "**Models + endpoints**".

1. בחר **+ Deploy model**.

1. בחר **Deploy Base Model**.

1. יוצגו בפניך רשימת דגמים זמינים. סנן או חפש דגם GPT מתאים. אנו ממליצים על `gpt-4o`.

1. בחר את הדגם הרצוי ולחץ **Confirm**.

1. בחר **Deploy**.

### הגדרת Azure OpenAI

לאחר הפריסה, תוכל לבחור את הפריסה מדף "**Models + endpoints**" כדי למצוא את **כתובת ה-REST של נקודת הקצה**, **מפתח**, **שם הפריסה**, **שם הדגם** וגרסת ה-API. מידע זה יידרש לשילוב דגם התרגום באפליקציה שלך.

> [!NOTE]
> ניתן לבחור גרסאות API מדף [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) בהתאם לצרכיך. שים לב כי **גרסת ה-API** שונה מגרסת הדגם המוצגת בדף **Models + endpoints** בתוך Azure AI Foundry.

## הגדר Azure Computer Vision לתרגום תמונות

כדי לאפשר תרגום טקסט מתוך תמונות, עליך למצוא את מפתח ה-API של שירות Azure AI ונקודת הקצה.

1. עבור לפרויקט Azure AI שלך (למשל, `CoopTranslator-Project`). ודא שאתה בדף הסקירה של הפרויקט.

### הגדרת שירות Azure AI

מצא את מפתח ה-API ונקודת הקצה משירות Azure AI.

1. עבור לפרויקט Azure AI שלך (למשל, `CoopTranslator-Project`). ודא שאתה בדף הסקירה של הפרויקט.

1. מצא את **מפתח ה-API** ו-**נקודת הקצה** מתוך לשונית שירות Azure AI.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

חיבור זה מאפשר את היכולות של משאב שירותי Azure AI הקישורים (כולל ניתוח תמונות) הזמינים לפרויקט Azure AI Foundry שלך. תוכל להשתמש בחיבור זה במחברות או באפליקציות שלך כדי לחלץ טקסט מתוך תמונות, אותו ניתן בהמשך לשלוח לדגם Azure OpenAI לתרגום.

## איחוד האישורים שלך

עד עכשיו, עליך לאסוף את הפרטים הבאים:

**עבור Azure OpenAI (תרגום טקסט):**
- נקודת קצה Azure OpenAI
- מפתח API של Azure OpenAI
- שם דגם Azure OpenAI (למשל, `gpt-4o`)
- שם פריסת Azure OpenAI (למשל, `cooptranslator-gpt4o`)
- גרסת API של Azure OpenAI

**עבור שירותי Azure AI (חילוץ טקסט מתמונה דרך Vision):**
- נקודת קצה שירות Azure AI
- מפתח API של שירות Azure AI

### דוגמה: הגדרת משתני סביבה (בגרסת תצוגה מקדימה)

בהמשך, כאשר תבנה את האפליקציה שלך, סביר שתגדיר אותה בעזרת האישורים שנאספו. למשל, תוכל להגדיר אותם כמשתני סביבה כך:

```bash
# אישורי שירות AI של Azure (נדרש לתרגום תמונות)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # לדוגמה, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ערכות גיבוי אופציונליות: שכפול משתנים עם הסיומת _1/_2 (אותו אינדקס לכל המשתנים בערכה)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# אישורי Azure OpenAI (נדרש לתרגום טקסט)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # לדוגמה, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # לדוגמה, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # לדוגמה, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # לדוגמה, 2024-12-01-preview

# ערכות גיבוי אופציונליות: שכפול כל קבוצת AZURE_OPENAI_* עם הסיומת _1/_2 (אותו אינדקס לכל המשתנים)
```

---

### קריאה נוספת

- [כיצד ליצור פרויקט ב-Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [כיצד ליצור משאבי Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [כיצד לפרוס דגמי OpenAI ב-Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עלולים לכלול טעויות או אי דיוקים. המסמך המקורי בשפת המקור שלו נחשב למקור הסמכותי. למידע קריטי, מומלץ לבצע תרגום מקצועי על ידי אדם. אנו לא נושאים באחריות על אי הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->