# I-update ang seksyong "Iba Pang Mga Kurso" (Microsoft Beginners repos)

Ipinaliwanag sa gabay na ito kung paano gawing awtomatikong nag‑synchronize ang seksyong "Iba Pang Mga Kurso" gamit ang Co‑op Translator, at kung paano i-update ang global template para sa lahat ng repos.

- Saklaw: Para lamang sa Microsoft Beginners repositories
- Gumagana sa: Co‑op Translator CLI at GitHub Actions
- Pinagmulan ng template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Mabilis na pagsisimula: Paganahin ang auto‑sync sa iyong repo

Idagdag ang mga sumusunod na marker sa paligid ng seksyong "Iba Pang Mga Kurso" sa iyong README. Papalitan ng Co‑op Translator ang lahat ng nasa pagitan ng mga marker na ito sa bawat pagtakbo.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Sa bawat pagtakbo ng Co‑op Translator—gamit ang CLI (hal., `translate -l "<language codes>"`) o GitHub Actions—awtomatiko nitong ina-update ang seksyong "Iba Pang Mga Kurso" na nakapaloob sa mga markang ito.

> [!NOTE]
> Kung mayroon ka nang umiiral na listahan, balutin mo lang ito gamit ang parehong mga marker. Papalitan ito ng susunod na pagtakbo gamit ang pinakabagong standardized na nilalaman.

---

## Paano baguhin ang global na nilalaman

Kung nais mong i-update ang standardized na nilalaman na lumalabas sa lahat ng Beginners repos:

1. I-edit ang template: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Magbukas ng pull request sa Co-op Translator repo kasama ang iyong mga pagbabago
3. Kapag na-merge na ang PR, ia-update ang bersyon ng Co‑op Translator
4. Sa susunod na pagtakbo ng Co‑op Translator (CLI o GitHub Action) sa target na repo, awtomatiko nitong isi-sync ang na-update na seksyon

Tinitiyak nito ang isang pinag-isang source of truth para sa nilalaman ng "Iba Pang Mga Kurso" sa lahat ng Beginners repositories.


## Sukat ng Repo

Maaaring lumaki ang mga repo dahil sa dami ng mga isinaling wika upang makatulong sa mga end user na magbigay ng gabay kung paano gamitin ang clone - sparse upang i-clone lamang ang mga kinakailangang wika at hindi ang buong repo

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
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat pinagsisikapan naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaintindihan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->