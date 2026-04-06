# 対応言語

以下の表は、現在 **Co-op Translator** が対応している言語を示しています。言語コード、言語名、および各言語に関する既知の問題が含まれています。新しい言語のサポートを追加したい場合は、`src/co_op_translator/fonts/` にある `font_language_mappings.yml` ファイルに該当する言語コード、言語名、適切なフォントを追加し、テスト後にpull requestを送信してください。

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | 英語                 | NotoSans-Medium.ttf               | No          | No           |
| fr            | フランス語           | NotoSans-Medium.ttf               | No          | No           |
| es            | スペイン語           | NotoSans-Medium.ttf               | No          | No           |
| de            | ドイツ語             | NotoSans-Medium.ttf               | No          | No           |
| ru            | ロシア語             | NotoSans-Medium.ttf               | No          | No           |
| ar            | アラビア語           | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | ペルシャ語 (ファルシ) | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | ウルドゥー語         | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh-CN         | 中国語（簡体字）     | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-MO         | 中国語（繁体字、マカオ） | NotoSansCJK-Medium.ttc         | No          | No           |
| zh-HK         | 中国語（繁体字、香港） | NotoSansCJK-Medium.ttc           | No          | No           |
| zh-TW         | 中国語（繁体字、台湾） | NotoSansCJK-Medium.ttc           | No          | No           |
| ja            | 日本語               | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | 韓国語               | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | ヒンディー語         | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | ベンガル語           | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | マラーティー語       | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | ネパール語           | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | パンジャブ語（グルムキー）| NotoSansGurmukhi-Medium.ttf    | No          | No           |
| pt-PT         | ポルトガル語（ポルトガル）| NotoSans-Medium.ttf            | No          | No           |
| pt-BR         | ポルトガル語（ブラジル）| NotoSans-Medium.ttf              | No          | No           |
| it            | イタリア語           | NotoSans-Medium.ttf               | No          | No           |
| lt            | リトアニア語         | NotoSans-Medium.ttf               | No          | No           |
| pl            | ポーランド語         | NotoSans-Medium.ttf               | No          | No           |
| tr            | トルコ語             | NotoSans-Medium.ttf               | No          | No           |
| el            | ギリシャ語           | NotoSans-Medium.ttf               | No          | No           |
| th            | タイ語               | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | スウェーデン語       | NotoSans-Medium.ttf               | No          | No           |
| da            | デンマーク語         | NotoSans-Medium.ttf               | No          | No           |
| no            | ノルウェー語         | NotoSans-Medium.ttf               | No          | No           |
| fi            | フィンランド語       | NotoSans-Medium.ttf               | No          | No           |
| nl            | オランダ語           | NotoSans-Medium.ttf               | No          | No           |
| he            | ヘブライ語           | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | ベトナム語           | NotoSans-Medium.ttf               | No          | No           |
| id            | インドネシア語       | NotoSans-Medium.ttf               | No          | No           |
| ms            | マレー語             | NotoSans-Medium.ttf               | No          | No           |
| tl            | タガログ語（フィリピン語）| NotoSans-Medium.ttf           | No          | No           |
| sw            | スワヒリ語           | NotoSans-Medium.ttf               | No          | No           |
| hu            | ハンガリー語         | NotoSans-Medium.ttf               | No          | No           |
| cs            | チェコ語             | NotoSans-Medium.ttf               | No          | No           |
| sk            | スロバキア語         | NotoSans-Medium.ttf               | No          | No           |
| ro            | ルーマニア語         | NotoSans-Medium.ttf               | No          | No           |
| bg            | ブルガリア語         | NotoSans-Medium.ttf               | No          | No           |
| sr            | セルビア語（キリル） | NotoSans-Medium.ttf               | No          | No           |
| hr            | クロアチア語         | NotoSans-Medium.ttf               | No          | No           |
| sl            | スロベニア語         | NotoSans-Medium.ttf               | No          | No           |
| uk            | ウクライナ語         | NotoSans-Medium.ttf               | No          | No           |
| my            | ビルマ語（ミャンマー）| NotoSansMyanmar-Medium.ttf       | No          | No           |
| ta            | タミル語             | NotoSansTamil-Medium.ttf          | No          | No           |
| et            | エストニア語         | NotoSans-Medium.ttf               | No          | No           |
| pcm           | ナイジェリア・ピジン語| NotoSans-Medium.ttf               | No          | No           |
| te            | テルグ語             | NotoSans-Medium.ttf               | No          | No           |
| ml            | マラヤーラム語       | NotoSans-Medium.ttf               | No          | No           |
| kn            | カンナダ語           | NotoSans-Medium.ttf               | No          | No           |
| km            | クメール語           | NotoSansKhmer-Medium.ttf          | No          | No           |

## 新しい言語の追加

新しい言語の追加に興味がありますか？以下の貢献ガイドをご参照ください：

- 貢献方法： [新しい言語を追加する](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご留意ください。原文の母国語版が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じたいかなる誤解や誤訳についても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->