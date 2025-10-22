<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T14:10:54+00:00",
  "source_file": "README.md",
  "language_code": "hr"
}
-->
# Co-op Translator

_Automatski prevedite svoj edukativni GitHub sadržaj na više jezika i dosegnite globalnu publiku._

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

### 🌐 Podrška za više jezika

#### Podržava [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pregled

**Co-op Translator** omogućuje brzo prevođenje vašeg edukativnog GitHub sadržaja na više jezika, tako da bez napora doprete do globalne publike. Kad ažurirate svoje Markdown datoteke, slike ili Jupyter bilježnice, prijevodi se automatski usklađuju kako bi vaš edukativni GitHub sadržaj uvijek bio svjež i relevantan za korisnike iz cijelog svijeta.

Pogledajte kako Co-op Translator organizira prevedeni edukativni GitHub sadržaj:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.hr.png)

## Brzi početak

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

## Minimalna konfiguracija

- Napravite `.env` koristeći predložak: [.env.template](../../.env.template)
- Konfigurirajte jednog LLM pružatelja (Azure OpenAI ili OpenAI)
- Za prijevod slika (`-img`), postavite i Azure AI Vision
- Preporuka: Ako imate prijevode generirane drugim alatima, prvo ih uklonite da izbjegnete konflikte (npr. `translations/`).
- Preporuka: Dodajte sekciju s prijevodima u svoj README koristeći [README predložak jezika](./README_languages_template.md)
- Pogledajte: [Postavljanje Azure AI](./getting_started/set-up-azure-ai.md)

## Korištenje

Prevedi sve podržane tipove:

```bash
translate -l "ko ja"
```

Samo Markdown:

```bash
translate -l "de" -md
```

Markdown + slike:

```bash
translate -l "pt" -md -img
```

Samo bilježnice:

```bash
translate -l "zh" -nb
```

Više opcija: [Referenca naredbi](./getting_started/command-reference.md)

## Značajke

- Automatski prijevod za Markdown, bilježnice i slike
- Održava prijevode usklađenima s izvornim promjenama
- Radi lokalno (CLI) ili u CI (GitHub Actions)
- Koristi Azure OpenAI ili OpenAI; opcionalno Azure AI Vision za slike
- Zadržava Markdown formatiranje i strukturu

## Dokumentacija

- [Vodič za naredbeni redak](./getting_started/command-line-guide/command-line-guide.md)
- [Vodič za GitHub Actions (Javni repozitoriji & standardne tajne)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Vodič za GitHub Actions (Microsoft organizacijski repozitoriji & postavke na razini organizacije)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Podržani jezici](./getting_started/supported-languages.md)
- [Rješavanje problema](./getting_started/troubleshooting.md)

## Podržite nas i potaknite globalno učenje

