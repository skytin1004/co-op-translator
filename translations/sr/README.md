# Co-op Translator

_Једноставно аутоматизујте и одржавајте преводе вашег едукативног GitHub садржаја на више језика како се ваш пројекат развија._

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

> **Претпочитате да клонирате локално?**
>
> Овај репозиторијум садржи више од 50 превода што значајно повећава величину скидања. Да бисте клонирали без превода, користите sparse checkout:
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
> Ово вам даје све што вам треба да завршите курс са много бржим скидањем.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Преглед

**Co-op Translator** вам помаже да лако локализујете ваш едукативни GitHub садржај на више језика.  
Када ажурирате ваше Markdown фајлове, слике или белешке (notebooks), преводи се аутоматски синхронизују, осигуравајући да садржај остане тачан и ажуран за ученике широм света.

Пример како је преведени садржај организован:

![Example](../../imgs/translation-ex.png)

## Како се управља стањем превода

Co-op Translator обрађује преведени садржај као **верзионисане софтверске артефакте**,  
не као статичне фајлове.

Алат прати стање преведеног Markdown-а, слика и бележница  
користећи **метаподатке у оквиру језика**.

Овај дизајн омогућава Co-op Translator-у да:

- Поуздано детектује застареле преводе
- Истоветно третира Markdown, слике и белешке
- Безбедно скалира на великим, брзо мењајућим, мулти-језичким репозиторијумима

Моделирањем превода као управљаних артефаката,  
радни токови превођења се природно усклађују са савременим  
практикама управљања софтверским зависностима и артефактима.

