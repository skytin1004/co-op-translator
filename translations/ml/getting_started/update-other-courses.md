# "മറ്റു കോഴ്‌സുകൾ" വിഭാഗം അപ്ഡേറ്റ് ചെയ്യുക (Microsoft Beginners repositories)

ഇത് Co‑op Translator ഉപയോഗിച്ച് "മറ്റു കോഴ്‌സുകൾ" വിഭാഗം ഓട്ടോ-സിംക്രൺലൈസ് ചെയ്യുന്നതിനും എല്ലാ repositories-ക്കും പ്രയോജനപ്രദമായ ഗ്ലോബൽ ടെംപ്ലേറ്റ് അപ്ഡേറ്റ് ചെയ്യുന്നതിനുടേയും മാർഗ്ഗരേഖയാണ്.

- ബാധകമാകുന്നത്: Microsoft Beginners repositories മാത്രം
- പ്രവർത്തിക്കുന്നു: Co‑op Translator CLIയും GitHub Actions ഉം
- ടെംപ്ലേറ്റ് സ്രോത്: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## ഫാസ്റ്റ് സ്റ്റാർട്ട്: നിങ്ങളുടെ repository-യിൽ ഓട്ടോ-സിങ്ക് എനേബിൾ ചെയ്യുക

താഴെ നൽകിയ മാർക്കറുകൾ നിങ്ങളുടെ README ഫയലിലെ "മറ്റു കോഴ്‌സുകൾ" വിഭാഗം ചുറ്റിപ്പുറത്ത് ചേർക്കുക. Co‑op Translator ഈ മാർക്കറുകൾക്കിടയിലെ എല്ലാം ഓരോ ഓടിപ്പോഴും മാറ്റിത്തരും.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator CLI (ഉദാഹരണത്തിന്, `translate -l "<language codes>"`) യുടെ സഹായത്തോടെയോ GitHub Actions വഴിയോ ഓടുമ്പോൾ, ഈ മാർക്കറുകളാൽ ചുറ്റപ്പെട്ട "മറ്റു കോഴ്‌സുകൾ" വിഭാഗം സ്വയമേവ അപ്ഡേറ്റ് ചെയ്യും.

> [!NOTE]
> നിങ്ങളുടെ നിലവിലുള്ള പട്ടിക ഉണ്ടെങ്കിൽ, അത് സദൃശമായ മാർക്കറുകൾ കൊണ്ടു ചുറ്റിവച്ചാൽ മതി. അടുത്ത ഓടിപ്പോൾ അത് പുതുമയുള്ള ഏകദേശ ഉള്ളടക്കത്തോടെ മാറ്റിവെക്കും.

---

## ഗ്ലോബൽ ഉള്ളടക്കം എങ്ങനെ മാറ്റാം

എല്ലാ Beginners repositories-ലും പ്രത്യക്ഷപ്പെടുന്ന ഏകദേശ ഉള്ളടക്കം അപ്ഡേറ്റ് ചെയ്യുവാൻ ആഗ്രഹിച്ചാൽ:

1. ടെംപ്ലേറ്റ് എഡിറ്റ് ചെയ്യുക: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. നിങ്ങൾ ചെയ്ത മാറ്റങ്ങൾക്ക് Co-op Translator repo-യിലേക്ക് ഒരു pull request തുറക്കുക
3. PR മേഴ്ജ് ചെയ്തശേഷം, Co‑op Translator പതിപ്പ് അപ്ഡേറ്റ് ചെയ്യും
4. അടുത്ത Co‑op Translator ഓടിപ്പോൾ (CLI അല്ലെങ്കിൽ GitHub Action) ലക്ഷ്യ repo-യിൽ ഓടുമ്പോൾ, അപ്ഡേറ്റ് ചെയ്ത വിഭാഗം സ്വയമേവ സിംക്രൺലൈസ് ചെയ്യും

ഇത് എല്ലാ Beginners repositories-ലും "മറ്റു കോഴ്‌സുകൾ" ഉള്ളടക്കത്തിന് ഏക സ്രോതസ്സായ സത്യം ഉറപ്പാക്കുന്നു.

## Repository വലിപ്പങ്ങൾ

ഉപയോക്താക്കളെ സഹായിക്കാൻ ഭാഷകൾക്ക് തർജ്ജിമ ചെയ്യുന്നതിനാൽ repositories വലുതാകും. ആവശ്യമായ ഭാഷകൾ മാത്രം ക്ലോൺ ചെയ്യുവാൻ, പൂർണ repo അല്ലാതെ clone - sparse രീതി ഉപയോഗിക്കുന്നതിനു മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു.

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
**ഡിസ്ക്ലെയിമർ**:  
ഈ ഡോക്യുമെന്റ് AI અનુവാദ സേവനമായ [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് പരിഭാഷപ്പെടുത്തിയതാണ്. ഞങ്ങൾ കൃത്യതയ്ക്ക് ശ്രമിക്കുന്നുവെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകൾത്തിൽ പിഴവുകൾ അതുകൊണ്ടുണ്ടാകാവുന്നതാണ്. ബന്ധപ്പെട്ട ഭാഷയിലുള്ള മൂല ഡോക്യുമെന്റ് ആയിരിക്കും അധികാരമുള്ള ഉറവിടം. പ്രധാന വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മനുഷ്യ പരിഭാഷ ശുപാർശ ആണ്. ഈ പരിഭാഷ ഉപയോഗിച്ചതിനാൽ ഉണ്ടാകുന്ന തെറിവുകളും തെറ്റായ വ്യാഖ്യാനങ്ങളും സംബന്ധിച്ച് ഞങ്ങൾ ഉത്തരവാദിത്വം ഏറ്റെടുക്കുന്നില്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->