# جڑ ڈائریکٹری میں *.env* فائل بنائیں

اس ٹیوٹوریل میں، ہم آپ کو Azure سروسز کے لیے اپنے ماحول کے متغیرات کو *.env* فائل کے ذریعے سیٹ کرنے کی رہنمائی کریں گے۔ ماحول کے متغیرات آپ کو حساس اسناد جیسے API کیز کو محفوظ طریقے سے منظم کرنے کی اجازت دیتے ہیں، بغیر ان کو اپنے کوڈبیس میں ہارڈ کوڈ کیے۔

> [!IMPORTANT]
> - صرف ایک زبان ماڈل سروس (Azure OpenAI یا OpenAI) کو ترتیب دینا ضروری ہے۔ اپنی پسندیدہ سروس کے ماحول کے متغیرات درج کریں۔ اگر متعدد زبان ماڈلز کے ماحول کے متغیرات سیٹ کیے گئے ہیں تو، co-op translator ترجیح کی بنیاد پر ایک کا انتخاب کرے گا۔
> - اگر Computer Vision کے ماحول کے متغیرات سیٹ نہیں کیے گئے تو، translator خودبخود [صرف مارک ڈاؤن وضع](./markdown-only-mode.md) میں تبدیل ہو جائے گا۔

> [!NOTE]
> یہ رہنما بنیادی طور پر Azure سروسز پر مرکوز ہے، لیکن آپ [مقبول ماڈلز اور خدمات کی فہرست](../README.md#-supported-models-and-services) سے کوئی بھی معاون زبان ماڈل منتخب کر سکتے ہیں۔

## *.env* فائل بنائیں

اپنے پروجیکٹ کی جڑ ڈائریکٹری میں، *.env* نامی فائل بنائیں۔ یہ فائل آپ کے تمام ماحول کے متغیرات ایک سادہ فارمیٹ میں ذخیرہ کرے گی۔

> [!WARNING]
> اپنی *.env* فائل کو Git جیسے ورژن کنٹرول سسٹمز میں کامٹ نہ کریں۔ غلطی سے کامٹ ہونے سے بچنے کے لیے *.env* کو اپنی .gitignore فائل میں شامل کریں۔

1. اپنے پروجیکٹ کی جڑ ڈائریکٹری پر جائیں۔

1. پروجیکٹ کی جڑ ڈائریکٹری میں *.env* فائل بنائیں۔

1. *.env* فائل کو کھولیں اور درج ذیل ٹیمپلیٹ پیسٹ کریں:

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
> اگر آپ اپنی API کیز اور انڈ پوائنٹس تلاش کرنا چاہتے ہیں، تو آپ [set-up-azure-ai.md](../set-up-azure-ai.md) کا حوالہ دے سکتے ہیں۔

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**دِسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہِ کرم یہ بات ذہن میں رکھیں کہ خودکار تراجم میں غلطیاں یا بے قاعدگیاں ہوسکتی ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمہ کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوگی۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->