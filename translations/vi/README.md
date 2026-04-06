# Co-op Translator

_Dễ dàng tự động hóa và duy trì các bản dịch cho nội dung giáo dục trên GitHub của bạn bằng nhiều ngôn ngữ khi dự án của bạn phát triển._

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

### 🌐 Hỗ trợ đa ngôn ngữ

#### Được hỗ trợ bởi [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Tiếng Ả Rập](../ar/README.md) | [Tiếng Bengal](../bn/README.md) | [Tiếng Bungari](../bg/README.md) | [Tiếng Miến Điện (Myanmar)](../my/README.md) | [Tiếng Trung (Giản thể)](../zh-CN/README.md) | [Tiếng Trung (Phồn thể, Hồng Kông)](../zh-HK/README.md) | [Tiếng Trung (Phồn thể, Ma Cao)](../zh-MO/README.md) | [Tiếng Trung (Phồn thể, Đài Loan)](../zh-TW/README.md) | [Tiếng Croatia](../hr/README.md) | [Tiếng Séc](../cs/README.md) | [Tiếng Đan Mạch](../da/README.md) | [Tiếng Hà Lan](../nl/README.md) | [Tiếng Estonia](../et/README.md) | [Tiếng Phần Lan](../fi/README.md) | [Tiếng Pháp](../fr/README.md) | [Tiếng Đức](../de/README.md) | [Tiếng Hy Lạp](../el/README.md) | [Tiếng Hebrew](../he/README.md) | [Tiếng Hindi](../hi/README.md) | [Tiếng Hungary](../hu/README.md) | [Tiếng Indonesia](../id/README.md) | [Tiếng Ý](../it/README.md) | [Tiếng Nhật](../ja/README.md) | [Tiếng Kannada](../kn/README.md) | [Tiếng Khmer](../km/README.md) | [Tiếng Hàn](../ko/README.md) | [Tiếng Litva](../lt/README.md) | [Tiếng Mã Lai](../ms/README.md) | [Tiếng Malayalam](../ml/README.md) | [Tiếng Marathi](../mr/README.md) | [Tiếng Nepal](../ne/README.md) | [Tiếng Pidgin Nigeria](../pcm/README.md) | [Tiếng Na Uy](../no/README.md) | [Tiếng Ba Tư (Farsi)](../fa/README.md) | [Tiếng Ba Lan](../pl/README.md) | [Tiếng Bồ Đào Nha (Brazil)](../pt-BR/README.md) | [Tiếng Bồ Đào Nha (Bồ Đào Nha)](../pt-PT/README.md) | [Tiếng Punjabi (Gurmukhi)](../pa/README.md) | [Tiếng Romania](../ro/README.md) | [Tiếng Nga](../ru/README.md) | [Tiếng Serbia (Cyrillic)](../sr/README.md) | [Tiếng Slovakia](../sk/README.md) | [Tiếng Slovenia](../sl/README.md) | [Tiếng Tây Ban Nha](../es/README.md) | [Tiếng Swahili](../sw/README.md) | [Tiếng Thụy Điển](../sv/README.md) | [Tiếng Tagalog (Filipino)](../tl/README.md) | [Tiếng Tamil](../ta/README.md) | [Tiếng Telugu](../te/README.md) | [Tiếng Thái](../th/README.md) | [Tiếng Thổ Nhĩ Kỳ](../tr/README.md) | [Tiếng Ukraina](../uk/README.md) | [Tiếng Urdu](../ur/README.md) | [Tiếng Việt](./README.md)

> **Ưu tiên clone cục bộ?**
>
> Kho lưu trữ này bao gồm hơn 50 bản dịch ngôn ngữ, điều này làm tăng đáng kể kích thước tải xuống. Để clone mà không lấy bản dịch, hãy sử dụng sparse checkout:
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/skytin1004/co-op-translator.git
> cd co-op-translator
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> Điều này cung cấp cho bạn tất cả những gì cần thiết để hoàn thành khóa học với tốc độ tải xuống nhanh hơn nhiều.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Tổng quan

**Co-op Translator** giúp bạn bản địa hóa nội dung giáo dục trên GitHub của bạn sang nhiều ngôn ngữ một cách dễ dàng.  
Khi bạn cập nhật các tệp Markdown, hình ảnh hoặc sổ tay, các bản dịch sẽ được tự động đồng bộ, đảm bảo nội dung của bạn luôn chính xác và cập nhật cho người học trên toàn thế giới.

