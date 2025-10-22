<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T11:59:26+00:00",
  "source_file": "README.md",
  "language_code": "ne"
}
-->
# Co-op Translator

_आफ्नो शैक्षिक GitHub सामग्रीलाई सजिलै धेरै भाषामा अनुवाद गरेर विश्वभरका दर्शकसम्म पुर्याउनुहोस्।_

### 🌐 बहुभाषिक समर्थन

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारा समर्थित

[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

## संक्षिप्त परिचय

**Co-op Translator** ले तपाईंको शैक्षिक GitHub सामग्रीलाई छिटो धेरै भाषामा अनुवाद गर्न सहयोग गर्छ, जसले तपाईंलाई सजिलै विश्वभरका दर्शकसम्म पुग्न सकिन्छ। तपाईंले Markdown फाइल, तस्बिर वा Jupyter नोटबुक अपडेट गर्दा, अनुवादहरू स्वचालित रूपमा समक्रमण हुन्छन् ताकि तपाईंको शैक्षिक GitHub सामग्री अन्तर्राष्ट्रिय प्रयोगकर्ताहरूका लागि सधैं ताजा र सान्दर्भिक रहोस्।

Co-op Translator ले अनुवादित शैक्षिक GitHub सामग्रीलाई कसरी व्यवस्थित गर्छ हेर्नुहोस्:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.ne.png)

## छिटो सुरु गर्ने तरिका

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## न्यूनतम सेटअप

- `.env` फाइल बनाउनुहोस्: [.env.template](../../.env.template) को टेम्प्लेट प्रयोग गर्नुहोस्
- एउटा LLM प्रदायक (Azure OpenAI वा OpenAI) कन्फिगर गर्नुहोस्
- तस्बिर अनुवाद (`-img`) को लागि Azure AI Vision पनि सेट गर्नुहोस्
- सिफारिस: यदि तपाईंले अन्य उपकरणबाट अनुवादहरू बनाउनु भएको छ भने, पहिले सफा गर्नुहोस् (जस्तै: `translations/`) ताकि द्वन्द्व नहोस्।
- सिफारिस: आफ्नो README मा अनुवादहरूको सेक्सन थप्नुहोस् [README languages template](./README_languages_template.md) प्रयोग गरेर
- हेर्नुहोस्: [Azure AI सेटअप गर्नुहोस्](./getting_started/set-up-azure-ai.md)

## प्रयोग गर्ने तरिका

सबै समर्थित प्रकार अनुवाद गर्न:

```bash
translate -l "ko ja"
```

Markdown मात्र:

```bash
translate -l "de" -md
```

Markdown + तस्बिरहरू:

```bash
translate -l "pt" -md -img
```

नोटबुक मात्र:

```bash
translate -l "zh" -nb
```

थप विकल्पहरू: [Command reference](./getting_started/command-reference.md)

## विशेषताहरू

- Markdown, नोटबुक, र तस्बिरहरूको स्वचालित अनुवाद
- स्रोतमा परिवर्तन हुँदा अनुवादहरू समक्रमणमा राख्छ
- स्थानीय रूपमा (CLI) वा CI (GitHub Actions) मा काम गर्छ
- Azure OpenAI वा OpenAI प्रयोग गर्छ; तस्बिरका लागि वैकल्पिक Azure AI Vision
- Markdown को ढाँचा र संरचना जस्ताको तस्तै राख्छ

## दस्तावेजहरू

