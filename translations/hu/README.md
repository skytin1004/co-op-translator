# Co-op Translator

_Könnyedén automatizálhatja és tarthatja karban oktatási GitHub tartalmai fordítását több nyelven projektje fejlődése során._

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

#### Támogatja a [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arab](../ar/README.md) | [Bengáli](../bn/README.md) | [Bolgár](../bg/README.md) | [Burmai (Myanmar)](../my/README.md) | [Kínai (egyszerűsített)](../zh-CN/README.md) | [Kínai (hagyományos, Hongkong)](../zh-HK/README.md) | [Kínai (hagyományos, Makaó)](../zh-MO/README.md) | [Kínai (hagyományos, Tajvan)](../zh-TW/README.md) | [Horvát](../hr/README.md) | [Cseh](../cs/README.md) | [Dán](../da/README.md) | [Holland](../nl/README.md) | [Észt](../et/README.md) | [Finn](../fi/README.md) | [Francia](../fr/README.md) | [Német](../de/README.md) | [Görög](../el/README.md) | [Héber](../he/README.md) | [Hindi](../hi/README.md) | [Magyar](./README.md) | [Indonéz](../id/README.md) | [Olasz](../it/README.md) | [Japán](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreai](../ko/README.md) | [Litván](../lt/README.md) | [Maláj](../ms/README.md) | [Malajálam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepáli](../ne/README.md) | [Nigériai pidgin](../pcm/README.md) | [Norvég](../no/README.md) | [Perzsa (Fárszi)](../fa/README.md) | [Lengyel](../pl/README.md) | [Portugál (Brazília)](../pt-BR/README.md) | [Portugál (Portugália)](../pt-PT/README.md) | [Pandzsábi (Gurmukhi)](../pa/README.md) | [Román](../ro/README.md) | [Orosz](../ru/README.md) | [Szerb (Cirill)](../sr/README.md) | [Szlovák](../sk/README.md) | [Szlovén](../sl/README.md) | [Spanyol](../es/README.md) | [Szuahéli](../sw/README.md) | [Svéd](../sv/README.md) | [Tagalog (Filippínó)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Török](../tr/README.md) | [Ukrán](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamita](../vi/README.md)

> **Szeretné helyben klónozni?**
>
> Ez a tároló több mint 50 nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. A fordítások nélküli klónozáshoz használja a sparse checkout-ot:
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
> Ez minden szükséges fájlt biztosít a kurzus elvégzéséhez sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Áttekintés

A **Co-op Translator** segít Önnek oktatási GitHub tartalmának több nyelvre könnyed lokalizálásában.  
Amikor frissíti Markdown fájljait, képeit vagy jegyzetfüzeteit, a fordítások automatikusan szinkronizálódnak, ezáltal biztosítva, hogy tartalma pontos és naprakész maradjon a tanulók számára világszerte.

Példa arra, hogyan van szervezve a lefordított tartalom:

![Példa](../../translated_images/hu/translation-ex.0c8aa6a7ee0aad2b.webp)

## Hogyan kezeljük a fordítási állapotot

A Co-op Translator a lefordított tartalmat **verziózott szoftver-artefaktumokként** kezeli,  
nem statikus fájlként.

Az eszköz a lefordított Markdown, képek és jegyzetfüzetek állapotát  
**nyelvre lebontott metaadatok** segítségével követi nyomon.

Ez a kialakítás lehetővé teszi a Co-op Translator számára, hogy:

- Megbízhatóan felismerje az elavult fordításokat
- Egységesen kezelje a Markdown, képeket és jegyzetfüzeteket
- Biztonságosan skálázódjon nagy, gyorsan változó, többnyelvű tárolók esetén

Azáltal, hogy a fordításokat kezelt artefaktumokként modellezi,  
a fordítási munkafolyamatok természetesen illeszkednek a modern  
szoftverfüggőségi és artefaktum-kezelési gyakorlatokhoz.

