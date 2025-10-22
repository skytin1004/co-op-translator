<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f579b7f148746593e3e9023b56a8c30d",
  "translation_date": "2025-10-22T12:09:43+00:00",
  "source_file": "README.md",
  "language_code": "vi"
}
-->
# Co-op Translator

_Tự động hóa việc dịch nội dung giáo dục trên GitHub của bạn sang nhiều ngôn ngữ để tiếp cận người dùng toàn cầu một cách dễ dàng._

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
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](./README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Azure AI Foundry Discord](https://dcbadge.limes.pink/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## Tổng quan

**Co-op Translator** giúp bạn dịch nhanh nội dung giáo dục trên GitHub sang nhiều ngôn ngữ, tiếp cận người dùng toàn cầu một cách dễ dàng. Khi bạn cập nhật các file Markdown, hình ảnh hoặc notebook Jupyter, bản dịch sẽ được đồng bộ tự động để đảm bảo nội dung giáo dục trên GitHub luôn mới và phù hợp với người dùng quốc tế.

Xem cách Co-op Translator tổ chức nội dung giáo dục đã dịch trên GitHub:

![Example](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.vi.png)

## Bắt đầu nhanh

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the package
pip install co-op-translator
# Translate
translate -l "ko ja fr" -md
```

Docker:

```bash
# Pull the public image from GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# Run with current folder mounted and .env provided (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## Thiết lập tối thiểu

- Tạo file `.env` dựa trên mẫu: [.env.template](../../.env.template)
- Cấu hình một nhà cung cấp LLM (Azure OpenAI hoặc OpenAI)
- Nếu muốn dịch hình ảnh (`-img`), cần thiết lập thêm Azure AI Vision
- Khuyến nghị: Nếu bạn đã có bản dịch từ các công cụ khác, hãy dọn dẹp trước để tránh xung đột (ví dụ: `translations/`).
- Khuyến nghị: Thêm mục các ngôn ngữ dịch vào README bằng [mẫu README languages](./README_languages_template.md)
- Xem thêm: [Thiết lập Azure AI](./getting_started/set-up-azure-ai.md)

## Sử dụng

Dịch tất cả các loại được hỗ trợ:

```bash
translate -l "ko ja"
```

Chỉ dịch Markdown:

```bash
translate -l "de" -md
```

Dịch Markdown + hình ảnh:

```bash
translate -l "pt" -md -img
```

Chỉ dịch notebook:

```bash
translate -l "zh" -nb
```

Thêm các tùy chọn: [Tham khảo lệnh](./getting_started/command-reference.md)

## Tính năng

- Tự động dịch Markdown, notebook và hình ảnh
- Giữ bản dịch luôn đồng bộ với nội dung gốc
- Hoạt động trên máy cá nhân (CLI) hoặc CI (GitHub Actions)
- Sử dụng Azure OpenAI hoặc OpenAI; tùy chọn Azure AI Vision cho hình ảnh
- Giữ nguyên định dạng và cấu trúc Markdown

## Tài liệu

- [Hướng dẫn dòng lệnh](./getting_started/command-line-guide/command-line-guide.md)
- [Hướng dẫn GitHub Actions (Repo công khai & secrets tiêu chuẩn)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [Hướng dẫn GitHub Actions (Repo tổ chức Microsoft & thiết lập cấp tổ chức)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [Các ngôn ngữ hỗ trợ](./getting_started/supported-languages.md)
- [Khắc phục sự cố](./getting_started/troubleshooting.md)

## Ủng hộ chúng tôi và thúc đẩy học tập toàn cầu

Hãy cùng chúng tôi thay đổi cách chia sẻ nội dung giáo dục trên toàn thế giới! Hãy tặng [Co-op Translator](https://github.com/azure/co-op-translator) một ⭐ trên GitHub và ủng hộ sứ mệnh phá vỡ rào cản ngôn ngữ trong học tập và công nghệ. Sự quan tâm và đóng góp của bạn tạo ra ảnh hưởng lớn! Luôn hoan nghênh đóng góp mã nguồn và đề xuất tính năng mới.

### Khám phá nội dung giáo dục của Microsoft bằng ngôn ngữ của bạn

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

## Video trình bày

Tìm hiểu thêm về Co-op Translator qua các video trình bày _(Nhấn vào hình bên dưới để xem trên YouTube.)_:

- **Open at Microsoft**: Giới thiệu ngắn 18 phút và hướng dẫn nhanh cách sử dụng Co-op Translator.

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.vi.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## Đóng góp

Dự án này luôn chào đón các đóng góp và ý kiến. Bạn muốn đóng góp cho Azure Co-op Translator? Vui lòng xem [CONTRIBUTING.md](./CONTRIBUTING.md) để biết hướng dẫn cách giúp Co-op Translator trở nên dễ tiếp cận hơn.

## Những người đóng góp

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## Quy tắc ứng xử

Dự án này tuân thủ [Quy tắc ứng xử mã nguồn mở của Microsoft](https://opensource.microsoft.com/codeofconduct/).
Để biết thêm thông tin, xem [Câu hỏi thường gặp về Quy tắc ứng xử](https://opensource.microsoft.com/codeofconduct/faq/) hoặc
liên hệ [opencode@microsoft.com](mailto:opencode@microsoft.com) nếu có câu hỏi hoặc ý kiến bổ sung.

## AI có trách nhiệm

Microsoft cam kết giúp khách hàng sử dụng sản phẩm AI một cách có trách nhiệm, chia sẻ kinh nghiệm và xây dựng quan hệ đối tác dựa trên sự tin tưởng thông qua các công cụ như Transparency Notes và Impact Assessments. Nhiều tài nguyên này có tại [https://aka.ms/RAI](https://aka.ms/RAI).
Cách tiếp cận AI có trách nhiệm của Microsoft dựa trên các nguyên tắc về công bằng, độ tin cậy và an toàn, quyền riêng tư và bảo mật, tính toàn diện, minh bạch và trách nhiệm.

Các mô hình ngôn ngữ, hình ảnh và giọng nói quy mô lớn - như những mô hình sử dụng trong ví dụ này - có thể hoạt động không công bằng, không đáng tin cậy hoặc gây phản cảm, dẫn đến các tác hại. Vui lòng tham khảo [Ghi chú minh bạch dịch vụ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) để nắm rõ rủi ro và giới hạn.

Cách tốt nhất để giảm thiểu rủi ro là tích hợp hệ thống an toàn vào kiến trúc của bạn để phát hiện và ngăn chặn hành vi gây hại. [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) cung cấp lớp bảo vệ độc lập, có thể phát hiện nội dung do người dùng hoặc AI tạo ra có hại trong ứng dụng và dịch vụ. Azure AI Content Safety có API cho văn bản và hình ảnh giúp phát hiện nội dung nguy hiểm. Ngoài ra còn có Content Safety Studio cho phép bạn xem, khám phá và thử mã mẫu để phát hiện nội dung gây hại ở nhiều dạng khác nhau. Tài liệu [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) sẽ hướng dẫn bạn cách gửi yêu cầu tới dịch vụ này.
Một khía cạnh khác cần lưu ý là hiệu năng tổng thể của ứng dụng. Với các ứng dụng đa phương thức và đa mô hình, hiệu năng được hiểu là hệ thống hoạt động đúng như bạn và người dùng mong đợi, bao gồm cả việc không tạo ra các kết quả gây hại. Việc đánh giá hiệu năng của toàn bộ ứng dụng bằng [các chỉ số chất lượng sinh và rủi ro, an toàn](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) là rất quan trọng.

Bạn có thể đánh giá ứng dụng AI của mình trong môi trường phát triển bằng [prompt flow SDK](https://microsoft.github.io/promptflow/index.html). Với một bộ dữ liệu kiểm thử hoặc mục tiêu, các kết quả sinh ra từ ứng dụng AI của bạn sẽ được đo lường định lượng bằng các bộ đánh giá tích hợp sẵn hoặc bộ đánh giá tùy chỉnh do bạn lựa chọn. Để bắt đầu sử dụng prompt flow sdk để đánh giá hệ thống, bạn có thể làm theo [hướng dẫn nhanh](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk). Sau khi thực hiện một lần đánh giá, bạn có thể [trực quan hóa kết quả trên Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results).

## Thương hiệu

Dự án này có thể chứa các thương hiệu hoặc logo của các dự án, sản phẩm hoặc dịch vụ. Việc sử dụng hợp lệ các thương hiệu hoặc logo của Microsoft phải tuân thủ
[Hướng dẫn về Thương hiệu & Nhãn hiệu của Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Việc sử dụng thương hiệu hoặc logo của Microsoft trong các phiên bản đã chỉnh sửa của dự án này không được gây nhầm lẫn hoặc ám chỉ sự bảo trợ của Microsoft.
Việc sử dụng thương hiệu hoặc logo của bên thứ ba phải tuân theo chính sách của bên thứ ba đó.

## Hỗ trợ

Nếu bạn gặp khó khăn hoặc có câu hỏi về việc xây dựng ứng dụng AI, hãy tham gia:

<a href="https://aka.ms/foundry/discord"><img src="https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff" alt="Azure AI Foundry Discord"></a>

Nếu bạn có phản hồi về sản phẩm hoặc gặp lỗi khi xây dựng, hãy truy cập:

<a href="https://aka.ms/foundry/forum"><img src="https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff" alt="Azure AI Foundry Developer Forum"></a>

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được coi là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.