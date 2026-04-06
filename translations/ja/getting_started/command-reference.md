# コマンドリファレンス

**Co-op Translator** CLIは翻訳プロセスをカスタマイズするためのいくつかのオプションを提供します:

コマンド                                       | 説明
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | 指定した言語にプロジェクトを翻訳します。例: translate -l "es fr de" はスペイン語、フランス語、ドイツ語に翻訳します。translate -l "all" を使うとすべてのサポートされている言語に翻訳します。
translate -l "language_codes" -u              | 既存の翻訳を削除して再作成することで翻訳を更新します。警告: 指定した言語のすべての現在の翻訳が削除されます。
translate -l "language_codes" -img            | 画像ファイルのみを翻訳します。
translate -l "language_codes" -md             | Markdownファイルのみを翻訳します。
translate -l "language_codes" -nb             | Jupyterノートブックファイル(.ipynb)のみを翻訳します。
translate -l "language_codes" --fix           | 以前の評価結果に基づいて信頼度が低いファイルを再翻訳します。
translate -l "language_codes" -d              | 詳細なログを出力するデバッグモードを有効にします。
translate -l "language_codes" --save-logs, -s | DEBUGレベルのログを<root_dir>/logs/ 以下のファイルに保存します（コンソールの表示は -d で制御）。
translate -l "language_codes" -r "root_dir"   | プロジェクトのルートディレクトリを指定します。
translate -l "language_codes" -f              | 画像翻訳で高速モードを使用します（品質や整合性を若干犠牲にして最大3倍速いプロットが可能）。
translate -l "language_codes" -y              | すべてのプロンプトを自動的に確認します（CI/CDパイプラインで有用）。
translate -l "language_codes" --add-disclaimer/--no-disclaimer | 翻訳されたMarkdownやノートブックに機械翻訳免責事項セクションを追加するか無効にします（デフォルトは有効）。
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | READMEの言語セクションの案内をリポジトリのURLでパーソナライズします（スパースチェックアウト用）。
translate -l "language_codes" --help          | 利用可能なコマンドを表示するCLI内ヘルプ。
evaluate -l "language_code"                  | 指定言語の翻訳品質を評価し、信頼度スコアを提供します。
evaluate -l "language_code" -c 0.8           | カスタム信頼度閾値で翻訳を評価します。
evaluate -l "language_code" -f               | 高速評価モード（ルールベースのみ、LLMは使用しません）。
evaluate -l "language_code" -D               | 詳細評価モード（LLMベースのみ、より詳細ですが処理は遅くなります）。
evaluate -l "language_code" --save-logs, -s  | DEBUGレベルのログを<root_dir>/logs/に保存します。
migrate-links -l "language_codes"             | 翻訳済みMarkdownファイルのリンクをノートブック(.ipynb)へのリンクに再処理します。翻訳済みノートブックがある場合はそれを優先し、なければ原本にフォールバック可能。
migrate-links -l "language_codes" -r          | プロジェクトのルートディレクトリを指定（デフォルトはカレントディレクトリ）。
migrate-links -l "language_codes" --dry-run   | 変更があったファイルを表示するだけで、変更は書き込みません。
migrate-links -l "language_codes" --no-fallback-to-original | 翻訳済みノートブックが無い場合に原本へのリンクを書き換えない（翻訳済みノートブックがある場合のみ更新）。
migrate-links -l "language_codes" -d          | 詳細なログを出力するデバッグモードを有効にします。
migrate-links -l "language_codes" --save-logs, -s | DEBUGレベルのログを<root_dir>/logs/に保存。
migrate-links -l "all" -y                      | すべての言語で処理し、警告プロンプトを自動確認。

## 使用例

  1. デフォルト動作（既存翻訳を削除せず新規翻訳を追加）:   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. 韓国語の画像翻訳のみ新規追加（既存翻訳は削除しません）:    translate -l "ko" -img

  3. すべての韓国語翻訳を更新（警告: 既存の韓国語翻訳はすべて削除後、再翻訳）:    translate -l "ko" -u

  4. 韓国語画像のみ更新（警告: 既存の韓国語画像はすべて削除後、再翻訳）:    translate -l "ko" -img -u

  5. 他の翻訳に影響なく韓国語のMarkdown翻訳を新規追加:    translate -l "ko" -md

  6. 以前の評価結果に基づく低信頼度翻訳の修正: translate -l "ko" --fix

  7. 特定ファイルのみの低信頼度翻訳修正（Markdownのみ）: translate -l "ko" --fix -md

  8. 特定ファイルのみの低信頼度翻訳修正（画像のみ）: translate -l "ko" --fix -img

  9. 画像翻訳で高速モード使用:    translate -l "ko" -img -f

  10. カスタム閾値で低信頼度翻訳を修正: translate -l "ko" --fix -c 0.8

  11. デバッグモード例: - translate -l "ko" -d: デバッグログを有効化。
  12. ログをファイルに保存: translate -l "ko" -s
  13. コンソールとファイルの両方でDEBUGログ: translate -l "ko" -d -s
  14. 出力に機械翻訳免責事項を追加しない翻訳: translate -l "ko" --no-disclaimer

  15. 韓国語翻訳のノートブックリンクを移行（翻訳済みノートブックへのリンクを更新）:    migrate-links -l "ko"

  15. dry-run付きリンク移行（ファイルは書き込みません）:    migrate-links -l "ko" --dry-run

  16. 翻訳済みノートブックがある場合のみリンクを更新（原本にはフォールバックしない）:    migrate-links -l "ko" --no-fallback-to-original

  17. すべての言語を処理し確認プロンプトあり:    migrate-links -l "all"

  18. すべての言語を処理し自動確認:    migrate-links -l "all" -y
  19. migrate-linksのログをファイルに保存:    migrate-links -l "ko ja" -s

  20. READMEの言語案内部分をリポジトリURLでパーソナライズ:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### 評価例

> [!WARNING]  
> <strong>ベータ機能</strong>: 評価機能は現在ベータ版です。この機能は翻訳済みドキュメントの評価を目的としてリリースされており、評価手法および詳細な実装は開発中で、変更される可能性があります。

  1. 韓国語翻訳を評価: evaluate -l "ko"

  2. カスタム信頼度閾値で評価: evaluate -l "ko" -c 0.8

  3. 高速評価（ルールベースのみ）: evaluate -l "ko" -f

  4. 詳細評価（LLMベースのみ）: evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文のドキュメントが正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->