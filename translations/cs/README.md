# Co-op Translator

_Elegantně automatizujte a udržujte překlady pro váš vzdělávací obsah na GitHubu ve více jazycích, jak se váš projekt vyvíjí._

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
> Toto repozitář obsahuje více než 50 jazykových překladů, což značně zvyšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
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
> Díky tomu získáte vše potřebné ke splnění kurzu s mnohem rychlejším stažením.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Přehled

**Co-op Translator** vám pomůže snadno lokalizovat váš vzdělávací obsah na GitHubu do více jazyků.  
Když aktualizujete své soubory Markdown, obrázky nebo notebooky, překlady se automaticky synchronizují a zajišťují, že váš obsah zůstává přesný a aktuální pro studenty po celém světě.

Příklad, jak je přeložený obsah organizován:

![Example](../../imgs/translation-ex.png)

## Jak je spravován stav překladu

Co-op Translator spravuje přeložený obsah jako **verzované softwarové artefakty**,  
nikoliv jako statické soubory.

Nástroj sleduje stav přeložených Markdownů, obrázků a notebooků  
pomocí **metadata specifických pro jazyk**.

Tento přístup umožňuje Co-op Translator:

- Spolehlivě detekovat zastaralé překlady
- Konzistentně zacházet s Markdowny, obrázky a notebooky
- Bezpečně škálovat v rozsáhlých, rychle se vyvíjejících, vícejazyčných repozitářích

Modelováním překladů jako spravovaných artefaktů  
jsou pracovní postupy překladu přirozeně sladěny s moderními  
postupy správy softwarových závislostí a artefaktů.

