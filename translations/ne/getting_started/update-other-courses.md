# "अन्य कोर्सहरू" सेक्सन अपडेट गर्नुहोस् (Microsoft Beginners रिपोजिटोरीहरू)

यस मार्गदर्शिकाले Co‑op Translator प्रयोग गरेर "अन्य कोर्सहरू" सेक्सन कसरी अटो‑सिंक गर्न सकिन्छ र सबै रिपोजिटोरीहरूको लागि ग्लोबल टेम्प्लेट कसरी अपडेट गर्ने भन्ने व्याख्या गर्दछ।

- लागू हुने: Microsoft Beginners रिपोजिटोरीहरू मात्र
- काम गर्ने: Co‑op Translator CLI र GitHub Actions सँग
- टेम्पलेट स्रोत: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## छिटो सुरूवात: तपाइँको रिपोमा अटो-सिंक सक्षम गर्नुहोस्

तपाइँको README मा "अन्य कोर्सहरू" सेक्सन वरिपरि तलका मार्करहरू थप्नुहोस्। Co‑op Translator ले प्रत्येक रनमा यी मार्करहरू बीचको सबै कुरा प्रतिस्थापन गर्नेछ।

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

हरेक पटक Co‑op Translator चल्दा—CLI मार्फत (उदा., `translate -l "<language codes>"`) वा GitHub Actions द्वारा—यसले स्वतः यी मार्करहरूले घेरेको "अन्य कोर्सहरू" सेक्सन अपडेट गर्दछ।

> [!NOTE]
> यदि तपाइँसँग पहिले देखि सूची छ भने, त्यसलाई पनि ती मार्करहरूसँग घेरिदिनुहोस्। अर्को रनले यसलाई नवीनतम मानकीकृत सामग्रीले प्रतिस्थापन गर्नेछ।

---

## ग्लोबल सामग्री कसरी परिवर्तन गर्ने

यदि तपाइँ सबै Beginners रिपोजिटोरीहरूमा देखिने मानकीकृत सामग्री अपडेट गर्न चाहनुहुन्छ भने:

1. टेम्पलेट सम्पादन गर्नुहोस्: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. तपाइँका परिवर्तनहरूसहित Co-op Translator रिपोमा pull request खोल्नुहोस्
3. PR मर्ज भएपछि, Co‑op Translator को भर्सन अपडेट हुनेछ
4. अर्को पटक Co‑op Translator (CLI वा GitHub Action) लक्षित रिपोमा चल्दा, यसले स्वतः अपडेट गरिएको सेक्सन सिंक गर्नेछ

यसले सबै Beginners रिपोजिटोरीहरूमा "अन्य कोर्सहरू" सामग्रीको लागि एकल सत्य स्रोत सुनिश्चित गर्छ।

## रिपो साइज़हरू

धेरै भाषामा अनुवाद गर्दा रिपोहरू ठूलो हुन सक्छन् जसले अन्तिम प्रयोगकर्तालाई मार्गदर्शन दिन्छ कि केवल आवश्यक भाषाहरू मात्र क्लोन गर्न कुन तरीकाले clone - sparse प्रयोग गर्ने र सम्पूर्ण रिपो क्लोन नगर्ने।

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
यस दस्तावेजलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा आधिकारिक स्रोतको रूपमा मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलत बुझाइ वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->