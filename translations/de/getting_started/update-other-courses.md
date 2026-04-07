# Aktualisieren Sie den Abschnitt "Weitere Kurse" (Microsoft Beginners Repositories)

Diese Anleitung erklärt, wie der Abschnitt "Weitere Kurse" mit Co‑op Translator automatisch synchronisiert wird und wie die globale Vorlage für alle Repositories aktualisiert wird.

- Gilt für: Nur Microsoft Beginners-Repositories
- Funktioniert mit: Co‑op Translator CLI und GitHub Actions
- Vorlagenquelle: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Schnellstart: Auto-Sync in Ihrem Repository aktivieren

Fügen Sie die folgenden Markierungen um den Abschnitt "Weitere Kurse" in Ihrem README hinzu. Co‑op Translator ersetzt bei jedem Lauf alles zwischen diesen Markierungen.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Jedes Mal, wenn Co‑op Translator ausgeführt wird – über CLI (z. B. `translate -l "<language codes>"`) oder GitHub Actions – wird der Abschnitt "Weitere Kurse", der von diesen Markierungen umschlossen ist, automatisch aktualisiert.

> [!NOTE]
> Wenn Sie bereits eine vorhandene Liste haben, umschließen Sie diese einfach mit denselben Markierungen. Der nächste Lauf ersetzt sie durch den neuesten standardisierten Inhalt.

---

## So ändern Sie den globalen Inhalt

Wenn Sie den standardisierten Inhalt aktualisieren möchten, der in allen Beginners-Repositories erscheint:

1. Bearbeiten Sie die Vorlage: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Erstellen Sie einen Pull Request mit Ihren Änderungen im Co-op Translator-Repository
3. Nachdem der PR gemerged wurde, wird die Co‑op Translator-Version aktualisiert
4. Beim nächsten Lauf von Co‑op Translator (CLI oder GitHub Action) in einem Ziel-Repository wird der aktualisierte Abschnitt automatisch synchronisiert

Dies stellt eine einzige zuverlässige Quelle für den Inhalt "Weitere Kurse" in allen Beginners-Repositories sicher.

## Repository-Größen

Die Repositories können aufgrund der Anzahl der übersetzten Sprachen groß werden, um Endbenutzern Anleitungen zur Verwendung von clone - sparse zu geben, damit nur die notwendigen Sprachen geklont werden und nicht das gesamte Repository.

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
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir um Genauigkeit bemüht sind, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle anzusehen. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->