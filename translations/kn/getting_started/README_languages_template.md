# 🌐 ಬಹುಕಾತಿ ಬೆಂಬಲ (ಟೆಂಪ್ಲೇಟ್)

ನಿರ್ವಹಣಾಕಾರರು: ಕೆಳಗಿನ ಬ್ಲಾಕ್ ಅನ್ನು Co-op Translator ಮೇಲ್ವಿಚಾರಣೆ ಮಾಡುವ "ಎಲ್ಲಾ ಭಾಷೆಗಳು" ಉದಾಹರಣೆ ಎಂದು ನಿರ್ವಹಿಸಲಾಗುತ್ತದೆ.

- ನೀವು Co-op Translator ಈ ಪಟ್ಟಿಯನ್ನು `translate` (ಏನಾದರೂ ಭಾಷೆ ಆಯ್ಕೆ) ಚಾಲನೆಯಲ್ಲಿರುವಾಗ ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಸಂಪೂರ್ಣವಾಗಿ ನವೀಕರಿಸಬೇಕಾದರೆ, ಎರಡು వ్యాఖ్య ಚಿಹ್ನೆಗಳನ್ನು ಏನೂ ಬದಲಾಯಿಸದೆ ಇಡಿ.
- ನೀವು ಭಾಷೆಗಳ ಉಪಸಮೂಹವನ್ನು ಮಾತ್ರ ತೋರಿಸಲು ಬಯಸದಿದ್ದರೆ, ಎರಡು వ్యాఖ్య ಚಿಹ್ನೆಗಳನ್ನು ತೆರವು ಮಾಡಿ ಮತ್ತು ತೋರಿಸಲು ಬಯಸದ ಯಾವುದೇ ಭಾಷೆಗಳನ್ನು ತೆಗೆದುಹಾಕಿ. ಚಿಹ್ನೆಗಳನ್ನು ತೆಗೆದುಹೊಂದಿದ ಮೇಲೆ, Co-op Translator ಈ ವಿಭಾಗವನ್ನು ಸ್ವಯಂಚಾಲಿತವಾಗಿ ಬದಲಾಯಿಸುವುದಿಲ್ಲ.

- ಈ ವಿಭಾಗದಲ್ಲಿ ಈಗ "ಸ್ಥಳೀಯವಾಗಿ ಕ್ಲೋನ್ ಮಾಡಬೇಕೆಂದು ಇಚ್ಛಿಸುವೀರಾ?" ಎಂಬ ಸಲಹೆ ಇದ್ದು, ಬಳಕೆದಾರರಿಗೂ ಭಾರಿ ಅನುವಾದ ಲೋಡ್ ಮಾಡದೆ ಕ್ಲೋನ್ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ. ನೀವು ನಿಮ್ಮ ಸಂಗ್ರಹಣಾ URL ನೊಂದಿಗೆ ಈ ಸಲಹೆಯನ್ನು ವೈಯಕ್ತೀಕರಿಸಬಹುದು ಉದಾಹರಣೆಗೆ:
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
**ತಪ್ಪುಮತಭ್ರಮೆ ನಿರಾಕರಣೆ**:  
ಈ ದಾಖಲೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಛಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಜ್ಞಾನಮಾಡಿಕೊಳ್ಳಿ. ಮೂಲ ದಾಖಲೆಯು ಅದರ ಮೂಲ ಭಾಷೆಯಲ್ಲಿ ಅಧಿಕೃತ ಮೂಲ ಎಂದು ಪರಿಗಣಿಸಬೇಕು. ಮಹತ್ವಪೂರ್ಣ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ಅರ್ಥಬೊಂದಿಕೆಗಳು ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆವಾರಿ ಹೊಂದಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->