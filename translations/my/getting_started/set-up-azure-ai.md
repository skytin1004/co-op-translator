# Set Up Azure AI for Co-op Translator (Azure OpneAI & Azure AI Vision)

ဤလမ်းညွှန်ချက်သည် Azure AI Foundry အတွင်းတွင် ဘာသာပြန်ခြင်းအတွက် Azure OpenAI နှင့် ပုံရိပ်အကြောင်းအရာများအား စိစစ်သုံးသပ်ခြင်းအတွက် Azure Computer Vision ကို စတင်တပ်ဆင်ခြင်းကို အဆင့်ဆင့် ဦးတည်ရှင်းလင်းပေးသည် (ထို့နောက် ပုံရိပ်ပေါ်မှ ဘာသာပြန်ခြင်းအတွက် အသုံးပြုနိုင်သည်)။

**လိုအပ်ချက်များ:**
- လုပ်ငန်းလည်ပတ်နေသော subscription နှင့် Azure အကောင့်တစ်ခု။
- သင်၏ Azure subscription တွင် အရင်းအမြစ်များနှင့် တပ်ဆင်ခြင်းများ ဖန်တီးရန် လုံလောက်သော ခွင့်ပြုချက်များ။

## Azure AI Project တစ်ခု ဖန်တီးပါ

သင်၏ AI အရင်းအမြစ်များကို စီမံခန့်ခွဲရန် အလယ်ဗဟိုနေရာအဖြစ် အလုပ်လုပ်သည့် Azure AI Project တစ်ခု ဖန်တီးရန် စတင်ပါမည်။

