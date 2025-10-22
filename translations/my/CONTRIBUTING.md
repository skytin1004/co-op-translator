<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T14:12:39+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "my"
}
-->
# Co-op Translator တွင် ပါဝင်ကူညီခြင်း

ဒီ project က ပါဝင်ကူညီမှုတွေနဲ့ အကြံပြုချက်တွေကို ကြိုဆိုပါတယ်။  များသောအားဖြင့် ပါဝင်ကူညီမှုတစ်ခုလုပ်ဖို့ Contributor License Agreement (CLA) ကို သဘောတူလက်မှတ်ရေးထိုးဖို့ လိုအပ်ပါတယ်။ ဒါက သင့်မှာ ဒီ project ကို အသုံးပြုခွင့်ရှိတယ်ဆိုတာနဲ့ သင့်ရဲ့ ပါဝင်ကူညီမှုကို ကျွန်တော်တို့အသုံးပြုခွင့်ရှိတယ်ဆိုတာ ကြေညာတာပါ။ အသေးစိတ်ကို https://cla.opensource.microsoft.com မှာ ကြည့်နိုင်ပါတယ်။

သင် pull request တင်တဲ့အခါ CLA bot က သင် CLA လိုအပ်/မလိုအပ် စစ်ဆေးပြီး PR ကို အခြေအနေ (status check, comment) နဲ့ ပြသပေးပါလိမ့်မယ်။ Bot ရဲ့ ညွှန်ကြားချက်အတိုင်း လိုက်နာရုံပါပဲ။ ဒီ CLA ကို သုံးတဲ့ repo တွေအားလုံးမှာ တစ်ကြိမ်တည်း လုပ်ရုံပါပဲ။

## Development environment တပ်ဆင်ခြင်း

ဒီ project အတွက် development environment တပ်ဆင်ဖို့ Poetry ကို dependency management အတွက် အသုံးပြုဖို့ အကြံပြုပါတယ်။ Project dependency တွေကို `pyproject.toml` မှာ စီမံထားတာကြောင့် dependency တွေ install လုပ်ဖို့ Poetry ကို သုံးသင့်ပါတယ်။

### Virtual environment တစ်ခု ဖန်တီးခြင်း

#### pip သုံးခြင်း

```bash
python -m venv .venv
```

#### Poetry သုံးခြင်း

```bash
poetry init
```

### Virtual environment ကို အသက်သွင်းခြင်း

#### pip နဲ့ Poetry နှစ်ခုလုံးအတွက်

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry သုံးခြင်း

```bash
poetry shell
```

### Package နဲ့ လိုအပ်တဲ့ Packages တွေ Install လုပ်ခြင်း

#### Poetry (pyproject.toml မှ) သုံးခြင်း

```bash
poetry install
```

### Manual စမ်းသပ်ခြင်း

PR တင်မယ့်အခါမှာ translation လုပ်တဲ့ function တွေကို documentation အမှန်နဲ့ စမ်းသပ်ကြည့်တာ အရေးကြီးပါတယ်။

1. root directory မှာ test directory တစ်ခု ဖန်တီးပါ။
    ```bash
    mkdir test_docs
    ```

2. သင်ဘာ markdown documentation နဲ့ image တွေကို ဘာသာပြန်ချင်လဲဆိုတာ test directory ထဲကို ကူးထည့်ပါ။ ဥပမာ -
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. package ကို local မှာ install လုပ်ပါ။
    ```bash
    pip install -e .
    ```

