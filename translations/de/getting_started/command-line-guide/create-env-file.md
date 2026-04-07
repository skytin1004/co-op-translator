# Erstellen Sie die *.env*-Datei im Stammverzeichnis

In diesem Tutorial führen wir Sie durch das Einrichten Ihrer Umgebungsvariablen für Azure-Dienste mit einer *.env*-Datei. Umgebungsvariablen ermöglichen es Ihnen, sensible Anmeldeinformationen, wie API-Schlüssel, sicher zu verwalten, ohne sie direkt in Ihren Code einzubetten.

> [!IMPORTANT]
> - Es muss nur ein Sprachmodell-Dienst (Azure OpenAI oder OpenAI) konfiguriert werden. Füllen Sie die Umgebungsvariablen für Ihren bevorzugten Dienst aus. Wenn Umgebungsvariablen für mehrere Sprachmodelle gesetzt sind, wählt der Co-op Translator eines basierend auf der Priorität aus.
> - Wenn die Umgebungsvariablen für Computer Vision nicht gesetzt sind, wechselt der Translator automatisch in den [Markdown-only-Modus](./markdown-only-mode.md).

> [!NOTE]
> Dieser Leitfaden konzentriert sich hauptsächlich auf Azure-Dienste, aber Sie können jedes unterstützte Sprachmodell aus der [Liste der unterstützten Modelle und Dienste](../README.md#-supported-models-and-services) wählen.

## Erstellen Sie die *.env*-Datei

Erstellen Sie im Stammverzeichnis Ihres Projekts eine Datei mit dem Namen *.env*. Diese Datei speichert alle Ihre Umgebungsvariablen in einem einfachen Format.

> [!WARNING]
> Committen Sie Ihre *.env*-Datei nicht in Versionskontrollsysteme wie Git. Fügen Sie *.env* zu Ihrer .gitignore-Datei hinzu, um versehentliche Commits zu verhindern.

1. Navigieren Sie zum Stammverzeichnis Ihres Projekts.

1. Erstellen Sie eine *.env*-Datei im Stammverzeichnis Ihres Projekts.

1. Öffnen Sie die *.env*-Datei und fügen Sie die folgende Vorlage ein:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> Wenn Sie Ihre API-Schlüssel und Endpunkte finden möchten, können Sie sich auf [set-up-azure-ai.md](../set-up-azure-ai.md) beziehen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache gilt als maßgebliche Quelle. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->