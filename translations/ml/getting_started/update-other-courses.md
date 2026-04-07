# "Other Courses" വിഭാഗം പുതുക്കുക (Microsoft Beginners റിപ്പോസിറ്ററീസ്)

ഈ ഗൈഡ് Co‑op Translator ഉപയോഗിച്ച് "Other Courses" വിഭാഗം ഓട്ടോ‑സങ്ക്രണൈസ് ചെയ്യുന്നത് എങ്ങനെ നടത്താമെന്ന്, കൂടാതെ എല്ലാ റിപ്പോസിറ്ററികളിലും പ്രാബല്യത്തിലാക്കാനുള്ള ആഗോള ടെംപ്ലേറ്റ് എങ്ങനെ അപ്ഡേറ്റ് ചെയ്യാമെന്ന് വിശദീകരിക്കുന്നു.

- ബാധകമാകുന്നത്: Microsoft Beginners റിപ്പോസിറ്ററീസ് മാത്രമാണ്
- പ്രവർത്തിക്കുന്നത്: Co‑op Translator CLI, GitHub Actions എന്നിവയുമായി
- ടെംപ്ലേറ്റ് ഉറവിടം: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## വേഗത്തിലുള്ള തുടക്കം: നിങ്ങളുടെ റിപ്പോസിറ്ററിയിൽ ഓട്ടോ‑സിങ്ക് സജ്ജീകരിക്കുക

നിങ്ങളുടെ README യിൽ "Other Courses" വിഭാഗം ചുറ്റിപ്പറ്റി താഴെയുള്ള മാർക്കറുകൾ ചേർക്കുക. Co‑op Translator ഈ മാർക്കറുകൾക്കിടയിലെ എല്ലാ ഉള്ളടക്കവും ഓരോ റണ്ണിലും മാറ്റി ചേർക്കും.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator ഓരോ തവണയും—CLI വഴി (ഉദാഹരണത്തിന്, `translate -l "<language codes>"`) അല്ലെങ്കിൽ GitHub Actions വഴി—ഈ മാർക്കറുകൾ കൊണ്ട് ചുറ്റപ്പെട്ട "Other Courses" വിഭാഗം അപ്പോഴത്തേയ്ക്ക് അപ്ഡേറ്റ് ചെയ്യും.

> [!NOTE]
> നിങ്ങള്‍ക്ക് നിലവിലുള്ള ഒരു പട്ടിക ഉണ്ടെങ്കിൽ, അതേ മാർക്കറുകൾ ഉപയോഗിച്ച് വെച്ച് മൂടുക മാത്രം. അടുത്ത റണ്ണിൽ അത് ഏറ്റവും പുതിയ സ്തനദ്ഡേഴ്‍ഡ് ഉള്ളടക്കത്തോടെ മാറ്റിമാറ്റിയിരിക്കും.

---

## ആഗോള ഉള്ളടക്കം എങ്ങനെ മാറ്റാം

എല്ലാ Beginners റിപ്പോസിറ്ററികളിലും പ്രയോഗിക്കുന്ന സ്റ്റാൻഡേർഡൈസ്ഡ് ഉള്ളടക്കം പുതുക്കാൻ താൽപര്യമുണ്ടെങ്കിൽ:

1. ടെംപ്ലേറ്റ് എഡിറ്റ് ചെയ്യുക: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. നിങ്ങളുടെ മാറ്റങ്ങൾ ഉൾപ്പെടുത്തുന്നായിരുന്നു Co-op Translator റിപ്പോസിറ്ററി വേണ്ടി ഒരു pull request തുറക്കുക
3. PR മേഴ്ജ് ചെയ്തതിന് ശേഷം Co‑op Translator പതിപ്പ് പുതുക്കപ്പെടും
4. Co‑op Translator അടുത്ത തവണ (CLI അല്ലെങ്കിൽ GitHub Action വഴിയോ) ടാർഗറ്റ് റിപ്പോസിറ്ററിയിൽ പ്രവർത്തിക്കുമ്പോൾ പുതുക്കിയ വിഭാഗം ഓട്ടോമാറ്റിക് syncing ചെയ്യും

ഇത് എല്ലാ Beginners റിപ്പോസിറ്ററികളിലുമുള്ള "Other Courses" ഉള്ളടക്കത്തിന് ഏക ഒരു സത്യ ഉറവിടമാക്കുന്നു.

## റിപ്പോസിറ്ററി വലുപ്പങ്ങൾ

ഭാഷകളുടെ എണ്ണം കൂട്ടിച്ചേർക്കുന്നതിനാൽ റിപ്പോസിറ്ററികൾ വലിയതായിരിക്കാം; ഉപഭോക്താക്കൾക്ക് ക്ലോൺ - സ്പാർസ് ഉപയോഗിച്ച് ആവശ്യമുള്ള ഭാഷകൾ മാത്രമേ ക്ലോൺ ചെയ്യണൂ, മുഴുവൻ റിപ്പോസ് ക്ലോൺ ചെയ്യേണ്ടതില്ലെന്നു മാർഗനിർദ്ദേശം നൽകാനാകും

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
**മുക്തഷരത**:  
ഈ രേഖ AI വിവര്‍ത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവര്‍ത്തനം ചെയ്തതാണ്. നാം സത്യസന്ധതയ്ക്കായി പരിശ്രമിച്ചിരിക്കുന്നു എങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവര്‍ത്തനങ്ങളിൽ പിഴവുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാനുള്ള സാധ്യതയുണ്ടെന്ന് ദയവായി മനസിലാക്കുക. അടിസ്ഥാന രേഖയുടെ സ്വദേശീയ ഭാഷയിലുള്ള രൂപം ഔത്തോറിറ്റേറ്റീവ് ഉറവിടമായി പരിഗണിക്കണം. നിർണ്ണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവര്‍ത്തനം ശിപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവര്‍ത്തനത്തിന്റെ ഉപയോഗത്തിൽ നിന്നു ഉണ്ടാകുന്ന எந்த തെറ്റുപ്പണവും അല്ലെങ്കിൽ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കും ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->