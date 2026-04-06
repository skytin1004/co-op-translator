# "기타 코스" 섹션 업데이트 (Microsoft Beginners 저장소)

이 가이드는 Co‑op Translator를 사용하여 "기타 코스" 섹션을 자동 동기화하는 방법과 모든 저장소에 대한 전역 템플릿을 업데이트하는 방법을 설명합니다.

- 적용 대상: Microsoft Beginners 저장소만
- 작동 방식: Co‑op Translator CLI 및 GitHub Actions와 함께 작동
- 템플릿 소스: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 빠른 시작: 저장소에서 자동 동기화 활성화

README의 "기타 코스" 섹션 주위에 다음 마커를 추가하세요. Co‑op Translator는 실행할 때마다 이 마커 사이의 모든 내용을 교체합니다.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator가 실행될 때마다—CLI(예: `translate -l "<language codes>"`)나 GitHub Actions를 통해—이 마커로 감싼 "기타 코스" 섹션이 자동으로 업데이트됩니다.

> [!NOTE]
> 기존 목록이 있으면 동일한 마커로 감싸기만 하면 됩니다. 다음 실행 시 최신 표준화된 콘텐츠로 교체됩니다.

---

## 전역 콘텐츠 변경 방법

모든 Beginners 저장소에 표시되는 표준화된 콘텐츠를 업데이트하려면:

1. 템플릿 편집: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 변경 사항을 포함하여 Co-op Translator 저장소에 pull request 열기
3. PR이 병합되면 Co‑op Translator 버전이 업데이트됨
4. 대상 저장소에서 Co‑op Translator가 다음에 실행될 때(CLI 또는 GitHub Action) 업데이트된 섹션이 자동으로 동기화됨

이를 통해 모든 Beginners 저장소에서 "기타 코스" 콘텐츠에 대한 단일 진실 소스를 보장합니다.


## 저장소 크기

저장소가 번역되는 언어 수 때문에 커질 수 있으며, 이로 인해 최종 사용자가 필요한 언어만 클론하도록 clone - sparse 사용법에 대한 안내를 제공합니다.

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 알려드립니다. 원문은 해당 언어의 원본 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인력의 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 오해 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->