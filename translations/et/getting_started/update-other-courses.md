# Uuenda jaotist "Muud kursused" (Microsoft Beginners repositooriumid)

See juhend selgitab, kuidas muuta jaotis "Muud kursused" automaatselt sünkroonitavaks, kasutades Co-op Translatorit, ning kuidas uuendada ülemaailmset malli kõigi repositooriumide jaoks.

- Kehtib: ainult Microsoft Beginners repositooriumide puhul
- Töötab koos: Co-op Translator CLI ja GitHub Actions
- Malli allikas: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kiire algus: Luba automaatne sünkroonimine oma repositooriumis

Lisa järgmised märgised oma README-s jaotise "Muud kursused" ümber. Co-op Translator asendab iga käivituse korral kõik nende märgiste vahele jääva sisu.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Iga kord, kui Co-op Translator töötab — CLI kaudu (nt `translate -l "<keelekoodid>"`) või GitHub Actionsi kaudu — uuendab see automaatselt nende märgistega ümbritsetud jaotist "Muud kursused".

> [!NOTE]
> Kui sul on olemasolev nimekiri, siis lihtsalt pane see samade märgiste vahele. Järgmine käivitamine asendab selle uusima standardiseeritud sisuga.

---

## Kuidas muuta ülemaailmset sisu

Kui soovid uuendada standardiseeritud sisu, mis kuvatakse kõigis Beginners repositooriumites:

1. Muuda malli: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ava Co-op Translator repositooriumisse pull request oma muudatustega
3. Pärast PR-i ühendamist värskendatakse Co-op Translatori versiooni
4. Järgmine kord, kui Co-op Translator töötab (CLI või GitHub Action) sihtrepositooriumis, sünkroonib see automaatselt uuendatud jaotise

See tagab ühtse tõeallika sisule "Muud kursused" kõigis Beginners repositooriumites.


## Reposuurused

Reposid võivad muutuda mahukaks tänu paljudele tõlgitud keeltele, et aidata lõppkasutajal juhenditega. Soovitame kasutada clone - sparse käsku, et kloonida ainult vajalikud keeled, mitte kogu repositooriumit.

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
**Vastutusest vabastamine**:  
See dokument on tõlgitud kasutades tehisintellekti tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, tuleb arvestada, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise info puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta tõlke kasutamisest tingitud arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->