# "Other Courses" ဌာနကို အပ်ဒိတ်လုပ်ပါ (Microsoft Beginners repos)

ဤလမ်းညွှန်သည် "Other Courses" ဌာနကို Co‑op Translator ဖြင့် အော်တို-စင့်တင်စနစ်ဖြင့် synchronize လုပ်မည်၊ နှင့် အားလုံးသော repos များအတွက် global template ကို မည်သို့အပ်ဒိတ်လုပ်မည်ကို ရှင်းပြသည်။

- သက်ဆိုင်မှု: Microsoft Beginners repositories သာ
- အသုံးပြုမှု: Co‑op Translator CLI နှင့် GitHub Actions နှင့်အတူ
- Template များရင်းမြစ်: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## အမြန်စတင်ခြင်း: သင့် repo တွင် auto-sync ကို ဖွင့်ပါ

သင့် README တွင် "Other Courses" ဌာနအနားတွင် အောက်ပါ markers များထည့်ပါ။ Co‑op Translator သည် အဆိုပါ markers များအကြားရှိ အရာအားလုံးကို run တစ်ကြိမ်တိုင်းတွင် အစားထိုးမည်ဖြစ်သည်။

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator run တိုင်တိုင်း (CLI ဖြင့် `translate -l "<language codes>"` သို့မဟုတ် GitHub Actions မှတစ်ဆင့်) သည် ဒီ markers များဖြင့် ပတ်ဝန်းကျင် သတ်မှတ်ထားသော "Other Courses" ဌာနကို အလိုအလျောက် update လုပ်ပေးလိမ့်မည်။

> [!NOTE]
> သင်မှာ ရှိပြီးသားစာရင်းရှိပါက၊ အဲဒီစာရင်းကို အတူတူ markers များဖြင့်သာ ဝတ်စားပါ။ နောက်တစ်ကြိမ် run တစ်ခါမှာ မူလစာရင်းကို နောက်ဆုံးပေါ်စံနှုန်းစာချုပ်ဖြင့် အစားထိုးပေးလိမ့်မည်။

---

## Global content ကို မည်သို့ပြောင်းလဲမည်လဲ

Beginners repos အားလုံးတွင် ပြသမည့် စံနှုန်းကောင်း content ကို အပ်ဒိတ်လုပ်လိုပါက -

1. Template ကို ဘာသာပြန်ပါ - [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ပြင်ဆင်မှုများဖြင့် Co-op Translator repo သို့ pull request တစ်ခု ဖွင့်ပါ
3. PR ပေါင်းသင်းပြီးနောက် Co‑op Translator ဗားရှင်းကို အပ်ဒိတ်လုပ်မည်
4. နောက်တစ်ကြိမ် Co‑op Translator (CLI သို့မဟုတ် GitHub Action) run မည့် target repo တွင် ပြင်ဆင်ချက်များ ပါဝင်သော အပိုင်းကို အလိုအလျောက် sync လုပ်ပေးမည်

ဒီလိုဖြင့် "Other Courses" content အတွက် Beginners repo အားလုံးတွင် တစ်ခုတည်းသော အချက်အလက် ရင်းမြစ်တစ်ခု ရရှိစေပါသည်။

## Repo စာမူအရွယ်အစားများ

ဘာသာစကားများ များပြားစွာ ဘာသာပြန်ပေးထားသောကြောင့် repo တွေ များကြီးလာနိုင်ပြီး အသုံးပြုသူများ Clone - Sparse ကို အသုံးပြု၍ လိုအပ်သော ဘာသာစကားများကိုသာ Clone လုပ်ပြီး အားလုံးကို မလိုအပ်ပဲ အသုံးပြုနိုင်ရန် လမ်းညွှန်ချက်ပေးရန် ရည်ရွယ်ပါသည်။

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
**တာဝန်မခံခြင်း**:  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) အသုံးပြု၍ ဘာသာပြန်ထားသည်။ ကျွန်ုပ်တို့သည် မှန်ကန်မှုအတွက် ကြိုးစားပေမယ့် အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် ဖိတ်ခေါ်ပါသည်။ မူရင်းစာရွက်စာတမ်းသည် ၎င်း၏မူလဘာသာဖြင့် တရားဝင်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်သည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ပရော်ဖက်ရှင်နယ် ဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှု အသုံးပြုမှုမှ ဖြစ်ပေါ်လာသော နားလည်မှုမှားယွင်းမှုများ အတွက် ကျွန်ုပ်တို့သည် တာဝန်မခံပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->