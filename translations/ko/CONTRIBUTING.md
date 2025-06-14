<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d95d7ec0097c5569ac16dd42840787a2",
  "translation_date": "2025-06-12T09:29:21+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ko"
}
-->
# Contributing to Co-op Translator

이 프로젝트는 기여와 제안을 환영합니다. 대부분의 기여는 Contributor License Agreement(CLA)에 동의해야 하며, 이는 기여한 내용을 사용할 권리를 실제로 부여한다는 것을 선언하는 문서입니다. 자세한 내용은 https://cla.opensource.microsoft.com 에서 확인하세요.

풀 리퀘스트를 제출하면 CLA 봇이 자동으로 CLA 제출 필요 여부를 판단하고 PR에 상태 검사나 코멘트 등으로 표시합니다. 봇이 안내하는 절차를 따르면 되며, CLA는 모든 저장소에서 한 번만 제출하면 됩니다.

## 개발 환경 설정

이 프로젝트의 개발 환경을 설정할 때는 의존성 관리를 위해 Poetry 사용을 권장합니다. 프로젝트 의존성 관리를 위해 `pyproject.toml`를 사용하므로, 의존성을 설치할 때는 Poetry를 사용해야 합니다.

### 가상 환경 만들기

#### pip 사용 시

```bash
python -m venv .venv
```

#### Poetry 사용 시

```bash
poetry init
```

### 가상 환경 활성화

#### pip와 Poetry 모두 공통

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry 사용 시

```bash
poetry shell
```

### 패키지 및 필수 패키지 설치

#### Poetry 사용 (pyproject.toml 기준)

```bash
poetry install
```

### 수동 테스트

PR 제출 전에 실제 문서로 번역 기능을 테스트하는 것이 중요합니다:

1. 루트 디렉터리에 테스트 디렉터리 생성:
    ```bash
    mkdir test_docs
    ```

2. 번역할 마크다운 문서와 이미지를 테스트 디렉터리에 복사합니다. 예를 들어:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 로컬에 패키지 설치:
    ```bash
    pip install -e .
    ```

4. 테스트 문서에 대해 Co-op Translator 실행:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` and `test_docs/translated_images` to verify:
   - The translation quality
   - The metadata comments are correct
   - The original markdown structure is preserved
   - Links and images are working properly

This manual testing helps ensure that your changes work well in real-world scenarios.

### Environment variables

1. Create an `.env` file in the root directory by copying the provided `.env.template` 파일에서 번역된 파일 확인
1. 환경 변수는 안내에 따라 채워 넣으세요.

> [!TIP]
>
> ### 추가 개발 환경 옵션
>
> 로컬 실행 외에도 GitHub Codespaces나 VS Code Dev Containers를 사용해 대체 개발 환경을 구축할 수 있습니다.
>
> #### GitHub Codespaces
>
> GitHub Codespaces를 사용하면 추가 설정 없이 가상으로 샘플을 실행할 수 있습니다.
>
> 아래 버튼을 클릭하면 브라우저에서 웹 기반 VS Code 인스턴스가 열립니다:
>
> 1. 템플릿 열기 (몇 분 걸릴 수 있음):
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers로 로컬 실행
>
> ⚠️ 이 옵션은 Docker Desktop에 최소 16GB RAM이 할당되어 있어야 작동합니다. 16GB 미만일 경우 [GitHub Codespaces 옵션](../..) 또는 [로컬 환경 설정](../..)을 시도하세요.
>
> 관련 옵션으로 VS Code Dev Containers가 있으며, [Dev Containers 확장](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)을 사용해 로컬 VS Code에서 프로젝트를 열 수 있습니다:
>
> 1. Docker Desktop 시작 (설치되어 있지 않다면 설치)
> 2. 프로젝트 열기:
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### 코드 스타일

프로젝트 전반에 걸쳐 일관된 코드 스타일 유지를 위해 [Black](https://github.com/psf/black)을 Python 코드 포매터로 사용합니다. Black은 자동으로 Python 코드를 Black 스타일에 맞게 재포맷하는 엄격한 포매터입니다.

#### 설정

Black 설정은 `pyproject.toml`에 명시되어 있습니다:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black 설치

Black은 Poetry(권장)나 pip를 통해 설치할 수 있습니다:

##### Poetry 사용 시

개발 환경 설정 시 Black이 자동으로 설치됩니다:
```bash
poetry install
```

##### pip 사용 시

pip를 사용하는 경우 Black을 직접 설치할 수 있습니다:
```bash
pip install black
```

#### Black 사용법

##### Poetry 사용 시

1. 프로젝트 내 모든 Python 파일 포맷팅:
    ```bash
    poetry run black .
    ```

2. 특정 파일이나 디렉터리 포맷팅:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip 사용 시

1. 프로젝트 내 모든 Python 파일 포맷팅:
    ```bash
    black .
    ```

2. 특정 파일이나 디렉터리 포맷팅:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 저장 시 Black으로 자동 포맷팅하도록 에디터를 설정하는 것을 권장합니다. 대부분의 최신 에디터가 확장 기능이나 플러그인으로 지원합니다.

## Co-op Translator 실행하기

Poetry 환경에서 Co-op Translator를 실행하려면 다음 단계를 따르세요:

1. 번역 테스트를 진행할 디렉터리로 이동하거나 임시 폴더를 만듭니다.

2. 아래 명령을 실행합니다. `-l ko` with the language code you wish to translate into. The `-d` 플래그는 디버그 모드를 의미합니다.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 명령 실행 전에 Poetry 환경이 활성화(poetry shell)되어 있는지 확인하세요.

## Maintainers

### 커밋 메시지 및 병합 전략

프로젝트의 커밋 히스토리를 일관되고 명확하게 유지하기 위해, **Squash and Merge** 전략을 사용할 때 **최종 커밋 메시지**는 특정 형식을 따릅니다.

풀 리퀘스트(PR)가 병합되면 여러 커밋이 하나로 합쳐집니다. 최종 커밋 메시지는 깔끔하고 일관된 히스토리를 위해 아래 형식을 따라야 합니다.

#### 커밋 메시지 형식 (squash and merge용)

커밋 메시지는 다음 형식을 사용합니다:

```bash
<type>: <description> (#<PR number>)
```

- **type**: 커밋 종류를 지정합니다. 다음 타입을 사용합니다:
  - `Docs`: For documentation updates.
  - `Build`: For changes related to the build system or dependencies, including updates to configuration files, CI workflows, or the Dockerfile.
  - `Core`: For modifications to the project's core functionality or features, particularly those involving files in the `src/co_op_translator/core` directory.

- **description**: A concise summary of the change.
- **PR number**: The number of the pull request associated with the commit.

**Examples**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> Currently, the **`Docs`**, **`Core`**, and **`Build`** prefixes are automatically added to PR titles based on the labels applied to the modified source code. As long as the correct label is applied, you typically don't need to manually update the PR title. You just need to verify that everything is correct and the prefix has been generated appropriately.

#### Merge strategy

We use **Squash and Merge** as our default strategy for pull requests. This strategy ensures that commit messages follow our format, even if individual commits don't.

**Reasons**:

- A clean, linear project history.
- Consistency in commit messages.
- Reduced noise from minor commits (e.g., "fix typo").

When merging, ensure the final commit message follows the commit message format described above.

**Example of Squash and Merge**
If a PR contains the following commits:

- `fix typo`
- `update README`
- `adjust formatting`

They should be squashed into:
`Docs: Improve documentation clarity and formatting (#65)`

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의해 주시기 바랍니다. 원본 문서는 해당 언어로 된 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인한 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.