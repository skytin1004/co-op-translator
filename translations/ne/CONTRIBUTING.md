<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:39:37+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ne"
}
-->
# Co-op Translator मा योगदान गर्ने

यो परियोजनाले योगदान र सुझावहरूलाई स्वागत गर्दछ।  अधिकांश योगदानका लागि तपाईंले एक
Contributor License Agreement (CLA) मा सहमति जनाउनु आवश्यक छ, जसले तपाईंले योगदान गर्न अधिकार राख्नुहुन्छ र हामीलाई तपाईंको योगदान प्रयोग गर्न अधिकार दिनुहुन्छ भन्ने घोषणा गर्दछ। थप जानकारीका लागि https://cla.opensource.microsoft.com मा जानुहोस्।

जब तपाईंले pull request पठाउनुहुन्छ, CLA बोटले स्वचालित रूपमा तपाईंलाई CLA आवश्यक छ कि छैन भनेर निर्धारण गर्छ र PR मा उपयुक्त रूपमा जानकारी दिन्छ (जस्तै, status check, टिप्पणी)। बोटले दिएको निर्देशनहरू पालना गर्नुहोस्। तपाईंले हाम्रो CLA प्रयोग गर्ने सबै repos मा यो एकपटक मात्र गर्नुपर्छ।

## विकास वातावरण सेटअप

यस परियोजनाको विकास वातावरण सेटअप गर्न, निर्भरता व्यवस्थापनका लागि Poetry प्रयोग गर्न सिफारिस गरिन्छ। हामी `pyproject.toml` प्रयोग गरेर परियोजनाका निर्भरता व्यवस्थापन गर्छौं, त्यसैले निर्भरता स्थापना गर्न Poetry प्रयोग गर्नुहोस्।

### भर्चुअल वातावरण बनाउने

#### pip प्रयोग गरेर

```bash
python -m venv .venv
```

#### Poetry प्रयोग गरेर

```bash
poetry init
```

### भर्चुअल वातावरण सक्रिय गर्ने

#### दुवै pip र Poetry का लागि

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry प्रयोग गरेर

```bash
poetry shell
```

### प्याकेज र आवश्यक प्याकेजहरू स्थापना गर्ने

#### Poetry प्रयोग गरेर (pyproject.toml बाट)

```bash
poetry install
```

### म्यानुअल परीक्षण

PR पठाउनु अघि, अनुवाद कार्यक्षमता वास्तविक डकुमेन्टेसनमा परीक्षण गर्नु महत्त्वपूर्ण छ:

1. मूल डाइरेक्टरीमा test डाइरेक्टरी बनाउनुहोस्:
    ```bash
    mkdir test_docs
    ```

2. अनुवाद गर्न चाहेको केही markdown डकुमेन्टेसन र छविहरू test डाइरेक्टरीमा प्रतिलिपि गर्नुहोस्। उदाहरणका लागि:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. प्याकेज स्थानीय रूपमा स्थापना गर्नुहोस्:
    ```bash
    pip install -e .
    ```

