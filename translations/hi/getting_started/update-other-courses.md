# "अन्य पाठ्यक्रम" अनुभाग अपडेट करें (Microsoft Beginners रिपोज़)

यह मार्गदर्शिका समझाती है कि Co‑op Translator का उपयोग करके "अन्य पाठ्यक्रम" अनुभाग को स्वचालित रूप से सिंक कैसे करें, और सभी रिपोज़ के लिए वैश्विक टेम्पलेट को कैसे अपडेट करें।

- लागू होता है: केवल Microsoft Beginners रिपोज़िटरीज़ पर
- काम करता है: Co‑op Translator CLI और GitHub Actions के साथ
- टेम्पलेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## त्वरित शुरुआत: अपने रिपो में ऑटो‑सिंक सक्षम करें

README के "अन्य पाठ्यक्रम" अनुभाग के चारों ओर निम्नलिखित मार्कर जोड़ें। Co‑op Translator हर रन पर इन मार्करों के बीच की सभी चीज़ों को बदल देगा।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

जब भी Co‑op Translator चलाया जाता है—CLI के माध्यम से (जैसे, `translate -l "<language codes>"`) या GitHub Actions के द्वारा—तो यह स्वतः ही इन मार्करों से घिरे "अन्य पाठ्यक्रम" अनुभाग को अपडेट कर देता है।

> [!NOTE]
> यदि आपके पास पहले से कोई सूची है, तो बस उसे उन्हीं मार्करों के साथ घेर दें। अगला रन इसे नवीनतम मानकीकृत सामग्री से बदल देगा।

---

## वैश्विक सामग्री कैसे बदलें

यदि आप सभी Beginners रिपोज़ में दिखाई देने वाली मानकीकृत सामग्री को अपडेट करना चाहते हैं:

1. टेम्पलेट संपादित करें: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. अपने परिवर्तनों के साथ Co-op Translator रिपो में एक pull request खोलें
3. PR मर्ज होने के बाद, Co‑op Translator संस्करण अपडेट हो जाएगा
4. अगली बार जब Co‑op Translator (CLI या GitHub Action के माध्यम से) एक लक्षित रिपो में चलेगा, तो यह अपडेट किए गए अनुभाग को स्वतः सिंक करेगा

यह सभी Beginners रिपोज़िटरीज में "अन्य पाठ्यक्रम" सामग्री के लिए एकमात्र सत्य स्रोत सुनिश्चित करता है।

## रिपो आकार

अनुवादित भाषाओं की संख्या के कारण रिपोज़ बड़ा हो सकता है ताकि अंतिम उपयोगकर्ताओं को केवल आवश्यक भाषाओं को क्लोन करने और पूरे रिपो को नहीं, इसके लिए क्लोन - sparse का उपयोग करने के लिए मार्गदर्शन प्रदान किया जा सके

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
यह दस्तावेज़ [Co-op Translator](https://github.com/Azure/co-op-translator) नामक एआई अनुवाद सेवा का उपयोग करके अनूदित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान रखें कि स्वचालित अनुवादों में त्रुटियां या गलतियां हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में अधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->