Japanese mode: マークダウンのトークンを厳密に保持してください。

ルール（必ず守ること）：
1) マークダウンリンクは正確に保持すること：[text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたテキスト](../../../../../../src/co_op_translator/templates/language/同じURL)。
2) リンクをプレーンテキストに書き換えないこと（例：「text」（URL）、text (URL)など）。
3) リンクテキストのみを翻訳し、マークダウンの構造とURLは変更しないこと。
4) マークダウンリンクの周りに「」を追加しないこと。ただし、リンク外の文法で必要な場合は除く。

構造はスタイルよりも重要です。
マークダウントークンが変わる場合は、日本語の自然さを最適化しないこと。

例
原文: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ತಪ್ಪು ದಾಯಿತ್ವ ನಿರಾಕರಣೆ**:
ಈ ದಸ್ತಾವೇಜು [Co-op Translator](https://github.com/Azure/co-op-translator) ಎಂಬ AI ಅನುವಾದ ಸೇವೆಯನ್ನು ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಗೆ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ഉണ്ടായಿರಬಹುದೆಂದು ಪಂದ್ಯವನ್ನು ಮನಗಂಡಿರಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಪ್ರಾಥಮಿಕ ದಸ್ತಾವೇಜು ಅಧಿಕಾರಪ್ರದ ಮೂಲ ಎನ್ನಿಸಬೇಕು. ಮಹತ್ವಪೂರ್ಣ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪುಗೋಷ್ಠಿಗಳು ಅಥವಾ ಅರ್ಥಮಾಡಿಕೆಯಲ್ಲಿ ಸಂಭವಿಸಿದ ತಪ್ಪುಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->