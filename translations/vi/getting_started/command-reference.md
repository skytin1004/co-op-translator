# Tham khảo lệnh

CLI **Co-op Translator** cung cấp một số tùy chọn để tùy chỉnh quá trình dịch:

Lệnh                                         | Mô tả
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Dịch dự án của bạn sang các ngôn ngữ được chỉ định. Ví dụ: translate -l "es fr de" dịch sang tiếng Tây Ban Nha, tiếng Pháp và tiếng Đức. Sử dụng translate -l "all" để dịch sang tất cả các ngôn ngữ được hỗ trợ.
translate -l "language_codes" -u              | Cập nhật bản dịch bằng cách xóa các bản dịch hiện có và tạo lại chúng. Cảnh báo: Điều này sẽ xóa tất cả các bản dịch hiện tại cho các ngôn ngữ được chỉ định.
translate -l "language_codes" -img            | Chỉ dịch các tệp hình ảnh.
translate -l "language_codes" -md             | Chỉ dịch các tệp Markdown.
translate -l "language_codes" -nb             | Chỉ dịch các tệp sổ tay Jupyter (.ipynb).
translate -l "language_codes" --fix           | Dịch lại các tệp có điểm tin cậy thấp dựa trên kết quả đánh giá trước đó.
translate -l "language_codes" -d              | Bật chế độ gỡ lỗi để có nhật ký chi tiết.
translate -l "language_codes" --save-logs, -s | Lưu nhật ký mức DEBUG vào các tệp trong <root_dir>/logs/ (bảng điều khiển vẫn kiểm soát bằng -d)
translate -l "language_codes" -r "root_dir"   | Chỉ định thư mục gốc của dự án
translate -l "language_codes" -f              | Sử dụng chế độ nhanh cho dịch hình ảnh (tăng tốc độ vẽ lên đến 3 lần với một chút giảm chất lượng và căn chỉnh).
translate -l "language_codes" -y              | Tự động xác nhận tất cả các lệnh nhắc (hữu ích cho pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Bật hoặc tắt việc thêm phần tuyên bố dịch máy vào markdown và sổ tay đã được dịch (mặc định: bật).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Cá nhân hóa phần khuyến cáo ngôn ngữ trong README (sparse checkout) với URL kho lưu trữ của bạn.
translate -l "language_codes" --help          | Chi tiết trợ giúp trong CLI hiển thị các lệnh có sẵn
evaluate -l "language_code"                  | Đánh giá chất lượng bản dịch cho một ngôn ngữ cụ thể và cung cấp điểm tin cậy
evaluate -l "language_code" -c 0.8           | Đánh giá bản dịch với ngưỡng tin cậy tùy chỉnh
evaluate -l "language_code" -f               | Chế độ đánh giá nhanh (chỉ dựa trên quy tắc, không dùng LLM)
evaluate -l "language_code" -D               | Chế độ đánh giá sâu (chỉ dựa trên LLM, kỹ hơn nhưng chậm hơn)
evaluate -l "language_code" --save-logs, -s  | Lưu nhật ký mức DEBUG vào các tệp trong <root_dir>/logs/
migrate-links -l "language_codes"             | Xử lý lại các tệp Markdown đã dịch để cập nhật liên kết đến các sổ tay (.ipynb). Ưu tiên các sổ tay đã dịch khi có; nếu không có thể dùng sổ tay gốc.
migrate-links -l "language_codes" -r          | Chỉ định thư mục gốc dự án (mặc định: thư mục hiện tại).
migrate-links -l "language_codes" --dry-run   | Hiển thị các tệp sẽ thay đổi mà không ghi thay đổi.
migrate-links -l "language_codes" --no-fallback-to-original | Không ghi lại liên kết đến sổ tay gốc khi bản dịch bị thiếu (chỉ cập nhật khi bản dịch tồn tại).
migrate-links -l "language_codes" -d          | Bật chế độ gỡ lỗi để có nhật ký chi tiết.
migrate-links -l "language_codes" --save-logs, -s | Lưu nhật ký mức DEBUG vào các tệp trong <root_dir>/logs/
migrate-links -l "all" -y                      | Xử lý tất cả các ngôn ngữ và tự động xác nhận lệnh nhắc cảnh báo.

## Ví dụ sử dụng

  1. Hành vi mặc định (thêm bản dịch mới mà không xóa các bản dịch hiện có):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Chỉ thêm bản dịch hình ảnh tiếng Hàn mới (không xóa bản dịch hiện có):    translate -l "ko" -img

  3. Cập nhật tất cả bản dịch tiếng Hàn (Cảnh báo: Xóa toàn bộ bản dịch tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -u

  4. Cập nhật chỉ hình ảnh tiếng Hàn (Cảnh báo: Xóa toàn bộ hình ảnh tiếng Hàn hiện có trước khi dịch lại):    translate -l "ko" -img -u

  5. Thêm bản dịch markdown mới cho tiếng Hàn mà không ảnh hưởng các bản dịch khác:    translate -l "ko" -md

  6. Sửa bản dịch có độ tin cậy thấp dựa trên kết quả đánh giá trước đó: translate -l "ko" --fix

  7. Sửa bản dịch có độ tin cậy thấp cho các tệp cụ thể (markdown): translate -l "ko" --fix -md

  8. Sửa bản dịch có độ tin cậy thấp cho các tệp cụ thể (hình ảnh): translate -l "ko" --fix -img

  9. Sử dụng chế độ nhanh cho dịch hình ảnh:    translate -l "ko" -img -f

  10. Sửa bản dịch có độ tin cậy thấp với ngưỡng tùy chỉnh: translate -l "ko" --fix -c 0.8

  11. Ví dụ chế độ gỡ lỗi: - translate -l "ko" -d: Bật ghi nhật ký gỡ lỗi.
  12. Lưu nhật ký vào tệp: translate -l "ko" -s
  13. DEBUG trên bảng điều khiển và file: translate -l "ko" -d -s
  14. Dịch mà không thêm tuyên bố dịch máy vào đầu ra: translate -l "ko" --no-disclaimer

  15. Di chuyển liên kết sổ tay cho bản dịch tiếng Hàn (cập nhật liên kết đến sổ tay đã dịch khi có):    migrate-links -l "ko"

  15. Di chuyển liên kết với chế độ dry-run (không ghi tệp):    migrate-links -l "ko" --dry-run

  16. Chỉ cập nhật liên kết khi có sổ tay đã dịch (không dùng sổ tay gốc):    migrate-links -l "ko" --no-fallback-to-original

  17. Xử lý tất cả các ngôn ngữ với thông báo xác nhận:    migrate-links -l "all"

  18. Xử lý tất cả ngôn ngữ và tự động xác nhận:    migrate-links -l "all" -y
  19. Lưu nhật ký vào tệp cho migrate-links:    migrate-links -l "ko ja" -s

  20. Cá nhân hóa khuyến cáo ngôn ngữ README bằng URL repo của bạn:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Ví dụ đánh giá

> [!WARNING]  
> **Tính năng Beta**: Chức năng đánh giá hiện đang ở giai đoạn beta. Tính năng này được phát hành để đánh giá các tài liệu đã dịch, các phương pháp đánh giá và triển khai chi tiết vẫn đang được phát triển và có thể thay đổi.

  1. Đánh giá bản dịch tiếng Hàn: evaluate -l "ko"

  2. Đánh giá với ngưỡng tin cậy tùy chỉnh: evaluate -l "ko" -c 0.8

  3. Đánh giá nhanh (chỉ dựa trên quy tắc): evaluate -l "ko" -f

  4. Đánh giá sâu (chỉ dựa trên LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc sự không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản của nó nên được coi là nguồn thông tin chính xác nhất. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->