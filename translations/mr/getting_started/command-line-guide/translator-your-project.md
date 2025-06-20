<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d238206c3503631e32774716d11d1868",
  "translation_date": "2025-06-12T18:45:17+00:00",
  "source_file": "getting_started/command-line-guide/translator-your-project.md",
  "language_code": "mr"
}
-->
# Co-op Translator वापरून तुमचा प्रकल्प भाषांतरित करा

**Co-op Translator** हा एक कमांड-लाइन इंटरफेस (CLI) टूल आहे जो तुमच्या प्रकल्पातील markdown आणि इमेज फाइल्स अनेक भाषांमध्ये भाषांतरित करण्यास मदत करतो. या विभागात टूल कसे वापरायचे, विविध CLI पर्याय काय आहेत आणि वेगवेगळ्या वापराच्या उदाहरणांसाठी माहिती दिली आहे.

> [!NOTE]
> कमांड्सची संपूर्ण यादी आणि त्यांचे तपशीलवार वर्णन पाहण्यासाठी, कृपया [Command reference](./command-reference.md) पहा.

---

## उदाहरण परिस्थिती आणि कमांड्स

खाली काही सामान्य वापराच्या उदाहरणांसाठी **Co-op Translator** कसे वापरायचे आणि त्यासाठी कोणते कमांड्स चालवायचे ते दिले आहे.

### 1. मूलभूत भाषांतर (एकच भाषा)

तुमचा संपूर्ण प्रकल्प (markdown फाइल्स आणि इमेजेस) एका भाषेत, जसे की कोरियन, भाषांतरित करण्यासाठी खालील कमांड वापरा:

```bash
translate -l "ko"
```

हा कमांड सर्व markdown आणि इमेज फाइल्स कोरियनमध्ये भाषांतरित करेल, आणि आधीच्या भाषांतरांना न हटवता नवीन भाषांतर जोडेल.

