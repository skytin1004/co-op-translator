# Co-op Translator

_आपल्या शैक्षणिक GitHub सामग्रीच्या भाषांतरांना सहजपणे स्वयंचलित करा आणि अनेक भाषांमध्ये प्रोजेक्ट विकसित होताना त्याचे व्यवस्थापन करा._

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

### 🌐 बहुभाषिक समर्थन

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारे समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानिक क्लोन प्राधान्य द्याल का?**
>
> हा रेपॉझिटरी ५०+ भाषांच्या भाषांतरांसह आहे ज्यामुळे डाउनलोड साइज खूप वाढतो. भाषांतरेशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> यामुळे तुम्हाला कोर्स पूर्ण करण्यासाठी आवश्यक असलेले सर्व काही जलद डाउनलोडसह प्राप्त होईल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## आढावा

**Co-op Translator** आपली शैक्षणिक GitHub सामग्री अनेक भाषांमध्ये सहजपणे स्थानिकीकरण करण्यात मदत करतो.  
जेव्हा आपण आपल्या Markdown फाइल्स, प्रतिमा किंवा नोटबुक्स अद्ययावत करता, तेव्हा भाषांतर आपोआप समक्रमित राहतात, ज्यामुळे आपली सामग्री संपूर्ण जगभरातील शिकणाऱ्यांसाठी अचूक आणि अद्ययावत राहते.

भाषांतरित सामग्री कशी आयोजित केली जाते याचा उदाहरण:

![Example](../../translated_images/mr/translation-ex.0c8aa6a7ee0aad2b.webp)

## भाषांतर स्थिती कशी व्यवस्थापित केली जाते

Co-op Translator भाषांतरित सामग्रीला **आवृत्तीवार सॉफ्टवेअर घटक** म्हणून व्यवस्थापित करतो,  
स्थिर फाइल्स म्हणून नाही.

हे टूल भाषांतरित Markdown, प्रतिमा आणि नोटबुक्सची स्थिती ट्रॅक करते  
**भाषा-विशिष्ट मेटाडेटा** वापरून.

हा डिझाइन Co-op Translator ला परवानगी देतो:

- जुनी झालेली भाषांतर विश्वसनीयरित्या ओळखण्याची
- Markdown, प्रतिमा आणि नोटबुक्सना सतत एकसमान वागणूक देण्याची
- मोठ्या, जलद गतीने बदलणाऱ्या, बहुभाषिक रेपॉझिटरीजमध्ये सुरक्षितपणे स्केल करण्याची

भाषांतरांना व्यवस्थापित घटक म्हणून मॉडेलिंग करून,  
भाषांतर कार्यप्रवाह आधुनिक  
सॉफ्टवेअर अवलंबित्व आणि घटक व्यवस्थापन पद्धतींशी निसर्गाने संरेखित होतात.

