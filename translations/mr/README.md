<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T11:58:44+00:00",
  "source_file": "README.md",
  "language_code": "mr"
}
-->
# को-ऑप ट्रान्सलेटर

_तुमच्या शैक्षणिक GitHub कंटेंटचे अनुवाद अनेक भाषांमध्ये सहजपणे ऑटोमेट करा आणि जागतिक प्रेक्षकांपर्यंत पोहोचा._

### 🌐 बहुभाषिक समर्थन

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) द्वारे समर्थित

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[अरबी](../ar/README.md) | [बंगाली](../bn/README.md) | [बल्गेरियन](../bg/README.md) | [बर्मी (म्यानमार)](../my/README.md) | [चिनी (सरलीकृत)](../zh/README.md) | [चिनी (परंपरागत, हाँगकाँग)](../hk/README.md) | [चिनी (परंपरागत, मकाऊ)](../mo/README.md) | [चिनी (परंपरागत, तैवान)](../tw/README.md) | [क्रोएशियन](../hr/README.md) | [झेक](../cs/README.md) | [डॅनिश](../da/README.md) | [डच](../nl/README.md) | [एस्टोनियन](../et/README.md) | [फिन्निश](../fi/README.md) | [फ्रेंच](../fr/README.md) | [जर्मन](../de/README.md) | [ग्रीक](../el/README.md) | [हिब्रू](../he/README.md) | [हिंदी](../hi/README.md) | [हंगेरीयन](../hu/README.md) | [इंडोनेशियन](../id/README.md) | [इटालियन](../it/README.md) | [जपानी](../ja/README.md) | [कोरियन](../ko/README.md) | [लिथुआनियन](../lt/README.md) | [मलय](../ms/README.md) | [मराठी](./README.md) | [नेपाली](../ne/README.md) | [नायजेरियन पिजिन](../pcm/README.md) | [नॉर्वेजियन](../no/README.md) | [फारसी (फारसी)](../fa/README.md) | [पोलिश](../pl/README.md) | [पोर्तुगीज (ब्राझील)](../br/README.md) | [पोर्तुगीज (पोर्तुगाल)](../pt/README.md) | [पंजाबी (गुरमुखी)](../pa/README.md) | [रोमानियन](../ro/README.md) | [रशियन](../ru/README.md) | [सर्बियन (सिरिलिक)](../sr/README.md) | [स्लोव्हाक](../sk/README.md) | [स्लोव्हेनियन](../sl/README.md) | [स्पॅनिश](../es/README.md) | [स्वाहिली](../sw/README.md) | [स्वीडिश](../sv/README.md) | [टागालोग (फिलिपिनो)](../tl/README.md) | [तमिळ](../ta/README.md) | [थाई](../th/README.md) | [तुर्की](../tr/README.md) | [युक्रेनियन](../uk/README.md) | [उर्दू](../ur/README.md) | [व्हिएतनामी](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ओळख

**Co-op Translator** तुम्हाला तुमचे शैक्षणिक GitHub कंटेंट वेगवेगळ्या भाषांमध्ये पटकन अनुवादित करण्याची सुविधा देते, त्यामुळे जागतिक प्रेक्षकांपर्यंत सहज पोहोचता येते. जेव्हा तुम्ही Markdown फाइल्स, प्रतिमा किंवा Jupyter नोटबुक्स अपडेट करता, तेव्हा अनुवाद आपोआप समक्रमित केले जातात, त्यामुळे तुमचे शैक्षणिक GitHub कंटेंट आंतरराष्ट्रीय वापरकर्त्यांसाठी नेहमी ताजे आणि संबंधित राहते.

Co-op Translator शैक्षणिक GitHub कंटेंटचे अनुवाद कसे व्यवस्थापित करते ते पहा:

![उदाहरण](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.mr.png)

## जलद सुरुवात

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

## किमान सेटअप

- [.env.template](../../.env.template) वापरून `.env` तयार करा
- एक LLM प्रदाता कॉन्फिगर करा (Azure OpenAI किंवा OpenAI)
- प्रतिमांसाठी अनुवाद (`-img`) करायचा असल्यास Azure AI Vision देखील सेट करा
- शिफारस: इतर टूल्सने तयार केलेले अनुवाद असल्यास, आधी ते काढून टाका, म्हणजे गोंधळ टाळता येईल (उदा: `translations/`).
- शिफारस: [README languages template](./README_languages_template.md) वापरून README मध्ये translations विभाग जोडा
- पहा: [Azure AI सेटअप करा](./getting_started/set-up-azure-ai.md)

## वापर

सर्व समर्थित प्रकारांचे अनुवाद करा:

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

अधिक फ्लॅग्स: [Command reference](./getting_started/command-reference.md)

## वैशिष्ट्ये

- Markdown, नोटबुक्स आणि प्रतिमांसाठी स्वयंचलित अनुवाद
- मूळ कंटेंटमध्ये बदल झाल्यास अनुवाद आपोआप समक्रमित राहतात
- स्थानिक (CLI) किंवा CI (GitHub Actions) मध्ये वापरता येते
- Azure OpenAI किंवा OpenAI वापरते; प्रतिमांसाठी ऐच्छिक Azure AI Vision
- Markdown चे स्वरूप आणि रचना जतन करते

## दस्तऐवजीकरण

- [कमांड-लाइन मार्गदर्शिका](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions मार्गदर्शिका (सार्वजनिक रेपॉजिटरी आणि स्टँडर्ड सीक्रेट्स)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions मार्गदर्शिका (Microsoft संस्था रेपॉजिटरी आणि संस्था-स्तरीय सेटअप)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [समर्थित भाषा](./getting_started/supported-languages.md)
- [समस्या निवारण](./getting_started/troubleshooting.md)

## आमचे समर्थन करा आणि जागतिक शिक्षणाला चालना द्या

शैक्षणिक कंटेंट जागतिक स्तरावर शेअर करण्याच्या क्रांतीत आमच्यात सामील व्हा! [Co-op Translator](https://github.com/azure/co-op-translator) ला GitHub वर ⭐ द्या आणि शिक्षण व तंत्रज्ञानातील भाषेच्या अडथळ्यांना दूर करण्याच्या आमच्या मिशनला पाठिंबा द्या. तुमची रुची आणि योगदान यामुळे मोठा फरक पडतो! कोड योगदान आणि फीचर सुचना नेहमीच स्वागतार्ह आहेत.

### तुमच्या भाषेत Microsoft चे शैक्षणिक कंटेंट एक्सप्लोर करा

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

Co-op Translator बद्दल अधिक जाणून घ्या आमच्या सादरीकरणांमधून _(खालील प्रतिमेवर क्लिक करून YouTube वर पहा.)_:

- **Open at Microsoft**: Co-op Translator वापरण्याबद्दल १८ मिनिटांची थोडक्यात ओळख आणि जलद मार्गदर्शक.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.mr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## योगदान

या प्रकल्पात योगदान आणि सूचना स्वागतार्ह आहेत. Azure Co-op Translator मध्ये योगदान द्यायचे आहे का? कृपया [CONTRIBUTING.md](./CONTRIBUTING.md) पहा, ज्यात Co-op Translator अधिक प्रवेशयोग्य कसा बनवता येईल याबद्दल मार्गदर्शक दिले आहे.

## योगदानकर्ते

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## आचारसंहिता

या प्रकल्पाने [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) स्वीकारली आहे.
अधिक माहितीसाठी [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) पहा किंवा
[opencode@microsoft.com](mailto:opencode@microsoft.com) वर तुमचे प्रश्न किंवा प्रतिक्रिया पाठवा.

## जबाबदार AI

Microsoft आमच्या ग्राहकांना आमची AI उत्पादने जबाबदारीने वापरता यावीत यासाठी, आमचे अनुभव शेअर करण्यासाठी आणि Transparency Notes आणि Impact Assessments सारख्या साधनांद्वारे विश्वासावर आधारित भागीदारी निर्माण करण्यासाठी वचनबद्ध आहे. यातील बरीच संसाधने [https://aka.ms/RAI](https://aka.ms/RAI) येथे उपलब्ध आहेत.
Microsoft चा जबाबदार AI कडे पाहण्याचा दृष्टिकोन आमच्या AI तत्त्वांवर आधारित आहे: न्याय, विश्वासार्हता आणि सुरक्षितता, गोपनीयता आणि सुरक्षा, सर्वसमावेशकता, पारदर्शकता आणि जबाबदारी.

मोठ्या प्रमाणावर नैसर्गिक भाषा, प्रतिमा आणि भाषण मॉडेल्स - जसे की या सॅम्पलमध्ये वापरले जातात - कधीकधी अन्यायकारक, अविश्वसनीय किंवा आक्षेपार्ह वर्तन करू शकतात, ज्यामुळे हानी होऊ शकते. कृपया [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) वाचा, ज्यात जोखमी आणि मर्यादा दिल्या आहेत.

या जोखमी कमी करण्यासाठी शिफारस केलेला उपाय म्हणजे तुमच्या आर्किटेक्चरमध्ये एक सुरक्षा प्रणाली समाविष्ट करणे, जी हानिकारक वर्तन ओळखू आणि थांबवू शकेल. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) एक स्वतंत्र सुरक्षा स्तर देते, जी वापरकर्त्यांनी किंवा AI ने तयार केलेल्या हानिकारक कंटेंटला ओळखू शकते. Azure AI Content Safety मध्ये मजकूर आणि प्रतिमा API आहेत, जे हानिकारक सामग्री ओळखू शकतात. आमच्याकडे Content Safety Studio देखील आहे, जिथे तुम्ही विविध प्रकारच्या हानिकारक कंटेंटचे नमुने पाहू, एक्सप्लोर करू आणि कोड वापरून तपासू शकता. पुढील [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) मध्ये सेवा वापरण्याचे मार्गदर्शन आहे.


एक महत्त्वाचा मुद्दा म्हणजे संपूर्ण ॲप्लिकेशनची कार्यक्षमता. मल्टी-मोडल आणि मल्टी-मॉडेल ॲप्लिकेशन्समध्ये, कार्यक्षमता म्हणजे प्रणालीने आपल्याला आणि आपल्या वापरकर्त्यांना अपेक्षित असलेली कामगिरी करणे, त्यात अपायकारक आउटपुट तयार न करणे याचा समावेश होतो. आपल्या संपूर्ण ॲप्लिकेशनची कार्यक्षमता [generation quality आणि risk आणि safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) वापरून तपासणे महत्त्वाचे आहे.

आपण आपल्या विकासाच्या वातावरणात [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) वापरून आपल्या AI ॲप्लिकेशनचे मूल्यांकन करू शकता. चाचणी डेटासेट किंवा टार्गेट दिल्यास, आपल्या जनरेटिव्ह AI ॲप्लिकेशनच्या आउटपुटचे मोजमाप अंगभूत किंवा आपल्या पसंतीच्या कस्टम इव्हॅल्युएटर्सने केले जाते. आपल्या प्रणालीचे मूल्यांकन करण्यासाठी prompt flow sdk वापरण्यास सुरुवात करण्यासाठी आपण [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) अनुसरू शकता. एकदा आपण मूल्यांकन रन पूर्ण केल्यावर, आपण [Azure AI Studio मध्ये निकालांचे व्हिज्युअलायझेशन करू शकता](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ट्रेडमार्क

या प्रकल्पात प्रकल्प, उत्पादने किंवा सेवांसाठी ट्रेडमार्क किंवा लोगो असू शकतात. Microsoft चे ट्रेडमार्क किंवा लोगो अधिकृतपणे वापरण्यासाठी [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) चे पालन करणे आवश्यक आहे.
या प्रकल्पाच्या बदललेल्या आवृत्त्यांमध्ये Microsoft ट्रेडमार्क किंवा लोगो वापरल्याने गोंधळ होऊ नये किंवा Microsoft प्रायोजकत्वाचा संकेत मिळू नये.
तृतीय-पक्ष ट्रेडमार्क किंवा लोगो वापरणे त्या तृतीय-पक्षाच्या धोरणांनुसार असते.

## मदतीसाठी

जर तुम्हाला अडचण आली किंवा AI ॲप्स तयार करताना काही प्रश्न असतील, तर सामील व्हा:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

जर तुम्हाला उत्पादनाबद्दल अभिप्राय द्यायचा असेल किंवा ॲप तयार करताना त्रुटी आढळल्या, तर भेट द्या:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**अस्वीकरण**:
हे दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील दस्तऐवज हा अधिकृत स्रोत मानावा. अत्यावश्यक माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर करून झालेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.