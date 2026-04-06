# "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು تازهಗೊಳಿಸಿ (Microsoft ಪ್ರಾರಂಭಿಕ ರೆಪೋಗಳು)

ಈ ಮಾರ್ಗಸೂಚಿ Co‑op Translator ಬಳಸಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಮಕಾಲೀನಗೊಳಿಸುವುದು ಹೇಗೆ ಮತ್ತು ಎಲ್ಲಾ ರೆಪೋಗಳಿಗೆ ಗ್ಲೋಬಲ್ ಟೆಂಪ್ಲೇಟ್ ಅನ್ನು ಹೇಗೆ تازهಗೊಳಿಸಲು ಎಂಬುದನ್ನು ವಿವರಿಸುತ್ತದೆ.

- ಅನ್ವಯಿಸುತ್ತದೆ: Microsoft ಪ್ರಾರಂಭಿಕ ರೆಪೋಗಳಿಗಷ್ಟೇ
- ಕಾರ್ಯಗತಗೊಳಿಸುತ್ತದೆ: Co‑op Translator CLI ಮತ್ತು GitHub Actions ಜೊತೆಗೆ
- ಟೆಂಪ್ಲೇಟ್ ಮೂಲ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ದ್ರುತಾರಂಭ: ನಿಮ್ಮ ರೆಪೋದಲ್ಲಿ ಸ್ವಯಂ-ಸಿಂಕ್ ಸಕ್ರಿಯಗೊಳಿಸಿ

ನಿಮ್ಮ README ನಲ್ಲಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗದ ಸುತ್ತ ಕೆಳಗಿನ ಮಾರ್ಕರ್‌ಗಳನ್ನು ಸೇರಿಸಿ. Co‑op Translator ಪ್ರತಿಯೊಂದು ಓಟದಲ್ಲೂ ಈ ಮಾರ್ಕರ್‌ಗಳ ನಡುವೆ ಇರುವ ಎಲ್ಲವನ್ನೂ ಬದಲಾಯಿಸುತ್ತದೆ.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ಪ್ರತಿ ಬಾರಿ Co‑op Translator ಓಡುವಾಗ — CLI ಮೂಲಕ (ಉದಾ., `translate -l "<language codes>"`) ಅಥವಾ GitHub Actions — ಈ ಮಾರ್ಕರ್‌ಗಳ ನಡುವೆ ಸುತ್ತುವ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ تازهಗೊಳಿಸುತ್ತದೆ.

> [!NOTE]
> ನೀವು ಈಗಾಗಲೆಪಟ್ಟಿ ಹೊಂದಿದ್ದಲ್ಲಿ, ಅದನ್ನು ಅದೇ ಮಾರ್ಕರ್‌ಗಳೊಂದಿಗೆ ಸುತ್ತಿಸಿ. ಮುಂದಿನ ಓಟದಲ್ಲಿ ಅದನ್ನು ಇತ್ತೀಚಿನ ಪ್ರಮಾಣೀಕೃತ ವಿಷಯದಿಂದ ಬದಲಾಯಿಸಲಾಗುತ್ತದೆ.

---

## ಗ್ಲೋಬಲ್ ವಿಷಯವನ್ನು ಹೇಗೆ ಬದಲಾಯಿಸಬೇಕು

ನೀವು ಎಲ್ಲಾ ಪ್ರಾರಂಭಿಕ ರೆಪೋಗಳಲ್ಲಿ ಕಾಣಿಸಿಕೊಳ್ಳುವ ಪ್ರಮಾಣೀಕೃತ ವಿಷಯವನ್ನು تازهಗೊಳಿಸಲು ಬಯಸಿದರೆ:

1. ಟೆಂಪ್ಲೇಟ್ ಸಂಪಾದಿಸಿ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ನಿಮ್ಮ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ Co-op Translator ರೆಪೋಗೆ pull request ತೆರೆಯಿರಿ
3. PR ನ ಲಿಖಿತಗೊಳಿಸಿದ ನಂತರ, Co‑op Translator ಆವೃತ್ತಿ تازهಗೊಳಿಸಲಾಗುತ್ತದೆ
4. ಮುಂದಿನ ಬಾರಿ Co‑op Translator ಓಡುವಾಗ (CLI ಅಥವಾ GitHub Action), ಗುರಿತಗೊಂಡ ರೆಪೋದಲ್ಲಿ تازهಗೊಳಿಸಿದ ವಿಭಾಗ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಿಂಕ್ ಆಗುತ್ತದೆ

ಇದು ಎಲ್ಲಾ ಪ್ರಾರಂಭಿಕ ರೆಪೋಗಳಲ್ಲಿ "ಇತರ ಕೋರ್ಸ್‌ಗಳು" ವಿಷಯಕ್ಕೆ ಒಂದೇ ಮೂಲ ಸತ್ಯವನ್ನು ಖಚಿತಪಡಿಸುತ್ತದೆ.

## ರೆಪೋ ಗಾತ್ರಗಳು

ಅನುವಾದಿಸಿದ ಭಾಷೆಗಳ ಸಂಖ್ಯೆಯಿಂದ ರೆಪೋಗಳು ದೊಡ್ಡದಾಗಬಹುದು, ಇದು ಅಂತಿಮ ಬಳಕೆದಾರರಿಗೆ `clone - sparse` ಯನ್ನು ಬಳಸುವ ಕುರಿತು ಮಾರ್ಗದರ್ಶನ ನೀಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ, ಇದರಿಂದ ಅವಶ್ಯಕ ಭಾಷೆಗಳ ಜೊತೆಗೆ ಮಾತ್ರ ಕ್ಲೋನ್ ಮಾಡಿ ಸಂಪೂರ್ಣ ರೆಪೋ ಕ್ಲೋನ್ ಮಾಡುವ ಅಗತ್ಯವಿಲ್ಲ.

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
**ನಿರಾಕರಣ**:
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯ ಮೇಲೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂಬುದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿನ ಮೂಲ ದಸ್ತಾವೇಜು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವದ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಗರ್ಭಿತತೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->