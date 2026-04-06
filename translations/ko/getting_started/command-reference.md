# 명령어 참조

**Co-op Translator** CLI는 번역 과정을 사용자 지정할 수 있는 여러 옵션을 제공합니다:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 프로젝트를 지정된 언어로 번역합니다. 예: translate -l "es fr de"는 스페인어, 프랑스어, 독일어로 번역합니다. 모든 지원 언어로 번역하려면 translate -l "all"을 사용하세요.
translate -l "language_codes" -u              | 기존 번역을 삭제하고 다시 생성하여 번역을 업데이트합니다. 경고: 지정된 언어에 대한 모든 현재 번역이 삭제됩니다.
translate -l "language_codes" -img            | 이미지 파일만 번역합니다.
translate -l "language_codes" -md             | 마크다운 파일만 번역합니다.
translate -l "language_codes" -nb             | Jupyter 노트북 파일(.ipynb)만 번역합니다.
translate -l "language_codes" --fix           | 이전 평가 결과에 기반한 낮은 신뢰도 점수 파일을 재번역합니다.
translate -l "language_codes" -d              | 자세한 로그를 위한 디버그 모드를 활성화합니다.
translate -l "language_codes" --save-logs, -s | DEBUG 수준의 로그를 <root_dir>/logs/ 아래 파일로 저장합니다 (콘솔은 -d에 의해 조절됨)
translate -l "language_codes" -r "root_dir"   | 프로젝트의 루트 디렉토리를 지정합니다.
translate -l "language_codes" -f              | 이미지 번역에 대해 빠른 모드를 사용합니다 (품질 및 정렬은 약간 손해보지만 최대 3배 빠른 플로팅).
translate -l "language_codes" -y              | 모든 프롬프트를 자동으로 확인합니다 (CI/CD 파이프라인에 유용).
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 번역된 마크다운 및 노트북에 기계 번역 면책 조항 섹션을 추가할지 여부를 설정합니다 (기본값: 활성화).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | README 언어 섹션 권고문(희소 체크아웃)을 저장소 URL에 맞게 개인화합니다.
translate -l "language_codes" --help          | 사용 가능한 명령어를 보여주는 CLI 내 도움말 세부사항.
evaluate -l "language_code"                  | 특정 언어에 대한 번역 품질을 평가하고 신뢰도 점수를 제공합니다.
evaluate -l "language_code" -c 0.8           | 사용자 정의 신뢰도 임계값으로 번역 평가.
evaluate -l "language_code" -f               | 빠른 평가 모드 (규칙 기반, LLM 없음).
evaluate -l "language_code" -D               | 심층 평가 모드 (LLM 기반, 더 철저하지만 느림).
evaluate -l "language_code" --save-logs, -s  | DEBUG 수준 로그를 <root_dir>/logs/에 파일로 저장.
migrate-links -l "language_codes"             | 번역된 마크다운 파일을 재처리하여 노트북(.ipynb) 링크를 업데이트합니다. 번역된 노트북이 있으면 이를 우선 사용하며, 없으면 원본 노트북으로 대체 가능.
migrate-links -l "language_codes" -r          | 프로젝트 루트 디렉토리를 지정합니다 (기본값: 현재 디렉토리).
migrate-links -l "language_codes" --dry-run   | 파일을 변경하지 않고 어떤 파일이 변경될지 보여줍니다.
migrate-links -l "language_codes" --no-fallback-to-original | 번역된 노트북이 없으면 원본 노트북으로의 링크를 변경하지 않습니다 (번역된 경우에만 업데이트).
migrate-links -l "language_codes" -d          | 자세한 로그를 위한 디버그 모드 활성화.
migrate-links -l "language_codes" --save-logs, -s | DEBUG 수준의 로그를 <root_dir>/logs/에 파일로 저장.
migrate-links -l "all" -y                      | 모든 언어를 처리하고 경고 프롬프트를 자동으로 확인합니다.

## 사용 예시

  1. 기본 동작 (기존 번역을 삭제하지 않고 새 번역만 추가):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 기존 번역을 삭제하지 않고 한국어 이미지 번역만 추가:    translate -l "ko" -img

  3. 모든 한국어 번역을 업데이트 (경고: 기존 한국어 번역 전부 삭제 후 재번역):    translate -l "ko" -u

  4. 한국어 이미지 번역만 업데이트 (경고: 기존 한국어 이미지 전부 삭제 후 재번역):    translate -l "ko" -img -u

  5. 다른 번역에는 영향 없이 한국어 마크다운 번역만 새로 추가:    translate -l "ko" -md

  6. 이전 평가 결과를 기반으로 낮은 신뢰도 번역 수정: translate -l "ko" --fix

  7. 특정 파일(마크다운)만 낮은 신뢰도 번역 수정: translate -l "ko" --fix -md

  8. 특정 파일(이미지)만 낮은 신뢰도 번역 수정: translate -l "ko" --fix -img

  9. 이미지 번역에 빠른 모드 사용:    translate -l "ko" -img -f

  10. 사용자 지정 임계값으로 낮은 신뢰도 번역 수정: translate -l "ko" --fix -c 0.8

  11. 디버그 모드 예시: - translate -l "ko" -d: 디버그 로그 활성화.
  12. 로그를 파일로 저장: translate -l "ko" -s
  13. 콘솔 DEBUG 및 파일 DEBUG 동시 사용: translate -l "ko" -d -s
  14. 출력에 기계 번역 면책 조항을 추가하지 않고 번역: translate -l "ko" --no-disclaimer

  15. 한국어 번역용 노트북 링크 마이그레이션 (가능한 경우 번역된 노트북 링크로 변경):    migrate-links -l "ko"

  15. 변경 사항 없이 어떤 파일이 변경될지 확인 (dry-run):    migrate-links -l "ko" --dry-run

  16. 번역된 노트북이 있을 경우에만 링크 업데이트 (원본 노트북 링크로 대체하지 않음):    migrate-links -l "ko" --no-fallback-to-original

  17. 확인 프롬프트와 함께 모든 언어 처리:    migrate-links -l "all"

  18. 모든 언어 처리 및 자동 확인:    migrate-links -l "all" -y
  19. migrate-links용 로그를 파일로 저장:    migrate-links -l "ko ja" -s

  20. 저장소 URL로 README 언어 권고문 개인화:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 평가 예시

> [!WARNING]  
> **베타 기능**: 평가 기능은 현재 베타 단계입니다. 이 기능은 번역된 문서를 평가하기 위해 공개되었으며, 평가 방법과 세부 구현은 아직 개발 중이며 변경될 수 있습니다.

  1. 한국어 번역 평가: evaluate -l "ko"

  2. 사용자 지정 신뢰도 임계값으로 평가: evaluate -l "ko" -c 0.8

  3. 빠른 평가 (규칙 기반만): evaluate -l "ko" -f

  4. 심층 평가 (LLM 기반만): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어의 원문이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->