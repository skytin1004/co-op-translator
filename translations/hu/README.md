# Co-op Translator

_Könnyedén automatizálhatja és tarthatja karban oktatási GitHub-tartalmai fordításait több nyelven projektje fejlődése során._

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

### 🌐 Többnyelvű támogatás

#### A [Co-op Translator](https://github.com/Azure/Co-op-Translator) támogatásával

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](./README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Szeretné helyben klónozni?**
>
> Ez a tároló több mint 50 nyelvű fordítást tartalmaz, ami jelentősen növeli a letöltési méretet. Fordítások nélkül klónozáshoz használja a sparse checkout-ot:
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
> Ez mindent megad, amire szüksége van a kurzus elvégzéséhez, sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Áttekintés

A **Co-op Translator** segít, hogy oktatási GitHub-tartalmait egyszerűen lokalizálja több nyelvre.  
Amikor frissíti Markdown fájljait, képeit vagy jegyzetfüzeteit, a fordítások automatikusan szinkronban maradnak, biztosítva, hogy tartalma pontos és naprakész legyen a tanulók számára világszerte.

A fordított tartalom szervezésének példája:

![Példa](../../imgs/translation-ex.png)

## Hogyan kezeljük a fordítás állapotát

A Co-op Translator a fordított tartalmat **verziózott szoftveres artefaktumként** kezeli,  
nem pedig statikus fájlként.

Az eszköz a fordított Markdown, képek és jegyzetfüzetek állapotát  
**nyelvi hatókörű metaadatok** segítségével követi nyomon.

Ez a kialakítás lehetővé teszi, hogy a Co-op Translator:

- Megbízhatóan felismerje az elavult fordításokat
- Egységesen kezelje a Markdown, képek és jegyzetfüzetek tartalmakat
- Biztonságosan méretezhető legyen nagy, gyorsan változó, többnyelvű tárolókhoz

A fordítások menedzselt artefaktumokként való kezelése révén  
a fordítási munkamenetek természetesen illeszkednek a modern  
szoftverfüggőség- és artefaktumkezelési gyakorlatokhoz.

→ [Hogyan kezeljük a fordítás állapotát](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Gyors kezdés

```bash
# Hozzon létre és aktiváljon egy virtuális környezetet (ajánlott)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Telepítse a csomagot
pip install co-op-translator
# Fordítás
translate -l "ko ja fr" -md
```

Docker:

```bash
# Töltsük le a nyilvános képet a GHCR-ről
docker pull ghcr.io/azure/co-op-translator:latest
# Futtatás a jelenlegi mappa csatolásával és .env megadása mellett (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimális beállítás

1. Ellenőrizze, hogy támogatott Python verziót használ (jelenleg 3.10–3.12). A poetry (pyproject.toml) ezt automatikusan kezeli.
2. Hozzon létre egy `.env` fájlt az alábbi sablon alapján: [.env.template](../../.env.template)
3. Állítson be egy LLM szolgáltatót (Azure OpenAI vagy OpenAI)
4. (Opcionális) Képfordításhoz (`-img`) konfigurálja az Azure AI Vision-t
5. (Opcionális) Több hitelesítési készlet konfigurálható az `_1`, `_2` stb. végződéssel ellátott változók duplikálásával. Egy készlet minden változója ugyanazzal a végződéssel kell, hogy rendelkezzen.
6. (Ajánlott) Takarítsa ki az előző fordításokat az esetleges ütközések elkerülése érdekében (pl. `translations/`)
7. (Ajánlott) Adjon hozzá egy fordítási részt README-jéhez a [README languages template](./getting_started/README_languages_template.md) alapján
8. Lásd: [Azure AI beállítása](./getting_started/set-up-azure-ai.md)

## Használat

Fordítsa le az összes támogatott típust:

```bash
translate -l "ko ja"
```

Csak Markdown:

```bash
translate -l "de" -md
```

Markdown + képek:

```bash
translate -l "pt" -md -img
```

Csak jegyzetfüzetek:

```bash
translate -l "zh" -nb
```

További kapcsolók: [Parancs referencia](./getting_started/command-reference.md)

## Jellemzők

- Automatikus fordítás Markdown, jegyzetfüzetek és képek számára
- A fordításokat szinkronban tartja a forrásváltozásokkal
- Helyileg (CLI) vagy CI-ben (GitHub Actions) működik
- Használja az Azure OpenAI-t vagy az OpenAI-t; opcionálisan Azure AI Vision képekhez
- Megőrzi a Markdown formázást és szerkezetet

## Dokumentáció

- [Parancssori útmutató](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions útmutató (Publikus tárolók és standard titkok)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions útmutató (Microsoft szervezeti tárolók és szervezeti szintű beállítások)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Támogatott nyelvek](./getting_started/supported-languages.md)
- [Hozzájárulás](./CONTRIBUTING.md)
- [Hibaelhárítás](./getting_started/troubleshooting.md)

### Microsoft-specifikus útmutató
> [!NOTE]
> Csak a Microsoft “For Beginners” tárolóinak karbantartói számára.

- [Az „egyéb kurzusok” lista frissítése (csak MS Beginners tárolókhoz)](./getting_started/update-other-courses.md)

## Támogasson minket és segítse elő a globális tanulást

Csatlakozzon hozzánk az oktatási tartalmak globális megosztásának forradalmasításában! Adjon egy ⭐-t a [Co-op Translator](https://github.com/azure/co-op-translator) projektnek a GitHub-on, és támogassa küldetésünket, hogy lebontsuk a nyelvi akadályokat a tanulásban és a technológiában. Az érdeklődése és hozzájárulásai jelentős hatással vannak! Kódhoz való hozzájárulásokat és funkciójavaslatokat mindig szívesen fogadunk.

### Fedezze fel a Microsoft oktatási tartalmait az Ön nyelvén

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

## Videós bemutatók

👉 Kattintson az alábbi képre a YouTube-on való megtekintéshez.

- **Open at Microsoft**: Egy rövid, 18 perces bemutató és gyors útmutató a Co-op Translator használatához.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Hozzájárulás

Ez a projekt szívesen fogad hozzájárulásokat és javaslatokat. Érdekli a részvétel az Azure Co-op Translator fejlesztésében? Kérjük, tekintse meg a [CONTRIBUTING.md](./CONTRIBUTING.md) dokumentumunkat, amely útmutatást nyújt arról, hogyan segíthet abban, hogy a Co-op Translator még hozzáférhetőbb legyen.

## Közreműködők
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Magatartási kódex

Ez a projekt elfogadta a [Microsoft Open Source Magatartási Kódexet](https://opensource.microsoft.com/codeofconduct/).
További információkért lásd a [Magatartási kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) oldalt, vagy lépj kapcsolatba az [opencode@microsoft.com](mailto:opencode@microsoft.com) címen bármilyen további kérdéssel vagy észrevétellel.

## Felelős mesterséges intelligencia

A Microsoft elkötelezett amellett, hogy segítse ügyfeleit mesterséges intelligencia termékeink felelős használatában, megossza tapasztalatainkat, és bizalmon alapuló partnerségeket építsen olyan eszközök segítségével, mint a Transzparencia Jegyzetek és Hatáselemzések. Ezek közül sok elérhető a [https://aka.ms/RAI](https://aka.ms/RAI) oldalon.
A Microsoft felelős mesterséges intelligenciához való megközelítése az AI igazságossági, megbízhatósági és biztonsági, adatvédelmi és biztonsági, befogadási, átláthatósági és elszámoltathatósági elvein alapul.

A nagy léptékű természetes nyelvi, képi és beszédmodellek – mint amilyenek ebben a mintában is szerepelnek – potenciálisan igazságtalan, megbízhatatlan vagy sértő módon viselkedhetnek, ami károkat okozhat. Kérjük, tekintse meg az [Azure OpenAI szolgáltatás Transzparencia jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) annak érdekében, hogy tájékozódjon a kockázatokról és korlátokról.

A kockázatok csökkentésének ajánlott módja egy olyan biztonsági rendszer beépítése az architektúrába, amely képes felismerni és megelőzni a káros viselkedést. Az [Azure AI Tartalombiztonság](https://learn.microsoft.com/azure/ai-services/content-safety/overview) független védelmi réteget biztosít, amely képes felismerni a felhasználók és az AI által generált káros tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Tartalombiztonság szöveges és képi API-kat tartalmaz, amelyek lehetővé teszik a káros anyagok felismerését. Emellett van egy interaktív Content Safety Studio, amelyben megtekintheti, felfedezheti és ki is próbálhatja a káros tartalmak különböző modalitások szerinti felismeréséhez készült mintakódokat. A következő [gyorsinduló dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) útmutatást nyújt a szolgáltatás felé történő lekérésekhez.

Egy másik figyelembe veendő szempont az általános alkalmazási teljesítmény. Többmodális és többmodell alkalmazások esetében a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogyan Ön és felhasználói elvárják, beleértve azt is, hogy nem generál káros kimeneteket. Fontos értékelni az alkalmazás teljesítményét [a generálási minőség és a kockázat- és biztonsági metrikák](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) alapján.

Értékelheti AI alkalmazását fejlesztői környezetében a [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) használatával. Legyen szó tesztadatokról vagy célról, a generatív AI alkalmazás generációi beépített vagy az Ön által választott egyéni értékelőkkel mennyiségileg mérhetők. A prompt flow sdk használatának megkezdéséhez és rendszerének értékeléséhez követheti a [gyorsinduló útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Értékelés lefuttatása után az eredményeket megtekintheti az [Azure AI Studioban](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Márkanevek

Ez a projekt tartalmazhat projektek, termékek vagy szolgáltatások márkajelzéseit vagy logóit. A Microsoft márkáit vagy logóit való jogosult használatuk a [Microsoft márka- és védjegyirányelveinek](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general) betartásához kötött.
A Microsoft márkák vagy logók módosított verziókban történő használata nem okozhat félreértést, és nem sugallhat Microsoft támogatást.
Harmadik fél márkáinak vagy logóinak bármilyen használata az adott harmadik fél szabályzataihoz kötött.

## Segítségkérés

Ha elakad vagy kérdése van AI alkalmazások fejlesztésével kapcsolatban, csatlakozzon:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termékvisszajelzése vagy hibák jelentkeznek fejlesztés közben, látogasson el ide:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén szakmai, emberi fordítást javasolunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->