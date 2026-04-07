# Azure Communication Services で音声トランスクリプションを使用する

このチュートリアルでは、﻿[Azure Communication Services](https://learn.microsoft.com/azure/communication-services/) (ACS)の‎[Speech SDK](https://learn.microsoft.com/azure/communication-services/quickstarts/speech-sdk)を使って音声の文字起こしを行う方法を説明します。

## 前提条件

- Visual Studio 2019 以降、もしくは同等の C# 対応の IDE
- [Azure サブスクリプション](https://azure.microsoft.com/free/)
- Azure Communication Services リソース

## ステップ 1: Azure Communication Services リソースの作成

1. Azure ポータルにサインインします。
2. 「リソースの作成」 > 「Communication Services」を検索し、リソースを作成します。
3. リソースの詳細を入力し、作成を完了します。
4. 作成後、<strong>接続文字列</strong>を取得してください。これは、後のアプリケーション設定で必要です。

## ステップ 2: プロジェクトのセットアップ

1. 新しい C# コンソールアプリケーションプロジェクトを作成します。
2. [Azure.Communication.Calling](https://www.nuget.org/packages/Azure.Communication.Calling/) と [Microsoft.CognitiveServices.Speech](https://www.nuget.org/packages/Microsoft.CognitiveServices.Speech/) の NuGet パッケージをインストールします。

```powershell
Install-Package Azure.Communication.Calling
Install-Package Microsoft.CognitiveServices.Speech
```

## ステップ 3: サンプルコード

以下のコードは、ACS と Speech SDK を使って音声認識を行うシンプルな例です。

```csharp
using System;
using Azure.Communication.Calling;
using Microsoft.CognitiveServices.Speech;

class Program
{
    static async Task Main(string[] args)
    {
        string connectionString = "<YOUR_ACS_CONNECTION_STRING>";
        var callClient = new CallClient();
        var callAgent = await callClient.CreateCallAgentAsync(new CommunicationUserCredential(connectionString));
        var conversation = await callAgent.JoinAsync(new GroupCallLocator(new Guid("<GROUP_CALL_ID>")));

        var config = SpeechConfig.FromSubscription("<YOUR_SPEECH_KEY>", "<YOUR_SPEECH_REGION>");
        using var recognizer = new SpeechRecognizer(config);

        recognizer.Recognizing += (s, e) =>
        {
            Console.WriteLine($"Recognizing: {e.Result.Text}");
        };

        recognizer.Recognized += (s, e) =>
        {
            if (e.Result.Reason == ResultReason.RecognizedSpeech)
            {
                Console.WriteLine($"Recognized: {e.Result.Text}");
            }
        };

        await recognizer.StartContinuousRecognitionAsync();
        Console.WriteLine("Press any key to stop...");
        Console.ReadKey();
        await recognizer.StopContinuousRecognitionAsync();
    }
}
```

## 参考情報

- [Azure Communication Services ドキュメント](https://learn.microsoft.com/azure/communication-services/)
- [Speech SDK の使い方](https://learn.microsoft.com/azure/communication-services/quickstarts/speech-sdk)
- [Azure Communication Services のチュートリアル（C#）](https://github.com/Azure/communication-services-dotnet-quickstarts)

このチュートリアルを完了後、リアルタイムの通話や会議などで音声の文字起こしを統合できます。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯而成。雖然我們力求準確，但請注意，機器翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威資料。對於重要資訊，建議使用專業人工翻譯。我們不對因使用本翻譯而引起之誤解或誤譯負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->