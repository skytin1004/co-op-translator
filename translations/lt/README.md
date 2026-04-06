# Co-op Translator

_Paprasta automatizuoti ir palaikyti vertimus jūsų edukaciniam GitHub turiniui keliose kalbose, kaip vystosi jūsų projektas._

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

#### Palaikoma [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](./README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Mėgstate klonuoti lokaliai?**
>
> Ši saugykla apima 50+ kalbų vertimus, kurie ženkliai padidina atsisiuntimo dydį. Norėdami klonuoti be vertimų, naudokite sparse checkout:
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
> Tai suteiks viską, ko reikia kursui užbaigti, stipriai spartinant atsisiuntimą.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Apžvalga

**Co-op Translator** leidžia lengvai lokalizuoti jūsų edukacinį GitHub turinį į daugelį kalbų.  
Kai atnaujinate Markdown failus, paveikslėlius ar užrašų knygutes, vertimai automatiškai sinchronizuojami, užtikrindami, kad turinys visada būtų tikslus ir atnaujintas mokiniams visame pasaulyje.

Vertimo turinio organizavimo pavyzdys:

![Example](../../translated_images/lt/translation-ex.0c8aa6a7ee0aad2b.webp)

## Kaip valdomas vertimo būsena

Co-op Translator valdo išverstą turinį kaip **versijuotus programinės įrangos artefaktus**,  
o ne kaip statinius failus.

Įrankis seka išverstų Markdown, paveikslėlių ir užrašų knygelių būseną  
naudodamas **kalbai pritaikytą metaduomenų lauką**.

Toks dizainas leidžia Co-op Translator:

- Patikimai aptikti pasenusį vertimą  
- Vienodai tvarkyti Markdown, paveikslėlius ir užrašų knygeles  
- Saugiai išplėsti veikimą didelėse, sparčiai besikeičiančiose, daugiakalbėse saugyklose

Vertimus modeliuojant kaip valdomus artefaktus,  
vertimo darbo eiga natūraliai suderinama su šiuolaikinėmis  
programinės įrangos priklausomybių ir artefaktų valdymo praktikomis.

