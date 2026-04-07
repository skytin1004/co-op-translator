# Co-op Translator

_Ľahko automatizujte a udržiavajte preklady vášho vzdelávacieho obsahu na GitHub v rôznych jazykoch počas vývoja vášho projektu._

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

### 🌐 Podpora viacerých jazykov

#### Podporované [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](./README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferujete klonovanie lokálne?**
>
> Toto repozitár obsahuje viac ako 50 jazykových prekladov, čo výrazne zvyšuje veľkosť stiahnutia. Ak chcete klonovať bez prekladov, použite sparse checkout:
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
> Takto získate všetko potrebné pre dokončenie kurzu s oveľa rýchlejším stiahnutím.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám pomáha jednoducho lokalizovať váš vzdelávací obsah na GitHub do viacerých jazykov.  
Keď aktualizujete svoje Markdown súbory, obrázky alebo poznámkové bloky, preklady zostávajú automaticky synchronizované, aby bol váš obsah presný a aktuálny pre študentov po celom svete.

Príklad, ako je preložený obsah organizovaný:

![Example](../../imgs/translation-ex.png)

## Ako sa spravuje stav prekladu

Co-op Translator spravuje preložený obsah ako **verzionované softvérové artefakty**,  
nie ako statické súbory.

Nástroj sleduje stav preložených Markdown súborov, obrázkov a poznámkových blokov  
pomocou **metaúdajov viazaných na jazyk**.

Tento dizajn umožňuje Co-op Translator-u:

- Spoľahlivo odhaliť zastarané preklady
- Konzistentne spracovávať Markdown, obrázky a poznámkové bloky
- Bezpečne škálovať vo veľkých, rýchlo sa meniacich multi-jazykových repozitároch

Modelovaním prekladov ako spravovaných artefaktov  
sú pracovné postupy prekladu prirodzene zosúladené s modernými  
praktikami správy softvérových závislostí a artefaktov.

