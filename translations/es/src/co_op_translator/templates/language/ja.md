---
title: "セキュリティで保護されたヘッダー"
description: "HTTP応答に含めることで、ブラウザでのクライアント側セキュリティが高まるヘッダーを設定する方法について学びます。"
ms.assetid: de4e952f-3376-4fc1-ae10-25e005877a62
ms.technology: azure-app-service
ms.topic: article
ms.tgt_pltp: Azure
ms.workload: Web Applications
ms.date: 2020-07-06
---

# セキュリティで保護されたヘッダー

クライアント側のセキュリティを強化するために、HTTP応答に特定のセキュリティ関連ヘッダーを追加することが推奨されています。これらのヘッダーは、ブラウザに追加のセキュリティ指示を提供します。この記事では、Azure App Service でこれらのヘッダーを設定する方法について説明します。

## よく使用されるセキュリティ ヘッダーの一覧

代表的なセキュリティ ヘッダーとその効果は以下のとおりです。

| ヘッダー名                         | 説明                                                        |
|-----------------------------------|-------------------------------------------------------------|
| `X-Content-Type-Options: nosniff` | ブラウザによる MIME タイプの推測を防止し、不正なリソースの誤った解釈を防止します。 |
| `X-Frame-Options: DENY`            | クリックジャッキングを防ぐために、ページの iframe 埋め込みを禁止します。       |
| `Strict-Transport-Security: max-age=...` | HTTPS への接続を強制するために、ブラウザに HTTPS のみを使用させる指示を出します。 |
| `Content-Security-Policy`          | クロスサイトスクリプティング (XSS) やその他の攻撃を緩和するために、許可されたリソースを規制します。 |
| `Referrer-Policy`                  | リファラー送信のポリシーを制御し、プライバシーとセキュリティを強化します。     |

## Azure App Service での設定方法

### 1. Azure Portal でのアプリケーション設定

1. Azure Portal にサインインし、対象の App Service を開きます。
2. 「設定」セクションから「構成」を選択します。
3. 「HTTP ヘッダー」セクション（またはカスタムヘッダー設定可能な場所）で、必要なセキュリティヘッダーを追加します。
4. 変更を保存し、アプリを再起動します。

### 2. web.config を使用する (Windows ベースのアプリ)

`web.config` ファイルに以下のような `<httpProtocol>` エレメントを追加します。

```xml
<system.webServer>
  <httpProtocol>
    <customHeaders>
      <add name="X-Content-Type-Options" value="nosniff" />
      <add name="X-Frame-Options" value="DENY" />
      <add name="Strict-Transport-Security" value="max-age=31536000; includeSubDomains" />
    </customHeaders>
  </httpProtocol>
</system.webServer>
```

### 3. Start-up スクリプトやアプリコードでの設定

アプリケーションコード内でヘッダーを直接追加することも可能です。たとえば、.NET Core ではミドルウェアを利用してセキュリティヘッダーを設定できます。

## 注意点

- `Strict-Transport-Security` を使用する場合、必ず HTTPS が有効であることを確認してください。
- Content-Security-Policy ヘッダーは適切に設定しないと、正常なページ表示に支障をきたす可能性があります。設定は慎重に行ってください。
- これらのヘッダーは、クライアント側でのセキュリティ向上に役立ちますが、サーバー側のセキュリティ対策と併用することが重要です。

詳細については、[OWASP Secure Headers Project](https://owasp.org/www-project-secure-headers/) をご参照ください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->