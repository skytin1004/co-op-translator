# Co-op Translator

_Eenvoudig vertalingen voor je educatieve GitHub-inhoud automatiseren en onderhouden in meerdere talen naarmate je project groeit._

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

### 🌐 Meertalige Ondersteuning

#### Ondersteund door [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisch](../ar/README.md) | [Bengaals](../bn/README.md) | [Bulgaars](../bg/README.md) | [Birmaans (Myanmar)](../my/README.md) | [Chinees (Vereenvoudigd)](../zh-CN/README.md) | [Chinees (Traditioneel, Hong Kong)](../zh-HK/README.md) | [Chinees (Traditioneel, Macau)](../zh-MO/README.md) | [Chinees (Traditioneel, Taiwan)](../zh-TW/README.md) | [Kroatisch](../hr/README.md) | [Tsjechisch](../cs/README.md) | [Deens](../da/README.md) | [Nederlands](./README.md) | [Estlands](../et/README.md) | [Fins](../fi/README.md) | [Frans](../fr/README.md) | [Duits](../de/README.md) | [Grieks](../el/README.md) | [Hebreeuws](../he/README.md) | [Hindi](../hi/README.md) | [Hongaars](../hu/README.md) | [Indonesisch](../id/README.md) | [Italiaans](../it/README.md) | [Japans](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreaans](../ko/README.md) | [Litouws](../lt/README.md) | [Maleis](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalees](../ne/README.md) | [Nigeriaans Pidgin](../pcm/README.md) | [Noors](../no/README.md) | [Perzisch (Farsi)](../fa/README.md) | [Pools](../pl/README.md) | [Portugees (Brazilië)](../pt-BR/README.md) | [Portugees (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Roemeens](../ro/README.md) | [Russisch](../ru/README.md) | [Servisch (Cyrillisch)](../sr/README.md) | [Slowaaks](../sk/README.md) | [Sloveens](../sl/README.md) | [Spaans](../es/README.md) | [Swahili](../sw/README.md) | [Zweeds](../sv/README.md) | [Tagalog (Filipijns)](../tl/README.md) | [Tamils](../ta/README.md) | [Telugu](../te/README.md) | [Thais](../th/README.md) | [Turks](../tr/README.md) | [Oekraïens](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamees](../vi/README.md)

> **Liever lokaal klonen?**
>
> Deze repository bevat meer dan 50 taalvertalingen, wat de downloadgrootte aanzienlijk verhoogt. Om zonder vertalingen te klonen, gebruik sparse checkout:
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
> Dit geeft je alles wat je nodig hebt om de cursus te voltooien met een veel snellere download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Overzicht

**Co-op Translator** helpt je om je educatieve GitHub-inhoud moeiteloos te lokaliseren in meerdere talen.  
Wanneer je je Markdown-bestanden, afbeeldingen of notebooks bijwerkt, blijven vertalingen automatisch gesynchroniseerd, waardoor je inhoud accuraat en up-to-date blijft voor leerlingen wereldwijd.

Voorbeeld van hoe vertaalde inhoud georganiseerd wordt:

![Example](../../imgs/translation-ex.png)

## Hoe de vertaalstatus wordt beheerd

Co-op Translator beheert vertaalde inhoud als **geversioneerde software-artifacten**,  
niet als statische bestanden.

De tool houdt de status bij van vertaalde Markdown, afbeeldingen en notebooks  
met behulp van **taalspecifieke metadata**.

Dit ontwerp stelt Co-op Translator in staat om:

- Betrouwbaar verouderde vertalingen te detecteren  
- Markdown, afbeeldingen en notebooks consequent te behandelen  
- Veilig te schalen in grote, snel bewegende, meertalige repositories  

Door vertalingen te modelleren als beheerde artifacten,  
passen vertaalworkflows naadloos binnen moderne  
softwareafhankelijkheids- en artifactbeheerpraktijken.

→ [Hoe de vertaalstatus wordt beheerd](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)

