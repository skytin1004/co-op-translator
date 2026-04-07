# أنشئ ملف *.env* في الدليل الجذري

في هذا الدليل، سنرشدك خلال إعداد متغيرات البيئة الخاصة بك لخدمات Azure باستخدام ملف *.env*. تتيح لك متغيرات البيئة إدارة بيانات الاعتماد الحساسة بأمان، مثل مفاتيح API، دون الحاجة إلى ترميزها مباشرة في قاعدة الشيفرة الخاصة بك.

> [!IMPORTANT]
> - تحتاج إلى تكوين خدمة نموذج لغة واحدة فقط (Azure OpenAI أو OpenAI). املأ متغيرات البيئة للخدمة التي تفضلها. إذا تم إعداد متغيرات بيئة لعدة نماذج لغوية، سيختار المترجم التعاوني واحدًا بناءً على الأولوية.
> - إذا لم يتم إعداد متغيرات بيئة رؤية الكمبيوتر، سيتحول المترجم تلقائيًا إلى [وضع Markdown فقط](./markdown-only-mode.md).

> [!NOTE]
> يركز هذا الدليل بشكل رئيسي على خدمات Azure، لكن يمكنك اختيار أي نموذج لغوي مدعوم من قائمة [النماذج والخدمات المدعومة](../README.md#-supported-models-and-services).

## أنشئ ملف *.env*

في الدليل الجذري لمشروعك، أنشئ ملفًا باسم *.env*. سيخزن هذا الملف جميع متغيرات البيئة الخاصة بك بصيغة بسيطة.

> [!WARNING]
> لا تقم بإضافة ملف *.env* إلى أنظمة التحكم في النسخ مثل Git. أضف *.env* إلى ملف .gitignore الخاص بك لمنع الالتزامات العرضية.

1. انتقل إلى الدليل الجذري لمشروعك.

1. أنشئ ملف *.env* في الدليل الجذري لمشروعك.

1. افتح ملف *.env* والصق القالب التالي:

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
> إذا كنت تريد العثور على مفاتيح API ونقاط النهاية الخاصة بك، يمكنك الرجوع إلى [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم بأن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغة المصدر المصدر الموثوق به. للمعلومات الهامة، يُنصح بالترجمة الاحترافية بواسطة مترجم بشري. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->