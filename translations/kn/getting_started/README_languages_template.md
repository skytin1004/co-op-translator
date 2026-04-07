# 🌐 ಬಹುಭಾಷಾ ಬೆಂಬಲ (ಟೆಂಪ್ಲೇಟ್)

ಪರಿಣತಿಕಾರರು: ಕೆಳಗಿನ ಬ್ಲಾಕ್ ಅನ್ನು Co-op Translator ನಿರ್ವಹಿಸುವ "ಎಲ್ಲ ಭಾಷೆಗಳು" ಉದಾಹರಣೆ.

- ನೀವು `translate` (ಯಾವುದೇ ಭಾಷಾ ಆಯ್ಕೆ) ಅನ್ನು ಚಲಾಯಿಸಿದಾಗ Co-op Translator ಈ ಪಟ್ಟಿ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಂಪೂರ್ಣವಾಗಿ ನವೀನಗೊಳಿಸಲಿ ಎಂದರೆ, ಎರಡು ಕಾಮೆಂಟ್ ಮಾರ್ಕರ್‌ಗಳನ್ನು ಹಾಗೇ ವಹಿಸಿ.
- ನೀವು ಕೆಲ ಭಾಷೆಗಳ ಮಾತ್ರ ತೋರಿಸಲು ಬಯಸಿದರೆ, ಎರಡು ಕಾಮೆಂಟ್ ಮಾರ್ಕರ್‌ಗಳನ್ನು ಅಳಿಸಿ ಮತ್ತು ನೀವು ಪಟ್ಟಿ ಮಾಡಬಯಸದ ಯಾವುದೇ ಭಾಷೆಗಳನ್ನು ತೆಗೆದು ಹಾಕಿ. ಮಾರ್ಕರ್‌ಗಳನ್ನು ತೆಗೆದ ನಂತರ, Co-op Translator ಈ ವಿಭಾಗವನ್ನು ಸ್ವಯಂಪ್ರತಿಷ್ಠಾಪಿಸಲಾಗುವುದಿಲ್ಲ.

- ಈಗಿನ ವಿಭಾಗದಲ್ಲಿ "ಸ್ಥಳೀಯವಾಗಿ ಕ್ಲೋನ್ ಮಾಡುವುದು ಮುಂದುವರಿಸುವಿರಾ?" ಎಂಬ ಸಲಹೆ ಸೇರಿಸಲಾಗಿದೆ, ಇದು ಬಳಕೆದಾರರು ದೊಡ್ಡ ಅನುವಾದ ಪೆಲೋಡನ್ನು ತಡೆಯುವಲ್ಲಿ ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನಿಮ್ಮ ರೆಪೊವೈ URL ನಿಂದ ಸಲಹೆಯನ್ನು ವೈಯಕ್ತೀಕರಿಸಲು ಉದಾಹರಣೆಗೆ, ಕೆಳಗಿನಂತೆ ರನ್ ಮಾಡಬಹುದು:
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.

<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ವೆಚ್ಚನೆ**:  
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿಕೊಂಡು ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ಶುದ್ಧತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ ಕೂಡ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳಿರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ದಾಖಲೆ ಅದರ ಮೂಲ ಭಾಷೆೆಯಲ್ಲಿ ಅಧಿಕೃತ ಉಲ್ಲೇಖವಾಗಿರುತ್ತದೆ. ಗಂಭೀರ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುರ್ಥಗಳು ಅಥವಾ ದೋಷ ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->