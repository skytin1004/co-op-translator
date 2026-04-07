# Co-op Translator

_Nemt automatiser og vedligehold oversættelser af dit uddannelsesmæssige GitHub-indhold på tværs af flere sprog, efterhånden som dit projekt udvikler sig._

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

### 🌐 Understøttelse af flere sprog

#### Understøttet af [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](./README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Foretrækker du at klone lokalt?**
>
> Dette repository inkluderer 50+ sprogoversættelser, hvilket øger downloadstørrelsen betydeligt. For at klone uden oversættelser, brug sparse checkout:
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
> Dette giver dig alt, hvad du behøver for at gennemføre kurset med en meget hurtigere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Oversigt

**Co-op Translator** hjælper dig med at lokalisere dit uddannelsesmæssige GitHub-indhold til flere sprog uden besvær.
Når du opdaterer dine Markdown-filer, billeder eller notebooks, bliver oversættelser automatisk synkroniseret, så dit indhold forbliver nøjagtigt og opdateret for lærende verden over.

Eksempel på, hvordan oversat indhold er organiseret:

![Example](../../imgs/translation-ex.png)

## Hvordan oversættelsesstatus håndteres

Co-op Translator håndterer oversat indhold som **versionsstyrede softwareartefakter**,  
ikke som statiske filer.

Værktøjet sporer tilstanden for oversat Markdown, billeder og notebooks
ved hjælp af **sprogafgrænset metadata**.

Denne opbygning gør det muligt for Co-op Translator at:

- Pålideligt opdage forældede oversættelser
- Behandle Markdown, billeder og notebooks konsekvent
- Skaler sikkert på tværs af store, hurtigbevægede, flersprogede repositories

Ved at modellere oversættelser som styrede artefakter,
stemmer oversættelsesarbejdsgange naturligt overens med moderne
praksis for softwareafhængigheder og artefaktstyring.

