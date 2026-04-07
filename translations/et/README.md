# Co-op Translator

_Lihtsasti automatiseeri ja halda tõlkeid oma haridusliku GitHubi sisu jaoks mitmes keeles, kui su projekt areneb._

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

### 🌐 Mitmekeelse toe

#### Toetatud [Co-op Translator](https://github.com/Azure/Co-op-Translator) poolt

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Araabia](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgaaria](../bg/README.md) | [Birma (Myanmar)](../my/README.md) | [Hiina (lihtsustatud)](../zh-CN/README.md) | [Hiina (traditsiooniline, Hongkong)](../zh-HK/README.md) | [Hiina (traditsiooniline, Macau)](../zh-MO/README.md) | [Hiina (traditsiooniline, Taiwan)](../zh-TW/README.md) | [Horvaadi](../hr/README.md) | [Tšehhi](../cs/README.md) | [Taani](../da/README.md) | [Hollandi](../nl/README.md) | [Eesti](./README.md) | [Soome](../fi/README.md) | [Prantsuse](../fr/README.md) | [Saksa](../de/README.md) | [Kreeka](../el/README.md) | [Heebrea](../he/README.md) | [Hindi](../hi/README.md) | [Ungari](../hu/README.md) | [Indoneesia](../id/README.md) | [Itaalia](../it/README.md) | [Jaapani](../ja/README.md) | [Kannada](../kn/README.md) | [Khmeeri](../km/README.md) | [Korea](../ko/README.md) | [Leedu](../lt/README.md) | [Malai](../ms/README.md) | [Malajalami](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigeeria pidgin](../pcm/README.md) | [Norra](../no/README.md) | [Pärsia (farsi)](../fa/README.md) | [Poola](../pl/README.md) | [Portugali (Brasiilia)](../pt-BR/README.md) | [Portugali (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumeenia](../ro/README.md) | [Vene](../ru/README.md) | [Serbia (kirillitsa)](../sr/README.md) | [Sloveaki](../sk/README.md) | [Sloveeni](../sl/README.md) | [Hispaania](../es/README.md) | [Suahiili](../sw/README.md) | [Rootsi](../sv/README.md) | [Tagalog (filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Tai](../th/README.md) | [Türgi](../tr/README.md) | [Ukraina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnami](../vi/README.md)

> **Eelistad kloonida lokaalselt?**
>
> See reposiit sisaldab üle 50 keele tõlget, mis suurendab märkimisväärselt allalaadimise suurust. Tõlgeteta kloonimiseks kasuta kihilist checkout'i (sparse checkout):
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
> See annab sulle kõik vajaliku kursuse läbimiseks palju kiirema allalaadimisega.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Ülevaade

**Co-op Translator** aitab sul lihtsalt lokaliseerida oma hariduslikku GitHubi sisu mitmesse keelde. Kui sa uuendad Markdown-faile, pilte või sülearvuteid, hoiavad tõlked end automaatselt sünkroonis, tagades, et su sisu on õige ja ajakohane õppijatele üle maailma.

Näide, kuidas tõlgitud sisu on organiseeritud:

![Example](../../imgs/translation-ex.png)

## Kuidas tõlke olekut hallatakse

Co-op Translator haldab tõlgitud sisu kui **versioonitud tarkvaraartefakte**,  
mitte staatiliste failidena.

Tööriist jälgib tõlgitud Markdowni, piltide ja sülearvutite olekut
kasutades **keelepiiranguga metaandmeid**.

See disain võimaldab Co-op Translatoril:

- Usaldusväärselt avastada aegunud tõlkeid
- Käsitleda Markdownit, pilte ja sülearvuteid ühtselt
- Ohutult skaleeruda suurtes, kiiresti arenevates mitmekeelsetes hoidlates

Tõlkeid haldatud artefaktidena modelleerides,
ühinevad tõlketöövood loomulikult kaasaegse
tarkvara sõltuvuste ja artefaktihalduse praktikatega.

→ [Kuidas tõlke olekut hallatakse](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Kiire algus

```bash
# Loo ja aktiveeri virtuaalkeskkond (soovitatav)
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
# Käivita praeguse kaustaga ja .env-failiga (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimaalne seadistus

1. Kontrolli, et sul on toetatud Python versioon (praegu 3.10-3.12). Poetry's (pyproject.toml) on see automaatselt lahendatud.
2. Loo `.env` fail, kasutades mallina: [.env.template](../../.env.template)
3. Sea üks LLM-teenuse pakkuja (Azure OpenAI või OpenAI)
4. (Vabatahtlik) Pilditõlke jaoks (`-img`) sea Azure AI Vision
5. (Vabatahtlik) Saad seadistada mitu volituste komplekti, kopeerides muutujad sufiksiga nagu `_1`, `_2` jne. Kõik komplekti muutujad peavad jagama sama sufiksit.
6. (Soovitatav) Puhasta varasemad tõlked, et vältida konflikte (nt `translations/`)
7. (Soovitatav) Lisa tõlke sektsioon oma README faili, kasutades [README keelte malli](./getting_started/README_languages_template.md)
8. Vaata: [Sea üles Azure AI](./getting_started/set-up-azure-ai.md)

## Kasutusjuhend

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

Ainult sülearvutid:

```bash
translate -l "zh" -nb
```

Rohkem lippe: [Käsurea viide](./getting_started/command-reference.md)

## Omadused

- Automaatne tõlge Markdowni, sülearvutite ja piltide jaoks
- Hoiab tõlked sünkroonis allika muudatustega
- Töötab lokaalselt (CLI) või CI-s (GitHub Actions)
- Kasutab Azure OpenAI või OpenAI; vabatahtlik Azure AI Vision piltide jaoks
- Säilitab Markdowni vorminduse ja struktuuri

## Dokumentatsioon

- [Käsurea juhend](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions juhend (avalikud hoidlad & tavalised salajased võtmed)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions juhend (Microsofti organisatsiooni hoidlad & organisatsioonitasandi seadistused)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README keelte mall](./getting_started/README_languages_template.md)
- [Toetatud keeled](./getting_started/supported-languages.md)
- [Panustamine](./CONTRIBUTING.md)
- [Probleemide lahendamine](./getting_started/troubleshooting.md)

### Microsofti-spetsiifiline juhend
> [!NOTE]
> Ainult Microsofti “Algajate” hoidlate hooldajatele.

- [“Muud kursused” nimekirja uuendamine (ainult MS Algajate hoidlad)](./getting_started/update-other-courses.md)

## Toeta meid ja edenda globaalseid õppimisvõimalusi

Liitu meiega haridusliku sisu jagamise revolutsioonis ülemaailmselt! Anna [Co-op Translator](https://github.com/azure/co-op-translator) GitHubis ⭐ ning toeta meie missiooni lõhkuda keelebarjääre õppimisel ja tehnikas. Su huvi ja panused avaldavad suurt mõju! Koodi panused ja funktsioonisoovitused on alati teretulnud.

### Uuri Microsofti haridussisu oma keeles

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
- [Kyberturvalisus algajatele](https://github.com/microsoft/Security-101)
- [Veebi arendus algajatele](https://aka.ms/webdev-beginners)
- [IOT algajatele](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Videotesitlused

👉 Klõpsa allolevale pildile, et vaadata YouTube’is.

- **Open at Microsoft**: Lühike 18-minutiline sissejuhatus ja kiire juhend, kuidas Co-op Translatorit kasutada.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Panustamine

See projekt ootab panuseid ja ettepanekuid. Huvi panustada Azure Co-op Translatorisse? Palun vaata meie [CONTRIBUTING.md](./CONTRIBUTING.md), kust leiad juhised, kuidas aidata muuta Co-op Translator kättesaadavamaks.

## Kaasalööjad
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Käitumiskoodeks

See projekt on vastu võtnud [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Lisateabe saamiseks vaadake [Käitumiskoodeksi KKK](https://opensource.microsoft.com/codeofconduct/faq/) või võtke ühendust aadressil [opencode@microsoft.com](mailto:opencode@microsoft.com) lisaküsimuste või kommentaaride puhul.

## Vastutustundlik tehisintellekt

Microsoft on pühendunud aitama oma kliente kasutada meie AI tooteid vastutustundlikult, jagades oma kogemusi ja luues usaldusel põhinevaid partnertsuhteid tööriistadega nagu Transparency Notes ja Impact Assessments. Palju neist ressurssidest on leitavad aadressil [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofti lähenemine vastutustundlikule tehisintellektile põhineb meie AI põhimõtetel: õiglus, usaldusväärsus ja turvalisus, privaatsus ja turvalisus, kaasatus, läbipaistvus ja aruandekohustus.

Suurte andmemahtudega loomuliku keele, pildi ja kõne mudelid – nagu need, mida selles näites kasutatakse – võivad potentsiaalselt käituda ebaõiglaselt, ebastabiilselt või solvavalt, põhjustades kahjustusi. Palun tutvuge [Azure OpenAI teenuse läbipaistvuse märkusega](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), et saada teavet riskide ja piirangute kohta.

Soovitatav lähenemine nende riskide leevendamiseks on lisada oma arhitektuuri turvasüsteem, mis suudab tuvastada ja takistada kahjulikku käitumist. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pakub sõltumatut kaitsekihi, mis suudab rakendustes ja teenustes tuvastada kahjulikku kasutaja loodud ja AI loodud sisu. Azure AI Content Safety sisaldab teksti ja pildi API-sid, mis võimaldavad tuvastada kahjulikku materjali. Meil on ka interaktiivne Content Safety Studio, mis võimaldab vaadata, uurida ja proovida proovikoodi kahjuliku sisu tuvastamiseks eri modaliteetides. Järgmine [kiirjuhendi dokumentatsioon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) juhendab teid teenuse päringute tegemisel.

Veel üks kaalutav aspekt on kogu rakenduse jõudlus. Mitmemodaalsete ja mitmemudelsete rakenduste puhul tähendab jõudlus seda, et süsteem toimib nii, nagu teie ja teie kasutajad ootavad, sealhulgas mitte genereerides kahjulikke väljundeid. Oluline on hinnata oma kogu rakenduse jõudlust, kasutades [generatsiooni kvaliteedi ning riski- ja ohutuse mõõdikuid](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Saate oma AI rakendust hinnata oma arenduskeskkonnas, kasutades [prompt flow SDK-d](https://microsoft.github.io/promptflow/index.html). Olenevalt kas testandmekogumist või sihtmärgist mõõdetakse teie generatiivse AI rakenduse genereeringuid kvantitatiivselt sisseehitatud või teie valitud kohandatud hindajate abil. Prompt flow SDK-ga süsteemi hindamiseks alustamiseks võite järgida [kiirjuhendit](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kui olete hindamisprotsessi läbi viinud, saate [visualiseerida tulemusi Azure AI Studio's](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Kaubamärgid

See projekt võib sisaldada kaubamärke või logosid projektide, toodete või teenuste jaoks. Microsofti kaubamärkide või logode autoriseeritud kasutamine allub ja peab järgima
[Microsofti kaubamärgi ja brändi juhiseid](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Microsofti kaubamärkide või logode kasutamine selle projekti muudetud versioonides ei tohi põhjustada segadust ega vihjata Microsofti sponsorlusele.
Kolmandate osapoolte kaubamärkide või logode kasutamine allub nende kolmandate osapoolte poliitikatele.

## Abi saamine

Kui jääte hätta või teil on küsimusi AI rakenduste ehitamise kohta, liituge:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kui teil on toote tagasisidet või ehitamisel esineb vigu, külastage:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vabandus**:  
See dokument on tõlgitud kasutades tehisintellektil põhinevat tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsetes tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Tähtsate andmete puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega kaasnevate arusaamatuste ega valesti mõistmiste eest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->