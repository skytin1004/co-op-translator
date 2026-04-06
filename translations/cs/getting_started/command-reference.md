# Command reference

The **Co-op Translator** CLI nabízí několik možností, jak přizpůsobit překladový proces:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Překládá váš projekt do zadaných jazyků. Příklad: translate -l "es fr de" překládá do španělštiny, francouzštiny a němčiny. Použijte translate -l "all" pro překlad do všech podporovaných jazyků.
translate -l "language_codes" -u              | Aktualizuje překlady odstraněním existujících a jejich znovuvytvořením. Varování: Toto vymaže všechny aktuální překlady pro zadané jazyky.
translate -l "language_codes" -img            | Překládá pouze obrazové soubory.
translate -l "language_codes" -md             | Překládá pouze Markdown soubory.
translate -l "language_codes" -nb             | Překládá pouze Jupyter notebook soubory (.ipynb).
translate -l "language_codes" --fix           | Překládá znovu soubory s nízkou úrovní důvěry na základě předchozích hodnotících výsledků.
translate -l "language_codes" -d              | Aktivuje režim ladění pro podrobné logování.
translate -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/ (konzole je stále řízena přepínačem -d)
translate -l "language_codes" -r "root_dir"   | Určuje kořenový adresář projektu
translate -l "language_codes" -f              | Používá rychlý režim pro překlad obrázků (až 3x rychlejší vykreslování s mírným poklesem kvality a zarovnání).
translate -l "language_codes" -y              | Automaticky potvrzuje všechny výzvy (užitečné pro CI/CD pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Povolit nebo zakázat přidání sekce o upozornění na strojový překlad do přeložených markdownů a notebooků (výchozí: povoleno).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalizovat doporučení o sekci jazyků v README (sparse checkout) pomocí URL vašeho repozitáře.
translate -l "language_codes" --help          | podrobnosti nápovědy v CLI zobrazující dostupné příkazy
evaluate -l "language_code"                  | Hodnotí kvalitu překladu pro konkrétní jazyk a poskytuje skóre důvěry
evaluate -l "language_code" -c 0.8           | Hodnotí překlady s vlastním prahem důvěry
evaluate -l "language_code" -f               | Rychlý režim hodnocení (pouze na základě pravidel, bez LLM)
evaluate -l "language_code" -D               | Hluboký režim hodnocení (pouze na základě LLM, důkladnější ale pomalejší)
evaluate -l "language_code" --save-logs, -s  | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "language_codes"             | Zpracuje znovu přeložené Markdown soubory pro aktualizaci odkazů na notebooky (.ipynb). Preferuje přeložené notebooky, pokud jsou dostupné; jinak může použít originální.
migrate-links -l "language_codes" -r          | Určuje kořenový adresář projektu (výchozí: aktuální adresář).
migrate-links -l "language_codes" --dry-run   | Ukáže, které soubory by se změnily, bez zápisu změn.
migrate-links -l "language_codes" --no-fallback-to-original | Neprovádí přepis odkazů na originální notebooky, pokud chybí překlad (aktualizuje pouze, když existuje překlad).
migrate-links -l "language_codes" -d          | Aktivuje režim ladění pro podrobné logování.
migrate-links -l "language_codes" --save-logs, -s | Uloží logy na úrovni DEBUG do souborů pod <root_dir>/logs/
migrate-links -l "all" -y                      | Zpracuje všechny jazyky a automaticky potvrdí varování.

## Použití - příklady

  1. Výchozí chování (přidat nové překlady bez mazání stávajících):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Přidat pouze nové korejské překlady obrázků (žádné stávající překlady nejsou mazány):    translate -l "ko" -img

  3. Aktualizovat všechny korejské překlady (Varování: Toto smaže všechny stávající korejské překlady před opětovným překladem):    translate -l "ko" -u

  4. Aktualizovat pouze korejské obrázky (Varování: Toto smaže všechny stávající korejské obrázky před opětovným překladem):    translate -l "ko" -img -u

  5. Přidat nové markdownové překlady pro korejštinu, aniž by se ovlivnily ostatní překlady:    translate -l "ko" -md

  6. Opravit překlady s nízkou důvěrou na základě předchozích hodnocení: translate -l "ko" --fix

  7. Opravit překlady s nízkou důvěrou pouze pro konkrétní soubory (markdown): translate -l "ko" --fix -md

  8. Opravit překlady s nízkou důvěrou pouze pro konkrétní soubory (obrázky): translate -l "ko" --fix -img

  9. Použít rychlý režim pro překlad obrázků:    translate -l "ko" -img -f

  10. Opravit překlady s nízkou důvěrou s vlastním prahem: translate -l "ko" --fix -c 0.8

  11. Příklad režimu ladění: - translate -l "ko" -d: Aktivovat ladící logování.
  12. Uložit logy do souborů: translate -l "ko" -s
  13. DEBUG v konzoli i v souborech: translate -l "ko" -d -s
  14. Překládat bez přidání upozornění o strojovém překladu do výstupů: translate -l "ko" --no-disclaimer

  15. Migrovat odkazy na notebooky pro korejské překlady (aktualizovat odkazy na přeložené notebooky, pokud jsou dostupné):    migrate-links -l "ko"

  15. Migrovat odkazy s dry-run (bez zápisu do souborů):    migrate-links -l "ko" --dry-run

  16. Aktualizovat odkazy pouze pokud existují přeložené notebooky (nezpětně použít originály):    migrate-links -l "ko" --no-fallback-to-original

  17. Zpracovat všechny jazyky s potvrzovacím dialogem:    migrate-links -l "all"

  18. Zpracovat všechny jazyky a automaticky potvrdit:    migrate-links -l "all" -y
  19. Uložit logy do souborů pro migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizovat doporučení v README týkající se jazyků s URL vašeho repozitáře:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Příklady hodnocení

> [!WARNING]  
> **Beta funkce**: Funkce hodnocení je momentálně v betě. Tato funkce byla vydána pro hodnocení přeložených dokumentů, metody hodnocení a podrobné implementace jsou stále ve vývoji a mohou se měnit.

  1. Hodnotit korejské překlady: evaluate -l "ko"

  2. Hodnotit s vlastním prahem důvěry: evaluate -l "ko" -c 0.8

  3. Rychlé hodnocení (pouze na základě pravidel): evaluate -l "ko" -f

  4. Hluboké hodnocení (pouze na základě LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoliv nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->