<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7593c1fad8734e4050b60fc3da614aa5",
  "translation_date": "2025-10-22T13:50:01+00:00",
  "source_file": "README.md",
  "language_code": "th"
}
-->
# Co-op Translator

_แปลเนื้อหาการศึกษาบน GitHub ของคุณเป็นหลายภาษาโดยอัตโนมัติ เพื่อเข้าถึงผู้คนทั่วโลกได้ง่ายขึ้น_

### 🌐 รองรับหลายภาษา

#### รองรับโดย [Co-op Translator](https://github.com/Azure/Co-op-Translator)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[อาหรับ](../ar/README.md) | [เบงกาลี](../bn/README.md) | [บัลแกเรีย](../bg/README.md) | [พม่า (เมียนมา)](../my/README.md) | [จีน (ตัวย่อ)](../zh/README.md) | [จีน (ตัวเต็ม, ฮ่องกง)](../hk/README.md) | [จีน (ตัวเต็ม, มาเก๊า)](../mo/README.md) | [จีน (ตัวเต็ม, ไต้หวัน)](../tw/README.md) | [โครเอเชีย](../hr/README.md) | [เช็ก](../cs/README.md) | [เดนมาร์ก](../da/README.md) | [ดัตช์](../nl/README.md) | [เอสโตเนีย](../et/README.md) | [ฟินแลนด์](../fi/README.md) | [ฝรั่งเศส](../fr/README.md) | [เยอรมัน](../de/README.md) | [กรีก](../el/README.md) | [ฮิบรู](../he/README.md) | [ฮินดี](../hi/README.md) | [ฮังการี](../hu/README.md) | [อินโดนีเซีย](../id/README.md) | [อิตาลี](../it/README.md) | [ญี่ปุ่น](../ja/README.md) | [เกาหลี](../ko/README.md) | [ลิทัวเนีย](../lt/README.md) | [มาเลย์](../ms/README.md) | [มราฐี](../mr/README.md) | [เนปาล](../ne/README.md) | [ไนจีเรียน พิดจิน](../pcm/README.md) | [นอร์เวย์](../no/README.md) | [เปอร์เซีย (ฟาร์ซี)](../fa/README.md) | [โปแลนด์](../pl/README.md) | [โปรตุเกส (บราซิล)](../br/README.md) | [โปรตุเกส (โปรตุเกส)](../pt/README.md) | [ปัญจาบี (กูร์มูขี)](../pa/README.md) | [โรมาเนีย](../ro/README.md) | [รัสเซีย](../ru/README.md) | [เซอร์เบีย (ซีริลลิก)](../sr/README.md) | [สโลวัก](../sk/README.md) | [สโลวีเนีย](../sl/README.md) | [สเปน](../es/README.md) | [สวาฮีลี](../sw/README.md) | [สวีเดน](../sv/README.md) | [ตากาล็อก (ฟิลิปปินส์)](../tl/README.md) | [ทมิฬ](../ta/README.md) | [ไทย](./README.md) | [ตุรกี](../tr/README.md) | [ยูเครน](../uk/README.md) | [อูรดู](../ur/README.md) | [เวียดนาม](../vi/README.md)
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

## ภาพรวม

**Co-op Translator** ช่วยให้คุณแปลเนื้อหาการศึกษาบน GitHub เป็นหลายภาษาได้อย่างรวดเร็ว เข้าถึงผู้ใช้ทั่วโลกได้ง่าย เมื่อคุณอัปเดตไฟล์ Markdown, รูปภาพ หรือ Jupyter notebook การแปลจะถูกซิงค์โดยอัตโนมัติ เพื่อให้เนื้อหาการศึกษาของคุณทันสมัยและเหมาะกับผู้ใช้ต่างประเทศ

ดูตัวอย่างการจัดระเบียบเนื้อหาการศึกษาที่แปลแล้วด้วย Co-op Translator:

![ตัวอย่าง](../../translated_images/translation-ex.0c8aa6a7ee0aad2b35cddcc110c719baf0afc640e8c5a45540e6c166b9907d91.th.png)

## เริ่มต้นใช้งานอย่างรวดเร็ว

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

## การตั้งค่าขั้นพื้นฐาน

- สร้างไฟล์ `.env` โดยใช้เทมเพลต: [.env.template](../../.env.template)
- ตั้งค่า LLM provider อย่างใดอย่างหนึ่ง (Azure OpenAI หรือ OpenAI)
- หากต้องการแปลรูปภาพ (`-img`) ให้ตั้งค่า Azure AI Vision ด้วย
- แนะนำ: หากคุณมีไฟล์แปลจากเครื่องมืออื่น ให้ลบออกก่อนเพื่อป้องกันปัญหา (เช่น `translations/`)
- แนะนำ: เพิ่มส่วนแปลภาษาใน README โดยใช้ [README languages template](./README_languages_template.md)
- ดูเพิ่มเติม: [ตั้งค่า Azure AI](./getting_started/set-up-azure-ai.md)

