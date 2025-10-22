<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:14:16+00:00",
  "source_file": "README.md",
  "language_code": "sk"
}
-->
# Co-op Translator

_Jednoducho automatizujte preklad svojho vzdelávacieho obsahu na GitHube do viacerých jazykov a oslovte globálne publikum._

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

#### Podporované nástrojom [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](./README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Prehľad

**Co-op Translator** vám umožňuje rýchlo prekladať váš vzdelávací obsah na GitHube do viacerých jazykov, takže môžete jednoducho osloviť medzinárodné publikum. Keď aktualizujete svoje Markdown súbory, obrázky alebo Jupyter notebooky, preklady sa automaticky synchronizujú, aby bol váš vzdelávací obsah na GitHube vždy aktuálny a relevantný pre používateľov z celého sveta.

Pozrite sa, ako Co-op Translator organizuje preložený vzdelávací obsah na GitHube:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.sk.png)

## Rýchly štart

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

## Minimálne nastavenie

- Vytvorte súbor `.env` podľa šablóny: [.env.template](../../.env.template)
- Nastavte jedného poskytovateľa LLM (Azure OpenAI alebo OpenAI)
- Pre preklad obrázkov (`-img`) nastavte aj Azure AI Vision
- Odporúčanie: Ak už máte preklady vytvorené inými nástrojmi, najskôr ich odstráňte, aby ste predišli konfliktom (napríklad: `translations/`).
- Odporúčanie: Pridajte sekciu s prekladmi do svojho README pomocou [README languages template](./README_languages_template.md)
- Pozrite si: [Nastavenie Azure AI](./getting_started/set-up-azure-ai.md)

## Použitie

Preklad všetkých podporovaných typov:

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

Len notebooky:

```bash
translate -l "zh" -nb
```

Viac možností: [Referenčný zoznam príkazov](./getting_started/command-reference.md)

## Funkcie

- Automatizovaný preklad Markdownu, notebookov a obrázkov
- Udržiava preklady synchronizované so zmenami zdroja
- Funguje lokálne (CLI) aj v CI (GitHub Actions)
- Používa Azure OpenAI alebo OpenAI; voliteľne Azure AI Vision pre obrázky
- Zachováva formátovanie a štruktúru Markdownu

## Dokumentácia

- [Príručka príkazového riadku](./getting_started/command-line-guide/command-line-guide.md)
- [Príručka pre GitHub Actions (verejné repozitáre & štandardné tajomstvá)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Príručka pre GitHub Actions (repozitáre organizácie Microsoft & nastavenia na úrovni organizácie)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Podporované jazyky](./getting_started/supported-languages.md)
- [Riešenie problémov](./getting_started/troubleshooting.md)

## Podporte nás a rozvíjajte globálne vzdelávanie

