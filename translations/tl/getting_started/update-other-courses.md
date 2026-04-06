# I-update ang seksyon na "Other Courses" (Microsoft Beginners repos)

Ipinaliwanag ng gabay na ito kung paano gawing auto‑synchronize ang seksyon na "Other Courses" gamit ang Co‑op Translator, at kung paano i-update ang global template para sa lahat ng repos.

- Nag-aaplay sa: Microsoft Beginners repositories lamang
- Gumagana sa: Co‑op Translator CLI at GitHub Actions
- Pinagmulan ng template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mabilisang pagsisimula: Paganahin ang auto‑sync sa iyong repo

Idagdag ang mga sumusunod na marker sa paligid ng seksyon na "Other Courses" sa iyong README. Papalitan ng Co‑op Translator ang lahat ng nasa pagitan ng mga marker na ito sa bawat takbo.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Sa bawat takbo ng Co‑op Translator—sa pamamagitan ng CLI (hal., `translate -l "<language codes>"`) o GitHub Actions—awtomatiko nitong ina-update ang seksyon na "Other Courses" na nakabalot sa mga marker na ito.

> [!NOTE]
> Kung mayroon ka nang umiiral na listahan, balutin lang ito gamit ang parehong mga marker. Papalitan ito sa susunod na takbo ng pinakabagong standardized na nilalaman.

---

## Paano baguhin ang global na nilalaman

Kung nais mong i-update ang standardized na nilalaman na lumalabas sa lahat ng Beginners repos:

1. I-edit ang template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Magbukas ng pull request sa Co-op Translator repo kasama ang iyong mga pagbabago
3. Pagkatapos ma-merge ang PR, mai-update ang bersyon ng Co‑op Translator
4. Sa susunod na takbo ng Co‑op Translator (CLI o GitHub Action) sa target na repo, awtomatiko nitong i-synchronize ang na-update na seksyon

Tinitiyak nito ang isang pinag-isang pinanggagalingan ng katotohanan para sa nilalaman ng "Other Courses" sa lahat ng Beginners repositories.


## Sukat ng Repo

Maaaring lumaki ang mga repo dahil sa dami ng mga isinaling wika upang matulungan ang mga end user na magkaroon ng gabay kung paano gamitin ang clone - sparse upang mag-clone lamang ng mga kinakailangang wika at hindi ang buong repo

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
**Pagsasabi ng Paunawa**:  
Ang dokumentong ito ay naisalin gamit ang serbisyong AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-katumpakan. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon mula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->