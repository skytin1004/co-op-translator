# Co-op Translator

_Effektiviser og vedlikehold enkelt oversettelser av ditt pedagogiske GitHub-innhold på flere språk etter hvert som prosjektet ditt utvikler seg._

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

### 🌐 Flerspråklig støtte

#### Støttet av [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabisk](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarsk](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Kinesisk (forenklet)](../zh-CN/README.md) | [Kinesisk (tradisjonell, Hong Kong)](../zh-HK/README.md) | [Kinesisk (tradisjonell, Macau)](../zh-MO/README.md) | [Kinesisk (tradisjonell, Taiwan)](../zh-TW/README.md) | [Kroatisk](../hr/README.md) | [Tsjekkisk](../cs/README.md) | [Dansk](../da/README.md) | [Nederlandsk](../nl/README.md) | [Estisk](../et/README.md) | [Finsk](../fi/README.md) | [Fransk](../fr/README.md) | [Tysk](../de/README.md) | [Gresk](../el/README.md) | [Hebraisk](../he/README.md) | [Hindi](../hi/README.md) | [Ungarsk](../hu/README.md) | [Indonesisk](../id/README.md) | [Italiensk](../it/README.md) | [Japansk](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Koreansk](../ko/README.md) | [Litauisk](../lt/README.md) | [Malaysisk](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepalesisk](../ne/README.md) | [Nigeriansk Pidgin](../pcm/README.md) | [Norsk](./README.md) | [Persisk (Farsi)](../fa/README.md) | [Polsk](../pl/README.md) | [Portugisisk (Brasil)](../pt-BR/README.md) | [Portugisisk (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Rumensk](../ro/README.md) | [Russisk](../ru/README.md) | [Serbisk (kyrillisk)](../sr/README.md) | [Slovakisk](../sk/README.md) | [Slovensk](../sl/README.md) | [Spansk](../es/README.md) | [Swahili](../sw/README.md) | [Svensk](../sv/README.md) | [Tagalog (Filippinsk)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Tyrkisk](../tr/README.md) | [Ukrainsk](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamesisk](../vi/README.md)

> **Foretrekker du å klone lokalt?**
>
> Dette repositoriet inkluderer over 50 språkoversettelser, noe som øker nedlastingsstørrelsen betydelig. For å klone uten oversettelser, bruk sparse checkout:
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
> Dette gir deg alt du trenger for å fullføre kurset med mye raskere nedlasting.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Oversikt

**Co-op Translator** hjelper deg med å lokaltilpasse ditt pedagogiske GitHub-innhold til flere språk uten problemer.  
Når du oppdaterer Markdown-filer, bilder eller notatbøker, holdes oversettelsene automatisk synkronisert, slik at innholdet ditt forblir korrekt og oppdatert for lærende over hele verden.

Eksempel på hvordan oversatt innhold er organisert:

![Example](../../translated_images/no/translation-ex.0c8aa6a7ee0aad2b.webp)

## Hvordan oversettelsestilstand styres

Co-op Translator håndterer oversatt innhold som **versjonerte programvareartefakter**,  
ikke som statiske filer.

Verktøyet sporer tilstanden til oversatt Markdown, bilder og notatbøker ved bruk av **språkspesifikk metadata**.

Denne designen gjør at Co-op Translator kan:

- Pålitelig oppdage utdaterte oversettelser  
- Behandle Markdown, bilder og notatbøker konsistent  
- Skalere sikkert over store, raskt bevegende, flerspråklige repositorier  

Ved å modellere oversettelser som administrerte artefakter,  
tilpasses oversettelsesarbeidsflyter naturlig med moderne programvareavhengighet- og artefakthåndteringspraksis.

