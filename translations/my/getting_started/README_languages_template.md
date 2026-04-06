# 🌐 မျိုးစုံဘာသာစကားပံ့ပိုးမှု (Template)

ပြုပြင်ထိန်းသိမ်းသူများ: အောက်တွင်ဖော်ပြထားသည်မှာ Co-op Translator မှ စီမံခန့်ခွဲသော "ဘာသာစကားအားလုံး" ဥပမာဖြစ် ပါသည်။

- သင်သည် Co-op Translator ကို `translate` ကိုယ်တိုင် run လုပ်သောအခါ (ဘာသာစကားရွေးချယ်မှု မည်မျှဖြစ်ပါစေ) ဤစာရင်းကို အပြည့်အစုံအလိုအလျောက်နောက်ဆုံးထိန်းသိမ်းဖို့လိုပါက အဆိုပါ comment marker နှစ်ခုကို မပြောင်းလဲဘဲထားရှိပါ။
- သင်သည် ဘာသာစကားတချို့သာ ပြသချင်ပါက comment marker နှစ်ခုကို ဖျက်ပြီး မလိုအပ်သော ဘာသာစကားများကို ဖယ်ရှားပါ။ marker များဖျက်ပြီးနောက် Co-op Translator သည် ဤအပိုင်းကို အလိုအလျောက် အစားထိုးမည် မဟုတ်တော့ပါ။

- ယခု အပိုင်းတွင် "တိုက်ရိုက် Clone လုပ်ရန် စိတ်ဝင်စားပါသလား?" ဟူသော အကြံပြုချက်ပါရှိပြီး အသုံးပြုသူများအား ဘာသာပြန်ဆို စာရွက်များ ပါဝင်မှု ကြီးမားမှုမရှိဘဲ clone လုပ်ရန် ကူညီပေးပါသည်။ သင်၏ repository URL ဖြင့် ကိုယ်ပိုင်လုပ်ဆောင်လိုပါက ဥပမာအားဖြင့် အောက်ပါအတိုင်း ပြုလုပ်နိုင်ပါသည်။
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](./README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**စာကြောင်းတောင်းပန်ချက်**:  
ဤစာတမ်းကို AI ဘာသာပြန် خدمت [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားခြင်းဖြစ်သည်။ ကျနော်တို့သည် တိကျမှုအတွက် ကြိုးစားပေမယ့်၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါရှိနိုင်ပါသဖြင့် သတိပြုပါရန် လိုအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ ယုံကြည်အပ်ပါသည်။ အရေးပါသော သတင်းအချက်အလက်များအတွက် ဆရာ/မသူများဖြင့် လက်မှတ်ရ လူအာရုံဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်နိုင်သည့် လွဲမှားမှုများ သို့မဟုတ် မှားနားစွာဖော်ပြမှုများအတွက် ကျွန်ုပ်တို့၏ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->