→ [भाषांतर स्थिती कशी व्यवस्थापित केली जाते](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## जलद प्रारंभ

```bash
# एक व्हर्च्युअल एन्व्हायरमेंट तयार करा आणि सक्रिय करा (शिफारस केली जाते)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# पॅकेज इंस्टॉल करा
pip install co-op-translator
# भाषांतर करा
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR कडून सार्वजनिक इमेज ओढा
docker pull ghcr.io/azure/co-op-translator:latest
# सध्याची फोल्डर माउंट करून आणि .env प्रदान करुन चालवा (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## किमान सेटअप

1. तपासा की तुमच्याकडे समर्थित Python आवृत्ती आहे (सद्यस्थितीत 3.10-3.12). poetry (pyproject.toml) मध्ये हे स्वयंचलितपणे होते.
2. टेम्प्लेट वापरून `.env` फाइल तयार करा: [.env.template](../../.env.template)
3. एक LLM प्रदाता कॉन्फिगर करा (Azure OpenAI किंवा OpenAI)
4. (पर्यायी) प्रतिमा भाषांतरासाठी (`-img`), Azure AI Vision कॉन्फिगर करा
5. (पर्यायी) तुम्ही अनेक क्रेडेन्शियल सेट्स कॉन्फिगर करू शकता ज्यासाठी `_1`, `_2` असे उपसर्ग असलेल्या बदलणाऱ्या नावांसह व्हेरिएबल्स डुप्लिकेट करा. एका सेटमधील सर्व व्हेरिएबल्स एकाच उपसर्गसह असावेत.
6. (शिफारसीय) संभाव्य संघर्ष टाळण्यासाठी पूर्वीच्या कोणत्याही भाषांतर साफ करा (उदा., `translations/`)
7. (शिफारसीय) आपल्या README मध्ये [README languages template](./getting_started/README_languages_template.md) वापरून भाषांतर विभाग जोडा
8. पहा: [Azure AI सेटअप करा](./getting_started/set-up-azure-ai.md)

## वापर

संपूर्ण समर्थित प्रकारांचे भाषांतर करा:

```bash
translate -l "ko ja"
```

फक्त Markdown:

```bash
translate -l "de" -md
```

Markdown + प्रतिमा:

```bash
translate -l "pt" -md -img
```

फक्त नोटबुक्स:

```bash
translate -l "zh" -nb
```

अधिक फ्लॅग्ज: [कमांड संदर्भ](./getting_started/command-reference.md)

## वैशिष्ट्ये

- Markdown, नोटबुक्स आणि प्रतिमांसाठी स्वयंचलित भाषांतर
- स्रोत बदलांशी भाषांतर समक्रमित ठेवते
- स्थानिकपणे (CLI) किंवा CI (GitHub Actions) मध्ये काम करते
- Azure OpenAI किंवा OpenAI वापरते; प्रतिमांसाठी Azure AI Vision पर्यायी
- Markdown फॉरमॅटिंग आणि रचनांचे संरक्षण करते

## दस्तऐवज

- [कमान्ड-लाइन मार्गदर्शक](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions मार्गदर्शक (सार्वजनिक रेपॉझिटरीज आणि सामान्य सीक्रेट्स)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions मार्गदर्शक (Microsoft संस्था रेपॉझिटरीज आणि संस्था-स्तरीय सेटअप्स)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Supported languages](./getting_started/supported-languages.md)
- [योगदान](./CONTRIBUTING.md)
- [समस्या निवारण](./getting_started/troubleshooting.md)

### Microsoft-विशिष्ट मार्गदर्शक
> [!NOTE]
> Microsoft “For Beginners” रेपॉझिटरीजच्या देखभाल करणाऱ्यांसाठीच.

- [“other courses” यादी अद्ययावत करणे (फक्त MS Beginners रेपॉझिटरीजसाठी)](./getting_started/update-other-courses.md)

## आमचा पाठिंबा करा व जागतिक शिक्षणाला प्रोत्साहन द्या

शैक्षणिक सामग्री जागतिकपणे कशी शेअर केली जाते यामध्ये क्रांती करा! [Co-op Translator](https://github.com/azure/co-op-translator) ला GitHub वर ⭐ द्या आणि शिक्षण व तंत्रज्ञानातील भाषा अडथळे मोडण्याच्या आमच्या मिशनला समर्थन करा. तुमची आवड आणि योगदान महत्त्वपूर्ण प्रभाव टाकतात! कोड योगदान आणि वैशिष्ट्यांच्या सूचना नेहमी स्वागतार्ह आहेत.

### Microsoft शैक्षणिक सामग्री तुमच्या भाषेत एक्सप्लोर करा

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

## व्हिडिओ सादरीकरणे

👉 खालील प्रतिमेवर क्लिक करून YouTube वर पाहा.

- **Open at Microsoft**: Co-op Translator कसा वापरायचा यावर एक १८ मिनिटांचा थोडक्यात परिचय आणि जलद मार्गदर्शक.

  [![Open at Microsoft](../../translated_images/mr/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

हा प्रोजेक्ट योगदान आणि सूचना स्वागत करतो. Azure Co-op Translator मध्ये योगदान देण्यास उत्सुक आहात का? कृपया आमच्या [CONTRIBUTING.md](./CONTRIBUTING.md) भेट द्या ज्यात Co-op Translator अधिक प्रवेशयोग्य बनवण्यासाठी कसे मदत करू शकता हे मार्गदर्शन आहे.

## योगदानकर्ते
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## वर्तनसंहिता

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारली आहे.
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा
कोणत्याही अतिरिक्त प्रश्नांसाठी किंवा टिप्पण्यांसाठी [opencode@microsoft.com](mailto:opencode@microsoft.com) शी संपर्क करा.

## जबाबदार AI

Microsoft आमचे ग्राहक जबाबदारीने आमची AI उत्पादने वापरतील यासाठी समर्पित आहे, आमचे शिकवण share करत आहे, आणि Transparency Notes आणि Impact Assessments सारख्या साधनांद्वारे विश्वास-आधारित भागीदारी तयार करत आहे. या अनेक संसाधने [https://aka.ms/RAI](https://aka.ms/RAI) येथे आढळू शकतात.
Microsoft चा जबाबदार AI कडे असलेला दृष्टीकोन हमारे AI तत्त्वांवर आधारलेला आहे: न्याय, विश्वसनीयता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, सर्वसमावेशकता, पारदर्शकता, आणि जबाबदारी.

मोठ्या प्रमाणावरील नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल - जसे या नमुना मध्ये वापरलेले आहेत - संभाव्यपणे अन्यायकारक, अविश्वसनीय किंवा अपमानजनक वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. कृपया जोखमी आणि मर्यादा यांची माहिती घेण्यासाठी [Azure OpenAI सेवा Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) पहा.

या जोखमी कमी करण्यासाठी शिफारस केलेला उपाय म्हणजे तुमच्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली असणे जिने हानिकारक वर्तन ओळखू आणि प्रतिबंधित करू शकेल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षणाचा स्तर पुरवते, जे अनुप्रयोगांमध्ये आणि सेवांमध्ये वापरकर्त्याद्वारे आणि AI द्वारे तयार करण्यात आलेल्या हानिकारक सामग्रीचा शोध घेण्यासाठी सक्षम आहे. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा APIs आहेत ज्यामुळे तुम्ही हानिकारक सामग्रीचा शोध घेऊ शकता. आमच्याकडे एक इंटरऍक्टिव्ह Content Safety Studio देखील आहे जे तुम्हाला हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहता, तपासू शकता आणि वापरू शकता, विविध प्रकारच्या माध्यमांमधील. पुढील [quickstart दस्तऐवज](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) तुम्हाला सेवेला विनंत्या कशा करायच्या यासाठी मार्गदर्शन करतात.

दुसरी बाब जी लक्षात घ्यावी ती म्हणजे एकंदर अनुप्रयोग कार्यक्षमता. बहु-माध्यम आणि बहु-मॉडेल अनुप्रयोगांसह, आम्ही कार्यक्षमता म्हणजे प्रणाली तशी कार्य करते जशी तुम्ही आणि तुमचे वापरकर्ते अपेक्षा करतात, ज्यात हानिकारक आउटपुट तयार न करणे समाविष्ट आहे. तुम्हाला तुमच्या एकंदरीत अनुप्रयोगाची कार्यक्षमता [उत्पादन गुणवत्ता आणि जोखीम व सुरक्षितता मेट्रिक्स](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून मूल्यांकन करणे महत्त्वाचे आहे.

तुम्ही तुमच्या AI अनुप्रयोगाचे मूल्यांकन तुमच्या विकास वातावरणामध्ये [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) वापरून करू शकता. चाचणी डेटासेट किंवा लक्ष्य दिल्यास, तुमच्या जनरेटिव्ह AI अनुप्रयोगाच्या निर्मिती चे गुणात्मक मापन अंगभूत मूल्यांकन साधने किंवा तुम्ही निवडलेल्या सानुकूल मूल्यांकन साधनांद्वारे केले जाते. तुमचा प्रणालीचे मूल्यांकन करण्यासाठी prompt flow sdk वापरण्यास सुरुवात करण्यासाठी, तुम्ही [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरू शकता. एकदा तुम्ही मूल्यांकन चालवले की, तुम्ही [Azure AI Studio मध्ये परिणाम दृष्टीकोन](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) करू शकता.

## ट्रेडमार्क

हा प्रकल्प प्रकल्प, उत्पादने किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतो. Microsoft ट्रेडमार्क किंवा लोगोच्या अधिकृत वापरासाठी खालील नियमांचे पालन आवश्यक आहे:  
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगोचा वापर गोंधळ निर्माण करू नये किंवा Microsoft च्या प्रायोजकत्वाचा अर्थ दर्शवू नये.  
तृतीय पक्षांच्या ट्रेडमार्क किंवा लोगो कोणत्याही वापरासाठी त्या तृतीय पक्षांच्या धोरणांचे पालन करावे लागेल.

## मदत मिळवा

जर तुम्हाला अडचण येत असेल किंवा AI अ‍ॅप्स तयार करताना काही प्रश्न असतील, तर या ठिकाणी सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

तुमच्याकडे उत्पादनाबाबत अभिप्राय किंवा त्रुटी असल्यास येथे भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**तोडगा**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अपपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकारप्राप्त स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाचा वापर करून उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकांसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->