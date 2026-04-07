# "अन्य पाठ्यक्रम" अनुभाग अपडेट करें (Microsoft Beginners रिपॉज़िटरी)

यह गाइड बताता है कि Co‑op Translator का उपयोग करके "अन्य पाठ्यक्रम" अनुभाग को स्वचालित रूप से सिंक कैसे करें, और सभी रिपॉज़िटरीज़ के लिए वैश्विक टेम्पलेट कैसे अपडेट करें।

- लागू होता है: केवल Microsoft Beginners रिपॉज़िटरीज़ पर
- काम करता है: Co‑op Translator CLI और GitHub Actions के साथ
- टेम्पलेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## त्वरित प्रारंभ: अपने रिपॉ में ऑटो-सिंक सक्षम करें

अपने README में "अन्य पाठ्यक्रम" अनुभाग के चारों ओर निम्न मार्कर जोड़ें। Co‑op Translator हर रन पर इन मार्करों के बीच की सभी सामग्री को बदल देगा।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

हर बार जब Co‑op Translator चलता है—CLI के माध्यम से (जैसे, `translate -l "<language codes>"`) या GitHub Actions के जरिए—यह स्वचालित रूप से इन मार्करों से घिरे "अन्य पाठ्यक्रम" अनुभाग को अपडेट करता है।

> [!NOTE]
> यदि आपके पास मौजूदा सूची है, तो बस उसे समान मार्करों के साथ घेर लें। अगली बार चलाने पर इसे नवीनतम मानकीकृत सामग्री के साथ बदल दिया जाएगा।

---

## वैश्विक सामग्री कैसे बदलें

यदि आप सभी Beginners रिपॉज़िटरीज़ में दिखने वाली मानकीकृत सामग्री को अपडेट करना चाहते हैं:

1. टेम्पलेट संपादित करें: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. अपने बदलावों के साथ Co-op Translator रिपॉज़िटरी में एक pull request खोलें
3. PR मर्ज हो जाने के बाद, Co‑op Translator संस्करण अपडेट हो जाएगा
4. अगली बार जब Co‑op Translator (CLI या GitHub Action) किसी लक्ष्य रिपॉ में चलेगा, यह अपडेट किए गए अनुभाग को स्वचालित रूप से सिंक करेगा

यह सुनिश्चित करता है कि सभी Beginners रिपॉज़िटरीज़ में "अन्य पाठ्यक्रम" सामग्री के लिए एक ही सत्य स्रोत मौजूद हो।

## रिपॉ आकार

भाषाओं की संख्या के कारण रिपॉज़िटरीज़ बड़ी हो सकती हैं जिन्हें अनुवादित किया गया है ताकि अंतिम उपयोगकर्ता को आवश्यक भाषाओं को क्लोन करने के लिए clone - sparse का उपयोग कैसे करें और पूरी रिपॉज़िटरी न क्लोन करें, इसके लिए मार्गदर्शन प्रदान किया जा सके

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
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में दस्तावेज़ को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या अन्य व्याख्याओं के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->