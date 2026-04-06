# Co-op Translator GitHub Action ఉపయోగించడం (పబ్లిక్ సెటప్)

**లక్ష్య ప్రేక్షకులు:** ఈ గైడ్ సాధారణ GitHub Actions అనుమతులు సరిపోతున్న పబ్లిక్ లేదా ప్రైవేట్ రిపోజిటరీలలోని వినియోగదారుల కోసం రూపొందించబడింది. ఇది అంతర్గత `GITHUB_TOKEN` ను ఉపయోగిస్తుంది.

మీ రిపోజిటరీ డాక్యుమెంటేషన్ అనువాదాన్ని సులభంగా ఆటోమేట్ చేయండి Co-op Translator GitHub Action ఉపయోగించి. ఈ గైడ్ మీ సోర్స్ Markdown ఫైళ్ల లేదా చిత్రాలు మారినప్పుడు అనువాదాలతో కూడిన పుల్ రిక్వెస్టులను ఆటోమేటిక్‌గా సృష్టించడానికి సెటప్ చేయడం ఎలా చేయాలో వివరంగా చూపిస్తుంది.

> [!IMPORTANT]
>
> **సరైన గైడ్ ఎంపిక:**
>
> ఈ గైడ్ **సాధారణ సెటప్ `GITHUB_TOKEN` ఉపయోగించి** వివరంగా చూపిస్తుంది. ఇది చాలా వినియోగదారులకు సిఫార్సు చేయబడిన పద్ధతి, ఎందుకంటే ఇది సెన్సిటివ్ GitHub App ప్రైవేట్ కీలను నిర్వహించాల్సిన అవసరం లేదు.
>

## ముందస్తు అవసరాలు

GitHub Action ను కాన్ఫిగర్ చేయడానికి ముందు, అవసరమైన AI సర్వీస్ క్రెడెన్షియల్స్ సిద్ధంగా ఉన్నాయా అని నిర్ధారించుకోండి.

**1. అవసరం: AI లాంగ్వేజ్ మోడల్ క్రెడెన్షియల్స్**
కనీసం ఒక మద్దతు ఉన్న లాంగ్వేజ్ మోడల్ కోసం క్రెడెన్షియల్స్ అవసరం:

- **Azure OpenAI**: ఎండ్‌పాయింట్, API కీ, మోడల్/డిప్లాయ్‌మెంట్ పేర్లు, API వెర్షన్ అవసరం.
- **OpenAI**: API కీ అవసరం, (ఐచ్ఛికం: ఆర్గ్ ID, బేస్ URL, మోడల్ ID).
- [మద్దతు ఉన్న మోడల్స్ మరియు సర్వీసులు](../../../../README.md) వివరాల కోసం చూడండి.

**2. ఐచ్ఛికం: AI విజన్ క్రెడెన్షియల్స్ (చిత్ర అనువాదం కోసం)**

- చిత్రాలలోని టెక్స్ట్ అనువదించాల్సిన అవసరం ఉంటే మాత్రమే అవసరం.
- **Azure AI Vision**: ఎండ్‌పాయింట్ మరియు సబ్‌స్క్రిప్షన్ కీ అవసరం.
- అందుబాటులో లేకపోతే, ఈ యాక్షన్ [Markdown-only mode](../markdown-only-mode.md) కు డిఫాల్ట్ అవుతుంది.

## సెటప్ మరియు కాన్ఫిగరేషన్

సాధారణ `GITHUB_TOKEN` ఉపయోగించి Co-op Translator GitHub Action ను మీ రిపోజిటరీలో సెటప్ చేయడానికి ఈ దశలను అనుసరించండి.

### దశ 1: ఆథెంటికేషన్ అర్థం చేసుకోండి (`GITHUB_TOKEN` ఉపయోగించి)

