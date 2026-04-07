# Co-op Translator

_Easily automate and maintain translations for your educational GitHub content across multiple languages as your project evolves._

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

### 🌐 Podpora více jazyků

#### Podporováno [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](./README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raději klonovat lokálně?**
>
> Toto úložiště obsahuje více než 50 jazykových překladů, což výrazně zvětšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
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
> Tím získáte vše potřebné pro dokončení kurzu a stahování bude mnohem rychlejší.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Přehled

**Co-op Translator** vám pomáhá snadno lokalizovat váš vzdělávací obsah na GitHubu do více jazyků.  
Když aktualizujete své Markdown soubory, obrázky nebo poznámkové bloky, překlady se automaticky synchronizují, což zajišťuje, že váš obsah zůstane přesný a aktuální pro studenty po celém světě.

Příklad, jak je přeložený obsah organizován:

![Example](../../translated_images/cs/translation-ex.0c8aa6a7ee0aad2b.webp)

## Jak se spravuje stav překladu

Co-op Translator spravuje přeložený obsah jako **verzované softwarové artefakty**,  
nikoli jako statické soubory.

Nástroj sleduje stav přeložených Markdown, obrázků a poznámkových bloků
pomocí **metadata specifická pro jazyk**.

Tento design umožňuje Co-op Translator:

- Spolehlivě rozpoznávat zastaralé překlady
- Konzistentně zacházet s Markdown, obrázky a bloky
- Bezpečně škálovat napříč velkými, rychle se vyvíjejícími repozitáři s více jazyky

Modelováním překladů jako spravovaných artefaktů,
pracovní postupy překladu přirozeně odpovídají moderním
praxím správy závislostí a artefaktů ve vývoji softwaru.

