# Uuenda jaotist "Muud kursused" (Microsoft Beginners hoidlad)

See juhend selgitab, kuidas teha jaotis "Muud kursused" automaatselt sünkroonitavaks, kasutades Co-op Translatorit, ning kuidas värskendada kõigi hoidlate globaalseid malle.

- Kehtib: ainult Microsoft Beginners hoidlate jaoks
- Töötab koos: Co-op Translator CLI ja GitHub Actionsiga
- Malle allikas: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Kiire algus: Luba oma hoidlale automaatne sünkroonimine

Lisa oma README-s jaotise "Muud kursused" ümber järgmised märgendid. Co-op Translator asendab kõike nende märgendite vahel iga käivituse ajal.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Iga kord, kui Co-op Translator töötab – CLI kaudu (nt `translate -l "<language codes>"`) või GitHub Actionsis – uuendab see automaatselt nende märgendite vahel olevat jaotist "Muud kursused".

> [!NOTE]
> Kui sul on juba olemasolev nimekiri, pane see lihtsalt samade märgenditega ümber. Järgmine käivitamine asendab selle uusima standardiseeritud sisuga.

---

## Kuidas muuta globaalset sisu

Kui soovid uuendada standardiseeritud sisu, mis kuvatakse kõigis Beginners hoidlates:

1. Muuda malli: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Ava pull request Co-op Translatori hoidlas oma muudatustega
3. Pärast PR-i ühendamist värskendatakse Co-op Translatori versioon
4. Järgmine kord, kui Co-op Translator töötab (CLI või GitHub Action) eesmärgihoidlas, sünkroonitakse see värskendatud jaotis automaatselt

See tagab "Muud kursused" sisu ainsa tõese allika kõigis Beginners hoidlates.


## Hoidla suurused

Hoidlad võivad muutuda mahukaks, sest tõlgitakse palju keeli, et aidata kasutajatel pakkuda juhiseid, kuidas kasutada clone - sparse ainult vajalike keelte kloonimiseks, mitte kogu hoidla allalaadimiseks

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
See dokument on tõlgitud kasutades tehisintellekti tõlkimisteenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame täpsust, palun arvestage, et automatiseeritud tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleb pidada autoriteetseks allikaks. Tähtsa info puhul soovitatakse professionaalset inimtõlget. Me ei vastuta ühegi arusaamatuse või väärtõlgenduse eest, mis võivad tuleneda selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->