# "इतर कोर्सेस" विभाग अद्यतनित करा (Microsoft Beginners रेपॉजिटरीज)

हा मार्गदर्शक Co‑op Translator वापरून "इतर कोर्सेस" विभाग स्वयंचलित समक्रमण कसा करावा आणि सर्व रेपॉजिटरीजसाठी जागतिक टेम्प्लेट कसा अद्यतनित करावा हे स्पष्ट करतो.

- लागू आहे: केवळ Microsoft Beginners रेपॉजिटरीजसाठी
- कार्य करते: Co‑op Translator CLI आणि GitHub Actions सह
- टेम्प्लेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## जलद प्रारंभ: आपल्या रेपॉमध्ये ऑटो‑सिंक सक्षम करा

आपल्या README मध्ये "इतर कोर्सेस" विभागाभोवती खालील मार्कर्स जोडा. Co‑op Translator प्रत्येक वेळी या मार्कर्समधील सर्व काही बदलेल.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रत्येक वेळी जेव्हा Co‑op Translator चालतो—CLI (उदा., `translate -l "<language codes>"`) किंवा GitHub Actions द्वारे—ते आपोआप या मार्कर्सद्वारे गुंडाळलेल्या "इतर कोर्सेस" विभागाचा अद्यतन करते.

> [!NOTE]
> जर तुमच्याकडे आधीच यादी असेल, तर फक्त तिला त्याच मार्कर्सने गुंडाळा. पुढील वेळी चालविल्यावर ते नवीनतम प्रमाणीकरण केलेल्या सामग्रीने बदलेल.

---

## जागतिक सामग्री कशी बदलावी

जर तुम्हाला सर्व Beginners रेपॉजिटरीजमध्ये दिसणारी प्रमाणीकरण केलेली सामग्री अद्यतनित करायची असेल:

1. टेम्प्लेट संपादित करा: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. आपल्या बदलांसह Co-op Translator रेपोपाशी एक pull request उघडा
3. PR मर्ज झाल्यानंतर, Co‑op Translator ची आवृत्ती अद्यतनित होईल
4. पुढील वेळी जेव्हा Co‑op Translator (CLI किंवा GitHub Action) लक्ष्य रेपोमध्ये चालेल, तेव्हा ते अद्यतनित विभाग स्वयंचलितपणे सिंक करेल

हे सर्व Beginners रेपॉजिटरीजसाठी "इतर कोर्सेस" सामग्रीचा एकच सत्य स्रोत कायम ठेवतो.


## रेपॉ आकार

रेपॉज भाषांतरित भाषा संख्येमुळे मोठे होऊ शकतात जेणेकरून अंतिम वापरकर्त्यांना मार्गदर्शन करण्यासाठी clone - sparse वापरून फक्त आवश्यक भाषा क्लोन करता येतील आणि संपूर्ण रेपो नाही.

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
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, तरी कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा दोष असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला पाहिजे. अत्यंत महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद शिफारस केला जातो. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा वाक्यप्रचारासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->