4. तपाईंको परीक्षण डकुमेन्टहरूमा Co-op Translator चलाउनुहोस्:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` र `test_docs/translated_images` मा अनुवादित फाइलहरू जाँच गर्नुहोस्:
   - अनुवादको गुणस्तर
   - मेटाडाटा टिप्पणीहरू सही छन् कि छैनन्
   - मूल markdown संरचना जस्ताको तस्तै छ कि छैन
   - लिंक र छविहरू ठीकसँग काम गरिरहेका छन् कि छैनन्

यस म्यानुअल परीक्षणले तपाईंका परिवर्तनहरू वास्तविक अवस्थामा राम्रोसँग काम गर्छन् कि गर्दैनन् भन्ने सुनिश्चित गर्न मद्दत गर्छ।

### वातावरण भेरिएबलहरू

1. मूल डाइरेक्टरीमा `.env.template` फाइलको प्रतिलिपि बनाएर `.env` फाइल बनाउनुहोस्।
1. निर्देशन अनुसार वातावरण भेरिएबलहरू भर्नुहोस्।

> [!TIP]
>
> ### थप विकास वातावरण विकल्पहरू
>
> परियोजना स्थानीय रूपमा चलाउनुका साथै, GitHub Codespaces वा VS Code Dev Containers पनि वैकल्पिक विकास वातावरणको रूपमा प्रयोग गर्न सक्नुहुन्छ।
>
> #### GitHub Codespaces
>
> तपाईंले यो नमुना GitHub Codespaces प्रयोग गरेर भर्चुअल रूपमा चलाउन सक्नुहुन्छ, कुनै अतिरिक्त सेटिङ वा सेटअप आवश्यक पर्दैन।
>
> तलको बटनले तपाईंको ब्राउजरमा वेब-आधारित VS Code खोल्नेछ:
>
> 1. टेम्प्लेट खोल्नुहोस् (यसमा केही मिनेट लाग्न सक्छ):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### स्थानीय रूपमा VS Code Dev Containers प्रयोग गरेर चलाउने
>
> ⚠️ यो विकल्प तभी काम गर्छ जब तपाईंको Docker Desktop मा कम्तिमा १६ GB RAM छुट्याइएको छ। यदि तपाईंको RAM १६ GB भन्दा कम छ भने, तपाईं [GitHub Codespaces विकल्प](../..) वा [स्थानीय रूपमा सेटअप](../..) गर्न सक्नुहुन्छ।
>
> सम्बन्धित विकल्प हो VS Code Dev Containers, जसले तपाईंको स्थानीय VS Code मा [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) प्रयोग गरेर परियोजना खोल्छ:
>
> 1. Docker Desktop सुरु गर्नुहोस् (यदि पहिले नै स्थापना गरिएको छैन भने स्थापना गर्नुहोस्)
> 2. परियोजना खोल्नुहोस्:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### कोड शैली

हामी [Black](https://github.com/psf/black) लाई Python कोड फर्म्याटरको रूपमा प्रयोग गर्छौं, जसले परियोजनामा ​​कोड शैली एकरूप राख्न मद्दत गर्छ। Black ले Python कोडलाई स्वचालित रूपमा Black कोड शैलीमा ढाल्छ।

#### कन्फिगरेसन

Black को कन्फिगरेसन हाम्रो `pyproject.toml` मा निर्दिष्ट गरिएको छ:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black स्थापना गर्ने

तपाईं Poetry (सिफारिस गरिएको) वा pip प्रयोग गरेर Black स्थापना गर्न सक्नुहुन्छ:

##### Poetry प्रयोग गरेर

Poetry बाट विकास वातावरण सेटअप गर्दा Black स्वचालित रूपमा स्थापना हुन्छ:
```bash
poetry install
```

##### pip प्रयोग गरेर

यदि तपाईं pip प्रयोग गर्दै हुनुहुन्छ भने, Black सिधै स्थापना गर्न सक्नुहुन्छ:
```bash
pip install black
```

#### Black प्रयोग गर्ने

##### Poetry सँग

1. परियोजनाका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black .
    ```

2. कुनै विशेष फाइल वा डाइरेक्टरी फर्म्याट गर्नुहोस्:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip सँग

1. परियोजनाका सबै Python फाइलहरू फर्म्याट गर्नुहोस्:
    ```bash
    black .
    ```

2. कुनै विशेष फाइल वा डाइरेक्टरी फर्म्याट गर्नुहोस्:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> तपाईंको सम्पादकमा Black प्रयोग गरेर कोड स्वतः फर्म्याट हुने गरी सेटअप गर्न सिफारिस गरिन्छ। अधिकांश आधुनिक सम्पादकहरूले यो सुविधा एक्सटेन्सन वा प्लगइनमार्फत समर्थन गर्छन्।

## Co-op Translator चलाउने

Poetry प्रयोग गरेर Co-op Translator चलाउन, तलका चरणहरू पालना गर्नुहोस्:

1. अनुवाद परीक्षण गर्न चाहेको डाइरेक्टरीमा जानुहोस् वा परीक्षणका लागि अस्थायी फोल्डर बनाउनुहोस्।

2. तलको आदेश चलाउनुहोस्। `-l ko` लाई तपाईं अनुवाद गर्न चाहेको भाषा कोडमा परिवर्तन गर्नुहोस्। `-d` फ्ल्यागले debug मोड जनाउँछ।

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> आदेश चलाउनु अघि तपाईंको Poetry वातावरण सक्रिय (poetry shell) भएको सुनिश्चित गर्नुहोस्।

## नयाँ भाषा योगदान गर्नुहोस्

नयाँ भाषाको समर्थन थप्नका लागि योगदानलाई स्वागत छ। PR खोल्नु अघि, तलका चरणहरू पूरा गर्नुहोस् ताकि समीक्षा सहज होस्।

1. भाषा फन्ट म्यापिङमा थप्नुहोस्
   - `src/co_op_translator/fonts/font_language_mappings.yml` सम्पादन गर्नुहोस्
   - तलका विवरणसहित प्रविष्टि थप्नुहोस्:
     - `code`: ISO-जस्तो भाषा कोड (जस्तै, `vi`)
     - `name`: बुझ्न सजिलो नाम
     - `font`: `src/co_op_translator/fonts/` मा उपलब्ध फन्ट, जसले स्क्रिप्ट समर्थन गर्छ
     - `rtl`: दायाँबाट-बायाँ हो भने `true`, नभए `false`

