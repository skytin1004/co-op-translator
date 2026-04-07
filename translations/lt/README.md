# Co-op Translator

_Lengvai automatizuokite ir palaikykite vertimus savo edukaciniam GitHub turiniui keliomis kalbomis, kai jūsų projektas vystosi._

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

### 🌐 Daugiakalbė palaikymas

#### Palaikoma su [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Norite klonuoti vietoje?**
>
> Šiame saugykloje yra daugiau nei 50 kalbų vertimų, kurie žymiai padidina atsisiuntimo dydį. Norėdami klonuoti be vertimų, naudokite ribotą checkout:
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
> Tai suteikia jums viską, ko reikia kursui užbaigti, daug greičiau atsisiunčiant.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Apžvalga

**Co-op Translator** padeda lengvai lokalizuoti jūsų edukacinį GitHub turinį keliomis kalbomis.  
Kai atnaujinate savo Markdown failus, paveikslėlius ar užrašų knygeles, vertimai automatiškai sinchronizuojami, užtikrinantys, kad jūsų turinys išliktų tikslus ir atnaujintas mokiniams visame pasaulyje.

Pavyzdys, kaip organizuojamas išverstas turinys:

![Example](../../imgs/translation-ex.png)

## Kaip valdomas vertimo būsenos valdymas

Co-op Translator valdo išverstą turinį kaip **versijuotus programinės įrangos artefaktus**,  
o ne kaip statinius failus.

Įrankis seka išverstų Markdown, paveikslėlių ir užrašų būseną  
naudodamas **kalbai pritaikytą metaduomenų sistemą**.

Šis dizainas leidžia Co-op Translator:

- Patikimai aptikti pasenusius vertimus
- Nuosekliai elgtis su Markdown, paveikslėliais ir užrašų knygelėmis
- Saugaus mastelio palaikymą didelėse, sparčiai besivystančiose daugakalbėse saugyklose

Modeliuodama vertimus kaip valdomus artefaktus,  
vertimų darbo eiga natūraliai dera su šiuolaikinėmis  
programinės įrangos priklausomybių ir artefaktų valdymo praktikomis.

