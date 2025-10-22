<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:07:37+00:00",
  "source_file": "README.md",
  "language_code": "fi"
}
-->
# Co-op Translator

_Automaattinen tapa kääntää opetusmateriaalisi GitHubissa useille kielille ja tavoittaa kansainvälinen yleisö._

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

#### Tuettu [Co-op Translatorilla](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Yleiskatsaus

**Co-op Translator** auttaa sinua kääntämään opetusmateriaalisi GitHubissa nopeasti useille kielille, jolloin tavoitat kansainvälisen yleisön helposti. Kun päivität Markdown-tiedostoja, kuvia tai Jupyter-notebookeja, käännökset synkronoidaan automaattisesti, jotta opetusmateriaalisi pysyy ajantasaisena ja relevanttina kansainvälisille käyttäjille.

Katso, miten Co-op Translator järjestää käännetyn opetusmateriaalin GitHubissa:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.fi.png)

## Nopea aloitus

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimiasennus

- Luo `.env` käyttämällä pohjaa: [.env.template](../../.env.template)
- Määritä yksi LLM-palveluntarjoaja (Azure OpenAI tai OpenAI)
- Kuvien kääntämiseen (`-img`) tarvitset myös Azure AI Visionin
- Suositus: Jos sinulla on käännöksiä muista työkaluista, siivoa ne ensin, jotta vältyt ristiriidoilta (esim. `translations/`).
- Suositus: Lisää README-tiedostoosi käännösosio käyttäen [README languages template](./README_languages_template.md)
- Katso: [Azure AI:n käyttöönotto](./getting_started/set-up-azure-ai.md)

## Käyttö

Käännä kaikki tuetut tiedostotyypit:

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

Vain notebookit:

```bash
translate -l "zh" -nb
```

Lisää lippuja: [Komentojen viite](./getting_started/command-reference.md)

## Ominaisuudet

- Automaattinen käännös Markdownille, notebookeille ja kuville
- Pitää käännökset synkronoituna lähdemateriaalin muutosten kanssa
- Toimii paikallisesti (CLI) tai CI-ympäristössä (GitHub Actions)
- Käyttää Azure OpenAI:ta tai OpenAI:ta; valinnainen Azure AI Vision kuvien kääntämiseen
- Säilyttää Markdownin muotoilun ja rakenteen

## Dokumentaatio

- [Komentorivin opas](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions -opas (Julkiset repositoriot & tavalliset salaisuudet)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions -opas (Microsoft-organisaation repositoriot & organisaatiotason asetukset)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Tuetut kielet](./getting_started/supported-languages.md)
- [Vianmääritys](./getting_started/troubleshooting.md)

## Tue meitä ja edistä kansainvälistä oppimista

