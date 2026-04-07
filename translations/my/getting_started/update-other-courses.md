# "Other Courses" အပိုင်းကို အပ်ဒိတ်လုပ်ခြင်း (Microsoft Beginners repos)

ဤလမ်းညွှန်သည် Co-op Translator ကို အသုံးပြုပြီး "Other Courses" အပိုင်းကို အလိုအလျောက် စနစ်တကျ ထပ်တလဲလဲလုပ်ရန်နည်းလမ်းနှင့်၊ မူလပုံစံကို အားလုံးသော repos များအတွက် မည်သို့ အပ်ဒိတ်လုပ်ရမည်ကို ရှင်းပြသည်။

- သက်ဆိုင်ရာ: Microsoft Beginners repositories များသာ
- အသုံးပြုပုံ: Co-op Translator CLI နှင့် GitHub Actions တို့နှင့်အတူ
- မူပိုင်ပုံစံ ရင်းမြစ်: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## လျင်မြန်စွာ စတင်ရန်: သင့် repo တွင် auto-sync ကို စတင်ဖွင့်ပါ

သင့် README အတွင်းရှိ "Other Courses" အပိုင်းနားတွင် အောက်ပါ မာကာများကို ထည့်သွင်းပါ။ Co-op Translator သည် မာကာများအကြားရှိ အရာအားလုံးကို run များတိုင်း တReplacement လုပ်ပေးပါမည်။

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co-op Translator သည် CLI (ဥပမာ `translate -l "<language codes>"`) သို့မဟုတ် GitHub Actions မှတစ်ဆင့် run လုပ်သောအခါတိုင်း၊ ဤမာကာများဖြင့် ထုပ်ပိုးထားသော "Other Courses" အပိုင်းကို အလိုအလျောက် အပ်ဒိတ်လုပ်ပေးပါသည်။

> [!NOTE]
> ပြီးခဲ့သောစာရင်းရှိပါကလည်း၊ အဲဒီလို မာကာများဖြင့် ထုပ်ပိုးပေးရန်သာလိုသည်။ နောက်တစ်ကြိမ် run လုပ်တိုင်း အဆင့်သစ် standardized အကြောင်းအရာဖြင့် အစားထိုးပေးမည်ဖြစ်သည်။

---

## မူလ အကြောင်းအရာ ကို မည်သို့ ပြောင်းလဲရမည်နည်း

Beginners repos အားလုံးတွင် ပြသဖို့ စံချိန်စံညွှန်းအကြောင်းအရာကို အပ်ဒိတ်လုပ်လိုပါက -

1. မူပိုင်ပုံစံကို ပြင်ဆင်ပါ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. သင့် ပြင်ဆင်မှုများဖြင့် Co-op Translator repo သို့ pull request တစ်ခု ဖွင့်ပါ
3. PR ပေါင်းသင်းပြီးနောက် Co-op Translator ဗားရှင်း ပဏာမ အပ်ဒိတ်လုပ်မည်
4. နောက်တစ်ကြိမ် Co-op Translator run (CLI သို့မဟုတ် GitHub Action) တည်ဆဲ repo တွင် auto-sync လုပ်ပေးမည်ဖြစ်သည်။

ဤနည်းပုံသည် Beginners repositories အားလုံးတွင် "Other Courses" အကြောင်းအရာအတွက် တစ်ခုတည်းသော မှန်ကန်သော အချက်အလက် ရရှိစေပါသည်။


## Repo အရွယ်အစားများ

လူအများဆုံးဘာသာစကားပြန်ထားမှုကြောင့် repo များသည် အရွယ်အစားကြီးလာနိုင်ပါသည်။ ဒါကြောင့် အသုံးပြုသူများအား လိုအပ်သောဘာသာစကားများကိုသာ clone - sparse ဖြင့် scope သတ်မှတ်ကာ မရိုးရိုး repo အားလုံးကို မယူရဘဲ အကူအညီပေးရန်ဒီအပိုင်းပါရှိသည်။

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**အသိပေးချက်**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်မှု ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားပေမယ့် စက်မှ ပြုလုပ်သောဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှန်ကန်မှုမရှိမှုများ ပါဝင်နိုင်သဖြင့် မူရင်းစာရွက်စာတမ်းကိုသာ တရားဝင်အာမခံနိုင်သောအရင်းအမြစ်အဖြစ်သတ်မှတ်ပါရန် အသိပေးအပ်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူမှုဘက် အရည်အချင်းရှိ ဘာသာပြန်သူမှ ပြန်ဆိုခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖော်ပြမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->