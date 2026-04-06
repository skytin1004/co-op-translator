# "इतर अभ्यासक्रम" विभाग अद्यतनित करा (Microsoft Beginners रिपॉजिटरीज)

हा मार्गदर्शक कसा "इतर अभ्यासक्रम" विभाग स्वयंचलितपणे Co-op Translator वापरून समक्रमित करायचा, आणि सर्व रिपॉजिटरीजसाठी ग्लोबल टेम्प्लेट कसा अद्यतनित करायचा हे स्पष्ट करतो.

- लागू: फक्त Microsoft Beginners रिपॉजिटरीजसाठी
- काम करते: Co-op Translator CLI आणि GitHub Actions सह
- टेम्प्लेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## जलद प्रारंभ: आपल्या रिपॉमध्ये ऑटो-सिंक सक्षम करा

README मध्ये "इतर अभ्यासक्रम" विभागाच्या भोवती खालील मार्कर्स जोडा. Co-op Translator प्रत्येक रनवर या मार्कर्समधील सर्वकाही बदलेल.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रत्येक वेळी Co-op Translator रन होतो—CLI द्वारे (उदा., `translate -l "<language codes>"`) किंवा GitHub Actions द्वारे—ते स्वयंचलितपणे या मार्कर्समध्ये असलेला "इतर अभ्यासक्रम" विभाग अद्यतनित करतो.

> [!NOTE]
> तुमच्याकडे आधीपासून सूची असल्यास, ती फक्त त्याच मार्कर्सने वेढा. पुढील रनमध्ये ती नवीनतम मानकीकृत सामग्रीने बदलली जाईल.

---

## ग्लोबल सामग्री कशी बदलायची

जर तुम्हाला सर्व Beginners रिपॉजिटरीजमध्ये दिसणारी मानकीकृत सामग्री अद्यतनित करायची असेल:

1. टेम्प्लेट संपादित करा: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Co-op Translator रिपोमध्ये आपल्या बदलांसह pull request उघडा
3. PR मर्ज झाल्यानंतर, Co-op Translator ची आवृत्ती अद्यतनित होईल
4. पुढच्या वेळी Co-op Translator (CLI किंवा GitHub Action) लक्ष्यित रिपोमध्ये रन होईल, तेव्हा अद्ययावत विभाग स्वयंचलितपणे सिंक्रनाइझ होईल

हे सुनिश्चित करते की सर्व Beginners रिपॉजिटरीजमधील "इतर अभ्यासक्रम" सामग्रीसाठी एकच सत्य स्रोत असेल.

## रिपॉ आकार 

रिपोज अनेक भाषांमध्ये अनुवादित केल्यामुळे मोठे होऊ शकतात, जे अंतिम वापरकर्त्यांना मार्गदर्शन करण्यासाठी आहेत की फक्त आवश्यक भाषा क्लोन कशा वापरायच्या आणि संपूर्ण रिपो नव्हे, म्हणून clone - sparse चा उपयोग करा.

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
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून भाषांतरित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील आहोत, तरी कृपया लक्षात ठेवा की स्वयंचलित भाषांतरांमध्ये चुका किंवा गैरशुद्धता असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत मानला जाणे आवश्यक आहे. महत्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुतींसाठी किंवा चुकीच्या अर्थ लावण्यांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->