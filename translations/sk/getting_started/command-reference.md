# Referencia príkazov

CLI **Co-op Translator** ponúka niekoľko možností na prispôsobenie prekladového procesu:

Príkaz                                       | Popis
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Prekladá váš projekt do určených jazykov. Príklad: translate -l "es fr de" preloží do španielčiny, francúzštiny a nemčiny. Použite translate -l "all" pre preklad do všetkých podporovaných jazykov.
translate -l "language_codes" -u              | Aktualizuje preklady odstránením existujúcich a ich opätovným vytvorením. Upozornenie: Toto vymaže všetky súčasné preklady pre určené jazyky.
translate -l "language_codes" -img            | Prekladá iba obrázkové súbory.
translate -l "language_codes" -md             | Prekladá iba Markdown súbory.
translate -l "language_codes" -nb             | Prekladá iba súbory Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Opätovne preloží súbory s nízkou dôverou na základe predchádzajúcich hodnotení.
translate -l "language_codes" -d              | Aktivuje režim ladenia pre podrobné zaznamenávanie.
translate -l "language_codes" --save-logs, -s | Uloží záznamy úrovne DEBUG do súborov pod <root_dir>/logs/ (konzola je riadená pomocou -d)
translate -l "language_codes" -r "root_dir"   | Špecifikuje koreňový adresár projektu
translate -l "language_codes" -f              | Použije rýchly režim pre preklad obrázkov (až 3x rýchlejšie vykresľovanie za mierny kompromis kvality a zarovnania).
translate -l "language_codes" -y              | Automaticky potvrdzuje všetky výzvy (užitočné pre CI/CD pipeline)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Zapnúť alebo vypnúť pridanie sekcie s upozornením o strojovom preklade do prekladaných markdown a notebookov (predvolené: zapnuté).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizovať sekciu jazykov v README so svojou URL adresou repozitára.
translate -l "language_codes" --help          | podrobnosti pomoci v CLI zobrazujúce dostupné príkazy
evaluate -l "language_code"                  | Vyhodnotí kvalitu prekladu pre konkrétny jazyk a poskytne skóre dôveryhodnosti
evaluate -l "language_code" -c 0.8           | Vyhodnotí preklady s vlastnou prahovou hodnotou dôveryhodnosti
evaluate -l "language_code" -f               | Rýchly hodnotiaci režim (len pravidlami, bez LLM)
evaluate -l "language_code" -D               | Hĺbkový hodnotiaci režim (iba na báze LLM, dôkladnejší ale pomalší)
evaluate -l "language_code" --save-logs, -s  | Uloží záznamy úrovne DEBUG do súborov pod <root_dir>/logs/
migrate-links -l "language_codes"             | Preprocesuje preložené Markdown súbory a aktualizuje odkazy na notebooky (.ipynb). Preferuje preložené notebooky, ak sú dostupné; inak môže použiť pôvodné notebooky.
migrate-links -l "language_codes" -r          | Špecifikuje koreňový adresár projektu (predvolené: aktuálny adresár).
migrate-links -l "language_codes" --dry-run   | Ukáže, ktoré súbory by sa zmenili bez zapísania zmien.
migrate-links -l "language_codes" --no-fallback-to-original | Neprepíše odkazy na pôvodné notebooky, ak chýbajú preložené verzie (aktualizuje iba, ak preložené existujú).
migrate-links -l "language_codes" -d          | Aktivuje režim ladenia pre podrobné zaznamenávanie.
migrate-links -l "language_codes" --save-logs, -s | Uloží záznamy úrovne DEBUG do súborov pod <root_dir>/logs/
migrate-links -l "all" -y                      | Spracuje všetky jazyky a automaticky potvrdí výzvu na upozornenie.

## Príklady použitia

  1. Predvolené správanie (pridá nové preklady bez mazania existujúcich):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridanie iba nových kórejských prekladov obrázkov (žiadne existujúce preklady sa nemažú):    translate -l "ko" -img

  3. Aktualizácia všetkých kórejských prekladov (Upozornenie: Toto vymaže všetky existujúce kórejské preklady pred opätovným prekladom):    translate -l "ko" -u

  4. Aktualizácia iba kórejských obrázkov (Upozornenie: Toto vymaže všetky existujúce kórejské obrázky pred opätovným prekladom):    translate -l "ko" -img -u

  5. Pridanie nových prekladov markdown pre kórejčinu bez ovplyvnenia ostatných prekladov:    translate -l "ko" -md

  6. Oprava prekladov s nízkou dôverou na základe predchádzajúcich výsledkov hodnotenia: translate -l "ko" --fix

  7. Oprava prekladov s nízkou dôverou iba pre špecifické súbory (markdown): translate -l "ko" --fix -md

  8. Oprava prekladov s nízkou dôverou iba pre špecifické súbory (obrázky): translate -l "ko" --fix -img

  9. Použitie rýchleho režimu pre preklad obrázkov:    translate -l "ko" -img -f

  10. Oprava prekladov s nízkou dôverou s vlastným prahom: translate -l "ko" --fix -c 0.8

  11. Príklad režimu ladenia: - translate -l "ko" -d: Aktivujte ladenie záznamov.
  12. Uloženie záznamov do súborov: translate -l "ko" -s
  13. DEBUG na konzole a v súbore: translate -l "ko" -d -s
  14. Prekladať bez pridávania upozornení o strojovom preklade do výstupov: translate -l "ko" --no-disclaimer

  15. Migrácia odkazov na notebooky pre kórejské preklady (aktualizovať odkazy na preložené notebooky, keď sú dostupné):    migrate-links -l "ko"

  15. Migrácia odkazov s suchým behom (žiadne zápisy do súborov):    migrate-links -l "ko" --dry-run

  16. Aktualizovať odkazy iba ak existujú preložené notebooky (nenahrádzať pôvodné):    migrate-links -l "ko" --no-fallback-to-original

  17. Spracovať všetky jazyky s výzvou na potvrdenie:    migrate-links -l "all"

  18. Spracovať všetky jazyky a automaticky potvrdiť:    migrate-links -l "all" -y
  19. Uložiť záznamy do súborov pre migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizovať sekciu jazykov v README s URL vaším repozitárom:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Príklady hodnotenia

> [!WARNING]  
> **Beta funkcia**: Funkcionalita hodnotenia je momentálne v beta verzii. Táto funkcia bola vydaná na hodnotenie preložených dokumentov, pričom metódy hodnotenia a detailná implementácia sú stále vo vývoji a môžu sa meniť.

  1. Hodnotenie kórejských prekladov: evaluate -l "ko"

  2. Hodnotenie s vlastným prahom dôveryhodnosti: evaluate -l "ko" -c 0.8

  3. Rýchle hodnotenie (len pravidlami): evaluate -l "ko" -f

  4. Hĺbkové hodnotenie (iba na báze LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by sa mal považovať za autorizovaný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek neporozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->