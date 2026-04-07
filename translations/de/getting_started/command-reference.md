# Befehlsreferenz

Die **Co-op Translator** CLI bietet mehrere Optionen, um den Übersetzungsprozess anzupassen:

Befehl                                       | Beschreibung
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Übersetzt Ihr Projekt in die angegebenen Sprachen. Beispiel: translate -l "es fr de" übersetzt ins Spanische, Französische und Deutsche. Verwenden Sie translate -l "all", um in alle unterstützten Sprachen zu übersetzen.
translate -l "language_codes" -u              | Aktualisiert Übersetzungen, indem vorhandene gelöscht und neu erstellt werden. Warnung: Dies löscht alle aktuellen Übersetzungen für die angegebenen Sprachen.
translate -l "language_codes" -img            | Übersetzt nur Bilddateien.
translate -l "language_codes" -md             | Übersetzt nur Markdown-Dateien.
translate -l "language_codes" -nb             | Übersetzt nur Jupyter-Notebook-Dateien (.ipynb).
translate -l "language_codes" --fix           | Übersetzt Dateien mit niedrigen Vertrauensscores basierend auf vorherigen Bewertungsergebnissen neu.
translate -l "language_codes" -d              | Aktiviert den Debug-Modus für detaillierte Protokollierung.
translate -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/ (Konsole wird weiterhin durch -d gesteuert)
translate -l "language_codes" -r "root_dir"   | Gibt das Stammverzeichnis des Projekts an
translate -l "language_codes" -f              | Verwendet den Schnellmodus für Bildübersetzung (bis zu 3x schnelleres Rendering bei geringem Qualitäts- und Ausrichtungsverlust).
translate -l "language_codes" -y              | Bestätigt automatisch alle Eingabeaufforderungen (nützlich für CI/CD-Pipelines)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktiviert oder deaktiviert das Hinzufügen eines maschinellen Übersetzungs-Haftungsausschlussabschnitts zu übersetzten Markdown- und Notebookdateien (Standard: aktiviert).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalisieren Sie den README-Sprachabschnitt (Sparse Checkout) mit Ihrer Repository-URL.
translate -l "language_codes" --help          | Hilfedetails innerhalb der CLI mit verfügbaren Befehlen
evaluate -l "language_code"                  | Bewertet die Übersetzungsqualität für eine bestimmte Sprache und gibt Vertrauensscores aus
evaluate -l "language_code" -c 0.8           | Bewertet Übersetzungen mit einem benutzerdefinierten Vertrauensschwellenwert
evaluate -l "language_code" -f               | Schnellbewertungsmodus (nur regelbasiert, kein LLM)
evaluate -l "language_code" -D               | Tiefenbewertungsmodus (nur LLM-basiert, gründlicher aber langsamer)
evaluate -l "language_code" --save-logs, -s  | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/
migrate-links -l "language_codes"             | Verarbeitet übersetzte Markdown-Dateien neu, um Links zu Notebooks (.ipynb) zu aktualisieren. Bevorzugt übersetzte Notebooks, wenn verfügbar; kann andernfalls auf Original-Notebooks zurückgreifen.
migrate-links -l "language_codes" -r          | Gibt das Projektstammverzeichnis an (Standard: aktuelles Verzeichnis).
migrate-links -l "language_codes" --dry-run   | Zeigt an, welche Dateien geändert würden, ohne Änderungen zu schreiben.
migrate-links -l "language_codes" --no-fallback-to-original | Schreibt Links zu Original-Notebooks nicht um, wenn übersetzte Gegenstücke fehlen (aktualisiert nur, wenn Übersetzungen existieren).
migrate-links -l "language_codes" -d          | Aktiviert den Debug-Modus für detaillierte Protokollierung.
migrate-links -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/
migrate-links -l "all" -y                      | Verarbeitet alle Sprachen und bestätigt die Warnhinweise automatisch.

## Anwendungsbeispiele

  1. Standardverhalten (fügt neue Übersetzungen hinzu, ohne vorhandene zu löschen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Fügt nur neue koreanische Bildübersetzungen hinzu (vorhandene Übersetzungen werden nicht gelöscht):    translate -l "ko" -img

  3. Aktualisiert alle koreanischen Übersetzungen (Warnung: Dies löscht alle vorhandenen koreanischen Übersetzungen vor der Neuübersetzung):    translate -l "ko" -u

  4. Aktualisiert nur koreanische Bilder (Warnung: Dies löscht alle vorhandenen koreanischen Bilder vor der Neuübersetzung):    translate -l "ko" -img -u

  5. Fügt neue Markdown-Übersetzungen für Koreanisch hinzu, ohne andere Übersetzungen zu beeinflussen:    translate -l "ko" -md

  6. Korrigiert Übersetzungen mit niedriger Zuverlässigkeit basierend auf vorherigen Bewertungsergebnissen: translate -l "ko" --fix

  7. Korrigiert Übersetzungen mit niedriger Zuverlässigkeit nur für bestimmte Dateien (Markdown): translate -l "ko" --fix -md

  8. Korrigiert Übersetzungen mit niedriger Zuverlässigkeit nur für bestimmte Dateien (Bilder): translate -l "ko" --fix -img

  9. Verwendet den Schnellmodus für Bildübersetzungen:    translate -l "ko" -img -f

  10. Korrigiert Übersetzungen mit niedriger Zuverlässigkeit mit benutzerdefiniertem Schwellenwert: translate -l "ko" --fix -c 0.8

  11. Beispiel Debug-Modus: - translate -l "ko" -d: Aktiviert Debug-Logging.
  12. Speichert Protokolle in Dateien: translate -l "ko" -s
  13. Konsole DEBUG und Datei DEBUG: translate -l "ko" -d -s
  14. Übersetzt ohne maschinelle Übersetzungs-Haftungsausschlüsse zu den Ausgaben hinzuzufügen: translate -l "ko" --no-disclaimer

  15. Migriert Notebook-Links für koreanische Übersetzungen (aktualisiert Links zu übersetzten Notebooks, wenn verfügbar):    migrate-links -l "ko"

  15. Migriert Links mit Trockenlauf (keine Dateischreibungen):    migrate-links -l "ko" --dry-run

  16. Aktualisiert Links nur wenn übersetzte Notebooks existieren (kein Rückgriff auf Originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Verarbeitet alle Sprachen mit Bestätigungsaufforderung:    migrate-links -l "all"

  18. Verarbeitet alle Sprachen und bestätigt automatisch:    migrate-links -l "all" -y
  19. Speichert Protokolle in Dateien für migrate-links:    migrate-links -l "ko ja" -s

  20. Personalisiert README-Sprachhinweis mit Ihrer Repository-URL:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Bewertungsbeispiele

> [!WARNING]  
> **Beta-Funktion**: Die Bewertungsfunktion befindet sich derzeit in der Beta-Phase. Diese Funktion wurde veröffentlicht, um übersetzte Dokumente zu bewerten, und die Bewertungsmethoden sowie die detaillierte Implementierung befinden sich noch in der Entwicklung und können sich ändern.

  1. Bewertet koreanische Übersetzungen: evaluate -l "ko"

  2. Bewertet mit benutzerdefiniertem Vertrauensschwellenwert: evaluate -l "ko" -c 0.8

  3. Schnelle Bewertung (nur regelbasiert): evaluate -l "ko" -f

  4. Tiefenbewertung (nur LLM-basiert): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir nach Genauigkeit streben, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->