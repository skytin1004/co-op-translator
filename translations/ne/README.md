# Co-op Translator

_आफ्नो शैक्षिक GitHub सामग्रीलाई प्रोजेक्ट विकासक्रममा विभिन्न भाषाहरूमा सजिलै अनुवाद र मर्मतसम्भार गर्नुहोस्।_

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 बहुभाषी समर्थन

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारा समर्थन गरिएको

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](./README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानीय रूपमा क्लोन गर्न चाहनुहुन्छ?**
>
> यो रिपोजिटरीमा ५०+ भाषा अनुवादहरू समावेश भएका छन् जसले डाउनलोड साइज उल्लेखनीय रूपमा बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै कुरा धेरै छिटो डाउनलोडको साथ प्रदान गर्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** तपाईंलाई सजिलैसँग आफ्नो शैक्षिक GitHub सामग्रीलाई विभिन्न भाषाहरूमा लोकलाइज गर्न मद्दत गर्छ।  
जब तपाईंले Markdown फाइलहरू, इमेजहरू, वा नोटबुकहरू अपडेट गर्नुहुन्छ, अनुवादहरू स्वतः समक्रमित रहन्छन्, जसले विश्वभरिका विद्यार्थीहरूको लागि तपाईंको सामग्री सधैं सही र अपडेटेड रहन्छ।

अनुवादित सामग्री कसरी व्यवस्थित हुन्छ भन्ने उदाहरण:

![Example](../../translated_images/ne/translation-ex.0c8aa6a7ee0aad2b.webp)

## अनुवाद स्थिति कसरी व्यवस्थापन गरिन्छ

Co-op Translator अनुवादित सामग्रीलाई **संस्करणयुक्त सफ्टवेयर आर्टिफ्याक्टहरू** को रूपमा व्यवस्थापन गर्दछ,  
स्थिर फाइलको रूपमा होइन।

यो उपकरण अनुवादित Markdown, इमेजहरू, र नोटबुकहरूको स्थिति  
**भाषा-स्कोप्ड मेटाडेटा** प्रयोग गरेर ट्र्याक गर्दछ।

यस डिजाइनले Co-op Translator लाई अनुमति दिन्छ:

- पुरानो अनुवादहरू आफ्नो विश्वसनीय रूपमा पत्ता लगाउन
- Markdown, इमेजहरू, र नोटबुकहरूलाई एकरूप व्यवहार गर्न
- ठूलो, छिटो फैलने, बहुभाषी रिपोजिटरीहरूमा सुरक्षित रूपमा स्केल गर्न

अनुवादहरूलाई व्यवस्थापन गरिएको आर्टिफ्याक्टको रूपमा मोडलिङ गरेर,  
अनुवाद कार्यप्रवाहहरू आधुनिक  
सफ्टवेयर निर्भरता र आर्टिफ्याक्ट व्यवस्थापन अभ्यासहरूसँग स्वाभाविक रूपमा मेल खान्छन्।

→ [अनुवाद स्थिति कसरी व्यवस्थापन गरिन्छ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## छिटो सुरु

```bash
# एक भर्चुअल वातावरण सिर्जना गर्नुहोस् र सक्रिय गर्नुहोस् (सिफारिस गरिएको)
python -m venv .venv
# विन्डोज
.venv\Scripts\activate
# म्याकओएस/लिनक्स
source .venv/bin/activate
# प्याकेज स्थापना गर्नुहोस्
pip install co-op-translator
# अनुवाद गर्नुहोस्
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR बाट सार्वजनिक छवि तान्नुहोस्
docker pull ghcr.io/azure/co-op-translator:latest
# वर्तमान फोल्डरसहित चलाउनुहोस् र .env प्रदान गरिएको छ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## न्यूनतम सेटअप

1. तपाईंले समर्थित Python संस्करण (हाल 3.10-3.12) छ कि छैन निश्चित गर्नुहोस्। poetry (pyproject.toml) मा यो स्वचालित रूपमा ह्यान्डल हुन्छ।
2. टेम्प्लेट प्रयोग गरी `.env` फाइल बनाउनुहोस्: [.env.template](../../.env.template)
3. एक LLM प्रदायक कन्फिगर गर्नुहोस् (Azure OpenAI वा OpenAI)
4. (वैकल्पिक) इमेज अनुवादका लागि (`-img`), Azure AI Vision कन्फिगर गर्नुहोस्
5. (वैकल्पिक) तपाईं बहुविध क्रेडेन्सियल सेटहरू `_1`, `_2` आदि उपसर्गहरू थपेर कन्फिगर गर्न सक्नुहुन्छ। एउटै सेटका सबै भेरिएबलहरूले एकै उपसर्ग साझा गर्नुपर्छ।
6. (सिफारिस गरिएको) कुनै पनि पूर्व अनुवादहरू सफा गर्नुहोस् ताकि द्विविधा नहोस् (जस्तै, `translations/`)
7. (सिफारिस गरिएको) तपाईंको README मा अनुवाद सेक्सन थप्नुहोस् [README भाषाहरू टेम्प्लेट](./getting_started/README_languages_template.md) प्रयोग गरेर
8. हेर्नुहोस्: [Azure AI सेटअप गर्नुहोस्](./getting_started/set-up-azure-ai.md)

## प्रयोग

समर्थित सबै प्रकारहरू अनुवाद गर्नुहोस्:

```bash
translate -l "ko ja"
```

केवल Markdown:

```bash
translate -l "de" -md
```

Markdown + इमेजहरू:

```bash
translate -l "pt" -md -img
```

केवल नोटबुकहरू:

```bash
translate -l "zh" -nb
```

थप फ्ल्यागहरू: [कमाण्ड सन्दर्भ](./getting_started/command-reference.md)

## सुविधाहरू

- Markdown, नोटबुकहरू, र इमेजहरूको लागि स्वचालित अनुवाद
- स्रोतमा भएका परिवर्तनहरूसँग अनुवादहरूलाई समक्रमित राख्छ
- स्थानीय रूपमा (CLI) वा CI (GitHub Actions) मा काम गर्छ
- Azure OpenAI वा OpenAI प्रयोग गर्छ; इमेजहरूका लागि वैकल्पिक Azure AI Vision
- Markdown को फर्म्याटिङ र संरचना जोगाउँछ

## डकुमेन्टहरू

- [कमाण्ड-लाइन गाइड](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions गाइड (सार्वजनिक रिपोजिटरीहरू र मानक गोप्य जानकारी)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions गाइड (Microsoft संगठन रिपोजिटरीहरू र संगठन-स्तर सेटअपहरू)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README भाषाहरू टेम्प्लेट](./getting_started/README_languages_template.md)
- [समर्थित भाषाहरू](./getting_started/supported-languages.md)
- [योगदान गर्ने तरिका](./CONTRIBUTING.md)
- [समस्या समाधान](./getting_started/troubleshooting.md)

### माइक्रोसफ्ट-विशिष्ट गाइड
> [!NOTE]
> Microsoft “For Beginners” रिपोजिटरीहरूका मर्मतकर्ताहरूका लागि मात्र।

- [“अन्य कोर्सहरू” सूची अपडेट गर्ने तरिका (MS Beginners रिपोजिटरीहरूका लागि मात्र)](./getting_started/update-other-courses.md)

## हामीलाई समर्थन गर्नुहोस् र विश्वव्यापी शिक्षा प्रवर्द्धन गर्नुहोस्

हामीसँग सामेल भएर विश्वव्यापी शैक्षिक सामग्री साझा गर्ने तरिका परिवर्तन गर्न मद्दत गर्नुहोस्! [Co-op Translator](https://github.com/azure/co-op-translator) लाई GitHub मा ⭐ दिनुहोस् र सिकाइ र प्रविधिमा भाषागत बाधाहरू हटाउने हाम्रो मिशनमा समर्थन गर्नुहोस्। तपाईंको चासो र योगदानले ठूलो प्रभाव पार्छ! कोड योगदान र सुविधाहरू सुझाबहरू सधैं स्वागत छन्।

### आफ्नो भाषामा Microsoft शैक्षिक सामग्री अन्वेषण गर्नुहोस्

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
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

👉 तलको छवि क्लिक गरी YouTube मा हेर्नुहोस्।

- **Open at Microsoft**: Co-op Translator कसरी प्रयोग गर्ने बारे छोटो १८ मिनेटको परिचय र छिटो गाइड।

  [![Open at Microsoft](../../translated_images/ne/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

यो प्रोजेक्टमा योगदान र सुझावहरू स्वागत छ। Azure Co-op Translator मा योगदान दिन इच्छुक? कृपया हाम्रो [CONTRIBUTING.md](./CONTRIBUTING.md) हेरौं जसले Co-op Translator लाई अझ पहुँचयोग्य बनाउन तपाईं कसरी सहयोग गर्न सक्नुहुन्छ निर्देशन दिन्छ।

## योगदानकर्ता
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अपनाएको छ।
थप जानकारीको लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा
कुनै थप प्रश्न वा टिप्पणीका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) सम्पर्क गर्नुहोस्।

## जिम्मेवार AI

Microsoft ले हाम्रा ग्राहकहरूलाई हाम्रा AI उत्पादनहरू जिम्मेवारीपूर्वक प्रयोग गर्न, हाम्रा सिकाइहरू साझा गर्न, र Transparency Notes र Impact Assessments जस्ता उपकरणहरू मार्फत विश्वासमा आधारित साझेदारीहरू निर्माण गर्न प्रतिबद्ध छ। यी स्रोत मध्ये धेरै [https://aka.ms/RAI](https://aka.ms/RAI) मा भेट्न सकिन्छ।
Microsoft को जिम्मेवार AI प्रति दृष्टिकोण हाम्रो AI सिद्धान्तहरूमा आधारित छ जसमा fairness, reliability and safety, privacy and security, inclusiveness, transparency, र accountability समावेश छन्।

ठूलो स्तरको प्राकृतिक भाषा, छवि, र भाषण मोडेलहरू - जसरी यस नमुनामा प्रयोग गरिएका छन् - सम्भावित रूपमा अन्यायपूर्ण, अविश्वसनीय वा अपमानजनक व्यवहार गर्न सक्छन्, जसले नोक्सान पुर्याउन सक्छ। कृपया जोखिम र सीमाहरूको जानकारीका लागि [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) हेर्नुहोस्।

यी जोखिमहरू कम गर्ने सिफारिस गरिएको तरीका भनेको तपाईँको वास्तुकलामा सुरक्षा प्रणाली समावेश गर्नु हो जसले हानिकारक व्यवहारलाई पहिचान र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ले स्वतन्त्र सुरक्षा तह प्रदान गर्छ, जसले आवेदन र सेवाहरूमा हानिकारक प्रयोगकर्ता-निर्मित र AI-निर्मित सामग्री पत्ता लगाउन सक्छ। Azure AI Content Safety मा पाठ र छवि API हरू छन् जसले हानिकारक सामग्री पत्ता लगाउन अनुमति दिन्छ। हामीसँग एक अन्तरक्रियात्मक Content Safety Studio पनि छ जसले तपाईंलाई बिभिन्न प्रकारका सामग्रीहरूमा हानिकारक सामग्री पत्ता लगाउने नमुना कोड हेर्न, अन्वेषण गर्न र प्रयास गर्न अनुमति दिन्छ। निम्न [quickstart दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ले तपाईंलाई सेवामा अनुरोधहरू गर्नुमा मार्गनिर्देशन गर्छ।

अर्को पक्षले समग्र आवेदन प्रदर्शनलाई ध्यानमा राख्नु आवश्यक छ। बहु-प्रकार र बहु-मोडेल आवेदनहरूमा, हामीले प्रदर्शनलाई त्यो प्रणालीले तपाईं र तपाईँका प्रयोगकर्ताहरूको अपेक्षा अनुसार काम गर्ने भन्ने बुझ्छौं, जसले हानिकारक परिणामहरू उत्पन्न नगर्ने समावेश छ। तपाईंले आफ्नो समग्र आवेदनको प्रदर्शनलाई [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गरी मूल्याङ्कन गर्न महत्वपूर्ण छ।

तपाईं [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरी आफ्नो विकास वातावरणमा AI आवेदन मूल्याङ्कन गर्न सक्नुहुन्छ। परीक्षण डेटासेट वा लक्ष्य दिएको अवस्थामा, तपाईंको जनरेटिभ AI आवेदनहरूले निर्मित मूल्यांकनकर्ता वा तपाईंले रोजेका कस्टम मूल्यांकनकर्ताको साथ मात्रात्मक रूपमा मापन हुन्छन्। आफ्नो प्रणाली मूल्याङ्कन गर्न prompt flow sdk प्रयोग गर्न, तपाईं [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) पालना गर्न सक्नुहुन्छ। मूल्याङ्कन रन पछि, तपाईंले [Azure AI Studio मा परिणामहरू दृश्यात्मक रूपमा](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) हेर्न सक्नुहुन्छ।

## ट्रेडमार्क

यस परियोजनामा प्रोजेक्टहरू, उत्पादनहरू, वा सेवाहरूका लागि ट्रेडमार्क वा लोगोहरू हुन सक्छन्। Microsoft ट्रेडमार्क वा लोगोहरूको स्वीकृत प्रयोग गरिनुपर्छ र यसले [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) पालन गर्नैपर्छ।
Microsoft ट्रेडमार्क वा लोगोहरूको संशोधित संस्करणहरूमा प्रयोगले भ्रम पैदा गर्नु हुँदैन वा Microsoft प्रायोजनको संकेत गर्नु हुँदैन।
तेस्रो पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग ती तेस्रो पक्षका नीतिहरू अनुसार हुनेछ।

## सहायता पाउने तरिका

यदि तपाईं अड्किनु हुन्छ वा AI अनुप्रयोगहरू बनाउन कुनै प्रश्न छ भने, सहभागी हुनुहोस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि तपाईंलाई उत्पादन प्रतिक्रिया वा निर्माण गर्दा त्रुटिहरू छन् भने भ्रमण गर्नुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धिहरू हुन सक्छन्। मूल दस्तावेज यसको मौलिक भाषामा आधिकारिक स्रोतको रूपमा मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत अर्थ लगाउने कुराको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->