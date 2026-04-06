# Parancs referencia

A **Co-op Translator** CLI több lehetőséget kínál a fordítási folyamat testreszabására:

Parancs                                       | Leírás
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Lefordítja projektjét a megadott nyelvekre. Példa: translate -l "es fr de" spanyolra, franciára és németre fordít. Használja a translate -l "all" parancsot az összes támogatott nyelv fordításához.
translate -l "language_codes" -u              | Frissíti a fordításokat azáltal, hogy törli a meglévőket és újra létrehozza őket. Figyelem: Ez törli az összes jelenlegi fordítást a megadott nyelveken.
translate -l "language_codes" -img            | Csak a képfájlokat fordítja le.
translate -l "language_codes" -md             | Csak a Markdown fájlokat fordítja le.
translate -l "language_codes" -nb             | Csak a Jupyter notebook fájlokat (.ipynb) fordítja le.
translate -l "language_codes" --fix           | Újrafordítja az alacsony bizalmi pontszámú fájlokat korábbi értékelési eredmények alapján.
translate -l "language_codes" -d              | Debug mód engedélyezése részletes naplózáshoz.
translate -l "language_codes" --save-logs, -s | DEBUG szintű naplók mentése a <root_dir>/logs/ könyvtárba (a konzol továbbra is a -d vezérli)
translate -l "language_codes" -r "root_dir"   | A projekt gyökérkönyvtárának megadása
translate -l "language_codes" -f              | Gyors mód használata képfájlok fordítására (akár 3-szor gyorsabb megjelenítés kisebb minőség- és illesztési kompromisszummal).
translate -l "language_codes" -y              | Automatikusan megerősít minden kérést (hasznos CI/CD pipeline-okhoz)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Gép fordítási nyilatkozat szekció engedélyezése vagy tiltása a lefordított markdownokban és notebookokban (alapértelmezett: engedélyezett).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Személyre szabja a README nyelvi szakasz tanácsát (ritka checkout) a repozitórium URL-jével.
translate -l "language_codes" --help          | a CLI-n belüli súgó részletei az elérhető parancsokról
evaluate -l "language_code"                  | Értékeli egy adott nyelv fordítási minőségét és bizalmi pontszámokat ad meg
evaluate -l "language_code" -c 0.8           | Egyedi bizalmi küszöbértékkel értékeli a fordításokat
evaluate -l "language_code" -f               | Gyors értékelési mód (csak szabályalapú, nem LLM)
evaluate -l "language_code" -D               | Mély értékelési mód (csak LLM alapú, alaposabb, de lassabb)
evaluate -l "language_code" --save-logs, -s  | DEBUG szintű naplók mentése a <root_dir>/logs/ könyvtárba
migrate-links -l "language_codes"             | Újrafeldolgozza a lefordított Markdown fájlokat a notebookok (.ipynb) linkjeinek frissítéséhez. Előnyben részesíti a lefordított notebookokat, ha azok rendelkezésre állnak; különben áttérhet az eredeti notebookokra.
migrate-links -l "language_codes" -r          | A projekt gyökérkönyvtárának megadása (alapértelmezett: aktuális könyvtár).
migrate-links -l "language_codes" --dry-run   | Megmutatja, mely fájlok változnának, anélkül hogy ténylegesen írná a változtatásokat.
migrate-links -l "language_codes" --no-fallback-to-original | Nem írja át a linkeket az eredeti notebookokra, ha hiányoznak a lefordított megfelelőik (csak akkor frissít, ha lefordított létezik).
migrate-links -l "language_codes" -d          | Debug mód engedélyezése részletes naplózáshoz.
migrate-links -l "language_codes" --save-logs, -s | DEBUG szintű naplók mentése a <root_dir>/logs/ könyvtárba
migrate-links -l "all" -y                      | Minden nyelv feldolgozása és a figyelmeztető kérdés automatikus megerősítése.

## Használati példák

  1. Alapértelmezett viselkedés (új fordítások hozzáadása a meglévők törlése nélkül):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Csak új koreai kép fordítások hozzáadása (a meglévő fordítások nem törlődnek):    translate -l "ko" -img

  3. Az összes koreai fordítás frissítése (Figyelem: Ez törli az összes meglévő koreai fordítást az újrafordítás előtt):    translate -l "ko" -u

  4. Csak koreai képek frissítése (Figyelem: Ez törli az összes meglévő koreai képet az újrafordítás előtt):    translate -l "ko" -img -u

  5. Új markdown fordítások hozzáadása koreaihoz anélkül, hogy más fordításokat érintene:    translate -l "ko" -md

  6. Alacsony bizalmi fordítások javítása korábbi értékelési eredmények alapján: translate -l "ko" --fix

  7. Alacsony bizalmi fordítások javítása csak specifikus fájloknál (markdown): translate -l "ko" --fix -md

  8. Alacsony bizalmi fordítások javítása csak specifikus fájloknál (képek): translate -l "ko" --fix -img

  9. Gyors mód használata képfordításhoz:    translate -l "ko" -img -f

  10. Alacsony bizalmi fordítások javítása egyedi küszöbértékkel: translate -l "ko" --fix -c 0.8

  11. Debug mód példa: - translate -l "ko" -d: Debug naplózás engedélyezése.
  12. Naplók fájlba mentése: translate -l "ko" -s
  13. Konzol DEBUG és fájl DEBUG: translate -l "ko" -d -s
  14. Fordítások gépi fordítási nyilatkozat nélkül: translate -l "ko" --no-disclaimer

  15. Notebook linkek átvitele koreai fordításokhoz (a lefordított notebookok linkjeinek frissítése ahol elérhető):    migrate-links -l "ko"

  15. Link átállítás száraz futással (módosítás nélküli megjelenítés):    migrate-links -l "ko" --dry-run

  16. Csak akkor frissíti a linkeket, ha lefordított notebookok vannak (nem tér vissza az eredetiekhez):    migrate-links -l "ko" --no-fallback-to-original

  17. Minden nyelv feldolgozása megerősítő kérdéssel:    migrate-links -l "all"

  18. Minden nyelv feldolgozása és automatikus megerősítés:    migrate-links -l "all" -y
  19. Naplók mentése migrate-links számára:    migrate-links -l "ko ja" -s

  20. README nyelvi tanácsának személyre szabása a saját repozitórium URL-jével:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Értékelési példák

> [!WARNING]  
> **Béta funkció**: Az értékelési funkció jelenleg béta állapotban van. Ez a funkció a lefordított dokumentumok értékelésére lett kiadva, és az értékelési módszerek és részletes megvalósítás még fejlesztés alatt áll, változhat.

  1. Koreai fordítások értékelése: evaluate -l "ko"

  2. Egyedi bizalmi küszöbértékkel való értékelés: evaluate -l "ko" -c 0.8

  3. Gyors értékelés (csak szabályalapú): evaluate -l "ko" -f

  4. Mély értékelés (csak LLM alapú): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatásával készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum a saját nyelvén számít hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->