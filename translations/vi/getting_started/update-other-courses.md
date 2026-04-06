# Cập nhật phần "Các Khóa Học Khác" (repos Microsoft Beginners)

Hướng dẫn này giải thích cách làm cho phần "Các Khóa Học Khác" tự động đồng bộ hóa bằng Co-op Translator, và cách cập nhật mẫu toàn cục cho tất cả các repos.

- Áp dụng cho: Chỉ các kho Microsoft Beginners
- Làm việc với: Co-op Translator CLI và GitHub Actions
- Nguồn mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Bắt đầu nhanh: Bật tự động đồng bộ trong repo của bạn

Thêm các dấu hiệu sau quanh phần "Các Khóa Học Khác" trong README của bạn. Co-op Translator sẽ thay thế mọi thứ giữa các dấu hiệu này mỗi lần chạy.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Mỗi lần Co-op Translator chạy — qua CLI (ví dụ, `translate -l "<language codes>"`) hoặc GitHub Actions — nó sẽ tự động cập nhật phần "Các Khóa Học Khác" được bao quanh bởi các dấu hiệu này.

> [!NOTE]
> Nếu bạn đã có danh sách sẵn, chỉ cần bao nó với cùng các dấu hiệu đó. Lần chạy tiếp theo sẽ thay thế bằng nội dung chuẩn hóa mới nhất.

---

## Cách thay đổi nội dung toàn cục

Nếu bạn muốn cập nhật nội dung chuẩn hóa xuất hiện trong tất cả các repo Beginners:

1. Chỉnh sửa mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Mở pull request vào repo Co-op Translator với các thay đổi của bạn
3. Sau khi PR được hợp nhất, phiên bản Co-op Translator sẽ được cập nhật
4. Lần tới khi Co-op Translator chạy (CLI hoặc GitHub Action) trong repo mục tiêu, nó sẽ tự động đồng bộ phần đã cập nhật

Điều này đảm bảo một nguồn duy nhất cho nội dung "Các Khóa Học Khác" trên tất cả các kho Beginners.


## Kích thước Repo

Các repo có thể trở nên lớn do số lượng ngôn ngữ được dịch để giúp người dùng cuối hướng dẫn cách sử dụng clone - sparse chỉ để clone những ngôn ngữ cần thiết mà không phải toàn bộ repo

```
> **Prefer to Clone Locally?**
>
> This repository includes 50+ language translations which significantly increases the download size. To clone without translations, use sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/*****.git
> cd *****
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> This gives you everything you need to complete the course with a much faster download.
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Tuyên bố từ chối trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Văn bản gốc bằng ngôn ngữ gốc phải được coi là nguồn chính xác và đáng tin cậy. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->