→ [Kaip valdomas vertimo būsena](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Greitas pradėjimas

```bash
# Sukurkite ir aktyvuokite virtualią aplinką (rekomenduojama)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Įdiekite paketą
pip install co-op-translator
# Išversti
translate -l "ko ja fr" -md
```

Docker:

```bash
# Atsisiųskite viešą atvaizdą iš GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Paleiskite su prijungtu esamu aplanku ir pateiktu .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalus nustatymas

1. Įsitikinkite, kad turite palaikomą Python versiją (šiuo metu 3.10-3.12). Poetry (pyproject.toml) tai valdo automatiškai.
2. Sukurkite `.env` failą naudodami šabloną: [.env.template](../../.env.template)
3. Konfigūruokite vieną LLM tiekėją (Azure OpenAI arba OpenAI)
4. (Pasirinktinai) Vaizdų vertimui (`-img`), konfigūruokite Azure AI Vision
5. (Pasirinktinai) Galite konfigūruoti kelis kredencialų rinkinius, dubliuodami kintamuosius su priesagomis kaip `_1`, `_2` ir t. t. Visi kintamieji rinkinyje turi turėti tą patį priesagą.
6. (Rekomenduojama) Išvalykite ankstesnius vertimus, kad išvengtumėte konfliktų (pvz., `translations/`)
7. (Rekomenduojama) Įtraukite vertimo sekciją į savo README naudodami [README kalbų šabloną](./getting_started/README_languages_template.md)
8. Žr.: [Azure AI nustatymas](./getting_started/set-up-azure-ai.md)

## Naudojimas

Versti visus palaikomus tipus:

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

- Automatizuotas vertimas Markdown, užrašų knygelių ir paveikslėlių  
- Vertimai visuomet sinchronizuojami su šaltinio pakeitimais  
- Veikia lokaliai (CLI) arba CI (GitHub Actions)  
- Naudoja Azure OpenAI arba OpenAI; pasirenkama Azure AI Vision vaizdams  
- Išlaiko Markdown formatavimą ir struktūrą

## Dokumentacija

- [Komandinės eilutės vadovas](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions vadovas (Viešos saugyklos ir įprasti slaptažodžiai)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions vadovas (Microsoft organizacijos saugyklos ir organizacijos lygio nustatymai)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README kalbų šablonas](./getting_started/README_languages_template.md)
- [Palaikomos kalbos](./getting_started/supported-languages.md)
- [Prisidėjimas prie projekto](./CONTRIBUTING.md)
- [Problemos sprendimas](./getting_started/troubleshooting.md)

### Microsoft specifinis vadovas
> [!NOTE]
> Tik Microsoft "Pradedantiesiems" saugyklų prižiūrėtojams.

- [„Kitų kursų“ sąrašo atnaujinimas (tik MS Pradedančiųjų saugykloms)](./getting_started/update-other-courses.md)

## Palaikykite mus ir skatinkite globalų mokymąsi

Prisijunkite prie mūsų ir revoliucionizuokite, kaip edukacinis turinys dalijamasi visame pasaulyje! Įvertinkite [Co-op Translator](https://github.com/azure/co-op-translator) GitHub su ⭐ ir palaikykite mūsų misiją sugriauti kalbos barjerus mokymesi bei technologijose. Jūsų susidomėjimas ir indėlis turi didelę reikšmę! Kodo indėliai ir funkcijų pasiūlymai visada laukiami.

### Atraskite Microsoft edukacinį turinį savo kalba

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

## Vaizdo pristatymai

👉 Spustelėkite žemiau esantį paveikslėlį, kad žiūrėtumėte „YouTube“.

- **Open at Microsoft**: Trumpas 18 minučių pristatymas ir greitas vadovas, kaip naudoti Co-op Translator.

  [![Open at Microsoft](../../translated_images/lt/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prisidėjimas

Šis projektas laukia jūsų indėlio ir pasiūlymų. Norite prisidėti prie Azure Co-op Translator? Prašome peržiūrėti mūsų [CONTRIBUTING.md](./CONTRIBUTING.md), kad sužinotumėte, kaip galite padėti padaryti Co-op Translator prieinamą visiems.

## Dalyviai
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Elgesio kodeksas

Šis projektas priėmė [Microsoft atvirojo kodo elgesio kodeksą](https://opensource.microsoft.com/codeofconduct/).
Daugiau informacijos rasite [Elgesio kodekso DUK](https://opensource.microsoft.com/codeofconduct/faq/) arba
kreipkitės el. paštu [opencode@microsoft.com](mailto:opencode@microsoft.com) dėl papildomų klausimų ar pastabų.

## Atsakingas dirbtinis intelektas

Microsoft įsipareigoja padėti savo klientams atsakingai naudoti mūsų DI produktus, dalintis mūsų patirtimi ir kurti pasitikėjimu paremtas partnerystes naudodama įrankius, tokius kaip Skaidrumo pastabos ir Poveikio vertinimai. Daugelį šių išteklių rasite adresu [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft atsakingo DI požiūris remiasi mūsų DI principais: sąžiningumu, patikimumu ir saugumu, privatumu ir saugumu, įtrauktimi, skaidrumu ir atsakomybe.

Didelio masto natūralios kalbos, vaizdų ir kalbos modeliai – tokie, kaip šio pavyzdžio – gali elgtis neteisingai, nepatikimai ar įžeidžiančiai, dėl ko gali kilti žala. Prašome susipažinti su [Azure OpenAI paslaugos Skaidrumo pastaba](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), kad sužinotumėte apie rizikas ir apribojimus.

Rekomenduojamas rizikos mažinimo būdas yra įtraukti saugumo sistemą į savo architektūrą, kuri gali aptikti ir užkirsti kelią kenksmingam elgesiui. [Azure AI turinio sauga](https://learn.microsoft.com/azure/ai-services/content-safety/overview) suteikia nepriklausomą apsaugos sluoksnį, galintį aptikti kenksmingą vartotojų ir DI sukurtą turinį programose ir paslaugose. Azure AI turinio sauga apima tekstų ir vaizdų API, leidžiančias aptikti kenksmingą medžiagą. Taip pat turime interaktyvų Turinio saugos studiją, leidžiančią peržiūrėti, tyrinėti ir išbandyti pavyzdinį kodą, skirtą kenksmingam turiniui aptikti skirtingose modalitetuose. Ši [greitojo paleidimo dokumentacija](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) padės jums atlikti užklausas paslaugai.

Kitas svarbus aspektas yra bendras programos našumas. Naudojant daugiamodelines ir daugiaprostorines programas, našumu laikome tai, kad sistema veikia taip, kaip tikitės jūs ir jūsų vartotojai, įskaitant ir kenksmingų rezultatų neviešinimą. Svarbu įvertinti bendrą programos našumą naudojant [generavimo kokybės ir rizikos bei saugumo metrikas](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Galite įvertinti savo DI programą savo kūrimo aplinkoje naudodami [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Turėdami testinį duomenų rinkinį arba tikslą, jūsų generatyvios DI programos generavimai kiekybiškai matuojami su įmontuotais vertintojais arba pasirinktinais vertintojais, kuriuos pasirenkate. Norėdami pradėti dirbti su prompt flow sdk savo sistemos vertinimui, galite sekti [greitojo paleidimo vadovą](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Baigę vertinimo vykdymą, galite [pamatyti rezultatus Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Prekės ženklai

Šiame projekte gali būti projektų, produktų ar paslaugų prekės ženklų arba logotipų. Leidžiamas Microsoft
prekės ženklų ar logotipų naudojimas yra reglamentuojamas ir turi atitikti
[Microsoft prekės ženklo ir prekės ženklo gairių](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsoft prekės ženklų ar logotipų naudojimas modifikuotose šio projekto versijose neturi sukelti painiavos ar rodyti Microsoft rėmimą.
Trečiųjų šalių prekės ženklų ar logotipų naudojimas yra reglamentuojamas atitinkamų trečiųjų šalių taisyklių.

## Pagalbos gavimas

Jei susiduriate su sunkumais arba turite klausimų apie DI programų kūrimą, prisijunkite prie:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jei turite produkto atsiliepimų ar klaidų, kurių metu kuriate, apsilankykite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, atkreipkite dėmesį, kad automatiniai vertimai gali būti netikslūs arba klaidingi. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojamas profesionalus vertimas, atliekamas žmogaus. Mes neprisiimame atsakomybės už bet kokius nesusipratimus ar klaidingą interpretaciją, kilusią dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->