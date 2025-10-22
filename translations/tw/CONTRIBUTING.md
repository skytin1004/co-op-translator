<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:30:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "tw"
}
-->
# 貢獻 Co-op Translator

歡迎大家對本專案提出貢獻與建議。大多數的貢獻都需要你同意一份貢獻者授權協議（CLA），聲明你有權利並實際授予我們使用你貢獻內容的權利。詳情請參閱 https://cla.opensource.microsoft.com。

當你提交 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA，並在 PR 上標註（例如狀態檢查、留言）。只需按照機器人的指示操作即可。你只需在所有使用我們 CLA 的倉庫中做一次這個動作。

## 開發環境設置

建議使用 Poetry 來管理本專案的依賴。我們使用 `pyproject.toml` 來管理專案依賴，因此安裝依賴時應使用 Poetry。

### 建立虛擬環境

#### 使用 pip

```bash
python -m venv .venv
```

#### 使用 Poetry

```bash
poetry init
```

### 啟用虛擬環境

#### pip 與 Poetry 通用

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### 使用 Poetry

```bash
poetry shell
```

### 安裝套件及所需依賴

#### 使用 Poetry（從 pyproject.toml）

```bash
poetry install
```

### 手動測試

在提交 PR 前，請務必用實際文件測試翻譯功能：

1. 在專案根目錄建立一個測試資料夾：
    ```bash
    mkdir test_docs
    ```

2. 將你想翻譯的 markdown 文件和圖片複製到測試資料夾。例如：
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. 在本地安裝套件：
    ```bash
    pip install -e .
    ```

4. 在你的測試文件上執行 Co-op Translator：
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. 檢查 `test_docs/translations` 和 `test_docs/translated_images` 內的翻譯檔案，確認：
   - 翻譯品質
   - 中繼資料註解正確
   - 原始 markdown 結構有保留
   - 連結與圖片運作正常

這樣的手動測試有助於確保你的修改在實際情境下能正常運作。

### 環境變數

1. 在根目錄複製 `.env.template` 檔案，建立 `.env` 檔。
1. 依指示填寫環境變數。

