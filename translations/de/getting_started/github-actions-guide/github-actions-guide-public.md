# Verwendung der Co-op Translator GitHub Action (Öffentliche Einrichtung)

**Zielgruppe:** Diese Anleitung richtet sich an Nutzer in den meisten öffentlichen oder privaten Repositories, bei denen die Standardberechtigungen von GitHub Actions ausreichen. Sie verwendet das integrierte `GITHUB_TOKEN`.

Automatisieren Sie die Übersetzung der Dokumentation Ihres Repositories mühelos mit der Co-op Translator GitHub Action. Diese Anleitung zeigt Ihnen Schritt für Schritt, wie Sie die Action so einrichten, dass bei Änderungen an Ihren Quell-Markdown-Dateien oder Bildern automatisch Pull Requests mit aktualisierten Übersetzungen erstellt werden.

> [!IMPORTANT]
>
> **Die richtige Anleitung wählen:**
>
> Diese Anleitung beschreibt die **einfachere Einrichtung mit dem Standard-`GITHUB_TOKEN`**. Diese Methode wird für die meisten Nutzer empfohlen, da Sie keine sensiblen GitHub App Private Keys verwalten müssen.
>

## Voraussetzungen

Bevor Sie die GitHub Action konfigurieren, stellen Sie sicher, dass Sie die erforderlichen Zugangsdaten für den KI-Dienst bereithalten.

**1. Erforderlich: Zugangsdaten für das KI-Sprachmodell**
Sie benötigen Zugangsdaten für mindestens ein unterstütztes Sprachmodell:

- **Azure OpenAI**: Erfordert Endpoint, API Key, Modell-/Deployment-Namen, API-Version.
- **OpenAI**: Erfordert API Key, (Optional: Org ID, Base URL, Model ID).
- Details finden Sie unter [Unterstützte Modelle und Dienste](../../../../README.md).

**2. Optional: Zugangsdaten für KI Vision (für Bildübersetzung)**

- Nur erforderlich, wenn Sie Text in Bildern übersetzen möchten.
- **Azure AI Vision**: Erfordert Endpoint und Subscription Key.
- Wenn nicht angegeben, läuft die Action standardmäßig im [Markdown-only mode](../markdown-only-mode.md).

## Einrichtung und Konfiguration

Folgen Sie diesen Schritten, um die Co-op Translator GitHub Action in Ihrem Repository mit dem Standard-`GITHUB_TOKEN` zu konfigurieren.

### Schritt 1: Authentifizierung verstehen (Verwendung von `GITHUB_TOKEN`)

Dieser Workflow verwendet das integrierte `GITHUB_TOKEN`, das von GitHub Actions bereitgestellt wird. Dieses Token gewährt dem Workflow automatisch die Berechtigungen, um mit Ihrem Repository zu interagieren – basierend auf den Einstellungen, die Sie in **Schritt 3** konfigurieren.

### Schritt 2: Repository-Secrets konfigurieren

Sie müssen lediglich Ihre **KI-Dienst-Zugangsdaten** als verschlüsselte Secrets in den Repository-Einstellungen hinterlegen.

1.  Navigieren Sie zu Ihrem Ziel-Repository auf GitHub.
2.  Gehen Sie zu **Settings** > **Secrets and variables** > **Actions**.
3.  Unter **Repository secrets** klicken Sie für jedes benötigte KI-Service-Secret unten auf **New repository secret**.

    ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.de.png) *(Bildreferenz: Zeigt, wo Secrets hinzugefügt werden)*

**Erforderliche KI-Service-Secrets (Fügen Sie ALLE hinzu, die laut Voraussetzungen benötigt werden):**

| Secret Name                         | Beschreibung                               | Wertquelle                     |
| :---------------------------------- | :---------------------------------------- | :----------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Schlüssel für Azure AI Service (Computer Vision)  | Ihr Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint für Azure AI Service (Computer Vision) | Ihr Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Schlüssel für Azure OpenAI Service              | Ihr Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint für Azure OpenAI Service         | Ihr Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | Ihr Azure OpenAI Modellname              | Ihr Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Ihr Azure OpenAI Deployment Name         | Ihr Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | API-Version für Azure OpenAI              | Ihr Azure AI Foundry               |
| `OPENAI_API_KEY`                    | API Key für OpenAI                        | Ihre OpenAI Plattform              |
| `OPENAI_ORG_ID`                     | OpenAI Organisations-ID (Optional)         | Ihre OpenAI Plattform              |
| `OPENAI_CHAT_MODEL_ID`              | Spezifische OpenAI Modell-ID (Optional)       | Ihre OpenAI Plattform              |
| `OPENAI_BASE_URL`                   | Benutzerdefinierte OpenAI API Base URL (Optional)     | Ihre OpenAI Plattform              |

### Schritt 3: Workflow-Berechtigungen konfigurieren

