# Päivitä "Other Courses" -osio (Microsoft Beginners -repositoriot)

Tämä opas selittää, miten "Other Courses" -osio saadaan automaattisesti synkronoitua Co-op Translatorin avulla, ja miten päivitetään globaali malli kaikille repuille.

- Koskee: Vain Microsoft Beginners -repositorioita
- Toimii yhdessä: Co-op Translator CLI:n ja GitHub Actionsin kanssa
- Mallin lähde: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Nopeaan alkuun: Ota automaattinen synkronointi käyttöön repossasi

Lisää seuraavat merkkien ympärille "Other Courses" -osiossasi README-tiedostossa. Co-op Translator korvaa kaiken näiden merkkien väliltä jokaisella suorituskerralla.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Aina kun Co-op Translator suoritetaan—CLI:n kautta (esim. `translate -l "<kielikoodit>"`) tai GitHub Actionsissa—se päivittää automaattisesti "Other Courses" -osion, joka on kääritty näiden merkkien sisälle.

> [!NOTE]
> Jos sinulla on jo olemassa oleva lista, kääri se samoilla merkeillä. Seuraava suoritus korvaa sen viimeisimmällä standardoidulla sisällöllä.

---

## Kuinka muuttaa globaalia sisältöä

Jos haluat päivittää standardoidun sisällön, joka näkyy kaikissa Beginners-repoissa:

1. Muokkaa mallia: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Avaa pull request Co-op Translator -repoon muutoksillasi
3. Kun PR on yhdistetty, Co-op Translatorin versio päivittyy
4. Seuraavan kerran, kun Co-op Translator ajetaan (CLI:llä tai GitHub Actionilla) kohderepossa, se synkronoi päivitetyn osion automaattisesti

Tällä varmistetaan yhtenäinen totuuden lähde "Other Courses" -sisällölle kaikissa Beginners-repositorioissa.

## Repon koot

Repot voivat kasvaa suuriksi käännettyjen kielten määrän vuoksi, jotta loppukäyttäjille voidaan tarjota ohjeita kloonaamiseen - sparse-kloonauksen avulla voidaan kloonata vain tarvittavat kielet koko repon sijaan.

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
Tämä asiakirja on käännetty käyttämällä tekoälyn käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää auktoritatiivisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnasta, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->