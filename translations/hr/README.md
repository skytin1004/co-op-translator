# Co-op Translator

_Lako automatizirajte i održavajte prijevode vašeg edukacijskog GitHub sadržaja na više jezika kako vaš projekt raste._

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

### 🌐 Podrška za više jezika

#### Podržano od strane [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Radije klonirati lokalno?**
>
> Ovaj repozitorij uključuje preko 50 prijevoda jezika što značajno povećava veličinu preuzimanja. Za kloniranje bez prijevoda, koristite sparsan checkout:
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
> Ovo vam daje sve što vam treba za dovršetak tečaja s puno bržim preuzimanjem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** pomaže vam da lokalizirate svoj edukacijski GitHub sadržaj na više jezika bez napora.
Kad ažurirate svoje Markdown datoteke, slike ili bilježnice, prijevodi se automatski sinkroniziraju, osiguravajući da vaš sadržaj ostane točan i ažuran za učenike širom svijeta.

Primjer kako je prevedeni sadržaj organiziran:

![Example](../../imgs/translation-ex.png)

## Kako se upravlja stanjem prijevoda

Co-op Translator upravlja prevedenim sadržajem kao **verzioniranim softverskim artefaktima**,  
a ne kao statičnim datotekama.

Alat prati stanje prevedenih Markdown, slika i bilježnica
koristeći **metapodatke specifične za jezik**.

Ovaj dizajn omogućava Co-op Translatoru da:

- Pouzdano otkrije zastarjele prijevode
- Postupa s Markdown, slikama i bilježnicama dosljedno
- Sigurno skalira preko velikih, brzo mijenjajućih, višelingvalnih repozitorija

Modeliranjem prijevoda kao upravljanih artefakata,
radni procesi prijevoda prirodno se usklađuju s modernim
praksama upravljanja softverskim ovisnostima i artefaktima.

