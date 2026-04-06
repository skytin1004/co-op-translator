# ធ្វើបច្ចុប្បន្នភាពផ្នែក "វគ្គផ្សេងទៀត" (Microsoft Beginners repos)

សៀវភៅណែនាំនេះពន្យល់ពីរបៀបធ្វើឱ្យផ្នែក "វគ្គផ្សេងទៀត" សមមូលម៉ាស៊ីនដោយស្វ័យប្រវត្តិដោយប្រើ Co‑op Translator និងរបៀបធ្វើបច្ចុប្បន្នភាពទម្រង់ពិភពលោកសម្រាប់ repos ទាំងអស់។

- ផ្ទេរតែទៅ: Microsoft Beginners repositories តែប៉ុណ្ណោះ
- ធ្វើការជាមួយ: Co‑op Translator CLI និង GitHub Actions
- ប្រភពទម្រង់៖ [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ចាប់ផ្តើមលឿន៖ បើកការសមមូលម៉ាស៊ីនក្នុង repo របស់អ្នក

បន្ថែមកម្មវិធីសញ្ញាខាងក្រោមជុំវិញផ្នែក "វគ្គផ្សេងទៀត" នៅក្នុង README របស់អ្នក។ Co‑op Translator នឹងជំនួសរបស់គ្រប់អ្វីដែលនៅចន្លោះសញ្ញាទាំងនេះនៅក្នុងរាល់ការប្រតិបត្តិការ។

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

រៀងរាល់ពេលដែល Co‑op Translator បើកដំណើរការ - តាម CLI (ឧ. `translate -l "<language codes>"`) ឬ GitHub Actions - វានឹងធ្វើបច្ចុប្បន្នភាពផ្នែក "វគ្គផ្សេងទៀត" ដែលត្រូវបានបិទបោះជុំវិញដោយសញ្ញាទាំងនេះដោយស្វ័យប្រវត្តិ។

> [!NOTE]
> ប្រសិនបើអ្នកមានបញ្ជីដែលមានរួចហើយ គ្រាន់តែបិទច្រកជុំវិញវាដោយសញ្ញាដូចគ្នា។ ការប្រតិបត្តិការបន្ទាប់នឹងជំនួសវាជាមួយមាតិកាស្តង់ដាថ្មីបំផុត។

---

## របៀបផ្លាស់ប្តូរមាតិកាពិភពលោក

ប្រសិនបើអ្នកចង់ធ្វើបច្ចុប្បន្នភាពមាតិកាស្តង់ដាដែលបង្ហាញនៅក្នុង repos Beginners ទាំងអស់៖

1. កែសម្រួលទម្រង់៖ [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. បើក pull request ទៅកាន់ repo Co-op Translator ជាមួយការផ្លាស់ប្តូររបស់អ្នក
3. បន្ទាប់ពី PR ត្រូវបានបញ្ចូលជាមួយ Co‑op Translator កំណែថ្មីនឹងត្រូវបានធ្វើបច្ចុប្បន្នក
4. ពេល Co‑op Translator រត់បន្ទាប់ (CLI ឬ GitHub Action) នៅ repo លាក់កំណត់ វានឹងសមមូលផ្នែកដែលបានធ្វើបច្ចុប្បន្នភាពដោយស្វ័យប្រវត្តិ

នេះធានាថាមានប្រភពតែមួយសម្រាប់មាតិកា "វគ្គផ្សេងទៀត" តាមរយៈ repos Beginners ទាំងអស់។

## ទំហំ Repo

repo អាចធំឡើងដោយសារ​ចំនួនភាសាដែលបានបកប្រែ ដើម្បីជួយអ្នកប្រើចុងក្រោយផ្តល់ការណែនាំពីរបៀបប្រើ clone - sparse ដើម្បី clone តែភាសាដែលត្រូវការ និងមិន clone repo ទាំងមូល។ 

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
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ក្នុងខណៈដែលយើងខិតខំប្រឹងប្រែងធ្វើឱ្យមានភាពត្រឹមត្រូវ សូមយល់ដឹងថាបកប្រែដោយស្វ័យប្រវត្តិនោះអាចមានកំហុសឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមជាភាសាដើមគួរត្រូវបានគេចាត់ទុកជាប្រភពដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមណែនាំឲ្យប្រើការបកប្រែដោយមនុស្សមុខជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកបែបខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->