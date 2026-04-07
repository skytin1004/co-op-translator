# Co-op Translator

_आफ्नो शैक्षिक GitHub सामग्रीलाई बहुभाषी बनाएर सजिलै अनुवाद स्वचालित र मर्मत गर्नुहोस्, जस्तै-जस्तै तपाईंको परियोजना विकास हुँदै जान्छ।_

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
> यो रिपोजिटरीमा ५०+ भाषा अनुवादहरू समावेश छन् जसले डाउनलोड साइजलाई निकै बढाउँछ। अनुवादहरू बिना क्लोन गर्न, sparse checkout प्रयोग गर्नुहोस्:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> यसले तपाईंलाई कोर्स पूरा गर्न आवश्यक सबै कुरा कम समयमै डाउनलोड गरेर दिन्छ।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** ले तपाईंको शैक्षिक GitHub सामग्रीलाई सजिलै बहुभाषामा स्थानिय बनाउन मद्दत गर्दछ।  
जब तपाईं आफ्नो Markdown फाइलहरू, तस्बिरहरू वा नोटबुकहरू अपडेट गर्नुहुन्छ, अनुवादहरू स्वचालित रूपमा समक्रमणमा रहन्छन्, जसले विश्वभरिका विद्यार्थीहरूका लागि तपाईंको सामग्री सही र अद्यावधिक रहन्छ।

अनुवादित सामग्री कसरी व्यवस्थित गरिएको छ भन्ने उदाहरण:

![Example](../../imgs/translation-ex.png)

## अनुवाद स्थिति कसरी व्यवस्थापन गरिन्छ

Co-op Translator ले अनुवादित सामग्रीलाई **संस्करण गरिएको सफ्टवेयर वस्तुहरू (versioned software artifacts)** को रूपमा व्यवस्थापन गर्छ,  
स्थिर फाइलहरूका रूपमा होइन।

यो उपकरणले अनुवादित Markdown, तस्बिरहरू, र नोटबुकहरूको अवस्थालाई  
**भाषा-विशिष्ट मेटाडाटा (language-scoped metadata)** प्रयोग गरेर ट्र्याक गर्छ।

यो डिजाइनले Co-op Translator लाई सक्षम बनाउँछ:

- अव्यवस्थित अनुवादहरू भरपर्दो रूपमा पत्ता लगाउन
- Markdown, तस्बिर र नोटबुकलाई समान तरिकाले व्यवहार गर्न
- ठूलो, छिटो सञ्चालित बहुभाषी रिपोजिटरीहरूमा सुरक्षित रूपमा मापन गर्न

अनुवादहरूलाई व्यवस्थित वस्तुका रूपमा मोडेलिङ गरेर,  
अनुवाद कार्यप्रवाहहरू स्वाभाविक रूपमा आधुनिक सफ्टवेयर निर्भरता र वस्तु व्यवस्थापन अभ्याससँग मेल खान्छ।

