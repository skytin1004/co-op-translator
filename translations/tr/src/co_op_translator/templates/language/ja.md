# フローの中で翻訳

[Localizeflow](https://localizeflow.com) は、翻訳者が自分の好きな開発者ワークフローの中で翻訳を行えるようにします。ローカライズプラットフォームとして、コードサイドの作業者と翻訳者の間のコミュニケーションギャップや複雑さを取り除き、両者のために開発体験をシンプルにすることを目指しています。

## コミット、PR、プルリクエストの中で翻訳

多くの会社では、翻訳はフローの中の単純な作業ではありません。他のチームメンバーのレビュー付きでプルリクエストでレビューされてマージされるコードの追加や修正に対し、翻訳作業もジレンマの中にあります。翻訳者がレビューされていない翻訳をどこか別の場所にコミットすることは決して適していません。レビューの枠組みの中で翻訳が行われ、実際のコードと一緒にバージョン管理されるべきです。もちろん、この問題は翻訳者がテキストファイルを直接編集できる場合に最も簡単に解決します。ただし、ほとんどの場合翻訳者はGitHubについての知識が限られています。梱包と運用の簡単さのために、翻訳はUIにルール化されていなければなりません。

Localizeflow は、開発者や翻訳者のためのGitHub Appで、この問題を解決し、簡単にローカライズ作業をプルリクエストの中に統合します。

## 翻訳のためのCo-op Translator

Localizeflowは [Co-op Translator](https://github.com/Azure/co-op-translator) を使って翻訳を行っています。このツールはプルリクエストの中で翻訳者を会わせ、UIを通じて簡単に翻訳を管理できます。翻訳者はGitHubのIssue、プルリクエストのコメント、または独自UIで直接翻訳できます。

翻訳作業が完了した後は、レビューとマージはいつものコードのものと同じプロセスで行われます。コードも翻訳も同じエコシステムの中にあり、違和感なく両者を操作できます。

この仕組みは、翻訳の質を向上させ、処理の透明性と追跡可能性を確保し、開発チーム全体の信頼を高めます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragat**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımıyla ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->