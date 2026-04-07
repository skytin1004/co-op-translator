# Co-op Translator

_Helposti automatisoi ja ylläpidä käännöksiä opetusmateriaaliisi GitHubissa useille kielille projektisi kehittyessä._

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

### 🌐 Monikielinen tuki

#### Tuettu [Co-op Translatorin](https://github.com/Azure/Co-op-Translator) toimesta

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Haluatko kloonata paikallisesti?**
>
> Tämä repositorio sisältää yli 50 käännöskieltä, mikä kasvattaa merkittävästi latauskokoa. Kloonaa ilman käännöksiä käyttämällä sparse checkout -toimintoa:
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
> Saat kaiken tarvittavan kurssin suorittamiseen paljon nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Yleiskatsaus

**Co-op Translator** auttaa sinua lokalisointiprosessissa kääntämään opetussisältösi GitHubissa useille kielille vaivattomasti.  
Kun päivität Markdown-tiedostoja, kuvia tai muistikirjoja, käännökset pysyvät automaattisesti synkronoituna, varmistaen, että sisältösi on ajantasaista ja tarkkaa oppijoille ympäri maailmaa.

Esimerkki siitä, miten käännetty sisältö on järjestetty:

![Example](../../imgs/translation-ex.png)

## Kuinka käännösten tila hallitaan

Co-op Translator käsittelee käännetyn sisällön **versioituna ohjelmistoartifaktina**,  
ei staattisina tiedostoina.

Työkalu seuraa käännettyjen Markdown-tiedostojen, kuvien ja muistikirjojen tilaa  
käyttäen **kieleen sidottua metadataa**.

Tämä malli mahdollistaa Co-op Translatorille:

- Vanhentuneiden käännösten luotettavan tunnistamisen  
- Markdownin, kuvien ja muistikirjojen yhdenmukaisen käsittelyn  
- Turvallisen skaalautumisen suurissa, nopeasti muuttuvissa monikielisissä repozitorioissa

Mallintamalla käännökset hallituiksi artifakteiksi,  
käännöstyönkulut ovat luonnollisesti linjassa nykyaikaisten  
ohjelmistoriippuvuuksien ja artifaktinhallinnan käytäntöjen kanssa.

