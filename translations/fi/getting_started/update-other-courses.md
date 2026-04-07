# Päivitä "Other Courses" -osio (Microsoft Beginners -repositoriot)

Tämä opas selittää, miten "Other Courses" -osio synkronoituu automaattisesti Co-op Translatorin avulla ja miten päivität globaalin mallipohjan kaikille repositorioille.

- Soveltuu vain: Microsoft Beginners -repositorioille
- Toimii yhdessä: Co-op Translator CLI:n ja GitHub Actionsin kanssa
- Mallin lähde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Pikakäyttö: Ota automaattinen synkronointi käyttöön repossasi

Lisää seuraavat merkit "Other Courses" -osion ympärille README-tiedostossasi. Co-op Translator korvaa nämä merkit sisältävän osion joka ajokerralla.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Joka kerta, kun Co-op Translator ajetaan – joko CLI:n kautta (esim. `translate -l "<language codes>"`) tai GitHub Actionsissa – se päivittää automaattisesti "Other Courses" -osion, joka on näiden merkkien sisällä.

> [!NOTE]
> Jos sinulla on jo olemassa oleva lista, kiedo se vain samoilla merkeillä. Seuraava ajokerta korvaa sen uusimmalla standardoidulla sisällöllä.

---

## Kuinka muuttaa globaalia sisältöä

Jos haluat päivittää standardoidun sisällön, joka näkyy kaikissa Beginners-repositorioissa:

1. Muokkaa mallipohjaa: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Avaa pull request Co-op Translator -repositorioosi tekemilläsi muutoksilla
3. Kun PR on hyväksytty, Co-op Translatorin versio päivittyy
4. Seuraavan kerran, kun Co-op Translator ajetaan (CLI:llä tai GitHub Actionissa) kohderepossa, päivitetty osio synkronoituu automaattisesti

Tämä varmistaa yhden totuuden lähteen "Other Courses" -sisällölle kaikissa Beginners-repositorioissa.


## Repositorioiden koot

Repositoriot voivat kasvaa suuriksi käännettyjen kielien määrän vuoksi. Tämä auttaa loppukäyttäjiä käyttämään clone - sparse -toimintoa, jolla voidaan kloonata vain tarvittavat kielet eikä koko repositorioa.

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
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja ota huomioon, että automaattikäännöksissä saattaa olla virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mistään väärinymmärryksistä tai tulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->