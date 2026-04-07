# Co-op Translator

_Madaling i-automate at panatilihin ang mga pagsasalin para sa iyong edukasyonal na nilalaman sa GitHub sa maraming wika habang umuunlad ang iyong proyekto._

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

### 🌐 Suporta ng Maramihang Wika

#### Sinusuportahan ng [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](./README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Mas gusto mo bang I-clone nang Lokal?**
>
> Ang repositoryong ito ay may kasamang 50+ mga pagsalin ng wika na malaki ang pinapataas sa laki ng pag-download. Upang mag-clone nang walang mga pagsasalin, gamitin ang sparse checkout:
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
> Binibigyan ka nito ng lahat ng kailangan mo para matapos ang kurso nang mas mabilis ang pag-download.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Pangkalahatang-ideya

**Co-op Translator** ay tumutulong sa iyo na i-localize ang iyong edukasyonal na nilalaman sa GitHub sa maraming wika nang walang kahirap-hirap.
Kapag ina-update mo ang iyong mga Markdown na file, mga larawan, o notebooks, nananatiling awtomatikong naka-synchronize ang mga pagsasalin, na tinitiyak na ang iyong nilalaman ay eksakto at napapanahon para sa mga nag-aaral sa buong mundo.

Halimbawa kung paano nakaayos ang isinaling nilalaman:

![Example](../../imgs/translation-ex.png)

## Paano pinamamahalaan ang estado ng pagsasalin

Pinamamahalaan ng Co-op Translator ang isinaling nilalaman bilang **versioned software artifacts**,  
hindi bilang mga static na file.

Minomonitor ng tool ang estado ng isinaling Markdown, mga larawan, at notebooks
gamit ang **language-scoped metadata**.

Pinapayagan ng disenyo na ito ang Co-op Translator na:

- Maaasahang matukoy ang lipas na mga pagsasalin
- Tratuhin nang pareho ang Markdown, mga larawan, at notebooks
- Ligtas na mag-scale sa malalaking, mabilis na umuusad, multi-lingual na repositoryo

Sa pamamagitan ng pagmodel ng mga pagsasalin bilang mga pinamamahalaang artifact,
natural na tumutugma ang mga workflow sa pagsasalin sa modernong
software dependency at artifact management na mga kasanayan.

