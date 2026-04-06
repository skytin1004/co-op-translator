# ルートディレクトリに *.env* ファイルを作成する

このチュートリアルでは、*.env* ファイルを使用して Azure サービスの環境変数を設定する方法をご案内します。環境変数を使うことで、API キーなどの機密情報をコードベースにハードコーディングすることなく安全に管理できます。

> [!IMPORTANT]
> - 設定が必要なのは言語モデルサービスのうちいずれか1つだけ（Azure OpenAI または OpenAI）です。使用したいサービスの環境変数を入力してください。複数の言語モデルの環境変数が設定されている場合、co-op translator が優先度に基づいて1つを選択します。
> - Computer Vision の環境変数が設定されていない場合、翻訳者は自動的に[Markdown 専用モード](./markdown-only-mode.md)に切り替わります。

> [!NOTE]
> 本ガイドは主に Azure サービスに焦点を当てていますが、[対応しているモデルとサービス一覧](../README.md#-supported-models-and-services)から任意の対応言語モデルを選ぶことも可能です。

## *.env* ファイルを作成する

プロジェクトのルートディレクトリに *.env* という名前のファイルを作成します。このファイルにすべての環境変数をシンプルな形式で保存します。

> [!WARNING]
> *.env* ファイルを Git などのバージョン管理システムにコミットしないでください。誤ってコミットしないように、*.env* を .gitignore ファイルに追加してください。

1. プロジェクトのルートディレクトリに移動します。

1. プロジェクトのルートディレクトリに *.env* ファイルを作成します。

1. *.env* ファイルを開き、次のテンプレートを貼り付けます：

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> API キーとエンドポイントの確認方法は、[set-up-azure-ai.md](../set-up-azure-ai.md) を参照してください。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責事項**：  
本書類は AI 翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。原文のオリジナル言語による文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因するいかなる誤解や解釈の違いについても、当方は責任を負いかねます。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->