Liity mukaan mullistamaan opetusmateriaalin jakamista maailmanlaajuisesti! Anna [Co-op Translatorille](https://github.com/azure/co-op-translator) ⭐ GitHubissa ja tue missiotamme poistaa kielimuurit oppimisessa ja teknologiassa. Kiinnostuksesi ja panoksesi ovat tärkeitä! Koodipanokset ja ominaisuusehdotukset ovat aina tervetulleita.

### Tutustu Microsoftin opetusmateriaaleihin omalla kielelläsi

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

## Videotallenteet

Opi lisää Co-op Translatorista esitystemme kautta _(Klikkaa kuvaa alla katsoaksesi YouTubessa.)_:

- **Open at Microsoft**: Lyhyt 18 minuutin esittely ja pikaopas Co-op Translatorin käyttöön.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.fi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Osallistuminen

Tämä projekti toivottaa tervetulleeksi panokset ja ehdotukset. Kiinnostaako osallistua Azure Co-op Translatoriin? Katso [CONTRIBUTING.md](./CONTRIBUTING.md) ohjeet, miten voit auttaa tekemään Co-op Translatorista saavutettavamman.

## Tekijät

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käyttäytymissäännöt

Tässä projektissa noudatetaan [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Lisätietoja löydät [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) -sivulta tai
voit ottaa yhteyttä [opencode@microsoft.com](mailto:opencode@microsoft.com) lisäkysymyksissä tai kommenteissa.

## Vastuullinen tekoäly

Microsoft on sitoutunut auttamaan asiakkaitaan käyttämään tekoälytuotteita vastuullisesti, jakamaan oppimaansa ja rakentamaan luottamukseen perustuvia kumppanuuksia työkalujen, kuten Transparency Notes ja Impact Assessments, avulla. Monet näistä resursseista löytyvät osoitteesta [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftin vastuullisen tekoälyn periaatteet perustuvat oikeudenmukaisuuteen, luotettavuuteen ja turvallisuuteen, yksityisyyteen ja tietoturvaan, osallisuuteen, läpinäkyvyyteen ja vastuullisuuteen.

Laajamittaiset kieli-, kuva- ja puhemallit – kuten tässä esimerkissä käytetyt – voivat joskus toimia epäoikeudenmukaisesti, epäluotettavasti tai loukkaavasti, mikä voi aiheuttaa haittaa. Tutustu [Azure OpenAI -palvelun Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) -dokumenttiin, jotta tiedät riskit ja rajoitukset.

Suositeltu tapa riskien hallintaan on sisällyttää turvallisuusjärjestelmä arkkitehtuuriin, joka tunnistaa ja estää haitallisen toiminnan. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tarjoaa riippumattoman suojakerroksen, joka tunnistaa haitallista käyttäjä- ja tekoälytuotettua sisältöä sovelluksissa ja palveluissa. Azure AI Content Safety sisältää tekstin ja kuvien API:t, joiden avulla voit tunnistaa haitallista materiaalia. Lisäksi käytettävissä on interaktiivinen Content Safety Studio, jossa voit tarkastella, kokeilla ja testata esimerkkikoodia haitallisen sisällön tunnistamiseen eri muodoissa. Seuraava [pikaopas](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) opastaa palvelun käyttöönotossa.
Toinen huomioon otettava seikka on sovelluksen yleinen suorituskyky. Monimuotoisissa ja monimallisissa sovelluksissa suorituskyvyllä tarkoitetaan sitä, että järjestelmä toimii sinun ja käyttäjiesi odotusten mukaisesti, eikä esimerkiksi tuota haitallisia tuloksia. On tärkeää arvioida koko sovelluksen suorituskykyä hyödyntämällä [generoinnin laatua sekä riski- ja turvallisuusmittareita](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Voit arvioida tekoälysovellustasi kehitysympäristössä käyttämällä [prompt flow SDK:ta](https://microsoft.github.io/promptflow/index.html). Kun käytössäsi on testiaineisto tai kohde, generatiivisen tekoälysovelluksesi tuotokset mitataan määrällisesti sisäänrakennetuilla arviointityökaluilla tai omilla arvioijillasi. Jos haluat aloittaa järjestelmäsi arvioinnin prompt flow SDK:lla, voit seurata [pikaopasta](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kun olet suorittanut arviointiajon, voit [visualisoida tulokset Azure AI Studiossa](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Tavara­merkit

Tämä projekti saattaa sisältää tavaramerkkejä tai logoja, jotka liittyvät projekteihin, tuotteisiin tai palveluihin. Microsoftin tavaramerkkien tai logojen luvallinen käyttö edellyttää, että noudatat [Microsoftin tavaramerkki- ja brändiohjeita](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general). Microsoftin tavaramerkkien tai logojen käyttö muokatuissa versioissa tästä projektista ei saa aiheuttaa sekaannusta tai antaa ymmärtää, että Microsoft tukee projektia. Kolmansien osapuolten tavaramerkkien tai logojen käyttöön sovelletaan kyseisten tahojen käytäntöjä.

## Apua saatavilla

Jos jäät jumiin tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity mukaan:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Jos haluat antaa palautetta tuotteesta tai kohtaat virheitä kehitystyössä, käy osoitteessa:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisissä tapauksissa suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinkäsityksistä tai tulkintavirheistä.