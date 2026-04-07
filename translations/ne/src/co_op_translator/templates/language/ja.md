---
title: "Azure Static Web Apps でユーザーが定義した関数ランタイムを使用する"
description: "Azure Static Web Apps ではユーザー定義の関数ランタイムを使用できます。"
---

# Azure Static Web Apps でユーザーが定義した関数ランタイムを使用する

Azure Static Web Apps では、カスタム関数ランタイムを使用して、標準の Azure Static Web Apps 関数の既定の環境以外を使用できます。

この機能は、次の場合に便利です。

- 追加のランタイムやライブラリをサポートしたい場合
- 固有の設定や構成が必要な関数を使用したい場合

## ユーザー定義関数ランタイムの概要

通常、Azure Static Web Apps は [Azure Functions](https://docs.microsoft.com/azure/azure-functions/) を使用してサーバーレス API をホストします。これには特定の Node.js または .NET ランタイムがバンドルされています。

しかし、Azure Static Web Apps では、カスタム Docker イメージを指定することで、独自のランタイムや構成を持つ関数環境を設定できます。

## カスタム関数ランタイムを指定する方法

### 1. Dockerfile を用意する

独自の環境をセットアップする Dockerfile をリポジトリの関数ディレクトリに配置します。例:

```dockerfile
FROM mcr.microsoft.com/azure-functions/dotnet:3.0

# カスタムの依存関係やツールを追加
RUN apt-get update && apt-get install -y some-package
```

### 2. `staticwebapp.config.json` にランタイム情報を追加する

```json
{
  "generatedFunctionsRuntime": "custom",
  "customFunctionsRuntimeImage": "myrepo/mycustomimage:latest"
}
```

- `generatedFunctionsRuntime` を `"custom"` に設定します。
- `customFunctionsRuntimeImage` に、使用するカスタム Docker イメージを指定します。

### 3. 関数のビルドとデプロイ

GitHub Actions や他の CI/CD を通じてコードをビルドしてプッシュすると、指定したカスタムランタイムイメージが使用されて関数をホストします。

## 制限事項

- カスタムランタイムには、Azure Functions の要求を満たす必要があります。
- GitHub Container Registry や Docker Hub などのパブリックイメージリポジトリにイメージをホストしてください。
- Azure Static Web Apps は現在、一部のプランでのみカスタム関数ランタイムをサポートしています。

## まとめ

ユーザー定義の関数ランタイムを使用すれば、さらに柔軟な関数のホスティングが可能になります。標準の Azure Functions では難しい構成や依存関係の追加を実現し、アプリケーションの拡張性が高まります。

詳細は [Azure Static Web Apps の関数に関するドキュメント](https://learn.microsoft.com/azure/static-web-apps/functions) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको छ। हामी सटीकताको लागि प्रयास गरिरहेका छौं, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल भाषामा रहेको दस्तावेजलाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार छैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->