> [!TIP]
>
> ### 其他開發環境選項
>
> 除了在本地執行專案外，你也可以使用 GitHub Codespaces 或 VS Code Dev Containers 來設置開發環境。
>
> #### GitHub Codespaces
>
> 你可以直接在 GitHub Codespaces 上虛擬執行本範例，無需額外設定。
>
> 點擊按鈕會在瀏覽器中開啟網頁版 VS Code：
>
> 1. 開啟範本（可能需要幾分鐘）：
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### 使用 VS Code Dev Containers 在本地執行
>
> ⚠️ 此選項僅適用於你的 Docker Desktop 至少分配了 16 GB RAM。如果你的 RAM 少於 16 GB，可以考慮 [GitHub Codespaces 選項](../..) 或 [本地設置](../..)。
>
> 另一個相關選項是 VS Code Dev Containers，會利用 [Dev Containers 擴充套件](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 開啟專案：
>
> 1. 啟動 Docker Desktop（如未安裝請先安裝）
> 2. 開啟專案：
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### 程式碼風格

我們使用 [Black](https://github.com/psf/black) 作為 Python 程式碼格式化工具，以維持專案內一致的程式碼風格。Black 是一個嚴格的格式化工具，會自動將 Python 程式碼重整為 Black 樣式。

#### 設定

Black 的設定寫在 `pyproject.toml`：

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### 安裝 Black

你可以用 Poetry（推薦）或 pip 安裝 Black：

##### 使用 Poetry

設置開發環境時會自動安裝 Black：
```bash
poetry install
```

##### 使用 pip

如果你用 pip，可以直接安裝 Black：
```bash
pip install black
```

#### 使用 Black

##### 使用 Poetry

1. 格式化專案內所有 Python 檔案：
    ```bash
    poetry run black .
    ```

2. 格式化特定檔案或資料夾：
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### 使用 pip

1. 格式化專案內所有 Python 檔案：
    ```bash
    black .
    ```

2. 格式化特定檔案或資料夾：
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> 建議你將編輯器設為儲存時自動用 Black 格式化程式碼。大多數現代編輯器都支援這個功能（可透過擴充套件或外掛）。

## 執行 Co-op Translator

若要在你的環境中用 Poetry 執行 Co-op Translator，請依下列步驟操作：

1. 進入你想進行翻譯測試的目錄，或建立一個暫時用來測試的資料夾。

2. 執行下列指令。將 `-l ko` 換成你想翻譯成的語言代碼。`-d` 參數代表除錯模式。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> 請確保已啟用 Poetry 環境（poetry shell）再執行指令。

## 貢獻新語言

我們歡迎你為本專案新增語言支援。在開 PR 前，請完成下列步驟，以便順利審查。

1. 新增語言到字型對應表
   - 編輯 `src/co_op_translator/fonts/font_language_mappings.yml`
   - 新增一筆資料，內容包含：
     - `code`：類似 ISO 的語言代碼（如 `vi`）
     - `name`：易讀的顯示名稱
     - `font`：`src/co_op_translator/fonts/` 內支援該語系的字型
     - `rtl`：若為由右至左語言填 `true`，否則填 `false`

2. 加入所需字型檔（如有需要）
   - 若需新字型，請確認其授權可用於開源發佈
   - 將字型檔加入 `src/co_op_translator/fonts/`

3. 本地驗證
   - 針對小範例（Markdown、圖片、notebook 視情況）執行翻譯
   - 確認輸出能正確顯示，包括字型與 RTL 版面（如適用）

4. 更新文件
   - 確認語言已出現在 `getting_started/supported-languages.md`
   - `README_languages_template.md` 無需修改，會自動從支援清單產生

5. 開 PR
   - 說明新增的語言及任何字型/授權考量
   - 如有可能，附上渲染結果的截圖

YAML 範例：

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 測試新語言

你可以用下列指令測試新語言：

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

## 維護者

### Commit 訊息與合併策略

為了讓專案的 commit 歷史保持一致且清晰，我們在使用 **Squash and Merge** 策略時，對**最終 commit 訊息**有特定格式要求。

當 pull request（PR）被合併時，所有 commit 會被壓縮成一個。最終 commit 訊息應遵循下列格式，以維持乾淨且一致的歷史紀錄。

#### Commit 訊息格式（squash and merge 適用）

我們的 commit 訊息格式如下：

```bash
<type>: <description> (#<PR number>)
```

- **type**：指定 commit 類型。我們使用以下類型：
  - `Docs`：文件更新。
  - `Build`：與建置系統或依賴相關的變更，包括設定檔、CI 工作流程或 Dockerfile 的更新。
  - `Core`：專案核心功能或特性的修改，特別是 `src/co_op_translator/core` 目錄下的檔案。

- **description**：簡要說明變更內容。
- **PR number**：與此 commit 相關的 pull request 編號。

**範例**：

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> 目前，**`Docs`**、**`Core`** 和 **`Build`** 前綴會根據標籤自動加到 PR 標題。只要標籤正確，通常不需手動修改 PR 標題。你只需確認一切正確，前綴已正確產生即可。

#### 合併策略

我們預設使用 **Squash and Merge** 作為 pull request 的合併策略。這能確保 commit 訊息符合我們的格式，即使每個 commit 本身沒有。

**原因**：

- 專案歷史乾淨、線性。
- commit 訊息一致。
- 減少瑣碎 commit（如「fix typo」）造成的雜訊。

合併時，請確保最終 commit 訊息符合上述格式。

**Squash and Merge 範例**
如果一個 PR 包含以下 commit：

- `fix typo`
- `update README`
- `adjust formatting`

合併後應壓縮成：
`Docs: Improve documentation clarity and formatting (#65)`

---

**免責聲明**：
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應視為具權威性的來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而產生的任何誤解或誤釋，我們概不負責。