# "ಇತರೆ ಕೋರ್ಸುಗಳು" ವಿಭಾಗವನ್ನು ನವೀಕರಿಸಿ (Microsoft Beginners ರೆಪೋಗಳು)

ಈ ಮಾರ್ಗಸೂಚಿ "ಇತರೆ ಕೋರ್ಸುಗಳು" ವಿಭಾಗವನ್ನು Co‑op Translator ಬಳಸಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ದಾಖಲೆ ಸಮನ್ವಯಗೊಳಿಸುವ ಮತ್ತು ಎಲ್ಲಾ ರೆಪೋಗಳಿಗಾಗಿ ಜಾಗತಿಕ ಟೆಂಪ್ಲೇಟನ್ನು ಹೇಗೆ ನವೀಕರಿಸಬೇಕು ಎಂಬುದನ್ನು ವಿವರಿಸುತ್ತದೆ.

- ಅನ್ವಯಿಸುವುದು: Microsoft Beginners ರೆಪೋಗಳಿಗಷ್ಟೇ
- ಕೆಲಸ ಮಾಡುವುದು: Co‑op Translator CLI ಮತ್ತು GitHub Actions ಜೊತೆ
- ಟೆಂಪ್ಲೇಟಿನ ಮೂಲ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ತ್ವರಿತ ಪ್ರಾರಂಭ: ನಿಮ್ಮ ರೆಪೋದಲ್ಲಿ ಸ್ವಯಂಚಾಲಿತ-ಸಿಂಕ್ ಸಕ್ರಿಯಗೊಳಿಸುವುದು

ನಿಮ್ಮ READMEನಲ್ಲಿ "ಇತರೆ ಕೋರ್ಸುಗಳು" ವಿಭಾಗದ ಸುತ್ತ ಕೆಳಗಿನ ಗುರುತುಗಳನ್ನು ಸೇರಿಸಿ. Co‑op Translator ಈ ಗುರುತುಗಳ ನಡುವೆ ಇರುವ ಎಲ್ಲವನ್ನೂ ಪ್ರತಿಕ್ಕೊಡುತ್ತದೆ.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ಪ್ರತಿ Co‑op Translator ಪ್ರಸರಣದಾಗು, CLI ಮೂಲಕ (ಉದಾ., `translate -l "<language codes>"`) ಅಥವಾ GitHub Actions ಮೂಲಕ, ಇದು ಈ ಗುರುತುಗಳ ಜತೆಗೆ ಮಡಿದ "ಇತರೆ ಕೋರ್ಸುಗಳು" ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನವೀಕರಿಸುತ್ತದೆ.

> [!NOTE]
> ನೀವು ಈಗಾಗಲೇ ಇರುವ ಪಟ್ಟಿಯನ್ನು ಹೊಂದಿದ್ದರೆ, ಅದನ್ನೇ ಆ ಗುರುತುಗಳೊಂದಿಗೆ ಸುತ್ತಿಕೊಳ್ಳಬೇಕು. ಮುಂದಿನ ಪ್ರಸರಣದಲ್ಲಿ ಅದನ್ನು ಹೊಸ ಇತ್ತೀಚಿನ ಪ್ರಮಾಣಿತ ವಿಷಯದಿಂದ ಬದಲಿಸಲಾಗುತ್ತದೆ.

---

## ಜಾಗತಿಕ ವಿಷಯವನ್ನು ಹೇಗೆ ಬದಲಾಯಿಸಬಹುದು

ಎಲ್ಲಾ Beginners ರೆಪೋಗಳಲ್ಲಿಯೂ ಕಂಡು ಬರುವ ಪ್ರಮಾಣಿತ ವಿಷಯವನ್ನು ನವೀಕರಿಸಲು:

1. ಟೆಂಪ್ಲೇಟನ್ನು ಸಂಪಾದಿಸಿ: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. ನಿಮ್ಮ ಬದಲಾವಣೆಗಳೊಂದಿಗೆ Co-op Translator ರೆಪೋಗೆ pull request ತೆರೆಯಿರಿ
3. PR ಏಕೀಕೃತವಾದ ನಂತರ, Co‑op Translator ಆವೃತ್ತಿ ನವೀಕರಿಸಲಾಗುತ್ತದೆ
4. ಮುಂದಿನ ಬಾರಿ Co‑op Translator (CLI ಅಥವಾ GitHub Action) ಗುರಿ ರೆಪೋದಲ್ಲಿ ಚಲಿಸಿದಾಗ, ಸ್ವಯಂಚಾಲಿತವಾಗಿ ನವೀಕೃತ ವಿಭಾಗವನ್ನು ಸಿಂಕ್ ಮಾಡುತ್ತದೆ

ಈದು ಎಲ್ಲಾ Beginners ರೆಪೋಗಳಲ್ಲಿ "ಇತರೆ ಕೋರ್ಸುಗಳು" ವಿಷಯಕ್ಕೆ ಏಕೈಕ ಸತ್ಯ ವಹಿಸುವ ಮೂಲವನ್ನು ಖಾತ್ರಿ ಪಡಿಸುತ್ತದೆ.

## ರೆಪೋ ಗಾತ್ರಗಳು

ಎನ್ಡ್ಇউಸರ್ಗಳಿಗೆ ಕೈಪಿಡಿ ನೀಡಲು ಅನುವಾದಿತ ಭಾಷೆಗಳ ಸಂಖ್ಯೆ ಹೆಚ್ಚಾದ ಕಾರಣ ರೆಪೋಗಳು ದೊಡ್ಡದಾಗಬಹುದು. ആവശ്യವಿರುವ ಭಾಷೆಗಳನ್ನೇ ಕ್ಲೋನ್ ಮಾಡಲು clone - sparse ಉಪಯೋಗಿಸುವ ಬಗ್ಗೆ ಮಾರ್ಗದರ್ಶನಕ್ಕಾಗಿ.

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
**ನಿರಾಕರಣೆ**:  
ಈ ದಾಖಲೆ AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆನ್ನು ಅಧಿಕಾರಿಕ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತ misunderstandings ್ಫಸ್ಯಗಳು ಅಥವಾ ತಪ್ಪು ಅರ್ಥೈಸಿಕೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗಿರುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->