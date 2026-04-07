# Co-op Translator

_Ľahko automatizujte a udržiavajte preklady vášho vzdelávacieho obsahu na GitHube v rôznych jazykoch, ako sa váš projekt vyvíja._

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
[Arabčina](../ar/README.md) | [Bengálčina](../bn/README.md) | [Bulharčina](../bg/README.md) | [Barmský (Myanmar)](../my/README.md) | [Čínština (zjednodušená)](../zh-CN/README.md) | [Čínština (tradičná, Hongkong)](../zh-HK/README.md) | [Čínština (tradičná, Macau)](../zh-MO/README.md) | [Čínština (tradičná, Taiwan)](../zh-TW/README.md) | [Chorvátčina](../hr/README.md) | [Čeština](../cs/README.md) | [Dánčina](../da/README.md) | [Holandčina](../nl/README.md) | [Estónčina](../et/README.md) | [Fínčina](../fi/README.md) | [Francúzština](../fr/README.md) | [Nemčina](../de/README.md) | [Gréčtina](../el/README.md) | [Hebrejčina](../he/README.md) | [Hinčina](../hi/README.md) | [Maďarčina](../hu/README.md) | [Indonézčina](../id/README.md) | [Taliančina](../it/README.md) | [Japončina](../ja/README.md) | [Kannadčina](../kn/README.md) | [Khmerčina](../km/README.md) | [Kórejčina](../ko/README.md) | [Litovčina](../lt/README.md) | [Malajčina](../ms/README.md) | [Malaijálamčina](../ml/README.md) | [Maráthčina](../mr/README.md) | [Nepálčina](../ne/README.md) | [Nigérijský pidžin](../pcm/README.md) | [Nórčina](../no/README.md) | [Perzština (Fársí)](../fa/README.md) | [Poľština](../pl/README.md) | [Portugalčina (Brazília)](../pt-BR/README.md) | [Portugalčina (Portugalsko)](../pt-PT/README.md) | [Pandžábčina (Gurmukhi)](../pa/README.md) | [Rumunčina](../ro/README.md) | [Ruština](../ru/README.md) | [Srbčina (cyrilika)](../sr/README.md) | [Slovenčina](./README.md) | [Slovinčina](../sl/README.md) | [Španielčina](../es/README.md) | [Svahilčina](../sw/README.md) | [Švédčina](../sv/README.md) | [Tagalog (Filipínčina)](../tl/README.md) | [Tamilčina](../ta/README.md) | [Telugčina](../te/README.md) | [Thajčina](../th/README.md) | [Turečtina](../tr/README.md) | [Ukrajinčina](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamčina](../vi/README.md)

> **Radšej klonovať lokálne?**
>
> Tento repozitár obsahuje preklady do viac ako 50 jazykov, čo výrazne zväčšuje veľkosť na stiahnutie. Ak chcete klonovať bez prekladov, použite sparse checkout:
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
> Takto získate všetko potrebné na absolvovanie kurzu oveľa rýchlejšie.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám pomáha lokalizovať váš vzdelávací obsah na GitHube do viacerých jazykov bez námahy.  
Keď aktualizujete svoje Markdown súbory, obrázky alebo zápisníky, preklady zostávajú automaticky synchronizované, čím sa zabezpečuje, že váš obsah ostáva presný a aktuálny pre študentov po celom svete.

Príklad, ako je preložený obsah organizovaný:

![Example](../../translated_images/sk/translation-ex.0c8aa6a7ee0aad2b.webp)

## Ako sa spravuje stav prekladu

Co-op Translator spravuje preložený obsah ako **verziované softvérové artefakty**,  
nie ako statické súbory.

Nástroj sleduje stav prekladaného Markdownu, obrázkov a zápisníkov  
pomocou **metadata viazaných na jazyk**.

Táto koncepcia umožňuje Co-op Translator:

- Spoľahlivo zistiť zastarané preklady
- Zaobchádzať s Markdownom, obrázkami a zápisníkmi konzistentne
- Bezpečne škálovať naprieč veľkými, rýchlo sa meniacimi multi-jazykovými repozitármi

Modelovaním prekladov ako spravovaných artefaktov,  
pracovné postupy prekladu sa prirodzene zhodujú s modernými  
praktikami správy závislostí a artefaktov v softvéri.

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
# Stiahnite verejný obrázok z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spustite s pripojenou aktuálnou zložkou a poskytnutým súborom .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimálne nastavenie

1. Overte, že máte podporovanú verziu Pythonu (momentálne 3.10-3.12). V poetry (pyproject.toml) sa to rieši automaticky.
2. Vytvorte `.env` súbor podľa šablóny: [.env.template](../../.env.template)
3. Nakonfigurujte jedného poskytovateľa LLM (Azure OpenAI alebo OpenAI)
4. (Voliteľné) Pre preklad obrázkov (`-img`) nakonfigurujte Azure AI Vision
5. (Voliteľné) Môžete nakonfigurovať viacero sád prihlasovacích údajov duplikáciou premenných so sufiksmi ako `_1`, `_2`, atď. Všetky premenné v sade musia mať rovnaký sufiks.
6. (Odporúčané) Vyčistite všetky predchádzajúce preklady, aby ste predišli konfliktom (napr. `translations/`)
7. (Odporúčané) Pridajte sekciu prekladov do vášho README pomocou [README languages template](./getting_started/README_languages_template.md)
8. Viac info: [Nastavenie Azure AI](./getting_started/set-up-azure-ai.md)

