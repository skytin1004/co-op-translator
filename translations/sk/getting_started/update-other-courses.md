# Aktualizujte sekciu "Other Courses" (Microsoft Beginners repozitáre)

Tento sprievodca vysvetľuje, ako automaticky synchronizovať sekciu "Other Courses" pomocou Co‑op Translator a ako aktualizovať globálnu šablónu pre všetky repozitáre.

- Platí pre: iba Microsoft Beginners repozitáre
- Funguje s: Co‑op Translator CLI a GitHub Actions
- Zdroj šablóny: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rýchly štart: Povolenie automatickej synchronizácie vo vašom repozitári

Pridajte nasledujúce značky okolo sekcie "Other Courses" vo vašom README. Co‑op Translator nahradí všetko medzi týmito značkami pri každom spustení.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pri každom spustení Co‑op Translator – cez CLI (napr. `translate -l "<language codes>"`) alebo GitHub Actions – sa automaticky aktualizuje sekcia "Other Courses" zabalená medzi týmito značkami.

> [!NOTE]
> Ak už máte existujúci zoznam, jednoducho ho obalte rovnakými značkami. Ďalšie spustenie ho nahradí najnovším štandardizovaným obsahom.

---

## Ako zmeniť globálny obsah

Ak chcete aktualizovať štandardizovaný obsah, ktorý sa zobrazuje vo všetkých Beginners repozitároch:

1. Upravte šablónu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otvorte pull request do repozitára Co-op Translator so svojimi zmenami
3. Po zlúčení PR sa verzia Co‑op Translator aktualizuje
4. Pri ďalšom spustení Co‑op Translatora (CLI alebo GitHub Action) v cieľovom repozitári sa automaticky synchronizuje aktualizovaná sekcia

Tým sa zabezpečí jediný zdroj pravdy pre obsah "Other Courses" vo všetkých Beginners repozitároch.


## Veľkosti repozitárov

Repozitáre môžu byť veľké vzhľadom na počet preložených jazykov, aby sa používateľom uľahčilo používanie clone - sparse na klonovanie iba potrebných jazykov a nie celého repozitára

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
**Vyhlásenie o odmietnutí zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->