1. [https://ai.azure.com](https://ai.azure.com) သို့ သွား၍ သင့် Azure အကောင့်ဖြင့် စာရင်းဝင်ပါ။

1. **+Create** ကို နှိပ်၍ ပရောဂျက်အသစ်တစ်ခု ဖန်တီးပါ။

1. အောက်ပါ အချက်များကို ပြုလုပ်ပါ-
   - **Project name** ထည့်ပါ (ဥပမာ - `CoopTranslator-Project`)။
   - **AI hub** ကို ရွေးပါ (ဥပမာ - `CoopTranslator-Hub`) (လိုအပ်ပါက အသစ်ဖန်တီးနိုင်သည်)။

1. **Review and Create** ကို နှိပ်၍ သင့်ပရောဂျက်ကို တပ်ဆင်ပါ။ သင်သည် သင့်ပရောဂျက်ရဲ့ အကြောင်းအရာ စာမျက်နှာသို့ ဦးစားပေးတက်သွားပါမည်။

## ဘာသာပြန်ခြင်းအတွက် Azure OpenAI ကို တပ်ဆင်ပါ

သင့်ပရောဂျက်အတွင်းတွင် စာသားဘာသာပြန်ရန် အနောက်ခံအဖြစ် ဆောင်ရွက်မည့် Azure OpenAI မော်ဒယ်တစ်ခု တပ်ဆင်ပါမည်။

### သင့်ပရောဂျက်သို့ သွားပါ

မဖြစ်သေးပါက Azure AI Foundry တွင် သင့်အသစ်ဖန်တီးသော ပရောဂျက် (ဥပမာ - `CoopTranslator-Project`) ကိုဖွင့်ပါ။

### OpenAI Model တပ်ဆင်ခြင်း

1. သင့်ပရောဂျက်၏ ဘယ်ဘက်မီနူးထဲမှ "My assets" အောက် "Models + endpoints" ကို ရွေးချယ်ပါ။

1. **+ Deploy model** ကို ရွေးချယ်ပါ။

1. **Deploy Base Model** ကို ရွေးချယ်ပါ။

1. ရနိုင်သည့် မော်ဒယ်များစာရင်းကို မြင်ရမည်။ သင့်လိုအပ်ချက်နှင့် ကိုက်ညီသော GPT မော်ဒယ်ကို ရှာဖွေ သို့မဟုတ် သတ်မှတ်ပါ။ `gpt-4o` ကို အကြံပြုပါသည်။

1. သင့်လိုချင်သော မော်ဒယ်ကို ရွေးချယ်ပြီး **Confirm** ကို နှိပ်ပါ။

1. **Deploy** ကို နှိပ်ပါ။

### Azure OpenAI ကို ဖန်တီးသတ်မှတ်ခြင်း

တပ်ဆင်ပြီးနောက်၊ "**Models + endpoints**" စာမျက်နှာမှ တပ်ဆင်မှုကို ရွေးပြီး ၎င်း၏ **REST endpoint URL**, **Key**, **Deployment name**, **Model name** နှင့် **API version** ကို ရယူနိုင်သည်။ ဤအချက်အလက်များသည် သင်၏လျော်နာတ် အပလီကေးရှင်းဖြင့် ဘာသာပြန်ခြင်းမော်ဒယ်ကို ပေါင်းစည်းရာတွင် လိုအပ်မည်ဖြစ်သည်။

> [!NOTE]
> သင်၏လိုအပ်ချက်အပေါ် မူတည်၍ [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) စာမျက်နှာမှ API ဗားရှင်းများကို ရွေးချယ်နိုင်သည်။ Azure AI Foundry ၏ **Models + endpoints** စာမျက်နှာ၌ ပြသထားသည့် **Model version** နှင့် **API version** သည် ကွာခြားကြောင်း သတိပြုပါ။

## ပုံပြင်ဘာသာပြန်ခြင်းအတွက် Azure Computer Vision အတွက် တပ်ဆင်ပါ

ပုံရိပ်များအတွင်း စာသားကို ဘာသာပြန်ရန်အတွက် Azure AI Service ၏ API Key နှင့် Endpoint ကို ရှာတွေ့ရမည်ဖြစ်သည်။

1. သင့် Azure AI Project (ဥပမာ - `CoopTranslator-Project`) သို့ သွားပါ။ ပရောဂျက်အကြာင္းအရာ စာမျက်နှာတွင်ရှိနေပြီးကြောင်းသေချာပါစေ။

### Azure AI Service ကို တပ်ဆင်သတ်မှတ်ခြင်း

Azure AI Service မှ API Key နှင့် Endpoint ကို ရှာဖွေပါ။

1. သင့် Azure AI Project (ဥပမာ - `CoopTranslator-Project`) သို့ သွားဖြစ်ပြီး ပရောဂျက်အကြောင်းအရာ စာမျက်နှာ၌ ရှိနေပါပြီကို သေချာစေပါ။

1. Azure AI Service တစ်ခု မှ **API Key** နှင့် **Endpoint** ကို ရှာဖွေပါ။

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ဤဆက်သွယ်မှုသည် ချိတ်ဆက်ထားသော Azure AI Services အရင်းအမြစ်၏ လုပ်ဆောင်ချက်များ (ပုံစစ်ဆေးခြင်းအပါအဝင်) ကို သင့် AI Foundry ပရောဂျက်တွင် အသုံးပြုနိုင်စေသည်။ ထို့နောက် သင်၏ notebooks သို့မဟုတ် အပလီကေးရှင်းများတွင် ဤဆက်သွယ်မှုကို အသုံးပြု၍ ပုံများမှ စာသားကို ထုတ်ယူနိုင်သည်။ ထိုစာသားကို နောက်ထပ် ဘာသာပြန်ရန်အတွက် Azure OpenAI မော်ဒယ်သို့ ပို့ပို်နိုင်သည်။

## သင့်လက်မှတ်များကို စုစည်းခြင်း

ယခုအချိန်အထိ သင်စုဆောင်းထားသင့်သည် -

**Azure OpenAI (စာသားဘာသာပြန်မှု) အတွက်:**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Azure OpenAI Model Name (ဥပမာ - `gpt-4o`)
- Azure OpenAI Deployment Name (ဥပမာ - `cooptranslator-gpt4o`)
- Azure OpenAI API Version

**Azure AI Services (Vision ဖြင့် ပုံစာသားထုတ်ယူမှု) အတွက်:**
- Azure AI Service Endpoint
- Azure AI Service API Key

### ဥပမာ - ပတ်ဝန်းကျင်အပြောင်းအလဲ ဖန်တီးခြင်း (ကြိုတင်ကြည့်ရှုမှု)

နောက်ပိုင်းသင်၏ အပလီကေးရှင်းတစ်ခု ဆောက်လုပ်ရာတွင် ယူဆရပါသည်၊ သင် စုဆောင်းထားသည့် သက်ဆိုင်ရာ လက်မှတ်များဖြင့် ဤအတိုင်း ပတ်ဝန်းကျင်အပြောင်းအလဲများ ကို သတ်မှတ်နိုင်သည်။

```bash
# Azure AI ဝန်ဆောင်မှု အတည်ပြုချက်များ (ရုပ်ပုံဘာသာပြန်ရန် လိုအပ်သည်)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ဥပမာ၊ 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ရွေးချယ်စရာ မဟုတ်မဖြစ် စုံများ - _1/_2 ဖြင့် တူညီသော အညွှန်းနှင့်ကူးယူသည့် အရေအတွက်များ
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI အတည်ပြုချက်များ (စာသားဘာသာပြန်ရန် လိုအပ်သည်)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ဥပမာ၊ 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ဥပမာ၊ gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ဥပမာ၊ cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ဥပမာ၊ 2024-12-01-preview

# ရွေးချယ်စရာ မဟုတ်မဖြစ် စုံများ - အပြည့်အစုံ AZURE_OPENAI_* အစုအစည်းကို _1/_2 ဖြင့် ကူးယူခြင်း (အညွှန်းတူညီသော အပြောင်းအလဲများ)
```

---

### နောက်ထပ်ဖတ်ရန်

- [How to Create a project in Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [How to Create Azure AI resources](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [How to Deploy OpenAI models in Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ပယ်ချခြင်း**။  
ဤစာတမ်းကို AI ဘာသာပြန်မှု ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းထားသော်လည်း၊ အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားအယွင်း သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါ။ မူလစာတမ်းကို အသုံးပြုနိုင်သော ကိုယ်ပိုင်ဘာသာစကားဖြင့်သာ တရားဝင်နှင့်အတည်ပြုရမည့် အရင်းအမြစ်အနေဖြင့် ကြည့်ရန်လိုအပ်ပါသည်။ အရေးကြီးသောသတင်းအချက်အလက်များအတွက် လူမှုထိတွေ့ဘဝမှ ဘာသာပြန်သူ လုပ်ငန်းအတွေ့အကြုံရှိသူအား တိုက်တွန်းပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့်ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှု မှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့မှာ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->