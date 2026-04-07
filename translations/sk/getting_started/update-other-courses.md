# Aktualizácia sekcie "Ďalšie kurzy" (Microsoft Beginners repozitáre)

Tento návod vysvetľuje, ako automaticky synchronizovať sekciu "Ďalšie kurzy" pomocou Co-op Translator a ako aktualizovať globálnu šablónu pre všetky repozitáre.

- Platí pre: iba Microsoft Beginners repozitáre
- Funguje s: Co-op Translator CLI a GitHub Actions
- Zdroj šablóny: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Rýchly štart: Povolenie auto‑synchronizácie vo vašom repozitári

Pridajte nasledujúce značky okolo sekcie "Ďalšie kurzy" vo vašom README. Co-op Translator nahradí všetko medzi týmito značkami pri každom spustení.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Pri každom spustení Co-op Translator – cez CLI (napr. `translate -l "<language codes>"`) alebo GitHub Actions – sa sekcia "Ďalšie kurzy" obalená týmito značkami automaticky aktualizuje.

> [!NOTE]
> Ak už máte existujúci zoznam, jednoducho ho obalte rovnakými značkami. Nasledujúce spustenie ho nahradí najnovším štandardizovaným obsahom.

---

## Ako zmeniť globálny obsah

Ak chcete aktualizovať štandardizovaný obsah, ktorý sa zobrazuje vo všetkých Beginners repozitároch:

1. Upravte šablónu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Otvorte pull request do repozitára Co-op Translator s vašimi zmenami
3. Po zlúčení PR bude aktualizovaná verzia Co-op Translator
4. Pri ďalšom spustení Co-op Translatora (CLI alebo GitHub Action) v cieľovom repozitári sa automaticky synchronizuje aktualizovaná sekcia

Týmto sa zabezpečí jeden jediný zdroj pravdy pre obsah "Ďalších kurzov" vo všetkých Beginners repozitároch.

## Veľkosť repozitárov

Repozitáre môžu byť veľké vzhľadom na počet preložených jazykov, aby sa používateľom poskytla pomoc pri používaní clone - sparse, ktorý umožňuje klonovať iba potrebné jazyky a nie celý repozitár.

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
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->