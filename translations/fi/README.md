# Co-op Translator

_Suositu sujuvasti GitHub-koulutussisältösi käännökset usealle kielelle sitä mukaa, kun projektisi kehittyy._

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
> Tämä repositorio sisältää yli 50 käännöstä, mikä kasvattaa merkittävästi latausmäärää. Kloonaa ilman käännöksiä käyttämällä sparse checkout -toimintoa:
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
> Saat kaiken tarvitsemasi kurssin suorittamiseen paljon nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Yleiskatsaus

**Co-op Translator** auttaa sinua lokalisoimaan koulutussisältösi GitHubissa useille kielille vaivattomasti.  
Kun päivität Markdown-tiedostojasi, kuvia tai muistikirjoja, käännökset pysyvät automaattisesti synkronoituina, varmistaen, että sisältösi on tarkkaa ja ajan tasalla oppijoille ympäri maailmaa.

Esimerkki siitä, miten käännetty sisältö on järjestetty:

![Example](../../translated_images/fi/translation-ex.0c8aa6a7ee0aad2b.webp)

## Kuinka käännöstila hallitaan

Co-op Translator käsittelee käännetyn sisällön **versionhallittuina ohjelmistoartefakteina**,  
ei staattisina tiedostoina.

Työkalu seuraa käännettyjen Markdown-, kuvien ja muistikirjojen tilaa  
käyttäen **kielikohtaisia metatietoja**.

Tämä suunnittelu antaa Co-op Translatorille mahdollisuuden:

- Luotettavasti havaita vanhentuneet käännökset
- Käsitellä Markdownia, kuvia ja muistikirjoja johdonmukaisesti
- Skaalata turvallisesti suurissa, nopeasti liikkuvissa, monikielisissä repositorioissa

Mallintamalla käännökset hallituiksi artefakteiksi,  
käännöstöiden työnkulut soveltuvat luontevasti nykyaikaisiin  
ohjelmistojen riippuvuuksien ja artefaktien hallinnan käytäntöihin.

