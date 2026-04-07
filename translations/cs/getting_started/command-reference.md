# Příkazový přehled

CLI **Co-op Translator** nabízí několik možností, jak přizpůsobit proces překladu:

Příkaz                                      | Popis
--------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Překládá váš projekt do zadaných jazyků. Příklad: translate -l "es fr de" přeloží do španělštiny, francouzštiny a němčiny. Použijte translate -l "all" pro překlad do všech podporovaných jazyků.
translate -l "language_codes" -u             | Aktualizuje překlady vymazáním stávajících a jejich znovuvytvořením. Pozor: Tímto se smažou všechny aktuální překlady pro zadané jazyky.
translate -l "language_codes" -img           | Překládá pouze obrázkové soubory.
translate -l "language_codes" -md            | Překládá pouze Markdown soubory.
translate -l "language_codes" -nb            | Překládá pouze soubory Jupyter notebooků (.ipynb).
translate -l "language_codes" --fix          | Znovu překládá soubory s nízkým skóre jistoty na základě předchozích výsledků hodnocení.
translate -l "language_codes" -d             | Zapne ladicí režim pro podrobné logování.
translate -l "language_codes" --save-logs, -s| Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/ (konzole je nadále řízena -d)
translate -l "language_codes" -r "root_dir"  | Určuje kořenový adresář projektu
translate -l "language_codes" -f             | Používá rychlý režim pro překlad obrázků (až 3x rychlejší vykreslování s mírným snížením kvality a zarovnání).
translate -l "language_codes" -y             | Automaticky potvrdí všechny výzvy (užitečné pro CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Povolit nebo zakázat přidání sekce upozornění o strojovém překladu do přeložených markdownů a notebooků (výchozí: povoleno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizuje sekci doporučení jazyků v README (sparse checkout) s URL vašeho repozitáře.
translate -l "language_codes" --help         | Zobrazí podrobnosti nápovědy v CLI, které ukazují dostupné příkazy
evaluate -l "language_code"                  | Hodnotí kvalitu překladu pro konkrétní jazyk a poskytuje skóre jistoty
evaluate -l "language_code" -c 0.8           | Hodnotí překlady s vlastním prahem jistoty
evaluate -l "language_code" -f               | Rychlý režim hodnocení (pouze na základě pravidel, bez LLM)
evaluate -l "language_code" -D               | Hloubkové hodnocení (pouze na bázi LLM, důkladnější, ale pomalejší)
evaluate -l "language_code" --save-logs, -s  | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "language_codes"             | Zpracuje přeložené Markdown soubory znovu, aby aktualizoval odkazy na notebooky (.ipynb). Preferuje přeložené notebooky, pokud jsou k dispozici; jinak může použít originální notebooky.
migrate-links -l "language_codes" -r          | Určuje kořenový adresář projektu (výchozí: aktuální adresář).
migrate-links -l "language_codes" --dry-run   | Zobrazí, které soubory by se změnily, aniž by změny zapsal.
migrate-links -l "language_codes" --no-fallback-to-original | Neprovádí přepisování odkazů na originální notebooky, pokud chybí přeložené verze (aktualizuje pouze, když přeložená verze existuje).
migrate-links -l "language_codes" -d          | Zapne ladicí režim pro podrobné logování.
migrate-links -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "all" -y                      | Zpracuje všechny jazyky a automaticky potvrdí varovnou výzvu.

## Příklady použití

  1. Výchozí chování (přidá nové překlady bez mazání existujících):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Přidat pouze nové korejské překlady obrázků (nebudou smazány žádné existující překlady):    translate -l "ko" -img

  3. Aktualizovat všechny korejské překlady (Pozor: Toto smaže všechny stávající korejské překlady před novým překladem):    translate -l "ko" -u

  4. Aktualizovat pouze korejské obrázky (Pozor: Toto smaže všechny existující korejské obrázky před opětovným překladem):    translate -l "ko" -img -u

  5. Přidat nové markdown překlady pro korejštinu aniž by to ovlivnilo jiné překlady:    translate -l "ko" -md

  6. Opravit překlady s nízkou jistotou na základě předchozích výsledků hodnocení: translate -l "ko" --fix

  7. Opravit překlady s nízkou jistotou pouze pro konkrétní soubory (markdown): translate -l "ko" --fix -md

  8. Opravit překlady s nízkou jistotou pouze pro konkrétní soubory (obrázky): translate -l "ko" --fix -img

  9. Použít rychlý režim pro překlad obrázků:    translate -l "ko" -img -f

  10. Opravit překlady s nízkou jistotou s vlastním prahem: translate -l "ko" --fix -c 0.8

  11. Příklad ladicího režimu: - translate -l "ko" -d: Zapnout ladicí logování.
  12. Uložit logy do souborů: translate -l "ko" -s
  13. DEBUG v konzoli a DEBUG v souborech: translate -l "ko" -d -s
  14. Překládat bez přidávání upozornění o strojovém překladu do výstupů: translate -l "ko" --no-disclaimer

  15. Migrovat odkazy na notebooky pro korejské překlady (aktualizovat odkazy na přeložené notebooky, pokud jsou k dispozici):    migrate-links -l "ko"

  15. Migrovat odkazy s dry-run (bez zápisu do souborů):    migrate-links -l "ko" --dry-run

  16. Aktualizovat odkazy pouze pokud existují přeložené notebooky (nepoužívat zpětný přechod na originály):    migrate-links -l "ko" --no-fallback-to-original

  17. Zpracovat všechny jazyky s potvrzovací výzvou:    migrate-links -l "all"

  18. Zpracovat všechny jazyky a automaticky potvrdit:    migrate-links -l "all" -y
  19. Uložit logy do souborů pro migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizovat doporučení jazyků v README s URL vašeho repozitáře:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Příklady hodnocení

> [!WARNING]  
> **Beta Funkce**: Funkce hodnocení je momentálně v beta verzi. Tato funkce byla vydána pro hodnocení přeložených dokumentů, a metody hodnocení i detailní implementace jsou stále ve vývoji a mohou se měnit.

  1. Ohodnotit korejské překlady: evaluate -l "ko"

  2. Hodnocení s vlastním prahem jistoty: evaluate -l "ko" -c 0.8

  3. Rychlé hodnocení (pouze na základě pravidel): evaluate -l "ko" -f

  4. Hloubkové hodnocení (pouze na bázi LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->