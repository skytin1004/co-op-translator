# Configurer Azure AI pour Co-op Translator (Azure OpneAI & Azure AI Vision)

Ce guide vous accompagne dans la configuration d'Azure OpenAI pour la traduction linguistique et d'Azure Computer Vision pour l'analyse de contenu d'image (qui peut ensuite être utilisé pour la traduction basée sur l'image) au sein d'Azure AI Foundry.

**Prérequis :**
- Un compte Azure avec un abonnement actif.
- Des autorisations suffisantes pour créer des ressources et des déploiements dans votre abonnement Azure.

## Créer un projet Azure AI

Vous commencerez par créer un projet Azure AI, qui servira de lieu central pour gérer vos ressources AI.

1. Rendez-vous sur [https://ai.azure.com](https://ai.azure.com) et connectez-vous avec votre compte Azure.

1. Sélectionnez **+Create** pour créer un nouveau projet.

1. Effectuez les tâches suivantes :
   - Saisissez un **Nom du projet** (ex. `CoopTranslator-Project`).
   - Sélectionnez le **Hub AI** (ex. `CoopTranslator-Hub`) (Créez-en un nouveau si nécessaire).

1. Cliquez sur "**Review and Create**" pour configurer votre projet. Vous serez redirigé vers la page de présentation de votre projet.

## Configurer Azure OpenAI pour la traduction linguistique

Dans votre projet, vous déploierez un modèle Azure OpenAI qui servira de moteur pour la traduction de texte.

### Accéder à votre projet

Si ce n’est pas déjà fait, ouvrez votre projet nouvellement créé (par ex. `CoopTranslator-Project`) dans Azure AI Foundry.

### Déployer un modèle OpenAI

1. Dans le menu de gauche de votre projet, sous "My assets", sélectionnez "**Models + endpoints**".

1. Sélectionnez **+ Deploy model**.

1. Sélectionnez **Deploy Base Model**.

1. Une liste de modèles disponibles vous sera présentée. Filtrez ou recherchez un modèle GPT adapté. Nous recommandons `gpt-4o`.

1. Sélectionnez votre modèle désiré et cliquez sur **Confirm**.

1. Sélectionnez **Deploy**.

### Configuration Azure OpenAI

Une fois déployé, vous pouvez sélectionner le déploiement depuis la page "**Models + endpoints**" pour trouver son **URL de point de terminaison REST**, **Clé**, **Nom de déploiement**, **Nom du modèle** et **Version de l'API**. Ceux-ci seront nécessaires pour intégrer le modèle de traduction dans votre application.

> [!NOTE]
> Vous pouvez sélectionner les versions de l'API depuis la page [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) selon vos besoins. Sachez que la **version de l'API** est différente de la **version du modèle** affichée sur la page **Models + endpoints** dans Azure AI Foundry.

## Configurer Azure Computer Vision pour la traduction d'images

Pour permettre la traduction de texte dans les images, vous devez récupérer la clé API et le point de terminaison du service Azure AI.

1. Accédez à votre projet Azure AI (par ex. `CoopTranslator-Project`). Assurez-vous d’être sur la page de présentation du projet.

### Configuration du service Azure AI

Récupérez la clé API et le point de terminaison depuis le service Azure AI.

1. Accédez à votre projet Azure AI (par ex. `CoopTranslator-Project`). Assurez-vous d’être sur la page de présentation du projet.

1. Trouvez la **Clé API** et le **Point de terminaison** dans l’onglet Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Cette connexion rend les capacités de la ressource Azure AI Services liée (y compris l’analyse d’image) disponibles pour votre projet AI Foundry. Vous pourrez alors utiliser cette connexion dans vos notebooks ou applications pour extraire du texte des images, qui pourra ensuite être envoyé au modèle Azure OpenAI pour traduction.

## Consolider vos informations d’identification

Vous devriez maintenant avoir collecté les éléments suivants :

**Pour Azure OpenAI (Traduction de texte) :**
- Point de terminaison Azure OpenAI
- Clé API Azure OpenAI
- Nom du modèle Azure OpenAI (ex. `gpt-4o`)
- Nom du déploiement Azure OpenAI (ex. `cooptranslator-gpt4o`)
- Version de l'API Azure OpenAI

**Pour les services Azure AI (Extraction de texte d’image via Vision) :**
- Point de terminaison du service Azure AI
- Clé API du service Azure AI

### Exemple : Configuration de variables d'environnement (aperçu)

Plus tard, lors de la création de votre application, vous configurerez probablement ces informations d’identification collectées. Par exemple, vous pourriez les définir en variables d’environnement comme suit :

```bash
# Identifiants du service Azure AI (requis pour la traduction d'images)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # par ex., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Jeux de secours optionnels : variables dupliquées avec suffixe _1/_2 (même indice pour toutes les variables du jeu)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Identifiants Azure OpenAI (requis pour la traduction de texte)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # par ex., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # par ex., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # par ex., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # par ex., 2024-12-01-preview

# Jeux de secours optionnels : dupliquer l'ensemble complet AZURE_OPENAI_* avec suffixe _1/_2 (même indice pour toutes les variables)
```

---

### Lectures complémentaires

- [Comment créer un projet dans Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Comment créer des ressources Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Comment déployer des modèles OpenAI dans Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer la précision, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction professionnelle humaine est recommandée. Nous ne pouvons être tenus responsables des malentendus ou des erreurs d’interprétation résultant de l’utilisation de cette traduction.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->