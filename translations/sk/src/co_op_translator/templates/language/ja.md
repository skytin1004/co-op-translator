# カスタムのAnalyzerの使用

テーブルを作成および更新する際、`mappings`に、Fieldのデータタイプのほかに、Analyzerを設定できます。このサンプルは、`name_ja`というフィールドがカスタムの［kuromoji］Analyzerを利用している例です。

```json
"mappings" : {
  "properties" : {
    "name_ja": {
      "type": "text",
      "analyzer": "kuromoji_analyzer"
    }
  }
}
```

このように設定しておくと、`name_ja`への検索は、`kuromoji_analyzer`を利用した全文検索になります。

# 独自Analyzerの作成

Defaultのkuromojiに加え、形態素解析の設定をカスタマイズしたい場合、独自Analyzerを作成します。

1. `analysis`設定を`settings`に指定します。
2. ここで、カスタムTokenizer、Filter、Analyzerを指定します。
3. Analyzerには、TokenizerとFilterの設定を与えます。

例:

```json
"settings": {
  "analysis": {
    "filter": {
      "kuromoji_baseform": {
        "type": "kuromoji_baseform"
      },
      "my_stopwords": {
        "type": "stop",
        "stopwords": ["の", "こと"]
      }
    },
    "analyzer": {
      "my_kuromoji_analyzer": {
        "type": "custom",
        "tokenizer": "kuromoji_tokenizer",
        "filter": [
          "kuromoji_baseform",
          "my_stopwords"
        ]
      }
    }
  }
}
```

# Analyzerの適用例

インデックス作成時に、このAnalyzerを利用してマッピングを設定します。

```json
PUT /my_index
{
  "settings": { ... },
  "mappings": {
    "properties": {
      "content": {
        "type": "text",
        "analyzer": "my_kuromoji_analyzer"
      }
    }
  }
}
```

# Analyzerが利用される場面

- 文書のインデックス作成
- クエリ解析時（デフォルトのAnalyzer指定なしの場合、フィールドのAnalyzerが使われる）

# 注意点

- Analyzerは検索時にも一致した形態素解析を行うため、マッピングのAnalyzer設定とクエリで使うAnalyzerを揃えることが望ましいです。
- カスタムAnalyzerを使用した場合には、使用したAnalyzerの定義をインデックス作成時に必ず含めておく必要があります。

以上、ElasticSearchにおけるカスタムAnalyzerの使い方の概要でした。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vzniknuté použitím tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->