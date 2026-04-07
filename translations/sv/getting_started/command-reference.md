# Kommandoreferens

**Co-op Translator** CLI erbjuder flera alternativ för att anpassa översättningsprocessen:

Command                                       | Beskrivning
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Översätter ditt projekt till angivna språk. Exempel: translate -l "es fr de" översätter till spanska, franska och tyska. Använd translate -l "all" för att översätta till alla stödda språk.
translate -l "language_codes" -u              | Uppdaterar översättningar genom att ta bort befintliga och skapa dem på nytt. Varning: Detta kommer att ta bort alla nuvarande översättningar för angivna språk.
translate -l "language_codes" -img            | Översätter endast bildfiler.
translate -l "language_codes" -md             | Översätter endast Markdown-filer.
translate -l "language_codes" -nb             | Översätter endast Jupyter notebook-filer (.ipynb).
translate -l "language_codes" --fix           | Översätter om filer med låg förtroendescore baserat på tidigare utvärderingsresultat.
translate -l "language_codes" -d              | Aktiverar felsökningsläge för detaljerad loggning.
translate -l "language_codes" --save-logs, -s | Spara DEBUG-loggar till filer under <root_dir>/logs/ (konsolen styrs fortfarande av -d)
translate -l "language_codes" -r "root_dir"   | Anger rotkatalogen för projektet
translate -l "language_codes" -f              | Använder snabb läge för bildöversättning (upp till 3x snabbare rendering med något lägre kvalitet och justering).
translate -l "language_codes" -y              | Bekräftar automatiskt alla uppmaningar (användbart för CI/CD-pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktivera eller inaktivera tillägg av en avsnitt om maskinöversättningsansvarsfriskrivning i översätt markdown och notebooks (standard: aktiverat).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Anpassa README-avsnittet för språk med din repository-URL.
translate -l "language_codes" --help          | hjälpinformation inom CLI som visar tillgängliga kommandon
evaluate -l "language_code"                  | Utvärderar översättningskvalitet för ett specifikt språk och ger förtroendescore
evaluate -l "language_code" -c 0.8           | Utvärderar översättningar med anpassad förtroendetröskel
evaluate -l "language_code" -f               | Snabb utvärderingsläge (endast regelbaserat, ingen LLM)
evaluate -l "language_code" -D               | Djup utvärderingsläge (endast LLM-baserat, mer grundligt men långsammare)
evaluate -l "language_code" --save-logs, -s  | Spara DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "language_codes"             | Omskriv översatta Markdown-filer för att uppdatera länkar till notebooks (.ipynb). Föredrar översatta notebooks när tillgängliga; kan annars falla tillbaka på original.
migrate-links -l "language_codes" -r          | Ange projektets rotkatalog (standard: aktuell katalog).
migrate-links -l "language_codes" --dry-run   | Visa vilka filer som skulle ändras utan att skriva ändringar.
migrate-links -l "language_codes" --no-fallback-to-original | Uppdatera inte länkar till originalnotebooks när översatta motsvarigheter saknas (uppdaterar bara när översatt finns).
migrate-links -l "language_codes" -d          | Aktivera felsökningsläge för detaljerad loggning.
migrate-links -l "language_codes" --save-logs, -s | Spara DEBUG-loggar till filer under <root_dir>/logs/
migrate-links -l "all" -y                      | Bearbeta alla språk och bekräfta varningsprompt automatiskt.

## Användningsexempel

  1. Standardbeteende (lägg till nya översättningar utan att ta bort befintliga):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Lägg till endast nya koreanska bildöversättningar (inga befintliga översättningar tas bort):    translate -l "ko" -img

  3. Uppdatera alla koreanska översättningar (Varning: Detta raderar alla befintliga koreanska översättningar innan ny översättning):    translate -l "ko" -u

  4. Uppdatera endast koreanska bilder (Varning: Detta raderar alla befintliga koreanska bilder innan ny översättning):    translate -l "ko" -img -u

  5. Lägg till nya markdown-översättningar för koreanska utan att påverka andra översättningar:    translate -l "ko" -md

  6. Åtgärda översättningar med låg förtroende baserat på tidigare utvärderingsresultat: translate -l "ko" --fix

  7. Åtgärda översättningar med låg förtroende för specifika filer endast (markdown): translate -l "ko" --fix -md

  8. Åtgärda översättningar med låg förtroende för specifika filer endast (bilder): translate -l "ko" --fix -img

  9. Använd snabb läge för bildöversättning:    translate -l "ko" -img -f

  10. Åtgärda översättningar med låg förtroende med anpassad tröskel: translate -l "ko" --fix -c 0.8

  11. Exempel på felsökningsläge: - translate -l "ko" -d: Aktivera felsökningsloggning.
  12. Spara loggar till filer: translate -l "ko" -s
  13. Konsol-DEBUG och fil-DEBUG: translate -l "ko" -d -s
  14. Översätt utan att lägga till maskinöversättningsansvarsfriskrivningar i resultat: translate -l "ko" --no-disclaimer

  15. Migrera notebooklänkar för koreanska översättningar (uppdatera länkar till översatta notebooks när tillgängliga):    migrate-links -l "ko"

  15. Migrera länkar med torrkörning (inga filskrivningar):    migrate-links -l "ko" --dry-run

  16. Uppdatera endast länkar när översatta notebooks finns (inte fall tillbaka till original):    migrate-links -l "ko" --no-fallback-to-original

  17. Bearbeta alla språk med bekräftelseprompt:    migrate-links -l "all"

  18. Bearbeta alla språk och bekräfta automatiskt:    migrate-links -l "all" -y
  19. Spara loggar till filer för migrate-links:    migrate-links -l "ko ja" -s

  20. Anpassa README-språkrådet med din repo-URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Utvärderingsexempel

> [!WARNING]  
> **Beta-funktion**: Utvärderingsfunktionen är för närvarande i beta. Denna funktion släpptes för att utvärdera översatta dokument, och utvärderingsmetoder och detaljerad implementering är fortfarande under utveckling och kan ändras.

  1. Utvärdera koreanska översättningar: evaluate -l "ko"

  2. Utvärdera med anpassad förtroendetröskel: evaluate -l "ko" -c 0.8

  3. Snabb utvärdering (endast regelbaserat): evaluate -l "ko" -f

  4. Djup utvärdering (endast LLM-baserat): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var god uppmärksam på att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För viktig information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->