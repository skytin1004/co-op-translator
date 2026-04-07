# Co-op Translator GitHub Action 사용 가이드 (조직용)

**대상:** 이 가이드는 **Microsoft 내부 사용자** 또는 **사전 구축된 Co-op Translator GitHub App에 필요한 자격 증명에 접근할 수 있는 팀** 혹은 자체 GitHub App을 만들 수 있는 팀을 위한 것입니다.

Co-op Translator GitHub Action을 사용해 저장소의 문서 번역을 자동화하세요. 이 가이드는 소스 Markdown 파일이나 이미지가 변경될 때마다 자동으로 번역이 업데이트된 Pull Request를 생성하는 방법을 안내합니다.

> [!IMPORTANT]
>
> **적합한 가이드 선택:**
>
> 이 가이드는 **GitHub App ID와 Private Key**를 사용하는 설정 방법을 설명합니다. 일반적으로 다음과 같은 경우 "조직용 가이드"가 필요합니다: **`GITHUB_TOKEN` 권한이 제한된 경우:** 조직 또는 저장소 설정에서 기본적으로 제공되는 `GITHUB_TOKEN`의 권한이 제한되어 있을 때입니다. 특히, `GITHUB_TOKEN`이 필요한 `write` 권한(예: `contents: write` 또는 `pull-requests: write`)을 허용하지 않는 경우, [공개 설정 가이드](./github-actions-guide-public.md)의 워크플로우는 권한 부족으로 실패합니다. 별도의 GitHub App을 사용하면 명시적으로 권한을 부여할 수 있어 이 제한을 우회할 수 있습니다.
>
> **위 내용이 해당되지 않는 경우:**
>
> 저장소에서 기본 `GITHUB_TOKEN`이 충분한 권한을 가지고 있다면(즉, 조직 정책에 의해 차단되지 않았다면), **[GITHUB_TOKEN을 사용하는 공개 설정 가이드](./github-actions-guide-public.md)**를 사용하세요. 공개 가이드는 App ID나 Private Key를 별도로 관리할 필요 없이, 표준 `GITHUB_TOKEN`과 저장소 권한만으로 동작합니다.

## 사전 준비

GitHub Action을 설정하기 전에 필요한 AI 서비스 자격 증명을 준비하세요.

**1. 필수: AI 언어 모델 자격 증명**
최소 한 가지 지원되는 언어 모델의 자격 증명이 필요합니다.

- **Azure OpenAI**: Endpoint, API Key, Model/Deployment Name, API Version 필요
- **OpenAI**: API Key 필요, (선택: Org ID, Base URL, Model ID)
- 자세한 내용은 [지원 모델 및 서비스](../../../../README.md) 참고
- 설정 가이드: [Azure OpenAI 설정](../set-up-resources/set-up-azure-openai.md)

**2. 선택: 컴퓨터 비전 자격 증명 (이미지 번역용)**

- 이미지 내 텍스트 번역이 필요한 경우에만 필요합니다.
- **Azure Computer Vision**: Endpoint와 Subscription Key 필요
- 미제공 시, [Markdown 전용 모드](../markdown-only-mode.md)로 동작합니다.
- 설정 가이드: [Azure Computer Vision 설정](../set-up-resources/set-up-azure-computer-vision.md)

## 설정 및 구성

아래 단계에 따라 저장소에 Co-op Translator GitHub Action을 설정하세요.

### 1단계: GitHub App 인증 설치 및 구성

워크플로우는 GitHub App 인증을 사용해 저장소에 안전하게 접근(예: Pull Request 생성)합니다. 아래 옵션 중 하나를 선택하세요.

#### **옵션 A: 사전 구축된 Co-op Translator GitHub App 설치 (Microsoft 내부용)**