## วิธีใช้งาน

แปลทุกประเภทที่รองรับ:

```bash
translate -l "ko ja"
```

เฉพาะ Markdown:

```bash
translate -l "de" -md
```

Markdown + รูปภาพ:

```bash
translate -l "pt" -md -img
```

เฉพาะ notebook:

```bash
translate -l "zh" -nb
```

ดูคำสั่งเพิ่มเติม: [Command reference](./getting_started/command-reference.md)

## จุดเด่น

- แปล Markdown, notebook และรูปภาพโดยอัตโนมัติ
- ซิงค์การแปลกับต้นฉบับเมื่อมีการเปลี่ยนแปลง
- ใช้งานได้ทั้งแบบ local (CLI) และใน CI (GitHub Actions)
- รองรับ Azure OpenAI หรือ OpenAI; เลือกใช้ Azure AI Vision สำหรับรูปภาพได้
- รักษารูปแบบและโครงสร้าง Markdown เดิม

## เอกสาร

- [คู่มือ command-line](./getting_started/command-line-guide/command-line-guide.md)
- [คู่มือ GitHub Actions (สำหรับ public repo & standard secrets)](./getting_started/github-actions-guide/github-actions-guide-public.md)
- [คู่มือ GitHub Actions (สำหรับ repo ในองค์กร Microsoft & org-level setups)](./getting_started/github-actions-guide/github-actions-guide-org.md)
- [ภาษาที่รองรับ](./getting_started/supported-languages.md)
- [การแก้ไขปัญหา](./getting_started/troubleshooting.md)

## สนับสนุนเราและส่งเสริมการเรียนรู้ทั่วโลก

