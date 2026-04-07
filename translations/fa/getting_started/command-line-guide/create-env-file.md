# ایجاد فایل *.env* در دایرکتوری ریشه

در این آموزش، ما شما را در راه‌اندازی متغیرهای محیطی برای سرویس‌های Azure با استفاده از فایل *.env* راهنمایی خواهیم کرد. متغیرهای محیطی به شما امکان می‌دهند تا اطلاعات حساس مانند کلیدهای API را به صورت ایمن مدیریت کنید بدون اینکه آن‌ها را به صورت مستقیم در کد خود وارد کنید.

> [!IMPORTANT]
> - تنها یک سرویس مدل زبانی (Azure OpenAI یا OpenAI) باید پیکربندی شود. متغیرهای محیطی را برای سرویس مورد نظر خود پر کنید. اگر متغیرهای محیطی چندین مدل زبانی تنظیم شده باشند، Co-op Translator بر اساس اولویت یکی را انتخاب خواهد کرد.
> - اگر متغیرهای محیطی Computer Vision تنظیم نشده باشند، مترجم به صورت خودکار به [حالت فقط Markdown](./markdown-only-mode.md) تغییر خواهد یافت.

> [!NOTE]
> این راهنما عمدتاً بر سرویس‌های Azure تمرکز دارد، اما شما می‌توانید هر مدل زبانی پشتیبانی شده را از [لیست مدل‌ها و سرویس‌های پشتیبانی شده](../README.md#-supported-models-and-services) انتخاب کنید.

## ایجاد فایل *.env*

در دایرکتوری ریشه پروژه خود، یک فایل با نام *.env* ایجاد کنید. این فایل تمام متغیرهای محیطی شما را در قالب ساده‌ای ذخیره خواهد کرد.

> [!WARNING]
> فایل *.env* خود را به سیستم‌های کنترل نسخه مانند Git ارسال نکنید. فایل *.env* را به فایل .gitignore خود اضافه کنید تا از ثبت ناخواسته جلوگیری شود.

1. به دایرکتوری ریشه پروژه خود بروید.

1. یک فایل *.env* در دایرکتوری ریشه پروژه خود ایجاد کنید.

1. فایل *.env* را باز کرده و قالب زیر را بچسبانید:

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
> اگر می‌خواهید کلیدها و نقاط پایان API خود را پیدا کنید، می‌توانید به [set-up-azure-ai.md](../set-up-azure-ai.md) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**توضیح مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا ناصحیحی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، توصیه می‌شود از ترجمه حرفه‌ای انسان استفاده کنید. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->