→ [Hogyan kezeljük a fordítás állapotát](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Gyors kezdés

```bash
# Virtuális környezet létrehozása és aktiválása (ajánlott)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Csomag telepítése
pip install co-op-translator
# Fordítás
translate -l "ko ja fr" -md
```

Docker:

```bash
# Húzza le a nyilvános képet a GHCR-ről
docker pull ghcr.io/azure/co-op-translator:latest
# Futtassa az aktuális mappával csatolva és a .env fájllal ellátva (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimális beállítás

1. Ellenőrizze, hogy támogatott Python verzióval rendelkezik-e (jelenleg 3.10-3.12). A poetry (pyproject.toml) ezt automatikusan kezeli.
2. Hozzon létre egy `.env` fájlt a sablon alapján: [.env.template](../../.env.template)
3. Állítson be egy LLM szolgáltatót (Azure OpenAI vagy OpenAI)
4. (Opcionális) Képfordításhoz (`-img`) állítsa be az Azure AI Vision-t
5. (Opcionális) Több hitelesítési készletet is beállíthat a változók *_1*, *_2* stb. suffix-szel való duplikálásával. Egy készlet összes változójának ugyanazt a suffix-et kell megosztania.
6. (Ajánlott) Törölje a korábbi fordításokat az esetleges ütközések elkerülésére (például `translations/`)
7. (Ajánlott) Adjon hozzá egy fordítási szekciót a README-jéhez a [README languages template](./getting_started/README_languages_template.md) segítségével
8. Tekintse meg: [Azure AI beállítása](./getting_started/set-up-azure-ai.md)

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

## Funkciók

- Automatikus fordítás Markdown-hoz, jegyzetfüzetekhez és képekhez
- Szinkronban tartja a fordításokat az eredeti változásokkal
- Helyben (CLI) vagy CI-ben (GitHub Actions) működik
- Használja az Azure OpenAI-t vagy OpenAI-t; kép esetén opcionálisan az Azure AI Vision-t
- Megőrzi a Markdown formázást és szerkezetet

## Dokumentációk

- [Parancssori útmutató](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions útmutató (nyilvános tárolók és szabványos titkok)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions útmutató (Microsoft szervezeti tárolók és szervezeti szintű beállítások)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README nyelvek sablon](./getting_started/README_languages_template.md)
- [Támogatott nyelvek](./getting_started/supported-languages.md)
- [Közreműködés](./CONTRIBUTING.md)
- [Hibaelhárítás](./getting_started/troubleshooting.md)

### Microsoft-specifikus útmutató
> [!NOTE]
> Csak a Microsoft “For Beginners” tárolóinak karbantartói számára.

- [„Egyéb kurzusok” lista frissítése (csak MS Beginners tárolókhoz)](./getting_started/update-other-courses.md)

## Támogasson minket és segítse a globális tanulást

Csatlakozzon hozzánk az oktatási tartalom globális megosztásának forradalmasításában! Adjon egy ⭐ értékelést a [Co-op Translator](https://github.com/azure/co-op-translator) GitHub oldalán, és támogassa küldetésünket, hogy lebontsuk a nyelvi akadályokat a tanulás és a technológia területén. Az Ön érdeklődése és hozzájárulásai jelentős hatással vannak! A kódhoz való hozzájárulásokat és funkciójavaslatokat mindig szívesen fogadjuk.

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

## Videó bemutatók

👉 Kattintson az alábbi képre a YouTube-on való megtekintéshez.

- **Open at Microsoft**: Egy rövid, 18 perces bevezető és gyors útmutató a Co-op Translator használatához.

  [![Open at Microsoft](../../translated_images/hu/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Közreműködés

Ez a projekt várja a hozzájárulásokat és javaslatokat. Érdekli, hogy hozzájáruljon az Azure Co-op Translator fejlesztéséhez? Kérjük, olvassa el a [CONTRIBUTING.md](./CONTRIBUTING.md) fájlt, amely útmutatást ad arról, hogyan segíthet abban, hogy a Co-op Translator elérhetőbb legyen.

## Közreműködők
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Magatartási kódex

Ez a projekt átvette a [Microsoft Open Source Magatartási Kódexét](https://opensource.microsoft.com/codeofconduct/).
További információkért lásd a [Magatartási kódex GYIK](https://opensource.microsoft.com/codeofconduct/faq/) részt, vagy
keresse a [opencode@microsoft.com](mailto:opencode@microsoft.com) címet további kérdésekkel vagy észrevételekkel.

## Felelős MI

A Microsoft elkötelezett amellett, hogy ügyfeleink felelősségteljesen használhassák MI-termékeinket, megossza tanulságainkat, és bizalmon alapuló partnerségeket építsen olyan eszközök, mint a Transzparencia Jegyzetek és Hatásvizsgálatok segítségével. Ezeknek a forrásoknak sok található a [https://aka.ms/RAI](https://aka.ms/RAI) címen.
A Microsoft felelős MI-hoz való megközelítése az MI alapelveinken alapszik: méltányosság, megbízhatóság és biztonság, adatvédelem és biztonság, befogadás, átláthatóság és elszámoltathatóság.

A nagy méretű természetes nyelvi, képi és beszédmodellek - mint amilyeneket ebben a példában használnak - potenciálisan méltánytalan, megbízhatatlan vagy sértő viselkedést tanúsíthatnak, ami károkat okozhat. Kérjük, tekintse meg az [Azure OpenAI szolgáltatás Transzparencia jegyzetét](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) a kockázatok és korlátok megismeréséhez.

A kockázatok csökkentésének ajánlott módja, hogy az architektúrájában biztonsági rendszert épít be, amely képes felismerni és megelőzni a káros viselkedést. Az [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) egy független védelmi réteget biztosít, amely képes felismerni a káros, felhasználó által generált és MI által generált tartalmakat alkalmazásokban és szolgáltatásokban. Az Azure AI Content Safety szöveg- és képi API-kat tartalmaz, melyek lehetővé teszik a káros anyagok felismerését. Ezenkívül interaktív Content Safety Studio áll rendelkezésre, amely lehetővé teszi a káros tartalom különböző modalitásokban történő felismerését szolgáló mintakódok megtekintését, felfedezését és kipróbálását. A következő [gyorsindítási dokumentáció](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) útmutatót ad a szolgáltatásnak történő kéréshez.

Egy másik figyelembe veendő szempont az alkalmazás általános teljesítménye. A többmodalitású és többmodellű alkalmazások esetében a teljesítmény azt jelenti, hogy a rendszer úgy működik, ahogy Ön és a felhasználók elvárják, beleértve, hogy nem generál káros kimeneteket. Fontos felmérni az alkalmazás teljesítményét [generálási minőség és kockázat- és biztonsági mutatók](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) használatával.

Az AI alkalmazását fejlesztői környezetben is értékelheti a [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) segítségével. Legyen az tesztadatkészlet vagy célkitűzés, generatív AI alkalmazásának generációit beépített vagy választott egyéni értékelők segítségével számszerűsítheti. Az értékelő SDK-hoz való gyors kezdéshez kövesse a [gyorsindítási útmutatót](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Értékelés lefuttatása után a [Azure AI Studio-ban megtekintheti az eredményeket](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Védjegyek

Ez a projekt tartalmazhat védjegyeket vagy logókat projektekhez, termékekhez vagy szolgáltatásokhoz kapcsolódóan. A Microsoft védjegyek vagy logók jogos használata függ
a [Microsoft Védjegy- és Márka irányelveitől](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
A Microsoft védjegyek vagy logók használata az ezen projekt módosított verzióiban nem okozhat zavart, és nem sugallhat Microsoft szponzorálást.
Harmadik fél védjegyeinek vagy logóinak használata azok irányelveinek alá tartozik.

## Segítségkérés

Ha elakad vagy kérdése van az MI-alkalmazások építésével kapcsolatban, csatlakozzon:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék visszajelzése vagy hibái vannak építés közben, látogasson el:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Kritikus információk esetén szakmai emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->