## Snelle start

```bash
# Maak en activeer een virtuele omgeving (aanbevolen)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installeer het pakket
pip install co-op-translator
# Vertalen
translate -l "ko ja fr" -md
```

Docker:

```bash
# Haal de openbare afbeelding van GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run met de huidige map gemonteerd en .env meegeleverd (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimale setup

1. Controleer dat je een ondersteunde Python-versie hebt (momenteel 3.10-3.12). In poetry (pyproject.toml) wordt dit automatisch geregeld.  
2. Maak een `.env`-bestand aan met de template: [.env.template](../../.env.template)  
3. Configureer één LLM-provider (Azure OpenAI of OpenAI)  
4. (Optioneel) Voor afbeeldingsvertaling (`-img`), configureer Azure AI Vision  
5. (Optioneel) Je kunt meerdere set inloggegevens configureren door variabelen te dupliceren met achtervoegsels zoals `_1`, `_2`, etc. Alle variabelen in een set moeten hetzelfde achtervoegsel delen.  
6. (Aanbevolen) Maak eventuele eerdere vertalingen schoon om conflicten te voorkomen (bijv. `translations/`)  
7. (Aanbevolen) Voeg een vertaalsectie toe aan je README met de [README taaltemplate](./getting_started/README_languages_template.md)  
8. Zie: [Azure AI instellen](./getting_started/set-up-azure-ai.md)

## Gebruik

Vertaal alle ondersteunde typen:

```bash
translate -l "ko ja"
```

Alleen Markdown:

```bash
translate -l "de" -md
```

Markdown + afbeeldingen:

```bash
translate -l "pt" -md -img
```

Alleen notebooks:

```bash
translate -l "zh" -nb
```

Meer opties: [Commandoreferentie](./getting_started/command-reference.md)

## Kenmerken

- Geautomatiseerde vertaling voor Markdown, notebooks en afbeeldingen  
- Houdt vertalingen synchroon met bronwijzigingen  
- Werkt lokaal (CLI) of in CI (GitHub Actions)  
- Gebruikt Azure OpenAI of OpenAI; optioneel Azure AI Vision voor afbeeldingen  
- Behoudt Markdown-opmaak en structuur

## Documentatie

- [Cli-gids](./getting_started/command-line-guide/command-line-guide.md)  
- [GitHub Actions gids (Openbare repos & standaardsecrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)  
- [GitHub Actions gids (Microsoft organisatie repos & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)  
- [README taaltemplate](./getting_started/README_languages_template.md)  
- [Ondersteunde talen](./getting_started/supported-languages.md)  
- [Bijdragen](./CONTRIBUTING.md)  
- [Probleemoplossing](./getting_started/troubleshooting.md)

### Microsoft-specifieke gids
> [!NOTE]
> Alleen voor beheerders van de Microsoft “For Beginners” repositories.

- [Bijwerken van de “andere cursussen” lijst (alleen voor MS Beginners repositories)](./getting_started/update-other-courses.md)

## Steun ons en bevorder wereldwijd leren

Doe met ons mee bij het transformeren van hoe educatieve content wereldwijd gedeeld wordt! Geef [Co-op Translator](https://github.com/azure/co-op-translator) een ⭐ op GitHub en steun onze missie om taalbarrières in leren en technologie af te breken. Jouw interesse en bijdragen maken een groot verschil! Codebijdragen en functiesuggesties zijn altijd welkom.

### Verken Microsoft educatieve inhoud in jouw taal

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

## Video presentaties

👉 Klik op de afbeelding hieronder om te kijken op YouTube.

- **Open at Microsoft**: Een korte introductie van 18 minuten en een snelle gids over het gebruik van Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bijdragen

Dit project verwelkomt bijdragen en suggesties. Geïnteresseerd in bijdragen aan Azure Co-op Translator? Bekijk onze [CONTRIBUTING.md](./CONTRIBUTING.md) voor richtlijnen over hoe je kunt helpen om Co-op Translator toegankelijker te maken.

## Bijdragers
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Gedragscode

Dit project heeft de [Microsoft Open Source Gedragscode](https://opensource.microsoft.com/codeofconduct/) overgenomen.
Voor meer informatie zie de [Gedragscode FAQ](https://opensource.microsoft.com/codeofconduct/faq/) of
neem contact op met [opencode@microsoft.com](mailto:opencode@microsoft.com) voor aanvullende vragen of opmerkingen.

## Verantwoord AI

Microsoft zet zich in om onze klanten te helpen onze AI-producten verantwoord te gebruiken, onze ervaringen te delen en vertrouwen op te bouwen via tools zoals Transparantienota's en Impactbeoordelingen. Veel van deze bronnen zijn te vinden op [https://aka.ms/RAI](https://aka.ms/RAI).
De benadering van Microsoft voor verantwoord AI is gebaseerd op onze AI-principes van rechtvaardigheid, betrouwbaarheid en veiligheid, privacy en beveiliging, inclusiviteit, transparantie en verantwoordelijkheid.

Grootschalige modellen voor natuurlijke taal, beeld en spraak - zoals die gebruikt worden in dit voorbeeld - kunnen zich mogelijk op manieren gedragen die onrechtvaardig, onbetrouwbaar of aanstootgevend zijn, wat schade kan veroorzaken. Raadpleeg de [Azure OpenAI service Transparantienota](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) om geïnformeerd te zijn over risico's en beperkingen.

De aanbevolen aanpak om deze risico's te beperken is het opnemen van een veiligheidssysteem in uw architectuur dat schadelijk gedrag kan detecteren en voorkomen. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) biedt een onafhankelijke beschermingslaag, die schadelijke door gebruikers of AI gegenereerde inhoud in toepassingen en diensten kan detecteren. Azure AI Content Safety bevat tekst- en beeld-API's waarmee u materiaal kunt detecteren dat schadelijk is. We hebben ook een interactieve Content Safety Studio waarmee u voorbeeldcode kunt bekijken, verkennen en uitproberen voor het detecteren van schadelijke inhoud over verschillende modaliteiten. De volgende [quickstart documentatie](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) begeleidt u bij het doen van verzoeken aan de service.

Een ander aspect om rekening mee te houden is de algehele prestatie van de applicatie. Bij multi-modale en multi-modelapplicaties verstaan we onder prestatie dat het systeem presteert zoals u en uw gebruikers verwachten, inclusief het niet genereren van schadelijke resultaten. Het is belangrijk om de prestatie van uw gehele applicatie te beoordelen met behulp van [generatiekwaliteit en risico- en veiligheidsmetrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

U kunt uw AI-applicatie evalueren in uw ontwikkelomgeving met behulp van de [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Aan de hand van een testdataset of een doel worden uw generatieve AI-generaties kwantitatief gemeten met ingebouwde of door uzelf gekozen evaluators. Om te beginnen met de prompt flow sdk om uw systeem te evalueren, kunt u de [quickstart gids](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) volgen. Nadat u een evaluatierun hebt uitgevoerd, kunt u de [resultaten visualiseren in Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Handelsmerken

Dit project kan handelsmerken of logo's bevatten van projecten, producten of diensten. Geautoriseerd gebruik van Microsoft  
handelsmerken of logo's is onderhevig aan en moet voldoen aan de  
[Microsoft's Richtlijnen voor Handelsmerken & Merken](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Gebruik van Microsoft handelsmerken of logo's in gewijzigde versies van dit project mag geen verwarring veroorzaken of Microsoft-sponsoring impliceren.  
Elk gebruik van handelsmerken of logo's van derden is onderhevig aan het beleid van die derden.

## Hulp krijgen

Als u vastloopt of vragen heeft over het bouwen van AI-apps, sluit u aan bij:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Als u productfeedback heeft of foutmeldingen ondervindt tijdens het bouwen, bezoek dan:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortkomen uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->