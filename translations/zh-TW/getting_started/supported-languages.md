# 支援語言

以下表格列出目前 **Co-op Translator** 支援的語言。包括語言代碼、語言名稱，以及每種語言已知的問題。如果您想新增支援語言，請將對應的語言代碼、名稱和適當的字型新增到位於 `src/co_op_translator/fonts/` 的 `font_language_mappings.yml` 檔案中，並在測試完成後提交 pull request。

| Language Code | Language Name        | Font                              | RTL Support | Known Issues |
|---------------|----------------------|-----------------------------------|-------------|--------------|
| en            | 英文                 | NotoSans-Medium.ttf               | No          | No           |
| fr            | 法文                 | NotoSans-Medium.ttf               | No          | No           |
| es            | 西班牙文             | NotoSans-Medium.ttf               | No          | No           |
| de            | 德文                 | NotoSans-Medium.ttf               | No          | No           |
| ru            | 俄文                 | NotoSans-Medium.ttf               | No          | No           |
| ar            | 阿拉伯文             | NotoSansArabic-Medium.ttf         | Yes         | No           |
| fa            | 波斯文 (Farsi)       | NotoSansArabic-Medium.ttf         | Yes         | No           |
| ur            | 烏爾都文             | NotoSansArabic-Medium.ttf         | Yes         | No           |
| zh-CN         | 中文（簡體）          | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-MO         | 中文（繁體，澳門）     | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-HK         | 中文（繁體，香港）     | NotoSansCJK-Medium.ttc            | No          | No           |
| zh-TW         | 中文（繁體，台灣）     | NotoSansCJK-Medium.ttc            | No          | No           |
| ja            | 日文                 | NotoSansCJK-Medium.ttc            | No          | No           |
| ko            | 韓文                 | NotoSansCJK-Medium.ttc            | No          | No           |
| hi            | 印地語               | NotoSansDevanagari-Medium.ttf     | No          | No           |
| bn            | 孟加拉文             | NotoSansBengali-Medium.ttf        | No          | No           |
| mr            | 馬拉地語             | NotoSansDevanagari-Medium.ttf     | No          | No           |
| ne            | 尼泊爾語             | NotoSansDevanagari-Medium.ttf     | No          | No           |
| pa            | 旁遮普文 (Gurmukhi)   | NotoSansGurmukhi-Medium.ttf       | No          | No           |
| pt-PT         | 葡萄牙文（葡萄牙）     | NotoSans-Medium.ttf               | No          | No           |
| pt-BR         | 葡萄牙文（巴西）       | NotoSans-Medium.ttf               | No          | No           |
| it            | 義大利文             | NotoSans-Medium.ttf               | No          | No           |
| lt            | 立陶宛文             | NotoSans-Medium.ttf               | No          | No           |
| pl            | 波蘭文               | NotoSans-Medium.ttf               | No          | No           |
| tr            | 土耳其文             | NotoSans-Medium.ttf               | No          | No           |
| el            | 希臘文               | NotoSans-Medium.ttf               | No          | No           |
| th            | 泰文                 | NotoSansThai-Medium.ttf           | No          | No           |
| sv            | 瑞典文               | NotoSans-Medium.ttf               | No          | No           |
| da            | 丹麥文               | NotoSans-Medium.ttf               | No          | No           |
| no            | 挪威文               | NotoSans-Medium.ttf               | No          | No           |
| fi            | 芬蘭文               | NotoSans-Medium.ttf               | No          | No           |
| nl            | 荷蘭文               | NotoSans-Medium.ttf               | No          | No           |
| he            | 希伯來文             | NotoSansHebrew-Medium.ttf         | Yes         | No           |
| vi            | 越南文               | NotoSans-Medium.ttf               | No          | No           |
| id            | 印尼文               | NotoSans-Medium.ttf               | No          | No           |
| ms            | 馬來文               | NotoSans-Medium.ttf               | No          | No           |
| tl            | 他加祿文（菲律賓語）   | NotoSans-Medium.ttf               | No          | No           |
| sw            | 斯瓦希里語           | NotoSans-Medium.ttf               | No          | No           |
| hu            | 匈牙利文             | NotoSans-Medium.ttf               | No          | No           |
| cs            | 捷克文               | NotoSans-Medium.ttf               | No          | No           |
| sk            | 斯洛伐克文           | NotoSans-Medium.ttf               | No          | No           |
| ro            | 羅馬尼亞文           | NotoSans-Medium.ttf               | No          | No           |
| bg            | 保加利亞文           | NotoSans-Medium.ttf               | No          | No           |
| sr            | 塞爾維亞文（西里爾字母）| NotoSans-Medium.ttf               | No          | No           |
| hr            | 克羅埃西亞文         | NotoSans-Medium.ttf               | No          | No           |
| sl            | 斯洛維尼亞文         | NotoSans-Medium.ttf               | No          | No           |
| uk            | 烏克蘭文             | NotoSans-Medium.ttf               | No          | No           |
| my            | 緬甸文（Myanmar）     | NotoSansMyanmar-Medium.ttf        | No          | No           |
| ta            | 泰米爾文             | NotoSansTamil-Medium.ttf          | No          | No           |
| et            | 愛沙尼亞文           | NotoSans-Medium.ttf               | No          | No           |
| pcm           | 尼日利亞畢欽語       | NotoSans-Medium.ttf               | No          | No           |
| te            | 泰盧固文             | NotoSans-Medium.ttf               | No          | No           |
| ml            | 馬拉雅拉姆文         | NotoSans-Medium.ttf               | No          | No           |
| kn            | 卡納達文             | NotoSans-Medium.ttf               | No          | No           |
| km            | 高棉文               | NotoSansKhmer-Medium.ttf          | No          | No           |

## 新增語言

想要新增語言嗎？請參考貢獻指南：

- 請見 Contributing: [貢獻新語言](../CONTRIBUTING.md#contribute-a-new-language)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威依據。對於關鍵資訊，建議尋求專業人工翻譯。因使用本翻譯而導致之任何誤解或誤譯，我們概不負責。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->