→ [अनुवाद स्थिति कसरी व्यवस्थापन गरिन्छ](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## छिटो सुरु

```bash
# एउटा भर्चुअल वातावरण सिर्जना गर्नुहोस् र सक्रिय गर्नुहोस् (सिफारिस गरिएको)
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
# वर्तमान फोल्डर माउन्ट गरिएको र .env प्रदान गरिएको छ (Bash/Zsh) चलाउनुहोस्
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## न्यूनतम सेटअप

1. तपाईंले Supported Python संस्करण (हाल ३.१०-३.१२) छ कि छैन भनि सुनिश्चित गर्नुहोस्। Poetry (pyproject.toml) मा यो स्वचालित रूपमा ह्यान्डल हुन्छ।
2. टेम्प्लेट प्रयोग गरेर `.env` फाइल सिर्जना गर्नुहोस्: [.env.template](../../.env.template)
3. एउटा LLM प्रदायक कन्फिगर गर्नुहोस् (Azure OpenAI वा OpenAI)
4. (वैकल्पिक) तस्बिर अनुवादको लागि (`-img`) Azure AI Vision कन्फिगर गर्नुहोस्
5. (वैकल्पिक) तपाईं सुफिक्स जस्तै `_1`, `_2`, आदि प्रयोग गरेर धेरै क्रेडेन्सियल सेटहरू कन्फिगर गर्न सक्नुहुन्छ। एउटै सेटका सबै भेरिएबलहरूमा एउटै सुफिक्स हुनुपर्छ।
6. (सिफारिस गरिन्छ) सञ्झ्यालहरू जस्तो `translations/` बाट कुनै पुराना अनुवाद सफा गर्नुहोस् ताकि द्वन्द्व नहोस्।
7. (सिफारिस गरिन्छ) तपाईंको README मा अनुवाद अनुभाग थप्न [README languages template](./getting_started/README_languages_template.md) प्रयोग गर्नुहोस्।
8. हेर्नुहोस्: [Azure AI सेटअप गर्नुहोस्](./getting_started/set-up-azure-ai.md)

## प्रयोग

सबै समर्थित प्रकारहरू अनुवाद गर्नुहोस्:

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

मात्र नोटबुकहरू:

```bash
translate -l "zh" -nb
```

अझै धेरै फ्ल्यागहरू: [Command reference](./getting_started/command-reference.md)

## सुविधाहरू

- Markdown, नोटबुक र तस्बिरहरूको स्वचालित अनुवाद
- स्रोतमा भएका परिवर्तनहरूसँग अनुवादलाई समान्तर राख्छ
- लोकलमा (CLI) वा CI मा (GitHub Actions) काम गर्दछ
- Azure OpenAI वा OpenAI प्रयोग गर्दछ; तस्बिरहरूको लागि वैकल्पिक Azure AI Vision
- Markdown को फर्म्याटिङ र संरचना संरक्षण गर्दछ

## कागजातहरू

- [कमाण्ड लाइन गाइड](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions गाइड (सार्वजनिक रिपोजिटरीहरू र सामान्य सिक्रेटहरू)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions गाइड (Microsoft संस्था रिपोजिटरीहरू र संस्थागत सेटअपहरू)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README भाषा टेम्प्लेट](./getting_started/README_languages_template.md)
- [समर्थित भाषाहरू](./getting_started/supported-languages.md)
- [योगदान दिनुहोस्](./CONTRIBUTING.md)
- [समस्या समाधान](./getting_started/troubleshooting.md)

### Microsoft विशिष्ट गाइड
> [!NOTE]
> Microsoft “For Beginners” रिपोजिटरीका मर्मतकर्ताहरूका लागि मात्र।

- [“other courses” सूची अद्यावधिक गर्ने (MS Beginners रिपोजिटरीहरूका लागि मात्र)](./getting_started/update-other-courses.md)

## हामीलाई समर्थन गर्नुहोस् र विश्वव्यापी सिकाइ प्रवर्द्धन गर्नुहोस्

शैक्षिक सामग्री विश्वभर कसरी साझा गरिन्छ त्यसमा क्रान्ति ल्याउन हामीसँग हातेमालो गर्नुहोस्!  
[Co-op Translator](https://github.com/azure/co-op-translator) लाई GitHub मा ⭐ दिनुहोस् र सिकाइ र प्रविधिमा भाषा बाधाहरूलाई भत्काउने हाम्रो मिशनलाई समर्थन गर्नुहोस्। तपाईंको रुचि र योगदानहरूले ठूलो प्रभाव पार्दछ!  
कोड योगदान र सुविधासम्बन्धी सुझावहरू सधैं स्वागत छन्।

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

👉 तलको तस्बिरमा क्लिक गरेर YouTube मा हेर्नुहोस्।

- **Open at Microsoft**: Co-op Translator कसरी प्रयोग गर्नेछ भनेर संक्षिप्त १८ मिनेटको परिचय र छिटो गाइड।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान दिनुहोस्

यो परियोजनामा योगदान र सुझावहरू स्वागतयोग्य छन्। Azure Co-op Translator मा योगदान दिन इच्छुक हुनुहुन्छ? कृपया हाम्रो [CONTRIBUTING.md](./CONTRIBUTING.md) हेर्नुहोस् जसले कसरी Co-op Translator लाई झन् पहुँचयोग्य बनाउन मद्दत गर्न सकिन्छ भनेर मार्गदर्शन गर्छ।

## योगदानकर्ताहरू
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

यस परियोजनाले [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) अंगिकार गरेको छ।
थप जानकारीका लागि [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) हेर्नुहोस् वा 
थप प्रश्न वा टिप्पणीका लागि [opencode@microsoft.com](mailto:opencode@microsoft.com) सम्पर्क गर्नुहोस्।

## जिम्मेवार AI

Microsoft हाम्रा ग्राहकहरूलाई हाम्रा AI उत्पादनहरू जिम्मेवार तरीकाले प्रयोग गर्न सहयोग गर्ने, हाम्रो सिकाइ साझा गर्ने, र Transparency Notes र Impact Assessments जस्ता उपकरणमार्फत विश्वास-आधारित साझेदारीहरू निर्माण गर्ने प्रतिबद्ध छ। यी मध्ये धेरै स्रोतहरू [https://aka.ms/RAI](https://aka.ms/RAI) मा पाउन सकिन्छ।
जिम्मेवार AI को लागि Microsoft को दृष्टिकोण हाम्रा AI सिद्धान्तहरूमा आधारित छ जसमा निष्पक्षता, भरपर्दोता र सुरक्षा, गोपनीयता र सुरक्षा, समावेशिता, पारदर्शिता, र जवाफदेहिता समावेश छन्।

ठूला-स्तरका प्राकृतिक भाषा, चित्र, र भाषण मोडेलहरू - जसरी यस नमुनामा प्रयोग भएका छन् - सम्भावित रूपमा अनुचित, अविश्वसनीय, वा अपमानजनक व्यवहार गर्न सक्छन्, जसले हानि पुर्‍याउन सक्छ। कृपया जोखिम र सीमाहरूको बारेमा जानकारीको लागि [Azure OpenAI सेवा Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) परामर्श गर्नुहोस्।

यी जोखिमहरू घटाउने सिफारिस गरिएको दृष्टिकोण भनेको तपाईंको वास्तुकलामा एक सुरक्षा प्रणाली समावेश गर्नु हो जसले हानिकारक व्यवहार पत्ता लगाउन र रोक्न सक्छ। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ले स्वतन्त्र सुरक्षा तह प्रदान गर्दछ, जुन अनुप्रयोगहरू र सेवाहरूमा नकारात्मक प्रयोगकर्ता-निर्मित र AI-निर्मित सामग्री पत्ता लगाउन सक्षम छ। Azure AI Content Safety मा text र image API हरू समावेश छन् जसले तपाईंलाई हानिकारक सामग्री पत्ता लगाउन अनुमति दिन्छ। हामीसँग एउटा अन्तरक्रियात्मक Content Safety Studio पनि छ जसले तपाईंलाई विभिन्न मोडलिटीहरूमा हानिकारक सामग्री पत्ता लगाउन नमूना कोड हेर्न, अनुसन्धान गर्न र प्रयास गर्न अनुमति दिन्छ। निम्न [quickstart डकुमेन्टेसन](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ले तपाईंलाई सेवामा अनुरोध गर्ने क्रममा मार्गदर्शन गर्दछ।

अर्को पक्ष हो समग्र अनुप्रयोग प्रदर्शन। बहु-मोडल र बहु-मोडेल अनुप्रयोगहरूसँग, हामी प्रदर्शनलाई त्यसरी बुझ्छौं कि प्रणाली तपाईं र तपाईंका प्रयोगकर्ताहरूले अपेक्षा गर्ने अनुसार काम गर्दछ, जसमा हानिकारक आउटपुट नउत्पन्न हुनु पर्छ। आफ्नो समग्र अनुप्रयोगको प्रदर्शन [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) प्रयोग गरी मूल्यांकन गर्नु महत्त्वपूर्ण छ।

तपाईं आफ्नो विकास वातावरणमा [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) प्रयोग गरी आफ्नो AI अनुप्रयोगको मूल्यांकन गर्न सक्नुहुन्छ। टेस्ट डेटासेट वा लक्ष्य दिइएपछि, तपाईंको जेनेरेटिभ AI अनुप्रयोगका जेनेरेसनहरू built-in मूल्यांकक वा तपाईंको रोजाइका कस्टम मूल्यांककहरूद्वारा मात्रात्मक रूपमा मापन गरिन्छ। प्रणालीको मूल्यांकन सुरु गर्न prompt flow sdk प्रयोग गरेर, तपाईं [quickstart गाइड](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) पछ्याउन सक्नुहुन्छ। मूल्यांकन रन सम्पन्न भएपछि, तपाईं [Azure AI Studio मा परिणामहरू देखाउन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) सक्नुहुन्छ।

## ट्रेडमार्कहरू

यस परियोजनामा परियोजना, उत्पादन, वा सेवाहरूका ट्रेडमार्क वा लोगोहरू हुन सक्छन्। Microsoft ट्रेडमार्क वा लोगोहरूको अधिकृत प्रयोग [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) पालना गर्नुपर्नेछ।
यो परियोजनाको परिमार्जित संस्करणहरूमा Microsoft ट्रेडमार्क वा लोगोहरूको प्रयोगले भ्रम उत्पन्न हुनु वा Microsoft को प्रायोजन संकेत गर्नु हुँदैन।
तृतीय-पक्ष ट्रेडमार्क वा लोगोहरूको कुनै पनि प्रयोग तिनीहरूको नीतिहरूमा निर्भर गर्छ।

## सहायता पाउनुहोस्

यदि तपाईं अड्किएको वा AI एपहरू निर्माण गर्दा कुनै प्रश्न छ भने, सहभागी हुनुहोस्:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि तपाईंको उत्पादन प्रतिक्रिया वा निर्माण गर्दा त्रुटिहरू छन् भने यहाँ जानुहोस्:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो कागजात [Co-op Translator](https://github.com/Azure/co-op-translator) नामक एआई अनुवाद सेवाको प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयासरत छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादहरूमा त्रुटिहरू वा अशुद्धि हुन सक्छन्। मूल कागजात यसको मातृ भाषामा अधिकृत स्रोतमात्र मानिनुपर्छ। महत्त्वपूर्ण जानकारीको लागि व्यावसायिक मानवीय अनुवादको सिफारिश गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै गलतफहमी वा भ्रामक व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->