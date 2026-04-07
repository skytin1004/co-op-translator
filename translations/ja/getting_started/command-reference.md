# コマンドリファレンス

**Co-op Translator** CLI は翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します：

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 指定した言語にプロジェクトを翻訳します。例：translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" を使うとサポートされているすべての言語に翻訳します。
translate -l "language_codes" -u              | 翻訳を更新するために既存の翻訳を削除して再作成します。警告：指定した言語の現在のすべての翻訳が削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdownファイルのみを翻訳します。
translate -l "language_codes" -nb             | Jupyterノートブックファイル（.ipynb）のみを翻訳します。
translate -l "language_codes" --fix           | 前回の評価結果に基づき、信頼度の低い翻訳を再翻訳します。
translate -l "language_codes" -d              | 詳細ログ出力のためデバッグモードを有効にします。
translate -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ 以下のファイルに保存します（コンソールの出力は -d によって制御されます）
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します
translate -l "language_codes" -f              | 画像翻訳に高速モードを使用します（品質や整列の若干の低下を伴い、最大3倍高速化します）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に承認します（CI/CDパイプラインに便利です）
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 翻訳済みのMarkdownやノートブックに機械翻訳に関する免責事項のセクションを追加するかどうかを有効／無効にします（デフォルトは有効）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | READMEの言語セクションのアドバイザリ（スパースチェックアウト）をリポジトリURLでカスタマイズします。
translate -l "language_codes" --help          | CLI内の詳細なヘルプ情報を表示します
evaluate -l "language_code"                  | 特定言語の翻訳品質を評価し、信頼度スコアを提供します
evaluate -l "language_code" -c 0.8           | カスタムの信頼度閾値で翻訳を評価します
evaluate -l "language_code" -f               | 高速評価モード（ルールベースのみ、LLMは使用しません）
evaluate -l "language_code" -D               | 深層評価モード（LLMベースのみ、より詳細ですが時間がかかります）
evaluate -l "language_code" --save-logs, -s  | DEBUGレベルのログを <root_dir>/logs/ 以下のファイルに保存します
migrate-links -l "language_codes"             | 翻訳済みMarkdownファイルを再処理し、ノートブック(.ipynb)へのリンクを更新します。翻訳済みノートブックがあればそれを優先し、なければ元のノートブックにフォールバックします。
migrate-links -l "language_codes" -r          | プロジェクトのルートディレクトリを指定します（デフォルトは現在のディレクトリ）。
migrate-links -l "language_codes" --dry-run   | 変更されるファイルを表示しますが、変更は書き込みません。
migrate-links -l "language_codes" --no-fallback-to-original | 翻訳済みノートブックがない場合、元のノートブックへのリンクを書き換えない（翻訳済みのみリンクを更新）。
migrate-links -l "language_codes" -d          | 詳細ログ出力のためデバッグモードを有効にします。
migrate-links -l "language_codes" --save-logs, -s | DEBUGレベルのログを <root_dir>/logs/ 以下のファイルに保存します
migrate-links -l "all" -y                      | すべての言語を処理し、警告プロンプトを自動承認します。

## 使用例

  1. デフォルト動作（既存の翻訳を削除せずに新規翻訳を追加）：   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 韓国語の画像翻訳のみ追加（既存翻訳は削除されません）：    translate -l "ko" -img

  3. すべての韓国語翻訳を更新（警告：既存のすべての韓国語翻訳が削除されてから再翻訳されます）：    translate -l "ko" -u

  4. 韓国語画像のみ更新（警告：既存の韓国語画像はすべて削除されてから再翻訳されます）：    translate -l "ko" -img -u

  5. 他の翻訳に影響を与えずに韓国語Markdown翻訳を新規追加：    translate -l "ko" -md

  6. 前回の評価結果に基づき信頼度の低い翻訳を修正： translate -l "ko" --fix

  7. 特定ファイルのみ信頼度の低いMarkdown翻訳を修正： translate -l "ko" --fix -md

  8. 特定ファイルのみ信頼度の低い画像翻訳を修正： translate -l "ko" --fix -img

  9. 画像翻訳に高速モードを使用：    translate -l "ko" -img -f

  10. カスタム閾値で信頼度の低い翻訳を修正： translate -l "ko" --fix -c 0.8

  11. デバッグモード例： - translate -l "ko" -d：デバッグログを有効化。
  12. ログをファイルに保存： translate -l "ko" -s
  13. コンソールDEBUGとファイルDEBUG両方： translate -l "ko" -d -s
  14. 機械翻訳の免責事項を出力に追加しないで翻訳： translate -l "ko" --no-disclaimer

  15. 韓国語翻訳のノートブックリンクを移行（翻訳ノートブックへのリンクを更新）：    migrate-links -l "ko"

  15. dry-runでリンク移行（ファイルは書き換えない）：    migrate-links -l "ko" --dry-run

  16. 翻訳済みノートブックがある場合のみリンクを更新（元のノートブックへのフォールバックはしない）：    migrate-links -l "ko" --no-fallback-to-original

  17. 確認プロンプト付きですべての言語を処理：    migrate-links -l "all"

  18. すべての言語を処理し、警告プロンプトを自動承認：    migrate-links -l "all" -y
  19. migrate-links のログをファイルに保存：    migrate-links -l "ko ja" -s

  20. READMEの言語アドバイザリをリポジトリURLでカスタマイズ：
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 評価の例

> [!WARNING]  
> <strong>ベータ機能</strong>：評価機能は現在ベータ版です。この機能は翻訳済みドキュメントを評価するためにリリースされており、評価手法や詳細実装は開発中であり変更される可能性があります。

  1. 韓国語翻訳を評価： evaluate -l "ko"

  2. カスタム信頼度閾値で評価： evaluate -l "ko" -c 0.8

  3. 高速評価（ルールベースのみ）： evaluate -l "ko" -f

  4. 深層評価（LLMベースのみ）： evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類はAI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文はその言語における正式な資料として扱われるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用による誤解や誤訳に対して、一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->