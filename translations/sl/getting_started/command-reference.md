# Referenca ukazov

Ukazna vrstica **Co-op Translator** ponuja več možnosti za prilagoditev prevajalskega postopka:

Ukaz                                         | Opis
----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevede vaš projekt v navedene jezike. Primer: translate -l "es fr de" prevede v španščino, francoščino in nemščino. Uporabite translate -l "all" za prevod v vse podprte jezike.
translate -l "language_codes" -u              | Posodobi prevode z brisanjem obstoječih in njihovo ponovnim ustvarjanjem. Opozorilo: To bo izbrisalo vse trenutne prevode za navedene jezike.
translate -l "language_codes" -img            | Prevede samo slikovne datoteke.
translate -l "language_codes" -md             | Prevede samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevede samo Jupyter beležke (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevede datoteke z nizko stopnjo zaupanja na podlagi prejšnjih rezultatov ocenjevanja.
translate -l "language_codes" -d              | Omogoči način za odpravljanje napak za podrobno beleženje.
translate -l "language_codes" --save-logs, -s | Shrani dnevniške datoteke na ravni DEBUG v <root_dir>/logs/ (konzola ostane pod nadzorom -d)
translate -l "language_codes" -r "root_dir"   | Določi korensko mapo projekta
translate -l "language_codes" -f              | Uporabi hitri način za prevajanje slik (do 3-krat hitrejše risanje z rahlo izgubo kakovosti in poravnave).
translate -l "language_codes" -y              | Samodejno potrdi vse potrditvene zahteve (uporabno za CI/CD cevi)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Omogoči ali onemogoči dodajanje odstavka o strojno prevajanem besedilu v prevedene markdown in beležke (privzeto: omogočeno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizira opozorilo v razdelku jezikov README (sparse checkout) z URL-jem vašega repozitorija.
translate -l "language_codes" --help          | podrobna pomoč znotraj CLI z razpoložljivimi ukazi
evaluate -l "language_code"                  | Ocenjuje kakovost prevoda za določen jezik in nudi rezultate zaupanja
evaluate -l "language_code" -c 0.8           | Ocenjuje prevode z uporabo lastnega praga zaupanja
evaluate -l "language_code" -f               | Hitri način ocenjevanja (samo na osnovi pravil, brez LLM)
evaluate -l "language_code" -D               | Globoko ocenjevanje (samo na osnovi LLM, bolj temeljito, a počasneje)
evaluate -l "language_code" --save-logs, -s  | Shrani dnevniške datoteke na ravni DEBUG v <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obdela prevedene Markdown datoteke za posodobitev povezav do beležk (.ipynb). Prednost imajo prevedene beležke, če so na voljo; sicer lahko uporabi originalne beležke.
migrate-links -l "language_codes" -r          | Določi korensko mapo projekta (privzeto: trenutna mapa).
migrate-links -l "language_codes" --dry-run   | Prikaže datoteke, ki bi se spremenile, brez zapisovanja sprememb.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepiše povezav do originalnih beležk, kadar manjkajo prevedene verzije (posodobi samo, če prevedena obstaja).
migrate-links -l "language_codes" -d          | Omogoči način za odpravljanje napak za podrobno beleženje.
migrate-links -l "language_codes" --save-logs, -s | Shrani dnevniške datoteke na ravni DEBUG v <root_dir>/logs/
migrate-links -l "all" -y                      | Obdelaj vse jezike in samodejno potrdi opozorilo.

## Primeri uporabe

  1. Privzeto delovanje (doda nove prevode brez brisanja obstoječih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske prevode slik (obstoječi prevodi niso izbrisani):    translate -l "ko" -img

  3. Posodobi vse korejske prevode (Opozorilo: to izbriše vse obstoječe korejske prevode pred ponovnim prevajanjem):    translate -l "ko" -u

  4. Posodobi samo korejske slike (Opozorilo: to izbriše vse obstoječe korejske slike pred ponovnim prevajanjem):    translate -l "ko" -img -u

  5. Dodaj nove prevode markdown za korejski jezik brez vpliva na druge prevode:    translate -l "ko" -md

  6. Popravi prevode z nizko zanesljivostjo na podlagi prejšnjih rezultatov ocenjevanja: translate -l "ko" --fix

  7. Popravi prevode z nizko zanesljivostjo samo za določene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravi prevode z nizko zanesljivostjo samo za določene datoteke (slike): translate -l "ko" --fix -img

  9. Uporabi hitri način za prevajanje slik:    translate -l "ko" -img -f

  10. Popravi prevode z nizko zanesljivostjo z lastnim pragom: translate -l "ko" --fix -c 0.8

  11. Primer načina odpravljanja napak: - translate -l "ko" -d: Omogoči beleženje za odpravljanje napak.
  12. Shrani dnevnike v datoteke: translate -l "ko" -s
  13. Konzolni in datotečni DEBUG: translate -l "ko" -d -s
  14. Prevedi brez dodajanja opomb o strojno prevajanem besedilu v izhode: translate -l "ko" --no-disclaimer

  15. Migriraj povezave do beležk za korejske prevode (posodobi povezave v prevedenih beležkah, če so na voljo):    migrate-links -l "ko"

  15. Migriraj povezave z izvajanjem suhega zagona (brez zapisovanja sprememb):    migrate-links -l "ko" --dry-run

  16. Posodobi povezave samo, če prevedene beležke obstajajo (ne uporablja originalnih):    migrate-links -l "ko" --no-fallback-to-original

  17. Obdelaj vse jezike z zahtevo za potrditev:    migrate-links -l "all"

  18. Obdelaj vse jezike in samodejno potrdi:    migrate-links -l "all" -y
  19. Shrani dnevnike za migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliziraj opozorilo v razdelku jezikov README z URL-jem vašega repozitorija:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Primeri ocenjevanja

> [!WARNING]  
> **Beta funkcija**: Funkcija ocenjevanja je trenutno v beta fazi. Ta funkcija je bila izdana za ocenjevanje prevedenih dokumentov, metode ocenjevanja in podrobna implementacija pa so še v razvoju in se lahko spremenijo.

  1. Ocenjuj korejske prevode: evaluate -l "ko"

  2. Ocenjuj z lastnim pragom zaupanja: evaluate -l "ko" -c 0.8

  3. Hitro ocenjevanje (samo na osnovi pravil): evaluate -l "ko" -f

  4. Globoko ocenjevanje (samo na osnovi LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku naj se šteje za pristni vir. Za kritične informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->