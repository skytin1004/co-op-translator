# צור את הקובץ *.env* בספריית השורש

בהדרכה זו ננחה אותך כיצד להגדיר את משתני הסביבה שלך לשירותי Azure באמצעות קובץ *.env*. משתני סביבה מאפשרים לך לנהל בצורה מאובטחת אישורים רגישים, כגון מפתחות API, מבלי להכניסם ישירות לקוד שלך.

> [!IMPORTANT]
> - יש להגדיר רק שירות מודל שפה אחד (Azure OpenAI או OpenAI). מלא את משתני הסביבה עבור השירות המועדף עליך. אם מוגדרים משתני סביבה עבור מספר מודלי שפה, ה-Co-op Translator יבחר אחד על פי עדיפות.
> - אם משתני הסביבה של Computer Vision אינם מוגדרים, המתורגמן יעבור אוטומטית למצב [Markdown-only mode](./markdown-only-mode.md).

> [!NOTE]
> מדריך זה מתמקד בעיקר בשירותי Azure, אך ניתן לבחור כל מודל שפה נתמך מהרשימה של [supported models and services](../README.md#-supported-models-and-services).

## צור את הקובץ *.env*

בספריית השורש של הפרויקט שלך, צור קובץ בשם *.env*. קובץ זה יאחסן את כל משתני הסביבה שלך בפורמט פשוט.

> [!WARNING]
> אל תבצע commit לקובץ ה-*.env* במערכות ניהול גרסאות כמו Git. הוסף את *.env* לקובץ ה-.gitignore שלך כדי למנוע commits בטעות.

1. נווט אל ספריית השורש של הפרויקט שלך.

1. צור קובץ *.env* בספריית השורש של הפרויקט שלך.

1. פתח את קובץ ה-*.env* והדבק את התבנית הבאה:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> אם ברצונך למצוא את מפתחות ה-API והנקודות הקצה שלך, תוכל לעיין ב-[set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). בזמן שאנו שואפים לדייק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי דיוקים. יש להחשיב את המסמך המקורי בשפתו המקורית כמקור מוסמך. למידע קריטי מומלץ לבצע תרגום מקצועי על ידי אדם. איננו אחראים לכל אי הבנה או פרשנות שגוייה הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->