→ [Kaip valdomas vertimo būsenos valdymas](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Greitas pradžios vadovas

```bash
# Sukurkite ir suaktyvinkite virtualią aplinką (rekomenduojama)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Įdiekite paketą
pip install co-op-translator
# Išverskite
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pasiimkite viešą atvaizdą iš GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Vykdykite su pritvirtinta esama aplanko vieta ir pateiktu .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalus nustatymas

1. Įsitikinkite, kad turite palaikomą Python versiją (šiuo metu 3.10-3.12). Poetry (pyproject.toml) tai valdo automatiškai.
2. Sukurkite `.env` failą naudodami šabloną: [.env.template](../../.env.template)
3. Konfigūruokite vieną LLM teikėją (Azure OpenAI arba OpenAI)
4. (Pasirinktinai) Vaizdų vertimui (`-img`) konfigūruokite Azure AI Vision
5. (Pasirinktinai) Galite sukonfigūruoti kelis kredencialų rinkinius, dubliuodami kintamuosius su priesagomis, tokiomis kaip `_1`, `_2` ir pan. Visi kintamieji rinkinyje turi turėti tą pačią priesagą.
6. (Rekomenduojama) Išvalykite ankstesnius vertimus, kad išvengtumėte konfliktų (pavyzdžiui, `translations/`)
7. (Rekomenduojama) Pridėkite vertimų skyrių į savo README naudodami [README kalbų šabloną](./getting_started/README_languages_template.md)
8. Žiūrėkite: [Azure AI nustatymas](./getting_started/set-up-azure-ai.md)

## Naudojimas

Versti visų palaikomų tipų turinį:

```bash
translate -l "ko ja"
```

Tik Markdown:

```bash
translate -l "de" -md
```

Markdown + paveikslėliai:

```bash
translate -l "pt" -md -img
```

Tik užrašų knygelės:

```bash
translate -l "zh" -nb
```

Daugiau parinkčių: [Komandų nuoroda](./getting_started/command-reference.md)

## Funkcijos

- Automatizuotas vertimas Markdown, užrašų knygelių ir paveikslėlių turiniui
- Išlaiko vertimus sinchronizuotus su šaltinio pakeitimais
- Veikia vietoje (CLI) arba CI (GitHub Actions)
- Naudoja Azure OpenAI arba OpenAI; pasirinktinai Azure AI Vision paveikslėliams
- Išlaiko Markdown formatavimą ir struktūrą

## Dokumentacija

- [Komandinės eilutės vadovas](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions vadovas (viešos saugyklos ir standartiniai slaptieji raktai)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions vadovas (Microsoft organizacijos saugyklos ir organizacijos lygio nustatymai)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README kalbų šablonas](./getting_started/README_languages_template.md)
- [Palaikomos kalbos](./getting_started/supported-languages.md)
- [Prisidėjimas](./CONTRIBUTING.md)
- [Trikčių šalinimas](./getting_started/troubleshooting.md)

### Microsoft specifinis vadovas
> [!NOTE]
> Tik Microsoft „Pradedantiesiems“ saugyklų prižiūrėtojams.

- [„Kitų kursų“ sąrašo atnaujinimas (tik MS Pradedančiųjų saugykloms)](./getting_started/update-other-courses.md)

## Palaikykite mus ir skatinkite pasaulinį mokymąsi

Prisijunkite prie mūsų revoliucijoje, kaip edukacinis turinys dalijamasi visame pasaulyje! Duokite [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ GitHub ir palaikykite mūsų misiją pašalinti kalbinius barjerus mokymesi ir technologijose. Jūsų susidomėjimas ir indėlis daro didelį poveikį! Kodo indėliai ir funkcijų pasiūlymai visada laukiami.

### Ištirkite Microsoft edukacinį turinį savo kalba

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generatyvus AI pradedantiesiems naudojant .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generatyvus AI pradedantiesiems](https://github.com/microsoft/generative-ai-for-beginners)
- [Generatyvus AI pradedantiesiems naudojant Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML pradedantiesiems](https://aka.ms/ml-beginners)
- [Duomenų mokslas pradedantiesiems](https://aka.ms/datascience-beginners)
- [AI pradedantiesiems](https://aka.ms/ai-beginners)
- [Kibernetinis saugumas pradedantiesiems](https://github.com/microsoft/Security-101)
- [Web kūrimas pradedantiesiems](https://aka.ms/webdev-beginners)
- [IoT pradedantiesiems](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Vaizdo pristatymai

👉 Spustelėkite žemiau esantį paveikslėlį, norėdami žiūrėti YouTube.

- **Open at Microsoft**: Trumpa 18 minučių įžanga ir greitas gidų, kaip naudoti Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prisidėjimas

Šis projektas laukia jūsų indėlių ir pasiūlymų. Norite prisidėti prie Azure Co-op Translator? Prašome peržiūrėti mūsų [CONTRIBUTING.md](./CONTRIBUTING.md), kad sužinotumėte, kaip galite padėti padaryti Co-op Translator prieinamesnį.

## Dalyviai
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba
kreipkitės el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com) su bet kokiais papildomais klausimais ar pastabomis.

## Atsakingas Dirbtinis Intelektas

Microsoft įsipareigoja padėti mūsų klientams atsakingai naudoti mūsų DI produktus, dalintis savo patirtimi ir kurti pasitikėjimu grįstas partnerystes, naudodama tokias priemones kaip Skaidrumo pastabos ir Poveikio vertinimai. Daugelį šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft atsakingo DI požiūris grindžiamas mūsų DI principais: teisingumu, patikimumu ir saugumu, privatumu ir apsauga, įtrauktimi, skaidrumu ir atsakingumu.

Didelio masto natūralios kalbos, vaizdų ir kalbos modeliai - pavyzdžiui, naudojami šiame pavyzdyje - gali pasireikšti neteisingu, nepatikimu ar įžeidžiančiu elgesiu, sukeldami žalą. Prašome susipažinti su [Azure OpenAI paslaugos Skaidrumo pastaba](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad sužinotumėte apie rizikas ir apribojimus.

Rekomenduojamas būdas mažinti šias rizikas – įtraukti į savo architektūrą saugos sistemą, galinčią aptikti ir užkirsti kelią žalingam elgesiui. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, gebantį aptikti žalingą vartotojų ir DI generuojamą turinį programėlėse ir paslaugose. Azure AI Content Safety apima teksto ir vaizdų API, leidžiančias aptikti žalingą medžiagą. Taip pat turime interaktyvų Content Safety Studio, leidžiantį peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą, skirtą žalingo turinio aptikimui skirtingose modalinėse srityse. Ši [greitojo starto dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) padės jums pateikti užklausas paslaugai.

Kitas svarbus aspektas yra bendras programėlės našumas. Multi-modaliose ir daugmodelių programėlėse, našumas reiškia, kad sistema veikia taip, kaip tikitės jūs ir jūsų naudotojai, įskaitant nekurti žalingų rezultatų. Svarbu įvertinti bendrą jūsų programėlės našumą naudodami [generavimo kokybės bei rizikos ir saugumo metrikas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Galite įvertinti savo DI programėlę savo kūrimo aplinkoje naudodami [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testinį duomenų rinkinį arba tikslą, jūsų generatyvių DI programėlės generacijų kokybė kiekybiškai vertinama su įmontuotais vertintojais arba pasirinktiniais vertintojais. Norėdami pradėti naudoti prompt flow sdk savo sistemos vertinimui, galite sekti [greitojo starto vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Vykdę vertinimo procesą, galite [vizualizuoti rezultatus Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Prekės ženklai

Šis projektas gali turėti projektų, produktų ar paslaugų prekių ženklus arba logotipus. Leidžiamas Microsoft
prekių ženklų arba logotipų naudojimas yra reglamentuojamas ir privalo atitikti
[Microsoft prekių ženklų ir prekės ženklų naudojimo taisykles](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Naudojant Microsoft prekių ženklus ar logotipus modifikuotose šio projekto versijose neturi kilti painiavos ar reikšti Microsoft rėmimą.
Bet koks trečiųjų šalių prekių ženklų ar logotipų naudojimas yra reglamentuojamas atitinkamų trečiųjų šalių politikos.

## Pagalba

Jei įstrigote arba turite klausimų apie DI programėlių kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite produktų atsiliepimų arba statymo klaidų, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatizuoti vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus žmogiškas vertimas. Mes neatsakome už jokius nesusipratimus ar klaidų interpretacijas, kylančias naudojant šį vertimą.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->