## Použitie

Preložte všetky podporované typy:

```bash
translate -l "ko ja"
```

Iba Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Iba zápisníky:

```bash
translate -l "zh" -nb
```

Viac príznakov: [Command reference](./getting_started/command-reference.md)

## Funkcie

- Automatizovaný preklad Markdownu, zápisníkov a obrázkov
- Udržiava preklady synchronizované so zmenami zdrojov
- Funguje lokálne (CLI) alebo v CI (GitHub Actions)
- Používa Azure OpenAI alebo OpenAI; nepovinne Azure AI Vision pre obrázky
- Zachováva formát a štruktúru Markdownu

## Dokumentácia

- [Príručka príkazového riadku](./getting_started/command-line-guide/command-line-guide.md)
- [Príručka GitHub Actions (verejné repozitáre & štandardné tajomstvá)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Príručka GitHub Actions (Microsoft organizácie & nastavenia na úrovni organizácie)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Prispievanie](./CONTRIBUTING.md)
- [Riešenie problémov](./getting_started/troubleshooting.md)

### Špecifická príručka pre Microsoft
> [!NOTE]
> Len pre správcov Microsoft repozitárov „For Beginners“.

- [Aktualizácia zoznamu „iných kurzov“ (len pre MS Beginners repozitáre)](./getting_started/update-other-courses.md)

## Podporte nás a podporujte globálne učenie

Pridajte sa k nám v revolúcii zdieľania vzdelávacieho obsahu po celom svete! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHube a podporujte našu misiu prekonávať jazykové bariéry vo vzdelávaní a technológiách. Váš záujem a príspevky majú veľký význam! Príspevky v kóde a nápady na funkcie sú vždy vítané.

### Preskúmajte vzdelávací obsah Microsoftu vo vašom jazyku

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

👉 Kliknite na obrázok nižšie pre sledovanie na YouTube.

- **Open at Microsoft**: Krátke 18-minútové predstavenie a rýchly návod, ako používať Co-op Translator.

  [![Open at Microsoft](../../translated_images/sk/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispievanie

Tento projekt prijíma príspevky a návrhy. Máte záujem prispieť do Azure Co-op Translator? Pozrite si prosím náš [CONTRIBUTING.md](./CONTRIBUTING.md) pre pokyny, ako môžete pomôcť sprístupniť Co-op Translator širšiemu publiku.

## Prispievatelia
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pre viac informácií pozrite si [Často kladené otázky o Kódexe správania](https://opensource.microsoft.com/codeofconduct/faq/) alebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s akýmikoľvek ďalšími otázkami alebo pripomienkami.

## Zodpovedná AI

Microsoft sa zaväzuje pomáhať našim zákazníkom zodpovedne využívať naše AI produkty, zdieľať naše poznatky a budovať vzťahy založené na dôvere prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI je založený na našich princípoch AI: spravodlivosť, spoľahlivosť a bezpečnosť, ochrana súkromia a bezpečnosť, inkluzívnosť, transparentnosť a zodpovednosť.

Veľkorozmerné modely prirodzeného jazyka, obrazu a reči – ako tie používané v tomto príklade – sa môžu potenciálne chovať nespravodlivo, nespoľahlivo alebo urážlivo, čím môžu spôsobiť škody. Prosím, pozrite si [Poznámku o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby ste boli informovaní o rizikách a obmedzeniach.

Odporúčaný prístup na zmiernenie týchto rizík je zahrnúť bezpečnostný systém do vašej architektúry, ktorý dokáže detekovať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú ochrannú vrstvu, ktorá dokáže detegovať škodlivý obsah vytvorený používateľmi a AI v aplikáciách a službách. Azure AI Content Safety obsahuje API pre text a obrázky, ktoré umožňujú detekovať škodlivý materiál. Máme tiež interaktívne Content Safety Studio, ktoré vám umožňuje prezerať, skúmať a vyskúšať ukážkový kód na detekciu škodlivého obsahu cez rôzne modality. Nasledujúca [rýchla príručka](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie vytváraním požiadaviek na službu.

Ďalším aspektom, ktorý treba zvážiť, je celkový výkon aplikácie. Pri multimodálnych a multimodelových aplikáciách považujeme výkon za to, že systém funguje tak, ako vy a vaši používatelia očakávate, vrátane neprodukovania škodlivých výstupov. Je dôležité hodnotiť výkon vašej celkovej aplikácie pomocou [metrík kvality generovania a rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikáciu môžete vyhodnotiť vo vašom vývojovom prostredí pomocou [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Pri použití testovacej dátovej sady alebo cieľa sú generácie vašej generatívnej AI aplikácie kvantitatívne merané pomocou zabudovaných evaluátorov alebo vlastných evaluátorov podľa vášho výberu. Ak chcete začať s prompt flow sdk na vyhodnotenie vášho systému, môžete sledovať [rýchlu príručku](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po vykonaní hodnotiaceho behu môžete [vizualizovať výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá pre projekty, produkty alebo služby. Autorizované používanie ochranných známok alebo log Microsoftu je predmetom a musí dodržiavať
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Používanie ochranných známok alebo log Microsoftu v upravených verziách tohto projektu nesmie spôsobovať zmätok alebo naznačovať sponzorstvo Microsoftom.
Akékoľvek používanie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Ako získať pomoc

Ak máte problém alebo otázky o tvorbe AI aplikácií, pripojte sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu k produktu alebo nahlásenie chýb počas vývoja, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrieknutie sa zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->