# Co-op Translator

_Lihtsalt automatiseeri ja halda oma haridusliku GitHubi sisu tõlkeid mitmesse keelde, kui su projekt areneb._

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

### 🌐 Mitmekeelne tugi

#### Toetatud [Co-op Translator](https://github.com/Azure/Co-op-Translator) poolt

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh-CN/README.md) | [Hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [Hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [Hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Khmeri](../km/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidžin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (Farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../pt-BR/README.md) | [Portugali (Portugal)](../pt-PT/README.md) | [Pandžabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Slovaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suaheli](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalogi (Filipino)](../tl/README.md) | [Tamili](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Eelistad kloonimist lokaalselt?**
>
> See hoidla sisaldab üle 50 keele tõlget, mis suurendab märkimisväärselt allalaadimise mahtu. Tõlgeteta kloonimiseks kasuta sparse checkout'i:
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
> See annab sulle kõik vajaliku kursuse lõpetamiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ülevaade

**Co-op Translator** aitab sul hõlpsasti lokaliseerida oma hariduslikku GitHubi sisu mitmesse keelde.
Kui uuendad oma Markdown-faile, pilte või märkmikke, püsivad tõlked automaatselt sünkroonis, tagades, et su sisu on õppijatele üle maailma täpne ja ajakohane.

Näide sellest, kuidas tõlgitud sisu on organiseeritud:

![Example](../../translated_images/et/translation-ex.0c8aa6a7ee0aad2b.webp)

## Kuidas tõlke olekut hallatakse

Co-op Translator haldab tõlgitud sisu kui **versioonitud tarkvaraartefakte**,  
mitte staatiliste failidena.

Tööriist jälgib tõlgitud Markdown'i, piltide ja märkmike olekut
kasutades **keelepiirilist metaandmeid**.

See disain võimaldab Co-op Translatoril:

- Usaldusväärselt tuvastada aegunud tõlkeid
- Kohtleda Markdown'i, pilte ja märkmikke ühtselt
- Ohutult skaleeruda suurtes, kiiresti arenevates mitmekeelsetes hoidlates

Tõlgete modelleerimisel kui hallatavaid artefakte
joondub tõlkelõim loomulikult kaasaegsete
tarkvara sõltuvuste ja artefaktihalduse praktikatega.

→ [Kuidas tõlke olekut hallatakse](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Kiirkäivitus

```bash
# Loo ja aktiveeri virtuaalne keskkond (soovitatav)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Paigalda pakett
pip install co-op-translator
# Tõlgi
translate -l "ko ja fr" -md
```

Docker:

```bash
# Tõmba avalik pilt GHCR-ist
docker pull ghcr.io/azure/co-op-translator:latest
# Käivita koos praeguse kaustaga ja .env failiga (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimaalne seadistus

1. Veendu, et sul on toetatud Pythoniversioon (praegu 3.10-3.12). Poetry (pyproject.toml) puhul on see automaatne.
2. Loo `.env` fail kasutades mustandit: [.env.template](../../.env.template)
3. Konfigureeri üks LLM pakkuja (Azure OpenAI või OpenAI)
4. (Valikuline) Piltide tõlke jaoks (`-img`) konfigureeri Azure AI Vision
5. (Valikuline) Võid seadistada mitu volituste komplekti, duplitseerides muutujad sufiksitega nagu `_1`, `_2` jne. Kõik komplekti muutujad peavad omama sama sufiksit.
6. (Soovitatav) Puhasta eelmised tõlked konflikti vältimiseks (nt `translations/`)
7. (Soovitatav) Lisa tõlke sektsioon oma README-sse, kasutades [README keelte mustandit](./getting_started/README_languages_template.md)
8. Vaata: [Azure AI seadistamine](./getting_started/set-up-azure-ai.md)

## Kasutus

Tõlgi kõik toetatud tüübid:

```bash
translate -l "ko ja"
```

Ainult Markdown:

```bash
translate -l "de" -md
```

Markdown + pildid:

```bash
translate -l "pt" -md -img
```

Ainult märkmikud:

```bash
translate -l "zh" -nb
```

Rohkem lippe: [Käsurea viide](./getting_started/command-reference.md)

## Funktsioonid

- Automatiseeritud tõlge Markdownile, märkmikele ja piltidele
- Hoiab tõlked sünkroonis lähte muudatustega
- Töötab lokaalselt (CLI) või CI-s (GitHub Actions)
- Kasutab Azure OpenAI või OpenAI; vabatahtlik Azure AI Vision piltidele
- Säilitab Markdowni vormingu ja struktuuri

## Dokumentatsioon

- [Käsurea juhend](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions juhend (avalikud hoidlad & standardsaladused)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions juhend (Microsofti organisatsiooni hoidlad & organisatsiooni tasemel seadistused)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README keelte mall](./getting_started/README_languages_template.md)
- [Toetatud keeled](./getting_started/supported-languages.md)
- [Panustamine](./CONTRIBUTING.md)
- [Veaotsing](./getting_started/troubleshooting.md)

### Microsoftile spetsiifiline juhend
> [!NOTE]
> Ainult Microsoft “Algajate jaoks” hoidlate hooldajatele.

- [“Muude kursuste” nimekirja uuendamine (ainult MS Algajate hoidlad)](./getting_started/update-other-courses.md)

## Toeta meid ja edenda ülemaailmset õppimist

Liitu meiega haridusliku sisu ülemaailmse jagamise revolutsioonis! Anna [Co-op Translatorile](https://github.com/azure/co-op-translator) GitHubis ⭐ ja toeta meie missiooni murda keelebarjäärid õppimisel ja tehnoloogias. Sinu huvi ja panused mõjutavad oluliselt! Koodipanused ja funktsioonisoovitused on alati oodatud.

### Avasta Microsofti hariduslikku sisu oma keeles

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

## Videoesitlused

👉 Klõpsa alloleval pildil, et vaadata YouTube'is.

- **Open at Microsoft**: Lühike 18-minutiline sissejuhatus ja kiire juhend Co-op Translatori kasutamiseks.

  [![Open at Microsoft](../../translated_images/et/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Panustamine

See projekt võtab vastu panuseid ja ettepanekuid. Huvi Azure Co-op Translatori arendamise vastu? Palun vaata meie [CONTRIBUTING.md](./CONTRIBUTING.md), kuidas saad aidata teha Co-op Translatori paremini ligipääsetavaks.

## Panustajad
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käitumiskoodeks

See projekt on võtnud kasutusele [Microsoft Open Source käitumiskoodeksi](https://opensource.microsoft.com/codeofconduct/).
Rohkem teavet leiate [käitumiskoodeksi KKK-st](https://opensource.microsoft.com/codeofconduct/faq/) või pöörduge täiendavate küsimuste või kommentaaride korral aadressile [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Vastutustundlik tehisintellekt

Microsoft on pühendunud aitama meie klientidel kasutada meie tehisintellekti tooteid vastutustundlikult, jagades meie õppetunde ja luues usaldusel põhinevaid partnerlusi tööriistade nagu Transparency Notes ja Impact Assessments kaudu. Paljusid neist ressurssidest leiate aadressilt [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie tehisintellekti põhimõtetel: õiglus, usaldusväärsus ja ohutus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja vastutus.

Suurte keele-, pildi- ja kõnemudelite puhul - nagu neid kasutatakse selles näites - võib esineda ebaõiglast, ebausaldusväärset või solvavat käitumist, mis omakorda võib põhjustada kahju. Palun tutvuge [Azure OpenAI teenuse läbipaistvuse märkusega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et olla teadlik riskidest ja piirangutest.

Soovitatav lähenemisviis nende riskide maandamiseks on lisada oma arhitektuuri ohutussüsteem, mis suudab tuvastada ja takistada kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutajate loodud ja AI loodud sisu. Azure AI Content Safety sisaldab teksti- ja pildirakenduste programmeerimisliideseid, mis võimaldavad tuvastada kahjulikku materjali. Meil on ka interaktiivne Content Safety Studio, mis võimaldab teil vaadata, uurida ja proovida näidiskoodi kahjuliku sisu tuvastamiseks erinevates modalitydes. Järgmine [kiirjuhendi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenusele päringute tegemisel.

Teiseks aspektiks, mida arvesse võtta, on kogu rakenduse jõudlus. Mitme moodali ja mitme mudeliga rakenduste puhul tähistame jõudlust selle järgi, et süsteem toimib nii, nagu teie ja teie kasutajad ootavad, sealhulgas ei genereeri kahjulikke väljundeid. On oluline hinnata kogu oma rakenduse jõudlust kasutades [generatsiooni kvaliteedi ja riski ning ohutuse mõõdikuid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Saate hinnata oma tehisintellekti rakendust oma arenduskeskkonnas, kasutades [prompt flow SDK-d](https://microsoft.github.io/promptflow/index.html). Kasutades kas testandmestikku või sihtmärki, mõõdetakse teie generatiivse tehisintellekti rakenduse generatsioone kvantitatiivselt sisseehitatud või teie enda valitud kohandatud hindajatega. Prompt flow SDK-ga alustamiseks ja oma süsteemi hindamiseks võite järgida [kiirjuhendi](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamisjooksu käivitanud, saate [tulemusi visualiseerida Azure AI Studios](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode autoriseeritud kasutamine on reguleeritud ja peab järgima
[Microsofti kaubamärgi- ja brändijuhiseid](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine selle projekti muundatud versioonides ei tohi tekitada segadust ega jätta muljet, et Microsoft seda sponsoreerib.
Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende osapoolte poliitikatele.

## Abi saamine

Kui te jääte hätta või teil on küsimusi AI rakenduste ehitamise kohta, liituge:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kui teil on toodete kohta tagasisidet või ehitamisel tekkivaid vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastutusest loobumine**:  
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüame täpsust, palun pange tähele, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Originaaldokument oma emakeeles tuleks pidada autoriteetseks allikaks. Kriitilise info puhul soovitatakse professionaalset inimtõlget. Me ei vastuta mis tahes arusaamatuste või valesti mõistmiste eest, mis tulenevad selle tõlke kasutamisest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->