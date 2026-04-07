# Co-op Translator

_ช่วยให้อัตโนมัติและดูแลการแปลสำหรับเนื้อหา GitHub ด้านการศึกษาของคุณในหลายภาษาอย่างง่ายดายในขณะที่โปรเจกต์ของคุณพัฒนาไป_

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

### 🌐 รองรับหลายภาษา

#### สนับสนุนโดย [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](./README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **ต้องการโคลนในเครื่องไหม?**
>
> ที่เก็บนี้ประกอบด้วยการแปลกว่า 50 ภาษา ซึ่งทำให้ขนาดดาวน์โหลดเพิ่มขึ้นอย่างมาก เพื่อโคลนโดยไม่รวมการแปล ให้ใช้ sparse checkout:
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
> วิธีนี้จะให้ทุกอย่างที่คุณต้องการเพื่อทำหลักสูตรให้เสร็จด้วยความเร็วดาวน์โหลดที่เร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator.svg?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ภาพรวม

**Co-op Translator** ช่วยให้คุณแปลเนื้อหา GitHub ด้านการศึกษาของคุณเป็นหลายภาษาได้อย่างง่ายดาย
เมื่อคุณอัปเดตไฟล์ Markdown รูปภาพ หรือโน้ตบุ๊ก การแปลจะถูกซิงโครไนซ์โดยอัตโนมัติ เพื่อทำให้มั่นใจว่าเนื้อหาของคุณถูกต้องและทันสมัยสำหรับผู้เรียนทั่วโลก

ตัวอย่างวิธีจัดระเบียบเนื้อหาที่แปล:

![Example](../../imgs/translation-ex.png)

## วิธีจัดการสถานะการแปล

Co-op Translator จัดการเนื้อหาที่แปลเป็น **ซอฟต์แวร์ที่มีเวอร์ชัน**  
ไม่ใช่ไฟล์แบบคงที่

เครื่องมือติดตามสถานะของ Markdown, รูปภาพ และโน้ตบุ๊กที่ถูกแปล
โดยใช้ **เมตาดาต้าที่จำกัดตามภาษา**

ดีไซน์นี้ช่วยให้ Co-op Translator:

- ตรวจจับการแปลที่ล้าสมัยได้อย่างน่าเชื่อถือ
- จัดการ Markdown, รูปภาพ และโน้ตบุ๊กอย่างเป็นระบบ
- ปรับขนาดได้อย่างปลอดภัยในที่เก็บขนาดใหญ่และเคลื่อนไหวรวดเร็วหลายภาษา

ด้วยการจำลองการแปลเป็นซอฟต์แวร์ที่บริหารจัดการ
เวิร์กโฟลว์การแปลจึงเข้ากันได้อย่างเป็นธรรมชาติกับ
แนวปฏิบัติการจัดการการพึ่งพาและซอฟต์แวร์รุ่นใหม่

