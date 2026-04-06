# Co-op Translator

_మీ విద్యా GitHub కంటెంట్ పలు భాషల్లో మీ ప్రాజెక్ట్ మార్పులు జరుగుతుండగా సులభంగా అనువాదాలను ఆటోమేటిగ రూపంలో నిర్వహించండి._

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

### 🌐 బహుభాషా మద్దతు

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) ద్వారా మద్దతు పొందబడినవి

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](./README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> ** స్థానికంగా క్లోన్ చేయాలని ఇష్టపడితే?**
>
> ఈ రిపోజిటరీలో 50+ భాషా అనువాదాలు ఉన్నాయి, ఇవి డౌన్లోడ్ సైజ్‌ను గణనీయంగా పెంచుతాయి. అనువాదాలు లేకుండా క్లోన్ చేయడానికి sparse checkout ఉపయోగించండి:
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
> ఇదివరకే కోర్సును పూర్తి చేసుకోవడానికి మీకు అవసరమైనదన్నిటిని మరింత వేగంగా డౌన్లోడ్ చేస్తుంది.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## అవలోకనం

**Co-op Translator** మీ విద్యా GitHub కంటెంట్‌ను సులభంగా పలు భాషల్లో స్థానీకరించడంలో సహాయపడుతుంది.  
మీ Markdown ఫైళ్లు, చిత్రాలు లేదా నోటుబుక్స్‌ను మీరు నవీకరించినప్పుడు, అనువాదాలు ఆటోమేటిగానే సింక్‌లో ఉంటాయి, ప్రపంచవ్యాప్తంగా ఉన్న విద్యార్ధులకు మీ కంటెంట్ ఖచ్చితంగా మరియు తాజా గా ఉంటుంది.

అనువాద కంటెంట్ ఎలా ఏర్పాటు చేయబడిందో ఉదాహరణ:

![Example](../../translated_images/te/translation-ex.0c8aa6a7ee0aad2b.webp)

## అనువాద స్థితిని ఎలా నిర్వహిస్తారు

Co-op Translator అనువదించిన కంటెంట్‌ను **వర్షన్ చేయబడిన సాఫ్ట్వేర్ ఆర్టిఫాక్ట్స్** గా నిర్వహిస్తుంది,  
స్థిరమైన ఫైళ్లుగా కాదు.

ఈ టూల్ అనువాదమైన Markdown, చిత్రాలు, నోటుబుక్స్ స్థితిని  
**భాష-పరిమితి మెటాడేటా** ఉపయోగించి ట్రాక్ చేస్తుంది.

ఈ రూపకల్పన Co-op Translator కి అనుమతిస్తుంది:

- పాతగనువదించిన అనువాదాలను నమ్మకంగా గుర్తించడం  
- Markdown, చిత్రాలు, నోటుబుక్స్‌ను సమానంగా వ్యవహరించడం  
- పెద్ద, వేగంగా మారే, బహుభాషా రిపోజిటరీలను సురక్షితంగా మేనేజు చేయడం

అనువాదాలను నిర్వహిత ఆర్టిఫాక్ట్స్‌గా మోడల్ చేయడం ద్వారా,  
అనువాద వర్క్‌ఫ్లోలు సహజంగానే ఆధునిక  
సాఫ్ట్వేర్ డిపెండెన్సీ మరియు ఆర్టిఫాక్ట్ నిర్వహణ పద్ధతులతో సరిపోతాయి.

→ [అనువాద స్థితి ఎలా నిర్వహించబడుతుందో](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## వేగవంతమైన ప్రారంభం

```bash
# ఒక వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించి సక్రియం చేయండి (సిఫార్సు చేయబడింది)
python -m venv .venv
# విండోస్
.venv\Scripts\activate
# మాక్‌ఓఎస్/లినక్స్
source .venv/bin/activate
# ప్యాకేజ్‌ను ఇన్‌స్టాల్ చేయండి
pip install co-op-translator
# అనువదించండి
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR నుండి పబ్లిక్ ఇమేజ్ ని తీసుకోండి
docker pull ghcr.io/azure/co-op-translator:latest
# ప్రస్తుత ఫోల్డర్ మౌంట్ చేసి మరియు .env అందించి నడపండి (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## కనిష్ఠ సెటప్

1. మీరు మద్దతు పొందిన Python వెర్షన్ ఉందని నిర్ధారించుకోండి (ప్రస్తుతం 3.10-3.12). poetry (pyproject.toml) లో ఇది ఆటోమేటిగ ఉంటుంది.  
2. టెంప్లేట్ ఉపయోగించి `.env` ఫైల్ క్రియేట్ చేయండి: [.env.template](../../.env.template)  
3. ఒక LLM ప్రొవైడర్ (Azure OpenAI లేదా OpenAI) సర్దుబాటు చేయండి  
4. (ఐచ్ఛికం) ఇమేజ్ అనువాదానికి (`-img`) Azure AI Vision సర్దుబాటు చేయండి  
5. (ఐచ్ఛికం) వేరువేరు క్రెడెన్షియల్ సెట్‌లు అవసరమైతే suffix లను ఉపయోగించి తరలింపులు చేయండి (`_1`, `_2` వంటి). ఒక సెట్‌లో గల అన్ని వేరియబుల్స్ కు ఒకే suffix ఉండాలి.  
6. (సిఫార్సు) యాజమాన్యం సంబంధ సమస్యలు నివారించడానికి పూర్వ అనువాదాలను క్లియర్ చేయండి (ఉదా: `translations/`)  
7. (సిఫార్సు) README కి అనువాద సెక్షన్ జోడించండి [README languages template](./getting_started/README_languages_template.md) ఉపయోగించి  
8. చూడండి: [Azure AI సెటప్](./getting_started/set-up-azure-ai.md)

## ఉపయోగం

అన్ని మద్దతు పొందిన రకాల్ని అనువదించండి:

```bash
translate -l "ko ja"
```

Markdown మాత్రమే:

```bash
translate -l "de" -md
```

Markdown + చిత్రాలు:

```bash
translate -l "pt" -md -img
```

పట్టికలు మాత్రమే:

```bash
translate -l "zh" -nb
```

ఇంకా ఫ్లగ్‌ల కోసం: [కమాండ్ సూచిక](./getting_started/command-reference.md)

## లక్షణాలు

- Markdown, పట్టికలు, చిత్రాల ఆటోమేటిక్ అనువాదం  
- మూల మార్పులతో అనువాదాలను సమకాలీకరణలో ఉంచటం  
- నిమ్నస్థాయిలో (CLI) లేదా CIలో (GitHub Actions) పనిచేయుట  
- Azure OpenAI లేదా OpenAI ఉపయోగించడం; చిత్రాలకై ఐచ్ఛిక Azure AI Vision  
- Markdown ఫార్మాటింగ్ మరియు నిర్మాణాన్ని పరిరక్షించడం

## డాక్యుమెంటేషన్

- [కమాండ్‌లైన్ గైడ్](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions గైడ్ (పబ్లిక్ రిపోధారాలు & స్టాండర్డ్ సీక్రెట్స్)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions గైడ్ (Microsoft ఆర్గనైజేషన్ రిపోధారాలు & ఆర్గ్-లెవెల్ సెటప్‌లు)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README భాషల టెంప్లేట్](./getting_started/README_languages_template.md)  
- [మద్దతు పొందిన భాషలు](./getting_started/supported-languages.md)  
- [కాంట్రిబ్యూటింగ్](./CONTRIBUTING.md)  
- [ట్రబుల్షూటింగ్](./getting_started/troubleshooting.md)

### Microsoft- నిర్దిష్ట గైడ్
> [!NOTE]
> Microsoft “For Beginners” రిపోధారాల నిర్వాహకులకు మాత్రమే.

- [“ఇతర కోర్సులు” జాబితాను నవీకరించడం (MS Beginners రిపోధారాల కోసం మాత్రమే)](./getting_started/update-other-courses.md)

## మాకు మద్దతు ఇస్తూ ఆగ్ని పనితీరును ప్రేరేపించండి

ప్రపంచవ్యాప్తంగా విద్యా కంటెంట్ పంచుకునే విధానాన్ని విప్లవాత్మకంగా మార్చడంలో మాతో చేరండి!  
[Co-op Translator](https://github.com/azure/co-op-translator) ను GitHub లో ఒక ⭐ ఇవ్వండి మరియు భాషా అడ్డంకులను తొలగించి నేర్చుకోవడంలో సహాయం చేయండి.  
మీ ఆసక్తి మరియు సహకారం గొప్ప ప్రభావాన్ని చూపిస్తాయి! కోడ్ సహాయాలు మరియు ఫీచర్ సూచనలు ఎల్లప్పుడూ స్వాగతం.

### మీ భాషలో Microsoft విద్యా కంటెంట్‌ను అన్వేషించండి

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

## వీడియో ప్రეზంటేషన్స్

👉 YouTube లో చూడడానికి దిగువ చిత్రం పై క్లిక్ చేయండి.

- **Microsoft వద్ద ఓపెన్**: Co-op Translator ను ఎలా ఉపయోగించాలో 18 నిమిషాల సంక్షిప్త పరిచయం మరియు వేగవంతమైన గైడ్.

  [![Open at Microsoft](../../translated_images/te/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## సహకారం

ఈ ప్రాజెక్ట్ కి సహకారాలు మరియు సూచనలు స్వాగతం. Azure Co-op Translator కి సహకరించడానికి ఆసక్తి ఉంటే, దయచేసి [CONTRIBUTING.md](./CONTRIBUTING.md) ను చూడండి. ఇందులో Co-op Translator ను మరింత అందుబాటులో చేయడానికి మీరు ఎలా సహాయం చేయగలరో వివరించబడింది.

## భాగస్వాములు
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ప్రవర్తన నియమాలు

ఈ ప్రాజెక్ట్ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ని అంగీకరించింది.  
మరిన్ని వివరాలకు [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) చూడండి లేదా  
ఏవైనా అదనపు ప్రశ్నలు లేదా వ్యాఖ్యల కోసం [opencode@microsoft.com](mailto:opencode@microsoft.com) ను సంప్రదించండి.

## బాధ్యతాయుత AI

Microsoft మా కస్టమర్లకు మా AI ఉత్పత్తులను బాధ్యతాయుతంగా ఉపయోగించుకోవడంలో సహాయపడడానికి, మా అనుభవాలను పంచుకోవడానికి, Transparency Notes మరియు Impact Assessments వంటి టూల్స్ ద్వారా విశ్వాసంపై ఆధారపడిన భాగస్వామ్యాలను నిర్మించడంలో కట్టుబడి ఉంది. ఈ వనరులలో చాలా వాటిని [https://aka.ms/RAI](https://aka.ms/RAI) వద్ద కనుగొనవచ్చు.  
బాధ్యతాయుత AIకు Microsoft యొక్క దృష్టికోణం న్యాయం, నమ్మకযোগ্যత మరియు భద్రత, గోప్యత మరియు భద్రత, సమగ్రత, పారదర్శకత, మరియు బాధ్యతాయుతత అనే AI సూత్రాలపై ఆధారపడింది.

ఈ నమూనాలో ఉపయోగించినట్టు పెద్ద స్థాయి న్యాచురల్ లాంగ్వేజ్, ఇమేజ్, మరియు స్పీచ్ మోడల్స్ - అవి అన్యాయం, నమ్మక లేకపోవడం లేదా అపవిత్రంగా ప్రవర్తించవచ్చు, తద్వారా హానికరంగా మారవచ్చు. ప్రమాదాలు మరియు పరిమితుల గురించి తెలుసుకోవడానికి [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ని సలహా తీసుకోండి.

ఈ ప్రమాదాలను తగ్గించడానికి సిఫార్సు చేయబడిన విధానం మీ స్థాపనలో హానికర వ్యవరాన్ని గుర్తించి అరికట్టగల భద్రతా వ్యవస్థను చేర్చడం. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) స్వతంత్ర రక్షణ పొరని అందిస్తుంది, ఇది అనువర్తనాలు మరియు సేవలలో హానికరమైన వినియోగదారు-తయారుచేసిన మరియు AI-తయారుచేసిన వాస్తవాలను గుర్తించగలదు. Azure AI Content Safety టెక్స్ట్ మరియు ఇమేజ్ APIs ని కలిగి ఉంది, ఇవి హానికర విషయాలను గుర్తించడానికి అనుమతిస్తాయి. మేము পাশাপাশি ఇంటరాక్టివ్ Content Safety Studio కలిగి ఉండి, ఇది హానికర విషయాలను వివిధ మోడాలిటీలలో గుర్తించడానికి ఉదాహరణ కోడ్ ను చూడటానికి, అవలోకనం చేసుకోవడానికి మరియు పరీక్షించడానికి అవకాశాన్ని ఇస్తుంది. ఈ క్రింది [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) సేవకు అభ్యర్థనలు పంపే విధానాన్ని 안내 చేస్తుంది.

మరొక అంశం మొత్తం అనువర్తన పనితీరు. బహుముఖ మరియు బహుమోడల్ అనువర్తనాలతో, మా అభిప్రాయం ప్రకారం పనితీరు అంటే మీరు మరియు మీ వినియోగదారులు అనుకుంటున్నట్లుగా వ్యవస్థ పని చేయడం, హానికరమైన అవుట్పుట్లను ఉత్పత్తి చేయడం కలపకుండా ఉండటం. మీ మొత్తం అనువర్తనం పనితీరును [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) ఉపయోగించి అంచనా వేయడం ముఖ్యం.

మీ AI అనువర్తనాన్ని అభివృద్ధి వాతావరణంలో [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ఉపయోగించి మూల్యాంకనం చేయవచ్చు. ఒక టెస్ట్ డేటాసెట్ లేదా లక్ష్యాన్ని తీసుకుంటే, మీ జనరేటివ్ AI అనువర్తన ఉత్పత్తులను ఏర్పాటు చేసిన వ్యవస్థలోని బిల్ట్-ఇన్ లేదా మీ ఎంచుకున్న కస్టమ్ మూల్యాంకకులతో సంఖ్యాత్మకంగా కొలవబడతాయి. మీ వ్యవస్థను మూల్యాంకనం చేయడానికి prompt flow sdk తో ప్రారంభించడానికి, మీరు [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ను అనుసరించవచ్చు. ఒకదాన్ని ఒకపుడు మూల్యాంకన నిర్వహణను పూర్తి చేసిన తర్వాత, మీరు [Azure AI Studio లో ఫలితాలను వీక్షించవచ్చు](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## ట్రేడ్‌మార్కులు

ఈ ప్రాజెక్ట్ ప్రాజెక్టులు, ఉత్పత్తులు లేదా సేవల ట్రేడ్‌మార్కులు లేదా లోగోలను కలిగి ఉండవచ్చు. Microsoft ట్రేడ్‌మార్కులు లేదా లోగోలను అనుమతితో ఉపయోగించడం [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) నిబంధనలకు లబ్ధిపడుతుంది మరియు ఆ విధంగా మాత్రమే జరుగాలి.  
Microsoft ట్రేడ్‌మార్కులు లేదా లోగోలను ఈ ప్రాజెక్ట్ మార్పులు చేసిన సంస్కరణలలో ఉపయోగించడం Microsoft స్పాన్సర్షిప్ ఉందని గందరగోళం కలిగించకూడదు లేదా సూచించకూడదు.  
మూడవ పక్ష ట్రేడ్‌మార్కులు లేదా లోగోలను ఉపయోగించడం ఆ మూడవ పక్ష ప్రయత్నాల విధానాల ఆధీనంలో ఉంటుంది.

## సహాయం పొందడం

మీరు ఇబ్బంది పడితే లేదా AI యాప్స్ నిర్మాణం గురించి ఏవైనా ప్రశ్నలు ఉంటే, చేరండి:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ప్రమాదాల సమాచారం లేదా నిర్మాణం సమయంలో లోపాలు ఉంటే సందర్శించండి:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**డిస్క్లైమర్**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మనము ఖచ్చితత్వం కోసం ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలలో లోపాలు లేదా తప్పిదాలు ఉండవచ్చు అని దయచేసి గమనించండి. స్వదేశీ భాషలో ఉన్న అసలు పత్రం అధికారిక మూలం‌గా పరిగణించబడాలి. కీలకమైన సమాచారం కోసం, నిపుణుల మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదాన్ని ఉపయోగించడం ద్వారా సంభవించే ఏవైనా అపార్థాలు లేదా తప్పుదారులపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->