Ví dụ về cách nội dung được dịch được tổ chức:

![Example](../../translated_images/vi/translation-ex.0c8aa6a7ee0aad2b.webp)

## Cách quản lý trạng thái bản dịch

Co-op Translator quản lý nội dung dịch như **các đối tượng phần mềm có phiên bản**,  
chứ không phải là các tệp tĩnh.

Công cụ theo dõi trạng thái của Markdown dịch, hình ảnh và sổ tay  
sử dụng **metadata theo phạm vi ngôn ngữ**.

Thiết kế này cho phép Co-op Translator:

- Phát hiện đáng tin cậy các bản dịch lỗi thời
- Xử lý Markdown, hình ảnh và sổ tay một cách nhất quán
- Mở rộng an toàn trên các kho lưu trữ lớn, di chuyển nhanh, đa ngôn ngữ

Bằng cách mô hình hóa bản dịch như là các đối tượng được quản lý,  
quy trình bản dịch tự nhiên phù hợp với  
thực tiễn quản lý phụ thuộc và đối tượng của phần mềm hiện đại.

→ [Cách quản lý trạng thái bản dịch](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## Bắt đầu nhanh

```bash
# Tạo và kích hoạt môi trường ảo (khuyến nghị)
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
# Kéo ảnh công khai từ GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Chạy với thư mục hiện tại được gắn và cung cấp .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Cài đặt tối thiểu

1. Đảm bảo bạn có phiên bản Python được hỗ trợ (hiện tại là 3.10-3.12). Trong poetry (pyproject.toml) điều này được xử lý tự động.
2. Tạo tệp `.env` bằng mẫu: [.env.template](../../.env.template)
3. Cấu hình một nhà cung cấp LLM (Azure OpenAI hoặc OpenAI)
4. (Tùy chọn) Để dịch hình ảnh (`-img`), cấu hình Azure AI Vision
5. (Tùy chọn) Bạn có thể cấu hình nhiều bộ thông tin xác thực bằng cách nhân bản các biến với hậu tố như `_1`, `_2`, v.v. Tất cả các biến trong một bộ phải có cùng hậu tố.
6. (Khuyến nghị) Dọn dẹp các bản dịch trước đó để tránh xung đột (ví dụ: `translations/`)
7. (Khuyến nghị) Thêm phần bản dịch vào README của bạn bằng mẫu [README languages template](./getting_started/README_languages_template.md)
8. Xem: [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

## Cách dùng

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

Thêm cờ lệnh: [Command reference](./getting_started/command-reference.md)

## Tính năng

- Tự động dịch cho Markdown, sổ tay và hình ảnh
- Giữ các bản dịch đồng bộ với các thay đổi nguồn
- Hoạt động cục bộ (CLI) hoặc trong CI (GitHub Actions)
- Sử dụng Azure OpenAI hoặc OpenAI; tùy chọn Azure AI Vision cho hình ảnh
- Giữ nguyên định dạng và cấu trúc Markdown

## Tài liệu

- [Hướng dẫn dòng lệnh](./getting_started/command-line-guide/command-line-guide.md)
- [Hướng dẫn GitHub Actions (Kho lưu trữ công khai & bí mật tiêu chuẩn)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Hướng dẫn GitHub Actions (Kho tổ chức Microsoft & thiết lập cấp tổ chức)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Mẫu ngôn ngữ README](./getting_started/README_languages_template.md)
- [Ngôn ngữ được hỗ trợ](./getting_started/supported-languages.md)
- [Đóng góp](./CONTRIBUTING.md)
- [Khắc phục sự cố](./getting_started/troubleshooting.md)

### Hướng dẫn dành riêng cho Microsoft
> [!NOTE]
> Dành cho những người duy trì các kho lưu trữ “For Beginners” của Microsoft.

- [Cập nhật danh sách “khóa học khác” (chỉ dành cho kho lưu trữ MS Beginners)](./getting_started/update-other-courses.md)

## Hỗ trợ chúng tôi và thúc đẩy học tập toàn cầu

Hãy tham gia cùng chúng tôi để cách mạng hóa cách nội dung giáo dục được chia sẻ trên toàn cầu! Hãy cho [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh của chúng tôi là phá bỏ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo ra ảnh hưởng lớn! Đóng góp mã và đề xuất tính năng luôn được hoan nghênh.

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

## Các bài thuyết trình video

👉 Nhấp vào hình bên dưới để xem trên YouTube.

- **Open tại Microsoft**: Một giới thiệu ngắn 18 phút và hướng dẫn nhanh về cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../translated_images/vi/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này hoan nghênh các đóng góp và đề xuất. Quan tâm đến việc đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) của chúng tôi để biết hướng dẫn cách bạn có thể giúp Co-op Translator trở nên dễ tiếp cận hơn.

## Những người đóng góp
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc ứng xử

Dự án này đã áp dụng [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, vui lòng xem [Câu hỏi thường gặp về Quy tắc ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có thêm câu hỏi hoặc góp ý.

## Trí tuệ nhân tạo có trách nhiệm

Microsoft cam kết giúp khách hàng sử dụng các sản phẩm AI của chúng tôi một cách có trách nhiệm, chia sẻ những bài học kinh nghiệm và xây dựng các đối tác dựa trên sự tin cậy thông qua các công cụ như Ghi chú minh bạch và Đánh giá tác động. Nhiều tài nguyên này có thể được tìm thấy tại [https://aka.ms/RAI](https://aka.ms/RAI).
Cách tiếp cận của Microsoft đối với AI có trách nhiệm dựa trên các nguyên tắc AI của chúng tôi về sự công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, sự bao trùm, tính minh bạch và trách nhiệm giải trình.

Các mô hình ngôn ngữ tự nhiên, hình ảnh và giọng nói quy mô lớn - như những mô hình được sử dụng trong mẫu này - có thể hành xử theo những cách không công bằng, không đáng tin cậy hoặc gây xúc phạm, từ đó gây ra các tác hại. Vui lòng tham khảo [Ghi chú minh bạch dịch vụ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để được thông tin về các rủi ro và giới hạn.

Cách tiếp cận được khuyến nghị để giảm thiểu các rủi ro này là bao gồm một hệ thống an toàn trong kiến trúc của bạn có thể phát hiện và ngăn chặn hành vi có hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp một lớp bảo vệ độc lập, có khả năng phát hiện nội dung gây hại do người dùng tạo ra và do AI tạo ra trong các ứng dụng và dịch vụ. Azure AI Content Safety bao gồm các API văn bản và hình ảnh cho phép bạn phát hiện các tài liệu có hại. Chúng tôi cũng có một Studio Content Safety tương tác cho phép bạn xem, khám phá và thử các mã mẫu để phát hiện nội dung có hại trên các phương thức khác nhau. Tài liệu [hướng dẫn nhanh sau đây](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) hướng dẫn bạn qua cách gửi yêu cầu đến dịch vụ.

Một khía cạnh khác cần xem xét là hiệu suất tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, chúng tôi coi hiệu suất là hệ thống hoạt động như bạn và người dùng mong đợi, bao gồm không tạo ra các đầu ra gây hại. Việc đánh giá hiệu suất của toàn bộ ứng dụng có thể thực hiện bằng cách sử dụng [đánh giá chất lượng tạo ra và các chỉ số rủi ro cũng như an toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in).

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng cách sử dụng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Với bộ dữ liệu thử nghiệm hoặc mục tiêu, các thế hệ AI sinh tạo của bạn được đo lường định lượng bằng các bộ đánh giá tích hợp sẵn hoặc bộ đánh giá tùy chỉnh theo lựa chọn của bạn. Để bắt đầu với prompt flow sdk để đánh giá hệ thống của bạn, bạn có thể theo dõi [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Khi bạn thực hiện một lần chạy đánh giá, bạn có thể [hình dung kết quả trong Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Nhãn hiệu

Dự án này có thể bao gồm các nhãn hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng có phép các nhãn hiệu hoặc logo của Microsoft phải tuân theo và theo các [Nguyên tắc sử dụng nhãn hiệu & thương hiệu của Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Việc sử dụng nhãn hiệu hoặc logo Microsoft trong các phiên bản chỉnh sửa của dự án này không được gây nhầm lẫn hoặc ngụ ý sự tài trợ của Microsoft.
Bất kỳ việc sử dụng các nhãn hiệu hoặc logo của bên thứ ba đều phải tuân theo chính sách của bên thứ ba đó.

## Nhận trợ giúp

Nếu bạn gặp khó khăn hoặc có bất kỳ câu hỏi nào về việc xây dựng các ứng dụng AI, hãy tham gia:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi trong quá trình xây dựng, hãy truy cập:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, vui lòng lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc thiếu sót. Tài liệu gốc bằng ngôn ngữ bản địa của nó nên được xem là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->