→ [Paano pinamamahalaan ang estado ng pagsasalin](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Mabilis na pagsisimula

```bash
# Gumawa at i-activate ang isang virtual na kapaligiran (inirerekomenda)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# I-install ang package
pip install co-op-translator
# Isalin
translate -l "ko ja fr" -md
```

Docker:

```bash
# Kunin ang pampublikong imahe mula sa GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Patakbuhin na may naka-mount na kasalukuyang folder at ibinigay na .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Minimal na setup

1. Tiyaking meron kang suportadong bersyon ng Python (kasalukuyang 3.10-3.12). Sa poetry (pyproject.toml) awtomatikong hinahandle ito.
2. Gumawa ng `.env` file gamit ang template: [.env.template](../../.env.template)
3. I-configure ang isang LLM provider (Azure OpenAI o OpenAI)
4. (Opsyonal) Para sa pagsasalin ng larawan (`-img`), i-configure ang Azure AI Vision
5. (Opsyonal) Maaari kang mag-configure ng maraming set ng kredensyal sa pamamagitan ng pag-duplicate ng mga variable na may mga suffix tulad ng `_1`, `_2`, atbp. Lahat ng variable sa isang set ay dapat may parehong suffix.
6. (Inirerekomenda) Linisin ang anumang naunang mga pagsasalin upang maiwasan ang mga conflict (hal., `translations/`)
7. (Inirerekomenda) Magdagdag ng seksyon ng pagsasalin sa iyong README gamit ang [README languages template](./getting_started/README_languages_template.md)
8. Tingnan: [I-set up ang Azure AI](./getting_started/set-up-azure-ai.md)

## Paggamit

Isalin lahat ng suportadong uri:

```bash
translate -l "ko ja"
```

Markdown lamang:

```bash
translate -l "de" -md
```

Markdown + mga larawan:

```bash
translate -l "pt" -md -img
```

Notebooks lamang:

```bash
translate -l "zh" -nb
```

Marami pang flags: [Command reference](./getting_started/command-reference.md)

## Mga Tampok

- Awtomatikong pagsasalin para sa Markdown, notebooks, at larawan
- Pinananatiling naka-sync ang mga pagsasalin sa mga pagbabago sa pinagmulan
- Gumagana lokal (CLI) o sa CI (GitHub Actions)
- Gumagamit ng Azure OpenAI o OpenAI; opsyonal ang Azure AI Vision para sa mga larawan
- Pinapanatili ang formatting at istruktura ng Markdown

## Dokumentasyon

- [Gabayan sa command-line](./getting_started/command-line-guide/command-line-guide.md)
- [Gabayan sa GitHub Actions (Public repositories & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Gabayan sa GitHub Actions (Microsoft organization repositories & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README languages template](./getting_started/README_languages_template.md)
- [Suportadong mga wika](./getting_started/supported-languages.md)
- [Pagtutulungan](./CONTRIBUTING.md)
- [Pagsasaayos ng Problema](./getting_started/troubleshooting.md)

### Microsoft-specific guide
> [!NOTE]
> Para sa mga tagapangasiwa lamang ng Microsoft “For Beginners” repositories.

- [Pag-update ng listahan ng “iba pang mga kurso” (para sa MS Beginners repositories lamang)](./getting_started/update-other-courses.md)

## Suportahan kami at palaganapin ang global na pagkatuto

Sumali sa amin sa pagbabago kung paano naaabot ang edukasyonal na nilalaman sa buong mundo! Bigyan ng ⭐ ang [Co-op Translator](https://github.com/azure/co-op-translator) sa GitHub at suportahan ang aming layunin na alisin ang hadlang sa wika sa pag-aaral at teknolohiya. Malaki ang epekto ng iyong interes at kontribusyon! Laging bukas ang kontribusyon ng code at mga mungkahi sa tampok.

### Tuklasin ang mga edukasyonal na nilalaman ng Microsoft sa iyong wika

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

## Mga Presentasyong Video

👉 I-click ang imahe sa ibaba upang manood sa YouTube.

- **Open at Microsoft**: Isang maikling 18-minutong pagpapakilala at mabilis na gabay kung paano gamitin ang Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Pagtutulungan

Tinatanggap ng proyektong ito ang mga kontribusyon at mungkahi. Interesado kang tumulong sa Azure Co-op Translator? Mangyaring tingnan ang aming [CONTRIBUTING.md](./CONTRIBUTING.md) para sa mga alituntunin kung paano ka makakatulong upang gawing mas accessible ang Co-op Translator.

## Mga Kontribyutor
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Code of Conduct

Inamponan ng proyektong ito ang [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
Para sa karagdagang impormasyon tingnan ang [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) o
makipag-ugnayan sa [opencode@microsoft.com](mailto:opencode@microsoft.com) para sa anumang karagdagang mga katanungan o komento.

## Responsible AI

Nakatutok ang Microsoft sa pagtulong sa aming mga customer na gamitin nang responsable ang aming mga produktong AI, ibahagi ang aming mga natutunan, at bumuo ng mga partnership na nakabase sa pagtitiwala sa pamamagitan ng mga kasangkapang tulad ng Transparency Notes at Impact Assessments. Maraming sa mga mapagkukunang ito ay matatagpuan sa [https://aka.ms/RAI](https://aka.ms/RAI).
Ang paraan ng Microsoft sa responsible AI ay nakabatay sa aming mga prinsipyo ng AI tulad ng katarungan, pagiging maaasahan at kaligtasan, privacy at seguridad, pagsasama-sama, pagiging bukas, at pananagutan.

Ang mga malakihang modelo para sa natural na wika, larawan, at pananalita - tulad ng ginagamit sa sample na ito - ay maaaring kumilos sa paraang hindi patas, hindi maaasahan, o nakasasakit, na maaaring magdulot ng kapinsalaan. Mangyaring sumangguni sa [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) upang malaman ang tungkol sa mga panganib at limitasyon.

Ang inirerekomendang paraan upang mabawasan ang mga panganib na ito ay ang pagsama ng sistema ng kaligtasan sa iyong arkitektura na kayang matukoy at pigilan ang mapanirang pag-uugali. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ay nagbibigay ng isang independiyenteng patong ng proteksyon, na kayang tuklasin ang mapanganib na nilikhang nilalaman ng gumagamit at AI sa mga aplikasyon at serbisyo. Ang Azure AI Content Safety ay may kasamang text at image APIs na nagpapahintulot sa iyo na matukoy ang materyal na mapanganib. Mayroon din kaming interactive Content Safety Studio na nagpapahintulot sa iyo na makita, tuklasin, at subukan ang mga halimbawa ng code para sa pagtuklas ng mapanganib na nilalaman sa iba't ibang anyo. Ang sumusunod na [quickstart documentation](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ay gagabay sa iyo sa paggawa ng mga kahilingan sa serbisyo.

Isa pang aspeto na dapat isaalang-alang ay ang pangkalahatang pagganap ng aplikasyon. Sa mga multi-modal at multi-model na aplikasyon, itinuturing naming ang pagganap ay nangangahulugang gumaganap ang sistema ayon sa inaasahan mo at ng iyong mga gumagamit, kabilang ang hindi paglikha ng mapanirang output. Mahalaga na suriin ang pagganap ng iyong pangkalahatang aplikasyon gamit ang [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Maaari mong suriin ang iyong AI application sa iyong development environment gamit ang [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Sa pamamagitan ng isang test dataset o target, nasusukat ng mga built-in na evaluator o sariling evaluator ang mga nilikha ng iyong generative AI application nang kwantitatibo. Para makapagsimula gamit ang prompt flow sdk upang suriin ang iyong sistema, maaari mong sundan ang [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Kapag naisagawa mo na ang isang evaluation run, maaari mong [ipakita ang mga resulta sa Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Trademarks

Maaaring naglalaman ang proyektong ito ng mga trademark o logo para sa mga proyekto, produkto, o serbisyo. Ang awtorisadong paggamit ng mga Microsoft
trademark o logo ay napapailalim at kailangang sumunod sa
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Ang paggamit ng mga Microsoft trademark o logo sa mga binagong bersyon ng proyektong ito ay hindi dapat magdulot ng kalituhan o magpahiwatig ng pagsuporta ng Microsoft.
Ang anumang paggamit ng mga trademark o logo ng third-party ay napapailalim sa mga patakaran ng mga iyon.

## Getting Help

Kung naipit ka o may mga tanong tungkol sa paggawa ng mga AI app, sumali sa:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Kung mayroon kang puna tungkol sa produkto o mga error habang bumubuo, bisitahin:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI na pagsasalin na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->