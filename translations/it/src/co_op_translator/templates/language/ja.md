---
title: ファイル システムの永続性について
description: Node.js のファイル システムでの永続性を検証します。
---

# ファイル システムの永続性について

このドキュメントでは、Node.js のファイル システムの変更がプロセス間でどのように永続するかを確認します。

## テスト

```bash
node fs.mjs && node fs.mjs
```

`fs.mjs` の内容は以下のとおりです:

```js
import fs from "fs";

if (!fs.existsSync("test.txt")) {
  fs.writeFileSync("test.txt", "hello");
}

const content = fs.readFileSync("test.txt", "utf8");
console.log(`file content: ${content}`);

fs.writeFileSync("test.txt", "world");
```

### 結果

初回の実行では `test.txt` が存在しないため、ファイルが作成され `hello` が書き込まれます。2回目の実行時には、`test.txt` が存在しその内容が表示され、その後 `world` に書き換えられます。

このことから、Node.js のファイル システムの変更は持続されていることがわかります。

[!IMPORTANT]
ファイル システムの永続性は、デプロイ環境の設定やボリュームのマウント状況によって異なる場合があります。このテストは一般的なローカル環境を想定しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di essere consapevoli che le traduzioni automatiche potrebbero contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->