Pridružite nam se u revoluciji dijeljenja edukativnog sadržaja širom svijeta! Dajte [Co-op Translatoru](https://github.com/azure/co-op-translator) ⭐ na GitHubu i podržite našu misiju uklanjanja jezičnih barijera u učenju i tehnologiji. Vaš interes i doprinosi čine veliku razliku! Kodni doprinosi i prijedlozi za nove značajke su uvijek dobrodošli.

### Istražite Microsoft edukativni sadržaj na svom jeziku

- [AZD za početnike](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI za početnike](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) za početnike](https://github.com/microsoft/mcp-for-beginners)
- [AI agenti za početnike](https://github.com/microsoft/ai-agents-for-beginners)
- [Generativna AI za početnike uz .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generativna AI za početnike](https://github.com/microsoft/generative-ai-for-beginners)
- [Generativna AI za početnike uz Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML za početnike](https://aka.ms/ml-beginners)
- [Data Science za početnike](https://aka.ms/datascience-beginners)
- [AI za početnike](https://aka.ms/ai-beginners)
- [Kibernetička sigurnost za početnike](https://github.com/microsoft/Security-101)
- [Web razvoj za početnike](https://aka.ms/webdev-beginners)
- [IoT za početnike](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video prezentacije

Saznajte više o Co-op Translatoru kroz naše prezentacije _(Kliknite na sliku ispod za gledanje na YouTubeu.)_:

- **Open at Microsoft**: Kratki 18-minutni uvod i brzi vodič za korištenje Co-op Translatora.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.hr.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Doprinos

Ovaj projekt pozdravlja doprinose i prijedloge. Želite doprinijeti Azure Co-op Translatoru? Pogledajte naš [CONTRIBUTING.md](./CONTRIBUTING.md) za smjernice kako možete pomoći da Co-op Translator bude još pristupačniji.

## Suradnici

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Pravila ponašanja

Ovaj projekt koristi [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Za više informacija pogledajte [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) ili
kontaktirajte [opencode@microsoft.com](mailto:opencode@microsoft.com) za dodatna pitanja ili komentare.

## Odgovorna AI

Microsoft je posvećen tome da korisnici odgovorno koriste naše AI proizvode, dijelimo svoja iskustva i gradimo partnerske odnose temeljene na povjerenju kroz alate poput Transparency Notes i Impact Assessments. Mnoge od tih resursa možete pronaći na [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoftov pristup odgovornoj AI temelji se na našim AI principima: pravednost, pouzdanost i sigurnost, privatnost i sigurnost, inkluzivnost, transparentnost i odgovornost.

Veliki jezični, slikovni i govorni modeli - poput onih korištenih u ovom primjeru - mogu se ponašati nepravedno, nepouzdano ili uvredljivo, što može uzrokovati štetu. Molimo pročitajte [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) kako biste bili informirani o rizicima i ograničenjima.

Preporučeni način za smanjenje tih rizika je uključivanje sigurnosnog sustava u vašu arhitekturu koji može otkriti i spriječiti štetno ponašanje. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) pruža neovisni sloj zaštite, sposoban za otkrivanje štetnog sadržaja generiranog od strane korisnika i AI-a u aplikacijama i servisima. Azure AI Content Safety uključuje API-je za tekst i slike koji omogućuju otkrivanje štetnog materijala. Također imamo interaktivni Content Safety Studio koji vam omogućuje pregled, istraživanje i isprobavanje uzoraka koda za otkrivanje štetnog sadržaja kroz različite modalitete. Sljedeća [dokumentacija za brzi početak](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) vodi vas kroz slanje zahtjeva servisu.


Još jedan aspekt koji treba uzeti u obzir je ukupna izvedba aplikacije. Kod aplikacija koje koriste više modaliteta i modela, izvedba znači da sustav radi onako kako vi i vaši korisnici očekujete, uključujući i to da ne generira štetne rezultate. Važno je procijeniti izvedbu vaše aplikacije koristeći [metrike kvalitete generiranja te rizika i sigurnosti](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Svoju AI aplikaciju možete procijeniti u razvojnom okruženju koristeći [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Na temelju testnog skupa podataka ili cilja, generacije vaše generativne AI aplikacije kvantitativno se mjere pomoću ugrađenih ili prilagođenih evaluatorima po vašem izboru. Za početak s prompt flow SDK-om i procjenu vašeg sustava, možete slijediti [vodič za brzi početak](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Nakon što pokrenete evaluaciju, rezultate možete [vizualizirati u Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Zaštitni znakovi

Ovaj projekt može sadržavati zaštitne znakove ili logotipe projekata, proizvoda ili usluga. Ovlaštena upotreba Microsoftovih
zaštitnih znakova ili logotipa podliježe i mora biti u skladu s
[Microsoftovim smjernicama za zaštitne znakove i brend](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Upotreba Microsoftovih zaštitnih znakova ili logotipa u izmijenjenim verzijama ovog projekta ne smije izazvati zabunu niti sugerirati da Microsoft sponzorira projekt.
Svaka upotreba zaštitnih znakova ili logotipa trećih strana podliježe pravilima tih trećih strana.

## Dobivanje pomoći

Ako zapnete ili imate pitanja o izradi AI aplikacija, pridružite se:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

Ako imate povratne informacije o proizvodu ili naiđete na greške tijekom izrade, posjetite:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**Odricanje od odgovornosti**:
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na svom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni ljudski prijevod. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.