# Co-op Translator

_Lako automatizirajte i održavajte prijevode vašeg obrazovnog GitHub sadržaja na više jezika kako se vaš projekt razvija._

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

### 🌐 Višejezična podrška

#### Podržano od [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Radije klonirate lokalno?**
>
> Ovo spremište uključuje prijevode na 50+ jezika što značajno povećava veličinu preuzimanja. Za kloniranje bez prijevoda, koristite sparse checkout:
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
> Ovo vam daje sve što vam treba za dovršavanje tečaja s puno bržim preuzimanjem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** pomaže vam da jednostavno lokalizirate vaš obrazovni GitHub sadržaj na više jezika.  
Kada ažurirate svoje Markdown datoteke, slike ili bilježnice, prijevodi se automatski sinkroniziraju, osiguravajući da vaš sadržaj ostane točan i ažuran za učenike širom svijeta.

Primjer kako je prevedeni sadržaj organiziran:

![Example](../../translated_images/hr/translation-ex.0c8aa6a7ee0aad2b.webp)

## Kako se upravlja stanjem prijevoda

Co-op Translator upravlja prevedenim sadržajem kao **verzioniranim softverskim artefaktima**,
a ne kao statičnim datotekama.

Alat prati stanje prevedenog Markdowna, slika i bilježnica  
koristeći **metapodatke ograničene na jezik**.

Ovaj dizajn omogućuje Co-op Translatoru da:

- Pouzdano otkriva zastarjele prijevode
- Dosljedno tretira Markdown, slike i bilježnice
- Sigurno skalira na velikim, brzo mijenjajućim, višejezičnim spremištima

Modeliranjem prijevoda kao upravljanih artefakata,  
radni procesi prijevoda prirodno se usklađuju s modernim  
softverskim praksama upravljanja ovisnostima i artefaktima.

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

## Minimalna postavka

1. Provjerite imate li podržanu verziju Pythona (trenutačno 3.10-3.12). U poetry (pyproject.toml) ovo se automatski rješava.
2. Kreirajte `.env` datoteku koristeći predložak: [.env.template](../../.env.template)
3. Konfigurirajte jednog LLM davatelja usluga (Azure OpenAI ili OpenAI)
4. (Opcionalno) Za prijevod slika (`-img`), konfigurirajte Azure AI Vision
5. (Opcionalno) Možete konfigurirati više skupova vjerodajnica dupliciranjem varijabli s sufiksima poput `_1`, `_2`, itd. Sve varijable u skupu moraju imati isti sufiks.
6. (Preporučeno) Očistite prethodne prijevode kako biste izbjegli sukobe (npr. `translations/`)
7. (Preporučeno) Dodajte odjeljak za prijevod u vaš README koristeći [README languages template](./getting_started/README_languages_template.md)
8. Pogledajte: [Postavljanje Azure AI](./getting_started/set-up-azure-ai.md)

## Upotreba

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

- Automatski prijevod Markdowna, bilježnica i slika
- Održava prijevode sinkroniziranim sa izvorom
- Radi lokalno (CLI) ili u CI (GitHub Actions)
- Koristi Azure OpenAI ili OpenAI; opcionalno Azure AI Vision za slike
- Očuva oblikovanje i strukturu Markdowna

## Dokumentacija

- [Vodič za naredbenu liniju](./getting_started/command-line-guide/command-line-guide.md)
- [Vodič za GitHub Actions (javni repozitoriji i standardni tajni ključevi)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodič za GitHub Actions (Microsoft organizacijski repozitoriji i postavke na razini organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Predložak za jezični odjeljak README](./getting_started/README_languages_template.md)
- [Podržani jezici](./getting_started/supported-languages.md)
- [Doprinos](./CONTRIBUTING.md)
- [Rješavanje problema](./getting_started/troubleshooting.md)

### Microsoft-specifični vodič
> [!NOTE]
> Samo za održavatelje Microsoft „For Beginners“ repozitorija.

- [Ažuriranje popisa „ostalih tečajeva“ (samo za MS Beginners repozitorije)](./getting_started/update-other-courses.md)

## Podržite nas i potaknite globalno učenje

Pridružite se revoluciji u načinu dijeljenja obrazovnog sadržaja širom svijeta! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) zvjezdicu ⭐ na GitHubu i podržite našu misiju uklanjanja jezičnih barijera u učenju i tehnologiji. Vaš interes i doprinosi čine značajnu razliku! Prijedlozi za kod i značajke uvijek su dobrodošli.