Pridajte sa k nám a pomôžte zmeniť spôsob, akým sa vzdelávací obsah zdieľa po celom svete! Dajte [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ na GitHube a podporte našu snahu odstrániť jazykové bariéry vo vzdelávaní a technológiách. Váš záujem a príspevky majú veľký význam! Príspevky do kódu a návrhy nových funkcií sú vždy vítané.

### Objavte vzdelávací obsah od Microsoftu vo svojom jazyku

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

Zistite viac o Co-op Translator prostredníctvom našich prezentácií _(Kliknite na obrázok nižšie a pozrite si video na YouTube.)_:

- **Open at Microsoft**: Krátke 18-minútové predstavenie a rýchly návod, ako používať Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.sk.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Prispievanie

Tento projekt víta príspevky a návrhy. Chcete prispieť do Azure Co-op Translator? Pozrite si náš [CONTRIBUTING.md](./CONTRIBUTING.md) pre pokyny, ako môžete pomôcť sprístupniť Co-op Translator širšiemu publiku.

## Prispievatelia

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Kódex správania

Tento projekt prijal [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Viac informácií nájdete v [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) alebo
kontaktujte [opencode@microsoft.com](mailto:opencode@microsoft.com) s ďalšími otázkami alebo pripomienkami.

## Zodpovedná AI

Microsoft sa zaviazal pomáhať zákazníkom používať naše AI produkty zodpovedne, zdieľať naše poznatky a budovať dôveru prostredníctvom nástrojov ako Transparency Notes a Impact Assessments. Mnohé z týchto zdrojov nájdete na [https://aka.ms/RAI](https://aka.ms/RAI).
Prístup Microsoftu k zodpovednej AI je založený na našich princípoch AI: spravodlivosť, spoľahlivosť a bezpečnosť, ochrana súkromia a bezpečnosť, inkluzívnosť, transparentnosť a zodpovednosť.

Veľké jazykové, obrazové a hlasové modely – ako tie použité v tejto ukážke – sa môžu správať nespravodlivo, nespoľahlivo alebo urážlivo, čo môže viesť k škodám. Prečítajte si [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text), aby ste boli informovaní o rizikách a obmedzeniach.

Odporúčaný spôsob, ako tieto riziká zmierniť, je zahrnúť do vašej architektúry bezpečnostný systém, ktorý dokáže rozpoznať a zabrániť škodlivému správaniu. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) poskytuje nezávislú vrstvu ochrany, ktorá dokáže rozpoznať škodlivý obsah generovaný používateľmi aj AI v aplikáciách a službách. Azure AI Content Safety zahŕňa API pre text a obrázky, ktoré vám umožnia detekovať škodlivý materiál. Máme aj interaktívne Content Safety Studio, kde si môžete pozrieť, vyskúšať a otestovať ukážkový kód na detekciu škodlivého obsahu v rôznych modalitách. Nasledujúca [dokumentácia pre rýchly štart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vás prevedie odoslaním požiadaviek na službu.


Ďalším aspektom, ktorý treba zohľadniť, je celkový výkon aplikácie. Pri aplikáciách, ktoré využívajú viaceré modality a modely, považujeme výkon za schopnosť systému fungovať podľa očakávaní vás a vašich používateľov, vrátane toho, že nevytvára škodlivé výstupy. Je dôležité hodnotiť výkon celej aplikácie pomocou [metrik kvality generovania a rizika a bezpečnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikáciu môžete vyhodnotiť vo vývojovom prostredí pomocou [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na základe testovacej dátovej sady alebo cieľa sú generácie vašej generatívnej AI aplikácie kvantitatívne merané pomocou vstavaných alebo vlastných hodnotiacich nástrojov podľa vášho výberu. Ak chcete začať s prompt flow sdk na hodnotenie vášho systému, môžete postupovať podľa [rýchleho sprievodcu](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Po vykonaní hodnotiaceho behu môžete [vizualizovať výsledky v Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Ochranné známky

Tento projekt môže obsahovať ochranné známky alebo logá projektov, produktov alebo služieb. Povolené používanie ochranných známok alebo log spoločnosti Microsoft podlieha a musí sa riadiť
[Pokynmi pre používanie ochranných známok a značky Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Použitie ochranných známok alebo log spoločnosti Microsoft v upravených verziách tohto projektu nesmie spôsobovať zmätok ani naznačovať sponzorstvo zo strany Microsoftu.
Akékoľvek použitie ochranných známok alebo log tretích strán podlieha pravidlám týchto tretích strán.

## Získanie pomoci

Ak sa zaseknete alebo máte otázky ohľadom tvorby AI aplikácií, pridajte sa do:

<a href="https://aka.ms/foundry/discord"><img alt="Azure AI Foundry Discord" src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff"></a>

Ak máte spätnú väzbu k produktu alebo narazíte na chyby pri tvorbe, navštívte:

<a href="https://aka.ms/foundry/forum"><img alt="Azure AI Foundry Developer Forum" src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff"></a>

---

**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladovej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Za autoritatívny zdroj sa považuje pôvodný dokument v jeho pôvodnom jazyku. Pre kritické informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.