ร่วมเปลี่ยนแปลงการแบ่งปันเนื้อหาการศึกษาสู่ระดับโลก! กดดาว [Co-op Translator](https://github.com/azure/co-op-translator) บน GitHub และสนับสนุนภารกิจของเราในการขจัดอุปสรรคด้านภาษาในการเรียนรู้และเทคโนโลยี ความสนใจและการมีส่วนร่วมของคุณสร้างผลกระทบอย่างมาก! ยินดีรับข้อเสนอแนะและโค้ดจากทุกคน

### สำรวจเนื้อหาการศึกษาของ Microsoft ในภาษาของคุณ

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

## วิดีโอแนะนำ

เรียนรู้เพิ่มเติมเกี่ยวกับ Co-op Translator จากวิดีโอของเรา _(คลิกที่ภาพด้านล่างเพื่อรับชมบน YouTube.)_:

- **Open at Microsoft**: แนะนำสั้น ๆ 18 นาที พร้อมวิธีใช้งาน Co-op Translator

  [![Open at Microsoft](../../translated_images/open-ms-thumbnail.946b356b89bc5f0e33dcebb852f7926b98c33f54c1a49ce01c36ae7f35e2443a.th.jpg)](https://www.youtube.com/watch?v=jX_swfH_KNU)

## การร่วมพัฒนา

โปรเจกต์นี้เปิดรับข้อเสนอแนะและการร่วมพัฒนา หากสนใจร่วมพัฒนา Azure Co-op Translator ดูรายละเอียดได้ที่ [CONTRIBUTING.md](./CONTRIBUTING.md) สำหรับแนวทางการช่วยให้ Co-op Translator เข้าถึงผู้ใช้มากขึ้น

## ผู้ร่วมพัฒนา

[![co-op-translator contributors](https://contrib.rocks/image?repo=Azure/co-op-translator)](https://github.com/Azure/co-op-translator/graphs/contributors)

## จรรยาบรรณ

โปรเจกต์นี้ใช้ [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
ดูข้อมูลเพิ่มเติมได้ที่ [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) หรือ
ติดต่อ [opencode@microsoft.com](mailto:opencode@microsoft.com) หากมีคำถามหรือข้อเสนอแนะเพิ่มเติม

## AI อย่างรับผิดชอบ

Microsoft มุ่งมั่นช่วยให้ลูกค้าใช้ AI อย่างรับผิดชอบ แบ่งปันประสบการณ์ และสร้างความไว้วางใจผ่านเครื่องมืออย่าง Transparency Notes และ Impact Assessments ทรัพยากรเหล่านี้ดูได้ที่ [https://aka.ms/RAI](https://aka.ms/RAI)
แนวทาง AI อย่างรับผิดชอบของ Microsoft ยึดหลักความยุติธรรม ความน่าเชื่อถือและความปลอดภัย ความเป็นส่วนตัวและความปลอดภัย การมีส่วนร่วม ความโปร่งใส และความรับผิดชอบ

โมเดลขนาดใหญ่สำหรับภาษา รูปภาพ และเสียง - เช่นที่ใช้ในตัวอย่างนี้ - อาจมีพฤติกรรมที่ไม่ยุติธรรม ไม่น่าเชื่อถือ หรือไม่เหมาะสม ซึ่งอาจก่อให้เกิดผลกระทบได้ โปรดอ่าน [Azure OpenAI service Transparency note](https://learn.microsoft.com/legal/cognitive-services/openai/transparency-note?tabs=text) เพื่อทราบความเสี่ยงและข้อจำกัด

แนวทางที่แนะนำในการลดความเสี่ยง คือการมีระบบความปลอดภัยในสถาปัตยกรรมของคุณ เพื่อช่วยตรวจจับและป้องกันพฤติกรรมที่เป็นอันตราย [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview) เป็นชั้นป้องกันอิสระที่สามารถตรวจจับเนื้อหาที่เป็นอันตรายทั้งจากผู้ใช้และ AI ในแอปและบริการ Azure AI Content Safety มี API สำหรับข้อความและรูปภาพที่ช่วยตรวจจับเนื้อหาที่เป็นอันตราย และยังมี Content Safety Studio ให้ทดลองใช้งานและดูตัวอย่างโค้ดสำหรับตรวจจับเนื้อหาที่เป็นอันตรายในหลายรูปแบบ ดู [เอกสาร quickstart](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Clinux&pivots=programming-language-rest) สำหรับวิธีเรียกใช้งานบริการนี้
อีกเรื่องหนึ่งที่ควรคำนึงถึงคือประสิทธิภาพโดยรวมของแอปพลิเคชัน สำหรับแอปพลิเคชันที่ใช้หลายโหมดและหลายโมเดล เราถือว่าประสิทธิภาพหมายถึงระบบทำงานได้ตามที่คุณและผู้ใช้คาดหวัง รวมถึงไม่สร้างผลลัพธ์ที่เป็นอันตรายด้วย การประเมินประสิทธิภาพของแอปพลิเคชันโดยรวมของคุณโดยใช้ [เกณฑ์คุณภาพการสร้างและตัวชี้วัดความเสี่ยงและความปลอดภัย](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in) จึงเป็นสิ่งสำคัญ

คุณสามารถประเมินแอปพลิเคชัน AI ของคุณในสภาพแวดล้อมการพัฒนาโดยใช้ [prompt flow SDK](https://microsoft.github.io/promptflow/index.html) ไม่ว่าจะเป็นชุดข้อมูลทดสอบหรือเป้าหมาย แอปพลิเคชัน generative AI ของคุณจะถูกวัดผลเชิงปริมาณด้วยตัวประเมินที่มีมาให้หรือจะใช้ตัวประเมินที่คุณกำหนดเองก็ได้ หากต้องการเริ่มต้นใช้งาน prompt flow sdk เพื่อประเมินระบบของคุณ สามารถดู [คู่มือเริ่มต้นใช้งาน](https://learn.microsoft.com/azure/ai-studio/how-to/develop/flow-evaluate-sdk) ได้เลย เมื่อคุณดำเนินการประเมินเสร็จแล้ว คุณสามารถ [ดูผลลัพธ์ใน Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-flow-results) ได้

## เครื่องหมายการค้า

โปรเจกต์นี้อาจมีเครื่องหมายการค้าหรือโลโก้สำหรับโปรเจกต์ ผลิตภัณฑ์ หรือบริการ การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ต้องได้รับอนุญาตและต้องปฏิบัติตาม
[แนวทางการใช้เครื่องหมายการค้าและแบรนด์ของ Microsoft](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)
การใช้เครื่องหมายการค้าหรือโลโก้ของ Microsoft ในเวอร์ชันที่ปรับแต่งต้องไม่ทำให้เกิดความสับสนหรือสื่อถึงการสนับสนุนจาก Microsoft
การใช้เครื่องหมายการค้าหรือโลโก้ของบุคคลที่สามใด ๆ จะต้องเป็นไปตามนโยบายของเจ้าของเครื่องหมายการค้านั้น

## ขอความช่วยเหลือ

หากคุณติดขัดหรือมีคำถามเกี่ยวกับการสร้างแอป AI เข้าร่วมได้ที่:

[![Azure AI Foundry Discord](https://img.shields.io/badge/Discord-Azure_AI_Foundry_Community_Discord-blue?style=for-the-badge&logo=discord&color=5865f2&logoColor=fff)](https://aka.ms/foundry/discord)

หากคุณมีข้อเสนอแนะเกี่ยวกับผลิตภัณฑ์หรือพบข้อผิดพลาดขณะสร้างแอป เข้าไปที่:

[![Azure AI Foundry Developer Forum](https://img.shields.io/badge/GitHub-Azure_AI_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

**ข้อจำกัดความรับผิดชอบ**:
เอกสารฉบับนี้ได้รับการแปลโดยใช้บริการแปลภาษา AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลโดยอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลสำคัญ ขอแนะนำให้ใช้บริการแปลโดยนักแปลมืออาชีพ ทางเราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่เกิดจากการใช้การแปลนี้