> [!TIP]
>
> **Co-op Translator** मध्ये कोणकोणत्या भाषा कोड्स उपलब्ध आहेत हे पाहायचे असल्यास, रिपॉझिटरीतील [Supported Languages](https://github.com/Azure/co-op-translator#supported-languages) विभागाला भेट द्या.

#### Phi-3 CookBook वर उदाहरण

**Phi-3 CookBook** मध्ये, मी विद्यमान markdown फाइल्स आणि इमेजेससाठी कोरियन भाषांतर जोडण्यासाठी खालील पद्धत वापरली.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko"
Translating images: 100%|███████████████████████████████████████████████████| 276/276 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 153/153 [1:43:07<00:00, 241.31s/it]
```

### 2. अनेक भाषा भाषांतरित करणे

तुमचा प्रकल्प अनेक भाषांमध्ये (उदा. स्पॅनिश, फ्रेंच, आणि जर्मन) भाषांतरित करण्यासाठी हा कमांड वापरा:

```bash
translate -l "es fr de"
```

हा कमांड प्रकल्प स्पॅनिश, फ्रेंच आणि जर्मनमध्ये भाषांतरित करेल, आणि आधीचे भाषांतर न हटवता नवीन भाषांतर जोडेल.

#### Phi-3 CookBook वर उदाहरण

**Phi-3 CookBook** मध्ये, नवीनतम कमिट्स प्रतिबिंबित करण्यासाठी नवीन बदल पुल केल्यानंतर, मी नव्याने जोडलेल्या markdown फाइल्स आणि इमेजेस भाषांतरित करण्यासाठी खालील पद्धत वापरली.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko ja zh tw es fr" -a
Translating images: 100%|███████████████████████████████████████████████████| 273/273 [1:09:56<00:00, 15.37s/it]
Translating markdown files: 100%|████████████████████████████████████████████████| 6/6 [24:07<00:00, 241.31s/it]
```

> [!NOTE]
> सामान्यतः एकावेळी एकच भाषा भाषांतरित करणे शिफारसीय असले तरी, विशिष्ट बदलांसाठी एकावेळी अनेक भाषा भाषांतरित करणे अधिक कार्यक्षम ठरू शकते.

### 3. भाषांतर अद्यतनित करणे (सध्याचे भाषांतर हटवून)

सध्याचे भाषांतर हटवून नवीन भाषांतर करायचे असल्यास, `-u` पर्याय वापरा. हा पर्याय दिलेल्या भाषांसाठी सध्याचे सर्व भाषांतर हटवून पुन्हा भाषांतर करेल.

```bash
translate -l "ko" -u
```

सूचना: या कमांडसाठी सध्याचे भाषांतर हटवायचे की नाही याची पुष्टी विचारली जाईल.

#### Phi-3 CookBook वर उदाहरण

**Phi-3 CookBook** मध्ये, स्पॅनिश भाषांतरित सर्व फाइल्स अद्यतनित करण्यासाठी मी खालील पद्धत वापरली. जर मूळ सामग्रीत अनेक markdown दस्तऐवजांमध्ये मोठे बदल असतील तर ही पद्धत उपयुक्त आहे. जर फक्त काही विशिष्ट फाइल्स अद्यतनित करायच्या असतील तर त्या फाइल्स मॅन्युअली हटवून `-a` पद्धत वापरून नवीन भाषांतर जोडणे अधिक कार्यक्षम आहे.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "es" -u
Warning: The update command will delete all existing translations for 'es' and re-translate everything.
Do you want to continue? Type 'yes' to proceed: yes
Proceeding with update...
Translating images: 100%|████████████████████████████████████████████| 150/150 [43:46<00:00, 15.55s/it]
Translating markdown files: 100%|███████████████████████████████████| 95/95 [1:40:27<00:00, 125.62s/it]
```

### 5. फक्त इमेजेस भाषांतरित करणे

प्रकल्पातील फक्त इमेज फाइल्स भाषांतरित करण्यासाठी `-img` पर्याय वापरा:

```bash
translate -l "ko" -img
```

हा कमांड फक्त इमेजेस कोरियनमध्ये भाषांतरित करेल, markdown फाइल्सवर परिणाम होणार नाही.

### 6. फक्त Markdown फाइल्स भाषांतरित करणे

प्रकल्पातील फक्त markdown फाइल्स भाषांतरित करण्यासाठी `-md` पर्याय वापरा:

```bash
translate -l "ko" -md
```

### 7. भाषांतरित फाइल्समध्ये त्रुटी तपासणे

जर तुम्हाला भाषांतरित फाइल्समध्ये त्रुटी तपासायच्या असतील आणि आवश्यक असल्यास पुनःभाषांतर चालवायचे असेल, तर `-chk` पर्याय वापरा:

```bash
translate -l "ko" -chk
```

हा कमांड भाषांतरित markdown फाइल्स स्कॅन करेल आणि त्रुटी असलेल्या फाइल्ससाठी भाषांतर पुन्हा चालवेल.

#### Phi-3 CookBook वर उदाहरण

**Phi-3 CookBook** मध्ये, कोरियन फाइल्समधील भाषांतर त्रुटी तपासण्यासाठी आणि त्रुटी आढळलेल्या फाइल्ससाठी स्वयंचलितपणे पुनःभाषांतर चालवण्यासाठी मी खालील पद्धत वापरली.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l"ko" -chk 
Checking translated files for errors in ko...
Checking files for ko: 100%|██████████████████████████████████████████████████| 95/95 [00:01<00:00, 65.47file/s]
Retrying vsc-extension-quickstart.md for ko:   0%|                                     | 0/17 [00:00<?, ?file/s] 
```

हा पर्याय भाषांतर त्रुटी तपासतो. सध्या, मूळ आणि भाषांतरित फाइलमधील ओळींच्या फरकाचा आकडा सहा पेक्षा जास्त असल्यास फाइलला भाषांतर त्रुटी म्हणून चिन्हांकित केले जाते. भविष्यात या निकषाला अधिक लवचीक करण्याचा मानस आहे.

उदाहरणार्थ, ही पद्धत गहाळ भाग किंवा खराब झालेले भाषांतर शोधण्यासाठी उपयुक्त आहे, आणि अशा फाइल्ससाठी स्वयंचलितपणे भाषांतर पुन्हा चालवेल.

तुम्हाला आधीच कोणत्या फाइल्स समस्या आहेत हे माहित असल्यास, त्या फाइल्स मॅन्युअली हटवून `-a` option to re-translate them.

### 8. Debug Mode

To enable detailed logging for troubleshooting, use the `-d` पर्याय वापरणे अधिक कार्यक्षम आहे:

```bash
translate -l "ko" -d
```

हा कमांड डिबग मोडमध्ये भाषांतर चालवेल, ज्यामुळे भाषांतर प्रक्रियेदरम्यान उद्भवणाऱ्या समस्यांची अधिक माहिती मिळेल.

#### Phi-3 CookBook वर उदाहरण

**Phi-3 CookBook** मध्ये, markdown फाइल्समधील अनेक दुवे असलेले भाषांतरित फाइल्समुळे फॉरमॅटिंग त्रुटी, जसे की भाषांतर तुटणे आणि ओळींचे ब्रेक लक्षात न घेणे, अशी समस्या आली होती. या समस्येचे निदान करण्यासाठी मी `-d` पर्याय वापरून भाषांतर प्रक्रिया कशी चालते ते पाहिले.

```bash
(.venv) C:\Users\sms79\dev\Phi-3CookBook>translate -l "ko" -d
DEBUG:openai._base_client:Request options: {'method': 'post', 'url': '/chat/completions', 'headers': {'api-key': 'af04e0bea45747d8a7b8c131c1971044'}, 'files': None, 'json_data': {'messages': [{'role': 'user', 'content': "Translate the following text to ko. NEVER ADD ANY EXTRA CONTENT OUTSIDE THE TRANSLATION. TRANSLATE ONLY WHAT IS GIVEN TO YOU.. MAINTAIN MARKDOWN FORMAT\n\n# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models [![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%
...
```

### 9. सर्व भाषा भाषांतरित करणे

जर तुम्हाला प्रकल्प सर्व समर्थित भाषांमध्ये भाषांतरित करायचा असेल, तर `all` कीवर्ड वापरा.

> [!WARNING]
> एकावेळी सर्व भाषा भाषांतरित करणे प्रकल्पाच्या आकारावर अवलंबून खूप वेळ लागू शकतो. उदाहरणार्थ, **Phi-3 CookBook** चे स्पॅनिशमध्ये भाषांतर करण्यास सुमारे २ तास लागले. अशा प्रमाणात, एकाच व्यक्तीसाठी २० भाषा हाताळणे व्यावहारिक नाही. त्यामुळे, अनेक योगदानकर्त्यांमध्ये काम विभागणे, प्रत्येकाने एक किंवा दोन भाषा सांभाळणे आणि हळूहळू भाषांतर अद्यतनित करणे शिफारसीय आहे.

```bash
translate -l "all"
```

हा कमांड प्रकल्प सर्व उपलब्ध भाषांमध्ये भाषांतरित करेल. पुढे जाण्यापूर्वी, प्रकल्पाच्या आकारावर अवलंबून भाषांतरास बराच वेळ लागू शकतो.

> [!TIP]
>
> ### भाषांतरित फाइल्स मॅन्युअली हटवणे (ऐच्छिक)
> जेव्हा मूळ फाइल अद्यतनित केली जाते, तेव्हा भाषांतरित फाइल्स आपोआप ओळखल्या जातात आणि साफ केल्या जातात.
>
> मात्र, जर तुम्हाला मॅन्युअली भाषांतर अद्यतनित करायचे असेल — उदाहरणार्थ, एखादी विशिष्ट फाइल पुन्हा तयार करायची किंवा सिस्टीम वर्तन ओव्हरराईड करायचे असेल — तर खालील कमांड वापरून त्या फाइलच्या सर्व भाषांतर आवृत्त्या हटवू शकता.
>
> ### Windows वर:
> 1. **Command Prompt वापरून**:
>    - Command Prompt उघडा.
>    - `cd` कमांड वापरून त्या फोल्डरमध्ये जा जिथे फाइल्स आहेत.
>    - फाइल्स हटवण्यासाठी खालील कमांड वापरा:
>      ```
>      del /s *filename*
>      ```
>      `filename` with the specific part of the file name you're looking for. The `/s` पर्याय उपफोल्डर्समध्येही शोध घेतो.
>
> 2. **PowerShell वापरून**:
>    - PowerShell उघडा.
>    - हा कमांड चालवा:
>      ```powershell
>      Get-ChildItem -Path "C:\YourPath" -Filter "*filename*" -Recurse | Remove-Item -Force
>      ```
>      `"C:\YourPath"` with the folder path and `filename` with the specific name.
>
> ### On macOS/Linux:
> 1. **Using Terminal**:
>   - Open Terminal.
>   - Navigate to the directory with `cd`.
>   - Use the `find` कमांड:
>     ```bash
>     find . -type f -name "*filename*" -delete
>     ```
>     `filename` with the specific name.
>
> Always double-check the files before deleting to avoid accidental loss. 
>
> Once you have deleted the files which need to be replace simply rerun your `translate -l` कमांड वापरून सर्वात अलीकडील फाइल बदल अद्यतनित करा.

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात ठेवा की स्वयंचलित अनुवादांमध्ये चुका किंवा अपूर्णता असू शकते. मूळ दस्तऐवज त्याच्या मूळ भाषेत अधिकृत स्रोत म्हणून मानला पाहिजे. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद करण्याचा सल्ला दिला जातो. या अनुवादाच्या वापरामुळे झालेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागीसाठी आम्ही जबाबदार नाही.