4. သင့် test document တွေမှာ Co-op Translator ကို run ပါ။
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` နဲ့ `test_docs/translated_images` ထဲက ဘာသာပြန်ပြီးတဲ့ ဖိုင်တွေကို စစ်ဆေးပါ -
   - ဘာသာပြန်မှု အရည်အသွေး
   - metadata comment တွေ မှန်/မမှန်
   - မူရင်း markdown ဖွဲ့စည်းပုံ မပြောင်းလဲဘူးလား
   - Link နဲ့ image တွေ အလုပ်လုပ်/မလုပ်

ဒီလို manual စမ်းသပ်ခြင်းက သင့်ပြင်ဆင်မှုတွေ အမှန်တကယ် အလုပ်လုပ်လားဆိုတာ သေချာစေပါတယ်။

### Environment variable တွေ

1. root directory မှာ `.env.template` ကို ကူးပြီး `.env` ဖိုင်တစ်ခု ဖန်တီးပါ။
1. ညွှန်ကြားချက်အတိုင်း environment variable တွေ ဖြည့်ပါ။

> [!TIP]
>
> ### Development environment တပ်ဆင်ဖို့ နောက်ထပ်ရွေးချယ်စရာများ
>
> Project ကို local မှာ run လုပ်ခြင်းအပြင် GitHub Codespaces သို့မဟုတ် VS Code Dev Containers ကိုလည်း အသုံးပြုနိုင်ပါတယ်။
>
> #### GitHub Codespaces
>
> GitHub Codespaces ကို အသုံးပြုပြီး sample တွေကို virtual အနေနဲ့ run လုပ်နိုင်ပါတယ်။ ထပ်မံတပ်ဆင်စရာမလိုပါ။
>
> ဒီ button ကိုနှိပ်ရုံနဲ့ browser ထဲမှာ web-based VS Code instance ကို ဖွင့်နိုင်ပါတယ် -
>
> 1. template ကို ဖွင့်ပါ (အချို့အခါ မိနစ်အနည်းငယ် ကြာနိုင်ပါတယ်) -
>
>     [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/azure/co-op-translator)
>
> #### VS Code Dev Containers နဲ့ Local မှာ Run လုပ်ခြင်း
>
> ⚠️ ဒီနည်းလမ်းကို သုံးချင်ရင် သင့် Docker Desktop မှာ အနည်းဆုံး 16 GB RAM ခွဲထားရပါမယ်။ 16 GB ထက်နည်းရင် [GitHub Codespaces](../..) သို့မဟုတ် [local မှာ တပ်ဆင်ခြင်း](../..) ကို စမ်းကြည့်နိုင်ပါတယ်။
>
> နောက်ထပ်ရွေးချယ်စရာတစ်ခုက VS Code Dev Containers ပါ။ ဒါက [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) ကို သုံးပြီး သင့် local VS Code မှာ project ကို ဖွင့်ပေးပါလိမ့်မယ်။
>
> 1. Docker Desktop ကို စတင်ပါ (မရှိသေးရင် install လုပ်ပါ)
> 2. Project ကို ဖွင့်ပါ -
>
>    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator)


### Code Style

Project တစ်ခုလုံးမှာ code style တူညီစေရန် [Black](https://github.com/psf/black) Python code formatter ကို သုံးပါတယ်။ Black က Python code ကို Black style နဲ့ အလိုအလျောက် ပြန်စီပေးပါတယ်။

#### Configuration

Black အတွက် configuration ကို `pyproject.toml` ထဲမှာ သတ်မှတ်ထားပါတယ် -

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black ကို Install လုပ်ခြင်း

Poetry (အကြံပြု) သို့မဟုတ် pip နဲ့ Black ကို install လုပ်နိုင်ပါတယ်။

##### Poetry သုံးခြင်း

Development environment တပ်ဆင်တဲ့အခါ Black ကို အလိုအလျောက် install လုပ်ပေးပါတယ် -
```bash
poetry install
```

##### pip သုံးခြင်း

pip သုံးရင် Black ကို တိုက်ရိုက် install လုပ်နိုင်ပါတယ် -
```bash
pip install black
```

#### Black ကို အသုံးပြုခြင်း

##### Poetry နဲ့

1. Project ထဲက Python ဖိုင်အားလုံးကို format လုပ်ပါ -
    ```bash
    poetry run black .
    ```

2. ဖိုင်တစ်ခု သို့မဟုတ် directory တစ်ခုကို format လုပ်ချင်ရင် -
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip နဲ့

1. Project ထဲက Python ဖိုင်အားလုံးကို format လုပ်ပါ -
    ```bash
    black .
    ```

2. ဖိုင်တစ်ခု သို့မဟုတ် directory တစ်ခုကို format လုပ်ချင်ရင် -
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> သင့် editor မှာ Black နဲ့ code ကို auto-format လုပ်ဖို့ on save ပြုလုပ်ထားဖို့ အကြံပြုပါတယ်။ Editor များစွာမှာ extension သို့မဟုတ် plugin တွေနဲ့ ဒီ feature ကို ထည့်နိုင်ပါတယ်။

## Co-op Translator ကို Run လုပ်ခြင်း

Poetry ကို သုံးပြီး Co-op Translator ကို run လုပ်ချင်ရင် အောက်ပါအဆင့်တွေလိုက်နာပါ -

1. ဘာသာပြန်စမ်းသပ်ချင်တဲ့ directory ကို သွားပါ သို့မဟုတ် စမ်းသပ်ဖို့အတွက် အချို့ folder တစ်ခု temporary ဖန်တီးပါ။

2. အောက်ပါ command ကို run ပါ။ `-l ko` ကို သင်ဘာဘာသာပြန်ချင်တဲ့ language code နဲ့ ပြောင်းပါ။ `-d` flag က debug mode ဖြစ်ပါတယ်။

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Command ကို run မလုပ်ခင် Poetry environment ကို activate (poetry shell) လုပ်ထားဖို့ သေချာပါစေ။

## ဘာသာစကားအသစ် ထပ်ထည့်လိုပါက

ဘာသာစကားအသစ်ထည့်ဖို့ ပါဝင်ကူညီမှုကို ကြိုဆိုပါတယ်။ PR တင်မယ့်အခါ အောက်ပါအဆင့်တွေ ပြီးစီးထားမှ review လုပ်ရလွယ်ပါတယ်။

1. Font mapping ထဲမှာ ဘာသာစကားထည့်ပါ
   - `src/co_op_translator/fonts/font_language_mappings.yml` ကို ပြင်ပါ
   - အောက်ပါအတိုင်း entry တစ်ခုထည့်ပါ -
     - `code`: ISO နဲ့ဆင်တဲ့ language code (ဥပမာ - `vi`)
     - `name`: လူသိများတဲ့ display name
     - `font`: `src/co_op_translator/fonts/` ထဲမှာပါဝင်ပြီး script ကို support လုပ်တဲ့ font
     - `rtl`: ညာဘက်မှ ဘယ်ဘက် (right-to-left) ဆိုရင် `true`, မဟုတ်ရင် `false`

2. လိုအပ်ရင် font ဖိုင်ထည့်ပါ
   - Font အသစ်လိုအပ်ရင် open source ဖြန့်ဝေခွင့်ရှိ/မရှိ စစ်ဆေးပါ
   - Font ဖိုင်ကို `src/co_op_translator/fonts/` ထဲထည့်ပါ

3. Local မှာ စမ်းသပ်ပါ
   - နမူနာ (Markdown, image, notebook) နဲ့ ဘာသာပြန် run လုပ်ပါ
   - Output မှာ font, RTL layout (လိုအပ်လျှင်) မှန်/မမှန် စစ်ပါ

4. Documentation ပြင်ပါ
   - `getting_started/supported-languages.md` ထဲမှာ ဘာသာစကားအသစ်ပါဝင်စေပါ
   - `README_languages_template.md` ကို ပြင်စရာမလိုပါဘူး။ ဒါက supported list မှ auto generate ဖြစ်ပါတယ်

5. PR တင်ပါ
   - ထည့်သွင်းတဲ့ ဘာသာစကားနဲ့ font/license အကြောင်းဖော်ပြပါ
   - ရနိုင်ရင် output screenshot တွေပါထည့်ပါ

YAML entry နမူနာ -

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### ဘာသာစကားအသစ်ကို စမ်းသပ်ခြင်း

အောက်ပါ command နဲ့ ဘာသာစကားအသစ်ကို စမ်းသပ်နိုင်ပါတယ် -

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

## Maintainers

### Commit message နဲ့ Merge strategy

Project ရဲ့ commit history ကို တစ်သွေတည်း၊ ရှင်းလင်းစေရန် **Squash and Merge** strategy ကို သုံးတဲ့အခါ **နောက်ဆုံး commit message** အတွက် commit message format တစ်ခု သတ်မှတ်ထားပါတယ်။

Pull request (PR) တစ်ခု merge လုပ်တဲ့အခါ commit တွေကို တစ်ခုတည်းအဖြစ် squash လုပ်ပါလိမ့်မယ်။ နောက်ဆုံး commit message ကို အောက်ပါ format နဲ့ ရေးသင့်ပါတယ်။

#### Commit message format (squash and merge အတွက်)

Commit message တွေကို အောက်ပါ format နဲ့ သုံးပါတယ် -

```bash
<type>: <description> (#<PR number>)
```

- **type**: commit ရဲ့ အမျိုးအစား။ အောက်ပါအမျိုးအစားတွေသုံးပါတယ် -
  - `Docs`: Documentation update တွေအတွက်။
  - `Build`: Build system သို့မဟုတ် dependency, config file, CI workflow, Dockerfile ပြင်ဆင်မှုအတွက်။
  - `Core`: Project ရဲ့ core function/feature တွေ (အထူးသဖြင့် `src/co_op_translator/core` ထဲက ဖိုင်တွေ) ပြင်ဆင်မှုအတွက်။

- **description**: ပြင်ဆင်မှုအကျဉ်းချုပ်။
- **PR number**: Pull request နံပါတ်။

**ဥပမာများ** -

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> လက်ရှိမှာ **`Docs`**, **`Core`**, **`Build`** prefix တွေကို PR title မှာ label အပေါ်မူတည်ပြီး auto ထည့်ပေးပါတယ်။ Label မှန်မှန်တပ်ထားရင် PR title ကို ကိုယ်တိုင်ပြင်စရာမလိုပါဘူး။ Prefix မှန်/မမှန် စစ်ဆေးပေးရုံပါပဲ။

#### Merge strategy

Pull request တွေအတွက် **Squash and Merge** ကို default strategy အနေနဲ့ သုံးပါတယ်။ ဒီနည်းလမ်းက commit message တွေ format ကို တစ်သွေတည်းထားနိုင်စေပါတယ်။

**အကြောင်းပြချက်များ** -

- Project history ကို ရှင်းလင်း၊ တစ်ကြောင်းတည်းထားနိုင်တယ်။
- Commit message တွေ တစ်သွေတည်း။
- အရေးမကြီးတဲ့ commit (ဥပမာ - "fix typo") တွေကြောင့် noise လျော့တယ်။

Merge လုပ်တဲ့အခါ နောက်ဆုံး commit message ကို အထက်ပါ format နဲ့ ရေးထားတာ သေချာပါစေ။

**Squash and Merge ဥပမာ**
PR တစ်ခုမှာ အောက်ပါ commit တွေပါဝင်ရင် -

- `fix typo`
- `update README`
- `adjust formatting`

ဒါတွေကို squash လုပ်ပြီး -
`Docs: Improve documentation clarity and formatting (#65)`

---

**သတိပေးချက်**:
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှုအတွက် ကြိုးစားနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မတိကျမှုများ ပါဝင်နိုင်သည်ကို သတိပြုပါ။ မူရင်းစာရွက်စာတမ်းသည် မူလဘာသာစကားဖြင့် အာဏာရှိသောရင်းမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသောအချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်များ၏ ဝန်ဆောင်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားလည်မှုမှားခြင်း သို့မဟုတ် အနားလည်မှုမှားခြင်းများအတွက် ကျွန်ုပ်တို့သည် တာဝန်ယူမည်မဟုတ်ပါ။