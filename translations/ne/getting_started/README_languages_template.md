# 🌐 बहुभाषी समर्थन (टेम्प्लेट)

रखवारी गर्नेहरू: तलको ब्लक "सबै भाषाहरू" को उदाहरण हो जुन Co-op Translator द्वारा व्यवस्थापन गरिन्छ।

- यदि तपाईं `translate` चलाउँदा (कुनैपनि भाषा चयन गर्दा) Co-op Translator ले यो सूची पूर्ण रूपमा स्वचालित रूपमा अद्यावधिक राख्न चाहनुहुन्छ भने, दुई टिप्पणी मार्करहरू यथावत राख्नुहोस्।
- यदि तपाईं केवल केही भाषाहरूको उपसमूह मात्र देखाउन चाहनुहुन्छ भने, दुई टिप्पणी मार्करहरू मेटाउनुहोस् र जुन भाषाहरू सूचीमा देखाउन चाहनुहुन्न ती मेटाउनुहोस्। मार्करहरू मेटाएपछि Co-op Translator यस खण्डलाई फेरि स्वचालित रूपमा प्रतिस्थापन गरिनेछैन।

- अब यस खण्डमा "स्थानीय रूपमा क्लोन गर्न मन लाग्छ?" सल्लाह पनि समावेश गरिएको छ जसले प्रयोगकर्ताहरूलाई ठूलो अनुवाद लोड बिना क्लोन गर्न मद्दत गर्दछ। तपाईं आफ्नो रिपोजिटरी URL सँग सल्लाहलाई वैयक्तिकृत गर्न सक्नुहुन्छ, उदाहरणका लागि:
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
यो कागजातलाई AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको छ। हामी शुद्धताका लागि प्रयासरत छौं, तर कृत्रिम अनुवादमा त्रुटि वा अन्योल हुन सक्ने कुरा कृपया ध्यान दिनुहोस्। मूल कागजातलाई यसको मातृभाषामा नै आधिकारिक स्रोतको रूपमा मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिश गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि भ्रम वा गलतफहमीका लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->