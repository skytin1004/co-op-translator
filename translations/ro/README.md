# Co-op Translator

_Automatizează și menține cu ușurință traducerile pentru conținutul educațional GitHub în mai multe limbi pe măsură ce proiectul tău evoluează._

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

### 🌐 Suport multilingv

#### Suportat de [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](./README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferi să clonezi local?**
>
> Acest depozit include peste 50 de traduceri în limbi care cresc semnificativ dimensiunea descărcării. Pentru a clona fără traduceri, folosește sparse checkout:
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
> Aceasta îți oferă tot ce ai nevoie pentru a finaliza cursul cu o descărcare mult mai rapidă.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prezentare generală

**Co-op Translator** te ajută să localizezi cu ușurință conținutul educațional GitHub în mai multe limbi.
Când actualizezi fișierele Markdown, imaginile sau caietele, traducerile rămân automat sincronizate, asigurând că materialul tău este întotdeauna exact și actualizat pentru cursanții din întreaga lume.

Exemplu despre cum este organizat conținutul tradus:

![Example](../../imgs/translation-ex.png)

## Cum este gestionată starea traducerii

Co-op Translator gestionează conținutul tradus ca **artefacte software versionate**,  
nu ca fișiere statice.

Instrumentul urmărește starea traducerilor pentru Markdown, imagini și caiete
folosind **metadate cu scop pe limbă**.

Această arhitectură permite Co-op Translator să:

- Detecteze în mod fiabil traducerile învechite
- Trateze Markdown, imaginile și caietele în mod consecvent
- Se scaleze în siguranță pe depozite mari, dinamice, multi-lingvistice

Prin modelarea traducerilor ca artefacte gestionate,
fluxurile de lucru pentru traducere se aliniază natural cu
practicile moderne de gestionare a dependențelor și artefactelor software.

