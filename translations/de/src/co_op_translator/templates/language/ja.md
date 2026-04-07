---
title: FAQ - Lokales Dev-Setup
description: Häufig gestellte Fragen für ein lokales Dev-Setup.
---

## Lokale Dev-Setup-FAQ

### Wie debugge ich eine Pull Request auf meinem lokalen Computer?

1. Checke die PR aus:<br />
   `gh pr checkout <PR-NUMMER>`
2. Erstellen Sie Ihren Feature-Branch vom PR: `git switch -c my-feature-branch`
3. Nehmen Sie die Änderungen an Ihrem Feature-Branch vor und committen Sie sie.
4. Pushen Sie Ihre Änderungen und aktualisieren Sie die PR, indem Sie `git push --set-upstream origin my-feature-branch` ausführen. Die PR-Seite wird automatisch aktualisiert.

### Wie bekomme ich eine lokale Entwicklungsumgebung mit meinem Pull Request zum Laufen?

Wenn Sie mit einem PR Pull Request debuggen und teilsandoffene Implementierungen lokal testen wollen, installieren Sie die GitHub App [Localizeflow](https://github.com/Localizeflow/localizeflow) lokal. Localizeflow integriert sich mit Ihrer Branch-Namenskonvention und hilft dabei, Ihre Änderungen lokal zu testen, bevor Sie diese in die Haupt-Branches einpflegen.

### Warum schlägt mein Build lokal fehl, aber auf CI nicht?

Dies passiert manchmal, wenn Ihre lokale Umgebung nicht exakt die gleiche Versionen von Tools wie Node.js, Yarn, etc. verwendet. Stellen Sie daher sicher, dass Sie die im Repo angegebenen Versionen verwenden. Nutzen Sie Tools wie `nvm` oder Docker-Container, die ci-konforme Umgebungen bereitstellen.

### Kann ich alte Pull Requests weiterhin lokal testen, wenn sie gemerged sind?

Ja. Checken Sie einfach den entsprechenden Commit oder Tag aus, auf dem der PR basiert, oder nutzen Sie Tools wie `git reflog`, um die genauen Commits zu finden. Alternativ können Sie einen Branch von dem ursprünglichen Commit erstellen und darauf weiterarbeiten.

### Wie aktualisiere ich meine lokale Branch, um Änderungen aus der Hauptentwicklungslinie zu holen?

Führen Sie `git fetch origin` aus und dann entweder `git rebase origin/main` (oder wie Ihr Hauptbranch auch immer heißt) oder `git merge origin/main` in Ihrem Feature-Branch, um auf dem neuesten Stand zu bleiben.

### Tipp: Verwenden Sie immer aussagekräftige Branch-Namen

Beispiel: `feature/xyz-meine-änderung` oder `bugfix/abc-issue123`. Das macht die Zusammenarbeit leichter.

---

Für weitere Fragen konsultieren Sie das Team oder die Dokumentation.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in der Originalsprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->