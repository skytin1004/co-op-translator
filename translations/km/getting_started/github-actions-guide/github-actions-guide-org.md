# ការប្រើប្រាស់ Co-op Translator GitHub Action (មគ្គុទេសក៍អង្គភាព)

**ទស្សនិកជនគោលដៅ៖** មគ្គុទេសក៍នេះមានគោលបំណងសម្រាប់ **អ្នកប្រើប្រាស់ Microsoft ខាងក្នុង** ឬ **ក្រុមដែលមានការចូលដំណើរការចំណុចសំខាន់សម្រាប់ GitHub App Co-op Translator ដែលបានបង្កើតរួចហើយ** ឬអាចបង្កើត GitHub App ផ្ទាល់ខ្លួនរបស់ខ្លួន។

ធ្វើអូតូម៉ាទិកការបកប្រែឯកសារប្រមូលផ្តុំរបស់អ្នកយ៉ាងងាយស្រួល ដោយប្រើប្រាស់ Co-op Translator GitHub Action។ មគ្គុទេសក៍នេះនាំឲ្យអ្នកដំណើរការការកំណត់សកម្មភាព ដើម្បីបង្កើត pull requests ដោយស្វ័យប្រវត្តិជាមួយការបកប្រែដែលបានបច្ចុប្បន្នភាពពេលមានការផ្លាស់ប្តូរបណ្តា Markdown ឬរូបភាពដើមរបស់អ្នក។

> [!IMPORTANT]
> 
> **ជ្រើសរើសមគ្គុទេសក៍ដែលត្រឹមត្រូវ៖**
>
> មគ្គុទេសក៍នេះពណ៌នាអំពីការកំណត់ដោយប្រើ **GitHub App ID និងកញ្ចប់ឯកជន**។ ប្រភេទ "មគ្គុទេសក៍អង្គភាព" នេះជាញឹកញាប់ត្រូវការបើ៖ **ភាពសិទ្ធ GITHUB_TOKEN ត្រូវបានដាក់កំណត់៖** ស្ថាបត្យកម្មអង្គភាពរបស់អ្នក ឬការកំណត់ផ្គុំរបស់អ្នកដាក់កំណត់នូវភាពសិទ្ធលំនាំដើមដែលបានផ្តល់ជូន GITHUB_TOKEN។ ជាពិសេស ប្រសិនបើ GITHUB_TOKEN មិនទទួលបានភាពសិទ្ធ `write` ដែលចាំបាច់ (ដូចជា `contents: write` ឬ `pull-requests: write`) សកម្មភាពក្នុង [Public Setup Guide](./github-actions-guide-public.md) នឹងបរាជ័យដោយសារខ្វះភាពសិទ្ធ។ ការប្រើ GitHub App ដែលមានសិទ្ធដោយផ្ទាល់ក្តៅកាច់នេះ អាចជៀសវាងការកំណត់កំណត់នេះ។
>
> **ប្រសិនបើមិនគួរផ្ទាល់ទៅអ្នក៖**
>
> ប្រសិនបើ GITHUB_TOKEN ល្អគ្រប់គ្រាន់ក្នុងផ្គុំរបស់អ្នក (មានន័យថា មិនត្រូវបានបិទដោយការកំណត់អង្គភាព) សូមប្រើ **[Public Setup Guide using GITHUB_TOKEN](./github-actions-guide-public.md)**។ មគ្គុទេសក៍សាធារណៈមិនត្រូវការទទួលឬគ្រប់គ្រង App IDs ឬកញ្ចប់ឯកជនឡើយ ហើយផ្អែកលើ GITHUB_TOKEN និងសិទ្ធផ្គុំរូបភេទលំនាំដើមតែប៉ុណ្ណោះ។

## លក្ខខណ្ឌមុន

មុនការកំណត់ Co-op Translator GitHub Action សូមប្រាកដថាអ្នកមានព័ត៌មានសម្គាល់សេវាកម្ម AI ដែលចាំបាច់រួចរាល់។

**១. អ្វីដែលចាំបាច់៖ ព័ត៍មានសម្គាល់ម៉ូដែលភាសា AI**  
អ្នកត្រូវការព័ត៌មានចូលសម្រាប់ម៉ូដែលភាសាមួយយ៉ាងហោចណាស់៖

- **Azure OpenAI**: ត្រូវការប្រភេទ Endpoint, យក API Key, ឈ្មោះម៉ូដែល/ការបំពេញ, ទំរង់ API Version។  
- **OpenAI**: ត្រូវការប្រភេទ API Key, (មិនចាំបាច់៖ Org ID, Base URL, Model ID)។  
- មើល [Supported Models and Services](../../../../README.md) សម្រាប់ព័ត៌មានលម្អិត។  
- មគ្គុទេសក៍កំណត់៖ [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)។

