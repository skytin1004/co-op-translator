# Atnaujinkite skyrių „Kiti kursai“ (Microsoft Beginners saugyklos)

Šiame vadove paaiškinama, kaip automatiškai sinchronizuoti skyrių „Kiti kursai“ naudojant Co-op Translator ir kaip atnaujinti globalią šablono versiją visoms saugykloms.

- Taikoma: tik Microsoft Beginners saugykloms
- Veikia su: Co-op Translator CLI ir GitHub Actions
- Šablono šaltinis: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Greitas pradėjimas: Įgalinkite automatinę sinchronizaciją savo saugykloje

Įterpkite šiuos žymeklius aplink skyrių „Kiti kursai“ savo README faile. Co-op Translator kiekvieno paleidimo metu pakeis viską tarp šių žymeklių.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kiekvieną kartą, kai Co-op Translator veikia – per CLI (pvz., `translate -l "<language codes>"`) arba GitHub Actions – jis automatiškai atnaujina „Kiti kursai“ skyrių, apsuptą šiais žymekliais.

> [!NOTE]
> Jei jau turite esamą sąrašą, tiesiog apsupti jį tais pačiais žymekliais. Kitas paleidimas pakeis jį naujausia standartizuota turinio versija.

---

## Kaip pakeisti globalų turinį

Jei norite atnaujinti standartizuotą turinį, kuris rodomas visose Beginners saugyklose:

1. Redaguokite šabloną: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Atidarykite pull request Co-op Translator saugykloje su savo pakeitimais
3. Kai PR bus sujungtas, atnaujinsis Co-op Translator versija
4. Kitą kartą, kai Co-op Translator paleidžiamas (per CLI arba GitHub Action) tikslo saugykloje, automatiškai sinchronizuos atnaujintą skyrių

Tai užtikrina vieningą tiesos šaltinį „Kiti kursai“ turiniui visuose Beginners saugyklose.

## Saugyklų dydžiai 

Saugyklos gali tapti didelės dėl daugybės išverstų kalbų, kad padėtų galutiniams vartotojams, ir suteiktų gaires, kaip naudoti clone - sparse, kad būtų galima klonuoti tik reikalingas kalbas, o ne visą saugyklą

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
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatizuotos vertimo paslaugos gali turėti klaidų ar netikslumų. Originalus dokumentas gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojamas profesionalus žmogaus vertimas. Mes neatsakome už bet kokius nesusipratimus ar neteisingus aiškinimus, kylančius naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->