2. आवश्यक फन्ट फाइलहरू समावेश गर्नुहोस् (आवश्यक परेमा)
   - नयाँ फन्ट आवश्यक भएमा, खुला स्रोत वितरणका लागि लाइसेन्स मिल्छ कि जाँच गर्नुहोस्
   - फन्ट फाइल `src/co_op_translator/fonts/` मा थप्नुहोस्

3. स्थानीय परीक्षण
   - सानो नमुनामा अनुवाद चलाउनुहोस् (Markdown, छवि, र नोटबुक आवश्यक अनुसार)
   - नतिजा सही देखिन्छ कि छैन, फन्ट र RTL लेआउट (यदि लागू हुन्छ) सहित जाँच गर्नुहोस्

4. डकुमेन्टेसन अपडेट गर्नुहोस्
   - भाषा `getting_started/supported-languages.md` मा देखिन्छ कि छैन सुनिश्चित गर्नुहोस्
   - `README_languages_template.md` मा परिवर्तन आवश्यक छैन; यो समर्थित सूचीबाट स्वतः बनाइन्छ

5. PR खोल्नुहोस्
   - थपिएको भाषा र फन्ट/लाइसेन्स सम्बन्धी कुरा उल्लेख गर्नुहोस्
   - सक्दो भएमा, नतिजाको स्क्रिनसट संलग्न गर्नुहोस्

YAML प्रविष्टिको उदाहरण:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### नयाँ भाषा परीक्षण गर्नुहोस्

तपाईं तलको आदेश चलाएर नयाँ भाषा परीक्षण गर्न सक्नुहुन्छ:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## मर्मतकर्ता

### Commit सन्देश र Merge रणनीति

हाम्रो परियोजनाको commit इतिहासमा एकरूपता र स्पष्टता सुनिश्चित गर्न, हामी **Squash and Merge** रणनीति प्रयोग गर्दा अन्तिम commit सन्देशका लागि विशेष ढाँचा पालना गर्छौं।

जब pull request (PR) merge गरिन्छ, व्यक्तिगत commit हरू एकै commit मा मिलाइन्छन्। अन्तिम commit सन्देश तलको ढाँचामा हुनुपर्छ ताकि इतिहास सफा र एकरूप रहोस्।

#### Commit सन्देश ढाँचा (squash and merge का लागि)

हामी commit सन्देशका लागि तलको ढाँचा प्रयोग गर्छौं:

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit को श्रेणी जनाउँछ। हामी तलका प्रकार प्रयोग गर्छौं:
  - `Docs`: डकुमेन्टेसन अपडेटका लागि।
  - `Build`: build सिस्टम वा निर्भरता सम्बन्धी परिवर्तनका लागि, जस्तै कन्फिगरेसन फाइल, CI workflow, वा Dockerfile अपडेट।
  - `Core`: परियोजनाको मुख्य कार्यक्षमता वा फिचरमा परिवर्तनका लागि, विशेष गरी `src/co_op_translator/core` डाइरेक्टरीमा।

- **description**: परिवर्तनको संक्षिप्त सारांश।
- **PR number**: commit सँग सम्बन्धित pull request नम्बर।

**उदाहरणहरू**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> हाल, **`Docs`**, **`Core`**, र **`Build`** prefix हरू PR शीर्षकमा source code मा लागू गरिएका label अनुसार स्वचालित रूपमा थपिन्छन्। सही label लागू भएको छ भने, तपाईंले PR शीर्षक म्यानुअली परिवर्तन गर्न आवश्यक पर्दैन। तपाईंले केवल सबै कुरा सही छ कि छैन र prefix ठीकसँग बनेको छ कि छैन जाँच गर्नुहोस्।

#### Merge रणनीति

हामी pull request का लागि **Squash and Merge** लाई डिफल्ट रणनीति बनाउँछौं। यसले commit सन्देश हाम्रो ढाँचामा रहोस् भन्ने सुनिश्चित गर्छ, भले पनि व्यक्तिगत commit हरूमा त्यो नहोस्।

**कारणहरू**:

- सफा, रेखीय परियोजना इतिहास।
- commit सन्देशमा एकरूपता।
- साना commit (जस्तै, "fix typo") बाट हुने अनावश्यक भीड कम।

Merge गर्दा, अन्तिम commit सन्देश माथि वर्णन गरिएको ढाँचामा छ कि छैन सुनिश्चित गर्नुहोस्।

**Squash and Merge को उदाहरण**
यदि कुनै PR मा तलका commit छन्:

- `fix typo`
- `update README`
- `adjust formatting`

यी सबैलाई मिलाएर यस्तो बनाउनुहोस्:
`Docs: Improve documentation clarity and formatting (#65)`

---

**अस्वीकरण**:
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज़ यसको मौलिक भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।