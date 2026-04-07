# Referenca naredbi

**Co-op Translator** CLI nudi nekoliko opcija za prilagodbu procesa prevođenja:

Naredba                                      | Opis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prevodi vaš projekt na navedene jezike. Primjer: translate -l "es fr de" prevodi na španjolski, francuski i njemački. Koristite translate -l "all" za prijevod na sve podržane jezike.
translate -l "language_codes" -u              | Ažurira prijevode brisanjem postojećih i njihovim ponovnim stvaranjem. Upozorenje: Ovo će izbrisati sve trenutne prijevode za navedene jezike.
translate -l "language_codes" -img            | Prevodi samo slike.
translate -l "language_codes" -md             | Prevodi samo Markdown datoteke.
translate -l "language_codes" -nb             | Prevodi samo Jupyter notebook datoteke (.ipynb).
translate -l "language_codes" --fix           | Ponovno prevodi datoteke s niskom pouzdanošću na temelju prethodnih rezultata evaluacije.
translate -l "language_codes" -d              | Uključuje debug način rada za detaljno zapisivanje.
translate -l "language_codes" --save-logs, -s | Spremi DEBUG zapisnike u datoteke unutar <root_dir>/logs/ (konzola ostaje pod kontrolom -d)
translate -l "language_codes" -r "root_dir"   | Navedite korijenski direktorij projekta
translate -l "language_codes" -f              | Koristi brzi način za prijevod slika (do 3x brže iscrtavanje uz malu cijenu kvalitete i poravnanosti).
translate -l "language_codes" -y              | Automatski potvrđuje sve upite (korisno za CI/CD pipelineove)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Uključi ili isključi dodavanje sekcije s odricanjem odgovornosti za strojni prijevod u prevedenim markdown i notebook datotekama (zadano: uključeno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizira dio s jezicima u README-u (sparse checkout) s URL-om vašeg repozitorija.
translate -l "language_codes" --help          | prikaz pomoći unutar CLI-ja koji pokazuje dostupne naredbe
evaluate -l "language_code"                  | Evaluira kvalitetu prijevoda za određeni jezik i daje ocjene pouzdanosti
evaluate -l "language_code" -c 0.8           | Evaluira prijevode s prilagođenim pragom pouzdanosti
evaluate -l "language_code" -f               | Brzi način evaluacije (samo pravila, bez LLM)
evaluate -l "language_code" -D               | Duboki način evaluacije (samo LLM, temeljito ali sporije)
evaluate -l "language_code" --save-logs, -s  | Spremanje DEBUG zapisnika u datoteke unutar <root_dir>/logs/
migrate-links -l "language_codes"             | Ponovno procesira prevedene Markdown datoteke za ažuriranje linkova na notebook-e (.ipynb). Preferira prevedene notebook-e kad su dostupni; u suprotnom može koristiti originalne notebook-e.
migrate-links -l "language_codes" -r          | Navedite korijenski direktorij projekta (zadano: trenutni direktorij).
migrate-links -l "language_codes" --dry-run   | Prikaži koje bi datoteke bile promijenjene bez zapisivanja promjena.
migrate-links -l "language_codes" --no-fallback-to-original | Ne prepisuj linkove na originalne notebook-e kada nedostaju prevedene verzije (ažuriraj samo kada prijevod postoji).
migrate-links -l "language_codes" -d          | Uključi debug način rada za detaljno zapisivanje.
migrate-links -l "language_codes" --save-logs, -s | Spremi DEBUG zapisnike u datoteke unutar <root_dir>/logs/
migrate-links -l "all" -y                      | Procesira sve jezike i automatski potvrđuje upozorenje.

## Primjeri korištenja

  1. Zadano ponašanje (dodaj nove prijevode bez brisanja postojećih):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Dodaj samo nove prijevode slika za korejski (bez brisanja postojećih):    translate -l "ko" -img

  3. Ažuriraj sve korejske prijevode (Upozorenje: Ovo briše sve postojeće korejske prijevode prije ponovnog prevođenja):    translate -l "ko" -u

  4. Ažuriraj samo korejske slike (Upozorenje: Ovo briše sve postojeće korejske slike prije ponovnog prevođenja):    translate -l "ko" -img -u

  5. Dodaj nove prijevode markdown datoteka za korejski bez utjecaja na ostale prijevode:    translate -l "ko" -md

  6. Ispravi prijevode s niskom pouzdanošću na temelju prethodnih rezultata evaluacije: translate -l "ko" --fix

  7. Ispravi prijevode s niskom pouzdanošću samo za određene datoteke (markdown): translate -l "ko" --fix -md

  8. Ispravi prijevode s niskom pouzdanošću samo za određene datoteke (slike): translate -l "ko" --fix -img

  9. Koristi brzi način prevođenja slika:    translate -l "ko" -img -f

  10. Ispravi prijevode s niskom pouzdanošću s prilagođenim pragom: translate -l "ko" --fix -c 0.8

  11. Primjer debug načina: - translate -l "ko" -d: Omogući debug zapisivanje.
  12. Spremi zapisnike u datoteke: translate -l "ko" -s
  13. DEBUG u konzoli i u datotekama: translate -l "ko" -d -s
  14. Prevedi bez dodavanja odricanja za strojni prijevod: translate -l "ko" --no-disclaimer

  15. Migriraj linkove na notebook-e za korejske prijevode (ažuriraj linkove na prevedene notebook-e kad su dostupni):    migrate-links -l "ko"

  15. Migriraj linkove sa suhim pokretom (bez pisanja u datoteke):    migrate-links -l "ko" --dry-run

  16. Ažuriraj linkove samo kada postoje prevedeni notebook-i (nemoj vraćati na originalne):    migrate-links -l "ko" --no-fallback-to-original

  17. Obradi sve jezike s upitom za potvrdu:    migrate-links -l "all"

  18. Obradi sve jezike i automatski potvrdi:    migrate-links -l "all" -y
  19. Spremi zapisnike u datoteke za migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliziraj savjet o jezicima u README-u s URL-om vašeg repozitorija:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Primjeri evaluacije

> [!WARNING]  
> **Beta značajka**: Funkcija evaluacije je trenutno u beta fazi. Ova značajka je izdana za evaluaciju prevedenih dokumenata, a metode evaluacije i detaljna implementacija su još uvijek u razvoju i podložne su promjenama.

  1. Evaluiraj korejske prijevode: evaluate -l "ko"

  2. Evaluiraj s prilagođenim pragom pouzdanosti: evaluate -l "ko" -c 0.8

  3. Brza evaluacija (samo pravila): evaluate -l "ko" -f

  4. Duboka evaluacija (samo LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je pomoću AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->