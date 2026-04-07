# Referencia príkazov

CLI **Co-op Translator** ponúka niekoľko možností na prispôsobenie prekladového procesu:

Príkaz                                      | Popis
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"               | Prekladá váš projekt do zadaných jazykov. Príklad: translate -l "es fr de" prekladá do španielčiny, francúzštiny a nemčiny. Použite translate -l "all" na preklad do všetkých podporovaných jazykov.
translate -l "language_codes" -u            | Aktualizuje preklady vymazaním existujúcich a ich opätovným vytvorením. Upozornenie: Toto vymaže všetky aktuálne preklady pre zadané jazyky.
translate -l "language_codes" -img          | Prekladá iba obrazové súbory.
translate -l "language_codes" -md           | Prekladá iba Markdown súbory.
translate -l "language_codes" -nb           | Prekladá iba Jupyter notebook súbory (.ipynb).
translate -l "language_codes" --fix         | Opätovne prekladá súbory s nízkou dôverou na základe predchádzajúcich hodnotení.
translate -l "language_codes" -d             | Aktivuje režim ladenia pre podrobné zaznamenávanie.
translate -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do súborov v <root_dir>/logs/ (konzola je riadená parametrom -d)
translate -l "language_codes" -r "root_dir" | Určuje koreňový adresár projektu
translate -l "language_codes" -f             | Používa rýchly režim pre preklad obrázkov (až 3x rýchlejšie vykresľovanie za mierny úbytok kvality a zarovnania).
translate -l "language_codes" -y             | Automaticky potvrdzuje všetky výzvy (užitočné pre CI/CD pipeline)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Povoliť alebo zakázať pridávanie sekcie upozornenia o strojovom preklade do preložených markdownov a notebookov (predvolené: povolené).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizujte sekciu jazykov v README (sparse checkout) pomocou URL vášho repozitára.
translate -l "language_codes" --help        | Zobrazenie nápovedy v CLI s dostupnými príkazmi
evaluate -l "language_code"                  | Vyhodnotí kvalitu prekladu pre konkrétny jazyk a poskytne skóre dôvery
evaluate -l "language_code" -c 0.8           | Vyhodnotí preklady s vlastným prahom dôvery
evaluate -l "language_code" -f               | Rýchly režim hodnotenia (iba pravidlami, bez LLM)
evaluate -l "language_code" -D               | Hlboký režim hodnotenia (iba LLM, dôkladnejší, ale pomalší)
evaluate -l "language_code" --save-logs, -s  | Uloží logy na úrovni DEBUG do súborov v <root_dir>/logs/
migrate-links -l "language_codes"             | Prepracuje preložené Markdown súbory na aktualizáciu odkazov na notebooky (.ipynb). Preferuje preložené notebooky, keď sú dostupné; inak môže použiť pôvodné notebooky.
migrate-links -l "language_codes" -r          | Určuje koreňový adresár projektu (predvolené: aktuálny adresár).
migrate-links -l "language_codes" --dry-run   | Zobrazí, ktoré súbory by sa zmenili, bez zapisovania zmien.
migrate-links -l "language_codes" --no-fallback-to-original | Neaktualizuje odkazy na pôvodné notebooky, keď chýbajú preložené verzie (aktualizuje iba, keď je preložený existujúci).
migrate-links -l "language_codes" -d          | Aktivuje režim ladenia pre podrobné zaznamenávanie.
migrate-links -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do súborov v <root_dir>/logs/
migrate-links -l "all" -y                      | Spracuje všetky jazyky a automaticky potvrdí výzvu na potvrdenie.

## Príklady použitia

  1. Predvolené správanie (pridať nové preklady bez vymazania existujúcich):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Pridať iba nové kórejské preklady obrázkov (žiadne existujúce preklady nie sú vymazané):    translate -l "ko" -img

  3. Aktualizovať všetky kórejské preklady (Upozornenie: Toto vymaže všetky existujúce kórejské preklady pred opätovným prekladom):    translate -l "ko" -u

  4. Aktualizovať iba kórejské obrázky (Upozornenie: Toto vymaže všetky existujúce kórejské obrázky pred opätovným prekladom):    translate -l "ko" -img -u

  5. Pridať nové markdown preklady pre kórejčinu bez ovplyvnenia iných prekladov:    translate -l "ko" -md

  6. Opraviť preklady s nízkou dôverou na základe predchádzajúcich hodnotení: translate -l "ko" --fix

  7. Opraviť preklady s nízkou dôverou iba pre konkrétne súbory (markdown): translate -l "ko" --fix -md

  8. Opraviť preklady s nízkou dôverou iba pre konkrétne súbory (obrázky): translate -l "ko" --fix -img

  9. Použiť rýchly režim pre preklad obrázkov:    translate -l "ko" -img -f

  10. Opraviť preklady s nízkou dôverou s vlastným prahom: translate -l "ko" --fix -c 0.8

  11. Príklad režimu ladenia: - translate -l "ko" -d: Aktivuje logovanie ladenia.
  12. Uložiť logy do súborov: translate -l "ko" -s
  13. Konzola DEBUG a súbor DEBUG: translate -l "ko" -d -s
  14. Prekladať bez pridávania upozornení o strojovom preklade do výstupov: translate -l "ko" --no-disclaimer

  15. Migrovať odkazy na notebooky pre kórejské preklady (aktualizovať odkazy na preložené notebooky, keď sú dostupné):    migrate-links -l "ko"

  15. Migrovať odkazy s dry-run (bez zápisu do súborov):    migrate-links -l "ko" --dry-run

  16. Aktualizovať odkazy iba keď existujú preložené notebooky (nevykonávať návrat k pôvodným):    migrate-links -l "ko" --no-fallback-to-original

  17. Spracovať všetky jazyky s výzvou na potvrdenie:    migrate-links -l "all"

  18. Spracovať všetky jazyky a automaticky potvrdiť:    migrate-links -l "all" -y
  19. Uložiť logy do súborov pre migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizovať informácie o jazykoch v README s URL vaším repozitárom:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Príklady hodnotenia

> [!WARNING]  
> **Beta Funkcia**: Funkcia hodnotenia je momentálne v beta verzii. Táto funkcia bola uvoľnená na hodnotenie preložených dokumentov a metódy hodnotenia a detailná implementácia sú stále vo vývoji a môžu sa meniť.

  1. Vyhodnotiť kórejské preklady: evaluate -l "ko"

  2. Vyhodnotiť s vlastným prahom dôvery: evaluate -l "ko" -c 0.8

  3. Rýchle hodnotenie (len pravidlami): evaluate -l "ko" -f

  4. Hlboké hodnotenie (len LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->