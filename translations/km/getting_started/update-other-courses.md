# អាប់ដេតផ្នែក "វគ្គផ្សេងទៀត" (មូលដ្ឋាន Microsoft Beginners)

មគ្គុទេសក៍នេះពន្យល់ពីរបៀបធ្វើឲ្យផ្នែក "វគ្គផ្សេងទៀត" ប្រើស្វ័យប្រវត្តិសម្របសម្រួលដោយ Co‑op Translator និងរបៀបអាប់ដេតសាច់ដុំទូទៅសម្រាប់គ្រប់មូលដ្ឋាន។

- អនុវត្តចំពោះ៖ មូលដ្ឋាន Microsoft Beginners តែប៉ុណ្ណោះ
- ប្រើបានជាមួយ៖ Co‑op Translator CLI និង GitHub Actions
- ប្រភពសាច់ដុំ៖ [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ចាប់ផ្តើមលឿន៖ បើកសម្របសម្រួលស្វ័យប្រវត្ត នៅក្នុង repo របស់អ្នក

បន្ថែមសញ្ញាសម្គាល់ខាងក្រោមជុំវិញផ្នែក "វគ្គផ្សេងទៀត" ក្នុង README របស់អ្នក។ Co‑op Translator នឹងជំនួសអ្វីដែលស្ថិតនៅចន្លោះសញ្ញាសម្គាល់ទាំងនេះនៅរាល់ដំណើរការ។

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

រាល់ពេល Co‑op Translator ដំណើរការ—តាម CLI (ឧ. `translate -l "<language codes>"`) ឬ GitHub Actions—វានឹងធ្វើការអាប់ដេតផ្នែក "វគ្គផ្សេងទៀត" ដែលមានរម្លោងដោយសញ្ញាសម្គាល់ទាំងនេះដោយស្វ័យប្រវត្តិ។

> [!NOTE]
> ប្រសិនបើអ្នកមានបញ្ជីរួចរាល់ហើយ គ្រាន់តែដាក់រម្លោងវាជាមួយសញ្ញាសម្គាល់ដដែល។ ដំណើរការបន្ទាប់នឹងជំនួសវាជាមួយមាតិកាតែមួយដែលបានស្ដង់ដារលើកថ្មីបំផុត។

---

## របៀបផ្លាស់ប្តូរសាច់ដុំទូទៅ

ប្រសិនបើអ្នកចង់អាប់ដេតមាតិកាតែមួយដែលបង្ហាញនៅគ្រប់ repo Beginners:

1. បន្តិចសាច់ដុំ៖ [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. បើក pull request ទៅ repo Co-op Translator ជាមួយការផ្លាស់ប្តូររបស់អ្នក
3. បន្ទាប់ពី PR បានបញ្ចូលចូលរួចហើយ សេចក្ដីប្រកាស Co‑op Translator នឹងត្រូវបានអាប់ដេត
4. ពេល Co‑op Translator ដំណើរការ (CLI ឬ GitHub Action) នៅ repo គោលដៅ វានឹងសម្របសម្រួលផ្នែកដែលបានអាប់ដេតដោយស្វ័យប្រវត្តិ

នេះធានាថាមានប្រភពមួយតែមួយសម្រាប់ "វគ្គផ្សេងទៀត" នៅគ្រប់មូលដ្ឋាន Beginners។

## ទំហំ Repo

repo អាចធំធាត់ដោយសារតែចំនួនភាសាដែលបានបកប្រែ ដើម្បីជួយអ្នកប្រើចុងក្រោយផ្តល់ការណែនាំពីរបៀបប្រើ clone - sparse ដើម្បី clone តែភាសាចាំបាច់ប៉ុណ្ណោះ ហើយមិនចាំបាច់ clone ទាំងមូល repo នោះឡើយ

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
**ការត្រៀមប្រកាស**៖  
ឯកសារនេះត្រូវបានបម្លែងជាភាសាដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះយើងខិតខំរកភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថា ការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬការមិនត្រឹមត្រូវ។ ឯកសារដើមភាសាដើមគួរត្រូវបានគិតថាជាដល់ប្រភពផ្លូវការផ្ទាល់។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ សូមផ្តល់អាទិភាពការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការពន្យល់ខុសពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->