Die GitHub Action benötigt Berechtigungen, die über das `GITHUB_TOKEN` gewährt werden, um Code auszuchecken und Pull Requests zu erstellen.

1.  Gehen Sie in Ihrem Repository zu **Settings** > **Actions** > **General**.
2.  Scrollen Sie nach unten zum Abschnitt **Workflow permissions**.
3.  Wählen Sie **Read and write permissions**. Dadurch erhält das `GITHUB_TOKEN` die erforderlichen Berechtigungen `contents: write` und `pull-requests: write` für diesen Workflow.
4.  Stellen Sie sicher, dass das Kontrollkästchen **Allow GitHub Actions to create and approve pull requests** **aktiviert** ist.
5.  Klicken Sie auf **Save**.

![Permission setting](../../../../translated_images/permission-setting.ae2f02748b0579e7dc3633f14dad67005b533ea8f69890818857de058089a7f5.de.png)

### Schritt 4: Workflow-Datei erstellen

Erstellen Sie abschließend die YAML-Datei, die den automatisierten Workflow mit `GITHUB_TOKEN` definiert.

1.  Legen Sie im Wurzelverzeichnis Ihres Repositories das Verzeichnis `.github/workflows/` an, falls es noch nicht existiert.
2.  Erstellen Sie darin eine Datei mit dem Namen `co-op-translator.yml`.
3.  Fügen Sie den folgenden Inhalt in `co-op-translator.yml` ein.

```yaml
name: Co-op Translator

on:
  push:
    branches:
      - main

jobs:
  co-op-translator:
    runs-on: ubuntu-latest

    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Co-op Translator
        run: |
          python -m pip install --upgrade pip
          pip install co-op-translator

      - name: Run Co-op Translator
        env:
          PYTHONIOENCODING: utf-8
          # === AI Service Credentials ===
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          OPENAI_ORG_ID: ${{ secrets.OPENAI_ORG_ID }}
          OPENAI_CHAT_MODEL_ID: ${{ secrets.OPENAI_CHAT_MODEL_ID }}
          OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
        run: |
          # =====================================================================
          # IMPORTANT: Set your target languages here (REQUIRED CONFIGURATION)
          # =====================================================================
          # Example: Translate to Spanish, French, German. Add -y to auto-confirm.
          translate -l "es fr de" -y  # <--- MODIFY THIS LINE with your desired languages

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "🌐 Update translations via Co-op Translator"
          title: "🌐 Update translations via Co-op Translator"
          body: |
            This PR updates translations for recent changes to the main branch.

            ### 📋 Changes included
            - Translated contents are available in the `translations/` directory
            - Translated images are available in the `translated_images/` directory

            ---
            🌐 Automatically generated by the [Co-op Translator](https://github.com/Azure/co-op-translator) GitHub Action.
          branch: update-translations
          base: main
          labels: translation, automated-pr
          delete-branch: true
          add-paths: |
            translations/
            translated_images/
```
4.  **Workflow anpassen:**
  - **[!IMPORTANT] Zielsprachen:** Im Schritt `Run Co-op Translator` müssen Sie **unbedingt die Liste der Sprachcodes** im Befehl `translate -l "..." -y` überprüfen und an die Anforderungen Ihres Projekts anpassen. Die Beispiel-Liste (`ar de es...`) muss ersetzt oder angepasst werden.
  - **Trigger (`on:`):** Der aktuelle Trigger läuft bei jedem Push auf `main`. Für große Repositories empfiehlt es sich, einen `paths:`-Filter hinzuzufügen (siehe auskommentiertes Beispiel im YAML), damit der Workflow nur bei Änderungen an relevanten Dateien (z. B. Quelldokumentation) ausgeführt wird und Runner-Minuten spart.
  - **PR-Details:** Passen Sie bei Bedarf die Felder `commit-message`, `title`, `body`, `branch` und `labels` im Schritt `Create Pull Request` an.

## Ausführung des Workflows

> [!WARNING]  
> **Zeitlimit für GitHub-gehostete Runner:**  
> GitHub-gehostete Runner wie `ubuntu-latest` haben ein **maximales Ausführungslimit von 6 Stunden**.  
> Bei großen Dokumentations-Repositories wird der Workflow automatisch abgebrochen, wenn der Übersetzungsprozess länger als 6 Stunden dauert.  
> Um dies zu vermeiden, sollten Sie:  
> - Einen **selbstgehosteten Runner** verwenden (kein Zeitlimit)  
> - Die Anzahl der Zielsprachen pro Durchlauf reduzieren

Sobald die Datei `co-op-translator.yml` in Ihren Hauptbranch (oder den im `on:`-Trigger angegebenen Branch) gemergt wurde, läuft der Workflow automatisch, wenn Änderungen in diesen Branch gepusht werden (und ggf. den `paths`-Filter erfüllen).

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.