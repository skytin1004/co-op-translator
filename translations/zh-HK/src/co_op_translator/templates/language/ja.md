# Localizeflow での Pull Request トリガー方法の選択

Localizeflow でソース管理と翻訳を統合する際には、翻訳ファイルの `pull request (PR)` をどのようにトリガーするか選択する必要があります。以下のオプションから選択できます。

## オプション

- **git commit による自動トリガー**  
  - Localizeflow は、ローカルマシンの `commit` 発生時に翻訳 PR を自動で作成・更新できます。  
  - これはスピードを重視する場合に便利です。

- <strong>手動トリガー</strong>  
  - すべての翻訳 PR は、GitHub の Web インターフェースからまたは GitHub Actions / API によりトリガーされます。  
  - プルリクエスト毎の正確な操作を制御したい場合に向いています。

- **CI/CD パイプライン統合**  
  - ビルドやデプロイのジョブに翻訳 PR 発行を組み込み、より厳格なワークフローを構築可能です。

## 推奨される使い方

大規模なチームや複雑なリリースサイクルの場合、<strong>手動トリガー</strong>または<strong>CI/CD 統合</strong>が安定性と管理を高めます。小規模で素早い変更を多用する場合は、<strong>commit によるトリガー</strong>が効率的です。

詳細は Localizeflow の公式ドキュメントを参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件經由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本才應被視為具權威性的資料來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->