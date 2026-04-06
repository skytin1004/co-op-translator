# Befehlsreferenz

Die **Co-op Translator** CLI bietet mehrere Optionen zur Anpassung des Übersetzungsprozesses:

Befehl                                       | Beschreibung
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Übersetzt Ihr Projekt in die angegebenen Sprachen. Beispiel: translate -l "es fr de" übersetzt ins Spanische, Französische und Deutsche. Verwenden Sie translate -l "all", um in alle unterstützten Sprachen zu übersetzen.
translate -l "language_codes" -u              | Aktualisiert Übersetzungen, indem bestehende gelöscht und neu erstellt werden. Warnung: Dies löscht alle aktuellen Übersetzungen für die angegebenen Sprachen.
translate -l "language_codes" -img            | Übersetzt nur Bilddateien.
translate -l "language_codes" -md             | Übersetzt nur Markdown-Dateien.
translate -l "language_codes" -nb             | Übersetzt nur Jupyter Notebook-Dateien (.ipynb).
translate -l "language_codes" --fix           | Übersetzt Dateien mit niedrigen Vertrauenswerten basierend auf vorherigen Bewertungsergebnissen neu.
translate -l "language_codes" -d              | Aktiviert den Debug-Modus für detaillierte Protokollierung.
translate -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/ (Konsole bleibt durch -d gesteuert)
translate -l "language_codes" -r "root_dir"   | Gibt das Stammverzeichnis des Projekts an.
translate -l "language_codes" -f              | Verwendet den Schnellmodus für die Bildübersetzung (bis zu 3x schnelleres Plotten bei leichtem Qualitäts- und Ausrichtungsverlust).
translate -l "language_codes" -y              | Bestätigt automatisch alle Eingabeaufforderungen (nützlich für CI/CD-Pipelines).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Aktiviert oder deaktiviert das Hinzufügen eines Maschinellen Übersetzungs-Hinweisabschnitts zu übersetzten Markdown- und Notebook-Dateien (Standard: aktiviert).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personalisieren Sie den README-Sprachen-Hinweisabschnitt (sparse checkout) mit Ihrer Repository-URL.
translate -l "language_codes" --help          | Hilfedetails innerhalb der CLI mit verfügbaren Befehlen.
evaluate -l "language_code"                  | Bewertet die Übersetzungsqualität für eine bestimmte Sprache und gibt Vertrauenswerte aus.
evaluate -l "language_code" -c 0.8           | Bewertet Übersetzungen mit benutzerdefiniertem Vertrauensschwellenwert.
evaluate -l "language_code" -f               | Schneller Bewertungsmodus (nur regelbasiert, ohne LLM).
evaluate -l "language_code" -D               | Tiefer Bewertungsmodus (nur LLM-basiert, gründlicher, aber langsamer).
evaluate -l "language_code" --save-logs, -s  | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/.
migrate-links -l "language_codes"             | Verarbeitet übersetzte Markdown-Dateien neu, um Links zu Notebooks (.ipynb) zu aktualisieren. Bevorzugt übersetzte Notebooks, falls verfügbar; andernfalls kann auf Original-Notebooks zurückgegriffen werden.
migrate-links -l "language_codes" -r          | Gibt das Projekt-Stammverzeichnis an (Standard: aktuelles Verzeichnis).
migrate-links -l "language_codes" --dry-run   | Zeigt an, welche Dateien sich ändern würden, ohne Änderungen zu schreiben.
migrate-links -l "language_codes" --no-fallback-to-original | Schreibt Links zu Original-Notebooks nicht um, wenn übersetzte Gegenstücke fehlen (Aktualisierung nur möglich, wenn Übersetzung existiert).
migrate-links -l "language_codes" -d          | Aktiviert den Debug-Modus für detaillierte Protokollierung.
migrate-links -l "language_codes" --save-logs, -s | Speichert DEBUG-Level-Protokolle in Dateien unter <root_dir>/logs/
migrate-links -l "all" -y                      | Verarbeitet alle Sprachen und bestätigt die Warnmeldung automatisch.

