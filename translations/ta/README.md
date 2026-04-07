# Co-op Translator

_உங்கள் கல்வி GitHub உள்ளடக்கங்களை பல மொழிகளில் எளிதில் தானாக மொழி மாற்றங்களையும் பராமரிக்கவும், உங்கள் திட்டம் மாறிக்கொண்டிருக்கும்போது._

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

### 🌐 பல மொழி ஆதரவு

#### [Co-op Translator](https://github.com/Azure/Co-op-Translator) மூலம் ஆதரிக்கப்படுகிறது

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](./README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **உள்ளூரில் கிளோன் செய்ய விரும்புகிறீர்களா?**
>
> இந்த ரெப்போசிடரி 50+ மொழி மொழிபெயர்ப்புகளை உள்ளடக்கியதால் பதிவிறக்கும் அளவை மிகவும் பெரிதாக்குகிறது. மொழிபெயர்ப்புகளின்றி கிளோன் செய்ய sparse checkout பயன்படுத்தவும்:
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
> இது பாடத்திட்டத்தை முடிக்க தேவையான அனைத்தையும் மிகவும் விரைவான பதிவிறக்கம் மூலம் உங்களுக்கு தரும்.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## மேலோட்டம்

**Co-op Translator** உங்களுக்கு உங்கள் கல்வி GitHub உள்ளடக்கங்களை பல மொழிகளில் எளிதில் உள்ளூராக்க உதவும்.
நீங்கள் உங்கள் Markdown கோப்புகள், படங்கள் அல்லது நோட்புக்க்களை புதுப்பிக்கும் போது, மொழிபெயர்ப்புகள் தானாக ஒத்திசைத்திருப்பதை உறுதிசெய்கிறது, இவ்வாறு உலகளாவிய மாணவர்களுக்கு உங்கள் உள்ளடக்கம் துல்லியமாகவும், புதுப்பிக்கப்பட்டதாகவும் இருக்கும்.

மொழிபெயர்க்கப்பட்ட உள்ளடக்கம் எவ்வாறு அமைக்கப்படுகிறது என்ற ஒரு உதாரணம்:

![Example](../../imgs/translation-ex.png)

## மொழிபெயர்ப்பு நிலை எப்படி நிர்வகிக்கப்படுகிறது

Co-op Translator மொழிபெயர்க்கப்பட்ட உள்ளடக்கத்தை **பதிப்புச்செய்யப்பட்ட மென்பொருள் உருவாக்குதல்களாக** நிர்வகிக்கிறது,  
நிரந்தர கோப்புகளாக அல்ல.

இந்த கருவி மொழிபெயர்க்கப்பட்ட Markdown, படங்கள், நோட்புக் நிலையை
**மொழி-களஞ்சியத் தகவலுடன்** கண்காணிக்கிறது.

இந்த வடிவமைப்பு Co-op Translator இற்கு உதவுகிறது:

- பழைய மொழிபெயர்ப்புகளை நம்பகமாக கண்டறிதல்
- Markdown, படங்கள், மற்றும் நோட்புக் களை ஒரே மாதிரியான முறையில் கையாளுதல்
- வேகமாக நகரும், பெரிய மற்றும் பல மொழி உள்ள கன்டெய்னர் நிர்வாகத்தில் பாதுகாப்பாக விரிவாக்கம்

மொழிபெயர்ப்புகளை நிர்வகிக்கப்படும் உருவாக்குதல்களாக வடிவமைச்சதால்,
மொழிபெயர்ப்பு பணிகள் சமகால
மென்பொருள் சார்பு மற்றும் உருவாக்குதல் நடைமுறைகளை இயல்பான முறையில் பின்பற்றுகின்றன.

→ [மொழிபெயர்ப்பு நிலை எப்படி நிர்வகிக்கப்படுகிறது](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## விரைவான தொடக்கம்

```bash
# ஒரு மெய்நிகர் சூழலை உருவாக்கி செயல்படுத்தவும் (பரிந்துரைக்கப்படுகிறது)
python -m venv .venv
# விண்டோஸ்
.venv\Scripts\activate
# மேக்OS/லினக்ஸ்
source .venv/bin/activate
# தொகுதியை நிறுவவும்
pip install co-op-translator
# மொழிபெயர்க்கவும்
translate -l "ko ja fr" -md
```

Docker:

```bash
# GHCR இல் இருந்து பொதுப்படத்தை எடு
docker pull ghcr.io/azure/co-op-translator:latest
# தற்போதைய கோப்புறை மவுண்ட் செய்யப்பட்டு .env கொடுக்கப்பட்டபடி இயக்கு (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## குறைந்தபட்ச அமைப்பு

1. உங்களிடம் ஆதரிக்கப்படும் Python பதிப்பு (தற்போது 3.10-3.12) இருப்பதை உறுதி செய்யுங்கள். poetry (pyproject.toml) இல் இது தானாக கையாளப்படுகிறது.
2. டெம்ப்ளேட் பயன்படுத்தி `.env` கோப்பை உருவாக்குங்கள்: [.env.template](../../.env.template)
3. ஒரு LLM வழங்கியாளரை ஒருமுறை அமைக்கவும் (Azure OpenAI அல்லது OpenAI)
4. (விருப்பமானது) பட மொழிபெயர்ப்புக்கு (`-img`), Azure AI Vision ஐ அமைக்கவும்
5. (விருப்பமானது) `_1`, `_2` போன்ற சப்ஸ்பீக்ஸ்களை பயன்படுத்தி பல போதுமான அங்கீகார தொகுதிகளை அமைக்கலாம். ஒரு தொகுதியில் அனைத்து மாறிலிகளும் அதே சப்ஸ்பீக்ஸை பகிர வேண்டும்.
6. (சிபார்சுகள்) முன் மொழிபெயர்ப்புகளை அழிந்து ஒத்திசைவற்றதைக் கையிருத்தல் (எ.கா., `translations/`)
7. (சிபார்சுகள்) உங்கள் README உள்நிலை மொழிபெயர்க்கும் பகுதியை [README languages template](./getting_started/README_languages_template.md) பயன்படுத்தி சேர்க்கவும்
8. பாருங்கள்: [Azure AI அமைப்பு](./getting_started/set-up-azure-ai.md)

## பயன்படுத்தும் முறை

அடையாளம் செய்யப்பட்ட அனைத்து ஆதரவு வகைகளையும் மொழிபெயர்க்கவும்:

```bash
translate -l "ko ja"
```

Markdown மட்டும்:

```bash
translate -l "de" -md
```

Markdown + படங்கள்:

```bash
translate -l "pt" -md -img
```

பட்டியல்கள் மட்டும்:

```bash
translate -l "zh" -nb
```

மேலும் கொடிகள்: [Command reference](./getting_started/command-reference.md)

## அம்சங்கள்

- Markdown, நோட்பூக்கள் மற்றும் படங்களுக்கான தானியங்கி மொழிபெயர்ப்பு
- மூல மாற்றங்களுடன் மொழிபெயர்ப்புகளை ஒத்திசைக்கிறது
- உள்ளூரிலும் (CLI) அல்லது CI (GitHub Actions) இலும் இயங்குகிறது
- Azure OpenAI அல்லது OpenAI பயன்படுத்துகிறது; படங்களுக்கு விருப்பமாக Azure AI Vision
- Markdown வடிவமைப்பையும் அமைப்பையும் பாதுகாக்கிறது

## ஆவணங்கள்

- [கமாண்ட்-லைன் வழிகாட்டு](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub செயலிகள் வழிகாட்டு (பொது ரெப்போசிடரிகள் & நிலையான ரகசியங்கள்)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub செயலிகள் வழிகாட்டு (Microsoft அமைப்பு ரெப்போசிடரிகள் & அமைப்புப் நிலை அமைப்புகள்)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README மொழி டெம்ப்ளேட்](./getting_started/README_languages_template.md)
- [ஆதரவு மொழிகள்](./getting_started/supported-languages.md)
- [பங்களிப்பு](./CONTRIBUTING.md)
- [சிக்கல் தீர்க்கும் வழிகாட்டு](./getting_started/troubleshooting.md)

### Microsoft-க்கு சிறந்த வழிகாட்டு
> [!NOTE]
> Microsoft “For Beginners” ரெப்போசிடரிகளை பராமரிப்பவர்களுக்கே.

- [“மற்ற பாடத்திட்டங்கள்” பட்டியலை புதுப்பித்தல் (MS Beginners ரெப்போசிடரிகளுக்கு மட்டும்)](./getting_started/update-other-courses.md)

## எங்களுக்கு ஆதரவாகவும், உலகளாவிய கற்றலையும் ஊக்கவும்

கல்வி உள்ளடக்கம் உலகளாவியமாவ முறையில் பகிரப்படுவதை மாற்றுவோம்! [Co-op Translator](https://github.com/azure/co-op-translator) GitHub இல் ⭐ தரவும், கற்றலும் தொழில்நுட்பமுமுள்ள மொழி தடைகளை உடைக்க இது ஒரு முக்கிய பணி என்பதை ஆதரிக்கவும். உங்கள் ஆர்வம் மற்றும் பங்களிப்புகள் பெரிய தாக்கங்களை ஏற்படுத்துகின்றன! குறியீட்டு பங்களிப்புகள் மற்றும் அம்ச பரிந்துரைகள் எப்போதும் வரவேற்கப்படுகின்றன.

### Microsoft கல்வி உள்ளடக்கத்தை உங்கள் மொழியில் ஆராய்க

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

## வீடியோ ஆவணங்கள்

👉 YouTube இல் பார்க்க கீழே உள்ள படத்தை அழுத்தவும்.

- **Microsoft இல் திறக்கவும்**: Co-op Translator பயன்பாட்டை விரைவாக அறிமுகம் செய்யும் 18 நிமிட குறும்படம்.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## பங்களிப்புகள்

இந்த திட்டம் பங்களிப்பும் பரிந்துரைகளையும் வரவேற்கிறது. Azure Co-op Translator யில் பங்களிக்க விருப்பர்கள், தயவுசெய்து எங்களது [CONTRIBUTING.md](./CONTRIBUTING.md) ஐப் பாருங்கள், எப்படி Co-op Translator ஐ மேலும் அணுகக்கூடியதாக மாற்றலாம் என்பதைப் பற்றி வழிகாட்டுதல்கள் உள்ளன.

## பங்களிப்பாளர்கள்
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## நடத்துமுறை விதிகள்

இந்த திட்டம் [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) ஐ ஏற்றுக்கொண்டுள்ளது. மேலும் தகவலுக்கு [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ஐ பார்க்கவும் அல்லது கூடுதல் கேள்விகள் அல்லது கருத்துக்களுக்கு [opencode@microsoft.com](mailto:opencode@microsoft.com) ஐ தொடர்பு கொள்ளவும்.

## பொறுப்பான AI

Microsoft எங்கள் AI தயாரிப்புகளை பொறுப்புடன் பயன்படுத்த எங்கள் வாடிக்கையாளர்களுக்கு உதவுவதைப் பணியாளர் நியமனம் செய்திருக்கிறது, எங்கள் கற்றல்களை பகிர்ந்து, Transparency Notes மற்றும் Impact Assessments போன்ற கருவிகளின் மூலம் நம்பகமான கூட்டுதொடர்புகளை உருவாக்குகிறது. இந்த வளங்கள் பலவற்றையும் [https://aka.ms/RAI](https://aka.ms/RAI) இல் காணலாம். Microsoft-ன் பொறுப்பான AI அணுகுமுறை நீதி, நம்பகத்தன்மை மற்றும் பாதுகாப்பு, தனியுரிமை மற்றும் பாதுகாப்பு, உள்ளடக்கம், வெளிப்படைமை மற்றும் கணக்காய்வேற்பு ஆகிய AI கொள்கைகளில் அடிப்படையாக்கப்பட்டுள்ளது.

இந்த மாதிரியில் பயன்படுத்தப்படும் பெரிய அளவிலான இயற்கை மொழி, படம் மற்றும் உரை மாதிரிகள் - அவை நியாயமில்லாத, நம்பிக்கையில்லாத அல்லது திடீரென அவமதிப்பான முறையில் நடந்துகொள்ளக்கூடும், இதனால் தீமைகள் ஏற்படலாம். ஆபத்துக்களும் வரம்புகளும் பற்றி அறிவதற்கு [Azure OpenAI சேவை Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) ஐ ஆலோசிக்கவும்.

இந்த ஆபத்துக்களை குறைக்க பரிந்துரைக்கப்படும் முறையானது உங்கள் கட்டமைப்பில் பளுவிழுப்பு நடந்துகொள்ளாததும் தீங்கான நடத்தை தடுக்கும் பாதுகாப்பு அமைப்பை உள்ளடக்குவதே ஆகும். [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ஒரு தனித்தனி பாதுகாப்பு அடுக்கை வழங்குகிறது, பயன்பாடுகள் மற்றும் சேவைகளில் தீங்கு தரும் பயனர் மற்றும் AI உருவாக்கிய உள்ளடக்கத்தை கண்டறியக்கூடியது. Azure AI Content Safety உரை மற்றும் பட API-களை உடையது, அதுவும் தீங்கு விளைவிக்கக்கூடிய உள்ளடக்கத்தை கண்டறிய உதவுகிறது. பல்வேறு முறைமைகளின் நீக்கம் சம்பந்தமான தீங்கு உள்ளடக்கத்தைக் கண்டறிய உதவுவதற்கான నమூனிக் குறியீடுகள் பார்க்க, சோதிக்க மற்றும் முயற்சிக்க இந்த இன்டரാക்டிவ் Content Safety Studio உள்ளது. சேவைக்கு கோரிக்கை செய்ய இந்த [quickstart ஆவணம்](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) உங்களை வழிநடத்தும்.

மற்றொரு அம்சம் முழுமையான பயன்பாட்டு செயல்திறனை கணக்கில் கொள்வதே ஆகும். பல-முறைமையாகவும் பல மாதிரிகளாகவும் செயல்படும் பயன்பாடுகளில், செயல்திறன் என்பது உங்கள் மற்றும் உங்கள் பயனர்களின் எதிர்பார்ப்பைப் பூர்த்தி செய்ய உரிய முறையில் செயல்படுவதாக கருதியுள்ளது, அதாவது தீங்கு விளைவிக்கக்கூடிய வெளியீடுகளை உருவாக்காமல் இருக்குதல். உங்கள் முழுமையான பயன்பாட்டின் செயல்திறன் மதிப்பீடு செய்ய [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) பயன்படுத்துவது முக்கியம்.

உங்கள் AI பயன்பாட்டை உங்கள் வளர்ப்பு சூழலில் [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) மூலம் மதிப்பீடு செய்யலாம். ஒரு சோதனை தரவுத்தொகையும் இலக்‌ஷியுமானவையும் கொடுக்கப்படும்போது, உங்கள் உருவாக்கும் AI பயன்பாட்டின் உருவாக்கங்கள் உள்நிலை மதிப்பீட்டாளர்களோ அல்லது உங்கள் விருப்பமான தனிப்பயன் மதிப்பீட்டாளர்களோ மூலம் மதிப்பிடப்படும். உங்கள் அமைப்பை மதிப்பீடு செய்ய prompt flow sdk உடன் தொடங்க, [quickstart கையேட்டை](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) பின்தொடரவும். மதிப்பீட்டு ஓட்டம் செயல்படுத்தியதற்கு பிறகு, [Azure AI Studio இல் முடிவுகளை காட்சி படுத்தலாம்](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## வர்த்தக அடையாளங்கள்

இந்த திட்டத்தில் திட்டங்கள், தயாரிப்புகள் அல்லது சேவைகள் தொடர்பான வர்த்தக அடையாளங்கள் அல்லது லோகோக்கள் இருக்கலாம். Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்களின் அனுமதிக்கப்பட்ட பயன்படுத்தல் [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) என்பதை பின்பற்ற வேண்டும். Microsoft வர்த்தக அடையாளங்கள் அல்லது லோகோக்கள் திருத்தப்பட்ட பதிப்புகளில் பயன்படுத்தப்படுவதை Microsoft ஆதரவு என்று தவறாக ஊகிக்க கூடாது அல்லது குழப்பம் ஏற்படுத்த கூடாது. மூன்றாம் பக்கம் வர்த்தக அடையாளங்கள் அல்லது லோகோக்களின் பயன்பாடு அந்த மூன்றாம் பக்கம் கொள்கைகளுக்கு உட்பட்டது.

## உதவி பெறுதல்

AI அப் தயாரிப்பில் சிக்கலானால் அல்லது கேள்விகள் இருந்தால், இணையுங்கள்:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

தயாரிப்புக்கு பின்னூட்டம் அல்லது பிழைகள் உள்ளனவேண்டுமானால்:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**விரோதத்தைத் தவிர்ப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) மூலம் மொழிபெயர்க்கப்பட்டதாகும். நாங்கள் துல்லியத்துக்காக உழைக்கிறோம் என்றாலும், தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனியுங்கள். சுருக்கமான ஆவணம் அதன் உள்ளடக்க மொழியில் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்படுத்தலால் ஏற்படும் எந்தவொரு தவறான புரிதலும் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பேற்க மாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->