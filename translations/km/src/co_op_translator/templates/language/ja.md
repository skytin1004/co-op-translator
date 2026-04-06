Japaneseモード：Markdownトークンを厳密に保持します。

ルール（必ず従ってください）:  
1) Markdownリンクは正確に保持します: [text](../../../../../../src/co_op_translator/templates/language/URL) -> [翻訳されたtext](../../../../../../src/co_op_translator/templates/language/同じURL)。  
2) リンクをプレーンテキストとして書き換えないでください（例：「text」（URL）、text (URL)など）。  
3) リンクテキストのみを翻訳し、Markdownの構造とURLは変更しないでください。  
4) 外部リンクの文法が必要でない限り、Markdownリンクに「」を付けないでください。

スタイルよりも構造が重要です。  
Markdownトークンが変わる場合は、日本語の自然さを最適化しないでください。  

例  
ソース: This document uses [Co-op Translator](https://github.com/Azure/co-op-translator).  
正解: 本書類は [Co-op Translator](https://github.com/Azure/co-op-translator) を使用しています。  
誤り: 本書類は「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用しています。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការសេចក្តីបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខិតខំប្រឹងប្រែងដើម្បីភាពត្រឹមត្រូវ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិក៏អាចមានកម្រិតកំហុសឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមនៅភាសាបឋមរបស់វាគួរត្រូវបានពិចារណាថាជាដើមតំណាងផ្លូវការជាសំខាន់។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ ច្បាប់អនុវត្តការបកប្រែដោយមនុស្សជំនាញគឺត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុសដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->