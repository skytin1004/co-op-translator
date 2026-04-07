# Cập nhật phần "Khóa học khác" (các kho Microsoft Beginners)

Hướng dẫn này giải thích cách làm cho phần "Khóa học khác" tự động đồng bộ hóa bằng Co‑op Translator, và cách cập nhật mẫu toàn cục cho tất cả các kho.

- Áp dụng cho: Chỉ các kho Microsoft Beginners
- Hoạt động với: Co‑op Translator CLI và GitHub Actions
- Nguồn mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Bắt đầu nhanh: Bật tự động đồng bộ trong kho của bạn

Thêm các dấu hiệu sau quanh phần "Khóa học khác" trong README của bạn. Co‑op Translator sẽ thay thế tất cả nội dung giữa các dấu hiệu này mỗi lần chạy.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Mỗi lần Co‑op Translator chạy — qua CLI (ví dụ, `translate -l "<language codes>"`) hoặc GitHub Actions — nó tự động cập nhật phần "Khóa học khác" được bao quanh bởi các dấu hiệu này.

> [!NOTE]
> Nếu bạn đã có danh sách hiện có, chỉ cần bao quanh nó bằng các dấu hiệu giống vậy. Lần chạy tiếp theo sẽ thay thế nó bằng nội dung chuẩn mới nhất.

---

## Cách thay đổi nội dung toàn cục

Nếu bạn muốn cập nhật nội dung chuẩn hiện diện trong tất cả các kho Beginners:

1. Chỉnh sửa mẫu: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Mở pull request vào kho Co-op Translator với thay đổi của bạn
3. Sau khi PR được hợp nhất, phiên bản Co‑op Translator sẽ được cập nhật
4. Lần chạy tiếp theo của Co‑op Translator (CLI hoặc GitHub Action) trong kho mục tiêu sẽ tự động đồng bộ phần cập nhật

Điều này đảm bảo một nguồn duy nhất về nội dung "Khóa học khác" trên tất cả các kho Beginners.


## Kích thước kho

Các kho có thể trở nên lớn do số lượng ngôn ngữ được dịch để giúp người dùng cuối có hướng dẫn về cách sử dụng clone - sparse chỉ để clone các ngôn ngữ cần thiết mà không phải toàn bộ kho

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
**Từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->