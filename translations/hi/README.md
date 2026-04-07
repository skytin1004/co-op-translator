# Co-op Translator

_अपनी शैक्षिक GitHub सामग्री के लिए कई भाषाओं में अनुवाद को स्वचालित रूप से सरलता से करें और अपने प्रोजेक्ट के विकास के साथ बनाए रखें।_

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

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारा समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](./README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **पसंद है स्थानीय क्लोनिंग?**
>
> यह रिपॉजिटरी 50+ भाषा अनुवाद शामिल करता है जो डाउनलोड आकार को काफी बढ़ा देता है। अनुवाद के बिना क्लोन करने के लिए, sparse checkout का उपयोग करें:
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
> यह आपको बहुत तेज़ डाउनलोड के साथ कोर्स पूरा करने के लिए सब कुछ देता है।
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** आपकी शैक्षिक GitHub सामग्री को कई भाषाओं में आसानी से लोकलाइज़ करने में मदद करता है।  
जब आप अपने Markdown फ़ाइलें, चित्र, या नोटबुक अपडेट करते हैं, तो अनुवाद स्वतः समकालीन रहते हैं, जिससे आपकी सामग्री विश्वभर के शिक्षार्थियों के लिए सटीक और अद्यतित बनी रहती है।

अनुवादित सामग्री के संगठन का उदाहरण:

![Example](../../imgs/translation-ex.png)

## अनुवाद की स्थिति कैसे प्रबंधित की जाती है

Co-op Translator अनुवादित सामग्री को **संस्करणित सॉफ़्टवेयर आर्टिफेक्ट्स** के रूप में प्रबंधित करता है,  
स्थिर फाइलों के रूप में नहीं।

यह टूल भाषा-प्रासंगिक मेटाडेटा का उपयोग करके अनुवादित Markdown, चित्र, और नोटबुक की स्थिति को ट्रैक करता है।

यह डिज़ाइन Co-op Translator को सक्षम बनाता है:

- पुरानी अनुवादों का विश्वसनीय पता लगाएं
- Markdown, चित्र, और नोटबुक को सुसंगत रूप से संभालें
- बड़े, तेज़ी से बढ़ते, बहुभाषी रिपॉजिटरीज़ के लिए सुरक्षित स्केल करें

अनुवादों को प्रबंधित किए गए आर्टिफेक्ट्स के रूप में मॉडल करके,  
अनुवाद कार्यप्रवाह स्वाभाविक रूप से आधुनिक सॉफ़्टवेयर निर्भरता और आर्टिफेक्ट प्रबंधन के अभ्यासों के साथ मेल खाते हैं।

→ [अनुवाद की स्थिति कैसे प्रबंधित की जाती है](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## त्वरित आरंभ

```bash
# एक वर्चुअल वातावरण बनाएं और सक्रिय करें (अनुशंसित)
python -m venv .venv
# विंडोज़
.venv\Scripts\activate
# मैकओएस/लिनक्स
source .venv/bin/activate
# पैकेज इंस्टॉल करें
pip install co-op-translator
# अनुवाद करें
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR से सार्वजनिक इमेज को खींचें
docker pull ghcr.io/azure/co-op-translator:latest
# वर्तमान फ़ोल्डर को माउंट करके और .env प्रदान करके चलाएं (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## न्यूनतम सेटअप

1. सुनिश्चित करें कि आपके पास एक समर्थित Python संस्करण है (वर्तमान में 3.10-3.12)। poetry (pyproject.toml) में यह स्वतः संचालित होता है।  
2. टेम्पलेट का उपयोग करके `.env` फ़ाइल बनाएं: [.env.template](../../.env.template)  
3. एक LLM प्रदाता कॉन्फ़िगर करें (Azure OpenAI या OpenAI)  
4. (वैकल्पिक) छवि अनुवाद (`-img`) के लिए Azure AI Vision कॉन्फ़िगर करें  
5. (वैकल्पिक) आप `_1`, `_2` जैसे उपसर्गों के साथ चर को डुप्लिकेट करके कई क्रेडेंशियल सेट कॉन्फ़िगर कर सकते हैं। एक सेट के सभी वेरिएबल समान उपसर्ग साझा करने चाहिए।  
6. (अनुशंसित) टकराव से बचने के लिए पिछले अनुवाद साफ़ करें (जैसे, `translations/`)  
7. (अनुशंसित) अपने README में अनुवाद अनुभाग जोड़ें [README languages template](./getting_started/README_languages_template.md) का उपयोग करके  
8. देखें: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

## उपयोग

सभी समर्थित प्रकार को अनुवादित करें:

```bash
translate -l "ko ja"
```

केवल Markdown:

```bash
translate -l "de" -md
```

Markdown + चित्र:

```bash
translate -l "pt" -md -img
```

केवल नोटबुक:

```bash
translate -l "zh" -nb
```

अधिक ध्वज: [Command reference](./getting_started/command-reference.md)

## विशेषताएं

- Markdown, नोटबुक, और चित्रों के लिए स्वचालित अनुवाद  
- स्रोत परिवर्तनों के साथ अनुवादों को सिंक में रखता है  
- स्थानीय रूप से (CLI) या CI (GitHub Actions) में काम करता है  
- Azure OpenAI या OpenAI का उपयोग करता है; चित्रों के लिए वैकल्पिक Azure AI Vision  
- Markdown फ़ॉर्मेटिंग और संरचना को संरक्षित करता है

## दस्तावेज़

- [कमान्ड-लाइन मार्गदर्शिका](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions मार्गदर्शिका (सार्वजनिक रिपॉजिटरी एवं मानक गुप्त)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions मार्गदर्शिका (Microsoft संस्था रिपॉजिटरी एवं संगठन-स्तर सेटअप)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README भाषाओं का टेम्पलेट](./getting_started/README_languages_template.md)  
- [समर्थित भाषाएँ](./getting_started/supported-languages.md)  
- [योगदान कैसे करें](./CONTRIBUTING.md)  
- [समस्या निवारण](./getting_started/troubleshooting.md)

### Microsoft-विशिष्ट मार्गदर्शिका
> [!NOTE]
> केवल Microsoft "For Beginners" रिपॉजिटरीज़ के मेंटेनरों के लिए।

- [“अन्य कोर्सेस” सूची अपडेट (केवल MS Beginners रिपॉजिटरीज़ के लिए)](./getting_started/update-other-courses.md)

## हमारा समर्थन करें और वैश्विक शिक्षण को बढ़ावा दें

शिक्षात्मक सामग्री को विश्व स्तर पर साझा करने के तरीके में क्रांति लाने में हमारे साथ जुड़ें! [Co-op Translator](https://github.com/azure/co-op-translator) को GitHub पर ⭐ दें और सीखने तथा प्रौद्योगिकी में भाषा की बाधाओं को तोड़ने के हमारे मिशन का समर्थन करें। आपकी रुचि और योगदान बड़ा प्रभाव डालते हैं! कोड योगदान और फीचर सुझाव हमेशा स्वागत योग्य हैं।

### अपनी भाषा में Microsoft शैक्षिक सामग्री एक्सप्लोर करें

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

## वीडियो प्रस्तुतियाँ

👉 YouTube पर देखने के लिए नीचे चित्र पर क्लिक करें।

- **Open at Microsoft**: Co-op Translator का संक्षिप्त 18 मिनट का परिचय और त्वरित मार्गदर्शिका।

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

यह प्रोजेक्ट योगदान और सुझावों का स्वागत करता है। Azure Co-op Translator में योगदान देना चाहते हैं? कृपया हमारी [CONTRIBUTING.md](./CONTRIBUTING.md) देखें यह जानने के लिए कि आप Co-op Translator को अधिक सुलभ बनाने में कैसे मदद कर सकते हैं।

## योगदानकर्ता
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

यह परियोजना [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) को अपनाती है।  
अधिक जानकारी के लिए देखें [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) या  
किसी भी अतिरिक्त प्रश्न या टिप्पणी के लिए संपर्क करें [opencode@microsoft.com](mailto:opencode@microsoft.com)।

## जिम्मेदार AI

Microsoft हमारे ग्राहकों को हमारे AI उत्पादों का जिम्मेदारी से उपयोग करने में मदद करने, हमारे सीखों को साझा करने, और Trust-based साझेदारियाँ बनाने के लिए प्रतिबद्ध है, जो Transparency Notes और Impact Assessments जैसे उपकरणों के माध्यम से संभव होता है। इन संसाधनों में से कई [https://aka.ms/RAI](https://aka.ms/RAI) पर उपलब्ध हैं।  
Microsoft का जिम्मेदार AI का दृष्टिकोण हमारे AI सिद्धांतों पर आधारित है: निष्पक्षता, विश्वसनीयता और सुरक्षा, गोपनीयता और सुरक्षा, समावेशिता, पारदर्शिता, और जवाबदेही।

बड़े पैमाने पर प्राकृतिक भाषा, छवि, और भाषण मॉडल — जैसे कि इस उदाहरण में उपयोग किए गए मॉडल — संभावित रूप से ऐसे व्यवहार कर सकते हैं जो अनुचित, अविश्वसनीय, या अपमानजनक हो सकते हैं, जो नुकसान पहुंचा सकते हैं। कृपया जोखिमों और सीमाओं के बारे में जानकारी के लिए [Azure OpenAI सेवा Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) देखें।

इन जोखिमों को कम करने के लिए सुझाया गया तरीका है कि अपने आर्किटेक्चर में एक सुरक्षा प्रणाली शामिल करें जो हानिकारक व्यवहार का पता लगा सके और उसे रोक सके। [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा परत प्रदान करता है, जो एप्लिकेशन और सेवाओं में हानिकारक उपयोगकर्ता-जनित और AI-जनित सामग्री का पता लगाने में सक्षम है। Azure AI Content Safety में टेक्स्ट और इमेज API शामिल हैं जो हानिकारक सामग्री का पता लगाने की अनुमति देते हैं। हमारे पास एक इंटरैक्टिव Content Safety Studio भी है जो आपको विभिन्न मॉडालिटीज़ में हानिकारक सामग्री का पता लगाने के लिए नमूना कोड देखने, एक्सप्लोर करने और आज़माने की सुविधा देता है। निम्नलिखित [quickstart दस्तावेज़](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपको सेवा के लिए अनुरोध करने का मार्गदर्शन करता है।

एक और पहलू जिसे ध्यान में रखना चाहिए वह है समग्र एप्लिकेशन प्रदर्शन। मल्टी-मॉडल और मल्टी-मॉडल एप्लिकेशन के साथ, हम प्रदर्शन को इस रूप में मानते हैं कि सिस्टम आपके और आपके उपयोगकर्ताओं की अपेक्षाओं के अनुसार काम करे, जिसमें हानिकारक आउटपुट न उत्पन्न होना भी शामिल है। अपने समग्र एप्लिकेशन के प्रदर्शन का आकलन करना महत्वपूर्ण है, इसके लिए आप [generation quality और risk and safety मेट्रिक्स](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) का उपयोग कर सकते हैं।

आप अपने विकास वातावरण में अपने AI एप्लिकेशन का मूल्यांकन [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) के साथ कर सकते हैं। किसी परीक्षण डेटासेट या लक्ष्य के आधार पर, आपके जेनरेटिव AI एप्लिकेशन की उत्पत्तियों को बिल्ट-इन मूल्यांकनकर्ताओं या अपनी पसंद के कस्टम मूल्यांकनकर्ताओं के साथ मात्रात्मक रूप से मापा जाता है। अपने सिस्टम का मूल्यांकन करने के लिए prompt flow sdk के साथ शुरुआत करने के लिए, आप [quickstart गाइड](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) का पालन कर सकते हैं। एक बार जब आप मूल्यांकन चलाते हैं, तो आप [Azure AI Studio में परिणामों का दृश्यावलोकन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) कर सकते हैं।

## ट्रेडमार्क

यह परियोजना परियोजनाओं, उत्पादों, या सेवाओं के लिए ट्रेडमार्क या लोगो शामिल कर सकती है। Microsoft ट्रेडमार्क या लोगो का अधिकृत उपयोग [Microsoft के Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) के अधीन और अनुसार होना चाहिए।  
Microsoft ट्रेडमार्क या लोगो का इस परियोजना के संशोधित संस्करणों में उपयोग भ्रम उत्पन्न नहीं करना चाहिए या Microsoft प्रायोजन का अर्थ नहीं होना चाहिए।  
तीसरे पक्ष के ट्रेडमार्क या लोगो का कोई भी उपयोग उन तीसरे पक्ष की नीतियों के अधीन होगा।

## सहायता प्राप्त करें

यदि आप अटक जाएं या AI एप्लिकेशन बनाने के बारे में कोई प्रश्न हो, तो जुड़ें:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

यदि आपके पास उत्पाद प्रतिक्रिया है या निर्माण के दौरान कोई त्रुटि होती है तो जाएँ:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल दस्तावेज़ अपने स्वदेशी भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफ़हमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->