→ [Kuinka käännöstila hallitaan](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Nopea aloitus

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
# Vedä julkinen kuva GHCR:stä
docker pull ghcr.io/azure/co-op-translator:latest
# Suorita nykyinen kansio liitettynä ja .env mukana (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimiasennus

1. Vahvista, että sinulla on tuettu Python-versio (tällä hetkellä 3.10-3.12). Poetryssa (pyproject.toml) tämä hoituu automaattisesti.
2. Luo `.env`-tiedosto mallin perusteella: [.env.template](../../.env.template)
3. Määritä yksi LLM-palveluntarjoaja (Azure OpenAI tai OpenAI)
4. (Valinnainen) Kuvien käännökseen (`-img`) määritä Azure AI Vision
5. (Valinnainen) Voit määrittää useita tunnistautumissarjoja kopioimalla muuttujat, joihin lisätään päätteitä kuten `_1`, `_2` jne. Kaikissa sarjan muuttujissa tulee olla sama pääte.
6. (Suositeltu) Puhdista aiemmat käännökset välttääksesi ristiriitoja (esim. `translations/`)
7. (Suositeltu) Lisää käännösosio README-tiedostoosi käyttämällä [README kielten mallia](./getting_started/README_languages_template.md)
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

Lisävalitsimia: [Komentoviite](./getting_started/command-reference.md)

## Ominaisuudet

- Automaattinen käännös Markdownille, muistikirjoille ja kuville
- Pidä käännökset synkronoituna lähdemuutosten kanssa
- Toimii paikallisesti (CLI) tai CI:ssä (GitHub Actions)
- Käyttää Azure OpenAI:ta tai OpenAI:ta; valinnainen Azure AI Vision kuvien käännöksessä
- Säilyttää Markdownin muotoilun ja rakenteen

## Dokumentaatio

- [Komentoriviohje](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions -opas (Julkiset repositoriot & standard salaisuudet)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions -opas (Microsoft-organisaation repositoriot & organisaatiotason asetukset)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README kielten malli](./getting_started/README_languages_template.md)
- [Tuetut kielet](./getting_started/supported-languages.md)
- [Osallistuminen](./CONTRIBUTING.md)
- [Vianmääritys](./getting_started/troubleshooting.md)

### Microsoftille suunnattu opas
> [!NOTE]
> Vain Microsoftin “For Beginners” -repositorion ylläpitäjille.

- [Päivitä ”other courses” -lista (vain MS Beginners -repositoriot)](./getting_started/update-other-courses.md)

## Tue meitä ja edistä maailmanlaajuista oppimista

Liity meihin muuttamaan koulutussisällön jakelua globaalisti! Anna [Co-op Translatorille](https://github.com/azure/co-op-translator) ⭐ GitHubissa ja tue missiotamme purkaa kielimuurit oppimisessa ja teknologiassa. Kiinnostuksesi ja panoksesi merkitsevät paljon! Koodiparannukset ja ominaisuusehdotukset ovat aina tervetulleita.

### Tutustu Microsoftin koulutussisältöön omalla kielelläsi

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

- **Open at Microsoft**: Lyhyt 18 minuutin johdanto ja nopea opas Co-op Translatorin käyttöön.

  [![Open at Microsoft](../../translated_images/fi/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Osallistu projektiin

Tämä projekti ottaa vastaan panoksia ja ehdotuksia. Kiinnostuitko osallistumaan Azure Co-op Translatorin kehitykseen? Katso ohjeet siitä, miten voit auttaa tekemään Co-op Translatorista entistä saavutettavamman, [CONTRIBUTING.md](./CONTRIBUTING.md) tiedostosta.

## Tekijät
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käyttäytymissäännöt

Tämä projekti on ottanut käyttöön [Microsoftin avoimen lähdekoodin käyttäytymissäännöt](https://opensource.microsoft.com/codeofconduct/). 
Lisätietoja löytyy [Käyttäytymissäännöt FAQ](https://opensource.microsoft.com/codeofconduct/faq/) -sivulta tai ota yhteyttä osoitteeseen [opencode@microsoft.com](mailto:opencode@microsoft.com) lisäkysymyksiä tai kommentteja varten.

## Vastuullinen tekoäly

Microsoft on sitoutunut auttamaan asiakkaitamme käyttämään tekoälytuotteitamme vastuullisesti, jakamaan oppejamme ja rakentamaan luottamukseen perustuvia kumppanuuksia läpinäkyvyysmuistiinpanojen ja vaikutusten arviointien kaltaisten työkalujen avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).  
Microsoftin lähestymistapa vastuulliseen tekoälyyn perustuu tekoälyn periaatteisiimme oikeudenmukaisuuden, luotettavuuden ja turvallisuuden, yksityisyyden ja tietoturvan, osallisuuden, läpinäkyvyyden ja vastuullisuuden osalta.

Suurikokoiset luonnollisen kielen, kuvan ja puheen mallit – kuten tässä esimerkissä käytetyt – voivat mahdollisesti käyttäytyä tavoilla, jotka ovat epäreiluja, epäluotettavia tai loukkaavia, aiheuttaen siten haittoja. Tutustu [Azure OpenAI -palvelun läpinäkyvyysmuistiinpanoon](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) saadaksesi tietoa riskeistä ja rajoituksista.

Suositeltu lähestymistapa näiden riskien vähentämiseksi on sisällyttää arkkitehtuuriisi turvallisuusjärjestelmä, joka pystyy havaitsemaan ja estämään haitallisen käyttäytymisen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa itsenäisen suojakerroksen, joka pystyy havaitsemaan haitallisen käyttäjän ja tekoälyn tuottaman sisällön sovelluksissa ja palveluissa. Azure AI Content Safety sisältää tekstin ja kuvan API:t, joiden avulla voit havaita haitallista materiaalia. Meillä on myös interaktiivinen Content Safety Studio, jonka avulla voit tarkastella, tutkia ja kokeilla näytetekstiä haitallisen sisällön tunnistamiseen eri muodoissa. Seuraava [pikakäyttöohje](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa sinua palvelupyynnön tekemisessä.

Toinen otettava huomioon oleva näkökulma on sovelluksen kokonaiskäyttösuorituskyky. Monimuotoisissa ja monimallipohjaisissa sovelluksissa suorituskyvyllä tarkoitetaan, että järjestelmä toimii odotustesi ja käyttäjiesi odotusten mukaisesti, mukaan lukien haitallisten tulosteiden välttäminen. On tärkeää arvioida kokonaisvaltaisen sovelluksesi suorituskykyä käyttäen [luontilaadun ja riskien sekä turvallisuuden mittareita](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Voit arvioida tekoälysovellustasi kehitysympäristössäsi käyttämällä [prompt flow SDK:ta](https://microsoft.github.io/promptflow/index.html). Olipa kyseessä testiaineisto tai tavoite, generatiivisen tekoälysovelluksesi tuotoksia mitataan määrällisesti sisäänrakennettujen tai valinnaisten arvioijien avulla. Aloittaaksesi prompt flow sdk:n käytön järjestelmäsi arviointiin, voit seurata [pikakäyttöohjetta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun suoritat arviointikierroksen, voit [visualisoida tulokset Azure AI Studiolla](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavara- ja palvelumerkit

Tämä projekti saattaa sisältää tavara- tai palvelumerkkejä tai logoja projekteista, tuotteista tai palveluista. Microsoftin tavara- ja palvelumerkkien oikeutettu käyttö on riippuvainen ja noudattaa [Microsoftin tavara- ja brändiohjeita](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Microsoftin tavara- tai palvelumerkkien käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta tai antaa vaikutelmaa Microsoftin sponsoroinnista.  
Kolmansien osapuolten tavara- tai palvelumerkkien käyttö on niiden kolmansien osapuolten sääntöjen alaista.

## Avun saaminen

Jos juutut tai sinulla on kysymyksiä tekoälysovellusten rakentamisesta, liity:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotearvioita tai kohtaat virheitä rakentamisen aikana, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, on otettava huomioon, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeitä tietoja varten suosittelemme ammatillista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä johtuvista väärinkäsityksistä tai väärin tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->