# Co-op Translator GitHub Action का उपयोग करना (संगठन गाइड)

**लक्ष्य दर्शक:** यह गाइड **Microsoft के आंतरिक उपयोगकर्ताओं** या उन टीमों के लिए है जिनके पास पहले से बने Co-op Translator GitHub App के लिए आवश्यक क्रेडेंशियल्स हैं या जो अपना खुद का कस्टम GitHub App बना सकते हैं।

अपने रिपॉजिटरी की डाक्यूमेंटेशन का अनुवाद ऑटोमेट करने के लिए Co-op Translator GitHub Action का उपयोग करें। यह गाइड आपको एक्शन सेटअप करने की प्रक्रिया समझाता है ताकि जब भी आपके सोर्स Markdown फाइल या इमेज बदलें, तब अपने आप अपडेटेड अनुवाद के साथ पुल रिक्वेस्ट बन जाए।

> [!IMPORTANT]
> 
> **सही गाइड चुनना:**
>
> यह गाइड **GitHub App ID और Private Key** का उपयोग करके सेटअप की प्रक्रिया बताता है। आपको आमतौर पर यह "संगठन गाइड" तब चाहिए जब: **`GITHUB_TOKEN` की परमिशन सीमित है:** आपके संगठन या रिपॉजिटरी की सेटिंग्स डिफॉल्ट `GITHUB_TOKEN` को दी गई परमिशन को सीमित करती हैं। खासकर, अगर `GITHUB_TOKEN` को जरूरी `write` परमिशन (जैसे `contents: write` या `pull-requests: write`) नहीं दी गई है, तो [Public Setup Guide](./github-actions-guide-public.md) में दिया वर्कफ्लो परमिशन की कमी के कारण फेल हो जाएगा। एक डेडिकेटेड GitHub App, जिसे स्पष्ट रूप से परमिशन दी गई है, इस लिमिटेशन को दूर करता है।
>
> **अगर ऊपर दिया गया आपके लिए लागू नहीं है:**
>
> अगर आपके रिपॉजिटरी में स्टैंडर्ड `GITHUB_TOKEN` के पास पर्याप्त परमिशन है (यानी आपको संगठन की सीमाओं से कोई रुकावट नहीं है), तो कृपया **[Public Setup Guide using GITHUB_TOKEN](./github-actions-guide-public.md)** का उपयोग करें। पब्लिक गाइड में App ID या Private Key लेने या संभालने की जरूरत नहीं होती, सिर्फ स्टैंडर्ड `GITHUB_TOKEN` और रिपॉजिटरी परमिशन पर निर्भर करता है।

## आवश्यकताएँ

GitHub Action को कॉन्फ़िगर करने से पहले, सुनिश्चित करें कि आपके पास जरूरी AI सेवा के क्रेडेंशियल्स हैं।

**1. जरूरी: AI Language Model क्रेडेंशियल्स**
आपको कम से कम एक सपोर्टेड Language Model के लिए क्रेडेंशियल्स चाहिए:

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Name, API Version चाहिए।
- **OpenAI**: API Key, (वैकल्पिक: Org ID, Base URL, Model ID) चाहिए।
- विवरण के लिए देखें [Supported Models and Services](../../../../README.md)।
- सेटअप गाइड: [Azure OpenAI सेटअप करें](../set-up-resources/set-up-azure-openai.md)।

**2. वैकल्पिक: Computer Vision क्रेडेंशियल्स (इमेज अनुवाद के लिए)**

- सिर्फ तब जरूरी है जब आपको इमेज के अंदर के टेक्स्ट का अनुवाद करना हो।
- **Azure Computer Vision**: Endpoint और Subscription Key चाहिए।
- अगर नहीं दिया गया, तो एक्शन [Markdown-only mode](../markdown-only-mode.md) पर डिफॉल्ट हो जाएगा।
- सेटअप गाइड: [Azure Computer Vision सेटअप करें](../set-up-resources/set-up-azure-computer-vision.md)।

## सेटअप और कॉन्फ़िगरेशन

नीचे दिए गए स्टेप्स को फॉलो करें ताकि Co-op Translator GitHub Action को अपने रिपॉजिटरी में कॉन्फ़िगर कर सकें:

### स्टेप 1: GitHub App Authentication इंस्टॉल और कॉन्फ़िगर करें

