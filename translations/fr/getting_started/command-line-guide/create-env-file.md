# Créez le fichier *.env* dans le répertoire racine

Dans ce tutoriel, nous vous guiderons pour configurer vos variables d'environnement pour les services Azure à l'aide d'un fichier *.env*. Les variables d'environnement vous permettent de gérer en toute sécurité des identifiants sensibles, tels que les clés API, sans les coder en dur dans votre base de code.

> [!IMPORTANT]
> - Un seul service de modèle de langage (Azure OpenAI ou OpenAI) doit être configuré. Remplissez les variables d'environnement pour le service de votre choix. Si les variables d'environnement pour plusieurs modèles de langage sont configurées, le traducteur coopératif en sélectionnera un en fonction de la priorité.
> - Si les variables d'environnement de Computer Vision ne sont pas définies, le traducteur passera automatiquement en [mode Markdown uniquement](./markdown-only-mode.md).

> [!NOTE]
> Ce guide se concentre principalement sur les services Azure, mais vous pouvez choisir n'importe quel modèle de langage pris en charge dans la [liste des modèles et services supportés](../README.md#-supported-models-and-services).

## Créez le fichier *.env*

Dans le répertoire racine de votre projet, créez un fichier nommé *.env*. Ce fichier contiendra toutes vos variables d'environnement dans un format simple.

> [!WARNING]
> Ne validez pas votre fichier *.env* dans les systèmes de contrôle de version tels que Git. Ajoutez *.env* à votre fichier .gitignore pour éviter des validations accidentelles.

1. Accédez au répertoire racine de votre projet.

1. Créez un fichier *.env* dans le répertoire racine de votre projet.

1. Ouvrez le fichier *.env* et collez le modèle suivant :

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
> Si vous voulez retrouver vos clés API et points de terminaison, vous pouvez consulter [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avis de non-responsabilité** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous fassions tout notre possible pour garantir l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations cruciales, il est recommandé de faire appel à une traduction professionnelle réalisée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->