# Commandoreferentie

De **Co-op Translator** CLI biedt verschillende opties om het vertaalproces aan te passen:

Command                                       | Beschrijving
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Vertaalt je project naar de opgegeven talen. Voorbeeld: translate -l "es fr de" vertaalt naar Spaans, Frans en Duits. Gebruik translate -l "all" om naar alle ondersteunde talen te vertalen.
translate -l "language_codes" -u              | Werk vertalingen bij door bestaande te verwijderen en opnieuw te maken. Waarschuwing: Dit verwijdert alle huidige vertalingen voor opgegeven talen.
translate -l "language_codes" -img            | Vertaalt alleen afbeeldingsbestanden.
translate -l "language_codes" -md             | Vertaalt alleen Markdown-bestanden.
translate -l "language_codes" -nb             | Vertaalt alleen Jupyter-notebookbestanden (.ipynb).
translate -l "language_codes" --fix           | Vertaal opnieuw bestanden met lage betrouwbaarheidscores op basis van eerdere evaluatieresultaten.
translate -l "language_codes" -d              | Schakelt debugmodus in voor gedetailleerde logging.
translate -l "language_codes" --save-logs, -s | Sla DEBUG-level logs op in bestanden onder <root_dir>/logs/ (console wordt geregeld door -d)
translate -l "language_codes" -r "root_dir"   | Geeft de hoofdmap van het project op
translate -l "language_codes" -f              | Gebruikt snelle modus voor afbeeldingsvertaling (tot 3x snellere plotting met een lichte vermindering van kwaliteit en uitlijning).
translate -l "language_codes" -y              | Bevestig automatisch alle prompts (handig voor CI/CD-pijplijnen)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Schakel het toevoegen van een disclaimersectie voor machinale vertaling in of uit in vertaalde markdown en notebooks (standaard: ingeschakeld).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliseer het README-talenadvies (sparse checkout) met uw repository-URL.
translate -l "language_codes" --help          | hulpdetails binnen de CLI met beschikbare commando's
evaluate -l "language_code"                  | Evalueert de vertaalkwaliteit voor een specifieke taal en geeft betrouwbaarheidscores
evaluate -l "language_code" -c 0.8           | Evalueert vertalingen met aangepaste betrouwbaarheidsdrempel
evaluate -l "language_code" -f               | Snelle evaluatiemodus (alleen regelgebaseerd, geen LLM)
evaluate -l "language_code" -D               | Diepe evaluatiemodus (alleen LLM-gebaseerd, grondiger maar langzamer)
evaluate -l "language_code" --save-logs, -s  | Sla DEBUG-level logs op in bestanden onder <root_dir>/logs/
migrate-links -l "language_codes"             | Verwerk vertaalde Markdown-bestanden opnieuw om links naar notebooks (.ipynb) bij te werken. Geeft de voorkeur aan vertaalde notebooks indien beschikbaar; anders kan teruggevallen worden op originele notebooks.
migrate-links -l "language_codes" -r          | Geef de project-hoofdmap op (standaard: huidige map).
migrate-links -l "language_codes" --dry-run   | Toon welke bestanden zouden veranderen zonder wijzigingen weg te schrijven.
migrate-links -l "language_codes" --no-fallback-to-original | Herschrijf links naar originele notebooks niet als vertaalde tegenhangers ontbreken (update alleen wanneer vertaling bestaat).
migrate-links -l "language_codes" -d          | Schakel debugmodus in voor gedetailleerde logging.
migrate-links -l "language_codes" --save-logs, -s | Sla DEBUG-level logs op in bestanden onder <root_dir>/logs/
migrate-links -l "all" -y                      | Verwerk alle talen en bevestig waarschuwingsprompt automatisch.

## Gebruik voorbeelden

  1. Standaardgedrag (voeg nieuwe vertalingen toe zonder bestaande te verwijderen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Voeg alleen nieuwe Koreaanse afbeeldingsvertalingen toe (geen bestaande vertalingen worden verwijderd):    translate -l "ko" -img

  3. Werk alle Koreaanse vertalingen bij (Waarschuwing: Dit verwijdert alle bestaande Koreaanse vertalingen voordat opnieuw wordt vertaald):    translate -l "ko" -u

  4. Werk alleen Koreaanse afbeeldingen bij (Waarschuwing: Dit verwijdert alle bestaande Koreaanse afbeeldingen voordat opnieuw wordt vertaald):    translate -l "ko" -img -u

  5. Voeg nieuwe markdown-vertalingen voor Koreaans toe zonder andere vertalingen te beïnvloeden:    translate -l "ko" -md

  6. Herstel vertalingen met lage betrouwbaarheid op basis van eerdere evaluatieresultaten: translate -l "ko" --fix

  7. Herstel vertalingen met lage betrouwbaarheid voor specifieke bestanden alleen (markdown): translate -l "ko" --fix -md

  8. Herstel vertalingen met lage betrouwbaarheid voor specifieke bestanden alleen (afbeeldingen): translate -l "ko" --fix -img

  9. Gebruik snelle modus voor afbeeldingsvertaling:    translate -l "ko" -img -f

  10. Herstel vertalingen met lage betrouwbaarheid met aangepaste drempel: translate -l "ko" --fix -c 0.8

  11. Debugmodus voorbeeld: - translate -l "ko" -d: Schakel debuglogging in.
  12. Logs opslaan in bestanden: translate -l "ko" -s
  13. Console DEBUG en bestand DEBUG: translate -l "ko" -d -s
  14. Vertaal zonder machinevertalingsdisclaimers aan outputs toe te voegen: translate -l "ko" --no-disclaimer

  15. Migreer notebook-links voor Koreaanse vertalingen (werk links bij naar vertaalde notebooks indien beschikbaar):    migrate-links -l "ko"

  15. Migreer links met dry-run (geen bestandswijzigingen):    migrate-links -l "ko" --dry-run

  16. Werk alleen links bij als vertaalde notebooks bestaan (val niet terug op origineel):    migrate-links -l "ko" --no-fallback-to-original

  17. Verwerk alle talen met bevestigingsprompt:    migrate-links -l "all"

  18. Verwerk alle talen en bevestig automatisch:    migrate-links -l "all" -y
  19. Logs opslaan voor migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliseer README talenadvies met je repo-URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluatie voorbeelden

> [!WARNING]  
> **Bèta Functie**: De evaluatiefunctie bevindt zich momenteel in bèta. Deze functie is uitgebracht om vertaalde documenten te evalueren, en de evaluatiemethoden en gedetailleerde implementatie zijn nog in ontwikkeling en kunnen veranderen.

  1. Evalueer Koreaanse vertalingen: evaluate -l "ko"

  2. Evalueer met aangepaste betrouwbaarheidsdrempel: evaluate -l "ko" -c 0.8

  3. Snelle evaluatie (alleen regelgebaseerd): evaluate -l "ko" -f

  4. Diepe evaluatie (alleen LLM-gebaseerd): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->