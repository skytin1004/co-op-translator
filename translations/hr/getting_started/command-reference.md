# Command reference

The **Co-op Translator** CLI nudi nekoliko opcija za prilagodbu procesa prevođenja:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevodi vaš projekt na navedene jezike. Primjer: translate -l "es fr de" prevodi na španjolski, francuski i njemački. Koristite translate -l "all" za prevođenje na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prijevode brisanjem postojećih i njihovim ponovnim stvaranjem. Upozorenje: Ovo će izbrisati sve trenutne prijevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo slikovne datoteke.
translate -l "language_codes" -md             | Prevodi samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevodi samo Jupyter bilježnice (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevodi datoteke s niskim ocjenama povjerenja temeljeno na prethodnim rezultatima evaluacije.
translate -l "language_codes" -d              | Omogućuje debug način za detaljno bilježenje.
translate -l "language_codes" --save-logs, -s | Spremi DEBUG razinu zapisa u datoteke ispod <root_dir>/logs/ (konzola ostaje pod kontrolom -d)
translate -l "language_codes" -r "root_dir"   | Navodi korijenski direktorij projekta
translate -l "language_codes" -f              | Koristi brzi način za prevođenje slika (do 3x brže iscrtavanje uz blagi trošak kvalitete i poravnanja).
translate -l "language_codes" -y              | Automatski potvrdi sve upite (korisno za CI/CD cjevovode)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Omogući ili onemogući dodavanje odjeljka o odricanju odgovornosti za strojni prijevod u prevedene markdown i bilježnice (zadano: omogućeno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizirajte odjeljak o jezicima u README datoteci s URL-om vašeg repozitorija.
translate -l "language_codes" --help          | Pomoć unutar CLI-a koja prikazuje dostupne naredbe
evaluate -l "language_code"                  | Evaluira kvalitetu prijevoda za određeni jezik i daje ocjene povjerenja
evaluate -l "language_code" -c 0.8           | Evaluira prijevode s prilagođenim pragom povjerenja
evaluate -l "language_code" -f               | Brzi način evaluacije (samo prema pravilima, bez LLM-a)
evaluate -l "language_code" -D               | Duboka evaluacija (samo na temelju LLM-a, temeljitije ali sporije)
evaluate -l "language_code" --save-logs, -s  | Spremi DEBUG razinu zapisa u datoteke ispod <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno obrađuje prevedene Markdown datoteke za ažuriranje veza na bilježnice (.ipynb). Preferira prevedene bilježnice ako su dostupne; inače može koristiti originalne bilježnice.
migrate-links -l "language_codes" -r          | Navedite korijenski direktorij projekta (zadano: trenutni direktorij).
migrate-links -l "language_codes" --dry-run   | Prikazuje koje bi datoteke bile promijenjene bez zapisivanja promjena.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepisuj veze na originalne bilježnice ako prevedene verzije nedostaju (ažuriraj samo ako postoji prijevod).
migrate-links -l "language_codes" -d          | Omogući debug način za detaljno bilježenje.
migrate-links -l "language_codes" --save-logs, -s | Spremi DEBUG razinu zapisa u datoteke ispod <root_dir>/logs/
migrate-links -l "all" -y                      | Obradi sve jezike i automatski potvrdi upit upozorenja.

## Usage examples

  1. Zadano ponašanje (dodaj nove prijevode bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove korejske prijevode slika (ne brišu se postojeći):    translate -l "ko" -img

  3. Ažuriraj sve korejske prijevode (Upozorenje: Ovo briše sve postojeće korejske prijevode prije ponovnog prevođenja):    translate -l "ko" -u

  4. Ažuriraj samo korejske slike (Upozorenje: Ovo briše sve postojeće korejske slike prije ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodaj nove prijevode markdowna za korejski bez utjecaja na druge prijevode:    translate -l "ko" -md

  6. Popravi prijevode s niskim povjerenjem prema prethodnim rezultatima evaluacije: translate -l "ko" --fix

  7. Popravi prijevode niske pouzdanosti samo za određene datoteke (markdown): translate -l "ko" --fix -md

  8. Popravi prijevode niske pouzdanosti samo za određene datoteke (slike): translate -l "ko" --fix -img

  9. Koristi brzi način za prevođenje slika:    translate -l "ko" -img -f

  10. Popravi prijevode niske pouzdanosti s prilagođenim pragom: translate -l "ko" --fix -c 0.8

  11. Primjer debug načina: - translate -l "ko" -d: Omogući debug zapis.
  12. Spremi zapise u datoteke: translate -l "ko" -s
  13. Konzola DEBUG i datoteka DEBUG: translate -l "ko" -d -s
  14. Prevedi bez dodavanja odricanja od odgovornosti za strojni prijevod u izlazima: translate -l "ko" --no-disclaimer

  15. Migriraj veze bilježnica za korejske prijevode (ažuriraj veze na prevedene bilježnice kad su dostupne):    migrate-links -l "ko"

  15. Migriraj veze s dry-run opcijom (bez zapisivanja promjena):    migrate-links -l "ko" --dry-run

  16. Ažuriraj veze samo kada postoje prevedene bilježnice (ne vraćaj se na originalne):    migrate-links -l "ko" --no-fallback-to-original

  17. Obradi sve jezike s upitom za potvrdu:    migrate-links -l "all"

  18. Obradi sve jezike i automatski potvrdi:    migrate-links -l "all" -y
  19. Spremi zapise u datoteke za migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliziraj obavijest o jezicima u README-u s URL-om svog repozitorija:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluation Examples

> [!WARNING]  
> **Beta Feature**: Funkcionalnost evaluacije je trenutno u beta verziji. Ova značajka je izdana za evaluaciju prevedenih dokumenata, a metode evaluacije i detaljna implementacija su još u razvoju i podložne promjenama.

  1. Evaluiraj korejske prijevode: evaluate -l "ko"

  2. Evaluiraj s prilagođenim pragom povjerenja: evaluate -l "ko" -c 0.8

  3. Brza evaluacija (samo prema pravilima): evaluate -l "ko" -f

  4. Duboka evaluacija (samo na temelju LLM-a): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj je dokument preveden pomoću AI servis za prijevod [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->