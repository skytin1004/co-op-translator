# Parancs referencia

A **Co-op Translator** CLI több opciót kínál a fordítási folyamat testreszabásához:

Parancs                                        | Leírás
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                  | Lefordítja projektjét a megadott nyelvekre. Példa: translate -l "es fr de" spanyolra, franciára és németre fordít. Használja a translate -l "all" parancsot az összes támogatott nyelvre történő fordításhoz.
translate -l "language_codes" -u               | Frissíti a fordításokat úgy, hogy törli a meglévőket és újra létrehozza őket. Figyelem: Ez törli az adott nyelvek összes aktuális fordítását.
translate -l "language_codes" -img             | Csak a képfájlokat fordítja le.
translate -l "language_codes" -md              | Csak a Markdown fájlokat fordítja le.
translate -l "language_codes" -nb              | Csak a Jupyter notebook fájlokat (.ipynb) fordítja le.
translate -l "language_codes" --fix            | Újrafordítja az alacsony bizalmi pontszámú fájlokat a korábbi értékelési eredmények alapján.
translate -l "language_codes" -d               | Engedélyezi a debug módot a részletes naplózás érdekében.
translate -l "language_codes" --save-logs, -s  | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtár alá (a konzol vezérlése a -d kapcsolóval történik)
translate -l "language_codes" -r "root_dir"    | Megadja a projekt gyökérkönyvtárát
translate -l "language_codes" -f               | Gyors módot használ a képfordításhoz (akár 3x gyorsabb ábrázolás kisebb minőség- és illeszkedésveszteséggel).
translate -l "language_codes" -y               | Automatikusan megerősíti az összes párbeszédet (hasznos CI/CD pipeline-okhoz)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Engedélyezi vagy letiltja a gépi fordítási felelősségvállalási szakasz hozzáadását a lefordított markdown és notebookokhoz (alapértelmezett: engedélyezett).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Személyre szabja a README nyelvi szakaszának tájékoztatóját (száraz checkout) a saját repository URL-jével.
translate -l "language_codes" --help           | súgó részletek a CLI-n belül az elérhető parancsokról
evaluate -l "language_code"                     | Értékeli a fordítás minőségét egy adott nyelven és bizalmi pontszámokat szolgáltat
evaluate -l "language_code" -c 0.8              | Egyéni bizalmi küszöbértékkel értékeli a fordításokat
evaluate -l "language_code" -f                  | Gyors értékelési mód (csak szabályalapú, nem LLM)
evaluate -l "language_code" -D                  | Mélyértékelési mód (csak LLM alapú, alaposabb, de lassabb)
evaluate -l "language_code" --save-logs, -s     | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtár alá
migrate-links -l "language_codes"                | Újrafeldolgozza a lefordított Markdown fájlokat az .ipynb notebookokra mutató hivatkozások frissítéséhez. Előnyben részesíti a lefordított notebookokat, ha elérhetők; ellenkező esetben visszatérhet az eredeti notebookokra.
migrate-links -l "language_codes" -r             | Megadja a projekt gyökérkönyvtárát (alapértelmezett: aktuális könyvtár).
migrate-links -l "language_codes" --dry-run      | Megmutatja, mely fájlok változnának, de nem írja át a fájlokat.
migrate-links -l "language_codes" --no-fallback-to-original | Nem írja át az eredeti notebookokra mutató linkeket, ha hiányoznak a lefordított változatok (csak akkor frissít, ha a lefordított létezik).
migrate-links -l "language_codes" -d             | Engedélyezi a debug módot a részletes naplózás érdekében.
migrate-links -l "language_codes" --save-logs, -s | DEBUG szintű naplókat ment fájlokba a <root_dir>/logs/ könyvtár alá
migrate-links -l "all" -y                         | Minden nyelvet feldolgoz, és automatikusan megerősíti a figyelmeztető párbeszédet.

## Használati példák

  1. Alapértelmezett viselkedés (új fordításokat ad hozzá a meglévők törlése nélkül):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Csak új koreai képfordításokat ad hozzá (nem törli a meglévő fordításokat):    translate -l "ko" -img

  3. Frissíti az összes koreai fordítást (Figyelem: Ez törli az összes meglévő koreai fordítást a újrafordítás előtt):    translate -l "ko" -u

  4. Csak a koreai képeket frissíti (Figyelem: Ez törli az összes meglévő koreai képet az újrafordítás előtt):    translate -l "ko" -img -u

  5. Csak új markdown fordításokat ad hozzá koreai nyelven a többi fordítás érintése nélkül:    translate -l "ko" -md

  6. Javítja az alacsony bizalmú fordításokat a korábbi értékelési eredmények alapján: translate -l "ko" --fix

  7. Javítja az alacsony bizalmú fordításokat csak meghatározott fájloknál (markdown): translate -l "ko" --fix -md

  8. Javítja az alacsony bizalmú fordításokat csak meghatározott fájloknál (képek): translate -l "ko" --fix -img

  9. Gyors mód használata képfordításhoz:    translate -l "ko" -img -f

  10. Egyéni küszöbértékkel javítja az alacsony bizalmú fordításokat: translate -l "ko" --fix -c 0.8

  11. Debug mód példa: - translate -l "ko" -d: Engedélyezi a debug naplózást.
  12. Naplók mentése fájlokba: translate -l "ko" -s
  13. Konzol DEBUG és fájl DEBUG: translate -l "ko" -d -s
  14. Fordítás gépi fordítási felelősségvállalás hozzáadása nélkül: translate -l "ko" --no-disclaimer

  15. Notebook linkek migrálása koreai fordításokhoz (frissíti a linkeket a lefordított notebookokra, ha elérhetők):    migrate-links -l "ko"

  15. Linkek migrálása dry-run módban (fájlírás nélkül):    migrate-links -l "ko" --dry-run

  16. Csak akkor frissíti a linkeket, ha a lefordított notebookok léteznek (nem használ visszafejlődést az eredetiekhez):    migrate-links -l "ko" --no-fallback-to-original

  17. Minden nyelv feldolgozása megerősítő párbeszéddel:    migrate-links -l "all"

  18. Minden nyelv feldolgozása és automatikus megerősítés:    migrate-links -l "all" -y
  19. Naplók mentése fájlokba a migrate-links esetén:    migrate-links -l "ko ja" -s

  20. README nyelvi tájékoztató személyre szabása a repo URL-jével:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Értékelési példák

> [!WARNING]  
> **Béta funkció**: Az értékelési funkció jelenleg béta állapotban van. Ezt a funkciót a lefordított dokumentumok értékelésére adták ki, és az értékelési módszerek, valamint a részletes megvalósítás még fejlesztés alatt állnak, változhatnak.

  1. Koreai fordítások értékelése: evaluate -l "ko"

  2. Egyéni bizalmi küszöbértékkel értékelés: evaluate -l "ko" -c 0.8

  3. Gyors értékelés (csak szabályalapú): evaluate -l "ko" -f

  4. Mélyértékelés (csak LLM alapú): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével került lefordításra. Bár az alaposságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->