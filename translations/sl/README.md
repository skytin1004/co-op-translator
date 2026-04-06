# Co-op Translator

_Enostavno avtomatizirajte in vzdržujte prevode vaših izobraževalnih GitHub vsebin v več jezikih, medtem ko se vaš projekt razvija._

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

### 🌐 Podpora več jezikom

#### Podprto z [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raje kopirate lokalno?**
>
> Ta repozitorij vsebuje prevode v več kot 50 jezikih, kar znatno poveča velikost prenosa. Če želite kopirati brez prevodov, uporabite sparse checkout:
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
> Tako dobite vse, kar potrebujete za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** vam pomaga brez težav lokalizirati izobraževalno GitHub vsebino v več jezikov.
Ko posodobite svoje Markdown datoteke, slike ali zvezke, so prevodi samodejno sinhronizirani, kar zagotavlja, da je vaša vsebina natančna in ažurna za udeležence po celem svetu.

Primer, kako je prevedena vsebina organizirana:

![Example](../../translated_images/sl/translation-ex.0c8aa6a7ee0aad2b.webp)

## Kako je upravljano stanje prevoda

Co-op Translator upravlja prevedeno vsebino kot **verzionirane programske artefakte**,  
ne kot statične datoteke.

Orodje spremlja stanje prevedenih Markdown, slik in zvezkov z  
uporabo **metapodatkov, omejenih na jezik**.

Ta zasnova omogoča Co-op Translator:

- Zanesljivo zaznavanje zastarelih prevodov
- Obravnavo Markdown, slik in zvezkov na dosleden način
- Varen razširljivost pri velikih, hitro rastočih, večjezičnih repozitorijih

Z modeliranjem prevodov kot upravljanih artefaktov,
prevodni postopki naravno sledijo sodobnim
praktikam upravljanja programske odvisnosti in artefaktov.

