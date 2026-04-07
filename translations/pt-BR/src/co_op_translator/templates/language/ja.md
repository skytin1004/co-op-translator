# Localizeflow を使った CodeQL 戦略の翻訳ワークフロー

このドキュメントでは、Localizeflow での「CodeQL（コード品質とセキュリティのための GitHub の静的解析ツール）」拡張機能の詳細な翻訳ワークフローを説明しています。

## フォルダー構成

CodeQL 拡張機能のファイル配置は次のとおりです。

- `src/`
  - `localizeflow/`：Localizeflow によって翻訳されたファイルが生成されるフォルダー
  - `resources/localizeflow/`：Localizeflow が翻訳ソースを検出するためのフォルダー
  - 独自の翻訳用リソースファイルはここに置きます（例：`package.nls.json`）

- `src/package.nls.json`  
  VS Code での英語の文字列リソースの元ファイルです（翻訳元）

- `src/localizeflow/<language-code>/package.nls.json`  
  Localizeflow によって自動生成される翻訳ファイルです（翻訳出力）

## Localizeflow での翻訳ワークフロー

### 1. 英語のリソースファイルを編集

`src/package.nls.json` に英語の文字列リソースを追加・編集します。

### 2. Localizeflow の構成ファイル編集

`localizeflow.yml` に、翻訳対象のファイルや翻訳設定を記述します。

例：

```yaml
strategy:
  codeql:
    baseDir: "src"
    languages: ["ja", "fr", "de"]
    srcDir: "resources/localizeflow"
```

### 3. 翻訳の実行

CLI から Localizeflow の CodeQL 戦略を使って以下を実行します。

```bash
localizeflow exec codeql
```

- `src/resources/localizeflow` の翻訳対象ファイルをスキャン
- 翻訳結果の json を `src/localizeflow/<language-code>` に出力
- 翻訳を PR のブランチにコミットする

### 4. PR の作成とレビュー

- GitHub App が PR を作成し、翻訳者やレビュワーに通知されます。
- レビュー後、PR をマージします。

### 5. 翻訳の反映

マージ後、翻訳済みの `package.nls.json` が自動で `src/localizeflow` に生成されますので、ビルドで読み込みます。

## フォルダーの注意点

- 元の英語ファイルは `src/package.nls.json` にまとめて管理します。
- ローカライズ結果は `src/localizeflow/<言語コード>/package.nls.json` に配置し、ソース管理に含めます。
- `resources/localizeflow` は Localizeflow が翻訳対象を検出するためのワークエリアです。

## まとめ

Localizeflow の CodeQL 戦略は、GitHub 上で翻訳を自動化し、PR 単位でレビューできる強力なワークフローです。  
これにより、VS Code 拡張の多言語化が効率よく進められます。

詳しくは [Localizeflow](https://github.com/Azure/localizeflow) のドキュメントをご参照ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->