## Anwendungsbeispiele

  1. Standardverhalten (fügt neue Übersetzungen hinzu, ohne bestehende zu löschen):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Fügt nur neue koreanische Bildübersetzungen hinzu (bestehende Übersetzungen werden nicht gelöscht):    translate -l "ko" -img

  3. Aktualisiert alle koreanischen Übersetzungen (Warnung: Dies löscht alle bestehenden koreanischen Übersetzungen, bevor neu übersetzt wird):    translate -l "ko" -u

  4. Aktualisiert nur koreanische Bilder (Warnung: Dies löscht alle bestehenden koreanischen Bilder, bevor neu übersetzt wird):    translate -l "ko" -img -u

  5. Fügt neue Markdown-Übersetzungen für Koreanisch hinzu, ohne andere Übersetzungen zu beeinflussen:    translate -l "ko" -md

  6. Korrigiert Übersetzungen mit niedrigem Vertrauensniveau basierend auf vorherigen Bewertungsergebnissen: translate -l "ko" --fix

  7. Korrigiert Übersetzungen mit niedrigem Vertrauensniveau nur für bestimmte Dateien (Markdown): translate -l "ko" --fix -md

  8. Korrigiert Übersetzungen mit niedrigem Vertrauensniveau nur für bestimmte Dateien (Bilder): translate -l "ko" --fix -img

  9. Verwendet Schnellmodus für Bildübersetzung:    translate -l "ko" -img -f

  10. Korrigiert Übersetzungen mit niedrigem Vertrauensniveau mit benutzerdefinierter Schwelle: translate -l "ko" --fix -c 0.8

  11. Debug-Modus Beispiel: - translate -l "ko" -d: Aktiviert die Debug-Protokollierung.  
  12. Speichert Protokolle in Dateien: translate -l "ko" -s  
  13. Konsole DEBUG und Datei DEBUG: translate -l "ko" -d -s  
  14. Übersetzen ohne Hinzufügen von maschinellen Übersetzungs-Hinweisen zur Ausgabe: translate -l "ko" --no-disclaimer

  15. Migriert Notebook-Links für koreanische Übersetzungen (aktualisiert Links zu übersetzten Notebooks, wenn verfügbar):    migrate-links -l "ko"

  15. Migriert Links mit Dry-Run (keine Dateischreibungen):    migrate-links -l "ko" --dry-run

  16. Aktualisiert Links nur, wenn übersetzte Notebooks existieren (kein Zurückfallen auf Originale):    migrate-links -l "ko" --no-fallback-to-original

  17. Verarbeitet alle Sprachen mit Bestätigungsaufforderung:    migrate-links -l "all"

  18. Verarbeitet alle Sprachen und bestätigt automatisch:    migrate-links -l "all" -y  
  19. Speichert Protokolle in Dateien für migrate-links:    migrate-links -l "ko ja" -s

  20. Personalisieren Sie den README-Sprachen-Hinweis mit Ihrer Repo-URL:  
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Evaluierungsbeispiele

> [!WARNING]  
> **Beta-Funktion**: Die Bewertungsfunktionalität befindet sich derzeit in der Beta-Phase. Dieses Feature wurde veröffentlicht, um übersetzte Dokumente zu bewerten, und die Bewertungsmethoden sowie die detaillierte Implementierung befinden sich noch in der Entwicklung und können sich ändern.

  1. Bewertet koreanische Übersetzungen: evaluate -l "ko"

  2. Bewertung mit benutzerdefiniertem Vertrauensschwellenwert: evaluate -l "ko" -c 0.8

  3. Schnelle Bewertung (nur regelbasiert): evaluate -l "ko" -f

  4. Tiefe Bewertung (nur LLM-basiert): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir bestrebt sind, Genauigkeit zu gewährleisten, beachten Sie bitte, dass automatische Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->