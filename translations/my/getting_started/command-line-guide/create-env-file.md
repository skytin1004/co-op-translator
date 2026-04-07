# Root directory တွင် *.env* ဖိုင်ကိုဖန်တီးပါ

ဤသင်ခန်းစာတွင် Azure ဝန်ဆောင်မှုများအတွက် သင့်ရဲ့ ပတ်ဝန်းကျင် အပြောင်းအလဲများကို *.env* ဖိုင်ဖြင့် စီမံရန် လမ်းညွှန်ပေးပါမည်။ ပတ်ဝန်းကျင် အပြောင်းအလဲများသည် API key များကဲ့သို့သော အချက်အလက် များကို မိမိကုဒ်အရင်းအမြစ်ထဲတွင် သန်းခြောက်ခြင်းမရှိပဲ လုံခြုံစွာ စီမံခန့်ခွဲနိုင်ရန်အတွက် အသုံးပြုသည်။

> [!IMPORTANT]
> - စာသားမော်ဒယ် ဝန်ဆောင်မှုတစ်ခု (Azure OpenAI သို့မဟုတ် OpenAI) သာ ကြိုတင်သတ်မှတ်ရန် လိုအပ်သည်။ သင်နှစ်သက်သော ဝန်ဆောင်မှုအတွက် ပတ်ဝန်းကျင်အပြောင်းအလဲများကို ဖြည့်စွက်ပါ။ စာသားမော်ဒယ်များစွာအတွက် ပတ်ဝန်းကျင်အပြောင်းအလဲများထည့်ထားပါက co-op translator သည် ဦးစားပေးမှုအပေါ် မူတည်၍ တစ်ခုကို ရွေးချယ်ပါလိမ့်မည်။
> - Computer Vision ပတ်ဝန်းကျင်အပြောင်းအလဲများ မသတ်မှတ်ထားပါက translator သည် သက်သေပြထားသော [Markdown-only mode](./markdown-only-mode.md)သို့ အလိုအလျောက် ပြောင်းရွှေ့ပါလိမ့်မည်။

> [!NOTE]
> ဤလမ်းညွှန်သည် အဓိကအားဖြင့် Azure ဝန်ဆောင်မှုများအပေါ် အာရုံစိုက်ပါသည်၊ သို့သော် သင်သည် [supported models and services list](../README.md#-supported-models-and-services) မှ ထောက်ခံသော မော်ဒယ်များကို မည်သည့်ဟုမဆို ရွေးချယ်နိုင်ပါသည်။

## *.env* ဖိုင်ကိုဖန်တီးပါ

သင့်ပရောဂျက်၏ root directory တွင် *.env* ဟု အမည်ရှိသော ဖိုင်ကို ဖန်တီးပါ။ ဤဖိုင်သည် သင်၏ ပတ်ဝန်းကျင်အပြောင်းအလဲများအားလုံးကို ရိုးရှင်းသော ဖော်မတ်ဖြင့် သိမ်းဆည်းပါမည်။

> [!WARNING]
> *.env* ဖိုင်ကို Git ကဲ့သို့သော ဗားရှင်းထိန်းချုပ်မှု စနစ်များထဲသို့ မသွင်းရန် သတိပြုပါ။ မတော်တဆပြုလုပ်မှုများမှ ကာကွယ်ရန် *.env* ကို .gitignore ဖိုင်တွင် ထည့်သွင်းထားပါ။

1. သင့္ပရောဂျက်၏ root directory သို့ သွားပါ။

1. သင့်ပရောဂျက်၏ root directory တွင် *.env* ဖိုင်ကို ဖန်တီးပါ။

1. *.env* ဖိုင်ကို ဖွင့်၍ အောက်ပါ မှန်ပုံကို မိတ္တူကူးထည့်ပါ။

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
> သင်၏ API keys နှင့် endpoints များကို ရှာဖွေလိုပါက [set-up-azure-ai.md](../set-up-azure-ai.md) ကို ကိုးကားနိုင်ပါသည်။

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အတည်မပြုချက်**၊  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့်ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည်တိကျမှန်ကန်မှုအတွက် ကြိုးစားပေမယ့်၊ စက်ရုပ်ဘာသာပြန်ခြင်းကြောင့် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်သည်ကို နားလည်ပေးပါရန် မေတ္တာရပ်ခံပါသည်။ မူရင်းစာတမ်းကို မိဖုရားဘာသာဖြင့်သာ တရားဝင်ကိုးကားအရင်းအမြစ်အဖြစ်ယူဆရမည် ဖြစ်ပါသည်။ အရေးကြီး သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်မှုကို အကြံပြုအပ်ပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုမှုမှ ဖြစ်ပေါ်လာနိုင်သည့် နားမလည်မှုများ သို့မဟုတ် မှားယူမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->