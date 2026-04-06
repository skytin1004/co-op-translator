Japanese mode: Markdown トークンを厳密に保持します。

ルール（必ず守ること）：
1) Markdown リンクは完全に保持： [text](../../../../../../src/co_op_translator/templates/language/URL) -> [translated text](../../../../../../src/co_op_translator/templates/language/同じ URL)。
2) リンクをプレーンテキスト（例：「text」（URL）, text (URL)）に書き換えない。
3) リンクのテキスト部分のみ翻訳し、Markdown 構造と URL は変更しない。
4) 外部リンクの文法上必要な場合を除き、Markdown リンクの周りに「」をつけない。

構造をスタイルより優先します。Markdown トークンが変わる場合は、日本語の自然さを最適化しないでください。

例
元文書: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**မှတ်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ တိကျမှန်ကန်မှုတိုးမြှင့်ရန်ကြိုးစားပေမယ့် အလိုအလျောက်ဘာသာပြန်ခြင်းအတွင်း အမှားများ သို့မဟုတ် တိကျမှုမရှိမှုများပါဝင်နိုင်ကြောင်း သိရှိထား၍ရပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ အတည်ပြုအရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက်တော့ လူ့ပညာရှင်များမှ လက်တွေ့ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက် အသုံးပြုရာမှ ဖြစ်ပေါ်လာသော နားလည်မှုကျရောက်မှုများ သို့မဟုတ် မှားယွင်းနားလည်မှုများအတွက် တာဝန်ယူရန် မဖြစ်ပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->