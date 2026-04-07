# 🌐 ബഹുഭാഷാ പിന്തുണ (ട്രെംപ്ലേറ്റ്)

സംരക്ഷകരെ: താഴെ കാണുന്ന ബ്ലോക്ക് Co-op Translator മുഖാന്തിരം നിയന്ത്രിക്കുന്ന "എല്ലാ ഭാഷകളും" ഉദാഹരണമാണ്.

- നിങ്ങൾ `translate` (ഏതെങ്കിലും ഭാഷ തിരഞ്ഞെടുപ്പ്) പ്രവർത്തിപ്പിക്കുമ്പോൾ Co-op Translator ഈ പട്ടിക സജീവമായി ഏറ്റവും പുതിയതാക്കാൻ ആഗ്രഹിക്കുന്നുവെങ്കിൽ, രണ്ടു കമന്റ് മാർക്കറുകളും അതേതായി വയ്ക്കുക.
- നിങ്ങൾ ഒരു കുറച്ചുപLanguage subset മാത്രം കാണിക്കാനാഗ്രഹിക്കുന്നുവെങ്കിൽ, കമന്റ് മാർക്കറുകൾ ഉപേക്ഷിച്ച് നിങ്ങൾ കാണിക്കാൻ ആഗ്രഹിക്കാത്ത മറ്റു ഭാഷകളും നീക്കം ചെയ്യുക. മാർക്കറുകൾ നീക്കം ചെയ്ത ശേഷം Co-op Translator ഈ വിഭാഗം സ്വയം പകരാനില്ല.

- ഈ വിഭാഗത്തിൽ ഇപ്പോൾ ഒരു "സഹജമായി പ്രാദേശികമായി ക്ലോൺ ചെയ്യാമോ?" ഉപദേശം ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, ഇത് ഉപയോക്താക്കളെ വലിയ വചനങ്ങൾ അടങ്ങിയ പായ്ലോഡ് ഇല്ലാതെ ക്ലോൺ ചെയ്യാൻ സഹായിക്കുന്നു. നിങ്ങളുടെ റിപ്പോസിറ്ററി URL-ഉം ഉൾപ്പെടുത്താൻ, ഉദാഹരണത്തിന് താഴെയുള്ള കമാൻഡ് പ്രവർത്തിപ്പിക്കാം:
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
**അുറപ്പിച്ചറിയിപ്പ്**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്യപ്പെട്ടതാണ്. ഞങ്ങൾ നിഷ്‌ഠയോടെ ശരിയായ വിവർത്തനത്തിനായി പരിശ്രമിക്കുന്നുവെങ്കിലും, യന്ത്രവത്കൃത വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ കൃത്യതയിൽ ചുരുക്കങ്ങൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. ഉറവിട ഭാഷയിലെ ആദിത്യ രേഖ മാത്രമാണ് സർവോപരി പ്രാമാണികമായ ഉറവിടം. നിർണായക വിവരംക്കായി, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിച്ചതിൽ നിന്ന് ഉണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കും പറയുന്നു തെറ്റിദ്ധാരണകൾക്കും ഞങ്ങൾ യാതൊരു ഉത്തരവാദിത്വവും ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->