# راه‌اندازی Azure AI برای Co-op Translator (Azure OpneAI و Azure AI Vision)

این راهنما مراحل راه‌اندازی Azure OpenAI برای ترجمه زبان و Azure Computer Vision برای تحلیل محتوای تصاویر (که سپس می‌تواند برای ترجمه مبتنی بر تصویر استفاده شود) در Azure AI Foundry را به شما نشان می‌دهد.

**پیش‌نیازها:**  
- یک حساب Azure با اشتراک فعال.  
- مجوزهای کافی برای ایجاد منابع و استقرارها در اشتراک Azure خود.  

## ایجاد پروژه Azure AI

شما با ایجاد یک پروژه Azure AI شروع خواهید کرد، که به عنوان مکان مرکزی برای مدیریت منابع AI شما عمل می‌کند.

1. به [https://ai.azure.com](https://ai.azure.com) بروید و با حساب Azure خود وارد شوید.

1. گزینه **+Create** را برای ساخت پروژه جدید انتخاب کنید.

1. کارهای زیر را انجام دهید:  
   - یک **نام پروژه** وارد کنید (مثلاً `CoopTranslator-Project`).  
   - **AI hub** را انتخاب کنید (مثلاً `CoopTranslator-Hub`) (در صورت نیاز یک مورد جدید ایجاد کنید).

1. روی "**Review and Create**" کلیک کنید تا پروژه شما تنظیم شود. صفحه نمای کلی پروژه به شما نمایش داده خواهد شد.

## راه‌اندازی Azure OpenAI برای ترجمه زبان

در پروژه خود، یک مدل Azure OpenAI را مستقر خواهید کرد تا به عنوان بک‌اند برای ترجمه متن خدمت کند.

### رفتن به پروژه خود

اگر هنوز در پروژه نیستید، پروژه تازه ایجاد شده خود (مثلاً `CoopTranslator-Project`) را در Azure AI Foundry باز کنید.

### استقرار مدل OpenAI

1. از منوی سمت چپ پروژه خود، در زیر "My assets"، گزینه "**Models + endpoints**" را انتخاب کنید.

1. گزینه **+ Deploy model** را انتخاب کنید.

1. گزینه **Deploy Base Model** را انتخاب کنید.

1. فهرستی از مدل‌های موجود به شما نمایش داده می‌شود. مدل GPT مناسب را فیلتر یا جستجو کنید. ما مدل `gpt-4o` را پیشنهاد می‌کنیم.

1. مدل مورد نظر خود را انتخاب کرده و روی **Confirm** کلیک کنید.

1. روی **Deploy** کلیک کنید.

### پیکربندی Azure OpenAI

پس از استقرار، می‌توانید استقرار را از صفحه "**Models + endpoints**" انتخاب کرده و **REST endpoint URL**، **کلید**، **نام استقرار**، **نام مدل** و **نسخه API** آن را بیابید. این موارد برای ادغام مدل ترجمه در برنامه شما لازم خواهند بود.

> [!NOTE]  
> می‌توانید نسخه‌های API را از صفحه [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) بر اساس نیازهای خود انتخاب کنید. توجه داشته باشید که **نسخه API** با **نسخه مدل** که در صفحه **Models + endpoints** در Azure AI Foundry نمایش داده می‌شود متفاوت است.

## راه‌اندازی Azure Computer Vision برای ترجمه تصویر

برای فعال‌سازی ترجمه متن داخل تصاویر، باید کلید API و نقطه پایانی (Endpoint) سرویس Azure AI را پیدا کنید.

1. به پروژه Azure AI خود مراجعه کنید (مثلاً `CoopTranslator-Project`). مطمئن شوید در صفحه نمای کلی پروژه هستید.

### پیکربندی سرویس Azure AI

کلید API و نقطه پایانی را از سرویس Azure AI بیابید.

1. به پروژه Azure AI خود مراجعه کنید (مثلاً `CoopTranslator-Project`). مطمئن شوید در صفحه نمای کلی پروژه هستید.

1. کلید **API Key** و **Endpoint** را در تب سرویس Azure AI پیدا کنید.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

این اتصال قابلیت‌های منبع مرتبط به سرویس‌های Azure AI (شامل تحلیل تصویر) را در پروژه AI Foundry شما در دسترس قرار می‌دهد. سپس می‌توانید از این اتصال در نوت‌بوک‌ها یا برنامه‌های خود برای استخراج متن از تصاویر استفاده کنید و این متن استخراج شده را به مدل Azure OpenAI برای ترجمه ارسال کنید.

## جمع‌آوری اطلاعات اعتبارسنجی شما

تا کنون باید موارد زیر را جمع‌آوری کرده باشید:

**برای Azure OpenAI (ترجمه متن):**  
- نقطه پایانی Azure OpenAI  
- کلید API Azure OpenAI  
- نام مدل Azure OpenAI (مثلاً `gpt-4o`)  
- نام استقرار Azure OpenAI (مثلاً `cooptranslator-gpt4o`)  
- نسخه API Azure OpenAI  

**برای سرویس‌های Azure AI (استخراج متن از تصویر از طریق Vision):**  
- نقطه پایانی سرویس Azure AI  
- کلید API سرویس Azure AI  

### مثال: پیکربندی متغیرهای محیطی (پیش‌نمایش)

بعداً هنگام ساخت برنامه خود، احتمالاً با استفاده از این اطلاعات اعتبارسنجی پیکربندی خواهید کرد. برای نمونه، ممکن است آن‌ها را به صورت متغیرهای محیطی به شکل زیر تنظیم کنید:

```bash
# اعتبارنامه‌های سرویس هوش مصنوعی آژور (برای ترجمه تصویر لازم است)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # مثلاً، 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# مجموعه‌های جایگزین اختیاری: متغیرهای تکراری با پسوند _1/_2 (اندیس یکسان برای همه متغیرهای مجموعه)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# اعتبارنامه‌های Azure OpenAI (برای ترجمه متن لازم است)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # مثلاً، 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # مثلاً، gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # مثلاً، cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # مثلاً، 2024-12-01-preview

# مجموعه‌های جایگزین اختیاری: تکرار کامل مجموعه AZURE_OPENAI_* با پسوند _1/_2 (اندیس یکسان برای همه متغیرها)
```
  
---

### مطالعات بیشتر

- [چگونه یک پروژه در Azure AI Foundry ایجاد کنیم](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)  
- [چگونه منابع Azure AI ایجاد کنیم](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)  
- [چگونه مدل‌های OpenAI را در Azure AI Foundry استقرار دهیم](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا عدم دقت باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچگونه سوءتفاهم یا تفسیر نادرستی که ناشی از استفاده از این ترجمه باشد، نیستیم.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->