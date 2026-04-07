# Configurar Azure AI para Co-op Translator (Azure OpneAI y Azure AI Vision)

Esta guía te lleva paso a paso para configurar Azure OpenAI para traducción de idiomas y Azure Computer Vision para el análisis de contenido de imágenes (que luego puede usarse para traducción basada en imágenes) dentro de Azure AI Foundry.

**Requisitos previos:**
- Una cuenta de Azure con una suscripción activa.
- Permisos suficientes para crear recursos y despliegues en tu suscripción de Azure.

## Crear un Proyecto Azure AI

Comenzarás creando un Proyecto Azure AI, que actúa como un lugar central para administrar tus recursos de IA.

1. Navega a [https://ai.azure.com](https://ai.azure.com) e inicia sesión con tu cuenta de Azure.

1. Selecciona **+Crear** para crear un nuevo proyecto.

1. Realiza las siguientes tareas:
   - Ingresa un **Nombre del proyecto** (por ejemplo, `CoopTranslator-Project`).
   - Selecciona el **Hub de IA** (por ejemplo, `CoopTranslator-Hub`) (crea uno nuevo si es necesario).

1. Haz clic en "**Revisar y crear**" para configurar tu proyecto. Serás llevado a la página de resumen de tu proyecto.

## Configurar Azure OpenAI para Traducción de Idiomas

Dentro de tu proyecto, desplegarás un modelo Azure OpenAI para que sirva como backend para la traducción de texto.

### Navegar a tu Proyecto

Si no estás ya allí, abre tu proyecto recién creado (por ejemplo, `CoopTranslator-Project`) en Azure AI Foundry.

### Desplegar un Modelo OpenAI

1. En el menú lateral de tu proyecto, bajo "Mis activos", selecciona "**Modelos + endpoints**".

1. Selecciona **+ Desplegar modelo**.

1. Selecciona **Desplegar modelo base**.

1. Se te mostrará una lista de modelos disponibles. Filtra o busca un modelo GPT adecuado. Recomendamos `gpt-4o`.

1. Selecciona el modelo deseado y haz clic en **Confirmar**.

1. Selecciona **Desplegar**.

### Configuración Azure OpenAI

Una vez desplegado, puedes seleccionar el despliegue desde la página de "**Modelos + endpoints**" para encontrar su **URL de endpoint REST**, **Clave**, **Nombre del despliegue**, **Nombre del modelo** y **Versión de la API**. Estos serán necesarios para integrar el modelo de traducción en tu aplicación.

> [!NOTE]
> Puedes seleccionar versiones de API desde la página de [desuso de versiones de API](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) según tus requisitos. Ten en cuenta que la **versión de la API** es diferente de la **versión del modelo** mostrada en la página de **Modelos + endpoints** en Azure AI Foundry.

## Configurar Azure Computer Vision para Traducción de Imágenes

Para habilitar la traducción de texto dentro de imágenes, necesitas encontrar la Clave API y el Endpoint del Servicio Azure AI.

1. Navega a tu Proyecto Azure AI (por ejemplo, `CoopTranslator-Project`). Asegúrate de estar en la página de resumen del proyecto.

### Configuración del Servicio Azure AI

Encuentra la Clave API y el Endpoint desde el Servicio Azure AI.

1. Navega a tu Proyecto Azure AI (por ejemplo, `CoopTranslator-Project`). Asegúrate de estar en la página de resumen del proyecto.

1. Encuentra la **Clave API** y el **Endpoint** desde la pestaña Servicio Azure AI.

    ![Encontrar Clave API y Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Esta conexión hace que las capacidades del recurso vinculado de Servicios Azure AI (incluido el análisis de imágenes) estén disponibles para tu proyecto AI Foundry. Luego puedes usar esta conexión en tus notebooks o aplicaciones para extraer texto de imágenes, el cual puede ser enviado posteriormente al modelo Azure OpenAI para traducción.

## Consolidando tus Credenciales

Para este momento, deberías haber recopilado lo siguiente:

**Para Azure OpenAI (Traducción de Texto):**
- Endpoint de Azure OpenAI
- Clave API de Azure OpenAI
- Nombre del modelo Azure OpenAI (por ejemplo, `gpt-4o`)
- Nombre del despliegue Azure OpenAI (por ejemplo, `cooptranslator-gpt4o`)
- Versión de la API Azure OpenAI

**Para Servicios Azure AI (Extracción de texto en imágenes vía Vision):**
- Endpoint del Servicio Azure AI
- Clave API del Servicio Azure AI

### Ejemplo: Configuración de Variables de Entorno (Vista previa)

Más adelante, cuando construyas tu aplicación, probablemente la configures usando estas credenciales recopiladas. Por ejemplo, puedes establecerlas como variables de entorno así:

```bash
# Credenciales del Servicio Azure AI (Requeridas para la traducción de imágenes)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # p.ej., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Conjuntos opcionales de respaldo: duplicar variables con sufijo _1/_2 (mismo índice para todas las variables en el conjunto)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Credenciales de Azure OpenAI (Requeridas para la traducción de texto)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # p.ej., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # p.ej., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # p.ej., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # p.ej., 2024-12-01-preview

# Conjuntos opcionales de respaldo: duplicar el conjunto completo AZURE_OPENAI_* con sufijo _1/_2 (mismo índice para todas las variables)
```

---

### Lecturas adicionales

- [Cómo crear un proyecto en Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Cómo crear recursos de Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Cómo desplegar modelos OpenAI en Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción AI [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos responsabilizamos por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->