→ [Kako se upravlja stanjem prijevoda](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Brzi početak

```bash
# Kreirajte i aktivirajte virtualno okruženje (preporučeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Instalirajte paket
pip install co-op-translator
# Prevedi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Povucite javnu sliku s GHCR-a
docker pull ghcr.io/azure/co-op-translator:latest
# Pokrenite s montiranim trenutnim direktorijem i pruženom .env datotekom (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna postava

1. Provjerite imate li podržanu verziju Pythona (trenutno 3.10-3.12). U poetry (pyproject.toml) to se automatski obrađuje.
2. Napravite `.env` datoteku koristeći predložak: [.env.template](../../.env.template)
3. Konfigurirajte jednog LLM pružatelja usluge (Azure OpenAI ili OpenAI)
4. (Neobavezno) Za prijevod slika (`-img`), konfigurirajte Azure AI Vision
5. (Neobavezno) Možete konfigurirati više skupova vjerodajnica dupliciranjem varijabli sa sufiksima kao što su `_1`, `_2` itd. Sve varijable u jednom skupu moraju imati isti sufiks.
6. (Preporučeno) Očistite prethodne prijevode kako biste izbjegli konflikte (npr. `translations/`)
7. (Preporučeno) Dodajte odjeljak za prijevod u svoj README koristeći [README languages template](./getting_started/README_languages_template.md)
8. Pogledajte: [Postavljanje Azure AI](./getting_started/set-up-azure-ai.md)

## Korištenje

Prevedite sve podržane tipove:

```bash
translate -l "ko ja"
```

Samo Markdown:

```bash
translate -l "de" -md
```

Markdown + slike:

```bash
translate -l "pt" -md -img
```

Samo bilježnice:

```bash
translate -l "zh" -nb
```

Više zastavica: [Referenca naredbi](./getting_started/command-reference.md)

## Značajke

- Automatizirani prijevod za Markdown, bilježnice i slike
- Drži prijevode u sinkronizaciji s izmjenama izvora
- Radi lokalno (CLI) ili u CI (GitHub Actions)
- Koristi Azure OpenAI ili OpenAI; opcionalno Azure AI Vision za slike
- Čuva Markdown formatiranje i strukturu

## Dokumentacija

- [Vodič za naredbeni redak](./getting_started/command-line-guide/command-line-guide.md)
- [Vodič za GitHub Actions (javni repozitoriji & standardni tajni ključevi)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodič za GitHub Actions (Microsoft organizacijski repozitoriji & postavke na razini organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Podržani jezici](./getting_started/supported-languages.md)
- [Doprinosi](./CONTRIBUTING.md)
- [Rješavanje problema](./getting_started/troubleshooting.md)

### Specifični Microsoft vodič
> [!NOTE]
> Samo za održavače Microsoft „Za početnike“ repozitorija.

- [Ažuriranje liste „ostalih tečajeva“ (samo za MS Beginners repozitorije)](./getting_started/update-other-courses.md)

## Podržite nas i potaknite globalno učenje

Pridružite nam se u revoluciji načina na koji se edukacijski sadržaj dijeli globalno! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubu i podržite našu misiju razbijanja jezičnih barijera u učenju i tehnologiji. Vaš interes i doprinosi čine značajan utjecaj! Kodni doprinosi i prijedlozi značajki su uvijek dobrodošli.

### Istražite Microsoft edukacijski sadržaj na vašem jeziku

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

## Video prezentacije

👉 Kliknite sliku dolje za gledanje na YouTubeu.

- **Open at Microsoft**: Kratka 18-minutna uvodna i brza uputa o korištenju Co-op Translatora.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Doprinosi

Ovaj projekt pozdravlja doprinose i prijedloge. Zainteresirani za doprinos Azure Co-op Translatoru? Molimo pogledajte naš [CONTRIBUTING.md](./CONTRIBUTING.md) za smjernice kako možete pomoći da Co-op Translator bude pristupačniji.

## Suradnici
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ponašanja

Ovaj je projekt usvojio [Microsoftov Kodeks ponašanja za otvoreni izvor](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pogledajte [Često postavljana pitanja o Kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/) ili
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Odgovorna AI

Microsoft je predan pomoći našim korisnicima pri odgovornom korištenju naših AI proizvoda, dijeljenju naših saznanja i izgradnji partnerstava temeljenih na povjerenju pomoću alata poput Transparency Notes i Impact Assessments. Mnogi ovi resursi dostupni su na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristup odgovornoj AI zasniva se na principima AI-a pravednosti, pouzdanosti i sigurnosti, privatnosti i sigurnosti, uključenosti, transparentnosti i odgovornosti.

Veliki modeli za prirodni jezik, slike i govor - poput onih korištenih u ovom primjeru - mogu se potencijalno ponašati na nepravedan, nepouzdan ili uvredljiv način, što može prouzročiti štete. Molimo konzultirajte [bilješku o transparentnosti usluge Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) kako biste bili informirani o rizicima i ograničenjima.

Preporučeni pristup za ublažavanje ovih rizika je uključivanje sigurnosnog sustava u vašu arhitekturu koji može otkriti i spriječiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža neovisni sloj zaštite, sposoban otkriti štetni sadržaj koji generiraju korisnici i AI u aplikacijama i uslugama. Azure AI Content Safety uključuje tekstualne i slikovne API-je koji vam omogućuju otkrivanje štetnog materijala. Također imamo interaktivni Content Safety Studio koji vam omogućuje pregled, istraživanje i isprobavanje primjera koda za otkrivanje štetnog sadržaja u različitim modalitetima. Sljedeća [dokumentacija za brzi početak](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz slanje zahtjeva usluzi.

Još jedan aspekt koji treba uzeti u obzir jest ukupna izvedba aplikacije. Kod višemodalnih i više-modelskih aplikacija smatramo izvedbom to da sustav radi kako vi i vaši korisnici očekujete, uključujući i ne generiranje štetnih rezultata. Važno je procijeniti izvedbu vaše ukupne aplikacije koristeći [mjerenja kvalitete generiranja i rizika i sigurnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoj AI sustav možete procijeniti u svom razvojnom okruženju koristeći [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Bilo da imate testni skup podataka ili cilj, generacije vaše generativne AI aplikacije kvantitativno se mjere ugrađenim ocjenjivačima ili prilagođenim ocjenjivačima po vašem izboru. Za početak s prompt flow sdk-om za evaluaciju sustava, možete slijediti [vodič za brzi početak](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Nakon pokretanja evaluacijskog izvođenja možete [vizualizirati rezultate u Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Zaštitni znakovi

Ovaj projekt može sadržavati zaštitne znakove ili logotipe projekata, proizvoda ili usluga. Ovlaštena upotreba Microsoftovih
zaštitnih znakova ili logotipa podliježe i mora slijediti
[Microsoftova pravila o korištenju zaštitnih znakova i brenda](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Upotreba Microsoftovih zaštitnih znakova ili logotipa u izmijenjenim verzijama ovog projekta ne smije izazvati zbunjenost niti implicirati sponzorstvo Microsofta.
Svaka upotreba zaštitnih znakova ili logotipa trećih strana podliježe pravilima tih trećih strana.

## Dobivanje pomoći

Ako zapnete ili imate bilo kakva pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili pogreške tijekom izrade posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj je dokument preveden pomoću AI servisa za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->