→ [Kako je upravljano stanje prevoda](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Hiter začetek

```bash
# Ustvarite in aktivirajte virtualno okolje (priporočeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Namestite paket
pip install co-op-translator
# Prevedi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Potegnite javno sliko iz GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Zaženite z montirano trenutno mapo in zagotovljenim .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimalna nastavitev

1. Preverite, da imate podprto različico Pythona (trenutno 3.10-3.12). V poetry (pyproject.toml) je to urejeno samodejno.
2. Ustvarite `.env` datoteko z uporabo predloge: [.env.template](../../.env.template)
3. Nastavite enega ponudnika LLM (Azure OpenAI ali OpenAI)
4. (Neobvezno) Za prevajanje slik (`-img`) nastavite Azure AI Vision
5. (Neobvezno) Nastavite lahko več sklopov poverilnic z dvojenjem spremenljivk s priponami, kot so `_1`, `_2` itd. Vse spremenljivke v sklopu morajo imeti enako pripono.
6. (Priporočeno) Očistite morebitne prejšnje prevode, da se izognete konfliktom (npr. `translations/`)
7. (Priporočeno) Dodajte prevodni razdelek v vaš README z uporabo [predloge za jezike README](./getting_started/README_languages_template.md)
8. Oglejte si: [Nastavitev Azure AI](./getting_started/set-up-azure-ai.md)

## Uporaba

Prevedite vse podprte tipe:

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

Samo zvezki:

```bash
translate -l "zh" -nb
```

Več parametrov: [Povzetek ukazov](./getting_started/command-reference.md)

## Značilnosti

- Avtomatiziran prevod za Markdown, zvezke in slike
- Prevodi so vedno sinhronizirani z izvorno vsebino
- Deluje lokalno (CLI) ali v CI (GitHub Actions)
- Uporablja Azure OpenAI ali OpenAI; neobvezno Azure AI Vision za slike
- Ohranja formatiranje in strukturo Markdown

## Dokumentacija

- [Vodič za ukazno vrstico](./getting_started/command-line-guide/command-line-guide.md)
- [Vodič za GitHub Actions (javni repozitoriji in osnovne skrivnosti)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodič za GitHub Actions (Microsoft organizacijski repozitoriji in organizacijske nastavitve)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Predloga za jezike README](./getting_started/README_languages_template.md)
- [Podprti jeziki](./getting_started/supported-languages.md)
- [Prispevanje](./CONTRIBUTING.md)
- [Reševanje težav](./getting_started/troubleshooting.md)

### Vodič za Microsoft specifične primere
> [!NOTE]
> Samo za skrbnike repozitorijev Microsoft "Za začetnike".

- [Posodabljanje seznama "drugih tečajev" (samo za repozitorije MS za začetnike)](./getting_started/update-other-courses.md)

## Podprite nas in spodbujajte globalno učenje

Pridružite se nam pri revoluciji deljenja izobraževalnih vsebin po vsem svetu! Podprite [Co-op Translator](https://github.com/azure/co-op-translator) z zvezdico na GitHubu in podprite naš cilj razbijanja jezikovnih ovir v učenju in tehnologiji. Vaša zanimanja in prispevki imajo velik vpliv! Prispevki kode in predlogi za izboljšave so vedno dobrodošli.

### Raziščite Microsoft izobraževalne vsebine v vašem jeziku

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

## Videopredstavitve

👉 Kliknite spodnjo sliko za ogled na YouTube.

- **Open at Microsoft**: Kratek 18-minutni uvod in hiter vodič o uporabi Co-op Translator.

  [![Open at Microsoft](../../translated_images/sl/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispevanje

Ta projekt sprejema prispevke in predloge. Vas zanima, kako prispevati k Azure Co-op Translator? Prosimo, preberite naš [CONTRIBUTING.md](./CONTRIBUTING.md) za navodila, kako lahko pomagate, da bo Co-op Translator bolj dostopen.

## Prispevalci
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kodeks ravnanja

Ta projekt je sprejel [Microsoftov kodeks ravnanja za odprtokodno programsko opremo](https://opensource.microsoft.com/codeofconduct/).
Za več informacij si oglejte [pogosta vprašanja o kodeksu ravnanja](https://opensource.microsoft.com/codeofconduct/faq/) ali se obrnite na [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna vprašanja ali komentarje.

## Odgovorna umetna inteligenca

Microsoft se zavezuje pomagati našim strankam, da odgovorno uporabljajo naše izdelke umetne inteligence, deliti pridobljeno znanje ter graditi partnerstva, ki temeljijo na zaupanju, s pomočjo orodij, kot so Opombe o preglednosti in Ocene vpliva. Veliko teh virov je na voljo na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristop k odgovorni umetni inteligenci temelji na naših načelih pravičnosti, zanesljivosti in varnosti, zasebnosti in varnosti, vključenosti, preglednosti in odgovornosti.

Modeli naravnega jezika, slik in govora na veliki lestvici – kot tisti, uporabljeni v tem vzorcu – se lahko potencialno obnašajo na načine, ki so nepravični, nezanesljivi ali žaljivi, kar lahko povzroči škodo. Prosimo, preglejte [Azure OpenAI storitev Opombo o preglednosti](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), da se seznanite s tveganji in omejitvami.

Priporočeni pristop za zmanjševanje teh tveganj je vključitev varnostnega sistema v vašo arhitekturo, ki lahko zazna in prepreči škodljivo vedenje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) nudi neodvisno zaščitno plast, ki omogoča zaznavanje škodljive vsebine, ki jo ustvarijo uporabniki ali AI, v aplikacijah in storitvah. Azure AI Content Safety vključuje API-je za besedilo in slike, ki omogočajo zaznavanje škodljivih vsebin. Prav tako imamo interaktivno Content Safety Studio, kjer si lahko ogledate, raziščete in preizkusite vzorčno kodo za zaznavanje škodljive vsebine v različnih modalitetah. Naslednja [hitri uvod v dokumentacijo](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vas vodi skozi postopke za pošiljanje zahtevkov storitvi.

Drugi pomemben vidik je splošna zmogljivost aplikacije. Pri aplikacijah z večmodalitetnimi in večmodelskimi rešitvami zmogljivost pomeni, da sistem deluje tako, kot pričakujete vi in vaši uporabniki, vključno s tem, da ne generira škodljivih izhodov. Pomembno je oceniti zmogljivost celotne aplikacije z uporabo [meril kakovosti generiranja ter tveganj in varnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vašo AI aplikacijo lahko ocenite v razvojnem okolju z uporabo [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Glede na testni podatkovni niz ali cilj so generacije vaše generativne AI aplikacije kvantitativno ocenjene z vgrajenimi ali po meri izbranimi ocenjevalci. Za začetek z uporabo prompt flow SDK za ocenjevanje sistema lahko sledite [hitremu uvodnemu vodiču](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Ko zaženete ocenjevalno izvedbo, lahko [vizualizirate rezultate v Azure AI Studiu](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Blagovne znamke

Ta projekt lahko vsebuje blagovne znamke ali logotipe za projekte, izdelke ali storitve. Dovoljeno uporabljanje Microsoftovih
blagovnih znamk ali logotipov je predmet in mora slediti
[Microsoftovim smernicam za blagovne znamke in blagovne znamke](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Uporaba Microsoftovih blagovnih znamk ali logotipov v spremenjenih različicah tega projekta ne sme povzročiti zmede ali nakazovati Microsoftovega sponzorstva.
Vsaka uporaba blagovnih znamk ali logotipov tretjih oseb je predmet pravil teh tretjih strani.

## Pridobivanje pomoči

Če se zataknete ali imate vprašanja o razvoju AI aplikacij, se pridružite:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali naletite na napake med razvojem, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovi izvorni različici velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->