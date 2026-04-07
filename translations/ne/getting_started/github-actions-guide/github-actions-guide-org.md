# Co-op Translator GitHub Action प्रयोग गर्ने तरिका (संस्थागत मार्गदर्शन)

**लक्ष्य समूह:** यो मार्गदर्शन **Microsoft आन्तरिक प्रयोगकर्ता** वा **त्यस्ता टिमहरू**का लागि हो जससँग तयार Co-op Translator GitHub App को आवश्यक प्रमाणपत्रहरू छन् वा आफैंले आफ्नो कस्टम GitHub App बनाउन सक्छन्।

आफ्नो रिपोजिटरीको डक्युमेन्टेसन अनुवाद स्वचालित रूपमा गर्न Co-op Translator GitHub Action प्रयोग गर्नुहोस्। यो मार्गदर्शनले तपाईंलाई कसरी सेटअप गर्ने भन्ने देखाउँछ ताकि जब तपाईंको स्रोत Markdown फाइलहरू वा तस्बिरहरू परिवर्तन हुन्छन्, अनुवाद अपडेट भएको Pull Request स्वचालित रूपमा बनोस्।

**महत्त्वपूर्ण**
**सही मार्गदर्शन छान्नुहोस्:**

यो मार्गदर्शनमा **GitHub App ID र Private Key** प्रयोग गरेर सेटअप गर्ने तरिका छ। तपाईंलाई यो "संस्थागत मार्गदर्शन" चाहिन्छ यदि: **`GITHUB_TOKEN` अनुमति सीमित छ:** तपाईंको संस्था वा रिपोजिटरी सेटिङले `GITHUB_TOKEN` लाई दिइने डिफल्ट अनुमति सीमित गर्छ। विशेष गरी, यदि `GITHUB_TOKEN` लाई आवश्यक `write` अनुमति (जस्तै `contents: write` वा `pull-requests: write`) छैन भने, [सार्वजनिक सेटअप मार्गदर्शन](./github-actions-guide-public.md) मा दिइएको workflow अनुमति अभावका कारण असफल हुन्छ। स्पष्ट अनुमति दिइएको GitHub App प्रयोग गर्दा यो समस्या आउँदैन।

**यदि माथिको कुरा तपाईंमा लागू हुँदैन भने:**

यदि तपाईंको रिपोजिटरीमा डिफल्ट `GITHUB_TOKEN` ले पर्याप्त अनुमति पाउँछ (अर्थात् संस्थागत सीमाले रोकिएको छैन), कृपया **[GITHUB_TOKEN प्रयोग गरेर सार्वजनिक सेटअप मार्गदर्शन](./github-actions-guide-public.md)** प्रयोग गर्नुहोस्। सार्वजनिक मार्गदर्शनमा App ID वा Private Key लिनु पर्दैन, केवल डिफल्ट `GITHUB_TOKEN` र रिपोजिटरी अनुमति प्रयोग हुन्छ।

## पूर्वशर्तहरू

GitHub Action कन्फिगर गर्नु अघि, आवश्यक AI सेवा प्रमाणपत्रहरू तयार गर्नुहोस्।

**१. आवश्यक: AI Language Model प्रमाणपत्रहरू**
कम्तीमा एउटा समर्थित Language Model को प्रमाणपत्र चाहिन्छ:

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Name, API Version चाहिन्छ।
- **OpenAI**: API Key चाहिन्छ, (Optional: Org ID, Base URL, Model ID)।
- थप जानकारीका लागि [समर्थित मोडेल र सेवाहरू](../../../../README.md) हेर्नुहोस्।
- सेटअप मार्गदर्शन: [Azure OpenAI सेटअप गर्नुहोस्](../set-up-resources/set-up-azure-openai.md)।

**२. वैकल्पिक: Computer Vision प्रमाणपत्रहरू (तस्बिर अनुवादका लागि)**

- तस्बिरभित्रको पाठ अनुवाद गर्न चाहनुहुन्छ भने मात्र आवश्यक।
- **Azure Computer Vision**: Endpoint र Subscription Key चाहिन्छ।
- यदि नदिएको खण्डमा, action [Markdown-only mode](../markdown-only-mode.md) मा चल्छ।
- सेटअप मार्गदर्शन: [Azure Computer Vision सेटअप गर्नुहोस्](../set-up-resources/set-up-azure-computer-vision.md)।

## सेटअप र कन्फिगरेसन

तलका चरणहरू पालना गरेर Co-op Translator GitHub Action आफ्नो रिपोजिटरीमा कन्फिगर गर्नुहोस्:

### चरण १: GitHub App Authentication स्थापना र कन्फिगर गर्नुहोस्

