# "Other Courses" 섹션 업데이트 (Microsoft Beginners 저장소)

이 가이드는 Co‑op Translator를 사용하여 "Other Courses" 섹션을 자동 동기화하는 방법과 모든 저장소에 대한 전역 템플릿을 업데이트하는 방법을 설명합니다.

- 적용 대상: Microsoft Beginners 저장소에만 해당
- 작동 방식: Co‑op Translator CLI 및 GitHub Actions와 함께 작동
- 템플릿 소스: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## 빠른 시작: 저장소에서 자동 동기화 활성화

README의 "Other Courses" 섹션 주위에 다음 마커를 추가하세요. Co‑op Translator는 이 마커 사이의 모든 내용을 실행할 때마다 교체합니다.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator가 CLI(예: `translate -l "<language codes>"`) 또는 GitHub Actions를 통해 실행될 때마다 자동으로 이 마커로 감싸진 "Other Courses" 섹션을 업데이트합니다.

> [!NOTE]
> 기존 목록이 있다면 동일한 마커로 감싸기만 하면 됩니다. 다음 실행 시 최신 표준화된 내용으로 교체됩니다.

---

## 전역 콘텐츠 변경 방법

모든 Beginners 저장소에 표시되는 표준화된 내용을 업데이트하려면:

1. 템플릿 편집: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. 변경 사항을 포함하여 Co-op Translator 저장소에 풀 리퀘스트를 엽니다.
3. PR이 병합되면 Co‑op Translator 버전이 업데이트됩니다.
4. 대상 저장소에서 다음에 Co‑op Translator(CLI 또는 GitHub Action)가 실행되면 업데이트된 섹션을 자동으로 동기화합니다.

이렇게 하면 모든 Beginners 저장소에서 "Other Courses" 콘텐츠의 단일 진실 공급원이 보장됩니다.


## 저장소 크기

사용자에게 가이드를 제공하기 위해 번역된 언어 수 때문에 저장소 크기가 커질 수 있으므로 전체 저장소가 아닌 필요한 언어만 클론하도록 clone - sparse 사용 방법을 안내합니다.

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
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역은 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문 문서는 원어로 된 원본이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우에는 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인한 오해나 잘못된 해석에 대해서는 저희가 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->