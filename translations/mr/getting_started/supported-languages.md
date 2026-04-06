# Supported languages

खालील तक्त्यामध्ये सध्या **Co-op Translator** द्वारे समर्थित भाषा सूचीबद्ध आहेत. यात भाषा कोड, भाषा नावे, आणि प्रत्येक भाषेशी संबंधित ज्ञात समस्या समाविष्ट आहेत. आपण नवीन भाषेसाठी समर्थन जोडू इच्छित असल्यास, कृपया `src/co_op_translator/fonts/` मध्ये असलेल्या `font_language_mappings.yml` फाईलमध्ये संबंधित भाषा कोड, नाव, आणि योग्य फॉन्ट जोडा आणि टेस्टिंगनंतर pull request सबमिट करा.

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

## Adding a new language

नवीन भाषा जोडण्यास इच्छुक आहात? कृपया योगदान मार्गदर्शकाचे पालन करा:

- पाहा Contributing: [Contribute a new language](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज एआय भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला गेला आहे. जरी आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या मूळ भाषेत प्राधिकृत स्रोत मानला जातो. महत्त्वाच्या माहितीकरिता, व्यावसायिक मानवी भाषांतर शिफारस केले जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थनिर्देशांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->