1. [Co-op Translator GitHub App](https://github.com/apps/co-op-translator) 페이지로 이동합니다.

1. **Install**을 선택하고, 대상 저장소가 있는 계정 또는 조직을 선택합니다.

    ![앱 설치](../../../../translated_images/install-app.d0f0a24cbb1d6c93f293f002eb34e633f7bc8f5caaba46b97806ba7bdc958f27.ko.png)

1. **Only select repositories**를 선택한 후, 대상 저장소(예: `PhiCookBook`)를 선택하고 **Install**을 클릭합니다. 인증을 요구할 수 있습니다.

    ![설치 인증](../../../../translated_images/install-authorize.29df6238c3eb8f707e7fc6f97a946cb654b328530c4aeddce28b874693f076a0.ko.png)

1. **앱 자격 증명 획득(내부 프로세스 필요):** 워크플로우가 앱으로 인증할 수 있도록 Co-op Translator 팀에서 제공하는 두 가지 정보가 필요합니다:
  - **App ID:** Co-op Translator 앱의 고유 식별자. App ID는 `1164076`입니다.
  - **Private Key:** 담당자에게서 받은 `.pem` 개인 키 파일의 **전체 내용**이 필요합니다. **이 키는 비밀번호처럼 안전하게 보관하세요.**

1. 2단계로 진행하세요.

#### **옵션 B: 자체 GitHub App 사용**

- 원한다면 직접 GitHub App을 생성해 구성할 수 있습니다. Contents와 Pull requests에 대한 읽기/쓰기 권한이 필요합니다. App ID와 생성된 Private Key가 필요합니다.

### 2단계: 저장소 시크릿 설정

GitHub App 자격 증명과 AI 서비스 자격 증명을 저장소의 암호화된 시크릿으로 추가해야 합니다.

1. 대상 GitHub 저장소(예: `PhiCookBook`)로 이동합니다.

1. **Settings** > **Secrets and variables** > **Actions**로 이동합니다.

1. **Repository secrets**에서 아래 목록의 각 시크릿마다 **New repository secret**을 클릭합니다.

   ![액션 시크릿 설정 선택](../../../../translated_images/select-setting-action.3b95c915d60311592ca51ecb91b3a7bbe0ae45438a2ee872c1520dc90b677780.ko.png)

**필수 시크릿(GitHub App 인증용):**

| 시크릿 이름           | 설명                                             | 값 출처                                         |
| :------------------- | :----------------------------------------------- | :----------------------------------------------- |
| `GH_APP_ID`          | GitHub App의 App ID (1단계에서 획득)             | GitHub App 설정                                 |
| `GH_APP_PRIVATE_KEY` | 다운로드한 `.pem` 파일의 **전체 내용**           | `.pem` 파일 (1단계에서 획득)                     |

**AI 서비스 시크릿(사전 준비에 따라 모두 추가):**

| 시크릿 이름                          | 설명                                         | 값 출처                         |
| :---------------------------------- | :------------------------------------------ | :------------------------------ |
| `AZURE_AI_SERVICE_API_KEY`            | Azure AI Service(Computer Vision) 키           | Azure AI Foundry                |
| `AZURE_AI_SERVICE_ENDPOINT`         | Azure AI Service(Computer Vision) 엔드포인트   | Azure AI Foundry                |
| `AZURE_OPENAI_API_KEY`              | Azure OpenAI 서비스 키                        | Azure AI Foundry                |
| `AZURE_OPENAI_ENDPOINT`             | Azure OpenAI 서비스 엔드포인트                 | Azure AI Foundry                |
| `AZURE_OPENAI_MODEL_NAME`           | Azure OpenAI 모델 이름                        | Azure AI Foundry                |
| `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` | Azure OpenAI 배포 이름                        | Azure AI Foundry                |
| `AZURE_OPENAI_API_VERSION`          | Azure OpenAI API 버전                         | Azure AI Foundry                |
| `OPENAI_API_KEY`                    | OpenAI API 키                                 | OpenAI Platform                 |
| `OPENAI_ORG_ID`                     | OpenAI 조직 ID                                | OpenAI Platform                 |
| `OPENAI_CHAT_MODEL_ID`              | 특정 OpenAI 모델 ID                           | OpenAI Platform                 |
| `OPENAI_BASE_URL`                   | 커스텀 OpenAI API Base URL                    | OpenAI Platform                 |

![환경 변수 이름 입력](../../../../translated_images/add-secrets-done.444861ce6956d5cb20781ead1237fcc12805078349bb0d4e95bb9540ee192227.ko.png)

### 3단계: 워크플로우 파일 생성

마지막으로, 자동화 워크플로우를 정의하는 YAML 파일을 만듭니다.

1. 저장소 루트에 `.github/workflows/` 디렉터리가 없다면 생성합니다.

1. `.github/workflows/` 안에 `co-op-translator.yml` 파일을 만듭니다.

1. 아래 내용을 co-op-translator.yml에 붙여넣습니다.

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

4.  **워크플로우 커스터마이즈:**
  - **[!IMPORTANT] 대상 언어:** `Run Co-op Translator` 단계에서, `translate -l "..." -y` 명령어의 언어 코드 목록을 **반드시 검토 및 수정**하여 프로젝트에 맞게 설정하세요. 예시 목록(`ar de es...`)은 실제 필요에 맞게 교체하거나 조정해야 합니다.
  - **트리거(`on:`):** 현재 트리거는 `main` 브랜치에 푸시될 때마다 실행됩니다. 대형 저장소의 경우, 워크플로우가 관련 파일(예: 소스 문서) 변경 시에만 실행되도록 `paths:` 필터(주석 예시 참고)를 추가해 러너 사용량을 절약할 수 있습니다.
  - **PR 세부 정보:** 필요에 따라 `commit-message`, `title`, `body`, `branch` 이름, `labels` 등을 `Create Pull Request` 단계에서 커스터마이즈하세요.

## 자격 증명 관리 및 갱신

- **보안:** 민감한 자격 증명(API 키, 개인 키 등)은 반드시 GitHub Actions 시크릿으로 저장하세요. 워크플로우 파일이나 저장소 코드에 노출하지 마세요.
- **[!IMPORTANT] 키 갱신(Microsoft 내부 사용자):** Microsoft 내부에서 사용하는 Azure OpenAI 키는 일정 주기(예: 5개월)마다 갱신이 필요할 수 있습니다. 워크플로우 오류를 방지하려면 만료 전에 해당 GitHub 시크릿(`AZURE_OPENAI_...` 키)을 **미리 갱신**하세요.

## 워크플로우 실행

> [!WARNING]  
> **GitHub 호스팅 러너 시간 제한:**  
> `ubuntu-latest`와 같은 GitHub 호스팅 러너는 **최대 실행 시간 6시간** 제한이 있습니다.  
> 대형 문서 저장소의 경우, 번역 작업이 6시간을 초과하면 워크플로우가 자동 종료됩니다.  
> 이를 방지하려면:  
> - **셀프 호스팅 러너** 사용(시간 제한 없음)  
> - 실행당 대상 언어 수를 줄이기

`co-op-translator.yml` 파일이 main 브랜치(또는 `on:` 트리거에 지정된 브랜치)에 병합되면, 해당 브랜치에 변경 사항이 푸시될 때마다(필요시 `paths` 필터와 일치할 때만) 워크플로우가 자동으로 실행됩니다.

번역이 생성되거나 업데이트되면, 액션이 자동으로 변경 사항이 담긴 Pull Request를 생성하므로 검토 후 병합하면 됩니다.

---

**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서(원어)가 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.