# ရှေ့နေ ဒါရိုက်တောရီမှာ *.env* ဖိုင် ဖန်တီးခြင်း

ဒီသင်ခန်းစာမှာ Azure ဝန်ဆောင်မှုများအတွက် သင့်ပတ်ဝန်းကျင် အပြောင်းအလဲများကို *.env* ဖိုင် အသုံးပြု၍ စီမံခန့်ခွဲနည်းကို လမ်းညွှန်ပေးသွားပါမယ်။ ပတ်ဝန်းကျင် အပြောင်းအလဲများက API key တွေလို အလွန်လျှို့ဝှက်တဲ့ အချက်အလက်များကို သင့်ကုဒ်အပိုင်းထဲမှာ တိုက်ရိုက်ထည့်ခြင်းမရှိဘဲ ဘေးကင်းသေချာစွာ စီမံခန့်ခွဲနိုင်စေပါတယ်။

> [!IMPORTANT]
> - ဘာသာစကားမော်ဒယ်ဝန်ဆောင်မှုတစ်ခု (Azure OpenAI သို့မဟုတ် OpenAI) ပဲ သတ်မှတ်ရန် လိုအပ်ပါသည်။ သင်ကြိုက်နှစ်သက်သော ဝန်ဆောင်မှုအတွက် ပတ်ဝန်းကျင် အပြောင်းအလဲများကို ဖြည့်စွက်ပါ။ ဘာသာစကားမော်ဒယ်များအတွက် ပတ်ဝန်းကျင် အပြောင်းအလဲများ အများကြီး ထည့်ထားပါက co-op translator က ဦးစားပေးချက်အရ တစ်ခုကို ရွေးချယ်ပါလိမ့်မယ်။
> - Computer Vision ပတ်ဝန်းကျင် အပြောင်းအလဲများ မဖြည့်သွင်းထားပါက ဘာသာပြန်မှာ အလိုအလျောက် [Markdown-only mode](./markdown-only-mode.md) သို့ ပြောင်းသွားပါလိမ့်မယ်။

> [!NOTE]
> ဤလမ်းညွှန်မှာ အဓိကအားဖြင့် Azure ဝန်ဆောင်မှုများကို အခြေခံထားသော်လည်း [supported models and services list](../README.md#-supported-models-and-services) မှ ထောက်ခံထားသော ဘာသာစကားမော်ဒယ် မည်သည့်အရောင်းအဝယ်ကိုမဆို ရွေးချယ်အသုံးပြုနိုင်ပါသည်။

## *.env* ဖိုင် ဖန်တီးခြင်း

သင့်ပရောဂျက် ရှေ့နေ ဒါရိုက်တောရီတွင် *.env* ဟု အမည်ပေး၍ ဖိုင်တစ်ဖိုင် ဖန်တီးပါ။ ဤဖိုင်သည် သင့်ပတ်ဝန်းကျင် အပြောင်းအလဲများအားလုံးကို ရိုးရှင်းသော ပုံစံဖြင့် သိမ်းဆည်းပေးပါလိမ့်မယ်။

> [!WARNING]
> *.env* ဖိုင်ကို Git ကဲ့သို့သော ဗားရှင်းထိန်းချုပ်မှု စနစ်များတွင် commit မလုပ်ရ။ စကတ်အမှား commit မဖြစ်အောင် *.env* ကို သင့် .gitignore ဖိုင်ထဲ ထည့်သွင်းပါ။

1. သင့်ပရောဂျက် ရှေ့နေ ဒါရိုက်တောရီသို့ သွားပါ။

1. သင့်ပရောဂျက် ရှေ့နေ ဒါရိုက်တောရီတွင် *.env* ဖိုင်ကို ဖန်တီးပါ။

1. *.env* ဖိုင်ကို ဖွင့်ပြီး အောက်ပါ ပုံစံကို ကူးထည့်ပါ-

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
> သင့် API key များနှင့် endpoints ကို ရှာဖွေနိုင်ရန် [set-up-azure-ai.md](../set-up-azure-ai.md) ကို ရှာဖတ်နိုင်ပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အတည်ပြုချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်တော်တို့မှာ တိကျမှုအတွက် ကြိုးစားနေသော်လည်း အလိုအလျောက် ဘာသာပြန်ချက်များတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ရှိနိုင်ကြောင်း အသိပေးလိုပါသည်။ မူရင်းစာတမ်းသည် မိမိဘာသာစကားဖြင့် ရေးသားထားသော စံနှုန်းဆိုင်ရာ အချက်အလက်ရင်းမြစ်ဟု သတ်မှတ်သင့်သည်။ အရေးကြီးသော အချက်အလက်များအတွက်တော့ လူကြီးမင်းတို့သည် ပရော်ဖက်ရှင်နယ်လူသားဘာသာပြန်ကို အသုံးပြုရန် အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသည့် စိတ် မမှန်ခြင်း သို့မဟုတ် မှားယွင်းပုံဖော်ခြင်းတို့အတွက် ကျွန်တော်တို့ ဝန်ခံမှု မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->