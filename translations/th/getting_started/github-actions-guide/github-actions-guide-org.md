# การใช้งาน Co-op Translator GitHub Action (คู่มือสำหรับองค์กร)

**กลุ่มเป้าหมาย:** คู่มือนี้เหมาะสำหรับ **ผู้ใช้ภายใน Microsoft** หรือ **ทีมที่มีสิทธิ์เข้าถึงข้อมูลรับรองสำหรับ Co-op Translator GitHub App ที่เตรียมไว้ล่วงหน้า** หรือสามารถสร้าง GitHub App ของตนเองได้

แปลเอกสารใน repository ของคุณโดยอัตโนมัติด้วย Co-op Translator GitHub Action คู่มือนี้จะแนะนำขั้นตอนการตั้งค่า action เพื่อสร้าง pull request พร้อมการแปลที่อัปเดตโดยอัตโนมัติทุกครั้งที่ไฟล์ Markdown ต้นทางหรือรูปภาพมีการเปลี่ยนแปลง

> [!IMPORTANT]
>
> **เลือกคู่มือให้ถูกต้อง:**
>
> คู่มือนี้อธิบายการตั้งค่าด้วย **GitHub App ID และ Private Key** โดยปกติคุณจะต้องใช้วิธี "คู่มือสำหรับองค์กร" นี้หาก: **`GITHUB_TOKEN` ถูกจำกัดสิทธิ์:** องค์กรหรือ repository ของคุณมีการจำกัดสิทธิ์เริ่มต้นของ `GITHUB_TOKEN` โดยเฉพาะหาก `GITHUB_TOKEN` ไม่ได้รับสิทธิ์ `write` ที่จำเป็น (เช่น `contents: write` หรือ `pull-requests: write`) workflow ใน [คู่มือสาธารณะ](./github-actions-guide-public.md) จะล้มเหลวเนื่องจากสิทธิ์ไม่เพียงพอ การใช้ GitHub App เฉพาะที่กำหนดสิทธิ์ชัดเจนจะช่วยแก้ปัญหานี้
>
> **หากข้อข้างต้นไม่ตรงกับคุณ:**
>
> หาก `GITHUB_TOKEN` มาตรฐานมีสิทธิ์เพียงพอใน repository ของคุณ (เช่น ไม่ถูกจำกัดโดยองค์กร) กรุณาใช้ **[คู่มือสาธารณะสำหรับ GITHUB_TOKEN](./github-actions-guide-public.md)** คู่มือสาธารณะไม่ต้องขอหรือจัดการ App ID หรือ Private Key ใดๆ ใช้แค่ `GITHUB_TOKEN` และสิทธิ์ repository เท่านั้น

## ข้อกำหนดเบื้องต้น

ก่อนตั้งค่า GitHub Action กรุณาเตรียมข้อมูลรับรอง AI service ที่จำเป็นให้พร้อม

**1. จำเป็น: ข้อมูลรับรอง AI Language Model**
คุณต้องมีข้อมูลรับรองสำหรับ Language Model ที่รองรับอย่างน้อย 1 รายการ:

- **Azure OpenAI**: ต้องใช้ Endpoint, API Key, ชื่อ Model/Deployment, API Version
- **OpenAI**: ต้องใช้ API Key, (ถ้ามี: Org ID, Base URL, Model ID)
- ดูรายละเอียดที่ [Supported Models and Services](../../../../README.md)
- คู่มือการตั้งค่า: [Set up Azure OpenAI](../set-up-resources/set-up-azure-openai.md)

**2. ไม่บังคับ: ข้อมูลรับรอง Computer Vision (สำหรับแปลข้อความในรูปภาพ)**

- ต้องใช้เฉพาะเมื่อคุณต้องการแปลข้อความในรูปภาพ
- **Azure Computer Vision**: ต้องใช้ Endpoint และ Subscription Key
- หากไม่ระบุ ระบบจะทำงานใน [Markdown-only mode](../markdown-only-mode.md) โดยอัตโนมัติ
- คู่มือการตั้งค่า: [Set up Azure Computer Vision](../set-up-resources/set-up-azure-computer-vision.md)

## ขั้นตอนการตั้งค่า

ทำตามขั้นตอนเหล่านี้เพื่อกำหนดค่า Co-op Translator GitHub Action ใน repository ของคุณ

### ขั้นตอนที่ 1: ติดตั้งและตั้งค่า GitHub App Authentication

