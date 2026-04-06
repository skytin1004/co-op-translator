# Komenttiviite

**Co-op Translator** CLI tarjoaa useita vaihtoehtoja käännösprosessin mukauttamiseen:

Komentti                                       | Kuvaus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Kääntää projektisi määriteltyihin kieliin. Esimerkki: translate -l "es fr de" kääntää espanjaksi, ranskaksi ja saksaksi. Käytä translate -l "all" kääntääksesi kaikille tuetuille kielille.
translate -l "language_codes" -u              | Päivittää käännökset poistamalla olemassa olevat ja luomalla ne uudelleen. Varoitus: Tämä poistaa kaikki nykyiset käännökset määritellyille kielille.
translate -l "language_codes" -img            | Kääntää vain kuv tiedostot.
translate -l "language_codes" -md             | Kääntää vain Markdown-tiedostot.
translate -l "language_codes" -nb             | Kääntää vain Jupyter-muistio-tiedostot (.ipynb).
translate -l "language_codes" --fix           | Uudelleenkääntää tiedostot, joiden luottamuspisteet ovat alhaiset aiempien arviointitulosten perusteella.
translate -l "language_codes" -d              | Ottaa käyttöön debug-tilan yksityiskohtaista lokitusta varten.
translate -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle (konsoli pysyy hallinnassa -d:llä)
translate -l "language_codes" -r "root_dir"   | Määrittää projektin juurihakemiston
translate -l "language_codes" -f              | Käyttää nopeaa tilaa kuva käännöksessä (jopa 3x nopeampi visualisointi lievällä laadun ja kohdistuksen heikennyksellä).
translate -l "language_codes" -y              | Vahvistaa automaattisesti kaikki kehotteet (hyödyllinen CI/CD-putkissa)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ota käyttöön tai poista konekäännösseloste osiot käännetyissä markdown- ja muistiofileissä (oletus: käytössä).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personoi README-kielten osion ohjeistus (harva checkout) oman reposi URL:llä.
translate -l "language_codes" --help          | Näyttää CLI:n sisäiset käytettävissä olevat komennot
evaluate -l "language_code"                  | Arvioi tietyn kielen käännösten laatua ja antaa luottamuspisteet
evaluate -l "language_code" -c 0.8           | Arvioi käännökset mukautetulla luottamuskynnyksellä
evaluate -l "language_code" -f               | Nopea arviointitila (vain sääntöpohjainen, ei LLM)
evaluate -l "language_code" -D               | Syväarviointitila (vain LLM-pohjainen, perusteellisempi mutta hitaampi)
evaluate -l "language_code" --save-logs, -s  | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle
migrate-links -l "language_codes"             | Käsittelee uudelleen käännetyt Markdown-tiedostot päivittääkseen linkit muistioihin (.ipynb). Suosii käännettyjä muistioita, kun niitä on; muussa tapauksessa voi palautua alkuperäisiin.
migrate-links -l "language_codes" -r          | Määrittää projektin juurihakemiston (oletus: nykyinen hakemisto).
migrate-links -l "language_codes" --dry-run   | Näyttää, mitkä tiedostot muuttuisivat, ilman että kirjoitetaan muutoksia.
migrate-links -l "language_codes" --no-fallback-to-original | Älä palauta linkkejä alkuperäisiin muistioihin, kun käännettyjä vastineita ei ole (päivitä vain kun käännettyjä on).
migrate-links -l "language_codes" -d          | Ota käyttöön debug-tila yksityiskohtaista lokitusta varten.
migrate-links -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle
migrate-links -l "all" -y                      | Käsittele kaikki kielet ja vahvista varoituskehote automaattisesti.

## Käyttöesimerkit

  1. Oletuskäyttäytyminen (lisää uusia käännöksiä poistamatta olemassa olevia):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisää vain uudet koreankieliset kuvakäännökset (ei poista olemassa olevia käännöksiä):    translate -l "ko" -img

  3. Päivitä kaikki koreankieliset käännökset (varoitus: tämä poistaa kaikki olemassa olevat koreankieliset käännökset ennen uudelleenkääntämistä):    translate -l "ko" -u

  4. Päivitä vain koreankieliset kuvat (varoitus: tämä poistaa kaikki olemassa olevat koreankieliset kuvat ennen uudelleenkääntämistä):    translate -l "ko" -img -u

  5. Lisää uudet markdown-käännökset koreaksi vaikuttamatta muihin käännöksiin:    translate -l "ko" -md

  6. Korjaa aiempien arviointien perusteella matalan luottamuksen käännökset: translate -l "ko" --fix

  7. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (markdown): translate -l "ko" --fix -md

  8. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (kuvat): translate -l "ko" --fix -img

  9. Käytä nopeaa tilaa kuvan käännöksessä:    translate -l "ko" -img -f

  10. Korjaa matalan luottamuksen käännökset mukautetulla kynnyksellä: translate -l "ko" --fix -c 0.8

  11. Debug-tilan esimerkki: - translate -l "ko" -d: Ota käyttöön debug-lokitus.
  12. Tallenna lokit tiedostoihin: translate -l "ko" -s
  13. Konsolin DEBUG ja tiedostojen DEBUG: translate -l "ko" -d -s
  14. Käännä ilman konekäännösvastuuvapautuslauseita tulosteissa: translate -l "ko" --no-disclaimer

  15. Siirrä muistioiden linkit koreankielisille käännöksille (päivitä linkit käännettyihin muistioihin, kun saatavilla):    migrate-links -l "ko"

  15. Siirrä linkkejä kuivaharjoituksella (ei kirjoiteta tiedostoja):    migrate-links -l "ko" --dry-run

  16. Päivitä linkkejä vain, kun käännettyjä muistioita on (älä palauta alkuperäisiin):    migrate-links -l "ko" --no-fallback-to-original

  17. Käsittele kaikki kielet vahvistuskehotteella:    migrate-links -l "all"

  18. Käsittele kaikki kielet ja vahvista automaattisesti:    migrate-links -l "all" -y
  19. Tallenna lokitiedostot migrate-links-käytössä:    migrate-links -l "ko ja" -s

  20. Personoi README-kielten ohjeistus omalla reposi URL:llä:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Arviointiesimerkit

> [!WARNING]  
> **Beetatoiminto**: Arviointitoiminto on parhaillaan beetavaiheessa. Tämä ominaisuus julkaistiin käännettyjen asiakirjojen arviointiin, ja arviointimenetelmät sekä tarkka toteutus ovat vielä kehitteillä ja voivat muuttua.

  1. Arvioi koreankieliset käännökset: evaluate -l "ko"

  2. Arvioi mukautetulla luottamuskynnyksellä: evaluate -l "ko" -c 0.8

  3. Nopea arviointi (vain sääntöpohjainen): evaluate -l "ko" -f

  4. Syväarviointi (vain LLM-pohjainen): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälykäännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automatisoiduissa käännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->