Workflow ले GitHub App authentication प्रयोग गरेर तपाईंको रिपोजिटरीमा सुरक्षित रूपमा काम गर्छ (जस्तै Pull Request बनाउने)। दुई विकल्प:

#### **विकल्प A: तयार Co-op Translator GitHub App स्थापना गर्नुहोस् (Microsoft आन्तरिक प्रयोगकर्ताका लागि)**

१. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) पेजमा जानुहोस्।

१. **Install** छान्नुहोस् र आफ्नो अकाउन्ट वा संस्था छान्नुहोस् जहाँ तपाईंको लक्षित रिपोजिटरी छ।

    <img src="../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ne.png" alt="Install app">

१. **Only select repositories** छान्नुहोस् र आफ्नो लक्षित रिपोजिटरी (जस्तै `PhiCookBook`) छान्नुहोस्। **Install** क्लिक गर्नुहोस्। तपाईंलाई प्रमाणिकरण गर्न भनिन सक्छ।

    <img src="../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ne.png" alt="Install authorize">

१. **App प्रमाणपत्र प्राप्त गर्नुहोस् (आन्तरिक प्रक्रिया आवश्यक):** Workflow लाई app को रूपमा प्रमाणिकरण गर्न, तपाईंलाई Co-op Translator टिमले दुई कुरा दिनुपर्छ:
  - **App ID:** Co-op Translator app को अद्वितीय पहिचानकर्ता। App ID हो: `1164076`।
  - **Private Key:** तपाईंले सम्पूर्ण `.pem` private key फाइलको सामग्री सम्पर्क व्यक्ति (maintainer) बाट लिनुपर्छ। **यो key लाई पासवर्ड जस्तै सुरक्षित राख्नुहोस्।**

१. चरण २ मा जानुहोस्।

#### **विकल्प B: आफ्नो कस्टम GitHub App प्रयोग गर्नुहोस्**

- चाहनुहुन्छ भने, तपाईंले आफ्नै GitHub App बनाउन र कन्फिगर गर्न सक्नुहुन्छ। यसमा Contents र Pull requests मा Read & write पहुँच हुनुपर्छ। तपाईंलाई यसको App ID र Private Key चाहिन्छ।

### चरण २: रिपोजिटरी Secrets कन्फिगर गर्नुहोस्

GitHub App प्रमाणपत्र र AI सेवा प्रमाणपत्रहरूलाई आफ्नो रिपोजिटरी सेटिङमा गोप्य secrets को रूपमा थप्नुहोस्।

१. आफ्नो लक्षित GitHub रिपोजिटरीमा जानुहोस् (जस्तै `PhiCookBook`)।

१. **Settings** > **Secrets and variables** > **Actions** मा जानुहोस्।

१. **Repository secrets** अन्तर्गत, तलका प्रत्येक secret का लागि **New repository secret** क्लिक गर्नुहोस्।

   <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ne.png" alt="Select setting action">

**GitHub App Authentication का लागि आवश्यक Secrets:**

| Secret Name          | विवरण                                      | स्रोत                                     |
| :------------------- | :------------------------------------------ | :---------------------------------------- |
| `GH_APP_ID`          | GitHub App को App ID (चरण १ बाट)            | GitHub App Settings                      |
| `GH_APP_PRIVATE_KEY` | डाउनलोड गरिएको `.pem` फाइलको सम्पूर्ण सामग्री | `.pem` फाइल (चरण १ बाट)                 |

**AI सेवा Secrets (पूर्वशर्त अनुसार सबै थप्नुहोस्):**

| Secret Name                         | विवरण                               | स्रोत                     |
| :---------------------------------- | :---------------------------------- | :------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) को Key  | Azure AI Foundry          |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) को Endpoint | Azure AI Foundry          |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI सेवा को Key              | Azure AI Foundry          |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI सेवा को Endpoint         | Azure AI Foundry          |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI Model Name              | Azure AI Foundry          |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI Deployment Name         | Azure AI Foundry          |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI को API Version          | Azure AI Foundry          |
| `OPENAI_API_KEY`                    | OpenAI को API Key                    | OpenAI Platform           |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID               | OpenAI Platform           |
| `OPENAI_CHAT_MODEL_ID`              | OpenAI को Specific model ID           | OpenAI Platform           |
| `OPENAI_BASE_URL`                   | OpenAI को Custom API Base URL         | OpenAI Platform           |

<img src="../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ne.png" alt="Enter environment variable name">

### चरण ३: Workflow फाइल बनाउनुहोस्

अन्तमा, स्वचालित workflow परिभाषित गर्ने YAML फाइल बनाउनुहोस्।

१. आफ्नो रिपोजिटरीको root directory मा `.github/workflows/` फोल्डर छैन भने बनाउनुहोस्।