→ [Hvordan oversættelsesstatus håndteres](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Hurtig start

```bash
# Opret og aktiver et virtuelt miljø (anbefalet)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installer pakken
pip install co-op-translator
# Oversæt
translate -l "ko ja fr" -md
```

Docker:

```bash
# Hent det offentlige billede fra GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Kør med den aktuelle mappe monteret og .env angivet (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal opsætning

1. Sørg for at du har en understøttet Python-version (p.t. 3.10-3.12). I poetry (pyproject.toml) håndteres dette automatisk.
2. Opret en `.env`-fil ud fra skabelonen: [.env.template](../../.env.template)
3. Konfigurer en LLM-udbyder (Azure OpenAI eller OpenAI)
4. (Valgfrit) For billedoversættelse (`-img`), konfigurer Azure AI Vision
5. (Valgfrit) Du kan konfigurere flere sæt legitimationsoplysninger ved at duplikere variabler med suffikser som `_1`, `_2` osv. Alle variabler i et sæt skal have samme suffiks.
6. (Anbefalet) Ryd op i tidligere oversættelser for at undgå konflikter (fx `translations/`)
7. (Anbefalet) Tilføj en oversættelsessektion til din README ved at bruge [README sprogskabelon](./getting_started/README_languages_template.md)
8. Se: [Opsætning af Azure AI](./getting_started/set-up-azure-ai.md)

## Brug

Oversæt alle understøttede typer:

```bash
translate -l "ko ja"
```

Kun Markdown:

```bash
translate -l "de" -md
```

Markdown + billeder:

```bash
translate -l "pt" -md -img
```

Kun notebooks:

```bash
translate -l "zh" -nb
```

Flere flag: [Kommando reference](./getting_started/command-reference.md)

## Funktioner

- Automatisk oversættelse for Markdown, notebooks og billeder
- Holder oversættelser synkroniseret med kildeforandringer
- Virker lokalt (CLI) eller i CI (GitHub Actions)
- Bruger Azure OpenAI eller OpenAI; valgfri Azure AI Vision til billeder
- Bevarer Markdown-format og struktur

## Dokumentation

- [Kommando-linje guide](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions guide (Offentlige repositories & standardhemmeligheder)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions guide (Microsoft organisations repositories & organisation-niveau opsætning)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README sprogskabelon](./getting_started/README_languages_template.md)
- [Understøttede sprog](./getting_started/supported-languages.md)
- [Bidrag](./CONTRIBUTING.md)
- [Fejlfinding](./getting_started/troubleshooting.md)

### Microsoft-specifik guide
> [!NOTE]
> Kun for vedligeholdere af Microsoft “For Beginners” repositories.

- [Opdatering af “andre kurser” liste (kun for MS Beginners repositories)](./getting_started/update-other-courses.md)

## Støt os og frem læring globalt

Vær med til at revolutionere, hvordan uddannelsesindhold deles globalt! Giv [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støt vores mission om at nedbryde sprogbarrierer i læring og teknologi. Din interesse og dine bidrag gør en stor forskel! Bidrag af kode og forslag til funktioner er altid velkomne.

### Udforsk Microsoft uddannelsesindhold på dit sprog

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

## Video-præsentationer

👉 Klik på billedet nedenfor for at se på YouTube.

- **Open at Microsoft**: En kort 18-minutters introduktion og hurtig guide til, hvordan man bruger Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidrag

Dette projekt byder velkommen til bidrag og forslag. Er du interesseret i at bidrage til Azure Co-op Translator? Se venligst vores [CONTRIBUTING.md](./CONTRIBUTING.md) for retningslinjer om, hvordan du kan hjælpe med at gøre Co-op Translator mere tilgængelig.

## Bidragydere
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Adfærdskodeks

Dette projekt har vedtaget [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
For mere information se [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller  
kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) med yderligere spørgsmål eller kommentarer.

## Ansvarlig AI

Microsoft er forpligtet til at hjælpe vores kunder med at anvende vores AI-produkter ansvarligt, dele vores erfaringer og opbygge tillidsbaserede partnerskaber gennem værktøjer som Transparency Notes og Impact Assessments. Mange af disse ressourcer kan findes på [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsofts tilgang til ansvarlig AI er baseret på vores AI-principper om retfærdighed, pålidelighed og sikkerhed, privatliv og sikkerhed, inklusivitet, gennemsigtighed og ansvarlighed.

Store sprog-, billede- og talemodeller – som dem, der bruges i dette eksempel – kan potentielt opføre sig på måder, der er uretfærdige, upålidelige eller stødelige, hvilket kan forårsage skader. Se venligst [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for at blive informeret om risici og begrænsninger.

Den anbefalede tilgang til at mindske disse risici er at inkludere et sikkerhedssystem i din arkitektur, som kan opdage og forhindre skadelig adfærd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tilbyder et uafhængigt beskyttelseslag, som kan opdage skadeligt bruger- og AI-genereret indhold i applikationer og tjenester. Azure AI Content Safety inkluderer tekst- og billed-API’er, der giver dig mulighed for at opdage skadeligt materiale. Vi har også et interaktivt Content Safety Studio, der giver dig mulighed for at se, udforske og prøve eksempel-kode til at opdage skadeligt indhold på tværs af forskellige modaliteter. Følgende [quickstart-dokumentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) guider dig gennem, hvordan du foretager anmodninger til servicen.

Et andet aspekt at tage i betragtning er den samlede applikationsydelse. Ved multimodale og multimodel-applikationer betragter vi ydelse som, at systemet fungerer som du og dine brugere forventer, herunder ikke genererer skadelig output. Det er vigtigt at vurdere ydelsen af din samlede applikation ved hjælp af [genereringskvalitets- og risiko- og sikkerhedsmålinger](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere din AI-applikation i dit udviklingsmiljø ved hjælp af [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Uanset om du har et testdatasæt eller et mål, bliver dine generative AI-applikationsgenerationer kvantitativt målt med indbyggede evalueringer eller tilpassede evalueringer efter eget valg. For at komme i gang med prompt flow sdk til at evaluere dit system kan du følge [quickstart-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har udført en evalueringskørsel, kan du [visualisere resultaterne i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemærker

Dette projekt kan indeholde varemærker eller logoer for projekter, produkter eller tjenester. Autoriseret brug af Microsofts  
varemærker eller logoer er underlagt og skal følge  
[Microsofts Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Brug af Microsofts varemærker eller logoer i modificerede versioner af dette projekt må ikke skabe forvirring eller antyde Microsoft-sponsorering.  
Enhver brug af tredjeparts varemærker eller logoer er underlagt tredjepartens politikker.

## Få hjælp

Hvis du kører fast eller har spørgsmål om opbygning af AI-apps, så deltag i:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktfeedback eller fejl under opbygning, besøg:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiske oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets originale sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->