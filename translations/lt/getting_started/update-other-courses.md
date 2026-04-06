# Atnaujinkite skiltį „Kiti kursai“ (Microsoft Beginners saugyklos)

Šiame vadove paaiškinama, kaip padaryti, kad skiltis „Kiti kursai“ automatiškai sinchronizuotųsi naudojant Co-op Translator, ir kaip atnaujinti bendrą šabloną visoms saugykloms.

- Taikoma: tik Microsoft Beginners saugykloms
- Veikia su: Co-op Translator CLI ir GitHub Actions
- Šablono šaltinis: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Greitas pradžia: Įgalinkite automatinę sinchronizaciją savo saugykloje

Pridėkite šiuos žymeklius aplink skiltį „Kiti kursai“ savo README faile. Co-op Translator pakeis viską tarp šių žymeklių kiekvieno paleidimo metu.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Kiekvieną kartą, kai Co-op Translator veikia – per CLI (pvz., `translate -l "<language codes>"`) arba GitHub Actions – jis automatiškai atnaujins skiltį „Kiti kursai“, aprėptą šiais žymekliais.

> [!NOTE]
> Jei jau turite esamą sąrašą, tiesiog apsupkite jį tais pačiais žymekliais. Kitas paleidimas pakeis jį į naujausią standartizuotą turinį.

---

## Kaip pakeisti bendrą turinį

Jei norite atnaujinti standartizuotą turinį, kuris rodomas visose Beginners saugyklose:

1. Redaguokite šabloną: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Atidarykite pull request Co-op Translator saugykloje su savo pakeitimais
3. Po PR sujungimo Co-op Translator versija bus atnaujinta
4. Kitą kartą, kai Co-op Translator bus paleistas (CLI arba GitHub Action) tikslinei saugyklai, jis automatiškai sinchronizuos atnaujintą skiltį

Tai užtikrina vienintelį tiesos šaltinį skiltyje „Kiti kursai“ visuose Beginners saugyklose.


## Saugyklų dydžiai

Saugyklos gali tapti didelės dėl išverstų kalbų skaičiaus, siekiant padėti galutiniams vartotojams, todėl rekomenduojama naudoti git clone - sparse, kad būtų kopijuojamos tik reikalingos kalbos, o ne visa saugykla

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
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neatsakome už bet kokius nesusipratimus ar klaidingas interpretacijas, kilusias dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->