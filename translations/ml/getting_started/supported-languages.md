# പിന്തുണയുള്ള ഭാഷകൾ

താഴെക്കൊടുത്തിട്ടുള്ള പട്ടികയിൽ **Co-op Translator** പിന്തുണയുള്ള നിലവിലുള്ള ഭാഷകൾ ഉൾപ്പെടുത്തിയിട്ടുണ്ട്. ഇതിൽ ഭാഷാ കോഡുകൾ, ഭാഷാ പേരുകൾ, ഓരോ ഭാഷയുമായി ബന്ധപ്പെട്ട അറിയപ്പെട്ട പ്രശ്നങ്ങൾ ഉൾപ്പെടുന്നു. പുതിയ ഒരു ഭാഷയുടെ പിന്തുണ ചേർക്കാൻ താൽപര്യമുണ്ടെങ്കിൽ, ദയവായി അനുയോജ്യമായ ഭാഷാ കോഡ്, പേര്, ഫോണ്ട് എല്ലാമായി `src/co_op_translator/fonts/` ലെ `font_language_mappings.yml` ഫയലിൽ ചേർത്ത് പരീക്ഷണത്തിന് ശേഷം ഒരു pull request സമർപ്പിക്കുക.

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | English              | NotoSans-Medium.ttf               | No          | No           |
| fr            | French               | NotoSans-Medium.ttf               | No          | No           |
| es            | Spanish              | NotoSans-Medium.ttf               | No          | No           |
| de            | German               | NotoSans-Medium.ttf               | No          | No           |
| ru            | Russian              | NotoSans-Medium.ttf               | No          | No           |
| ar            | Arabic               | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | Persian (Farsi)      | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | Urdu                 | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh-CN         | Chinese (Simplified) | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-MO         | Chinese (Traditional, Macau) | NotoSansCJK-Medium.ttc    | No          | No           |
| zh-HK         | Chinese (Traditional, Hong Kong) | NotoSansCJK-Medium.ttc| No          | No           |
| zh-TW         | Chinese (Traditional, Taiwan) | NotoSansCJK-Medium.ttc   | No          | No           |
| ja            | Japanese             | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | Korean               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | Hindi                | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | Bengali              | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | Marathi              | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | Nepali               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | Punjabi (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt-PT         | Portuguese (Portugal)| NotoSans-Medium.ttf               | No          | No           |
| pt-BR         | Portuguese (Brazil)  | NotoSans-Medium.ttf               | No          | No           |
| it            | Italian              | NotoSans-Medium.ttf               | No          | No           |
| lt            | Lithuanian           | NotoSans-Medium.ttf               | No          | No           |
| pl            | Polish               | NotoSans-Medium.ttf               | No          | No           |
| tr            | Turkish              | NotoSans-Medium.ttf               | No          | No           |
| el            | Greek                | NotoSans-Medium.ttf               | No          | No           |
| th            | Thai                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | Swedish              | NotoSans-Medium.ttf               | No          | No           |
| da            | Danish               | NotoSans-Medium.ttf               | No          | No           |
| no            | Norwegian            | NotoSans-Medium.ttf               | No          | No           |
| fi            | Finnish              | NotoSans-Medium.ttf               | No          | No           |
| nl            | Dutch                | NotoSans-Medium.ttf               | No          | No           |
| he            | Hebrew               | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | Vietnamese           | NotoSans-Medium.ttf               | No          | No           |
| id            | Indonesian           | NotoSans-Medium.ttf               | No          | No           |
| ms            | Malay                | NotoSans-Medium.ttf               | No          | No           |
| tl            | Tagalog (Filipino)   | NotoSans-Medium.ttf               | No          | No           |
| sw            | Swahili              | NotoSans-Medium.ttf               | No          | No           |
| hu            | Hungarian            | NotoSans-Medium.ttf               | No          | No           |
| cs            | Czech                | NotoSans-Medium.ttf               | No          | No           |
| sk            | Slovak               | NotoSans-Medium.ttf               | No          | No           |
| ro            | Romanian             | NotoSans-Medium.ttf               | No          | No           |
| bg            | Bulgarian            | NotoSans-Medium.ttf               | No          | No           |
| sr            | Serbian (Cyrillic)   | NotoSans-Medium.ttf               | No          | No           |
| hr            | Croatian             | NotoSans-Medium.ttf               | No          | No           |
| sl            | Slovenian            | NotoSans-Medium.ttf               | No          | No           |
| uk            | Ukrainian            | NotoSans-Medium.ttf               | No          | No           |
| my            | Burmese (Myanmar)    | NotoSansMyanmar-Medium.ttf        | No          | No           |
| ta            | Tamil                | NotoSansTamil-Medium.ttf          | No          | No           |
| et            | Estonian             | NotoSans-Medium.ttf               | No          | No           |
| pcm           | Nigerian Pidgin      | NotoSans-Medium.ttf               | No          | No           |
| te            | Telugu               | NotoSans-Medium.ttf               | No          | No           |
| ml            | Malayalam            | NotoSans-Medium.ttf               | No          | No           |
| kn            | Kannada              | NotoSans-Medium.ttf               | No          | No           |
| km            | Khmer                | NotoSansKhmer-Medium.ttf          | No          | No           |

## ഒരു പുതിയ ഭാഷ ചേർക്കൽ

പുതിയ ഒരു ഭാഷ ഉൾപ്പെടുത്താൻ താൽപര്യമുണ്ടോ? ദയവായി സംഭാവന മാർഗ്ഗനിർദേശത്തിന്റെ പിന്തുടരുക:

- Contributing പരിശോധിക്കുക: [Contribute a new language](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**പ്രതിജ്ഞ**:  
ഈ ഡോക്യുമെന്റ് AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. ഞങ്ങൾ നിഷ്‌ഠയോടെ ശുദ്ധതയ്ക്ക് ശ്രമിക്കുമ്പോഴും, യന്ത്രം നിർവ്വഹിക്കുന്ന വിവർത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അസംഘടിതത്വങ്ങൾ ഉണ്ടാകുമെന്ന കാര്യം ദയവായി അവഗണിക്കരുത്. സ്വഭാവഭാഷയിലുള്ള മൗലിക ഡോക്യുമെന്റ് ആണ് പ്രമാണമായ ഉറവിടം എന്നായി കരുതേണ്ടത്. നിർണ്ണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം നിർദ്ദേശിക്കുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന എന്തെങ്കിലും തിരിച്ചറിവിലോ തെറ്റായ വ്യാഖ്യാനത്തിലോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->