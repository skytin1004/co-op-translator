# Co-op Translator

_Tự động hóa và duy trì bản dịch cho nội dung giáo dục GitHub của bạn trên nhiều ngôn ngữ một cách dễ dàng theo sự phát triển của dự án._

![Python 3.10–3.12](https://img.shields.io/badge/python-3.10--3.12-blue)
[![Python package](https://img.shields.io/pypi/v/co-op-translator?color=4BA3FF)](https://pypi.org/project/co-op-translator/)
[![License: MIT](https://img.shields.io/github/license/azure/co-op-translator?color=4BA3FF)](https://github.com/azure/co-op-translator/blob/main/LICENSE)
[![Downloads](https://static.pepy.tech/badge/co-op-translator)](https://pepy.tech/project/co-op-translator)
[![Downloads](https://static.pepy.tech/badge/co-op-translator/month)](https://pepy.tech/project/co-op-translator)
[![Container: GHCR](https://img.shields.io/badge/Container-GHCR-2496ED?logo=docker&logoColor=fff)](https://github.com/azure/co-op-translator/pkgs/container/co-op-translator)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![GitHub contributors](https://img.shields.io/github/contributors/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/azure/co-op-translator.svg)](https://GitHub.com/azure/co-op-translator/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

### 🌐 Hỗ trợ Đa Ngôn Ngữ

#### Được hỗ trợ bởi [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](./README.md)

> **Ưu tiên sao chép nội dung về máy?**
>
> Kho lưu trữ này bao gồm hơn 50 bản dịch ngôn ngữ, điều này làm tăng đáng kể kích thước tải về. Để sao chép mà không có bản dịch, hãy sử dụng sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/Azure/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Điều này sẽ cung cấp cho bạn mọi thứ cần thiết để hoàn thành khóa học với tốc độ tải về nhanh hơn nhiều.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Tổng quan

**Co-op Translator** giúp bạn bản địa hóa nội dung giáo dục trên GitHub sang nhiều ngôn ngữ một cách dễ dàng.  
Khi bạn cập nhật các tệp Markdown, hình ảnh hoặc sổ tay, các bản dịch sẽ tự động được đồng bộ, đảm bảo nội dung của bạn luôn chính xác và cập nhật cho người học trên toàn thế giới.

Ví dụ về cách tổ chức nội dung đã dịch:

![Example](../../imgs/translation-ex.png)

## Cách quản lý trạng thái bản dịch

Co-op Translator quản lý nội dung dịch như các **tác phẩm phần mềm có phiên bản**,  
không phải là các tệp tĩnh.

Công cụ theo dõi trạng thái của các tài liệu Markdown, hình ảnh và sổ tay đã dịch  
bằng **siêu dữ liệu giới hạn theo ngôn ngữ**.

Thiết kế này cho phép Co-op Translator:

- Phát hiện đáng tin cậy các bản dịch đã lỗi thời
- Xử lý nhất quán Markdown, hình ảnh và sổ tay
- Mở rộng an toàn trên các kho lưu trữ đa ngôn ngữ lớn và thay đổi nhanh

Bằng cách mô hình hóa các bản dịch dưới dạng tác phẩm được quản lý,  
quy trình làm việc bản dịch phù hợp tự nhiên với  
các thực hành hiện đại về quản lý phụ thuộc và tác phẩm phần mềm.

→ [Cách quản lý trạng thái bản dịch](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Bắt đầu nhanh

```bash
# Tạo và kích hoạt một môi trường ảo (được khuyến nghị)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Cài đặt gói
pip install co-op-translator
# Dịch
translate -l "ko ja fr" -md
```

Docker:

```bash
# Kéo hình ảnh công khai từ GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Chạy với thư mục hiện tại được gắn và cung cấp .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Thiết lập tối thiểu

1. Đảm bảo bạn có phiên bản Python được hỗ trợ (hiện tại từ 3.10 đến 3.12). Trong poetry (pyproject.toml) điều này được xử lý tự động.
2. Tạo tệp `.env` sử dụng mẫu: [.env.template](../../.env.template)
3. Cấu hình một nhà cung cấp LLM (Azure OpenAI hoặc OpenAI)
4. (Tùy chọn) Để dịch hình ảnh (`-img`), cấu hình Azure AI Vision
5. (Tùy chọn) Bạn có thể cấu hình nhiều bộ thông tin xác thực bằng cách nhân bản biến với các hậu tố như `_1`, `_2`, v.v. Tất cả biến trong một bộ phải có cùng hậu tố.
6. (Khuyến nghị) Dọn sạch các bản dịch trước đó để tránh xung đột (ví dụ: `translations/`)
7. (Khuyến nghị) Thêm phần bản dịch vào README của bạn sử dụng [mẫu ngôn ngữ README](./getting_started/README_languages_template.md)
8. Xem thêm: [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

## Cách sử dụng

Dịch tất cả các loại được hỗ trợ:

```bash
translate -l "ko ja"
```

Chỉ Markdown:

```bash
translate -l "de" -md
```

Markdown + hình ảnh:

```bash
translate -l "pt" -md -img
```

Chỉ sổ tay:

```bash
translate -l "zh" -nb
```

Thêm cờ tùy chọn: [Tham khảo lệnh](./getting_started/command-reference.md)

## Tính năng

- Tự động dịch Markdown, sổ tay và hình ảnh
- Giữ bản dịch đồng bộ với các thay đổi nguồn
- Hoạt động cục bộ (CLI) hoặc trong CI (GitHub Actions)
- Sử dụng Azure OpenAI hoặc OpenAI; có thể thêm Azure AI Vision cho hình ảnh
- Giữ nguyên định dạng và cấu trúc Markdown

## Tài liệu

- [Hướng dẫn dòng lệnh](./getting_started/command-line-guide/command-line-guide.md)
- [Hướng dẫn GitHub Actions (Kho công khai & bí mật tiêu chuẩn)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Hướng dẫn GitHub Actions (Kho tổ chức Microsoft & thiết lập cấp tổ chức)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Mẫu ngôn ngữ README](./getting_started/README_languages_template.md)
- [Ngôn ngữ được hỗ trợ](./getting_started/supported-languages.md)
- [Đóng góp](./CONTRIBUTING.md)
- [Khắc phục sự cố](./getting_started/troubleshooting.md)

### Hướng dẫn đặc thù Microsoft
> [!NOTE]
> Dành riêng cho người duy trì các kho “Dành cho người mới bắt đầu” của Microsoft.

- [Cập nhật danh sách “khóa học khác” (chỉ cho kho MS Beginners)](./getting_started/update-other-courses.md)

## Hỗ trợ chúng tôi và thúc đẩy học tập toàn cầu

Hãy cùng chúng tôi cách mạng hóa cách chia sẻ nội dung giáo dục trên toàn cầu! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh phá bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo nên ảnh hưởng lớn! Chúng tôi luôn hoan nghênh những đóng góp mã và đề xuất tính năng.

### Khám phá nội dung giáo dục Microsoft bằng ngôn ngữ của bạn

- [LangChain4j-for-Beginners](https://github.com/microsoft/LangChain4j-for-Beginners)
- [AZD for Beginners](https://github.com/microsoft/AZD-for-beginners)
- [Edge AI for Beginners](https://github.com/microsoft/edgeai-for-beginners)
- [Model Context Protocol (MCP) For Beginners](https://github.com/microsoft/mcp-for-beginners)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners)
- [Generative AI for Beginners using .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners)
- [Generative AI for Beginners using Java](https://github.com/microsoft/generative-ai-for-beginners-java)
- [ML for Beginners](https://aka.ms/ml-beginners)
- [Data Science for Beginners](https://aka.ms/datascience-beginners)
- [AI for Beginners](https://aka.ms/ai-beginners)
- [Cybersecurity for Beginners](https://github.com/microsoft/Security-101)
- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [PhiCookBook](https://github.com/microsoft/PhiCookBook)

## Video giới thiệu

👉 Bấm vào hình dưới để xem trên YouTube.

- **Open at Microsoft**: Giới thiệu ngắn gọn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này hoan nghênh các đóng góp và gợi ý. Bạn quan tâm đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn cách bạn có thể giúp Co-op Translator dễ tiếp cận hơn.

## Những người đóng góp
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc ứng xử

Dự án này đã áp dụng [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Để biết thêm thông tin, hãy xem [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) hoặc  
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có bất kỳ câu hỏi hoặc nhận xét bổ sung nào.

## AI Có Trách Nhiệm

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI của chúng tôi một cách có trách nhiệm, chia sẻ những bài học kinh nghiệm và xây dựng các mối quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).  
Phương pháp của Microsoft về AI có trách nhiệm dựa trên các nguyên tắc AI của chúng tôi về sự công bằng, độ tin cậy và an toàn, sự riêng tư và bảo mật, tính bao trùm, minh bạch và trách nhiệm giải trình.

Các mô hình ngôn ngữ tự nhiên, hình ảnh và giọng nói ở quy mô lớn - như những mô hình được sử dụng trong ví dụ này - có thể hành xử theo cách không công bằng, không đáng tin cậy hoặc gây khó chịu, từ đó gây ra các tác hại. Vui lòng tham khảo [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được biết về những rủi ro và giới hạn.

Phương pháp được khuyến nghị để giảm thiểu các rủi ro này là bao gồm một hệ thống an toàn trong kiến trúc của bạn có thể phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung do người dùng và AI tạo ra có hại trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện tài liệu có hại. Chúng tôi cũng có một Content Safety Studio tương tác cho phép bạn xem, khám phá và thử nghiệm mã mẫu để phát hiện nội dung có hại trên các dạng thức khác nhau. Tài liệu [bắt đầu nhanh sau đây](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) sẽ hướng dẫn bạn cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần xem xét là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa mô thức và đa mô hình, chúng tôi xem hiệu suất là hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra kết quả đầu ra có hại. Việc đánh giá hiệu suất toàn bộ ứng dụng của bạn bằng cách sử dụng [chỉ số chất lượng sinh và rủi ro và an toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) là rất quan trọng.

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Với tập dữ liệu kiểm thử hoặc mục tiêu, các thế hệ AI tạo sinh của bạn được đo lường định lượng bằng các bộ đánh giá tích hợp hoặc bộ đánh giá tùy chỉnh mà bạn chọn. Để bắt đầu với prompt flow sdk để đánh giá hệ thống của bạn, bạn có thể theo hướng dẫn [bắt đầu nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi bạn thực hiện một lần chạy đánh giá, bạn có thể [trực quan hóa kết quả trong Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Nhãn hiệu

Dự án này có thể chứa nhãn hiệu hoặc logo cho các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng nhãn hiệu hoặc logo của Microsoft được ủy quyền phải tuân theo và không được vi phạm [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).  
Việc sử dụng nhãn hiệu hoặc logo của Microsoft trong các phiên bản sửa đổi của dự án này không được gây nhầm lẫn hoặc ngụ ý sự tài trợ của Microsoft.  
Mọi việc sử dụng nhãn hiệu hoặc logo của bên thứ ba đều phải tuân theo chính sách của bên thứ ba đó.

## Nhận Hỗ Trợ

Nếu bạn gặp khó khăn hoặc có câu hỏi về việc xây dựng ứng dụng AI, hãy tham gia:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi khi xây dựng, hãy truy cập:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn đáng tin cậy nhất. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->