→ [Jak se spravuje stav překladu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Rychlý start

```bash
# Vytvořte a aktivujte virtuální prostředí (doporučeno)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Nainstalujte balíček
pip install co-op-translator
# Přeložit
translate -l "ko ja fr" -md
```

Docker:

```bash
# Stáhnout veřejný obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spustit s namontovanou aktuální složkou a poskytnutým .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimální nastavení

1. Ujistěte se, že máte podporovanou verzi Pythonu (aktuálně 3.10-3.12). V poetry (pyproject.toml) je to automaticky ošetřeno.
2. Vytvořte soubor `.env` pomocí šablony: [.env.template](../../.env.template)
3. Nakonfigurujte jednoho poskytovatele LLM (Azure OpenAI nebo OpenAI)
4. (Nepovinné) Pro překlad obrázků (`-img`) nastavte Azure AI Vision
5. (Nepovinné) Můžete nakonfigurovat více sad přihlašovacích údajů duplikací proměnných s příponami jako `_1`, `_2` atd. Všechny proměnné v sadě musí mít stejnou příponu.
6. (Doporučeno) Vyčistěte předchozí překlady, aby nedocházelo ke konfliktům (např. `translations/`)
7. (Doporučeno) Přidejte sekci s překlady do svého README pomocí [README languages template](./getting_started/README_languages_template.md)
8. Viz: [Nastavení Azure AI](./getting_started/set-up-azure-ai.md)

## Použití

Přeložte všechny podporované typy:

```bash
translate -l "ko ja"
```

Pouze Markdown:

```bash
translate -l "de" -md
```

Markdown + obrázky:

```bash
translate -l "pt" -md -img
```

Pouze poznámkové bloky:

```bash
translate -l "zh" -nb
```

Další příznaky: [Reference příkazů](./getting_started/command-reference.md)

## Funkce

- Automatizovaný překlad Markdown, poznámkových bloků a obrázků
- Udržuje překlady v synchronizaci se zdrojovými změnami
- Funguje lokálně (CLI) nebo v CI (GitHub Actions)
- Používá Azure OpenAI nebo OpenAI; volitelně Azure AI Vision pro obrázky
- Zachovává formátování a strukturu Markdown

## Dokumentace

- [Průvodce příkazovou řádkou](./getting_started/command-line-guide/command-line-guide.md)
- [Průvodce GitHub Actions (veřejná repozitáře & standardní tajemství)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Průvodce GitHub Actions (repozitáře Microsoft organizace & nastavení na úrovni organizace)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Přispívání](./CONTRIBUTING.md)
- [Řešení problémů](./getting_started/troubleshooting.md)

### Microsoft-specifický průvodce
> [!NOTE]
> Pouze pro správce repozitářů Microsoft „Pro začátečníky“.

- [Aktualizace seznamu „ostatní kurzy“ (pouze pro repozitáře MS pro začátečníky)](./getting_started/update-other-courses.md)

## Podpořte nás a podpořte globální vzdělávání

Připojte se k nám a revolučně měňte způsob, jakým se vzdělávací obsah sdílí globálně! Oceněte [Co-op Translator](https://github.com/azure/co-op-translator) hvězdičkou na GitHubu a podpořte naši misi bourat jazykové bariéry ve vzdělávání a technologiích. Váš zájem a příspěvky mají velký dopad! Příspěvky s kódem a návrhy funkcí jsou vždy vítány.

### Prozkoumejte vzdělávací obsah Microsoftu ve vašem jazyce

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

## Video prezentace

👉 Klikněte na obrázek níže pro sledování na YouTube.

- **Open at Microsoft**: Krátké 18-minutové představení a rychlý průvodce, jak používat Co-op Translator.

  [![Open at Microsoft](../../translated_images/cs/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Přispívání

Tento projekt vítá příspěvky a návrhy. Máte zájem přispět do Azure Co-op Translator? Prosím, podívejte se na naše pokyny v [CONTRIBUTING.md](./CONTRIBUTING.md), jak můžete pomoci zpřístupnit Co-op Translator širšímu okruhu lidí.

## Přispěvatelé
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod chování

Tento projekt přijal [Kodex chování Microsoft Open Source](https://opensource.microsoft.com/codeofconduct/).
Více informací najdete v [Často kladených otázkách o kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s jakýmikoli dalšími dotazy nebo připomínkami.

## Odpovědná AI

Microsoft se zavazuje pomáhat našim zákazníkům používat naše AI produkty odpovědně, sdílet naše poznatky a budovat důvěryhodná partnerství prostřednictvím nástrojů jako jsou Poznámky o transparentnosti a Hodnocení dopadů. Mnoho těchto zdrojů naleznete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich principech AI: spravedlnost, spolehlivost a bezpečnost, soukromí a zabezpečení, inkluzivita, transparentnost a odpovědnost.

Velké modely pro přirozený jazyk, obrázky a řeč – jako ty, které jsou použity v tomto příkladu – se mohou potenciálně chovat způsobem, který je nespravedlivý, nespolehlivý nebo urážlivý, což může vést k újmu. Pro informace o rizicích a omezeních si prosím přečtěte [Poznámku o transparentnosti služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text).

Doporučený přístup k minimalizaci těchto rizik je zahrnout do vaší architektury bezpečnostní systém, který dokáže detekovat a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou ochrannou vrstvu, schopnou detekovat škodlivý obsah vytvořený uživateli i umělou inteligencí v aplikacích a službách. Azure AI Content Safety zahrnuje API pro text a obrázky, které umožňují detekovat škodlivý materiál. Také máme interaktivní Content Safety Studio, které umožňuje zobrazovat, prozkoumávat a vyzkoušet ukázkové kódy pro detekci škodlivého obsahu napříč různými modality. Následující [dokumentace quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede tvorbou požadavků na službu.

Dalším aspektem, který je třeba vzít v úvahu, je celkový výkon aplikace. U multimodálních a multimodelových aplikací rozumíme výkonu jako tomu, že systém pracuje způsobem, jaký vy a vaši uživatelé očekáváte, včetně toho, že nevytváří škodlivý výstup. Je důležité vyhodnotit výkon vaší aplikace pomocí [metrik kvality generování a rizik a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Vaši AI aplikaci můžete vyhodnotit ve vývojovém prostředí pomocí [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Ať už máte testovací datovou sadu nebo cíl, generování vaší generativní AI aplikace je kvantitativně měřeno pomocí vestavěných hodnotitelů nebo vlastních hodnotitelů podle vašeho výběru. Pro začátek s prompt flow SDK pro hodnocení vašeho systému můžete sledovat [průvodce rychlým startem](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po provedení vyhodnocovacího běhu můžete [vizualizovat výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované použití ochranných známek nebo log Microsoftu musí podléhat a dodržovat [Pravidla pro ochranné známky a značky Microsoftu](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v upravených verzích tohoto projektu nesmí způsobit záměnu nebo naznačovat sponzorství Microsoftem.
Jakékoli použití ochranných známek nebo log třetích stran podléhá zásadám těchto třetích stran.

## Kde získat pomoc

Pokud narazíte na problém nebo budete mít jakékoli otázky ohledně tvorby AI aplikací, připojte se na:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo zaznamenáte chyby během vývoje, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoli nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->