# Co-op Translator

_Лако аутоматизујте и одржавајте преводе вашег едукативног GitHub садржаја на више језика како ваш пројекат напредује._

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

### 🌐 Подршка за више језика

#### Подржано од стране [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](./README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Више волите да клонирате локално?**
>
> Ово складиште укључује преко 50 превода што значајно повећава величину преузимања. Да бисте клонирали без превода, користите sparse checkout:
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
> Ово вам даје све што вам треба за завршетак курса са много бржим преузимањем.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Преглед

**Co-op Translator** вам помаже да лако лоцирате ваш едукативни GitHub садржај на више језика.  
Када ажурирате своје Markdown датотеке, слике или нотебукове, преводи остају аутоматски синхронизовани што осигурава да ваш садржај буде тачан и ажуран за ученике широм света.

Пример како је преведени садржај организован:

![Example](../../translated_images/sr/translation-ex.0c8aa6a7ee0aad2b.webp)

## Како се управља стањем превода

Co-op Translator управља преведеним садржајем као **верзионисаним софтверским артефактима**,  
а не као статичним датотекама.

Алат прати стање преведеног Markdown-а, слика и нотебукова  
користећи **метаподатке специфичне за језик**.

Овај дизајн омогућава Co-op Translator-у да:

- Поуздано открива застареле преводе
- Обрађује Markdown, слике и нотебуке доследно
- Безбедно скалира кроз велика, брзо мењајућа складишта која подржавају више језика

Моделирајући преводе као управљане артефакте,  
радни токови превођења природно се уклапају у савремене  
практике управљања софтверским зависностима и артефактима.

