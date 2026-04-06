# Referenca ukazov

**Co-op Translator** CLI ponuja več možnosti za prilagoditev prevajalskega procesa:

Ukaz                                         | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevede vaš projekt v določene jezike. Primer: translate -l "es fr de" prevede v španščino, francoščino in nemščino. Uporabite translate -l "all" za prevod v vse podprte jezike.
translate -l "language_codes" -u              | Posodobi prevode tako, da izbriše obstoječe in jih ponovno ustvari. Opozorilo: To bo izbrisalo vse trenutne prevode za določene jezike.
translate -l "language_codes" -img            | Prevede samo slikovne datoteke.
translate -l "language_codes" -md             | Prevede samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevede samo Jupyter beležnice (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevede datoteke z nizko zanesljivostjo na podlagi preteklih rezultatov ocenjevanja.
translate -l "language_codes" -d              | Omogoči debug način za podrobno beleženje.
translate -l "language_codes" --save-logs, -s | Shrani DEBUG nivo beleženja v datoteke pod <root_dir>/logs/ (konzola ostane pod nadzorom -d)
translate -l "language_codes" -r "root_dir"   | Določi korenski imenik projekta
translate -l "language_codes" -f              | Uporabi hitri način za prevajanje slik (do 3x hitrejše risanje z rahlo izgubo kakovosti in ujemanja).
translate -l "language_codes" -y              | Samodejno potrdi vse pozive (uporabno za CI/CD pipe)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Omogoči ali onemogoči dodajanje odstavka o strojno prevajanem besedilu v prevedene markdown in beležnice (privzeto: omogočeno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizira nasvet v razdelku jezikov README datoteke (sparse checkout) z URL naslovom vašega repozitorija.
translate -l "language_codes" --help          | Podrobnosti pomoči znotraj CLI, ki kažejo razpoložljive ukaze
evaluate -l "language_code"                  | Ocenjuje kakovost prevoda za določen jezik in zagotavlja zanesljivostne ocene
evaluate -l "language_code" -c 0.8           | Ocenjuje prevode z lastnim pragom zanesljivosti
evaluate -l "language_code" -f               | Hiter način ocenjevanja (le na podlagi pravil, brez LLM)
evaluate -l "language_code" -D               | Globoko ocenjevanje (le na podlagi LLM, temeljitejše, a počasnejše)
evaluate -l "language_code" --save-logs, -s  | Shrani DEBUG nivo beleženja v datoteke pod <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obdela prevedene Markdown datoteke za posodobitev povezav do beležnic (.ipynb). Preferira prevedene beležnice, če so na voljo; sicer lahko uporabi originalne beležnice.
migrate-links -l "language_codes" -r          | Določi korenski imenik projekta (privzeto: trenutni imenik).
migrate-links -l "language_codes" --dry-run   | Prikaže, katere datoteke bi se spremenile, brez zapisovanja sprememb.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepisuje povezav na originalne beležnice, kadar manjkajo prevedene različice (posodobi le, če prevedene obstajajo).
migrate-links -l "language_codes" -d          | Omogoči debug način za podrobno beleženje.
migrate-links -l "language_codes" --save-logs, -s | Shrani DEBUG nivo beleženja v datoteke pod <root_dir>/logs/
migrate-links -l "all" -y                      | Obdelaj vse jezike in samodejno potrdi opozorilni poziv.

## Primeri uporabe

  1. Privzeto vedenje (dodaj nove prevode brez brisanja obstoječih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske prevode slik (obstoječi prevodi niso izbrisani):    translate -l "ko" -img

  3. Posodobi vse korejske prevode (Opozorilo: To izbrisuje vse obstoječe korejske prevode pred ponovnim prevajanjem):    translate -l "ko" -u

  4. Posodobi samo korejske slike (Opozorilo: To izbrisuje vse obstoječe korejske slike pred ponovnim prevajanjem):    translate -l "ko" -img -u

  5. Dodaj nove markdown prevode za korejščino, brez vpliva na druge prevode:    translate -l "ko" -md

  6. Popravi prevode z nizko zanesljivostjo na podlagi prejšnjih rezultatov ocene: translate -l "ko" --fix

  7. Popravi prevode z nizko zanesljivostjo samo za določene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravi prevode z nizko zanesljivostjo samo za določene datoteke (slike): translate -l "ko" --fix -img

  9. Uporabi hitri način za prevajanje slik:    translate -l "ko" -img -f

  10. Popravi prevode z nizko zanesljivostjo z lastnim pragom: translate -l "ko" --fix -c 0.8

  11. Primer debug načina: - translate -l "ko" -d: Omogoči beleženje za debug.
  12. Shrani zapise v datoteke: translate -l "ko" -s
  13. DEBUG konzola in DEBUG datoteke: translate -l "ko" -d -s
  14. Prevajaj brez dodajanja obvestil o strojno prevajanem besedilu: translate -l "ko" --no-disclaimer

  15. Migriraj povezave beležnic za korejske prevode (posodobi povezave na prevedene beležnice, če so na voljo):    migrate-links -l "ko"

  15. Migriraj povezave z dry-run (brez zapisovanja datotek):    migrate-links -l "ko" --dry-run

  16. Posodobi povezave samo, če obstajajo prevedene beležnice (ne vračaj se na izvirnike):    migrate-links -l "ko" --no-fallback-to-original

  17. Obdelaj vse jezike s potrditvenim pozivom:    migrate-links -l "all"

  18. Obdelaj vse jezike in samodejno potrdi:    migrate-links -l "all" -y
  19. Shrani zapise za migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliziraj nasvet o jezikih v README z URLjem vašega repozitorija:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Primeri ocenjevanja

> [!WARNING]  
> **Beta funkcija**: Funkcionalnost ocenjevanja je trenutno v beta fazi. Ta funkcija je bila izdana za ocenjevanje prevedenih dokumentov, metode ocenjevanja in podrobna implementacija pa so še v razvoju in se lahko spremenijo.

  1. Ocenjuj korejske prevode: evaluate -l "ko"

  2. Ocenjuj z lastnim pragom zanesljivosti: evaluate -l "ko" -c 0.8

  3. Hitra ocena (le na podlagi pravil): evaluate -l "ko" -f

  4. Globoka ocena (le na podlagi LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni prevod s strani človeka. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->