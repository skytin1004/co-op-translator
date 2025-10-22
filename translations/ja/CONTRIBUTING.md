<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:33:34+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ja"
}
-->
# Co-op Translator への貢献

このプロジェクトでは、貢献や提案を歓迎しています。ほとんどの貢献には、Contributor License Agreement (CLA) への同意が必要です。これは、あなたが貢献する権利を持ち、実際にその権利を私たちに付与することを宣言するものです。詳細は https://cla.opensource.microsoft.com をご覧ください。

プルリクエストを提出すると、CLA ボットが自動的に CLA の提出が必要かどうかを判定し、PR にステータスチェックやコメントなどで案内します。ボットの指示に従ってください。CLA の提出は、同じ CLA を使うすべてのリポジトリで一度だけ行えば大丈夫です。

## 開発環境のセットアップ

このプロジェクトの開発環境をセットアップするには、依存関係管理に Poetry の利用を推奨しています。プロジェクトの依存関係は `pyproject.toml` で管理しているため、依存パッケージのインストールには Poetry を使ってください。

### 仮想環境の作成

#### pip を使う場合

```bash
python -m venv .venv
```

#### Poetry を使う場合

```bash
poetry init
```

### 仮想環境の有効化

#### pip・Poetry 共通

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Poetry を使う場合

```bash
poetry shell
```

### パッケージと必要なパッケージのインストール

#### Poetry（pyproject.toml から）

```bash
poetry install
```

### 手動テスト

PR を提出する前に、実際のドキュメントで翻訳機能をテストすることが重要です。

1. ルートディレクトリにテスト用ディレクトリを作成します:
    ```bash
    mkdir test_docs
    ```

2. 翻訳したい Markdown ドキュメントや画像をテストディレクトリにコピーします。例:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. パッケージをローカルにインストールします:
    ```bash
    pip install -e .
    ```

4. テストドキュメントで Co-op Translator を実行します:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. `test_docs/translations` と `test_docs/translated_images` の翻訳ファイルを確認し、以下をチェックします:
   - 翻訳品質
   - メタデータコメントが正しいか
   - 元の Markdown 構造が維持されているか
   - リンクや画像が正しく動作しているか

この手動テストにより、あなたの変更が実際の利用シーンで問題なく動作することを確認できます。

### 環境変数

1. ルートディレクトリに `.env.template` ファイルをコピーして `.env` ファイルを作成します。
1. 指示に従って環境変数を設定してください。

> [!TIP]
>
> ### 開発環境の追加オプション
>
> プロジェクトをローカルで実行する以外にも、GitHub Codespaces や VS Code Dev Containers を使って開発環境を構築できます。
>
> #### GitHub Codespaces
>
> GitHub Codespaces を使えば、追加の設定なしでサンプルを仮想的に実行できます。
>
> このボタンをクリックすると、ブラウザ上で VS Code が開きます:
>
> 1. テンプレートを開く（数分かかる場合があります）:
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### VS Code Dev Containers を使ってローカルで実行
>
> ⚠️ このオプションは、Docker Desktop に最低 16 GB の RAM が割り当てられている場合のみ動作します。16 GB 未満の場合は [GitHub Codespaces オプション](../..) や [ローカルセットアップ](../..) をご利用ください。
>
> 関連オプションとして VS Code Dev Containers があります。これは [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) を使ってローカルの VS Code でプロジェクトを開きます:
>
> 1. Docker Desktop を起動（未インストールの場合はインストール）
> 2. プロジェクトを開く:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### コードスタイル