ఈ వర్క్‌ఫ్లో GitHub Actions అందించిన అంతర్గత `GITHUB_TOKEN` ను ఉపయోగిస్తుంది. ఈ టోకెన్ **దశ 3** లో కాన్ఫిగర్ చేసిన సెట్టింగుల ఆధారంగా మీ రిపోజిటరీతో ఇంటరాక్ట్ చేయడానికి వర్క్‌ఫ్లోకు ఆటోమేటిక్‌గా అనుమతులు ఇస్తుంది.

### దశ 2: రిపోజిటరీ సీక్రెట్స్ కాన్ఫిగర్ చేయండి

మీ **AI సర్వీస్ క్రెడెన్షియల్స్** ను మీ రిపోజిటరీ సెట్టింగులలో ఎన్క్రిప్టెడ్ సీక్రెట్స్ గా జోడించాలి.

1.  మీ లక్ష్య GitHub రిపోజిటరీకి వెళ్లండి.
2.  **Settings** > **Secrets and variables** > **Actions** కు వెళ్లండి.
3.  **Repository secrets** కింద, క్రింది అవసరమైన AI సర్వీస్ సీక్రెట్స్ కోసం **New repository secret** క్లిక్ చేయండి.

    ![సెట్టింగ్ యాక్షన్ ఎంపిక](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png) *(చిత్ర సూచన: సీక్రెట్స్ ఎక్కడ జోడించాలో చూపిస్తుంది)*

**అవసరమైన AI సర్వీస్ సీక్రెట్స్ (మీ ముందస్తు అవసరాల ఆధారంగా వర్తించే వాటిని జోడించండి):**

| సీక్రెట్ పేరు                         | వివరణ                               | విలువ మూలం                     |
| :---------------------------------- | :---------------------------------------- | :------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service (Computer Vision) కోసం కీ  | మీ Azure AI Foundry               |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service (Computer Vision) కోసం ఎండ్‌పాయింట్ | మీ Azure AI Foundry               |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI సర్వీస్ కోసం కీ              | మీ Azure AI Foundry               |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI సర్వీస్ కోసం ఎండ్‌పాయింట్         | మీ Azure AI Foundry               |
| `AZURE_OPENAI_MODEL_NAME`           | మీ Azure OpenAI మోడల్ పేరు              | మీ Azure AI Foundry               |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | మీ Azure OpenAI డిప్లాయ్‌మెంట్ పేరు         | మీ Azure AI Foundry               |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI కోసం API వెర్షన్              | మీ Azure AI Foundry               |
| `OPENAI_API_KEY`                    | OpenAI కోసం API కీ                        | మీ OpenAI ప్లాట్‌ఫారమ్              |
| `OPENAI_ORG_ID`                     | OpenAI ఆర్గనైజేషన్ ID (ఐచ్ఛికం)         | మీ OpenAI ప్లాట్‌ఫారమ్              |
| `OPENAI_CHAT_MODEL_ID`              | నిర్దిష్ట OpenAI మోడల్ ID (ఐచ్ఛికం)       | మీ OpenAI ప్లాట్‌ఫారమ్              |
| `OPENAI_BASE_URL`                   | కస్టమ్ OpenAI API బేస్ URL (ఐచ్ఛికం)     | మీ OpenAI ప్లాట్‌ఫారమ్              |

### దశ 3: వర్క్‌ఫ్లో అనుమతులను కాన్ఫిగర్ చేయండి

GitHub Action ఈ వర్క్‌ఫ్లో కోసం కోడ్‌ను చెక్ అవుట్ చేయడానికి మరియు పుల్ రిక్వెస్టులను సృష్టించడానికి `GITHUB_TOKEN` ద్వారా అనుమతులు అవసరం.

1.  మీ రిపోజిటరీలో, **Settings** > **Actions** > **General** కు వెళ్లండి.
2.  **Workflow permissions** విభాగానికి స్క్రోల్ చేయండి.
3.  **Read and write permissions** ను ఎంచుకోండి. ఇది ఈ వర్క్‌ఫ్లో కోసం `contents: write` మరియు `pull-requests: write` అనుమతులను `GITHUB_TOKEN` కు ఇస్తుంది.
4.  **Allow GitHub Actions to create and approve pull requests** కోసం చెక్‌బాక్స్ **చెక్ చేయబడింది** అని నిర్ధారించుకోండి.
5.  **Save** ను ఎంచుకోండి.