१. `.github/workflows/` भित्र `co-op-translator.yml` नामको फाइल बनाउनुहोस्।

१. तलको सामग्री co-op-translator.yml मा टाँस्नुहोस्।

```
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
          # Azure AI Service Credentials
          AZURE_AI_SERVICE_API_KEY: ${{ secrets.AZURE_AI_SERVICE_API_KEY }}
          AZURE_AI_SERVICE_ENDPOINT: ${{ secrets.AZURE_AI_SERVICE_ENDPOINT }}

          # Azure OpenAI Credentials
          AZURE_OPENAI_API_KEY: ${{ secrets.AZURE_OPENAI_API_KEY }}
          AZURE_OPENAI_ENDPOINT: ${{ secrets.AZURE_OPENAI_ENDPOINT }}
          AZURE_OPENAI_MODEL_NAME: ${{ secrets.AZURE_OPENAI_MODEL_NAME }}
          AZURE_OPENAI_CHAT_DEPLOYMENT_NAME: ${{ secrets.AZURE_OPENAI_CHAT_DEPLOYMENT_NAME }}
          AZURE_OPENAI_API_VERSION: ${{ secrets.AZURE_OPENAI_API_VERSION }}

          # OpenAI Credentials
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

      - name: Authenticate GitHub App
        id: generate_token
        uses: tibdex/github-app-token@v1
        with:
          app_id: ${{ secrets.GH_APP_ID }}
          private_key: ${{ secrets.GH_APP_PRIVATE_KEY }}

      - name: Create Pull Request with translations
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ steps.generate_token.outputs.token }}
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

४.  **Workflow अनुकूलन गर्नुहोस्:**
  - **Target Languages:** `Run Co-op Translator` स्टेपमा, तपाईंले `translate -l "..." -y` कमाण्डमा दिइएको भाषा कोडहरूको सूची **आफ्नो परियोजनाको आवश्यकता अनुसार अनिवार्य रूपमा परिमार्जन गर्नुहोस्**। उदाहरण सूची (`ar de es...`) लाई बदल्नुहोस् वा मिलाउनुहोस्।
  - **Trigger (`on:`):** हालको trigger ले `main` मा हरेक push मा workflow चलाउँछ। ठूलो रिपोजिटरीका लागि, `paths:` filter थप्नुहोस् (YAML मा टिप्पणी गरिएको उदाहरण हेर्नुहोस्) ताकि केवल सम्बन्धित फाइल परिवर्तन हुँदा मात्र workflow चलोस्, runner minutes बचत गर्न।
  - **PR विवरण:** `Create Pull Request` स्टेपमा `commit-message`, `title`, `body`, `branch` नाम, र `labels` अनुकूलन गर्नुहोस् यदि आवश्यक छ भने।

## प्रमाणपत्र व्यवस्थापन र नवीकरण

- **सुरक्षा:** संवेदनशील प्रमाणपत्रहरू (API key, private key) सधैं GitHub Actions secrets मा सुरक्षित राख्नुहोस्। workflow फाइल वा रिपोजिटरी कोडमा कहिल्यै देखाउनुहोस्।
- **Key नवीकरण (Microsoft आन्तरिक प्रयोगकर्ता):** Microsoft भित्र प्रयोग हुने Azure OpenAI key को अनिवार्य नवीकरण नीति हुन सक्छ (जस्तै, हरेक ५ महिनामा)। workflow असफल हुन नदिन, GitHub secrets (`AZURE_OPENAI_...` keys) **समयमै अपडेट गर्नुहोस्**।

## Workflow चलाउने तरिका

**GitHub-hosted Runner Time Limit:**  
GitHub-hosted runner (जस्तै `ubuntu-latest`) को **अधिकतम execution समय ६ घण्टा** छ।  
ठूलो डक्युमेन्टेसन रिपोजिटरीमा, अनुवाद प्रक्रिया ६ घण्टा भन्दा बढी लागेमा workflow स्वचालित रूपमा बन्द हुन्छ।  
यसलाई रोक्न:  
- **self-hosted runner** प्रयोग गर्नुहोस् (समय सीमा छैन)  
- हरेक रनमा अनुवाद हुने भाषाको संख्या घटाउनुहोस्

`co-op-translator.yml` फाइल मुख्य शाखामा (वा `on:` trigger मा निर्दिष्ट शाखामा) merge भएपछि, त्यो शाखामा परिवर्तन push हुँदा (र `paths` filter मिल्यो भने) workflow स्वचालित रूपमा चल्छ।

अनुवादहरू बने वा अपडेट भएमा, action ले स्वचालित रूपमा Pull Request बनाउँछ, जुन तपाईंले review र merge गर्न सक्नुहुन्छ।

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज़ यसको मौलिक भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।