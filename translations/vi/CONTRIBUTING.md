<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:57:39+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "vi"
}
-->
# Đóng góp cho Co-op Translator

Dự án này hoan nghênh mọi đóng góp và ý kiến. Hầu hết các đóng góp yêu cầu bạn đồng ý với Thỏa thuận cấp phép cho người đóng góp (CLA), xác nhận rằng bạn có quyền và thực sự cấp cho chúng tôi quyền sử dụng đóng góp của bạn. Để biết chi tiết, hãy truy cập https://cla.opensource.microsoft.com.

Khi bạn gửi pull request, một bot CLA sẽ tự động xác định xem bạn có cần cung cấp CLA hay không và sẽ đánh dấu PR phù hợp (ví dụ: kiểm tra trạng thái, bình luận). Chỉ cần làm theo hướng dẫn của bot. Bạn chỉ cần thực hiện việc này một lần cho tất cả các kho sử dụng CLA của chúng tôi.

## Thiết lập môi trường phát triển

Để thiết lập môi trường phát triển cho dự án này, chúng tôi khuyến nghị sử dụng Poetry để quản lý các gói phụ thuộc. Chúng tôi dùng `pyproject.toml` để quản lý các gói phụ thuộc của dự án, vì vậy bạn nên dùng Poetry để cài đặt các gói này.

### Tạo môi trường ảo

#### Sử dụng pip

```bash
python -m venv .venv
```

#### Sử dụng Poetry

```bash
poetry init
```

### Kích hoạt môi trường ảo

#### Dùng cho cả pip và Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Sử dụng Poetry

```bash
poetry shell
```

### Cài đặt gói và các gói cần thiết

#### Sử dụng Poetry (từ pyproject.toml)

```bash
poetry install
```

### Kiểm thử thủ công

Trước khi gửi PR, bạn nên kiểm thử chức năng dịch với tài liệu thực tế:

1. Tạo một thư mục kiểm thử ở thư mục gốc:
    ```bash
    mkdir test_docs
    ```

2. Sao chép một số tài liệu markdown và hình ảnh bạn muốn dịch vào thư mục kiểm thử. Ví dụ:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Cài đặt gói cục bộ:
    ```bash
    pip install -e .
    ```

4. Chạy Co-op Translator trên các tài liệu kiểm thử của bạn:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Kiểm tra các file đã dịch trong `test_docs/translations` và `test_docs/translated_images` để xác nhận:
   - Chất lượng bản dịch
   - Các bình luận metadata chính xác
   - Cấu trúc markdown gốc được giữ nguyên
   - Liên kết và hình ảnh hoạt động đúng

Việc kiểm thử thủ công này giúp đảm bảo các thay đổi của bạn hoạt động tốt trong thực tế.

### Biến môi trường

1. Tạo file `.env` ở thư mục gốc bằng cách sao chép file mẫu `.env.template` được cung cấp.
1. Điền các biến môi trường theo hướng dẫn.

