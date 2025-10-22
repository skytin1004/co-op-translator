<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:49:38+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "th"
}
-->
# การมีส่วนร่วมกับ Co-op Translator

โปรเจกต์นี้เปิดรับการมีส่วนร่วมและข้อเสนอแนะจากทุกคน โดยส่วนใหญ่การมีส่วนร่วมจะต้องตกลงใน Contributor License Agreement (CLA) เพื่อยืนยันว่าคุณมีสิทธิ์และอนุญาตให้เราใช้ผลงานของคุณ ดูรายละเอียดเพิ่มเติมได้ที่ https://cla.opensource.microsoft.com

เมื่อคุณส่ง pull request จะมีบอท CLA ตรวจสอบโดยอัตโนมัติว่าคุณต้องกรอก CLA หรือไม่ และจะแสดงสถานะหรือคอมเมนต์ใน PR ให้คุณทำตามคำแนะนำของบอท ซึ่งคุณจะต้องทำขั้นตอนนี้เพียงครั้งเดียวสำหรับทุก repo ที่ใช้ CLA ของเรา

## การตั้งค่าสภาพแวดล้อมสำหรับการพัฒนา

สำหรับโปรเจกต์นี้ เราแนะนำให้ใช้ Poetry ในการจัดการ dependencies โดยเราใช้ `pyproject.toml` ในการจัดการ dependencies ของโปรเจกต์ ดังนั้นควรติดตั้ง dependencies ด้วย Poetry

### สร้าง virtual environment

#### ใช้ pip

```bash
python -m venv .venv
```

#### ใช้ Poetry

```bash
poetry init
```

### เปิดใช้งาน virtual environment

#### สำหรับทั้ง pip และ Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### ใช้ Poetry

```bash
poetry shell
```

### ติดตั้งแพ็กเกจและแพ็กเกจที่จำเป็น

#### ใช้ Poetry (จาก pyproject.toml)

```bash
poetry install
```

### ทดสอบแบบ manual

ก่อนจะส่ง PR ควรทดสอบฟีเจอร์แปลภาษาโดยใช้เอกสารจริง:

1. สร้างโฟลเดอร์สำหรับทดสอบใน root directory:
    ```bash
    mkdir test_docs
    ```

2. คัดลอกไฟล์ markdown และรูปภาพที่ต้องการแปลไปไว้ในโฟลเดอร์ทดสอบ เช่น:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. ติดตั้งแพ็กเกจแบบ local:
    ```bash
    pip install -e .
    ```

4. รัน Co-op Translator กับเอกสารทดสอบของคุณ:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. ตรวจสอบไฟล์ที่แปลแล้วใน `test_docs/translations` และ `test_docs/translated_images` เพื่อดูว่า:
   - คุณภาพการแปลดีหรือไม่
   - คอมเมนต์ metadata ถูกต้องหรือเปล่า
   - โครงสร้าง markdown เดิมยังอยู่ครบ
   - ลิงก์และรูปภาพใช้งานได้ถูกต้อง

การทดสอบแบบ manual นี้ช่วยให้มั่นใจว่าการเปลี่ยนแปลงของคุณใช้งานได้จริง

### ตัวแปรสภาพแวดล้อม

1. สร้างไฟล์ `.env` ใน root directory โดยคัดลอกจากไฟล์ `.env.template`
1. กรอกค่าตัวแปรสภาพแวดล้อมตามคำแนะนำ

