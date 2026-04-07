# Co-op Translator کے لیے Azure AI سیٹ اپ کریں (Azure OpneAI اور Azure AI Vision)

یہ گائیڈ آپ کو Azure AI Foundry کے اندر زبان کی ترجمہ کے لیے Azure OpenAI اور تصویر کے مواد کے تجزیے کے لیے Azure Computer Vision کو سیٹ اپ کرنے کے مراحل سے گزارتا ہے (جسے بعد میں تصویر کی بنیاد پر ترجمہ کے لیے استعمال کیا جا سکتا ہے)۔

**ضروریات:**
- ایک Azure اکاؤنٹ جس کی سبسکرپشن فعال ہو۔
- Azure سبسکرپشن میں وسائل اور ڈیپلائمنٹ بنانے کی مناسب اجازتیں۔

## ایک Azure AI پروجیکٹ بنائیں

آپ ایک Azure AI پروجیکٹ بنانے سے شروع کریں گے، جو آپ کے AI وسائل کو منظم کرنے کے لیے ایک مرکزی جگہ کے طور پر کام کرتا ہے۔

1. [https://ai.azure.com](https://ai.azure.com) پر جائیں اور اپنے Azure اکاؤنٹ سے سائن ان کریں۔

1. نیا پروجیکٹ بنانے کے لیے **+Create** منتخب کریں۔

1. درج ذیل کام انجام دیں:
   - ایک **Project name** درج کریں (مثلاً `CoopTranslator-Project`)۔
   - **AI hub** منتخب کریں (مثلاً `CoopTranslator-Hub`) (اگر ضرورت ہو تو نیا بنائیں)۔

1. اپنا پروجیکٹ سیٹ اپ کرنے کے لیے "**Review and Create**" پر کلک کریں۔ آپ کو اپنے پروجیکٹ کے اوورویو صفحے پر لے جایا جائے گا۔

## زبان کے ترجمہ کے لیے Azure OpenAI سیٹ اپ کریں

اپنے پروجیکٹ میں، آپ ایک Azure OpenAI ماڈل ڈیپلائے کریں گے تاکہ ٹیکسٹ ترجمے کے لیے بیک اینڈ کے طور پر کام کرے۔

### اپنے پروجیکٹ پر جائیں

اگر پہلے سے نہیں ہیں تو، اپنے نئے بنائے ہوئے پروجیکٹ (مثلاً `CoopTranslator-Project`) کو Azure AI Foundry میں کھولیں۔

### OpenAI ماڈل ڈیپلائے کریں

1. اپنے پروجیکٹ کے بائیں مینو میں، "My assets" کے تحت، "**Models + endpoints**" منتخب کریں۔

1. **+ Deploy model** منتخب کریں۔

1. **Deploy Base Model** منتخب کریں۔

1. دستیاب ماڈلز کی فہرست آپ کے سامنے آئے گی۔ ایک مناسب GPT ماڈل تلاش کریں یا فلٹر کریں۔ ہم `gpt-4o` کی سفارش کرتے ہیں۔

1. مطلوبہ ماڈل منتخب کریں اور **Confirm** پر کلک کریں۔

1. **Deploy** منتخب کریں۔

### Azure OpenAI کنفیگریشن

ڈیپلائمنٹ کے بعد، آپ "**Models + endpoints**" صفحے سے اس کی **REST endpoint URL**، **Key**، **Deployment name**، **Model name** اور **API version** حاصل کر سکتے ہیں۔ ان کی ضرورت آپ کی ایپلیکیشن میں ترجمہ ماڈل کو ضم کرنے کے لیے ہوگی۔

> [!NOTE]
> آپ اپنی ضروریات کے مطابق [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) صفحے سے API ورژن منتخب کر سکتے ہیں۔ جان لیں کہ **API version** Azure AI Foundry میں "**Models + endpoints**" صفحے پر دکھائے گئے **Model version** سے مختلف ہوتا ہے۔

## تصویر کے ترجمہ کے لیے Azure Computer Vision سیٹ اپ کریں

تصاویر میں موجود ٹیکسٹ کے ترجمہ کو فعال کرنے کے لیے، آپ کو Azure AI Service API Key اور Endpoint تلاش کرنے کی ضرورت ہے۔

1. اپنے Azure AI پروجیکٹ (مثلاً `CoopTranslator-Project`) پر جائیں۔ یقینی بنائیں کہ آپ پروجیکٹ کے اوورویو صفحے پر ہیں۔

### Azure AI Service کنفیگریشن

Azure AI Service سے API Key اور Endpoint حاصل کریں۔

1. اپنے Azure AI پروجیکٹ (مثلاً `CoopTranslator-Project`) پر جائیں۔ یقینی بنائیں کہ آپ پروجیکٹ کے اوورویو صفحے پر ہیں۔

1. Azure AI Service کے ٹیب سے **API Key** اور **Endpoint** تلاش کریں۔

    ![API Key اور Endpoint تلاش کریں](../../../getting_started/imgs/find-azure-ai-info.png)

یہ کنکشن جڑے ہوئے Azure AI Services ریسورس کی صلاحیتوں (بشمول تصویر کے تجزیے) کو آپ کے AI Foundry پروجیکٹ کے لیے دستیاب بناتا ہے۔ آپ اس کنکشن کو اپنے نوٹ بکس یا ایپلیکیشنز میں استعمال کر کے تصاویر سے متن نکال سکتے ہیں، جسے بعد میں ترجمہ کے لیے Azure OpenAI ماڈل کو بھیجا جا سکتا ہے۔

## اپنے اسناد کو مضبوط کرنا

اب تک، آپ نے درج ذیل جمع کر لیے ہوں گے:

**Azure OpenAI (ٹیکسٹ ترجمہ) کے لیے:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (مثلاً `gpt-4o`)
- Azure OpenAI Deployment Name (مثلاً `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (ویژن کے ذریعے تصویر کے متن کا استخراج) کے لیے:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### مثال: ماحولیاتی متغیرات کی کنفیگریشن (پری ویو)

بعد میں، جب آپ اپنی ایپلیکیشن تیار کریں گے، تو آپ غالباً ان حاصل کردہ اسناد کو ماحولیاتی متغیرات کے طور پر ترتیب دیں گے، مثلاً:

```bash
# آزور اے آئی سروس کے اسناد (تصویر ترجمہ کے لیے ضروری)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # مثلاً، 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# اختیاری بیک اپ سیٹ: اضافی متغیرات کو لاحقہ _1/_2 کے ساتھ نقل کریں (سیٹ میں تمام متغیرات کے لیے ایک ہی انڈیکس)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# آزور اوپن اے آئی کے اسناد (متن ترجمہ کے لیے ضروری)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # مثلاً، 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # مثلاً، gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # مثلاً، cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # مثلاً، 2024-12-01-preview

# اختیاری بیک اپ سیٹ: پورے AZURE_OPENAI_* سیٹ کو لاحقہ _1/_2 کے ساتھ نقل کریں (تمام متغیرات کے لیے ایک ہی انڈیکس)
```

---

### مزید پڑھیں

- [Azure AI Foundry میں پروجیکٹ بنانے کا طریقہ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI ریسورس بنانے کا طریقہ](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry میں OpenAI ماڈلز کی تعیناتی کا طریقہ](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ڈسکلیمر**:  
اس دستاویز کا ترجمہ AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے کیا گیا ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم یہ بات ذہن میں رکھیں کہ خودکار ترجموں میں غلطیاں یا غیر یقینی عناصر ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں مستند ذریعہ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔
<!-- CO-OP TRANSLATOR DISCLAIMER END -->