**២. មិនចាំបាច់៖ ព័ត៌មានសម្គាល់ Computer Vision (សម្រាប់បកប្រែរូបភាព)**

- ត្រូវការ ប៉ុណ្ណោះ ប្រសិនបើអ្នកចង់បកប្រែអត្ថបទក្នុងរូបភាព។  
- **Azure Computer Vision**: ត្រូវការប្រភេទ Endpoint និង Subscription Key។  
- ប្រសិនបើមិនបានផ្តល់ វា នឹងប្រើ [Markdown-only mode](../markdown-only-mode.md) ដោយបើកចំហលំនាំដើម។  
- មាគ្គុទេសក៍កំណត់៖ [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)។

## ការតំឡើង និង ការកំណត់

អនុវត្តតាមជំហានទាំងនេះ ដើម្បីកំណត់ Co-op Translator GitHub Action ក្នុងផ្គុំរបស់អ្នក៖

### ជំហានទី ១៖ ដំឡើង និង កំណត់ការផ្ទៀងផ្ទាត់ GitHub App

កម្មវិធីនេះប្រើការផ្ទៀងផ្ទាត់ GitHub App ដើម្បីធ្វើសកម្មភាពនៅក្នុងផ្គុំរបស់អ្នក (ដូចជា បង្កើតមេកា PR) ដោយសុវត្ថិភាព។ ជ្រើសរើសជម្រើសមួយ៖

#### **ជម្រើស ក៖ ដំឡើង GitHub App Co-op Translator ដែលបានបង្កើតរួចហើយ (សម្រាប់ការប្រើប្រាស់ Microsoft ខាងក្នុង)**

