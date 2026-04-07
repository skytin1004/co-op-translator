# Co-op Translator

_आपल्या शैक्षणिक GitHub सामग्रीसाठी आपल्या प्रकल्पाच्या प्रगतीनुसार एकाधिक भाषांमध्ये अनुवाद सहज स्वयंचलित करा आणि राखा._

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

### 🌐 मल्टी-भाषा समर्थन

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारे समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](./README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **स्थानिकरित्या क्लोन करण्यास प्राधान्य देता का?**
>
> या रिपॉझिटरीमध्ये 50+ भाषा अनुवाद आहेत ज्यामुळे डाउनलोड आकार लक्षणीयरीत्या वाढतो. भाषा अनुवादांशिवाय क्लोन करण्यासाठी sparse checkout वापरा:
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
> यामुळे आपल्याला कोर्स पूर्ण करण्यासाठी आवश्यक सर्व काही खूप जलद डाउनलोड होईल.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## अवलोकन

**Co-op Translator** आपली शैक्षणिक GitHub सामग्री अनेक भाषांमध्ये सहजपणे स्थानिक करते.
जेव्हा आपण आपली Markdown फाइल्स, प्रतिमा किंवा नोटबुक्स अपडेट करता, तेव्हा अनुवाद स्वयंचलितपणे समक्रमित राहतात, ज्यामुळे आपल्या सामग्रीचा अचूकपणा आणि अद्ययावतता शिका-यांसाठी जगभर कायम राहते.

अनुवादित सामग्री कशी आयोजित केली जाते याचा उदाहरण:

![Example](../../imgs/translation-ex.png)

## अनुवाद स्थिती कशी व्यवस्थापित केली जाते

Co-op Translator अनुवादित सामग्रीला **आवृत्ती नियंत्रित सॉफ्टवेअर घटक** म्हणून व्यवस्थापित करतो,  
स्थिर फाइल्स म्हणून नाही.

हे उपकरण अनुवादित Markdown, प्रतिमा, आणि नोटबुक्सची स्थिती  
**भाषानिहाय मेटाडेटा** वापरून ट्रॅक करते.

हे डिझाइन Co-op Translator ला अनुमती देते:

- जुने झालेले अनुवाद विश्वसनीयपणे शोधणे
- Markdown, प्रतिमा, आणि नोटबुक्सचे सतत व्यवस्थापन
- मोठ्या, जलद गतीने बदलणाऱ्या, बहुभाषिक रिपॉझिटरीजमध्ये सुरक्षित स्केलिंग

अनुवादांना व्यवस्थापित घटक म्हणून मॉडेल करून,
अनुवाद कार्यप्रवाह नैसर्गिकरित्या आधुनिक  
सॉफ्टवेअर अवलंबित्व आणि घटक व्यवस्थापन पद्धतींसोबत जुळतात.

→ [अनुवाद स्थिती कशी व्यवस्थापित केली जाते](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## झटपट सुरूवात

```bash
# व्हर्च्युअल एन्व्हायर्नमेंट तयार करा आणि सक्रिय करा (शिफारस केली आहे)
python -m venv .venv
# विंडोज
.venv\Scripts\activate
# मॅकओएस/लिनक्स
source .venv/bin/activate
# पॅकेज स्थापित करा
pip install co-op-translator
# भाषांतर करा
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR मधून सार्वजनिक प्रतिमा ओढा
docker pull ghcr.io/azure/co-op-translator:latest
# वर्तमान फोल्डर माउंट करुन आणि .env प्रदान करुन चालवा (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## किमान सेटअप

1. आपल्याकडे समर्थित Python आवृत्ती आहे का ते तपासा (सध्या 3.10-3.12). कविता (pyproject.toml) मध्ये हे आपोआप हाताळले जाते.
2. टेम्पलेट वापरून `.env` फाइल तयार करा: [.env.template](../../.env.template)
3. एक LLM प्रदाता कॉन्फिगर करा (Azure OpenAI किंवा OpenAI)
4. (पर्यायी) प्रतिमा अनुवादासाठी (`-img`), Azure AI Vision कॉन्फिगर करा
5. (पर्यायी) आपण सोबत जोडलेल्या प्रत्ययांपासून `_1`, `_2`, इ. नावे असलेल्या अनेक क्रेडेन्शियल सेट कॉन्फिगर करू शकता. एका सेटमधील सर्व चलनांमध्ये समान प्रत्यय असणे आवश्यक आहे.
6. (शिफारस केलेले) कोणत्याही आधीच्या अनुवादांचे क्लीनअप करा जेणेकरून संघर्ष होणार नाही (उदा. `translations/`)
7. (शिफारस केलेले) आपल्या README मध्ये अनुवाद विभाग जोडा [README languages template](./getting_started/README_languages_template.md) वापरून
8. बघा: [Azure AI सेटअप करा](./getting_started/set-up-azure-ai.md)

## वापर

सर्व समर्थित प्रकार अनुवादित करा:

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

अधिक फलकांसाठी: [कमांड संदर्भ](./getting_started/command-reference.md)

## वैशिष्ट्ये

- Markdown, नोटबुक्स, आणि प्रतिमांसाठी स्वयंचलित अनुवाद
- स्त्रोत बदलांसोबत अनुवाद समक्रमित ठेवतो
- स्थानिकपणे (CLI) किंवा CI मध्ये (GitHub Actions) काम करतो
- Azure OpenAI किंवा OpenAI वापरतो; प्रतिमांसाठी पर्यायी Azure AI Vision
- Markdown फॉरमॅटिंग आणि रचना राखतो

## दस्तऐवज

- [कमांड-लाइन मार्गदर्शक](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions मार्गदर्शक (सार्वजनिक रिपॉझिटरीज व मानक गुप्तांक)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions मार्गदर्शक (Microsoft संघटन रिपॉझिटरीज व संघ-स्तरीय सेटअप)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README भाषांचा टेम्पलेट](./getting_started/README_languages_template.md)
- [समर्थित भाषा](./getting_started/supported-languages.md)
- [योगदान कसे द्यावे](./CONTRIBUTING.md)
- [समस्या निवारण](./getting_started/troubleshooting.md)

### Microsoft-विशिष्ट मार्गदर्शक
> [!NOTE]
> फक्त Microsoft “For Beginners” रिपॉझिटरीजसाठी देखभाल करणाऱ्यांसाठी.

- [“इतर कोर्सेस” सूची अद्ययावत करणे (फक्त MS Beginners रिपॉझिटरीजसाठी)](./getting_started/update-other-courses.md)

## आम्हाला समर्थन द्या आणि जागतिक शिक्षणाला प्रोत्साहन द्या

आमच्यासोबत सामील व्हा आणि शैक्षणिक सामग्री जागतिक स्तरावर कशी सामायिक केली जाते याला क्रांतिकारक ठरवा! [Co-op Translator](https://github.com/azure/co-op-translator) ला GitHub वर ⭐ देऊन शिका-यांसाठी आणि तंत्रज्ञानासाठी भाषा अडथळे तोडण्याच्या आमच्या ध्येयाला पाठिंबा द्या. आपली आवड आणि योगदान मोठा फरक आणतात! कोड योगदान आणि वैशिष्ट्य सुचना नेहमीच स्वागतार्ह आहेत.

### आपल्या भाषेत Microsoft शैक्षणिक सामग्रीचा शोध घ्या

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

👉 YouTube वर पाहण्यासाठी खालील प्रतिमेवर क्लिक करा.

- **Open at Microsoft**: Co-op Translator कसा वापरायचा याचा 18 मिनिटांचा संक्षिप्त परिचय आणि जलद मार्गदर्शक.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

हा प्रकल्प योगदान आणि सूचना स्वागत करतो. Azure Co-op Translator मध्ये योगदान देण्यास उत्सुक आहात का? कृपया आमच्या [CONTRIBUTING.md](./CONTRIBUTING.md) पाहा ज्यात Co-op Translator अधिक प्रवेशयोग्य कसा करायचा यासाठी मार्गदर्शक दिले आहेत.

## योगदानकर्ता
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचार संहिता

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारला आहे.  
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा  
कोणत्याही अतिरिक्त प्रश्नांसाठी किंवा टिप्पण्यांसाठी [opencode@microsoft.com](mailto:opencode@microsoft.com) शी संपर्क साधा.

## जबाबदार AI

Microsoft आमच्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरण्यात मदत करण्यासाठी, आमच्या शिकवणुका शेअर करण्यासाठी, आणि Transparency Notes आणि Impact Assessments सारख्या साधनांच्या माध्यमातून विश्वासाधारित भागीदारी तयार करण्यासाठी वचनबद्ध आहे. या संसाधनांपैकी बरेच काही येथे उपलब्ध आहेत: [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoft चे जबाबदार AI चे दृष्टीकोन आमच्या AI तत्त्वांवर आधारित आहे ज्यात न्याय्यपणा, विश्वासार्हता आणि सुरक्षा, गोपनीयता आणि सुरक्षितता, समावेशिता, पारदर्शकता आणि जबाबदारी यांचा समावेश आहे.

मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा, आणि भाषण मॉडेल्स - उदाहरणार्थ या सॅम्पलमध्ये वापरले जाणारे - कधीकधी अन्यायकारक, अविश्वसनीय किंवा आक्षेपार्ह वर्तन करू शकतात, ज्यामुळे नुकसान होऊ शकते. कृपया [Azure OpenAI सेवा Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) तपासा ज्यामुळे जोखमी आणि मर्यादांबद्दल माहिती मिळेल.

या जोखमी कमी करण्यासाठी शिफारस केलेला दृष्टिकोन म्हणजे आपल्या आर्किटेक्चरमध्ये अशा सुरक्षा प्रणालीचा समावेश करणे जी हानिकारक वर्तन ओळखू आणि प्रतिबंधित करू शकेल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) स्वतंत्र संरक्षणाचं स्तर प्रदान करते, जे अनुप्रयोगांमध्ये आणि सेवांमध्ये हानिकारक वापरकर्त्याद्वारे निर्मित आणि AI वापरून निर्मित सामग्री शोधू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा API आहेत जे हानिकारक सामग्री शोधू शकतात. आमच्याकडे interactive Content Safety Studio देखील आहे, जे विविध प्रकारच्या माध्यमांमधील हानिकारक सामग्री शोधण्यासाठी नमुना कोड पाहण्यास, तपासण्यास आणि वापरून पाहण्यास अनुमती देते. खालील [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) आपल्याला सेवा वापरण्यासाठी विनंती कशी करावी हे शिकवते.

आणखी एक बाब लक्षात घेण्याजोगी म्हणजे एकूण अनुप्रयोग कार्यक्षमता. बहु-माध्यमीय आणि बहु-मॉडेल अनुप्रयोगांमध्ये, कार्यक्षमता म्हणजे प्रणाली आपण आणि आपल्या वापरकर्त्यांनी अपेक्षित प्रमाणे काम करणे, ज्यात हानिकारक आउटपुट तयार न होणे समाविष्ट आहे. आपला एकूण अनुप्रयोगाचा कार्यप्रदर्शन [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून मोजणे महत्त्वाचे आहे.

आपण आपल्या AI अनुप्रयोगाचे मूल्यमापन आपल्या विकास वातावरणात [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) वापरून करू शकता. चाचणी डेटासेट किंवा उद्दीष्ट दिल्यास, आपल्या जनरेटिव्ह AI अनुप्रयोगांच्या आवृत्त्यांचे संख्यात्मक मूल्यांकन अंगभूत मूल्यांकनकर्ता किंवा आपल्या पसंतीनुसार सानुकूल मूल्यांकनकर्ता वापरून केले जाते. system चे मूल्यमापन करण्यासाठी prompt flow sdk वापरण्यास प्रारंभ करण्यासाठी, आपण [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) याचा अवलंब करू शकता. एकदा आपण मूल्यमापन प्रक्रिया पार पडल्यावर, आपण [Azure AI Studio मध्ये निकालांचे दृश्य पाहू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ट्रेडमार्क

या प्रकल्पात प्रकल्प, उत्पादन, किंवा सेवा यांचे ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft चे ट्रेडमार्क किंवा लोगो वापरणे अधिकृत आहे आणि ते [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) यांचे अनुसरण करणे आवश्यक आहे.  
Microsoft चे ट्रेडमार्क किंवा लोगो या प्रकल्पाच्या सुधारित आवृत्त्यांमध्ये वापरल्यास गोंधळ किंवा Microsoft ची प्रायोजकता दर्शवू नये.  
तृतीय पक्ष ट्रेडमार्क किंवा लोगो वापर संबंधित तृतीय पक्षांच्या धोरणांनुसारच असावे.

## मदत मिळवा

जर अडचण आली किंवा AI अॅप्स बांधण्यात काही प्रश्न असतील, तर सामील व्हा:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

उत्पादनाविषयी अभिप्राय किंवा अॅप बांधताना त्रुटी असल्यास भेट द्या:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्न करतो, पण कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा असत्यता असू शकतात. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकारप्राप्त स्रोत मानला जावा. महत्त्वपूर्ण माहितीसाठी व्यावसायिक मानवी अनुवाद शिफारस केली जाते. या अनुवादाच्या वापरातून उद्भवणाऱ्या कोणत्याही गैरसमजुतीं किंवा चुकीच्या समजुतींसाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->