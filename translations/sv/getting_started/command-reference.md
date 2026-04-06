# Kommandoreferens

**Co-op Translator** CLI erbjuder flera alternativ för att anpassa översättningsprocessen:

Command                                       | Beskrivning
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Översätter ditt projekt till angivna språk. Exempel: translate -l "es fr de" översätter till spanska, franska och tyska. Använd translate -l "all" för att översätta till alla stödda språk.
translate -l "language_codes" -u              | Uppdaterar översättningar genom att ta bort befintliga och skapa dem på nytt. Varning: Detta kommer att ta bort alla nuvarande översättningar för angivna språk.
translate -l "language_codes" -img            | Översätter endast bildfiler.
translate -l "language_codes" -md             | Översätter endast Markdown-filer.
translate -l "language_codes" -nb             | Översätter endast Jupyter-notebookfiler (.ipynb).
translate -l "language_codes" --fix           | Omöversätter filer med låga förtroendepoäng baserat på tidigare evalueringsresultat.
translate -l "language_codes" -d              | Aktiverar debug-läge för detaljerad loggning.
translate -l "language_codes" --save-logs, -s | Sparar DEBUG-loggar till filer under <root_dir>/logs/ (konsollen styrs fortfarande av -d)
translate -l "language_codes" -r "root_dir"   | Anger projektets rotkatalog
translate -l "language_codes" -f              | Använder snabbt läge för bildöversättning (upp till 3x snabbare renderering med viss kostnad för kvalitet och justering).
translate -l "language_codes" -y              | Bekräftar automatiskt alla uppmaningar (nyttigt för CI/CD-pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktivera eller inaktivera tillägget av en maskinöversättningsansvarsfriskrivningssektion till översatta markdown- och notebookfiler (standard: aktiverat).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalisera README-språkssektionens vägledning (sparse checkout) med din repository-URL.
translate -l "language_codes" --help          | Hjälpdetaljer i CLI som visar tillgängliga kommandon
evaluate -l "language_code"                  | Utvärderar översättningskvalitet för ett specifikt språk och ger förtroendepoäng
evaluate -l "language_code" -c 0.8           | Utvärderar översättningar med anpassad förtroendetröskel
evaluate -l "language_code" -f               | Snabb utvärderingsläge (endast regelbaserat, inget LLM)
evaluate -l "language_code" -D               | Djup utvärderingsläge (endast LLM-baserat, mer grundligt men långsammare)
evaluate -l "language_code" --save-logs, -s  | Sparar DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "language_codes"             | Ominläser översatta Markdown-filer för att uppdatera länkar till notebooks (.ipynb). Föredrar översatta notebooks när de finns; kan annars återgå till originalnotebooks.
migrate-links -l "language_codes" -r          | Ange projektets rotkatalog (standard: aktuell katalog).
migrate-links -l "language_codes" --dry-run   | Visa vilka filer som skulle ändras utan att skriva ändringar.
migrate-links -l "language_codes" --no-fallback-to-original | Skriv inte om länkar till originalnotebooks när översatta motsvarigheter saknas (uppdatera bara när översatt finns).
migrate-links -l "language_codes" -d          | Aktivera debug-läge för detaljerad loggning.
migrate-links -l "language_codes" --save-logs, -s | Sparar DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Behandla alla språk och automatiskt bekräfta varningsprompten.

## Användningsexempel

  1. Standardbeteende (lägg till nya översättningar utan att ta bort befintliga):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lägg endast till nya koreanska bildöversättningar (inga befintliga översättningar tas bort):    translate -l "ko" -img

  3. Uppdatera alla koreanska översättningar (Varning: Detta tar bort alla befintliga koreanska översättningar innan ominläsning):    translate -l "ko" -u

  4. Uppdatera endast koreanska bilder (Varning: Detta tar bort alla befintliga koreanska bilder innan ominläsning):    translate -l "ko" -img -u

  5. Lägg till nya markdown-översättningar för koreanska utan att påverka andra översättningar:    translate -l "ko" -md

  6. Åtgärda översättningar med lågt förtroende baserat på tidigare utvärderingsresultat: translate -l "ko" --fix

  7. Åtgärda översättningar med lågt förtroende för specifika filer endast (markdown): translate -l "ko" --fix -md

  8. Åtgärda översättningar med lågt förtroende för specifika filer endast (bilder): translate -l "ko" --fix -img

  9. Använd snabbt läge för bildöversättning:    translate -l "ko" -img -f

  10. Åtgärda översättningar med lågt förtroende med anpassad tröskel: translate -l "ko" --fix -c 0.8

  11. Exempel på debug-läge: - translate -l "ko" -d: Aktivera debug-loggning.
  12. Spara loggar till filer: translate -l "ko" -s
  13. Konsoll DEBUG och fil DEBUG: translate -l "ko" -d -s
  14. Översätt utan att lägga till ansvarsfriskrivningar för maskinöversättning i utdata: translate -l "ko" --no-disclaimer

  15. Migrera notebook-länkar för koreanska översättningar (uppdatera länkar till översatta notebooks när de finns):    migrate-links -l "ko"

  15. Migrera länkar med dry-run (ingen filskrivning):    migrate-links -l "ko" --dry-run

  16. Uppdatera endast länkar när översatta notebooks finns (inte återgå till original):    migrate-links -l "ko" --no-fallback-to-original

  17. Bearbeta alla språk med bekräftelseprompt:    migrate-links -l "all"

  18. Bearbeta alla språk och bekräfta automatiskt:    migrate-links -l "all" -y
  19. Spara loggar till filer för migrate-links:    migrate-links -l "ko ja" -s

  20. Personalisera README-språkråd med din repo-URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exempel på utvärdering

> [!WARNING]  
> **Beta-funktion**: Utvärderingsfunktionen är för närvarande i beta. Denna funktion släpptes för att utvärdera översatta dokument, och utvärderingsmetoderna samt detaljerad implementering är fortfarande under utveckling och kan komma att ändras.

  1. Utvärdera koreanska översättningar: evaluate -l "ko"

  2. Utvärdera med anpassad förtroendetröskel: evaluate -l "ko" -c 0.8

  3. Snabb utvärdering (endast regelbaserat): evaluate -l "ko" -f

  4. Djup utvärdering (endast LLM-baserat): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var god observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->