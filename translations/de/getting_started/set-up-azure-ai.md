# Azure AI für Co-op Translator einrichten (Azure OpneAI & Azure AI Vision)

Diese Anleitung führt Sie durch die Einrichtung von Azure OpenAI für die Sprachübersetzung und Azure Computer Vision für die Analyse von Bildinhalten (die dann für bildbasierte Übersetzungen verwendet werden können) innerhalb von Azure AI Foundry.

**Voraussetzungen:**
- Ein Azure-Konto mit einem aktiven Abonnement.
- Ausreichende Berechtigungen zum Erstellen von Ressourcen und Bereitstellungen in Ihrem Azure-Abonnement.

## Erstellen Sie ein Azure AI-Projekt

Sie beginnen mit der Erstellung eines Azure AI-Projekts, das als zentraler Ort für die Verwaltung Ihrer KI-Ressourcen dient.

1. Navigieren Sie zu [https://ai.azure.com](https://ai.azure.com) und melden Sie sich mit Ihrem Azure-Konto an.

1. Wählen Sie **+Create**, um ein neues Projekt zu erstellen.

1. Führen Sie folgende Aufgaben aus:
   - Geben Sie einen **Projektnamen** ein (z. B. `CoopTranslator-Project`).
   - Wählen Sie den **AI Hub** aus (z. B. `CoopTranslator-Hub`) (Erstellen Sie bei Bedarf einen neuen).

1. Klicken Sie auf "**Review and Create**", um Ihr Projekt einzurichten. Sie werden zur Übersichtsseite Ihres Projekts weitergeleitet.

## Azure OpenAI für Sprachübersetzung einrichten

Innerhalb Ihres Projekts werden Sie ein Azure OpenAI-Modell bereitstellen, das als Backend für die Textübersetzung dient.

### Navigieren Sie zu Ihrem Projekt

Falls noch nicht geöffnet, öffnen Sie Ihr neu erstelltes Projekt (z. B. `CoopTranslator-Project`) in Azure AI Foundry.

### Bereitstellen eines OpenAI-Modells

1. Wählen Sie im linken Menü Ihres Projekts unter "My assets" "**Models + endpoints**".

1. Wählen Sie **+ Deploy model**.

1. Wählen Sie **Deploy Base Model**.

1. Ihnen wird eine Liste verfügbarer Modelle angezeigt. Filtern oder suchen Sie nach einem geeigneten GPT-Modell. Wir empfehlen `gpt-4o`.

1. Wählen Sie Ihr gewünschtes Modell aus und klicken Sie auf **Confirm**.

1. Wählen Sie **Deploy**.

### Azure OpenAI-Konfiguration

Nach der Bereitstellung können Sie die Bereitstellung auf der Seite "**Models + endpoints**" auswählen, um die **REST-Endpunkt-URL**, den **Schlüssel**, den **Bereitstellungsnamen**, den **Modellnamen** und die **API-Version** einzusehen. Diese werden benötigt, um das Übersetzungsmodell in Ihre Anwendung zu integrieren.

> [!NOTE]
> Sie können API-Versionen basierend auf Ihren Anforderungen auf der Seite [API Version Deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) auswählen. Beachten Sie, dass die **API-Version** sich von der **Modellversion** unterscheidet, die auf der Seite **Models + endpoints** in Azure AI Foundry angezeigt wird.

## Azure Computer Vision für Bildübersetzung einrichten

Um die Übersetzung von Text in Bildern zu ermöglichen, müssen Sie den Azure AI Service API-Schlüssel und Endpunkt finden.

1. Navigieren Sie zu Ihrem Azure AI-Projekt (z. B. `CoopTranslator-Project`). Stellen Sie sicher, dass Sie sich auf der Übersichtsseite des Projekts befinden.

### Azure AI Service-Konfiguration

Finden Sie den API-Schlüssel und Endpunkt des Azure AI Service.

1. Navigieren Sie zu Ihrem Azure AI-Projekt (z. B. `CoopTranslator-Project`). Stellen Sie sicher, dass Sie sich auf der Übersichtsseite des Projekts befinden.

1. Finden Sie den **API-Schlüssel** und **Endpunkt** im Tab Azure AI Service.

    ![API-Schlüssel und Endpunkt finden](../../../getting_started/imgs/find-azure-ai-info.png)

Diese Verbindung macht die Funktionen der verknüpften Azure AI Services-Ressource (einschließlich Bildanalyse) in Ihrem AI Foundry-Projekt verfügbar. Sie können diese Verbindung dann in Ihren Notebooks oder Anwendungen verwenden, um Text aus Bildern zu extrahieren, der anschließend an das Azure OpenAI-Modell zur Übersetzung gesendet werden kann.

## Konsolidierung Ihrer Zugangsdaten

Bis jetzt sollten Sie Folgendes gesammelt haben:

**Für Azure OpenAI (Textübersetzung):**
- Azure OpenAI Endpunkt
- Azure OpenAI API-Schlüssel
- Azure OpenAI Modellname (z. B. `gpt-4o`)
- Azure OpenAI Bereitstellungsname (z. B. `cooptranslator-gpt4o`)
- Azure OpenAI API-Version

**Für Azure AI Services (Textextraktion aus Bildern via Vision):**
- Azure AI Service Endpunkt
- Azure AI Service API-Schlüssel

### Beispiel: Umgebungsvariablen-Konfiguration (Vorschau)

Später, beim Erstellen Ihrer Anwendung, konfigurieren Sie diese wahrscheinlich mit den gesammelten Zugangsdaten. Zum Beispiel könnten Sie sie als Umgebungsvariablen wie folgt setzen:

```bash
# Azure KI-Dienstanmeldeinformationen (Erforderlich für die Bildübersetzung)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # z.B., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Optionale Ersatzsätze: duplizieren Sie Variablen mit dem Suffix _1/_2 (gleicher Index für alle Variablen im Satz)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI-Anmeldeinformationen (Erforderlich für die Textübersetzung)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # z.B., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # z.B., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # z.B., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # z.B., 2024-12-01-preview

# Optionale Ersatzsätze: duplizieren Sie den vollständigen AZURE_OPENAI_* Satz mit dem Suffix _1/_2 (gleicher Index für alle Variablen)
```

---

### Weiterführende Literatur

- [Wie man ein Projekt in Azure AI Foundry erstellt](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Wie man Azure AI-Ressourcen erstellt](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Wie man OpenAI-Modelle in Azure AI Foundry bereitstellt](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache ist als maßgebliche Quelle zu betrachten. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->