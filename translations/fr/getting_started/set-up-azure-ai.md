# Configurer Azure AI pour Co-op Translator (Azure OpneAI & Azure AI Vision)

Ce guide vous accompagne dans la configuration d'Azure OpenAI pour la traduction linguistique et d'Azure Computer Vision pour l'analyse du contenu des images (qui peut ensuite être utilisé pour la traduction basée sur les images) au sein d'Azure AI Foundry.

**Prérequis :**
- Un compte Azure avec un abonnement actif.
- Des autorisations suffisantes pour créer des ressources et des déploiements dans votre abonnement Azure.

## Créer un projet Azure AI

Vous commencerez par créer un projet Azure AI, qui sert de point central pour gérer vos ressources IA.

1. Accédez à [https://ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.

1. Sélectionnez **+Create** pour créer un nouveau projet.

1. Effectuez les tâches suivantes :
   - Saisissez un **Nom de projet** (par exemple, `CoopTranslator-Project`).
   - Sélectionnez le **AI hub** (par exemple, `CoopTranslator-Hub`) (Créez-en un nouveau si nécessaire).

1. Cliquez sur "**Review and Create**" pour configurer votre projet. Vous serez redirigé vers la page de présentation de votre projet.

## Configurer Azure OpenAI pour la traduction linguistique

Dans votre projet, vous allez déployer un modèle Azure OpenAI pour servir de backend à la traduction textuelle.

### Accéder à votre projet

Si vous n'y êtes pas déjà, ouvrez votre projet nouvellement créé (par exemple, `CoopTranslator-Project`) dans Azure AI Foundry.

### Déployer un modèle OpenAI

1. Dans le menu de gauche de votre projet, sous "My assets", sélectionnez "**Models + endpoints**".

1. Sélectionnez **+ Deploy model**.

1. Sélectionnez **Deploy Base Model**.

1. Une liste des modèles disponibles vous sera présentée. Filtrez ou recherchez un modèle GPT approprié. Nous recommandons `gpt-4o`.

1. Sélectionnez le modèle souhaité et cliquez sur **Confirm**.

1. Sélectionnez **Deploy**.

### Configuration Azure OpenAI

Une fois déployé, vous pouvez sélectionner le déploiement depuis la page "**Models + endpoints**" pour trouver son **URL de point de terminaison REST**, sa **Clé**, son **Nom de déploiement**, son **Nom de modèle** et sa **Version d'API**. Ces informations seront nécessaires pour intégrer le modèle de traduction dans votre application.

> [!NOTE]
> Vous pouvez sélectionner les versions d'API sur la page de [dépréciation des versions d'API](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) selon vos besoins. Notez que la **version d'API** est différente de la **version du modèle** affichée sur la page **Models + endpoints** dans Azure AI Foundry.

## Configurer Azure Computer Vision pour la traduction d'images

Pour permettre la traduction du texte dans les images, vous devez récupérer la clé API et le point de terminaison du service Azure AI.

1. Accédez à votre projet Azure AI (par exemple, `CoopTranslator-Project`). Assurez-vous d'être sur la page de présentation du projet.

### Configuration du service Azure AI

Trouvez la clé API et le point de terminaison dans le service Azure AI.

1. Accédez à votre projet Azure AI (par exemple, `CoopTranslator-Project`). Assurez-vous d'être sur la page de présentation du projet.

1. Trouvez la **Clé API** et le **Point de terminaison** dans l'onglet du service Azure AI.

    ![Find API Key and Endpoint](../../../translated_images/fr/find-azure-ai-info.0e00140419c12517.webp)

Cette connexion rend les capacités de la ressource Azure AI Services liée (y compris l'analyse d'images) disponibles pour votre projet AI Foundry. Vous pouvez ensuite utiliser cette connexion dans vos notebooks ou applications pour extraire du texte des images, qui pourra ensuite être envoyé au modèle Azure OpenAI pour traduction.

## Consolider vos informations d'identification

Vous devriez maintenant avoir collecté les éléments suivants :

**Pour Azure OpenAI (Traduction Textuelle) :**
- Point de terminaison Azure OpenAI
- Clé API Azure OpenAI
- Nom du modèle Azure OpenAI (par exemple, `gpt-4o`)
- Nom du déploiement Azure OpenAI (par exemple, `cooptranslator-gpt4o`)
- Version d'API Azure OpenAI

**Pour Azure AI Services (Extraction de texte d’image via Vision) :**
- Point de terminaison Azure AI Service
- Clé API Azure AI Service

### Exemple : Configuration de variables d’environnement (Aperçu)

Plus tard, lors de la construction de votre application, vous configurerez probablement celle-ci à l’aide de ces informations collectées. Par exemple, vous pourriez définir des variables d’environnement comme suit :

```bash
# Identifiants du service Azure AI (requis pour la traduction d'images)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # par ex., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Jeux de secours optionnels : dupliquer les variables avec le suffixe _1/_2 (même index pour toutes les variables du jeu)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Identifiants Azure OpenAI (requis pour la traduction de texte)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # par ex., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # par ex., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # par ex., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # par ex., 2024-12-01-preview

# Jeux de secours optionnels : dupliquer l’ensemble complet AZURE_OPENAI_* avec le suffixe _1/_2 (même index pour toutes les variables)
```

---

### Lectures complémentaires

- [Comment créer un projet dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Comment créer des ressources Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Comment déployer des modèles OpenAI dans Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer la précision, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des imprécisions. Le document original dans sa langue native doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle humaine est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d’interprétations erronées résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->