![అనుమతి సెట్టింగ్](../../../../getting_started/github-actions-guide/imgs/permission-setting.png)

### దశ 4: వర్క్‌ఫ్లో ఫైల్ సృష్టించండి

చివరగా, `GITHUB_TOKEN` ఉపయోగించి ఆటోమేటెడ్ వర్క్‌ఫ్లోను నిర్వచించే YAML ఫైల్‌ను సృష్టించండి.

1.  మీ రిపోజిటరీ రూట్ డైరెక్టరీలో `.github/workflows/` డైరెక్టరీ లేదు అయితే సృష్టించండి.
2.  `.github/workflows/` లో, `co-op-translator.yml` అనే ఫైల్‌ను సృష్టించండి.
3.  `co-op-translator.yml` లో క్రింది కంటెంట్‌ను పేస్ట్ చేయండి.

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
4.  **వర్క్‌ఫ్లోను అనుకూలీకరించండి:**
  - **[!IMPORTANT] లక్ష్య భాషలు:** `Run Co-op Translator` దశలో, మీరు **మీ ప్రాజెక్ట్ అవసరాలకు సరిపోయేలా** `translate -l "..." -y` కమాండ్‌లో భాష కోడ్ల జాబితాను సమీక్షించి మార్చాలి. ఉదాహరణ జాబితా (`ar de es...`) ను భర్తీ చేయాలి లేదా సర్దుబాటు చేయాలి.
  - **ట్రిగ్గర్ (`on:`):** ప్రస్తుత ట్రిగ్గర్ `main` కు ప్రతి పుష్‌పై నడుస్తుంది. పెద్ద రిపోజిటరీల కోసం, వర్క్‌ఫ్లోను సంబంధిత ఫైళ్లు (ఉదా: సోర్స్ డాక్యుమెంటేషన్) మారినప్పుడు మాత్రమే నడపడానికి `paths:` ఫిల్టర్ జోడించడం (YAML లో కామెంట్ చేసిన ఉదాహరణ చూడండి) runner నిమిషాలను ఆదా చేస్తుంది.
  - **PR వివరాలు:** `Create Pull Request` దశలో `commit-message`, `title`, `body`, `branch` పేరు, మరియు `labels` ను అవసరమైతే అనుకూలీకరించండి.

## వర్క్‌ఫ్లో నడపడం

> [!WARNING]  
> **GitHub-హోస్టెడ్ రన్నర్ టైమ్ లిమిట్:**  
> `ubuntu-latest` వంటి GitHub-హోస్టెడ్ రన్నర్లకు **గరిష్ట అమలు సమయ పరిమితి 6 గంటలు** ఉంటుంది.  
> పెద్ద డాక్యుమెంటేషన్ రిపోజిటరీల కోసం, అనువాద ప్రక్రియ 6 గంటలు మించితే, వర్క్‌ఫ్లో ఆటోమేటిక్‌గా నిలిపివేయబడుతుంది.  
> దీన్ని నివారించడానికి, పరిగణించండి:  
> - **సెల్ఫ్-హోస్టెడ్ రన్నర్** ఉపయోగించడం (టైమ్ లిమిట్ లేదు)  
> - ప్రతి రన్‌కు లక్ష్య భాషల సంఖ్యను తగ్గించడం

`co-op-translator.yml` ఫైల్ మీ మెయిన్ బ్రాంచ్ (లేదా `on:` ట్రిగ్గర్‌లో పేర్కొన్న బ్రాంచ్) లో విలీనం చేయబడిన తర్వాత, వర్క్‌ఫ్లో ఆ బ్రాంచ్‌కు మార్పులు పుష్ చేసినప్పుడు (మరియు `paths` ఫిల్టర్, కాన్ఫిగర్ చేసినట్లయితే) ఆటోమేటిక్‌గా నడుస్తుంది.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:  
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->