プロジェクト全体のコードスタイルを統一するため、Python コードフォーマッター [Black](https://github.com/psf/black) を使用しています。Black は妥協のないコードフォーマッターで、Python コードを自動的に Black のスタイルに整形します。

#### 設定

Black の設定は `pyproject.toml` に記載されています:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Black のインストール

Poetry（推奨）または pip で Black をインストールできます。

##### Poetry を使う場合

開発環境セットアップ時に Black も自動的にインストールされます:
```bash
poetry install
```

##### pip を使う場合

pip を使う場合は、Black を直接インストールできます:
```bash
pip install black
```

#### Black の使い方

##### Poetry で

1. プロジェクト内のすべての Python ファイルを整形:
    ```bash
    poetry run black .
    ```

2. 特定のファイルやディレクトリを整形:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### pip で

1. プロジェクト内のすべての Python ファイルを整形:
    ```bash
    black .
    ```

2. 特定のファイルやディレクトリを整形:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> エディターの保存時に自動で Black で整形する設定をおすすめします。多くのエディターで拡張機能やプラグインで対応しています。

## Co-op Translator の実行

Poetry を使って Co-op Translator を実行するには、以下の手順に従ってください。

1. 翻訳テストを行いたいディレクトリに移動するか、テスト用の一時フォルダーを作成します。

2. 以下のコマンドを実行します。`-l ko` の部分は翻訳したい言語コードに置き換えてください。`-d` フラグはデバッグモードです。

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> コマンド実行前に Poetry 環境（poetry shell）が有効になっていることを確認してください。

## 新しい言語の追加

新しい言語のサポート追加も歓迎しています。PR を作成する前に、以下の手順を完了してください。

1. フォントマッピングへの言語追加
   - `src/co_op_translator/fonts/font_language_mappings.yml` を編集
   - 以下の項目でエントリを追加:
     - `code`: ISO 風の言語コード（例: `vi`）
     - `name`: 人が見て分かりやすい表示名
     - `font`: その言語の文字体系をサポートする `src/co_op_translator/fonts/` 配下のフォント
     - `rtl`: 右から左書きの場合は `true`、それ以外は `false`

2. 必要なフォントファイルの追加（必要な場合）
   - 新しいフォントが必要な場合は、オープンソース配布に適したライセンスか確認
   - フォントファイルを `src/co_op_translator/fonts/` に追加

3. ローカル検証
   - サンプル（Markdown、画像、ノートブックなど）で翻訳を実行
   - フォントや RTL レイアウトも含めて、出力が正しく表示されるか確認

4. ドキュメントの更新
   - `getting_started/supported-languages.md` に言語が記載されていることを確認
   - `README_languages_template.md` の変更は不要です。これはサポートリストから自動生成されます

5. PR の作成
   - 追加した言語やフォント・ライセンスの注意点を説明
   - 可能ならレンダリング結果のスクリーンショットを添付

YAML の例:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### 新しい言語のテスト

以下のコマンドで新しい言語をテストできます:

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

## メンテナー向け

### コミットメッセージとマージ戦略

プロジェクトのコミット履歴の一貫性と明確さを保つため、**Squash and Merge** 戦略を使う際の**最終コミットメッセージ**には特定のフォーマットを採用しています。

プルリクエスト（PR）がマージされると、個々のコミットは一つにまとめられます。最終コミットメッセージは、以下のフォーマットに従ってください。

#### コミットメッセージのフォーマット（Squash and Merge 用）

コミットメッセージは以下の形式です:

```bash
<type>: <description> (#<PR number>)
```

- **type**: コミットのカテゴリを指定します。以下のタイプを使います:
  - `Docs`: ドキュメントの更新
  - `Build`: ビルドシステムや依存関係の変更（設定ファイル、CI ワークフロー、Dockerfile なども含む）
  - `Core`: プロジェクトのコア機能や特徴の変更（特に `src/co_op_translator/core` ディレクトリのファイル）

- **description**: 変更内容の簡潔な要約
- **PR number**: コミットに関連するプルリクエスト番号

**例**:

- `Docs: インストール手順を分かりやすく更新 (#50)`
- `Core: 画像翻訳の処理を改善 (#60)`

> [!NOTE]
> 現在、**`Docs`**、**`Core`**、**`Build`** のプレフィックスは、変更されたソースコードにラベルが付与されることで PR タイトルに自動的に追加されます。正しいラベルが付いていれば、通常は PR タイトルを手動で修正する必要はありません。内容が正しいか、プレフィックスが適切に生成されているかだけ確認してください。

#### マージ戦略

プルリクエストのデフォルト戦略は **Squash and Merge** です。この戦略により、個々のコミット内容に関わらず、コミットメッセージがフォーマットに従うことが保証されます。

**理由**:

- プロジェクト履歴がシンプルで直線的になる
- コミットメッセージの一貫性
- 細かなコミット（例: "fix typo"）によるノイズの削減

マージ時は、最終コミットメッセージが上記フォーマットに従っていることを確認してください。

**Squash and Merge の例**
PR に以下のコミットが含まれている場合:

- `fix typo`
- `update README`
- `adjust formatting`

これらはまとめて次のようにします:
`Docs: ドキュメントの明確化とフォーマット調整 (#65)`

---

**免責事項**：
本書類は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な表現が含まれる場合がありますのでご注意ください。原文（元の言語の文書）が正式な情報源となります。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤認についても、当方は責任を負いかねます。