वर्कफ्लो आपके रिपॉजिटरी के साथ सुरक्षित रूप से इंटरैक्ट करने के लिए GitHub App authentication का उपयोग करता है (जैसे पुल रिक्वेस्ट बनाना)। कोई एक विकल्प चुनें:

#### **विकल्प A: Pre-built Co-op Translator GitHub App इंस्टॉल करें (Microsoft आंतरिक उपयोग के लिए)**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) पेज पर जाएँ।

1. **Install** चुनें और उस अकाउंट या संगठन को चुनें जिसमें आपका टारगेट रिपॉजिटरी है।

    <img src="../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.hi.png" alt="ऐप इंस्टॉल करें">

1. **Only select repositories** चुनें और अपना टारगेट रिपॉजिटरी (जैसे `PhiCookBook`) चुनें। **Install** पर क्लिक करें। आपसे ऑथेंटिकेट करने के लिए कहा जा सकता है।

    <img src="../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.hi.png" alt="इंस्टॉल ऑथराइज़ करें">

1. **App क्रेडेंशियल्स प्राप्त करें (आंतरिक प्रक्रिया जरूरी):** वर्कफ्लो को ऐप के रूप में ऑथेंटिकेट करने के लिए आपको Co-op Translator टीम से दो जानकारी लेनी होगी:
  - **App ID:** Co-op Translator ऐप का यूनिक आइडेंटिफायर। App ID है: `1164076`.
  - **Private Key:** आपको मेंटेनर से **पूरे `.pem` प्राइवेट की फाइल का कंटेंट** लेना होगा। **इस की को पासवर्ड की तरह सुरक्षित रखें।**

1. स्टेप 2 पर जाएँ।

#### **विकल्प B: अपना खुद का कस्टम GitHub App उपयोग करें**

- अगर आप चाहें, तो अपना खुद का GitHub App बना सकते हैं। सुनिश्चित करें कि उसमें Contents और Pull requests के लिए Read & write एक्सेस हो। आपको उसका App ID और जनरेटेड Private Key चाहिए होगी।

### स्टेप 2: रिपॉजिटरी सीक्रेट्स कॉन्फ़िगर करें

आपको GitHub App के क्रेडेंशियल्स और AI सेवा के क्रेडेंशियल्स को अपने रिपॉजिटरी सेटिंग्स में एन्क्रिप्टेड सीक्रेट्स के रूप में जोड़ना होगा।

1. अपने टारगेट GitHub रिपॉजिटरी (जैसे `PhiCookBook`) पर जाएँ।

1. **Settings** > **Secrets and variables** > **Actions** पर जाएँ।

1. **Repository secrets** के तहत, नीचे दिए गए हर सीक्रेट के लिए **New repository secret** पर क्लिक करें।

   <img src="../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.hi.png" alt="सेटिंग एक्शन चुनें">

**जरूरी सीक्रेट्स (GitHub App Authentication के लिए):**

| सीक्रेट नाम          | विवरण                                      | वैल्यू स्रोत                                     |
| :------------------- | :----------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | GitHub App का App ID (स्टेप 1 से)।         | GitHub App Settings                             |
| `GH_APP_PRIVATE_KEY` | डाउनलोड किए गए `.pem` फाइल का **पूरा कंटेंट**। | `.pem` फाइल (स्टेप 1 से)                        |

**AI सेवा के सीक्रेट्स (आवश्यकता अनुसार सभी जोड़ें):**

| सीक्रेट नाम                         | विवरण                               | वैल्यू स्रोत                     |
| :---------------------------------- | :---------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) के लिए Key  | Azure AI Foundry                    |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) के लिए Endpoint | Azure AI Foundry                     |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI सेवा के लिए Key              | Azure AI Foundry                     |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI सेवा के लिए Endpoint         | Azure AI Foundry                     |
| `AZURE_OPENAI_MODEL_NAME`           | आपका Azure OpenAI Model Name              | Azure AI Foundry                     |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | आपका Azure OpenAI Deployment Name         | Azure AI Foundry                     |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI के लिए API Version           | Azure AI Foundry                     |
| `OPENAI_API_KEY`                    | OpenAI के लिए API Key                     | OpenAI Platform                  |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                    | OpenAI Platform                  |
| `OPENAI_CHAT_MODEL_ID`              | स्पेसिफिक OpenAI मॉडल ID                  | OpenAI Platform                    |
| `OPENAI_BASE_URL`                   | कस्टम OpenAI API Base URL                 | OpenAI Platform                    |

