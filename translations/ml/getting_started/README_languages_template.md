# 🌐 ബഹുഭാഷാ പിന്തുണ (ടെംപ്ലേറ്റ്)

പരിപാലകർ: താഴെയുള്ള ബ്ലോക്ക് Co-op Translator দ্বারা മാനേജുചെയ്‌ത "എല്ലാ ഭാഷകളും" ഉദാഹരണമാണ്.

- നിങ്ങൾ Co-op Translator-ന് `translate` (ഏതെങ്കിലും ഭാഷാ തിരഞ്ഞെടുപ്പ്) ഓടിക്കുമ്പോൾ ഈ ലിസ്റ്റ് പൂർണ്ണമായി സ്വയം അപ്പ്‌ഡേറ്റ് ചെയ്യാൻ ആഗ്രഹിക്കുന്ന പക്ഷം, രണ്ട് കമന്റ് മാർക്കർമാരെ അതിന്റെ നിലവിലായിരിക്കുന്ന പോലെ ആണ്‌ നിലനിർത്തേണ്ടത്.
- നിങ്ങൾക്ക് ചില ഭാഷകളുടെ ഉപസമൂഹം മാത്രം കാണിക്കണമെന്ന് ആഗ്രഹിക്കുന്ന പക്ഷം, രണ്ട് കമന്റ് മാർക്കർമാരെ ഇല്ലാതാക്കി നിങ്ങൾ കാണിക്കാൻ ആഗ്രഹിക്കുന്നില്ലാത്ത ഏതെങ്കിലും ഭാഷകൾ ഒഴിവാക്കുക. മാർക്കർമാരെ പിന്‍വലിച്ചശേഷം Co-op Translator ഈ സെക്ഷനെ ഓട്ടോ-റിപ്ലേസ് ചെയ്യുന്നതില്ല.

- ഇപ്പോഴുള്ള സെക്ഷനിൽ "പ്രാദേശികമായി ക്ലോൺ ചെയ്യുന്നത_prefer_ ചെയ്യാമോ?" എന്ന ഉപദേശം ഉൾപ്പെടുത്തിയിട്ടുണ്ട്, ഇത് വൻപരിഭാഷാ പേലോഡുകൾ ഇല്ലാത്തതുകൊണ്ട് ഉപയോക്താക്കളെ സഹായിക്കുന്നു. നിങ്ങളുടെ റിപ്പോസിറ്ററി URL ഉപയോഗിച്ച് ഉപദേശം വ്യക്തിഗതമാക്കാൻ, ഉദാഹരണത്തിന് ചുവടെയുള്ള കമാൻഡ് ഓടിക്കാം:
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
**തള്ളിവేయൽ**:  
ഈ രേഖ AI തർജ്ജുമാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജമ ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, യാന്ത്രിക തർജ്ജുമകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റായ വിവരങ്ങൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. ഇതിന്റെ മാതൃഭാഷയിലെ യഥാർത്ഥ രേഖ തന്നെയാണ് സമർപ്പണമായ ഉറവിടം എന്ന് കണക്കാക്കേണ്ടത്. പ്രധാനപ്പെട്ട വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മാനുഷിക തർജ്ജുമ നിർദ്ദേശിക്കുന്നു. ഈ തർജ്ജുമ ഉപയോഗിച്ച് ഉണ്ടാകുന്ന യാതൊരു തെറ്റിദ്ധാരണയ്ക്ക് ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->