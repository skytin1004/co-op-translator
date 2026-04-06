# Aktualisieren Sie den Abschnitt "Weitere Kurse" (Microsoft Beginners Repos)

Diese Anleitung erklärt, wie der Abschnitt "Weitere Kurse" mithilfe von Co‑op Translator automatisch synchronisiert wird und wie die globale Vorlage für alle Repos aktualisiert wird.

- Gilt für: Nur Microsoft Beginners Repositories
- Funktioniert mit: Co‑op Translator CLI und GitHub Actions
- Vorlagenquelle: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Schnellstart: Auto‑Sync in Ihrem Repo aktivieren

Fügen Sie die folgenden Marker um den Abschnitt "Weitere Kurse" in Ihrem README hinzu. Co‑op Translator ersetzt bei jedem Lauf alles zwischen diesen Markern.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Jedes Mal, wenn Co‑op Translator ausgeführt wird – über CLI (z. B. `translate -l "<language codes>"`) oder GitHub Actions – aktualisiert es automatisch den Abschnitt "Weitere Kurse", der von diesen Markern umschlossen ist.

> [!NOTE]
> Wenn Sie bereits eine Liste haben, umschließen Sie sie einfach mit denselben Markern. Der nächste Lauf ersetzt sie durch den neuesten standardisierten Inhalt.

---

## So ändern Sie den globalen Inhalt

Wenn Sie den standardisierten Inhalt aktualisieren möchten, der in allen Beginners Repos angezeigt wird:

1. Bearbeiten Sie die Vorlage: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. Öffnen Sie eine Pull Anfrage im Co-op Translator Repo mit Ihren Änderungen  
3. Nach dem Zusammenführen der PR wird die Co‑op Translator-Version aktualisiert  
4. Beim nächsten Ausführen von Co‑op Translator (CLI oder GitHub Action) in einem Ziel-Repo wird der aktualisierte Abschnitt automatisch synchronisiert  

Dies stellt eine einzige Wahrheitsquelle für den Inhalt "Weitere Kurse" in allen Beginners Repositories sicher.


## Repo-Größen

Die Repos können aufgrund der Anzahl der übersetzten Sprachen groß werden, um Endbenutzern Anleitungen zu geben, wie man clone - sparse verwendet, um nur notwendige Sprachen zu klonen und nicht das gesamte Repo

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->