→ [Kuinka käännösten tila hallitaan](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Nopeasti käyntiin

```bash
# Luo ja aktivoi virtuaaliympäristö (suositeltavaa)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Asenna paketti
pip install co-op-translator
# Käännä
translate -l "ko ja fr" -md
```

Docker:

```bash
# Hae julkinen kuva GHCR:stä
docker pull ghcr.io/azure/co-op-translator:latest
# Suorita nykyisen kansion ollessa liitetty ja .env tiedosto mukana (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimiasennus

1. Varmista, että sinulla on tuettu Python-versio (tällä hetkellä 3.10–3.12). Poetryssa (pyproject.toml) tämä hoituu automaattisesti.  
2. Luo `.env`-tiedosto mallin perusteella: [.env.template](../../.env.template)  
3. Määritä yksi LLM-palveluntarjoaja (Azure OpenAI tai OpenAI)  
4. (Valinnainen) Kuvakäännöksiä varten (`-img`), määritä Azure AI Vision  
5. (Valinnainen) Voit määrittää useita tunnistetietojoukkoja monistamalla muuttujat tunnisteilla kuten `_1`, `_2` jne. Kaikilla joukon muuttujilla tulee olla sama tunniste.  
6. (Suositeltavaa) Siivoa aiemmat käännökset ristiriitojen välttämiseksi (esim. `translations/`)  
7. (Suositeltavaa) Lisää README-tiedostoon käännösosio käyttäen [README kielten mallia](./getting_started/README_languages_template.md)  
8. Katso: [Azure AI:n asetukset](./getting_started/set-up-azure-ai.md)

## Käyttö

Käännä kaikki tuetut tyypit:

```bash
translate -l "ko ja"
```

Vain Markdown:

```bash
translate -l "de" -md
```

Markdown + kuvat:

```bash
translate -l "pt" -md -img
```

Vain muistikirjat:

```bash
translate -l "zh" -nb
```

Lisäasetuksia: [Komentojen viite](./getting_started/command-reference.md)

## Ominaisuudet

- Kääntää automaattisesti Markdownia, muistikirjoja ja kuvia  
- Pitää käännökset synkronoituna lähdemuutosten kanssa  
- Toimii paikallisesti (CLI) tai CI:ssä (GitHub Actions)  
- Käyttää Azure OpenAI:ta tai OpenAI:tä; valinnainen Azure AI Vision kuville  
- Säilyttää Markdownin muotoilun ja rakenteen

## Dokumentaatio

- [Komentoriviohje](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions -opas (julkiset repositoriot & standard salaisuudet)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions -opas (Microsoft organisaation repositoriot & organisaatiotason asetukset)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README kielten malli](./getting_started/README_languages_template.md)  
- [Tuetut kielet](./getting_started/supported-languages.md)  
- [Osallistuminen](./CONTRIBUTING.md)  
- [Vianmääritys](./getting_started/troubleshooting.md)

### Microsoft-spesifinen opas
> [!NOTE]
> Vain Microsoftin “For Beginners” -repositorioiden ylläpitäjille.

- [“Muut kurssit” -listan päivitys (vain MS Beginners -repositorioille)](./getting_started/update-other-courses.md)

## Tue meitä ja edistä globaalin oppimisen tulevaisuutta

Liity muutokseen, jossa opetussisältöjä jaetaan maailmanlaajuisesti uudella tavalla! Anna [Co-op Translatorille](https://github.com/azure/co-op-translator) ⭐ GitHubissa ja tue missiotamme murtaa kielimuureja oppimisessa ja teknologiassa. Kiinnostuksesi ja panoksesi ovat merkittäviä! Koodifleksit ja ominaisuusideat ovat aina tervetulleita.

### Tutustu Microsoftin opetussisältöön omalla kielelläsi

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

## Videoesitykset

👉 Klikkaa alla olevaa kuvaa katsoaksesi YouTubessa.

- **Open at Microsoft**: Lyhyt 18 minuutin esittely ja pikaopas Co-op Translatorin käyttöön.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Osallistuminen

Tätä projektia saa mielellään kehittää ja antaa ehdotuksia. Oletko kiinnostunut osallistumaan Azure Co-op Translatorin kehitykseen? Katso [CONTRIBUTING.md](./CONTRIBUTING.md) ohjeet siitä, miten voit auttaa tekemään Co-op Translatorista entistä saavutettavamman.

## Avustajat
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoftin avointen lähdekoodien käyttäytymissäännöt](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löydät osoitteesta [Käyttäytymissäännöt FAQ](https://opensource.microsoft.com/codeofconduct/faq/) tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) kaikissa lisäkysymyksissä tai -kommenteissa.

## Vastuullinen tekoäly

Microsoft sitoutuu auttamaan asiakkaitaan käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia työkalujen, kuten Läpinäkyvyysmuistiinpanojen ja Vaikutusten arviointien, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftin lähestymistapa vastuulliseen tekoälyyn perustuu tekoälyperiaatteisiimme, jotka ovat oikeudenmukaisuus, luotettavuus ja turvallisuus, yksityisyys ja tietoturva, osallistavuus, läpinäkyvyys ja vastuullisuus.

Laajamittaiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä esimerkissä käytetyt – voivat potentiaalisesti käyttäytyä epäoikeudenmukaisesti, epäluotettavasti tai loukkaavasti, mikä voi aiheuttaa haittaa. Katso riskien ja rajoitusten osalta [Azure OpenAI -palvelun läpinäkyvyysmuistio](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Suositeltu tapa lieventää näitä riskejä on sisällyttää järjestelmääsi turvallisuusjärjestelmä, joka pystyy havaitsemaan ja estämään haitallisen käyttäytymisen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa riippumattoman suojakerroksen, joka pystyy havaitsemaan sovelluksissa ja palveluissa syntyvää haitallista käyttäjän ja tekoälyn generoitua sisältöä. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit tunnistaa haitallista materiaalia. Meillä on myös interaktiivinen Content Safety Studio, jonka avulla voit tarkastella, tutkia ja kokeilla esimerkkikoodia haitallisen sisällön havaitsemiseen eri muodoissa. Seuraava [aloitusdokumentaatio](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa sinut tekemään palvelupyynnöt.

Toinen huomioon otettava seikka on sovelluksen kokonaisuudellinen suorituskyky. Monimuoto- ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosteiden välttäminen. On tärkeää arvioida kokonaissovelluksesi suorituskyky käyttäen [luontilaadun sekä riskien ja turvallisuusmittareita](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä [prompt flow SDK:ta](https://microsoft.github.io/promptflow/index.html). Antamalla joko testidatan tai tavoitteen, generaatiivisen tekoälysovelluksesi tuotokset mitataan määrällisesti sisäänrakennetuilla tai valitsemillasi mukautetuilla arvioijilla. Aloittaaksesi prompt flow sdk:n käytön järjestelmäsi arviointiin voit seurata [aloitusopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Azure AI Studiossa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavaramerkit

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja projekteille, tuotteille tai palveluille. Microsoftin tavaramerkkien tai logojen käyttö on sallittu ja niiden käyttöä tulee noudattaa [Microsoftin tavaramerkki- ja brändiohjeita](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsoftin tavaramerkkien tai logojen käyttö tämän projektin muokatuissa versioissa ei saa aiheuttaa sekaannusta tai antaa ymmärtää, että Microsoft sponsoroisi projektia.
Kolmansien osapuolten tavaramerkkien tai logojen käyttöä ohjaavat kyseisten osapuolten käytännöt.

## Apua saatavilla

Jos jumitut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on palautetta tuotteesta tai kohtaat virheitä rakentaessasi, vieraile:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty AI-käännöspalvelu [Co-op Translator](https://github.com/Azure/co-op-translator) avulla. Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattilaisen tekemää ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkintojen seurauksista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->