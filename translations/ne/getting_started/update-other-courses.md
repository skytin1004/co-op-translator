# "अर्का कोर्सहरू" खण्ड अपडेट गर्नुहोस् (Microsoft Beginners रिपोजिटोरीहरू)

यो मार्गदर्शनले Co‑op Translator को प्रयोग गरेर "अर्का कोर्सहरू" खण्ड कसरी अटो-सिंक्रोनाइज गर्दा र सबै रिपोजिटोरीहरूको लागि ग्लोबल टेम्प्लेट कसरी अपडेट गर्ने बारे व्याख्या गर्दछ।

- लागू हुने: Microsoft Beginners रिपोजिटोरीहरू मात्र
- काम गर्ने: Co‑op Translator CLI र GitHub Actions सँग
- टेम्प्लेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## छिटो सुरु: तपाईंको रिपोमा अटो-सिंक सक्षम पार्नुहोस्

तपाईंको README मा "अर्का कोर्सहरू" खण्ड वरिपरि तलका मार्करहरू थप्नुहोस्। Co‑op Translator प्रत्येक रनमा यी मार्करहरूले घेरिएको सबै कुरा प्रतिस्थापन गर्नेछ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

प्रत्येक पटक Co‑op Translator चलाउँदा—CLI मार्फत (जस्तै, `translate -l "<language codes>"`) वा GitHub Actions मार्फत—यो स्वतः यी मार्करहरूले घेरिएको "अर्का कोर्सहरू" खण्ड अपडेट गर्नेछ।

> [!NOTE]
> यदि तपाईंसँग पहिलेदेखि सूचि छ भने, त्यसलाई एउटै मार्करहरूसँग मात्र घेरिदिनुहोस्। अर्को रनले यसलाई नयाँ मानकीकृत सामग्रीले प्रतिस्थापन गर्नेछ।

---

## ग्लोबल सामग्री कसरी परिवर्तन गर्ने

यदि तपाईँ सबै Beginners रिपोजहरूमा देखिने मानकीकृत सामग्री अपडेट गर्न चाहनुहुन्छ भने:

1. टेम्प्लेट सम्पादन गर्नुहोस्: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. तपाईँका परिवर्तनहरू सहित Co-op Translator रिपोमा pull request खोल्नुहोस्
3. PR मर्ज भएपछि Co‑op Translator संस्करण अपडेट हुनेछ
4. अर्को पटक Co‑op Translator चल्दा (CLI वा GitHub Action मार्फत) लक्ष्य रिपोमा यो अपडेट गरिएको खण्ड स्वचालित रूपमा सिंक हुनेछ

यसले सबै Beginners रिपोजिटोरीहरूमा "अर्का कोर्सहरू" सामग्रीको लागि एकल सत्य स्रोत सुनिश्चित गर्दछ।

## रिपो साइजहरू

अनुवाद गरिएको भाषाको सङ्ख्या धेरै हुँदा रिपो ठूलो हुन सक्छ जसले अन्तिम प्रयोगकर्ताहरूलाई आवश्यक भाषाहरू मात्र क्लोन गर्न र सम्पूर्ण रिपो क्लोन नगर्न 'clone - sparse' प्रयोग गर्ने सुझाव प्रदान गर्न सहयोग पुर्‍याउँछ।

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
यस कागजातलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत भए तापनि, कृपया जानकार हुनुस् कि स्वत: अनुवादमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल कागजात यसको मातृभाषामा नै प्रामाणिक स्रोत मानिनुपर्छ। महत्वपूर्ण सूचनाका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्यासँग हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->