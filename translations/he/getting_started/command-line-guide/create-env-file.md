# צור את קובץ *.env* בתיקיית השורש

בהדרכה זו, ננחה אותך כיצד להגדיר את משתני הסביבה שלך לשירותי Azure באמצעות קובץ *.env*. משתני סביבה מאפשרים לך לנהל בצורה מאובטחת פרטי גישה רגישים, כגון מפתחות API, מבלי לקודד אותם ישירות בקוד שלך.

> [!IMPORTANT]
> - יש להגדיר שירות אחד בלבד של דגם שפה (Azure OpenAI או OpenAI). מלא את משתני הסביבה עבור השירות המועדף עליך. אם מוגדרים משתני סביבה למספר דגמי שפה, מתרגם ה-Co-op יבחר אחד על פי סדר עדיפות.
> - אם משתני הסביבה של Computer Vision אינם מוגדרים, המתרגם יחליף אוטומטית ל-[מצב Markdown בלבד](./markdown-only-mode.md).

> [!NOTE]
> מדריך זה מתמקד בעיקר בשירותי Azure, אך באפשרותך לבחור כל דגם שפה נתמך מהרשימה של [מודלים ושירותים נתמכים](../README.md#-supported-models-and-services).

## צור את קובץ *.env*

בתיקיית השורש של הפרויקט שלך, צור קובץ בשם *.env*. קובץ זה יאחסן את כל משתני הסביבה שלך בפורמט פשוט.

> [!WARNING]
> אל תתחייב לקובץ *.env* במערכות בקרת גרסאות כמו Git. הוסף את *.env* לקובץ .gitignore שלך כדי למנוע התחייבויות בשוגג.

1. עבור לתיקיית השורש של הפרויקט שלך.

1. צור קובץ *.env* בתיקיית השורש של הפרויקט שלך.

1. פתח את קובץ *.env* והדבק את התבנית הבאה:

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
> אם ברצונך למצוא את מפתחות ה-API והנקודות הקצה שלך, ניתן לעיין ב-[set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**כתב הבהרה**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית יש להחשיב כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי מבוצע על ידי אדם. אנו לא נושאים באחריות לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->