→ [วิธีจัดการสถานะการแปล](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


## เริ่มต้นอย่างรวดเร็ว

```bash
# สร้างและเปิดใช้งานสภาพแวดล้อมเสมือน (แนะนำ)
python -m venv .venv
# วินโดวส์
.venv\Scripts\activate
# แมคโอเอส/ลินุกซ์
source .venv/bin/activate
# ติดตั้งแพ็กเกจ
pip install co-op-translator
# แปลภาษา
translate -l "ko ja fr" -md
```

Docker:

```bash
# ดึงภาพสาธารณะที่ GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# รันโดยมีโฟลเดอร์ปัจจุบันที่เมานต์และให้ .env (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## การตั้งค่าขั้นต่ำ

1. ตรวจสอบว่าคุณมีเวอร์ชัน Python ที่รองรับ (ปัจจุบันคือ 3.10-3.12) ใน poetry (pyproject.toml) จะจัดการให้อัตโนมัติ
2. สร้างไฟล์ `.env` โดยใช้เทมเพลต: [.env.template](../../.env.template)
3. ตั้งค่าผู้ให้บริการ LLM หนึ่งราย (Azure OpenAI หรือ OpenAI)
4. (ไม่บังคับ) สำหรับการแปลรูปภาพ (`-img`) ตั้งค่า Azure AI Vision
5. (ไม่บังคับ) คุณสามารถตั้งค่าชุดบัญชีรับรองหลายชุดโดยคัดลอกตัวแปรพร้อมคำต่อท้ายเช่น `_1`, `_2` เป็นต้น ตัวแปรทั้งหมดในชุดต้องมีคำต่อท้ายเหมือนกัน
6. (แนะนำ) ล้างการแปลที่มีอยู่ก่อนเพื่อหลีกเลี่ยงความขัดแย้ง (เช่น `translations/`)
7. (แนะนำ) เพิ่มส่วนการแปลใน README ของคุณโดยใช้ [เทมเพลตภาษา README](./getting_started/README_languages_template.md)
8. ดู: [ตั้งค่า Azure AI](./getting_started/set-up-azure-ai.md)

## การใช้งาน

แปลทุกประเภทที่รองรับ:

```bash
translate -l "ko ja"
```

แค่ Markdown:

```bash
translate -l "de" -md
```

Markdown + รูปภาพ:

```bash
translate -l "pt" -md -img
```

เฉพาะโน้ตบุ๊ก:

```bash
translate -l "zh" -nb
```

ธงเพิ่มเติม: [เอกสารอ้างอิงคำสั่ง](./getting_started/command-reference.md)

## คุณสมบัติ

- แปลอัตโนมัติสำหรับ Markdown, โน้ตบุ๊ก และรูปภาพ
- เก็บการแปลให้สอดคล้องกับการเปลี่ยนแหล่งที่มา
- ทำงานได้ทั้งในเครื่อง (CLI) หรือใน CI (GitHub Actions)
- ใช้ Azure OpenAI หรือ OpenAI; รองรับ Azure AI Vision สำหรับรูปภาพเสริม
- รักษารูปแบบและโครงสร้าง Markdown

## เอกสาร

- [คู่มือ Command-line](./getting_started/command-line-guide/command-line-guide.md)
- [คู่มือ GitHub Actions (ที่เก็บสาธารณะ & ความลับมาตรฐาน)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [คู่มือ GitHub Actions (ที่เก็บองค์กร Microsoft & การตั้งค่าในระดับองค์กร)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [เทมเพลตภาษา README](./getting_started/README_languages_template.md)
- [ภาษาที่รองรับ](./getting_started/supported-languages.md)
- [การร่วมพัฒนา](./CONTRIBUTING.md)
- [การแก้ปัญหา](./getting_started/troubleshooting.md)

### คู่มือเฉพาะ Microsoft
> [!NOTE]
> สำหรับผู้ดูแลที่เก็บ Microsoft “For Beginners” เท่านั้น

- [อัปเดตรายการหลักสูตรอื่น (สำหรับที่เก็บ MS Beginners เท่านั้น)](./getting_started/update-other-courses.md)

## สนับสนุนเราและส่งเสริมการเรียนรู้ระดับโลก

มาร่วมกันปฏิวัติวิธีการแชร์เนื้อหาด้านการศึกษาทั่วโลก! ให้ [Co-op Translator](https://github.com/azure/co-op-translator) ⭐ บน GitHub และสนับสนุนพันธกิจของเราในการทำลายอุปสรรคทางภาษาในการเรียนรู้และเทคโนโลยี ความสนใจและการมีส่วนร่วมของคุณมีผลกระทบอย่างมาก! ยินดีรับทั้งการมีส่วนร่วมของโค้ดและข้อเสนอแนะคุณสมบัติอยู่เสมอ

### สำรวจเนื้อหาการศึกษาของ Microsoft ในภาษาของคุณ

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

## วิดีโอการนำเสนอ

👉 คลิกภาพด้านล่างเพื่อดูบน YouTube

- **เปิดที่ Microsoft**: บทนำสั้น 18 นาทีและคู่มือด่วนวิธีใช้ Co-op Translator

  [![Open at Microsoft](../../imgs/open-ms-thumbnail.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## การร่วมพัฒนา

โปรเจกต์นี้ยินดีรับการมีส่วนร่วมและข้อเสนอแนะ สนใจร่วมพัฒนา Azure Co-op Translator ไหม? กรุณาอ่าน [CONTRIBUTING.md](./CONTRIBUTING.md) ของเราเพื่อดูแนวทางการช่วยทำให้ Co-op Translator เข้าถึงได้ง่ายขึ้น

## ผู้ร่วมพัฒนา
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## ระเบียบปฏิบัติ

โครงการนี้ได้นำ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) มาใช้
สำหรับข้อมูลเพิ่มเติมดูที่ [คำถามที่พบบ่อยเกี่ยวกับ Code of Conduct](https://opensource.microsoft.com/codeofconduct/faq/) หรือติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือความคิดเห็นเพิ่มเติม

## ปัญญาประดิษฐ์ที่รับผิดชอบ

Microsoft มุ่งมั่นที่จะช่วยลูกค้าใช้ผลิตภัณฑ์ AI ของเราอย่างรับผิดชอบ แบ่งปันประสบการณ์ และสร้างความสัมพันธ์ที่เชื่อถือได้ผ่านเครื่องมือต่าง ๆ เช่น Transparency Notes และ Impact Assessments ทรัพยากรเหล่านี้ส่วนใหญ่สามารถพบได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)
แนวทางของ Microsoft ในการใช้ AI อย่างรับผิดชอบตั้งอยู่บนหลักการ AI ของเรา ได้แก่ ความเป็นธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความปลอดภัย ความครอบคลุม ความโปร่งใส และความรับผิดชอบ

แบบจำลองภาษาธรรมชาติ ภาพ และเสียงขนาดใหญ่—เช่นแบบจำลองที่ใช้ในตัวอย่างนี้—อาจมีพฤติกรรมที่ไม่เป็นธรรม ไม่น่าเชื่อถือ หรือก้าวร้าว ซึ่งอาจก่อให้เกิดอันตราย กรุณาปรึกษา [หมายเหตุความโปร่งใสของบริการ Azure OpenAI](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อรับทราบความเสี่ยงและข้อจำกัด

แนวทางแนะนำในการลดความเสี่ยงเหล่านี้คือ การใส่ระบบความปลอดภัยลงในสถาปัตยกรรมของคุณเพื่อสามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตรายได้ [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้การปกป้องอิสระที่สามารถตรวจจับเนื้อหาที่สร้างโดยผู้ใช้หรือ AI ที่เป็นอันตรายในแอปพลิเคชันและบริการ Azure AI Content Safety มี API สำหรับข้อความและภาพที่ช่วยให้คุณสามารถตรวจจับเนื้อหาที่เป็นอันตรายได้ เรายังมี Content Safety Studio แบบโต้ตอบที่ให้คุณดู สำรวจ และทดลองโค้ดตัวอย่างสำหรับการตรวจจับเนื้อหาที่เป็นอันตรายในหลากหลายรูปแบบ เอกสาร [เริ่มต้นอย่างรวดเร็ว](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ต่อไปนี้จะนำทางคุณในการส่งคำขอไปยังบริการ

อีกหนึ่งประเด็นที่ควรพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน ด้วยแอปพลิเคชันที่รองรับหลายรูปแบบและหลายแบบจำลอง เราถือว่าประสิทธิภาพหมายถึงระบบทำงานได้ตามที่คุณและผู้ใช้ของคุณคาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตราย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมของคุณจึงมีความสำคัญโดยใช้ [คุณภาพการสร้างและเมตริกความเสี่ยงและความปลอดภัย](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาของคุณโดยใช้ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ไม่ว่าจะเป็นชุดข้อมูลทดสอบหรือเป้าหมาย การสร้างสรรค์จาก AI ของคุณจะถูกวัดอย่างเป็นปริมาณด้วยตัวประเมินมาตรฐานหรือตัวประเมินที่กำหนดเองตามที่คุณเลือก เพื่อเริ่มต้นใช้ prompt flow sdk ในการประเมินระบบของคุณ คุณสามารถติดตาม [คู่มือเริ่มต้นอย่างรวดเร็ว](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) เมื่อคุณดำเนินการประเมินเสร็จแล้ว คุณสามารถ [ดูผลลัพธ์ใน Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ได้

## เครื่องหมายการค้า

โครงการนี้อาจมีเครื่องหมายการค้าหรือโลโก้สำหรับโครงการ ผลิตภัณฑ์ หรือบริการ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft อย่างถูกต้องนั้นต้องปฏิบัติตามและสอดคล้องกับ
[แนวทางการใช้เครื่องหมายการค้าและแบรนด์ของ Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่แก้ไขของโครงการนี้ต้องไม่ทำให้เกิดความสับสนหรือสร้างความหมายว่าสนับสนุนโดย Microsoft
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใด ๆ ต้องเป็นไปตามนโยบายของบุคคลที่สามนั้น

## รับความช่วยเหลือ

หากคุณติดปัญหาหรือมีคำถามใด ๆ เกี่ยวกับการสร้างแอป AI เข้าร่วม:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

หากคุณมีข้อเสนอแนะเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดขณะพัฒนา โปรดเข้าไปที่:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) ในขณะที่เรามุ่งมั่นเพื่อความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือตัวไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่ถูกต้อง สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์เป็นการดีที่สุด เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->