### Istražite Microsoftov obrazovni sadržaj na vašem jeziku

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

👉 Kliknite na sliku ispod za gledanje na YouTubeu.

- **Open at Microsoft**: Kratki 18-minutni uvod i brzi vodič o korištenju Co-op Translatora.

  [![Open at Microsoft](../../translated_images/hr/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Doprinos

Ovaj projekt poziva na doprinose i prijedloge. Zainteresirani za doprinos Azure Co-op Translatoru? Molimo pogledajte naš [CONTRIBUTING.md](./CONTRIBUTING.md) za smjernice kako možete pomoći da Co-op Translator bude pristupačniji.

## Suradnici
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ponašanja

Ovaj je projekt usvojio [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pogledajte [Često postavljana pitanja o kodeksu ponašanja](https://opensource.microsoft.com/codeofconduct/faq/) ili
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Odgovorni AI

Microsoft je posvećen pomaganju našim korisnicima da odgovorno koriste naše AI proizvode, dijeleći naša saznanja i gradeći partnerstva temeljena na povjerenju kroz alate poput Transparency Notes i Impact Assessments. Mnogi od ovih resursa dostupni su na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristup odgovornom AI-u temelji se na našim AI načelima pravednosti, pouzdanosti i sigurnosti, privatnosti i sigurnosti, uključivosti, transparentnosti i odgovornosti.

Modeli prirodnog jezika, slike i govora velikih razmjera – poput onih korištenih u ovom primjeru – mogu potencijalno imati ponašanja koja su nepravedna, nepouzdana ili uvredljiva, što može uzrokovati štete. Molimo konzultirajte [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) kako biste bili informirani o rizicima i ograničenjima.

Preporučeni pristup ublažavanju ovih rizika jest uključivanje sustava sigurnosti u vašu arhitekturu koji može otkriti i spriječiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža neovisni sloj zaštite, sposoban detektirati štetni sadržaj generiran od strane korisnika i AI-ja u aplikacijama i uslugama. Azure AI Content Safety uključuje API-je za tekst i slike koji vam omogućuju otkrivanje štetnog materijala. Također imamo interaktivni Content Safety Studio koji vam omogućuje pregled, istraživanje i isprobavanje primjera koda za otkrivanje štetnog sadržaja u različitim modalitetima. Sljedeća [dokumentacija za brzo pokretanje](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz slanje zahtjeva prema usluzi.

Drugi aspekt koji treba uzeti u obzir je ukupna izvedba aplikacije. Kod aplikacija s više modaliteta i modela, izvedbom smatramo da sustav radi onako kako vi i vaši korisnici očekujete, uključujući da ne generira štetne rezultate. Važno je procijeniti izvedbu vaše aplikacije koristeći [kriterije kvalitete generiranja i metričke podatke rizika i sigurnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Možete procijeniti svoju AI aplikaciju u razvojnom okruženju korištenjem [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ako imate testni skup podataka ili cilj, generacije vaše generativne AI aplikacije kvantitativno se mjere ugrađenim ili prilagođenim vrednovateljima po vašem izboru. Za početak korištenja prompt flow SDK-a za evaluaciju sustava možete slijediti [vodič za brzo pokretanje](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Nakon što izvedete evaluacijski pokret, možete [vizualizirati rezultate u Azure AI Studiju](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Zaštićeni znakovi

Ovaj projekt može sadržavati zaštićene znakove ili logotipe projekata, proizvoda ili usluga. Ovlaštena upotreba Microsoftovih
zaštićenih znakova ili logotipa mora se pridržavati i slijediti
[Microsoftove smjernice za korištenje zaštitnih znakova i branda](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Upotreba Microsoftovih zaštitnih znakova ili logotipa u modificiranim verzijama ovog projekta ne smije izazvati zabunu niti implicirati Microsoftovo sponzorstvo.
Svaka upotreba zaštitnih znakova ili logotipa trećih strana podliježe pravilima tih trećih strana.

## Dobivanje pomoći

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratnu informaciju o proizvodu ili greške tijekom razvoja, posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Izjava o odricanju od odgovornosti**:
Ovaj dokument je preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako se trudimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->