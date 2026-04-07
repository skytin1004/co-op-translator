# Co-op Translator 用 Azure AI のセットアップ（Azure OpenAI & Azure AI Vision）

このガイドでは、Azure AI Foundry 内で言語翻訳に Azure OpenAI、および画像ベースの翻訳に使用可能な画像コンテンツ分析のための Azure Computer Vision のセットアップ手順を説明します。

**前提条件:**
- アクティブなサブスクリプションを持つ Azure アカウント。
- Azure サブスクリプションでリソースおよびデプロイメントを作成するための十分な権限。

## Azure AI プロジェクトの作成

まず、AI リソースの管理の中心として機能する Azure AI プロジェクトを作成します。

1. [https://ai.azure.com](https://ai.azure.com) にアクセスして、Azure アカウントでサインインします。

1. **+Create** を選択して新しいプロジェクトを作成します。

1. 以下を行います：
   - **Project name**（例: `CoopTranslator-Project`）を入力します。
   - **AI hub**（例: `CoopTranslator-Hub`）を選択します（必要に応じて新規作成）。

1. 「**Review and Create**」をクリックしてプロジェクトを設定します。プロジェクトの概要ページに移動します。

## 言語翻訳のための Azure OpenAI のセットアップ

プロジェクト内で、テキスト翻訳のバックエンドとして機能する Azure OpenAI モデルをデプロイします。

### プロジェクトに移動する

まだの場合は、Azure AI Foundry で新しく作成したプロジェクト（例: `CoopTranslator-Project`）を開きます。

### OpenAI モデルのデプロイ

1. プロジェクトの左側メニューで「My assets」内の「**Models + endpoints**」を選択します。

1. **+ Deploy model** を選択します。

1. **Deploy Base Model** を選択します。

1. 利用可能なモデルのリストが表示されます。適切な GPT モデルを絞り込みまたは検索してください。`gpt-4o` を推奨します。

1. 目的のモデルを選択し、**Confirm** をクリックします。

1. **Deploy** を選択します。

### Azure OpenAI の設定

デプロイ後、「**Models + endpoints**」ページからデプロイメントを選択すると、**REST endpoint URL**、**Key**、**Deployment name**、**Model name**、**API version** を確認できます。これらは翻訳モデルをアプリケーションに統合する際に必要です。

> [!NOTE]
> ご要件に応じて [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) ページから API バージョンを選択できます。**API version** は Azure AI Foundry の「Models + endpoints」ページに表示される **Model version** とは異なるのでご注意ください。

## 画像翻訳のための Azure Computer Vision セットアップ

画像内のテキストを翻訳可能にするには、Azure AI Service の API キーとエンドポイントが必要です。

1. Azure AI プロジェクト（例: `CoopTranslator-Project`）に移動し、プロジェクト概要ページにいることを確認します。

### Azure AI Service の設定

Azure AI Service タブから API キーとエンドポイントを取得します。

1. Azure AI プロジェクト（例: `CoopTranslator-Project`）に移動し、プロジェクト概要ページにいることを確認します。

1. Azure AI Service タブにある **API Key** と **Endpoint** を見つけます。

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

この接続により、リンクされた Azure AI Services リソース（画像分析を含む）の機能を AI Foundry プロジェクトで使用可能になります。その後、この接続をノートブックやアプリケーションで利用し、画像からテキストを抽出し、それを Azure OpenAI モデルへ翻訳用に送信できます。

## 認証情報の統合

この時点で、以下の情報が揃っているはずです：

**Azure OpenAI（テキスト翻訳用）:**
- Azure OpenAI エンドポイント
- Azure OpenAI API キー
- Azure OpenAI モデル名（例: `gpt-4o`）
- Azure OpenAI デプロイメント名（例: `cooptranslator-gpt4o`）
- Azure OpenAI API バージョン

**Azure AI Services（Vision 経由の画像テキスト抽出用）:**
- Azure AI Service エンドポイント
- Azure AI Service API キー

### 例：環境変数の設定例（プレビュー）

後ほどアプリケーションを構築する際に、これらの認証情報を環境変数として設定することが考えられます:

```bash
# Azure AI サービスの認証情報（画像翻訳に必要）
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # 例: 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# オプションのフォールバックセット: 接尾辞 _1/_2 を付けた重複変数（セット内のすべての変数に同じインデックス）
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI の認証情報（テキスト翻訳に必要）
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # 例: 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # 例: gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # 例: cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # 例: 2024-12-01-preview

# オプションのフォールバックセット: 接尾辞 _1/_2 を付けた完全な AZURE_OPENAI_* セットの複製（すべての変数に同じインデックス）
```

---

### 参考資料

- [Azure AI Foundry でのプロジェクト作成方法](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI リソースの作成方法](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundry での OpenAI モデルのデプロイ方法](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**:  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性には努めておりますが、自動翻訳には誤りや不正確な部分が含まれている可能性があることをご承知おきください。原文の言語で記載された文書が権威ある情報源と見なされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤訳について、当社は一切の責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->