> [!TIP]
>
> ### Các lựa chọn môi trường phát triển bổ sung
>
> Ngoài việc chạy dự án cục bộ, bạn cũng có thể sử dụng GitHub Codespaces hoặc VS Code Dev Containers để thiết lập môi trường phát triển thay thế.
>
> #### GitHub Codespaces
>
> Bạn có thể chạy các ví dụ này trực tuyến bằng GitHub Codespaces mà không cần cài đặt hay thiết lập thêm.
>
> Nút sau sẽ mở một phiên bản VS Code trên trình duyệt của bạn:
>
> 1. Mở template (có thể mất vài phút):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### Chạy cục bộ bằng VS Code Dev Containers
>
> ⚠️ Tùy chọn này chỉ hoạt động nếu Docker Desktop của bạn được cấp ít nhất 16 GB RAM. Nếu bạn có ít hơn 16 GB RAM, hãy thử [tùy chọn GitHub Codespaces](../..) hoặc [thiết lập cục bộ](../..).
>
> Một lựa chọn liên quan là VS Code Dev Containers, sẽ mở dự án trong VS Code cục bộ của bạn bằng [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Khởi động Docker Desktop (cài đặt nếu chưa có)
> 2. Mở dự án:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>


### Phong cách mã nguồn

Chúng tôi sử dụng [Black](https://github.com/psf/black) làm trình định dạng mã Python để duy trì phong cách mã nhất quán cho toàn dự án. Black là trình định dạng mã tự động, giúp mã Python tuân thủ phong cách của Black.

#### Cấu hình

Cấu hình Black được chỉ định trong `pyproject.toml` của chúng tôi:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Cài đặt Black

Bạn có thể cài đặt Black bằng Poetry (khuyến nghị) hoặc pip:

##### Sử dụng Poetry

Black sẽ được cài đặt tự động khi bạn thiết lập môi trường phát triển:
```bash
poetry install
```

##### Sử dụng pip

Nếu bạn dùng pip, có thể cài đặt Black trực tiếp:
```bash
pip install black
```

#### Sử dụng Black

##### Với Poetry

1. Định dạng tất cả file Python trong dự án:
    ```bash
    poetry run black .
    ```

2. Định dạng một file hoặc thư mục cụ thể:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Với pip

1. Định dạng tất cả file Python trong dự án:
    ```bash
    black .
    ```

2. Định dạng một file hoặc thư mục cụ thể:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Chúng tôi khuyến nghị bạn thiết lập trình soạn thảo để tự động định dạng mã với Black khi lưu. Hầu hết các trình soạn thảo hiện đại đều hỗ trợ thông qua extension hoặc plugin.

## Chạy Co-op Translator

Để chạy Co-op Translator bằng Poetry trong môi trường của bạn, hãy làm theo các bước sau:

1. Di chuyển đến thư mục bạn muốn kiểm thử dịch hoặc tạo một thư mục tạm để kiểm thử.

2. Thực hiện lệnh sau. Thay `-l ko` bằng mã ngôn ngữ bạn muốn dịch sang. Cờ `-d` dùng để bật chế độ debug.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Đảm bảo môi trường Poetry của bạn đã được kích hoạt (poetry shell) trước khi chạy lệnh.

## Đóng góp ngôn ngữ mới

Chúng tôi hoan nghênh các đóng góp bổ sung hỗ trợ ngôn ngữ mới. Trước khi mở PR, hãy hoàn thành các bước dưới đây để quá trình kiểm duyệt diễn ra suôn sẻ.

1. Thêm ngôn ngữ vào ánh xạ font
   - Sửa file `src/co_op_translator/fonts/font_language_mappings.yml`
   - Thêm một mục với:
     - `code`: Mã ngôn ngữ dạng ISO (ví dụ: `vi`)
     - `name`: Tên hiển thị thân thiện
     - `font`: Một font có sẵn trong `src/co_op_translator/fonts/` hỗ trợ bộ ký tự đó
     - `rtl`: `true` nếu là ngôn ngữ viết từ phải sang trái, ngược lại là `false`

2. Thêm file font cần thiết (nếu có)
   - Nếu cần font mới, hãy kiểm tra giấy phép có phù hợp để phân phối mã nguồn mở không
   - Thêm file font vào `src/co_op_translator/fonts/`

3. Kiểm thử cục bộ
   - Chạy dịch cho một mẫu nhỏ (Markdown, hình ảnh, và notebook nếu cần)
   - Kiểm tra đầu ra hiển thị đúng, bao gồm font và bố cục RTL nếu có

4. Cập nhật tài liệu
   - Đảm bảo ngôn ngữ xuất hiện trong `getting_started/supported-languages.md`
   - Không cần thay đổi `README_languages_template.md`; file này được tạo tự động từ danh sách hỗ trợ

5. Mở PR
   - Mô tả ngôn ngữ đã thêm và các vấn đề về font/giấy phép nếu có
   - Đính kèm ảnh chụp màn hình đầu ra nếu có thể

Ví dụ mục YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Kiểm thử ngôn ngữ mới

Bạn có thể kiểm thử ngôn ngữ mới bằng cách chạy lệnh sau:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## Người duy trì dự án

### Định dạng commit và chiến lược gộp

Để đảm bảo lịch sử commit của dự án nhất quán và rõ ràng, chúng tôi tuân theo định dạng commit cụ thể **cho commit cuối cùng** khi sử dụng chiến lược **Squash and Merge**.

Khi một pull request (PR) được gộp, các commit riêng lẻ sẽ được gộp thành một commit duy nhất. Commit cuối cùng nên tuân theo định dạng dưới đây để giữ lịch sử sạch sẽ và nhất quán.

#### Định dạng commit (cho squash and merge)

Chúng tôi sử dụng định dạng sau cho commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Chỉ loại commit. Chúng tôi dùng các loại sau:
  - `Docs`: Cập nhật tài liệu.
  - `Build`: Thay đổi liên quan đến hệ thống build hoặc các gói phụ thuộc, bao gồm cập nhật file cấu hình, workflow CI, hoặc Dockerfile.
  - `Core`: Sửa đổi chức năng cốt lõi của dự án, đặc biệt là các file trong thư mục `src/co_op_translator/core`.

- **description**: Tóm tắt ngắn gọn về thay đổi.
- **PR number**: Số pull request liên quan đến commit.

**Ví dụ**:

- `Docs: Cập nhật hướng dẫn cài đặt cho rõ ràng hơn (#50)`
- `Core: Cải thiện xử lý dịch hình ảnh (#60)`

> [!NOTE]
> Hiện tại, các tiền tố **`Docs`**, **`Core`**, và **`Build`** sẽ được tự động thêm vào tiêu đề PR dựa trên nhãn áp dụng cho mã nguồn đã sửa đổi. Miễn là nhãn đúng được áp dụng, bạn thường không cần cập nhật tiêu đề PR thủ công. Bạn chỉ cần kiểm tra mọi thứ đã đúng và tiền tố đã được tạo phù hợp.

#### Chiến lược gộp

Chúng tôi sử dụng **Squash and Merge** làm chiến lược mặc định cho pull request. Chiến lược này đảm bảo commit tuân theo định dạng của chúng tôi, ngay cả khi các commit riêng lẻ không tuân theo.

**Lý do**:

- Lịch sử dự án sạch, tuyến tính.
- Nhất quán về định dạng commit.
- Giảm nhiễu từ các commit nhỏ (ví dụ: "fix typo").

Khi gộp, hãy đảm bảo commit cuối cùng tuân theo định dạng commit đã mô tả ở trên.

**Ví dụ về Squash and Merge**
Nếu một PR có các commit sau:

- `fix typo`
- `update README`
- `adjust formatting`

Chúng sẽ được gộp thành:
`Docs: Cải thiện độ rõ ràng và định dạng tài liệu (#65)`

---

**Tuyên bố miễn trừ trách nhiệm**:
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ bản địa nên được xem là nguồn tham khảo chính thức. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc diễn giải sai nào phát sinh từ việc sử dụng bản dịch này.