> [!TIP]
>
> ### ตัวเลือกเพิ่มเติมสำหรับสภาพแวดล้อมการพัฒนา
>
> นอกจากการรันโปรเจกต์บนเครื่องของคุณเองแล้ว คุณยังสามารถใช้ GitHub Codespaces หรือ VS Code Dev Containers เพื่อสร้างสภาพแวดล้อมการพัฒนาแบบอื่นได้
>
> #### GitHub Codespaces
>
> คุณสามารถรันตัวอย่างนี้แบบ virtual ผ่าน GitHub Codespaces โดยไม่ต้องตั้งค่าเพิ่มเติม
>
> ปุ่มนี้จะเปิด VS Code แบบเว็บในเบราว์เซอร์ของคุณ:
>
> 1. เปิดเทมเพลต (อาจใช้เวลาสักครู่):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces"></a>
>
> #### การรันบนเครื่องโดยใช้ VS Code Dev Containers
>
> ⚠️ ตัวเลือกนี้จะใช้ได้ก็ต่อเมื่อ Docker Desktop ของคุณถูกจัดสรร RAM อย่างน้อย 16 GB หากมี RAM น้อยกว่านี้ ให้ลองใช้ [GitHub Codespaces](../..) หรือ [ตั้งค่าบนเครื่องเอง](../..)
>
> อีกทางเลือกหนึ่งคือ VS Code Dev Containers ซึ่งจะเปิดโปรเจกต์ใน VS Code บนเครื่องคุณโดยใช้ [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. เปิด Docker Desktop (ติดตั้งถ้ายังไม่มี)
> 2. เปิดโปรเจกต์:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Open in Dev Containers"></a>

### รูปแบบโค้ด

เราใช้ [Black](https://github.com/psf/black) เป็นตัวจัดรูปแบบโค้ด Python เพื่อให้โค้ดในโปรเจกต์มีมาตรฐานเดียวกัน Black จะจัดรูปแบบโค้ด Python ให้อัตโนมัติตามมาตรฐานของ Black

#### การตั้งค่า

การตั้งค่า Black อยู่ในไฟล์ `pyproject.toml` ของเรา:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### การติดตั้ง Black

คุณสามารถติดตั้ง Black ด้วย Poetry (แนะนำ) หรือ pip:

##### ใช้ Poetry

Black จะถูกติดตั้งอัตโนมัติเมื่อคุณตั้งค่าสภาพแวดล้อมการพัฒนา:
```bash
poetry install
```

##### ใช้ pip

ถ้าใช้ pip สามารถติดตั้ง Black ได้โดยตรง:
```bash
pip install black
```

#### การใช้งาน Black

##### กับ Poetry

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    poetry run black .
    ```

2. จัดรูปแบบไฟล์หรือโฟลเดอร์เฉพาะ:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### กับ pip

1. จัดรูปแบบไฟล์ Python ทั้งหมดในโปรเจกต์:
    ```bash
    black .
    ```

2. จัดรูปแบบไฟล์หรือโฟลเดอร์เฉพาะ:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> แนะนำให้ตั้งค่า editor ของคุณให้จัดรูปแบบโค้ดด้วย Black อัตโนมัติเมื่อบันทึกไฟล์ Editor ส่วนใหญ่รองรับผ่าน extension หรือ plugin

## การรัน Co-op Translator

หากต้องการรัน Co-op Translator ด้วย Poetry ในสภาพแวดล้อมของคุณ ให้ทำตามขั้นตอนนี้:

1. ไปยังโฟลเดอร์ที่ต้องการทดสอบการแปล หรือสร้างโฟลเดอร์ชั่วคราวสำหรับทดสอบ

2. รันคำสั่งนี้ โดยเปลี่ยน `-l ko` เป็นรหัสภาษาที่ต้องการแปล และใช้ `-d` เพื่อเปิดโหมด debug

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> ตรวจสอบให้แน่ใจว่าได้เปิดใช้งานสภาพแวดล้อม Poetry (poetry shell) ก่อนรันคำสั่ง

## การเพิ่มภาษาใหม่

เรายินดีรับการมีส่วนร่วมที่เพิ่มการรองรับภาษาใหม่ ก่อนเปิด PR กรุณาทำตามขั้นตอนด้านล่างเพื่อให้การตรวจสอบเป็นไปอย่างราบรื่น

1. เพิ่มภาษาใน font mapping
   - แก้ไขไฟล์ `src/co_op_translator/fonts/font_language_mappings.yml`
   - เพิ่ม entry โดยระบุ:
     - `code`: รหัสภาษาแบบ ISO (เช่น `vi`)
     - `name`: ชื่อที่อ่านเข้าใจง่าย
     - `font`: ฟอนต์ที่อยู่ใน `src/co_op_translator/fonts/` และรองรับตัวอักษรของภาษา
     - `rtl`: `true` ถ้าเป็นภาษาเขียนจากขวาไปซ้าย, ถ้าไม่ใช่ให้ใช้ `false`

2. เพิ่มไฟล์ฟอนต์ที่จำเป็น (ถ้ามี)
   - ถ้าต้องใช้ฟอนต์ใหม่ ตรวจสอบว่า license สามารถแจกจ่ายแบบ open source ได้
   - เพิ่มไฟล์ฟอนต์ใน `src/co_op_translator/fonts/`

3. ตรวจสอบแบบ local
   - รันการแปลกับตัวอย่างเล็ก ๆ (Markdown, รูปภาพ, และ notebooks ถ้ามี)
   - ตรวจสอบผลลัพธ์ว่าการแสดงผลถูกต้อง รวมถึงฟอนต์และการจัด layout แบบ RTL ถ้ามี

4. อัปเดตเอกสาร
   - ตรวจสอบว่าภาษานั้นปรากฏใน `getting_started/supported-languages.md`
   - ไม่ต้องแก้ไข `README_languages_template.md` เพราะไฟล์นี้ถูกสร้างจากรายการภาษา

5. เปิด PR
   - อธิบายภาษาที่เพิ่มและข้อควรพิจารณาเรื่องฟอนต์/ลิขสิทธิ์
   - แนบภาพหน้าจอของผลลัพธ์ที่แสดงผลถ้าเป็นไปได้

ตัวอย่าง entry ใน YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### ทดสอบภาษาใหม่

คุณสามารถทดสอบภาษาใหม่โดยรันคำสั่งนี้:

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

## ผู้ดูแลโปรเจกต์

### รูปแบบข้อความ commit และกลยุทธ์การ merge

เพื่อความสม่ำเสมอและชัดเจนในประวัติ commit ของโปรเจกต์ เราใช้รูปแบบข้อความ commit เฉพาะ **สำหรับข้อความ commit สุดท้าย** เมื่อใช้กลยุทธ์ **Squash and Merge**

เมื่อ pull request (PR) ถูก merge, commit ทั้งหมดจะถูกรวมเป็น commit เดียว ข้อความ commit สุดท้ายควรใช้รูปแบบด้านล่างเพื่อให้ประวัติสะอาดและสม่ำเสมอ

#### รูปแบบข้อความ commit (สำหรับ squash and merge)

เราใช้รูปแบบนี้สำหรับข้อความ commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: ระบุประเภทของ commit โดยใช้ประเภทต่อไปนี้:
  - `Docs`: สำหรับอัปเดตเอกสาร
  - `Build`: สำหรับการเปลี่ยนแปลงที่เกี่ยวกับระบบ build หรือ dependencies รวมถึงไฟล์ config, CI workflow หรือ Dockerfile
  - `Core`: สำหรับการแก้ไขฟีเจอร์หลักของโปรเจกต์ โดยเฉพาะไฟล์ใน `src/co_op_translator/core`

- **description**: สรุปการเปลี่ยนแปลงอย่างกระชับ
- **PR number**: หมายเลข pull request ที่เกี่ยวข้องกับ commit

**ตัวอย่าง**:

- `Docs: Update installation instructions for clarity (#50)`
- `Core: Improve handling of image translation (#60)`

> [!NOTE]
> ขณะนี้ prefix **`Docs`**, **`Core`**, และ **`Build`** จะถูกเพิ่มอัตโนมัติในชื่อ PR ตาม label ที่ใช้กับ source code ที่แก้ไข ดังนั้นถ้า label ถูกต้อง คุณไม่จำเป็นต้องแก้ไขชื่อ PR เอง เพียงตรวจสอบให้แน่ใจว่าทุกอย่างถูกต้องและ prefix ถูกสร้างมาเหมาะสม

#### กลยุทธ์การ merge

เราใช้ **Squash and Merge** เป็นกลยุทธ์หลักสำหรับ pull request วิธีนี้ช่วยให้ commit message เป็นไปตามรูปแบบที่กำหนด แม้แต่ commit ย่อย ๆ ก็จะถูกรวม

**เหตุผล**:

- ประวัติโปรเจกต์สะอาดและเป็นเส้นตรง
- ข้อความ commit สม่ำเสมอ
- ลด commit เล็ก ๆ ที่ไม่สำคัญ (เช่น "fix typo")

เมื่อ merge ให้ตรวจสอบว่าข้อความ commit สุดท้ายเป็นไปตามรูปแบบที่กำหนด

**ตัวอย่าง Squash and Merge**
ถ้า PR มี commit เหล่านี้:

- `fix typo`
- `update README`
- `adjust formatting`

ควรถูกรวมเป็น:
`Docs: Improve documentation clarity and formatting (#65)`

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้เอกสารแปลนี้