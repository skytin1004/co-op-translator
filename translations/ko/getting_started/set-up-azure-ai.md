# Co-op Translator용 Azure AI 설정 (Azure OpneAI 및 Azure AI Vision)

이 가이드는 Azure AI Foundry 내에서 언어 번역을 위한 Azure OpenAI와 이미지 기반 번역에 사용할 수 있는 이미지 콘텐츠 분석을 위한 Azure Computer Vision 설정 방법을 안내합니다.

**사전 조건:**
- 활성 구독이 있는 Azure 계정.
- Azure 구독 내에서 리소스 및 배포를 생성할 수 있는 충분한 권한.

## Azure AI 프로젝트 만들기

AI 리소스를 관리하는 중심지 역할을 하는 Azure AI 프로젝트를 만드는 것부터 시작합니다.

1. [https://ai.azure.com](https://ai.azure.com)로 이동하여 Azure 계정으로 로그인합니다.

1. <strong>+Create</strong>를 선택하여 새 프로젝트를 만듭니다.

1. 다음 작업을 수행합니다:
   - **프로젝트 이름** 입력 (예: `CoopTranslator-Project`).
   - **AI hub** 선택 (예: `CoopTranslator-Hub`) (필요 시 새로 만듭니다).

1. "**검토 및 만들기**"를 클릭하여 프로젝트를 설정합니다. 프로젝트 개요 페이지로 이동됩니다.

## 언어 번역을 위한 Azure OpenAI 설정

프로젝트 내에서 텍스트 번역을 위한 백엔드로 사용할 Azure OpenAI 모델을 배포합니다.

### 프로젝트로 이동

아직 이동하지 않았다면 Azure AI Foundry에서 새로 만든 프로젝트(예: `CoopTranslator-Project`)를 엽니다.

### OpenAI 모델 배포

1. 프로젝트 왼쪽 메뉴에서 "내 자산" 아래의 "**Models + endpoints**"를 선택합니다.

1. <strong>+ 모델 배포</strong>를 선택합니다.

1. <strong>기본 모델 배포</strong>를 선택합니다.

1. 사용할 수 있는 모델 목록이 표시됩니다. 적합한 GPT 모델을 필터하거나 검색합니다. 권장 모델은 `gpt-4o`입니다.

1. 원하는 모델을 선택하고 <strong>확인</strong>을 클릭합니다.

1. <strong>배포</strong>를 선택합니다.

### Azure OpenAI 구성

배포가 완료되면 "**Models + endpoints**" 페이지에서 배포를 선택하여 **REST 엔드포인트 URL**, <strong>키</strong>, **배포 이름**, **모델 이름**, <strong>API 버전</strong>을 확인할 수 있습니다. 이 정보들은 번역 모델을 애플리케이션에 통합하는 데 필요합니다.

> [!NOTE]
> [API 버전 폐기](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) 페이지에서 요구 사항에 따라 API 버전을 선택할 수 있습니다. <strong>API 버전</strong>은 Azure AI Foundry의 "**Models + endpoints**" 페이지에 표시된 <strong>모델 버전</strong>과 다르다는 점에 유의하세요.

## 이미지 번역을 위한 Azure Computer Vision 설정

이미지 내 텍스트 번역을 활성화하려면 Azure AI 서비스 API 키와 엔드포인트를 찾아야 합니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동하여 프로젝트 개요 페이지에 있는지 확인합니다.

### Azure AI 서비스 구성

Azure AI 서비스에서 API 키와 엔드포인트를 찾습니다.

1. Azure AI 프로젝트(예: `CoopTranslator-Project`)로 이동하여 프로젝트 개요 페이지에 있는지 확인합니다.

1. Azure AI 서비스 탭에서 <strong>API 키</strong>와 <strong>엔드포인트</strong>를 찾습니다.

    ![API 키 및 엔드포인트 찾기](../../../getting_started/imgs/find-azure-ai-info.png)

이 연결은 연결된 Azure AI 서비스 리소스(이미지 분석 포함)의 기능을 AI Foundry 프로젝트에서 사용할 수 있게 합니다. 이후 노트북이나 애플리케이션에서 이 연결을 사용하여 이미지에서 텍스트를 추출하고, 추출한 텍스트를 Azure OpenAI 모델로 보내 번역할 수 있습니다.

## 인증 정보 통합

지금쯤 다음 정보를 수집했을 것입니다:

**Azure OpenAI (텍스트 번역용):**
- Azure OpenAI 엔드포인트
- Azure OpenAI API 키
- Azure OpenAI 모델 이름 (예: `gpt-4o`)
- Azure OpenAI 배포 이름 (예: `cooptranslator-gpt4o`)
- Azure OpenAI API 버전

**Azure AI 서비스 (Vision을 통한 이미지 텍스트 추출용):**
- Azure AI 서비스 엔드포인트
- Azure AI 서비스 API 키

### 예: 환경 변수 구성 (미리보기)

나중에 애플리케이션을 구성할 때, 이러한 수집한 인증 정보를 다음과 같이 환경 변수로 설정할 수 있습니다:

```bash
# Azure AI 서비스 자격 증명 (이미지 번역에 필요)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 예: 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# 선택적 대체 세트: 접미사 _1/_2가 붙은 중복 변수 (세트 내 모든 변수에 동일한 인덱스)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI 자격 증명 (텍스트 번역에 필요)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 예: 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 예: gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 예: cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 예: 2024-12-01-preview

# 선택적 대체 세트: 접미사 _1/_2가 붙은 전체 AZURE_OPENAI_* 세트 중복 (모든 변수에 동일한 인덱스)
```

---

### 추가 참고 자료

- [Azure AI Foundry에서 프로젝트 만드는 방법](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI 리소스 만드는 방법](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry에서 OpenAI 모델 배포하는 방법](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의해 주시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우 전문적인 사람 번역을 권장합니다. 본 번역 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->