→ [Ako sa spravuje stav prekladu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Rýchly štart

```bash
# Vytvorte a aktivujte virtuálne prostredie (odporúčané)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainštalujte balík
pip install co-op-translator
# Preložiť
translate -l "ko ja fr" -md
```

Docker:

```bash
# Stiahnuť verejný obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spustiť s pripojenou aktuálnou zložkou a poskytnutým súborom .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimálne nastavenie

1. Uistite sa, že máte podporovanú verziu Pythonu (momentálne 3.10-3.12). V poetry (pyproject.toml) je to riešené automaticky.
2. Vytvorte súbor `.env` podľa šablóny: [.env.template](../../.env.template)
3. Nakonfigurujte jedného poskytovateľa LLM (Azure OpenAI alebo OpenAI)
4. (Voliteľné) Pre preklad obrázkov (`-img`) nakonfigurujte Azure AI Vision
5. (Voliteľné) Môžete konfigurovať viacero sád prihlasovacích údajov duplikovaním premenných s príponami ako `_1`, `_2` atď. Všetky premenne v sade musia mať rovnakú príponu.
6. (Odporúčané) Vyčistite predchádzajúce preklady, aby ste sa vyhli konfliktom (napr. `translations/`)
7. (Odporúčané) Pridajte sekciu o preklade do vášho README podľa [README languages template](./getting_started/README_languages_template.md)
8. Pozrite: [Nastavenie Azure AI](./getting_started/set-up-azure-ai.md)

## Použitie

Preložte všetky podporované typy:

```bash
translate -l "ko ja"
```

Len Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Len poznámkové bloky:

```bash
translate -l "zh" -nb
```

Viac príznakov: [Referenčný manuál príkazov](./getting_started/command-reference.md)

## Funkcie

- Automatizovaný preklad Markdown, poznámkových blokov a obrázkov
- Udržiava preklady synchronizované so zdrojovými zmenami
- Funguje lokálne (CLI) alebo v CI (GitHub Actions)
- Používa Azure OpenAI alebo OpenAI; voliteľne Azure AI Vision pre obrázky
- Zachováva formátovanie a štruktúru Markdown

## Dokumentácia

- [Príručka príkazového riadku](./getting_started/command-line-guide/command-line-guide.md)
- [Príručka GitHub Actions (verejné repozitáre a štandardné tajomstvá)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Príručka GitHub Actions (Microsoft organizácie a nastavenia na úrovni organizácie)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Šablóna jazykov README](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Kontribúcia](./CONTRIBUTING.md)
- [Riešenie problémov](./getting_started/troubleshooting.md)

### Microsoft špecifická príručka
> [!NOTE]
> Len pre správcov repozitárov Microsoft "For Beginners".

- [Aktualizácia zoznamu „ostatné kurzy“ (len pre MS Beginners repozitáre)](./getting_started/update-other-courses.md)

## Podporte nás a napomôžte globálnemu vzdelávaniu

Pridajte sa k nám v revolúcii spôsobu, akým sa vzdelávací obsah zdieľa globálne! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHub a podporte našu misiu rozbiť jazykové bariéry vo vzdelávaní a technológiách. Vaša angažovanosť a príspevky majú veľký význam! Kódové príspevky a návrhy funkcií sú vždy vítané.

### Preskúmajte vzdelávací obsah Microsoft vo vašom jazyku

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

## Video prezentácie

👉 Kliknite na obrázok nižšie a pozrite si na YouTube.

- **Open at Microsoft**: Krátka 18-minútová úvodná prezentácia a rýchly návod, ako používať Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Kontribúcia

Tento projekt vítá príspevky a návrhy. Zaujíma vás prispievanie do Azure Co-op Translator? Pozrite si prosím náš [CONTRIBUTING.md](./CONTRIBUTING.md), kde nájdete smernice, ako môžete pomôcť sprístupniť Co-op Translator širšej verejnosti.

## Prispievatelia
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kód správania

Tento projekt prijal [Microsoft Open Source Kód správania](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií pozri [Často kladené otázky kódu správania](https://opensource.microsoft.com/codeofconduct/faq/) alebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo pripomienkami.

## Zodpovedná AI

Microsoft sa zaväzuje pomáhať našim zákazníkom zodpovedne používať naše AI produkty, zdieľať naše poznatky a budovať dôveryhodné partnerstvá prostredníctvom nástrojov, ako sú Poznámky o transparentnosti a Hodnotenia dopadov. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI vychádza z našich princípov AI spravodlivosti, spoľahlivosti a bezpečnosti, ochrany súkromia a zabezpečenia, inkluzívnosti, transparentnosti a zodpovednosti.

Veľkorozsahové modely prírodného jazyka, obrazu a reči – ako tie použité v tomto príklade – sa potenciálne môžu správať nespravodlivo, nespoľahlivo alebo urážlivo, čo môže viesť k škodám. Informujte sa o rizikách a obmedzeniach v [Poznámke o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Odporúčaný prístup na zmiernenie týchto rizík je zahrnúť do vašej architektúry bezpečnostný systém, ktorý dokáže detegovať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú ochrannú vrstvu schopnú detegovať škodlivý obsah vytváraný používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety zahŕňa textové a obrazové API, ktoré umožňujú detekciu škodlivého materiálu. Tiež máme interaktívne Content Safety Studio, ktoré vám umožní zobraziť, preskúmať a otestovať ukážkové kódy na detekciu škodlivého obsahu v rôznych modalitách. Nasledujúca [rýchla dokumentácia](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie tým, ako komunikovať so službou.

Ďalším aspektom, ktorý treba vziať do úvahy, je celkový výkon aplikácie. Pri multi-modálnych a multi-modelových aplikáciách považujeme výkon za schopnosť systému pracovať tak, ako očakávate vy a vaši používatelia, vrátane toho, že nevytvára škodlivé výstupy. Je dôležité vyhodnotiť výkon vašej aplikácie pomocou [metrik kvality generovania a rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vašu AI aplikáciu môžete vyhodnocovať vo vašom vývojovom prostredí pomocou [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na základe testovacej dátovej sady alebo cieľa sú vaše generatívne AI výstupy kvantitatívne merané pomocou zabudovaných alebo vlastných hodnotiacich nástrojov podľa vášho výberu. Na začiatok s prompt flow sdk na vyhodnocovanie vášho systému môžete použiť [rýchleho sprievodcu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po vykonaní vyhodnotenia môžete [vizualizovať výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá projektov, produktov alebo služieb. Autorizované použitie ochranných známok alebo log Microsoftu podlieha a musí dodržiavať
[Pravidlá používania ochranných známok a značiek Microsoftu](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použitie ochranných známok alebo log Microsoftu v upravených verziách tohto projektu nesmie spôsobovať zmätok ani naznačovať sponzorstvo spoločnosťou Microsoft.
Akékoľvek použitie ochranných známok alebo log tretích strán podlieha zásadám týchto tretích strán.

## Získanie pomoci

Ak sa zaseknete alebo máte otázky ohľadom budovania AI aplikácií, pridajte sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu k produktu alebo chyby počas vývoja, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladačskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa usilujeme o presnosť, majte prosím na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z používania tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->