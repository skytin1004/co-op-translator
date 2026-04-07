# Co-op Translator

_แปลภาษาและดูแลการแปลเนื้อหาการศึกษาใน GitHub ของคุณให้รองรับหลายภาษาได้อย่างง่ายดายขณะที่โปรเจกต์ของคุณเติบโตขึ้น_

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

> **ต้องการโคลนแบบ Local?**
>
> รีโพสนี้รวมการแปลกว่า 50 ภาษา ซึ่งทำให้ขนาดดาวน์โหลดเพิ่มขึ้นอย่างมาก หากต้องการโคลนโดยไม่ดาวน์โหลดการแปล ใช้ sparse checkout:
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
> สิ่งนี้จะช่วยให้คุณมีทุกสิ่งที่ต้องใช้เพื่อจบคอร์สด้วยความเร็วดาวน์โหลดที่เร็วขึ้นมาก
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

[![GitHub watchers](https://img.shields.io/github/watchers/azure/co-op-translator.svg?style=social&label=Watch)](https://GitHub.com/azure/co-op-translator/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/azure/co-op-translator.svg?style=social&label=Fork)](https://GitHub.com/azure/co-op-translator/network/)
[![GitHub stars](https://img.shields.io/github/stars/azure/co-op-translator?style=social&label=Star)](https://GitHub.com/azure/co-op-translator/stargazers/)

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=Github%20Codespaces&message=Open&color=24292F&logo=github)](https://codespaces.new/azure/co-op-translator)

## ภาพรวม

**Co-op Translator** ช่วยแปลเนื้อหาการศึกษาใน GitHub ของคุณเป็นหลายภาษาได้อย่างง่ายดาย  
เมื่อคุณอัปเดตไฟล์ Markdown รูปภาพ หรือโน้ตบุ๊ก การแปลจะถูกซิงค์โดยอัตโนมัติ เพื่อให้เนื้อหาของคุณถูกต้องและทันสมัยสำหรับผู้เรียนทั่วโลก

ตัวอย่างการจัดระเบียบเนื้อหาการแปล:

![Example](../../translated_images/th/translation-ex.0c8aa6a7ee0aad2b.webp)

## วิธีการจัดการสถานะการแปล

Co-op Translator จัดการเนื้อหาการแปลเป็น **ซอฟต์แวร์อาร์ติแฟกต์ที่มีเวอร์ชัน**  
ไม่ใช่ไฟล์แบบคงที่

เครื่องมือตรวจสอบสถานะ Markdown, รูปภาพ และโน้ตบุ๊กที่แปลแล้ว
โดยใช้ **เมตาดาต้าที่กำหนดตามภาษา**

การออกแบบนี้ช่วยให้ Co-op Translator:

- ตรวจจับการแปลที่ล้าสมัยได้อย่างน่าเชื่อถือ
- จัดการ Markdown รูปภาพ และโน้ตบุ๊กอย่างสม่ำเสมอ
- ขยายขนาดได้อย่างปลอดภัยในรีโพสที่ใหญ่และเคลื่อนไหวเร็วหลายภาษา

โดยการจำลองการแปลเป็นอาร์ติแฟกต์ที่จัดการได้  
เวิร์กโฟลว์การแปลจึงสอดคล้องกับการจัดการ  
การพึ่งพาซอฟต์แวร์และอาร์ติแฟกต์ในยุคสมัยใหม่อย่างเป็นธรรมชาติ

→ [วิธีการจัดการสถานะการแปล](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/rethinking-documentation-translation-treating-translations-as-versioned-software/4491755)


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
# แปล
translate -l "ko ja fr" -md
```

Docker:

```bash
# ดึงภาพสาธารณะจาก GHCR
docker pull ghcr.io/azure/co-op-translator:latest
# รันพร้อมเมานต์โฟลเดอร์ปัจจุบันและ .env ที่จัดเตรียมไว้ (Bash/Zsh)
docker run --rm -it --env-file .env -v "${PWD}:/work" ghcr.io/azure/co-op-translator:latest -l "ko ja fr" -md
```

## การตั้งค่าขั้นต่ำ

1. ตรวจสอบว่าคุณใช้ Python เวอร์ชันที่รองรับ (ปัจจุบันคือ 3.10-3.12) ใน poetry (pyproject.toml) จะจัดการให้อัตโนมัติ
2. สร้างไฟล์ `.env` โดยใช้เทมเพลต: [.env.template](../../.env.template)
3. ตั้งค่าโปรไวเดอร์ LLM อย่างน้อยหนึ่งตัว (Azure OpenAI หรือ OpenAI)
4. (ไม่จำเป็น) สำหรับการแปลรูปภาพ (`-img`) ตั้งค่า Azure AI Vision
5. (ไม่จำเป็น) คุณสามารถตั้งค่าชุดข้อมูลรับรองหลายชุดโดยทำซ้ำตัวแปรโดยมีคำต่อท้าย เช่น `_1`, `_2` เป็นต้น ตัวแปรทั้งหมดในชุดต้องใช้คำต่อท้ายเดียวกัน
6. (แนะนำ) ลบการแปลก่อนหน้าเพื่อหลีกเลี่ยงความขัดแย้ง (เช่น `translations/`)
7. (แนะนำ) เพิ่มส่วนการแปลใน README ของคุณโดยใช้ [เทมเพลตภาษา README](./getting_started/README_languages_template.md)
8. ดูเพิ่มเติม: [ตั้งค่า Azure AI](./getting_started/set-up-azure-ai.md)

## การใช้งาน

แปลทุกชนิดที่รองรับ:

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

แค่โน้ตบุ๊ก:

```bash
translate -l "zh" -nb
```

ดูแฟลกเพิ่มเติม: [คำอ้างอิงคำสั่ง](./getting_started/command-reference.md)

## คุณสมบัติ

- แปลอัตโนมัติสำหรับ Markdown โน้ตบุ๊ก และรูปภาพ
- รักษาการแปลให้สอดคล้องกับการเปลี่ยนแปลงต้นฉบับ
- ทำงานได้ทั้งในเครื่อง (CLI) หรือใน CI (GitHub Actions)
- ใช้ Azure OpenAI หรือ OpenAI; รองรับ Azure AI Vision สำหรับรูปภาพ
- รักษารูปแบบและโครงสร้าง Markdown

## เอกสาร

- [คู่มือบรรทัดคำสั่ง](./getting_started/command-line-guide/command-line-guide.md)
- [คู่มือ GitHub Actions (รีโพสสาธารณะ & ความลับมาตรฐาน)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [คู่มือ GitHub Actions (รีโพสองค์กร Microsoft & การตั้งค่าองค์กร)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [เทมเพลตภาษา README](./getting_started/README_languages_template.md)
- [ภาษาที่รองรับ](./getting_started/supported-languages.md)
- [การมีส่วนร่วม](./CONTRIBUTING.md)
- [แก้ไขปัญหา](./getting_started/troubleshooting.md)

### คู่มือสำหรับ Microsoft โดยเฉพาะ
> [!NOTE]
> สำหรับผู้ดูแลรีโพส “For Beginners” ของ Microsoft เท่านั้น

- [อัปเดตรายการ “คอร์สอื่นๆ” (สำหรับรีโพส MS Beginners เท่านั้น)](./getting_started/update-other-courses.md)

## สนับสนุนเราและส่งเสริมการเรียนรู้ทั่วโลก

มาร่วมเปลี่ยนแปลงวิธีการแบ่งปันเนื้อหาการศึกษาทั่วโลก! ให้ดาว [Co-op Translator](https://github.com/azure/co-op-translator) บน GitHub เพื่อสนับสนุนภารกิจของเราในการทำลายอุปสรรคด้านภาษาในการเรียนรู้และเทคโนโลยี ความสนใจและการมีส่วนร่วมของคุณมีผลกระทบอย่างมาก! ยินดีรับการร่วมเขียนโค้ดและข้อเสนอแนะฟีเจอร์เสมอ

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

👉 คลิกภาพด้านล่างเพื่อชมบน YouTube

- **Open at Microsoft**: บทแนะนำสั้น 18 นาทีและคู่มือด่วนเกี่ยวกับการใช้ Co-op Translator

  [![Open at Microsoft](../../translated_images/th/open-ms-thumbnail.946b356b89bc5f0e.webp)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## การมีส่วนร่วม

โปรเจกต์นี้ยินดีต้อนรับการมีส่วนร่วมและข้อเสนอแนะ สนใจมีส่วนร่วมใน Azure Co-op Translator? โปรดดูที่ [CONTRIBUTING.md](./CONTRIBUTING.md) เพื่อเรียนรู้วิธีช่วยทำให้ Co-op Translator เข้าถึงได้มากขึ้น

## ผู้ร่วมพัฒนา
[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## มาตรฐานการปฏิบัติ

โครงการนี้ได้นำ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) มาใช้  
สำหรับข้อมูลเพิ่มเติมโปรดดูที่ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) หรือ  
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือความคิดเห็นเพิ่มเติม

## ปัญญาประดิษฐ์ที่รับผิดชอบ

Microsoft มุ่งมั่นที่จะช่วยให้ลูกค้าใช้ผลิตภัณฑ์ AI ของเราอย่างรับผิดชอบ แบ่งปันประสบการณ์ของเรา และสร้างพันธมิตรที่มีความไว้วางใจผ่านเครื่องมือต่างๆ เช่น Transparency Notes และ Impact Assessments แหล่งข้อมูลเหล่านี้สามารถดูเพิ่มเติมได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)  
แนวทางของ Microsoft ในการใช้ AI อย่างรับผิดชอบนั้นตั้งอยู่บนหลักการ AI ของเราที่เน้นเรื่องความยุติธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความมั่นคง ความครอบคลุม ความโปร่งใส และความรับผิดชอบ

โมเดลใหญ่ของภาษา ภาพ และเสียงตามธรรมชาติ — เช่นที่ใช้ในตัวอย่างนี้ — อาจมีพฤติกรรมที่ไม่ยุติธรรมหรือไม่น่าเชื่อถือ หรืออาจทำให้เกิดความผิดหวัง ส่งผลให้เกิดความเสียหายได้ โปรดตรวจสอบ [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อรับทราบเกี่ยวกับความเสี่ยงและข้อจำกัด

วิธีที่แนะนำเพื่อบรรเทาความเสี่ยงเหล่านี้คือต้องมีระบบความปลอดภัยในสถาปัตยกรรมของคุณที่สามารถตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) ให้ชั้นป้องกันอิสระ ที่สามารถตรวจจับเนื้อหาที่เป็นอันตรายซึ่งสร้างโดยผู้ใช้และ AI ในแอปพลิเคชันและบริการ Azure AI Content Safety มี API สำหรับข้อความและภาพที่ช่วยตรวจจับเนื้อหาที่เป็นอันตราย นอกจากนี้เรายังมี Content Safety Studio แบบโต้ตอบที่ช่วยให้คุณดู สำรวจ และทดลองโค้ดตัวอย่างสำหรับการตรวจจับเนื้อหาที่เป็นอันตรยาในรูปแบบต่างๆ เอกสาร [quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) ต่อไปนี้จะแนะนำวิธีการส่งคำขอไปยังบริการนี้

อีกประเด็นหนึ่งที่ต้องพิจารณาคือประสิทธิภาพโดยรวมของแอปพลิเคชัน สำหรับแอปพลิเคชันแบบหลายรูปแบบและมีหลายโมเดล เราพิจารณาว่าประสิทธิภาพหมายความว่าระบบทำงานได้ตามที่คุณและผู้ใช้ของคุณคาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตราย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมควรใช้ [generation quality and risk and safety metrics](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in)

คุณสามารถประเมินแอป AI ของคุณในสภาพแวดล้อมการพัฒนาโดยใช้ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) โดยให้ชุดข้อมูลทดสอบหรือเป้าหมาย แอปรุ่นปัญญาประดิษฐ์ของคุณจะถูกวัดเชิงปริมาณด้วยเครื่องมือประเมินในตัวหรือเครื่องมือประเมินที่คุณเลือกเอง เพื่อเริ่มต้นใช้งาน prompt flow sdk เพื่อประเมินระบบสามารถทำตาม [quickstart guide](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) หลังจากที่คุณเรียกใช้งานประเมินแล้ว คุณสามารถ [แสดงผลลัพธ์ใน Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results)

## เครื่องหมายการค้า

โปรเจคนี้อาจประกอบด้วยเครื่องหมายการค้าหรือโลโก้ของโปรเจค ผลิตภัณฑ์ หรือบริการ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ที่ได้รับอนุญาตต้องปฏิบัติตาม  
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)  
การใช้เครื่องหมายการค้าหรือโลโก้ Microsoft ในเวอร์ชันที่แก้ไขของโปรเจคนี้ต้องไม่ก่อให้เกิดความสับสนหรือบ่งบอกว่ามีการสนับสนุนจาก Microsoft  
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใดๆ จะต้องเป็นไปตามนโยบายของบุคคลที่สามเหล่านั้น

## รับความช่วยเหลือ

หากคุณติดขัดหรือมีคำถามใดๆ เกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

ถ้าคุณมีข้อเสนอแนะหรือตรวจพบข้อผิดพลาดในขณะสร้างโปรดเยี่ยมชม:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด กรุณาทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมควรถูกพิจารณาเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญควรใช้การแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์เท่านั้น เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้
<!-- CO-OP TRANSLATOR DISCLAIMER END -->