→ [Jak je spravován stav překladu](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


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
# Stáhněte veřejný obraz z GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Spusťte s namontovanou aktuální složkou a poskytnutým .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimální nastavení

1. Ujistěte se, že máte podporovanou verzi Pythonu (aktuálně 3.10–3.12). V poetry (pyproject.toml) je to řešeno automaticky.
2. Vytvořte soubor `.env` pomocí šablony: [.env.template](../../.env.template)
3. Nakonfigurujte jednoho poskytovatele LLM (Azure OpenAI nebo OpenAI)
4. (Volitelné) Pro překlad obrázků (`-img`) nastavte Azure AI Vision
5. (Volitelné) Můžete konfigurovat více sad přihlašovacích údajů duplikací proměnných s příponou jako `_1`, `_2` apod. Všechny proměnné v sadě musí mít stejnou příponu.
6. (Doporučeno) Vyčistěte případné předchozí překlady, aby nedocházelo ke konfliktům (např. `translations/`)
7. (Doporučeno) Přidejte překladovou sekci do vašeho README pomocí [README languages template](./getting_started/README_languages_template.md)
8. Viz: [Set up Azure AI](./getting_started/set-up-azure-ai.md)

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

Pouze notebooky:

```bash
translate -l "zh" -nb
```

Další přepínače: [Příkazový manuál](./getting_started/command-reference.md)

## Funkce

- Automatizovaný překlad Markdownu, notebooků a obrázků
- Udržuje překlady v synchronizaci s původními změnami
- Funguje lokálně (CLI) i v CI (GitHub Actions)
- Používá Azure OpenAI nebo OpenAI; volitelně Azure AI Vision pro obrázky
- Zachovává formátování a strukturu Markdownu

## Dokumentace

- [Příručka příkazové řádky](./getting_started/command-line-guide/command-line-guide.md)
- [Příručka GitHub Actions (veřejné repozitáře & standardní tajné klíče)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Příručka GitHub Actions (repozitáře Microsoft organizace & nastavení na úrovni organizace)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Šablona jazyků README](./getting_started/README_languages_template.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Přispívání](./CONTRIBUTING.md)
- [Řešení problémů](./getting_started/troubleshooting.md)

### Průvodce specifický pro Microsoft
> [!NOTE]
> Pouze pro správce repozitářů Microsoft „Pro začátečníky“.

- [Aktualizace seznamu „dalších kurzů“ (pouze pro MS Beginners repozitáře)](./getting_started/update-other-courses.md)

## Podpořte nás a napomozte celosvětovému vzdělávání

Přidejte se k nám v revoluci sdílení vzdělávacího obsahu po celém světě! Dejte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHubu a podpořte náš cíl překonat jazykové bariéry ve vzdělávání a technologiích. Váš zájem a příspěvky mají významný dopad! Vítáme kódové příspěvky a návrhy funkcí.

### Objevte vzdělávací obsah Microsoft ve vašem jazyce

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

👉 Klikněte na obrázek níže pro zhlédnutí na YouTube.

- **Open at Microsoft**: Stručný 18minutový úvod a rychlý průvodce používáním Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Přispívání

Tento projekt vítá příspěvky a návrhy. Máte zájem přispět do Azure Co-op Translator? Prosím prostudujte si naše [CONTRIBUTING.md](./CONTRIBUTING.md) s pokyny, jak můžete pomoci zpřístupnit Co-op Translator širšímu publiku.

## Přispěvatelé
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kod chování

Tento projekt přijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Pro více informací viz [Často kladené dotazy k Kodexu chování](https://opensource.microsoft.com/codeofconduct/faq/) nebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s dalšími otázkami či komentáři.

## Odpovědná umělá inteligence

Microsoft se zavazuje pomáhat našim zákazníkům používat naše AI produkty odpovědně, sdílet naše poznatky a budovat důvěryhodná partnerství prostřednictvím nástrojů jako Transparency Notes a Impact Assessments. Mnoho těchto zdrojů naleznete na [https://aka.ms/RAI](https://aka.ms/RAI).
Přístup Microsoftu k odpovědné AI je založen na našich principech AI – spravedlnosti, spolehlivosti a bezpečnosti, soukromí a zabezpečení, inkluzivnosti, transparentnosti a odpovědnosti.

Velké modely pro přirozený jazyk, obraz a řeč – jako ty použité v tomto příkladu – se mohou potenciálně chovat nespravedlivě, nespolehlivě nebo urážlivě, což může způsobit škody. Prosím, přečtěte si [Transparency note služby Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), abyste byli informováni o rizicích a omezeních.

Doporučeným přístupem ke zmírnění těchto rizik je začlenit do vaší architektury bezpečnostní systém, který dokáže odhalit a zabránit škodlivému chování. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislou vrstvu ochrany schopnou detekovat škodlivý uživatelský i AI generovaný obsah v aplikacích a službách. Azure AI Content Safety zahrnuje textové a obrazové API, které umožňují detekovat škodlivý materiál. Máme také interaktivní Content Safety Studio, které vám umožní zobrazit, prozkoumat a vyzkoušet ukázky kódu pro detekci škodlivého obsahu napříč různými modalitami. Následující [rýchlý start dokumentace](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás provede procesu odesílání požadavků na službu.

Dalším aspektem k zvážení je celkový výkon aplikace. U multimodálních a multi-modelových aplikací považujeme výkon za to, že systém funguje tak, jak vy a vaši uživatelé očekáváte, včetně neprodukování škodlivých výstupů. Je důležité hodnotit výkon vaší celkové aplikace pomocí [metrik kvality generování a rizikového a bezpečnostního hodnocení](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoji AI aplikaci můžete hodnotit ve vašem vývojovém prostředí pomocí [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). S použitím testovací datové sady nebo cíle se generování vaší generativní AI aplikace kvantitativně měří pomocí vestavěných hodnotitelů nebo vlastních hodnotitelů dle vašeho výběru. Pro začátek s prompt flow sdk pro hodnocení vašeho systému můžete sledovat [rádce rychlým startem](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Jakmile provedete běh hodnocení, můžete [vizualizovat výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt může obsahovat ochranné známky nebo loga projektů, produktů či služeb. Autorizované použití ochranných známek nebo log Microsoftu podléhá a musí dodržovat
[Pravidla pro ochranné známky a značky Microsoftu](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použití ochranných známek nebo log Microsoftu v modifikovaných verzích tohoto projektu nesmí vést k záměně nebo naznačovat sponzorství Microsoftem.
Použití ochranných známek nebo log třetích stran podléhá pravidlům daných třetích stran.

## Získání pomoci

Pokud narazíte na problémy nebo máte otázky ohledně tvorby AI aplikací, připojte se:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo chyby během vývoje, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neneseme odpovědnost za jakékoliv nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->