workflow นี้ใช้ GitHub App authentication เพื่อเชื่อมต่อกับ repository ของคุณอย่างปลอดภัย (เช่น สร้าง pull request) เลือกหนึ่งในสองตัวเลือกนี้:

#### **ตัวเลือก A: ติดตั้ง Co-op Translator GitHub App ที่เตรียมไว้ (สำหรับผู้ใช้ Microsoft ภายใน)**

1. ไปที่หน้า [Co-op Translator GitHub App](https://github.com/apps/co-op-translator)

1. เลือก **Install** และเลือกบัญชีหรือองค์กรที่มี repository เป้าหมายของคุณ

    ![Install app](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.th.png)

1. เลือก **Only select repositories** แล้วเลือก repository เป้าหมายของคุณ (เช่น `PhiCookBook`) จากนั้นคลิก **Install** อาจมีการขอให้ยืนยันตัวตน

    ![Install authorize](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.th.png)

1. **ขอรับข้อมูลรับรอง App (ต้องดำเนินการภายใน):** เพื่อให้ workflow สามารถยืนยันตัวตนในนามของ app ได้ คุณต้องขอข้อมูล 2 อย่างจากทีม Co-op Translator:
  - **App ID:** รหัสประจำตัวของ Co-op Translator app โดย App ID คือ: `1164076`
  - **Private Key:** คุณต้องขอ **เนื้อหาทั้งหมด** ของไฟล์ private key `.pem` จากผู้ดูแล **เก็บรักษา key นี้ให้ปลอดภัยเหมือนรหัสผ่าน**

1. ไปยังขั้นตอนที่ 2

#### **ตัวเลือก B: สร้าง GitHub App ของคุณเอง**

- หากต้องการ คุณสามารถสร้างและตั้งค่า GitHub App ของคุณเอง ให้แน่ใจว่าได้กำหนดสิทธิ์ Read & write สำหรับ Contents และ Pull requests คุณจะต้องใช้ App ID และ Private Key ที่สร้างขึ้น

### ขั้นตอนที่ 2: กำหนดค่า Repository Secrets

คุณต้องเพิ่มข้อมูลรับรอง GitHub App และ AI service ของคุณเป็น secrets ที่เข้ารหัสใน repository

1. ไปที่ repository เป้าหมายของคุณ (เช่น `PhiCookBook`)

1. ไปที่ **Settings** > **Secrets and variables** > **Actions**

1. ใต้ **Repository secrets** คลิก **New repository secret** สำหรับแต่ละ secret ที่ระบุด้านล่าง

   ![Select setting action](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.th.png)

**Secrets ที่จำเป็น (สำหรับ GitHub App Authentication):**

| ชื่อ Secret           | คำอธิบาย                                         | แหล่งที่มา                                      |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | App ID ของ GitHub App (จากขั้นตอนที่ 1)          | GitHub App Settings                             |
| `GH_APP_PRIVATE_KEY` | **เนื้อหาทั้งหมด** ของไฟล์ `.pem` ที่ดาวน์โหลด   | ไฟล์ `.pem` (จากขั้นตอนที่ 1)                   |

**AI Service Secrets (เพิ่มทุกตัวที่เกี่ยวข้องตามข้อกำหนดเบื้องต้น):**

| ชื่อ Secret                          | คำอธิบาย                                 | แหล่งที่มา                        |
| :---------------------------------- | :---------------------------------------- | :--------------------------------- |
| `AZURE_AI_SERVICE_API_KEY`            | Key สำหรับ Azure AI Service (Computer Vision)  | Azure AI Foundry                  |
| `AZURE_AI_SERVICE_ENDPOINT`         | Endpoint สำหรับ Azure AI Service (Computer Vision) | Azure AI Foundry                 |
| `AZURE_OPENAI_API_KEY`              | Key สำหรับ Azure OpenAI service           | Azure AI Foundry                  |
| `AZURE_OPENAI_ENDPOINT`             | Endpoint สำหรับ Azure OpenAI service      | Azure AI Foundry                  |
| `AZURE_OPENAI_MODEL_NAME`           | ชื่อ Model ของ Azure OpenAI ของคุณ        | Azure AI Foundry                  |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | ชื่อ Deployment ของ Azure OpenAI ของคุณ   | Azure AI Foundry                  |
| `AZURE_OPENAI_API_VERSION`          | API Version สำหรับ Azure OpenAI           | Azure AI Foundry                  |
| `OPENAI_API_KEY`                    | API Key สำหรับ OpenAI                     | OpenAI Platform                   |
| `OPENAI_ORG_ID`                     | OpenAI Organization ID                    | OpenAI Platform                   |
| `OPENAI_CHAT_MODEL_ID`              | รหัส model เฉพาะของ OpenAI               | OpenAI Platform                   |
| `OPENAI_BASE_URL`                   | Base URL ของ OpenAI API ที่กำหนดเอง        | OpenAI Platform                   |

![Enter environment variable name](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.th.png)

### ขั้นตอนที่ 3: สร้าง Workflow File

สุดท้าย สร้างไฟล์ YAML ที่กำหนด workflow อัตโนมัติ

1. ที่ root directory ของ repository ให้สร้างโฟลเดอร์ `.github/workflows/` หากยังไม่มี

1. ใน `.github/workflows/` สร้างไฟล์ชื่อ `co-op-translator.yml`

1. วางเนื้อหาต่อไปนี้ลงใน co-op-translator.yml

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

4.  **ปรับแต่ง Workflow:**
  - **[!IMPORTANT] ภาษาที่ต้องการ:** ในขั้นตอน `Run Co-op Translator` คุณ **ต้องตรวจสอบและแก้ไขรายชื่อรหัสภาษา** ในคำสั่ง `translate -l "..." -y` ให้ตรงกับความต้องการของโปรเจกต์ รายการตัวอย่าง (`ar de es...`) ต้องเปลี่ยนหรือปรับให้เหมาะสม
  - **Trigger (`on:`):** ปัจจุบันจะทำงานทุกครั้งที่มี push ไปที่ `main` สำหรับ repository ขนาดใหญ่ แนะนำให้เพิ่ม `paths:` filter (ดูตัวอย่างที่คอมเมนต์ไว้ใน YAML) เพื่อให้ workflow ทำงานเฉพาะเมื่อไฟล์ที่เกี่ยวข้อง (เช่น เอกสารต้นทาง) เปลี่ยนแปลง จะช่วยประหยัด runner minutes
  - **รายละเอียด PR:** ปรับแต่ง `commit-message`, `title`, `body`, ชื่อ `branch` และ `labels` ในขั้นตอน `Create Pull Request` ได้ตามต้องการ

## การจัดการและต่ออายุข้อมูลรับรอง

- **ความปลอดภัย:** เก็บข้อมูลรับรองที่สำคัญ (API key, private key) ไว้ใน GitHub Actions secrets เท่านั้น ห้ามเปิดเผยใน workflow file หรือโค้ด repository
- **[!IMPORTANT] การต่ออายุ key (สำหรับผู้ใช้ Microsoft ภายใน):** โปรดทราบว่า Azure OpenAI key ที่ใช้ภายใน Microsoft อาจมีนโยบายต่ออายุ (เช่น ทุก 5 เดือน) กรุณาอัปเดต GitHub secrets (`AZURE_OPENAI_...`) **ก่อนหมดอายุ** เพื่อป้องกัน workflow ล้มเหลว

## การรัน Workflow

> [!WARNING]  
> **ขีดจำกัดเวลา Runner ที่ GitHub ให้บริการ:**  
> Runner ที่ GitHub ให้บริการ เช่น `ubuntu-latest` มี **ขีดจำกัดเวลาในการทำงานสูงสุด 6 ชั่วโมง**  
> สำหรับ repository เอกสารขนาดใหญ่ หากกระบวนการแปลใช้เวลานานเกิน 6 ชั่วโมง workflow จะถูกยกเลิกโดยอัตโนมัติ  
> เพื่อป้องกันปัญหานี้ แนะนำให้:  
> - ใช้ **self-hosted runner** (ไม่มีขีดจำกัดเวลา)  
> - ลดจำนวนภาษาที่แปลต่อรอบ

เมื่อไฟล์ `co-op-translator.yml` ถูก merge เข้าสู่ main branch (หรือ branch ที่ระบุใน trigger `on:`) workflow จะทำงานโดยอัตโนมัติทุกครั้งที่มีการ push ไปยัง branch นั้น (และตรงกับ filter `paths` หากตั้งค่าไว้)

หากมีการสร้างหรืออัปเดตไฟล์แปล Action จะสร้าง Pull Request พร้อมการเปลี่ยนแปลงโดยอัตโนมัติ เพื่อให้คุณตรวจสอบและ merge ได้ทันที

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้