→ [Hvordan oversettelsestilstand styres](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Rask start

```bash
# Opprett og aktiver et virtuelt miljø (anbefalt)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Installer pakken
pip install co-op-translator
# Oversett
translate -l "ko ja fr" -md
```

Docker:

```bash
# Hent det offentlige bildet fra GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Kjør med gjeldende mappe montert og .env levert (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal oppsett

1. Bekreft at du har en støttet Python-versjon (for tiden 3.10-3.12). I poetry (pyproject.toml) håndteres dette automatisk.
2. Lag en `.env`-fil ved bruk av malen: [.env.template](../../.env.template)
3. Konfigurer én LLM-leverandør (Azure OpenAI eller OpenAI)
4. (Valgfritt) For bildeoversettelse (`-img`), konfigurer Azure AI Vision
5. (Valgfritt) Du kan konfigurere flere legitimasjonssett ved å duplisere variabler med suffikser som `_1`, `_2` osv. Alle variabler i et sett må ha samme suffiks.
6. (Anbefalt) Rens tidligere oversettelser for å unngå konflikter (f.eks. `translations/`)
7. (Anbefalt) Legg til en oversettelsesseksjon i README ved bruk av [README-språkmalen](./getting_started/README_languages_template.md)
8. Se: [Sett opp Azure AI](./getting_started/set-up-azure-ai.md)

## Bruk

Oversett alle støttede typer:

```bash
translate -l "ko ja"
```

Kun Markdown:

```bash
translate -l "de" -md
```

Markdown + bilder:

```bash
translate -l "pt" -md -img
```

Kun notatbøker:

```bash
translate -l "zh" -nb
```

Flere flagg: [Kommando-referanse](./getting_started/command-reference.md)

## Funksjoner

- Automatisk oversettelse av Markdown, notatbøker og bilder  
- Holder oversettelser synkronisert med kildeforandringer  
- Fungerer lokalt (CLI) eller i CI (GitHub Actions)  
- Bruker Azure OpenAI eller OpenAI; valgfritt Azure AI Vision for bilder  
- Bevarer Markdown-formatering og struktur  

## Dokumentasjon

- [Kommando-linjeveiledning](./getting_started/command-line-guide/command-line-guide.md)
- [GitHub Actions-veiledning (offentlige repositorier & standard hemmeligheter)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [GitHub Actions-veiledning (Microsoft organisasjonsrepositorier & org-nivå oppsett)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README-språkmal](./getting_started/README_languages_template.md)
- [Støttede språk](./getting_started/supported-languages.md)
- [Bidra](./CONTRIBUTING.md)
- [Feilsøking](./getting_started/troubleshooting.md)

### Microsoft-spesifikk veiledning
> [!NOTE]
> For vedlikeholdere av Microsoft “For Beginners”-repositorier kun.

- [Oppdatere “andre kurs”-listen (kun for MS Beginners-repositorier)](./getting_started/update-other-courses.md)

## Støtt oss og frem global læring

Bli med oss i å revolusjonere hvordan pedagogisk innhold deles globalt! Gi [Co-op Translator](https://github.com/azure/co-op-translator) en ⭐ på GitHub og støtt vårt oppdrag om å bryte ned språkbarrierer innen læring og teknologi. Din interesse og bidrag har stor betydning! Kodebidrag og forslag til funksjoner er alltid velkomne.

### Utforsk Microsoft pedagogisk innhold på ditt språk

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

## Video-presentasjoner

👉 Klikk bildet nedenfor for å se på YouTube.

- **Open at Microsoft**: En kort 18-minutters introduksjon og rask guide for hvordan du bruker Co-op Translator.

  [![Open at Microsoft](../../translated_images/no/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Bidra

Dette prosjektet ønsker bidrag og forslag velkommen. Interessert i å bidra til Azure Co-op Translator? Se vår [CONTRIBUTING.md](./CONTRIBUTING.md) for retningslinjer om hvordan du kan hjelpe til med å gjøre Co-op Translator mer tilgjengelig.

## Bidragsytere
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Oppførselskode

Dette prosjektet har tatt i bruk [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For mer informasjon, se [Oppførselskode FAQ](https://opensource.microsoft.com/codeofconduct/faq/) eller
kontakt [opencode@microsoft.com](mailto:opencode@microsoft.com) hvis du har flere spørsmål eller kommentarer.

## Ansvarlig AI

Microsoft er forpliktet til å hjelpe våre kunder med å bruke AI-produktene våre på en ansvarlig måte, dele våre erfaringer og bygge tillitsbaserte partnerskap gjennom verktøy som Transparency Notes og Impact Assessments. Mange av disse ressursene finnes på [https://aka.ms/RAI](https://aka.ms/RAI).
Microsofts tilnærming til ansvarlig AI er basert på våre AI-prinsipper om rettferdighet, pålitelighet og sikkerhet, personvern og sikkerhet, inkludering, åpenhet og ansvarlighet.

Store naturlige språk-, bilde- og tale-modeller – som de som brukes i dette eksemplet – kan potensielt oppføre seg på måter som er urettferdige, upålitelige eller støtende, noe som igjen kan forårsake skade. Vennligst se [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) for å bli informert om risiko og begrensninger.

Den anbefalte tilnærmingen for å redusere disse risikoene er å inkludere et sikkerhetssystem i arkitekturen din som kan oppdage og forhindre skadelig atferd. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) tilbyr et uavhengig beskyttelseslag som kan oppdage skadelig bruker- og AI-generert innhold i apper og tjenester. Azure AI Content Safety inkluderer tekst- og bilde-API-er som lar deg oppdage skadelig materiale. Vi har også en interaktiv Content Safety Studio som lar deg se, utforske og prøve ut eksempel-kode for å oppdage skadelig innhold på tvers av ulike modaliteter. Følgende [kom i gang-dokumentasjon](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) veileder deg gjennom hvordan du sender forespørsler til tjenesten.

Et annet aspekt å ta i betraktning er den totale applikasjonsytelsen. Med multimodale- og multimodellapplikasjoner anser vi ytelse som at systemet fungerer som du og brukerne dine forventer, inkludert at det ikke genererer skadelige utdata. Det er viktig å vurdere ytelsen til hele applikasjonen ved å bruke [generasjonskvalitet og risiko- og sikkerhetsmålinger](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Du kan evaluere AI-applikasjonen din i utviklingsmiljøet ved å bruke [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Gjennom enten et testdatasett eller et mål, blir genereringene til generativ AI-applikasjonen kvantitativt målt med innebygde eller egendefinerte evalueringer etter eget valg. For å komme i gang med prompt flow SDK for å evaluere systemet ditt, kan du følge [kom i gang-guiden](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Når du har utført en evalueringskjøring, kan du [visualisere resultatene i Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Varemerker

Dette prosjektet kan inneholde varemerker eller logoer for prosjekter, produkter eller tjenester. Autorisert bruk av Microsofts 
varemerker eller logoer er underlagt og må følge
[Microsofts varemerke- og merkevare-retningslinjer](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Bruk av Microsofts varemerker eller logoer i modifiserte versjoner av dette prosjektet må ikke skape forvirring eller antyde at Microsoft sponser prosjektet.
All bruk av tredjeparts varemerker eller logoer er underlagt tredjepartens retningslinjer.

## Få hjelp

Hvis du står fast eller har spørsmål om å bygge AI-apper, bli med på:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Hvis du har produktinnspill eller opplever feil under bygging, besøk:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->