→ [Како се управља стањем превода](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Брзи почетак

```bash
# Креирајте и активирајте виртуелно окружење (препоручено)
python -m venv .venv
# Виндоус
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Инсталирајте пакет
pip install co-op-translator
# Преведи
translate -l "ko ja fr" -md
```

Docker:

```bash
# Повуците јавну слику са GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Покрените са монтираним тренутним фолдером и обезбеђеним .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Минимално подешавање

1. Уверите се да имате подржану верзију Python-а (тренутно 3.10-3.12). У poetry (pyproject.toml) је ово аутоматски решено.
2. Креирајте `.env` фајл користећи шаблон: [.env.template](../../.env.template)
3. Конфигуришите једног провајдера LLM (Azure OpenAI или OpenAI)
4. (Опционо) За превођење слика (`-img`), конфигуришите Azure AI Vision
5. (Опционо) Можете конфигурисати више сета акредитива дуплицирајући променљиве са наставцима као `_1`, `_2` итд. Све променљиве у скупу морају имати исти наставак.
6. (Препоручено) Очистите све претходне преводе како бисте избегли конфликте (нпр. `translations/`)
7. (Препоручено) Додајте одељак за превођење у ваш README користећи [README languages template](./getting_started/README_languages_template.md)
8. Погледајте: [Подешавање Azure AI](./getting_started/set-up-azure-ai.md)

## Употреба

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

Само белешке:

```bash
translate -l "zh" -nb
```

Више параметара: [Командна референца](./getting_started/command-reference.md)

## Карактеристике

- Аутоматизовано превођење за Markdown, белешке и слике
- Преводи се држе усклађеним са променама у извору
- Ради локално (CLI) или у CI (GitHub Actions)
- Користи Azure OpenAI или OpenAI; опционално Azure AI Vision за слике
- Чува Markdown формат и структуру

## Документација

- [Водич за командну линију](./getting_started/command-line-guide/command-line-guide.md)
- [Водич за GitHub Actions (Јавни репозиторијуми и стандардни секрети)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Водич за GitHub Actions (Microsoft организациони репозиторијуми и организациона подешавања)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [README шаблон за језике](./getting_started/README_languages_template.md)
- [Подржани језици](./getting_started/supported-languages.md)
- [Учествовање у развоју](./CONTRIBUTING.md)
- [Решавање проблема](./getting_started/troubleshooting.md)

### Водич специфичан за Microsoft
> [!NOTE]
> Само за одржаваоце Microsoft “For Beginners” репозиторијума.

- [Ажурирање листе “других курсева” (само за MS Beginners репозиторијуме)](./getting_started/update-other-courses.md)

## Подржите нас и промовишите глобално учење

Придружите нам се у револуционисању начина на који се едукативни садржај дели глобално! Дајте [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ на GitHub-у и подржите нашу мисију уклањања језичких баријера у учењу и технологији. Ваш интерес и доприноси имају значајан утицај! Доприноси коду и предлози за функције су увек добродошли.

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

👉 Кликните на слику испод да гледате на YouTube-у.

- **Open at Microsoft**: Кратак 18-минутни увод и брзи водич како користити Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Учествовање у развоју

Овај пројекат је отворен за доприносе и предлоге. Заинтересовани сте да допринесете Azure Co-op Translator-у? Молимо вас погледајте наш [CONTRIBUTING.md](./CONTRIBUTING.md) за упутства како можете помоћи да Co-op Translator буде приступачнији.

## Доприносиоци
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Кодекс понашања

Овај пројекат је прихватио [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
За више информација погледајте [Честа питања о Кодексу понашања](https://opensource.microsoft.com/codeofconduct/faq/) или
контактирајте [opencode@microsoft.com](mailto:opencode@microsoft.com) са додатним питањима или коментарима.

## Одговорни AI

Microsoft је посвећен помагању нашим корисницима да одговорно користе наше AI производе, делећи наша сазнања и градећи партнерства заснована на поверењу кроз алате као што су Transparency Notes и Impact Assessments. Многи од ових ресурса могу се пронаћи на [https://aka.ms/RAI](https://aka.ms/RAI).
Приступ Microsoft-а одговорном AI-у заснован је на нашим AI принципима праведности, поузданости и безбедности, приватности и безбедности, инклузивности, транспарентности и одговорности.

Модели великог обима за природни језик, слику и говор - као они који се користе у овом примеру - потенцијално могу да се понашају на начине који нису праведни, поуздани или могу бити увредљиви, што може изазвати штету. Молимо вас да консултујете [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) како бисте били информисани о ризицима и ограничењима.

Препоручени приступ ублажавању ових ризика је укључивање система безбедности у вашу архитектуру који може да детектује и спречи штетно понашање. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) пружа независни слој заштите, способан да детектује штетни кориснички и AI генерисани садржај у апликацијама и сервисима. Azure AI Content Safety укључује текстуалне и сликовне API-је који вам омогућавају да детектујете материјал који је штетан. Такође имамо интерактивни Content Safety Studio који вам омогућава да гледате, истражујете и испробате пример кода за детекцију штетног садржаја кроз разне модалитете. Следећа [quickstart документација](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) вас води кроз прављење захтева сервису.

Још један аспект који треба узети у обзир је укупна перформанса апликације. Код мултимодалних и мултимоделских апликација, перформанса подразумева да систем делује онако како ви и ваши корисници очекујете, укључујући да не генерише штетне резултате. Важно је проценити перформансе ваше укупне апликације користећи [метрике квалитета генерације и ризика и безбедности](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Можете проценити вашу AI апликацију у вашем развојном окружењу користећи [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Узете генерације ваше генеративне AI апликације се квантитативно мере помоћу уграђених или прилагођених евалуатора по вашем избору, уз тест скуп података или циљ. Да бисте започели коришћење prompt flow SDK за процену вашег система, можете пратити [quickstart водич](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Када извршите процену, можете [визуализовати резултате у Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Заштитни знаци

Овај пројекат може садржати заштитне знаке или логотипе пројеката, производа или услуга. Овлашћена употреба Microsoft
заштитних знакова или логотипа подлеже и мора пратити
[Microsoft-ова правила за коришћење заштитних знакова и брендова](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Употреба Microsoft заштитних знакова или логотипа у модификованим верзијама овог пројекта не сме изазивати забуну нити имплицирати спонзорство Microsoft-а.
Употреба заштитних знакова или логотипа трећих страна подложна је правилима тих трећих страна.

## Добијање помоћи

Ако сте заглављени или имате питања о изградњи AI апликација, придружите се:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Уколико имате повратне информације о производу или грешке током развоја посете:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање од одговорности**:  
Овај документ је преведен коришћењем АИ преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо тачности, имајте на уму да аутоматизовани преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешна тумачења која произлазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->