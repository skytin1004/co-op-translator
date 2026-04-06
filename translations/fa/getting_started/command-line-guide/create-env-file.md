# ایجاد فایل *.env* در دایرکتوری ریشه

در این آموزش، شما را در تنظیم متغیرهای محیطی برای سرویس‌های Azure با استفاده از یک فایل *.env* راهنمایی می‌کنیم. متغیرهای محیطی به شما امکان می‌دهند تا مدارک حساس مانند کلیدهای API را به‌صورت ایمن مدیریت کنید، بدون اینکه آنها را به‌طور سخت‌کد شده در کد خود قرار دهید.

> [!IMPORTANT]
> - فقط یکی از سرویس‌های مدل زبان (Azure OpenAI یا OpenAI) باید پیکربندی شود. متغیرهای محیطی مربوط به سرویس ترجیحی خود را پر کنید. اگر متغیرهای محیطی چند مدل زبان تنظیم شده باشند، Co-op Translator بر اساس اولویت یکی را انتخاب می‌کند.
> - اگر متغیرهای محیطی Computer Vision تنظیم نشوند، مترجم به‌طور خودکار به [حالت فقط Markdown](./markdown-only-mode.md) تغییر حالت می‌دهد.

> [!NOTE]
> این راهنما عمدتاً بر سرویس‌های Azure تمرکز دارد، اما می‌توانید هر مدل زبانی پشتیبانی‌شده از [فهرست مدل‌ها و سرویس‌های پشتیبانی‌شده](../README.md#-supported-models-and-services) را انتخاب کنید.

## ایجاد فایل *.env*

در دایرکتوری ریشه پروژه خود، فایلی با نام *.env* ایجاد کنید. این فایل، تمام متغیرهای محیطی شما را در قالبی ساده ذخیره خواهد کرد.

> [!WARNING]
> فایل *.env* خود را در سیستم‌های کنترل نسخه مانند Git کامیت نکنید. فایل *.env* را به .gitignore خود اضافه کنید تا از کامیت‌های تصادفی جلوگیری شود.

1. به دایرکتوری ریشه پروژه خود بروید.

1. یک فایل *.env* در دایرکتوری ریشه پروژه خود ایجاد کنید.

1. فایل *.env* را باز کنید و قالب زیر را الصاق کنید:

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
> اگر می‌خواهید کلیدهای API و نقاط انتهایی خود را پیدا کنید، می‌توانید به [set-up-azure-ai.md](../set-up-azure-ai.md) مراجعه کنید.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرست ناشی از استفاده از این ترجمه نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->