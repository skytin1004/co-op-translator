# Komenttiviite

**Co-op Translator** CLI tarjoaa useita vaihtoehtoja käännösprosessin mukauttamiseen:

Komento                                       | Kuvaus
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Kääntää projektisi määriteltyihin kieliin. Esimerkki: translate -l "es fr de" kääntää espanjaksi, ranskaksi ja saksaksi. Käytä translate -l "all" kääntääksesi kaikkiin tuettuihin kieliin.
translate -l "language_codes" -u              | Päivittää käännökset poistamalla nykyiset ja luomalla ne uudelleen. Varoitus: Tämä poistaa kaikki nykyiset käännökset määritellyiltä kieliltä.
translate -l "language_codes" -img            | Kääntää vain kuva-tiedostot.
translate -l "language_codes" -md             | Kääntää vain Markdown-tiedostot.
translate -l "language_codes" -nb             | Kääntää vain Jupyter-muistikirjatiedostot (.ipynb).
translate -l "language_codes" --fix           | Kääntää uudelleen tiedostot, joilla on matala luottamusarvo aikaisempien arviointitulosten perusteella.
translate -l "language_codes" -d              | Ottaa debug-tilan käyttöön yksityiskohtaista lokitusta varten.
translate -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle (konsoli pysyy -d:n ohjaamana)
translate -l "language_codes" -r "root_dir"   | Määrittää projektin juuressa olevan hakemiston
translate -l "language_codes" -f              | Käyttää nopeaa tilaa kuvakäännöksissä (jopa 3x nopeampi piirtäminen pienellä laadun ja kohdistuksen heikennyksellä).
translate -l "language_codes" -y              | Vahvistaa automaattisesti kaikki kehotteet (kätevää CI/CD-putkistoissa)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ottaa käyttöön tai poistaa käytöstä konekäännösvastuuvapautusosioiden lisäämisen käännettyihin markdown- ja muistikirjatiedostoihin (oletus: käytössä).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Henkilökohtaistaa README-kieliosion neuvontaa (sparse checkout) oman reposi URL:llä.
translate -l "language_codes" --help          | cli:n sisäinen ohje, jossa näkyvät saatavilla olevat komennot
evaluate -l "language_code"                  | Arvioi käännösten laatua tietylle kielelle ja antaa luottamusarvot
evaluate -l "language_code" -c 0.8           | Arvioi käännökset mukautetulla luottamuskynnyksellä
evaluate -l "language_code" -f               | Nopea arviointitila (vain sääntöpohjainen, ei LLM)
evaluate -l "language_code" -D               | Syväarviointitila (vain LLM-pohjainen, perusteellisempi mutta hitaampi)
evaluate -l "language_code" --save-logs, -s  | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle
migrate-links -l "language_codes"             | Käsittelee uudelleen käännetyt Markdown-tiedostot päivittääkseen linkit muistikirjoihin (.ipynb). Käyttää mieluiten käännettyjä muistikirjoja, jos saatavilla; muuten voi käyttää alkuperäisiä muistikirjoja.
migrate-links -l "language_codes" -r          | Määrittää projektin juurihakemiston (oletus: nykyinen hakemisto).
migrate-links -l "language_codes" --dry-run   | Näyttää, mitkä tiedostot muuttuisi ilman, että muutoksia tallennetaan.
migrate-links -l "language_codes" --no-fallback-to-original | Älä kirjoita linkkejä alkuperäisiin muistikirjoihin, kun käännettyjä vastineita ei ole (päivitä vain, kun käännetty on olemassa).
migrate-links -l "language_codes" -d          | Ottaa debug-tilan käyttöön yksityiskohtaista lokitusta varten.
migrate-links -l "language_codes" --save-logs, -s | Tallentaa DEBUG-tason lokit tiedostoihin polun <root_dir>/logs/ alle
migrate-links -l "all" -y                      | Käsittelee kaikki kielet ja vahvistaa varoituskehotteen automaattisesti.

## Käyttöesimerkit

  1. Oletuskäyttäytyminen (lisää uusia käännöksiä poistamatta olemassa olevia):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lisää vain uusia koreankielisiä kuvakäännöksiä (ei poista olemassa olevia käännöksiä):    translate -l "ko" -img

  3. Päivitä kaikki koreankieliset käännökset (Varoitus: Tämä poistaa kaikki nykyiset koreankieliset käännökset ennen uudelleenkääntämistä):    translate -l "ko" -u

  4. Päivitä vain koreankieliset kuvat (Varoitus: Tämä poistaa kaikki nykyiset koreankieliset kuvat ennen uudelleenkääntämistä):    translate -l "ko" -img -u

  5. Lisää uusia koreankielisiä markdown-käännöksiä vaikuttamatta muihin käännöksiin:    translate -l "ko" -md

  6. Korjaa matalan luottamuksen käännökset aiempien arviointitulosten perusteella: translate -l "ko" --fix

  7. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (markdown): translate -l "ko" --fix -md

  8. Korjaa matalan luottamuksen käännökset vain tietyille tiedostoille (kuvat): translate -l "ko" --fix -img

  9. Käytä nopeaa tilaa kuvakäännöksessä:    translate -l "ko" -img -f

  10. Korjaa matalan luottamuksen käännökset mukautetulla kynnyksellä: translate -l "ko" --fix -c 0.8

  11. Debug-tila esimerkki: - translate -l "ko" -d: Ota debug-lokit käyttöön.
  12. Tallenna lokit tiedostoihin: translate -l "ko" -s
  13. Konsoliin DEBUG ja tiedostoon DEBUG: translate -l "ko" -d -s
  14. Käännä ilman konekäännösvastuuvapautusten lisäämistä: translate -l "ko" --no-disclaimer

  15. Siirrä muistikirjalinkit koreankielisissä käännöksissä (päivitä linkit käännettyihin muistikirjoihin, kun saatavilla):    migrate-links -l "ko"

  15. Siirrä linkit kuiva-ajolla (ei kirjoita tiedostoja):    migrate-links -l "ko" --dry-run

  16. Päivitä linkit vain, kun käännetyt muistikirjat ovat olemassa (älä käytä alkuperäisiä):    migrate-links -l "ko" --no-fallback-to-original

  17. Käsittele kaikki kielet vahvistuskehotteella:    migrate-links -l "all"

  18. Käsittele kaikki kielet ja vahvista automaattisesti:    migrate-links -l "all" -y
  19. Tallenna lokitiedostot migrate-links-komennolle:    migrate-links -l "ko ja" -s

  20. Henkilökohtaista README-kieliosion neuvontaa omalla reposi URL:llä:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Arviointiesimerkit

> [!WARNING]  
> **Beta-ominaisuus**: Arviointitoiminto on tällä hetkellä beta-vaiheessa. Tämä ominaisuus julkaistiin käännettyjen asiakirjojen arviointiin, ja arviointimenetelmät sekä yksityiskohtainen toteutus ovat edelleen kehitysvaiheessa ja voivat muuttua.

  1. Arvioi koreankieliset käännökset: evaluate -l "ko"

  2. Arvioi mukautetulla luottamuskynnyksellä: evaluate -l "ko" -c 0.8

  3. Nopea arviointi (vain sääntöpohjainen): evaluate -l "ko" -f

  4. Syvä arviointi (vain LLM-pohjainen): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ole hyvä ja huomioi, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->