- [Command-line गाइड](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions गाइड (सार्वजनिक repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions गाइड (Microsoft संगठन repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [समर्थित भाषाहरू](./getting_started/supported-languages.md)
- [समस्या समाधान](./getting_started/troubleshooting.md)

## हामीलाई समर्थन गर्नुहोस् र विश्वव्यापी सिकाइलाई प्रोत्साहन दिनुहोस्

शैक्षिक सामग्री विश्वभर कसरी साझा गर्ने भन्ने कुरामा क्रान्ति ल्याउन हामीसँग जोडिनुहोस्! [Co-op Translator](https://github.com/azure/co-op-translator) लाई GitHub मा ⭐ दिनुहोस् र सिकाइ तथा प्रविधिमा भाषा बाधा हटाउने हाम्रो अभियानलाई समर्थन गर्नुहोस्। तपाईंको चासो र योगदानले ठूलो प्रभाव पार्छ! कोड योगदान र फिचर सुझावहरू सधैं स्वागत छ।

### आफ्नो भाषामा Microsoft शैक्षिक सामग्री अन्वेषण गर्नुहोस्

- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## भिडियो प्रस्तुतीकरणहरू

Co-op Translator को बारेमा थप जान्नका लागि हाम्रो प्रस्तुतीकरण हेर्नुहोस् _(तलको तस्बिरमा क्लिक गर्नुहोस् YouTube मा हेर्न)_:

- **Open at Microsoft**: Co-op Translator कसरी प्रयोग गर्ने भन्ने १८ मिनेटको छोटो परिचय र छिटो गाइड।

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.ne.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

यो परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्छ। Azure Co-op Translator मा योगदान गर्न इच्छुक हुनुहुन्छ? कृपया [CONTRIBUTING.md](./CONTRIBUTING.md) हेर्नुहोस्, जहाँ तपाईंले Co-op Translator लाई अझ पहुँचयोग्य बनाउन सहयोग गर्न सक्ने तरिका उल्लेख गरिएको छ।

## योगदानकर्ताहरू

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

यो परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ।
थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा
[opencode@microsoft.com](mailto:opencode@microsoft.com) मा थप प्रश्न वा टिप्पणी पठाउनुहोस्।

## जिम्मेवार AI

Microsoft ले आफ्ना ग्राहकहरूलाई AI उत्पादनहरू जिम्मेवारीपूर्वक प्रयोग गर्न सहयोग गर्ने, सिकाइहरू साझा गर्ने, र विश्वासमा आधारित साझेदारी बनाउने प्रतिबद्धता लिएको छ। Transparency Notes र Impact Assessments जस्ता उपकरणहरू मार्फत हामीले धेरै स्रोतहरू उपलब्ध गराएका छौं: [https://aka.ms/RAI](https://aka.ms/RAI)।
Microsoft को जिम्मेवार AI को दृष्टिकोण निष्पक्षता, विश्वसनीयता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशिता, पारदर्शिता, र उत्तरदायित्वका AI सिद्धान्तमा आधारित छ।

ठूलो स्तरका प्राकृतिक भाषा, तस्बिर, र आवाज मोडेलहरू - जस्तै यस नमुनामा प्रयोग गरिएका - कहिलेकाहीं अनुचित, अविश्वसनीय, वा आपत्तिजनक व्यवहार गर्न सक्छन्, जसले हानि पुर्याउन सक्छ। कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) हेर्नुहोस्, जोखिम र सीमाहरूको जानकारीका लागि।

यी जोखिमहरू कम गर्न सिफारिस गरिएको उपाय भनेको तपाईंको आर्किटेक्चरमा सुरक्षा प्रणाली समावेश गर्नु हो, जसले हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ले स्वतन्त्र सुरक्षा तह प्रदान गर्छ, जसले प्रयोगकर्ता-जनित र AI-जनित हानिकारक सामग्री पत्ता लगाउन सक्छ। Azure AI Content Safety मा पाठ र तस्बिर API छन्, जसले हानिकारक सामग्री पत्ता लगाउन सहयोग गर्छ। हामीसँग Interactive Content Safety Studio पनि छ, जहाँ तपाईंले विभिन्न modality मा हानिकारक सामग्री पत्ता लगाउने नमुना कोड हेर्न, अन्वेषण गर्न र प्रयास गर्न सक्नुहुन्छ। तलको [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ले सेवा अनुरोध गर्ने तरिका देखाउँछ।
अर्को ध्यान दिनुपर्ने पक्ष भनेको सम्पूर्ण एप्लिकेशनको प्रदर्शन हो। बहु-मोडल र बहु-मोडल एप्लिकेशनहरूमा, प्रदर्शन भन्नाले तपाईं र तपाईंका प्रयोगकर्ताहरूले अपेक्षा गरेअनुसार प्रणालीले काम गर्छ भन्ने बुझिन्छ, जसमा हानिकारक नतिजा नआउनु पनि समावेश छ। तपाईंको सम्पूर्ण एप्लिकेशनको प्रदर्शन मूल्याङ्कन गर्न [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गर्नु महत्त्वपूर्ण छ।

तपाईं आफ्नो विकास वातावरणमा [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरेर आफ्नो AI एप्लिकेशन मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डाटासेट वा लक्षित डाटा दिइएको अवस्थामा, तपाईंको जेनेरेटिभ AI एप्लिकेशनका नतिजाहरूलाई बिल्ट-इन इभालुएटर वा तपाईंले रोजेको कस्टम इभालुएटरमार्फत मात्रात्मक रूपमा मापन गरिन्छ। आफ्नो प्रणाली मूल्याङ्कन गर्न prompt flow sdk सुरु गर्नका लागि [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरण गर्न सक्नुहुन्छ। एकपटक मूल्याङ्कन रन सञ्चालन गरेपछि, तपाईं [Azure AI Studio मा नतिजा हेर्न सक्नुहुन्छ](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)।

## ट्रेडमार्कहरू

यो परियोजनामा परियोजना, उत्पादन, वा सेवाका लागि ट्रेडमार्क वा लोगोहरू समावेश हुन सक्छन्। Microsoft ट्रेडमार्क वा लोगोको अधिकृत प्रयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) अनुसार हुनुपर्छ। यस परियोजनाको परिमार्जित संस्करणमा Microsoft ट्रेडमार्क वा लोगो प्रयोग गर्दा भ्रम सिर्जना हुनु हुँदैन वा Microsoft को प्रायोजन भएको देखाउनु हुँदैन। तेस्रो पक्षका ट्रेडमार्क वा लोगोको प्रयोग तिनीहरूको नीति अनुसार हुनुपर्छ।

## सहयोग प्राप्त गर्ने तरिका

यदि तपाईं अड्किनु भयो वा AI एप्लिकेशन बनाउने क्रममा कुनै प्रश्न छ भने, सहभागी हुनुहोस्:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

यदि तपाईंलाई उत्पादन सम्बन्धी प्रतिक्रिया दिनु छ वा निर्माण गर्दा त्रुटि आयो भने, जानुहोस्:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेज़लाई नै अधिकारिक स्रोत मान्नुपर्छ। महत्वपूर्ण जानकारीको लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।