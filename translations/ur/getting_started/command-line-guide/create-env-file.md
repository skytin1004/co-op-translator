# روٹ ڈائریکٹری میں *.env* فائل بنائیں

اس ٹیوٹوریل میں، ہم آپ کو Azure سروسز کے لیے اپنے ماحول کے متغیرات سیٹ اپ کرنے کی رہنمائی کریں گے جس کے لیے ایک *.env* فائل استعمال کی جائے گی۔ ماحول کے متغیرات آپ کو حساس اسناد جیسے API کیز کو محفوظ طریقے سے منظم کرنے کی اجازت دیتے ہیں، بغیر انہیں اپنے کوڈ بیس میں سخت کوڈ کیے۔

> [!IMPORTANT]
> - صرف ایک زبان ماڈل سروس (Azure OpenAI یا OpenAI) کو ترتیب دینا ضروری ہے۔ اپنے ترجیحی سروس کے لیے ماحول کے متغیرات پُر کریں۔ اگر متعدد زبان ماڈلز کے ماحول کے متغیرات سیٹ کیے گئے ہیں، تو Co-op Translator ترجیح کی بنیاد پر ایک کا انتخاب کرے گا۔
> - اگر کمپیوٹر وژن کے ماحول کے متغیرات سیٹ نہیں ہیں، تو مترجم خود بخود [صرف مارک ڈاؤن موڈ](./markdown-only-mode.md) پر سوئچ کر جائے گا۔

> [!NOTE]
> یہ رہنمائی بنیادی طور پر Azure سروسز پر مرکوز ہے، لیکن آپ [موجودہ ماڈلز اور سروسز کی فہرست](../README.md#-supported-models-and-services) سے کوئی بھی سپورٹ شدہ زبان ماڈل منتخب کر سکتے ہیں۔

## *.env* فائل بنائیں

اپنے پروجیکٹ کی روٹ ڈائریکٹری میں، *.env* نامی فائل بنائیں۔ یہ فائل آپ کے تمام ماحول کے متغیرات کو ایک سادہ فارمیٹ میں محفوظ کرے گی۔

> [!WARNING]
> اپنی *.env* فائل کو ورژن کنٹرول سسٹمز جیسے Git میں شامل نہ کریں۔ غلطی سے کمیٹ کرنے سے بچنے کے لیے *.env* کو اپنی .gitignore فائل میں شامل کریں۔

1. اپنے پروجیکٹ کی روٹ ڈائریکٹری پر جائیں۔

1. پروجیکٹ کی روٹ ڈائریکٹری میں ایک *.env* فائل بنائیں۔

1. *.env* فائل کھولیں اور درج ذیل ٹیمپلیٹ پیسٹ کریں:

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
> اگر آپ کو اپنی API کیز اور اینڈپوائنٹس تلاش کرنے ہوں تو آپ [set-up-azure-ai.md](../set-up-azure-ai.md) کا حوالہ دے سکتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**اخطار**:  
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم ذہن میں رکھیں کہ خودکار تراجم میں غلطیاں یا عدم درستیاں ہوسکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ماخذ تصور کی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہم پر نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->