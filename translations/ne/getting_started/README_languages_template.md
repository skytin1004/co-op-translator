# 🌐 बहुभाषिक समर्थन (टेम्प्लेट)

रखरखाव गर्नेहरू: तलको ब्लक Co-op Translator द्वारा व्यवस्थापन गरिएको "सबै भाषा" को उदाहरण हो।

- यदि तपाईं `translate` चलाउँदा (कुनै पनि भाषा चयन) Co-op Translator लाई यो सूची पूर्ण रूपमा स्वचालित रूपमा अद्यावधिक गर्न चाहनुहुन्छ भने, दुई टिप्पणी मार्करहरू यथावत् राख्नुहोस्।
- यदि तपाईं केवल केही भाषाहरू मात्र देखाउन चाहनुहुन्छ भने, दुई टिप्पणी मार्करहरू हटाउनुहोस् र तपाइँले देखाउन नचाहने भाषाहरू हटाउनुहोस्। मार्करहरू हटाएपछि Co-op Translator यो खण्डलाई स्वतः प्रतिस्थापन राख्दैन।

- हालको खण्डमा प्रयोगकर्ताहरूलाई ठूला अनुवाद डेटा बिना क्लोन गर्न मद्दत गर्न "स्थानीय रूपमा क्लोन गर्न प्राथमिकता?" सल्लाह समावेश गरिएको छ। तपाईं आफ्नो रिपोजिटोरी URL प्रयोग गरेर यो सल्लाहलाई व्यक्तिगत बनाउन सक्नुहुन्छ, उदाहरणका लागि:
  - `translate -l "ko" --repo-url "https://github.com/org/repo.git"`

```markdown

### 🌐 Multi-Language Support

#### Supported by [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
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
**अस्वीकरण**:  
यो दस्तावेज़लाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी सही अनुवाद पस्किन प्रयास गर्छौं, तर कृपया अवगत हुनुहोस् कि स्वतः अनुवादमा त्रुटिहरू वा असत्यताहरू हुन सक्छन्। मूल दस्तावेज़ आफ्नो स्थानिय भाषामा आधिकारिक स्रोतको रूपमा मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौँ।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->