→ [Како се управља стањем превода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Брзи почетак

```bash
# Креирајте и активирајте виртуелно окружење (препоручено)
python -m venv .venv
# Виндоус
.venv\Scripts\activate
# мацОС/Линукс
source .venv/bin/activate
# Инсталирајте пакет
pip install co-op-translator
# Преведи
translate -l "ko ja fr" -md
```

Docker:

```bash
# Преузмите јавну слику са GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Покрените са монтираним тренутним фолдером и обезбеђеним .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Минимална подешавања

1. Проверите да ли имате подржану верзију Питона (тренутно 3.10-3.12). У poetry (pyproject.toml) ово се аутоматски обрађује.
2. Креирајте `.env` датотеку користећи шаблон: [.env.template](../../.env.template)
3. Конфигуришите једног LLM провајдера (Azure OpenAI или OpenAI)
4. (Опционо) За превод слика (`-img`), конфигуришите Azure AI Vision
5. (Опционо) Можете конфигурисати више скупова акредитива дуплирањем променљивих са суфиксима као што су `_1`, `_2` итд. Све променљиве у скупу морају имати исти суфикс.
6. (Препоручено) Очистите било какве претходне преводе да бисте избегли конфликте (нпр. `translations/`)
7. (Препоручено) Додајте секцију за превод у ваш README користећи [README language template](./getting_started/README_languages_template.md)
8. Погледајте: [Подешавање Azure AI](./getting_started/set-up-azure-ai.md)

## Коришћење

Преведите све подржане типове:

```bash
translate -l "ko ja"
```

Само Markdown:

```bash
translate -l "de" -md
```

Markdown + слике:

```bash
translate -l "pt" -md -img
```

Само нотебуке:

```bash
translate -l "zh" -nb
```

Више опција: [Командна референца](./getting_started/command-reference.md)

## Функције

- Аутоматизован превод за Markdown, нотебуке и слике
- Одржава преводе у синхронизацији са променама у извору
- Ради локално (CLI) или у CI (GitHub Actions)
- Користи Azure OpenAI или OpenAI; по избору Azure AI Vision за слике
- Чува формат и структуру Markdown-а

## Документација

- [Водич за командну линију](./getting_started/command-line-guide/command-line-guide.md)
- [Водич за GitHub Actions (јавни репозиторијуми и стандардне тајне)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Водич за GitHub Actions (Microsoft организациони репозиторијуми и подешавања на нивоу организације)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README language template](./getting_started/README_languages_template.md)
- [Подржани језици](./getting_started/supported-languages.md)
- [Како допринети](./CONTRIBUTING.md)
- [Решавање проблема](./getting_started/troubleshooting.md)

### Microsoft-специфични водич
> [!NOTE]
> Само за одржаваоце Microsoft репозиторијума „За почетнике“.

- [Ажурирање листе „осталих курсева“ (само за Microsoft почетничке репозиторијуме)](./getting_started/update-other-courses.md)

## Подржите нас и унапредите глобално учење

Придружите нам се у револуционисању начина на који се едукативни садржај дели глобално! Дајте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub-у и подржите нашу мисију у скидању језичких баријера у учењу и технологији. Ваш интерес и доприноси сигурно имају значајан утицај! Код и предлози за функције су увек добродошли.

### Истражите Microsoft едукативни садржај на вашем језику

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

## Видео презентације

👉 Кликните на слику испод за гледање на YouTube-у.

- **Open at Microsoft**: Кратак увод од 18 минута и брзи водич како користити Co-op Translator.

  [![Open at Microsoft](../../translated_images/sr/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Како допринети

Овај пројекат добродошло прихвата доприносе и предлоге. Занима вас допринос Azure Co-op Translator-у? Молимо вас да погледате наш [CONTRIBUTING.md](./CONTRIBUTING.md) за смернице како можете помоћи да Co-op Translator буде доступнији.

## Доприносиоци
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Код понашања

Овај пројекат је усвојио [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За више информација погледајте [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) или се обратите на [opencode@microsoft.com](mailto:opencode@microsoft.com) са додатним питањима или коментарима.

## Одговорна вештачка интелигенција

Microsoft је посвећен помагању нашим корисницима да одговорно користе наше AI производе, делећи наша сазнања и градећи партнерства заснована на поверењу кроз алате попут Transparency Notes и Impact Assessments. Многи од ових ресурса могу се наћи на [https://aka.ms/RAI](https://aka.ms/RAI).
Microsoft-ов приступ одговорној вештачкој интелигенцији заснован је на нашим AI принципима праведности, поузданости и безбедности, приватности и сигурности, инклузивности, транспарентности и одговорности.

Велики модели природног језика, слика и говора - као они коришћени у овом примеру - могу потенцијално да се понашају на начине који нису праведни, поуздани или могу бити увредљиви, што може изазвати штете. Молимо вас да консултујете [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.

Препоручени приступ за ублажавање ових ризика јесте укључивање система безбедности у вашу архитектуру који може детектовати и спречити штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) пружа независни слој заштите, способан да детектује штетни кориснички и AI генерисани садржај у апликацијама и сервисима. Azure AI Content Safety укључује текстуалне и сликовне API-је који вам омогућавају да детектујете штетни материјал. Такође имамо интерактивно Content Safety Studio које вам омогућава да погледате, истражите и испробате пример кода за детекцију штетног садржаја кроз различите модалитете. Следећа [quickstart документација](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) вас води кроз како да правите захтеве сервису.

Још један аспект који треба узети у обзир је укупне перформансе апликације. Са мултимодалним и мултимодел апликацијама, перформансе сматрамо као то да систем ради онако како ви и ваши корисници очекујете, укључујући и то да не генерише штетне излазне податке. Важно је проценити перформансе ваше укупне апликације користећи [генеративне квалитете и метрике ризика и безбедности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете проценити своју AI апликацију у вашем развојном окружењу користећи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Са или тестним скупом података или циљем, генерације ваше генеративне AI апликације су квантитативно мерене са интегрисаним или прилагођеним процењивачима по вашем избору. Да бисте почели са prompt flow SDK за процену вашег система, можете пратити [quickstart водич](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када извршите процену, можете [види резултате у Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Знакови заштићене робне марке

Овај пројекат може садржати заштићене робне марке или логотипе пројеката, производа или услуга. Овлашћена употреба Microsoft
заштићених робних марки или логотипа је предмет и мора се придржавати
[Microsoft-ових смерница за заштићене знакове и бренд](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Употреба Microsoft-ових робних марки или логотипа у модификованим верзијама овог пројекта не сме изазивати забуну или имплицирати спонзорство од стране Microsoft-а.
Било каква употреба трећих робних марки или логотипа подлежe политикама тих трећих лица.

## Како добити помоћ

Ако запнете или имате питања о изради AI апликација, придружите се:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате повратне информације о производу или грешке током израде посетите:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ограничење одговорности**:  
Овај документ је преведен користећи AI услугу за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->