<img src="../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.hi.png" alt="एनवायरनमेंट वेरिएबल नाम दर्ज करें">

### स्टेप 3: वर्कफ्लो फाइल बनाएं

अंत में, YAML फाइल बनाएं जो ऑटोमेटेड वर्कफ्लो को परिभाषित करती है।

1. अपने रिपॉजिटरी के रूट डायरेक्टरी में `.github/workflows/` डायरेक्टरी बनाएं (अगर नहीं है)।

1. `.github/workflows/` के अंदर `co-op-translator.yml` नाम से फाइल बनाएं।

1. नीचे दिया गया कंटेंट co-op-translator.yml में पेस्ट करें।

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

4.  **वर्कफ्लो कस्टमाइज़ करें:**
  - **[!IMPORTANT] टारगेट भाषाएँ:** `Run Co-op Translator` स्टेप में, आपको **भाषा कोड्स की लिस्ट** को `translate -l "..." -y` कमांड में अपनी प्रोजेक्ट की जरूरत के अनुसार बदलना या एडजस्ट करना जरूरी है। उदाहरण वाली लिस्ट (`ar de es...`) को बदलें या एडजस्ट करें।
  - **ट्रिगर (`on:`):** अभी का ट्रिगर हर बार `main` पर पुश होने पर चलता है। बड़े रिपॉजिटरी के लिए, `paths:` फिल्टर (YAML में कमेंटेड उदाहरण देखें) जोड़ने पर विचार करें ताकि वर्कफ्लो सिर्फ तब चले जब जरूरी फाइलें (जैसे सोर्स डाक्यूमेंटेशन) बदलें, जिससे रनर मिनट्स बचें।
  - **PR विवरण:** अगर जरूरत हो तो `commit-message`, `title`, `body`, `branch` नाम, और `labels` को `Create Pull Request` स्टेप में कस्टमाइज़ करें।

## क्रेडेंशियल प्रबंधन और नवीनीकरण

- **सुरक्षा:** संवेदनशील क्रेडेंशियल्स (API keys, private keys) को हमेशा GitHub Actions सीक्रेट्स के रूप में स्टोर करें। इन्हें कभी भी वर्कफ्लो फाइल या रिपॉजिटरी कोड में एक्सपोज़ न करें।
- **[!IMPORTANT] की नवीनीकरण (Microsoft आंतरिक उपयोगकर्ता):** ध्यान रखें कि Microsoft के अंदर उपयोग की जा रही Azure OpenAI key का अनिवार्य नवीनीकरण पॉलिसी हो सकती है (जैसे हर 5 महीने में)। वर्कफ्लो फेल होने से बचाने के लिए संबंधित GitHub सीक्रेट्स (`AZURE_OPENAI_...` keys) को **समय रहते अपडेट करें**।

## वर्कफ्लो चलाना

> [!WARNING]  
> **GitHub-hosted Runner समय सीमा:**  
> GitHub-hosted रनर जैसे `ubuntu-latest` की **अधिकतम रनिंग समय सीमा 6 घंटे** है।  
> अगर बड़े डाक्यूमेंटेशन रिपॉजिटरी में ट्रांसलेशन प्रोसेस 6 घंटे से ज्यादा हो जाता है, तो वर्कफ्लो अपने आप बंद हो जाएगा।  
> इससे बचने के लिए:  
> - **सेल्फ-होस्टेड रनर** का उपयोग करें (कोई समय सीमा नहीं)  
> - हर रन में टारगेट भाषाओं की संख्या कम करें

जब `co-op-translator.yml` फाइल आपके मुख्य ब्रांच (या `on:` ट्रिगर में दी गई ब्रांच) में मर्ज हो जाती है, तो वर्कफ्लो अपने आप चलेगा जब भी उस ब्रांच में बदलाव पुश किए जाएँ (और अगर `paths` फिल्टर कॉन्फ़िगर किया है तो उसके अनुसार)।

अगर अनुवाद जनरेट या अपडेट होते हैं, तो एक्शन अपने आप बदलाव के साथ एक Pull Request बना देगा, जो आपकी समीक्षा और मर्जिंग के लिए तैयार रहेगा।

---

**अस्वीकरण**:
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयास करते हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।