→ [Cum este gestionată starea traducerii](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Început rapid

```bash
# Creează și activează un mediu virtual (recomandat)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalează pachetul
pip install co-op-translator
# Traduce
translate -l "ko ja fr" -md
```

Docker:

```bash
# Preia imaginea publică de la GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Rulează cu folderul curent montat și .env furnizat (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Configurare minimală

1. Asigură-te că ai o versiune Python suportată (în prezent 3.10-3.12). În poetry (pyproject.toml) acest lucru este gestionat automat.
2. Creează un fișier `.env` folosind șablonul: [.env.template](../../.env.template)
3. Configurează un furnizor LLM (Azure OpenAI sau OpenAI)
4. (Opțional) Pentru traducerea imaginilor (`-img`), configurează Azure AI Vision
5. (Opțional) Poți configura mai multe seturi de credențiale duplicând variabilele cu sufixe precum `_1`, `_2`, etc. Toate variabilele dintr-un set trebuie să aibă același sufix.
6. (Recomandat) Curăță orice traduceri anterioare pentru a evita conflictele (ex.: `translations/`)
7. (Recomandat) Adaugă o secțiune pentru traduceri în README folosind [șablonul README languages](./getting_started/README_languages_template.md)
8. Vezi: [Configurare Azure AI](./getting_started/set-up-azure-ai.md)

## Utilizare

Tradu toate tipurile suportate:

```bash
translate -l "ko ja"
```

Doar Markdown:

```bash
translate -l "de" -md
```

Markdown + imagini:

```bash
translate -l "pt" -md -img
```

Doar caiete:

```bash
translate -l "zh" -nb
```

Mai multe opțiuni: [Referință comenzi](./getting_started/command-reference.md)

## Caracteristici

- Traducere automată pentru Markdown, caiete și imagini
- Menține traducerile sincronizate cu modificările sursă
- Funcționează local (CLI) sau în CI (GitHub Actions)
- Folosește Azure OpenAI sau OpenAI; opțional Azure AI Vision pentru imagini
- Păstrează formatul și structura Markdown

## Documentație

- [Ghid linie de comandă](./getting_started/command-line-guide/command-line-guide.md)
- [Ghid GitHub Actions (depozite publice & secrete standard)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Ghid GitHub Actions (depozite organizație Microsoft & configurări la nivel de organizație)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Șablon README languages](./getting_started/README_languages_template.md)
- [Limbi suportate](./getting_started/supported-languages.md)
- [Contribuții](./CONTRIBUTING.md)
- [Depanare](./getting_started/troubleshooting.md)

### Ghid specific Microsoft
> [!NOTE]
> Pentru întreținătorii depozitelor „For Beginners” Microsoft numai.

- [Actualizarea listei „other courses” (doar pentru depozitele MS Beginners)](./getting_started/update-other-courses.md)

## Susține-ne și promovează învățarea globală

Alătură-te revoluției în modul în care conținutul educațional este distribuit la nivel global! Dă un ⭐ pe GitHub proiectului [Co-op Translator](https://github.com/azure/co-op-translator) și susține misiunea noastră de a elimina barierele lingvistice în învățare și tehnologie. Interesul și contribuțiile tale au un impact semnificativ! Contribuțiile de cod și sugestiile de funcționalități sunt întotdeauna binevenite.

### Explorează conținutul educațional Microsoft în limba ta

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

## Prezentări video

👉 Click pe imaginea de mai jos pentru a viziona pe YouTube.

- **Open at Microsoft**: O introducere scurtă de 18 minute și un ghid rapid despre cum să folosești Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Contribuții

Acest proiect este deschis pentru contribuții și sugestii. Ești interesat să contribui la Azure Co-op Translator? Te rugăm să consulți [CONTRIBUTING.md](./CONTRIBUTING.md) pentru ghiduri despre cum poți ajuta la creșterea accesibilității Co-op Translator.

## Contributori
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Codul de conduită

Acest proiect a adoptat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pentru mai multe informații vedeți [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) sau
contactați [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru orice întrebări sau comentarii suplimentare.

## Inteligență Artificială Responsabilă

Microsoft este angajată să ajute clienții noștri să utilizeze responsabil produsele noastre AI, împărtășind experiențele noastre și construind parteneriate bazate pe încredere prin instrumente precum Transparency Notes și Impact Assessments. Multe dintre aceste resurse pot fi găsite la [https://aka.ms/RAI](https://aka.ms/RAI).
Abordarea Microsoft privind inteligența artificială responsabilă se bazează pe principiile noastre AI de echitate, fiabilitate și siguranță, confidențialitate și securitate, incluziune, transparență și responsabilitate.

Modelele de limbaj natural, imagine și vorbire la scară largă - cum sunt cele folosite în acest exemplu - pot avea comportamente care sunt nedrepte, nesigure sau ofensatoare, cauzând astfel prejudicii. Vă rugăm să consultați [Notă de transparență a serviciului Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) pentru a fi informat despre riscuri și limitări.

Abordarea recomandată pentru atenuarea acestor riscuri este să includeți un sistem de siguranță în arhitectura dvs. care poate detecta și preveni comportamentele dăunătoare. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) oferă un strat independent de protecție, capabil să detecteze conținutul generat de utilizatori și de AI care este dăunător în aplicații și servicii. Azure AI Content Safety include API-uri de text și imagine care vă permit să detectați materiale dăunătoare. De asemenea, avem un Content Safety Studio interactiv care vă permite să vizualizați, să explorați și să încercați coduri de probă pentru detectarea conținutului dăunător în diferite modalități. Următoarea [documentație quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vă ghidează cum să faceți solicitări către serviciu.

Un alt aspect de luat în calcul este performanța generală a aplicației. În cazul aplicațiilor multi-modale și multi-model, considerăm performanța ca fiind faptul că sistemul funcționează așa cum vă așteptați dvs. și utilizatorii dvs., inclusiv evitând generarea de rezultate dăunătoare. Este important să evaluați performanța aplicației dvs. globale folosind [metrici de calitate a generării și de risc și siguranță](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Puteți evalua aplicația AI în mediul dvs. de dezvoltare folosind [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Având un set de date de testare sau un obiectiv, generațiile aplicației dvs. generative AI sunt măsurate cantitativ cu evaluatori încorporați sau evaluatori personalizați la alegere. Pentru a începe cu prompt flow sdk pentru a evalua sistemul, puteți urma [ghidul quickstart](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). După ce executați o rulare de evaluare, puteți [vizualiza rezultatele în Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Mărci comerciale

Acest proiect poate conține mărci comerciale sau logo-uri pentru proiecte, produse sau servicii. Utilizarea autorizată a mărcilor comerciale sau logo-urilor Microsoft este supusă și trebuie să respecte [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Utilizarea mărcilor comerciale sau logo-urilor Microsoft în versiuni modificate ale acestui proiect nu trebuie să creeze confuzie sau să sugereze sponsorizarea Microsoft.
Orice utilizare a mărcilor sau logo-urilor unor terți este supusă politicilor acelorași terți.

## Obținerea ajutorului

Dacă vă blocați sau aveți întrebări despre dezvoltarea aplicațiilor AI, alăturați-vă:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Dacă aveți feedback despre produs sau erori în timpul dezvoltării vizitați:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu suntem responsabili pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->