1. យកទៅកាន់ទំព័រ [Co-op Translator GitHub App](https://github.com/apps/co-op-translator)។

1. ជ្រើស **Install** ហើយជ្រើសគណនី ឬអង្គភាពដែលផ្គុំទិសដៅរបស់អ្នកស្ថិតនៅតំណាង។

    ![Install app](../../../../getting_started/github-actions-guide/imgs/install-app.png)

1. ជ្រើស **Only select repositories** ហើយជ្រើសផ្គុំទិសដៅរបស់អ្នក (ឧ. `PhiCookBook`) ចុច **Install**។ អ្នកប្រហែលជាត្រូវតែផ្ទៀងផ្ទាត់។

    ![Install authorize](../../../../getting_started/github-actions-guide/imgs/install-authorize.png)

1. **ទទួលព័ត៌មានសម្គាល់ App (ដំណើរការខាងក្នុងត្រូវការ):** ដើម្បីអោយកម្មវិធីផ្ទៀងផ្ទាត់ជាបណ្តើរជាអ្នកប្រើ app អ្នកត្រូវការព័ត៌មាន ២ ផ្នែកដែលបានផ្តល់ឡើងដោយបុគ្គលកាន់កាប់ Co-op Translator៖  
  - **App ID:** លេខសម្គាល់ពិសេសសម្រាប់មុខងារ Co-op Translator។ App ID គឺ៖ `1164076`។  
  - **កញ្ចប់ឯកជន Private Key:** អ្នកត្រូវទទួលបាន **មាតិកាលំបាកទាំងស្រុង** នៃឯកសារ `.pem` ពីអ្នកទំនាក់ទំនង់។ **រក្សាទុក key នេះដូចជាការពាក្យសម្ងាត់ និងរក្សាទុកឲ្យបានសុវត្ថិភាព។**

1. បន្តទៅជំហាន ២។

#### **ជម្រើស ខ៖ ប្រើ GitHub App ផ្ទាល់ខ្លួនរបស់អ្នក**

- ប្រសិនបើចង់ អ្នកអាចបង្កើត និងកំណត់ GitHub App ផ្ទាល់ខ្លួន មានសិទ្ធអាន និងសរសេរ លើមាតិកា និង Pull requests។ អ្នកនឹងត្រូវការទទួល App ID និងកញ្ចប់ឯកជន Private Key ដែលបានបង្កើត។

### ជំហានទី ២៖ កំណត់ Secrets សម្រាប់ផ្គុំ

អ្នកត្រូវបន្ថែមព័ត៌មាន GitHub App និងព័ត៌មានសេវា AI របស់អ្នកជារបាំងសម្ងាត់ (encrypted secrets) នៅក្នុងការកំណត់ផ្គុំរបស់អ្នក។

1. យកទៅផ្គុំ GitHub ទិសដៅរបស់អ្នក (ឧ. `PhiCookBook`)។

1. ទៅកាន់ **Settings** > **Secrets and variables** > **Actions**។

1. នៅក្រោម **Repository secrets** ចុច **New repository secret** សម្រាប់មួយឯកសារសម្ងាត់នីមួយៗដែលបានរាយបញ្ចូលនៅខាងក្រោម។

   ![Select setting action](../../../../getting_started/github-actions-guide/imgs/select-setting-action.png)

**ព័ត៍មានសម្ងាត់ចាំបាច់ (សម្រាប់ចូលប្រើ GitHub App Authentication):**

| ឈ្មោះសម្ងាត់       | សេចក្តីពិពណ៌នា                                  | ផ្លូវប្រភពតម្លៃ                              |
| :------------------- | :----------------------------------------------- | :--------------------------------------------- |
| `GH_APP_ID`          | លេខសម្គាល់ App នៃ GitHub App (ពីជំហានទី ១)     | ការកំណត់ GitHub App                        |
| `GH_APP_PRIVATE_KEY` | **មាតិកាលំបាកទាំងស្រុង** នៃឯកសារ `.pem` ពីការទាញយក | ឯកសារ `.pem` (ពីជំហានទី ១)             |

**ព័ត៍មានសម្ងាត់សេវា AI (បន្ថែមរួចទៅទាំងអស់ដែលអនុវត្តតាមលក្ខខណ្ឌមុន):**

| ឈ្មោះសម្ងាត់                         | ពិពណ៌នា                                  | ផ្លូវប្រភពតម្លៃ                                 |
| :---------------------------------- | :---------------------------------------- | :----------------------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`          | Key សម្រាប់ Azure AI Service (Computer Vision)  | Azure AI Foundry                                |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint សម្រាប់ Azure AI Service (Computer Vision) | Azure AI Foundry                             |
| `AZURE_OPENAI_API_KEY`               | Key សម្រាប់ Azure OpenAI service           | Azure AI Foundry                                |
| `AZURE_OPENAI_ENDPOINT`              | Endpoint សម្រាប់ Azure OpenAI service       | Azure AI Foundry                                |
| `AZURE_OPENAI_MODEL_NAME`            | ឈ្មោះម៉ូដែល Azure OpenAI របស់អ្នក        | Azure AI Foundry                                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | ឈ្មោះការប្រើការបង្ហោះ Azure OpenAI របស់អ្នក | Azure AI Foundry                             |
| `AZURE_OPENAI_API_VERSION`           | ទំរង់ API សម្រាប់ Azure OpenAI             | Azure AI Foundry                                |
| `OPENAI_API_KEY`                     | Key API សម្រាប់ OpenAI                      | OpenAI Platform                                |
| `OPENAI_ORG_ID`                     | លេខសម្គាល់អង្គភាព OpenAI                  | OpenAI Platform                                |
| `OPENAI_CHAT_MODEL_ID`              | លេខសម្គាល់ម៉ូដែលពិសេស OpenAI               | OpenAI Platform                                |
| `OPENAI_BASE_URL`                   | URL ផ្ទាល់ខ្លួនសម្រាប់ OpenAI API           | OpenAI Platform                                |

![Enter environment variable name](../../../../getting_started/github-actions-guide/imgs/add-secrets-done.png)

### ជំហានទី ៣៖ បង្កើតឯកសារកម្មវិធី Workflow

ចុងក្រោយ បង្កើតឯកសារ YAML ដែលកំណត់កម្មវិធីដំណើរការអូតូម៉ាទិក។

1. នៅក្នុងថត root នៃផ្គុំរបស់អ្នក បង្កើតថត `.github/workflows/` ប្រសិនបើមិនមាន។

1. នៅក្នុង `.github/workflows/` បង្កើតឯកសារជា `co-op-translator.yml`។

1. បិទបន្តខ្លឹមសារខាងក្រោមទៅក្នុង co-op-translator.yml។

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

4.  **កែសម្រួលកម្មវិធី Workflow៖**
  - **[!IMPORTANT] ភាសាគោលដៅ៖** នៅជំហាន `Run Co-op Translator` អ្នក **ត្រូវតែពិនិត្យឡើងវិញ និងកែប្រែបញ្ជីកូដភាសា** នៅក្នុង `translate -l "..." -y` ដើម្បីឲ្យសម្របទៅតាមតម្រូវការគម្រោងរបស់អ្នក។ បញ្ជីឧទាហរណ៍ (`ar de es...`) ត្រូវបានប្ដូរឬកែប្រែបាន។  
  - **ព្រឹត្តិការណ៍ប្រើ (trigger `on:`):** ព្រឹត្តិការណ៍បច្ចុប្បន្នដំណើរការត្រូវធ្វើពេលមានកំណត់ជា push ទៅ `main`។ សម្រាប់ផ្គុំធំនោះ សូមពិចារណាការបន្ថែម filter `paths:` (មើលឧទាហរណ៍បានយល់ព្រមក្នុង YAML) ដើម្បីដំណើរការកម្មវិធីនៅពេលមានការផ្លាស់ប្តូរឯកសារសម្រួល (ឧ. ឯកសារបទបញ្ជាដើមប៉ុណ្ណោះ) ដើម្បីរក្សាsecon runner។  
  - **ព័ត៌មាន PR ៖** ជៀសរើស `commit-message`, `title`, `body`, ឈ្មោះ `branch` និង `labels` នៅជំហាន `Create Pull Request` ប្រសិនបើចាំបាច់។

## ការគ្រប់គ្រង និង ការបង្ហាញបច្ចុប្បន្នភាពភស្តុតាង

- **សុវត្ថិភាព៖** សូមរក្សាទុកព័ត៍មានសម្គាល់ដែលមានសំខាន់ (API keys, private keys) ទាំងអស់ជា Secrets ក្នុង GitHub Action។ មិនចាញ់បង្ហាញក្នុងឯកសារកម្មវិធី ឬកូដផ្គុំ។  
- **[!IMPORTANT] ការបន្តបន្ទុកកូនសោ (សម្រាប់អ្នកប្រើប្រាស់ Microsoft ខាងក្នុង):** សូមយល់ថា key Azure OpenAI ដែលប្រើនៅ Microsoft អាចមានគោលនយោបាយបង្ហាប់ការបន្ត (យ៉ាងហោចណាស់រាល់ ៥ ខែ)។ សូមប្រាកដថាអ្នកធ្វើបច្ចុប្បន្នភាព GitHub secrets (`AZURE_OPENAI_...`) **មុនពេលវាប្រហែលផុតកំណត់** ដើម្បីការពារការបរាជ័យបច្ចេកទេសសកម្មភាព។

## ការដំណើរការកម្មវិធី Workflow

> [!WARNING]  
> **ពេលវេលាដំណើរការ GitHub-hosted Runner:**  
> GitHub-hosted runners ដូចជា `ubuntu-latest` មាន **ពេលវេលាដំណើរការក្រោម6ម៉ោង**។  
> សម្រាប់ផ្គុំឯកសារធំ ប្រសិនបើដំណើរការបកប្រែលើស 6 ម៉ោង កម្មវិធីនឹងត្រូវបានបញ្ចប់ដោយស្វ័យប្រវត្តិ។  
> ដើម្បីជៀសវាង នេះ សូមពិចារណា៖  
> - ប្រើប្រាស់ **self-hosted runner** (គ្មានកំណត់ពេលវេលា)  
> - បន្ថយចំនួនភាសាគោលដៅក្នុងមួយដំណើរការ  

ពេលឯកសារ `co-op-translator.yml` ត្រូវបានបញ្ចូល (merge) ទៅក្នុងសាខា main របស់អ្នក (ឬសាខានៅក្នុងព្រឹត្តិការណ៍ `on:`) សកម្មភាពនឹងដំណើរការដោយស្វ័យប្រវត្តិពេលមានការផ្លាស់ប្តូរដាក់ចូលក្នុងសាខានោះ (ហើយត្រូវតាម filter `paths` ប្រសិនបើបានកំណត់)។

ប្រសិនបើមានការបង្កើត ឬបច្ចុប្បន្នភាពការបកប្រែ សកម្មភាពនឹងបង្កើត Pull Request ដោយស្វ័យប្រវត្តិរួចរាល់ សម្រាប់អ្នកពិនិត្យ និងផ្សំរួម។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបញ្ចាក់**៖  
ឯកសារនេះបានបំលែងភាសាដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់ព្រមថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬការខុសប្រក្រតីណាមួយ។ ឯកសារដើមក្នុងភាសាមួយរបស់វាគួរត្រូវបានគេចាត់ទុកជាមូលដ្ឋានដែលមានតម្លៃខ្ពស់។ សម្រាប់ព័ត៌មានដែលសំខាន់ ប្រសិនបើអាចធ្វើទៅបាន គួរប្រើការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយខុសៗ កើតមានដោយសារការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->