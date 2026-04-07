# "மற்ற பாடத்திட்டங்கள்" பிரிவை புதுப்பிக்கவும் (Microsoft Beginners repositories)

இந்த வழிகாட்டி Co‑op Translator பயன்படுத்தி "மற்ற பாடத்திட்டங்கள்" பிரிவை தானாக ஒத்திசைக்க எப்படி செய்வதென்று, மற்றும் அனைத்து repositories க்கான உலகளாவிய வார்ப்புருவை எப்படி புதுப்பிப்பதென்று விளக்குகிறது.

- பொருந்தும்: Microsoft Beginners repositories மட்டுமே
- இயங்குகிறது: Co‑op Translator CLI மற்றும் GitHub Actions உடன்
- வார்ப்புரு மூலம்: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## விரைவு தொடக்கம்: உங்கள் repository இல் தானான ஒத்திசைவை இயக்கவும்

உங்கள் README இல் "மற்ற பாடத்திட்டங்கள்" பிரிவின் சுற்றிலும் கீழ்க்காணும் குறியீடுகளை சேர்க்கவும். Co‑op Translator ஒவ்வொரு ஓட்டத்திலும் இந்த குறியீடுகளுக்குள் உள்ள அனைத்தையும் மாற்றிப் பதியக் கூடியது.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ஒவ்வொரு முறையும் Co‑op Translator இயக்கப்படும் போது—CLI (எ.கா., `translate -l "<language codes>"`) அல்லது GitHub Actions மூலம்—இந்த குறியீடுகளால் சூழப்பட்ட "மற்ற பாடத்திட்டங்கள்" பிரிவு தானாக புதுப்பிக்கப்படும்.

> [!NOTE]
> நீங்கள் ஏற்கனவே உள்ள பட்டியலை வைத்திருந்தால், அதே குறியீடுகளால் அதைச் சுற்றி வையுங்கள். அடுத்த ஓட்டத்தில் அது சமீபத்திய தரமான உள்ளடக்கத்தால் புதுப்பிக்கப்படும்.

---

## உலகளாவிய உள்ளடக்கத்தை எப்படிப் மாற்றுவது

எல்லா Beginners repositories இலும் தோன்றும் நிலைத்துள்ள உள்ளடக்கத்தை நீங்கள் புதுப்பிக்க விரும்பினால்:

1. வார்ப்புருவை திருத்தவும்: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. உங்கள் மாற்றங்களுடன் Co-op Translator repository க்கான pull request ஒன்றை திறக்கவும்
3. PR இணைக்கப்பட்ட பின், Co‑op Translator பதிப்பு புதுப்பிக்கப்படும்
4. அடுத்த முறையும் Co‑op Translator (CLI அல்லது GitHub Action) இலக்கு repository இல் இயக்கப்படும் போது, அது தானாக அந்தப் பிரிவை ஒத்திசைக்கும்

இதனால் அனைத்து Beginners repositories க்கும் "மற்ற பாடத்திட்டங்கள்" உள்ளடக்கத்திற்கு ஒரு முகப்பு மூலத்தளமாகும்.

## Repository அளவுகள்

End user களுக்கு வழிகாட்டல் அளிக்க பல மொழிகளில் மொழிபெயர்க்கப்பட்டதால், repositories பெரிதாக உருவாகலாம், அதனால் clone - sparse ஐப் பயன்படுத்தி அவசியமான மொழிகள் மட்டுமே உள்ளடக்கமாகக் கொண்டு முழுதும் clone செய்யாமல் இருக்க உதவுகிறது.

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
**செய்திக்குறிப்பு**:  
இந்த ஆவணம் AI மொழிபெயர்ப்பு சேவை [Co-op Translator](https://github.com/Azure/co-op-translator) பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயற்சித்தாலும், தானாகக் கான மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கருத்தில் கொள்ளவும். அதற்கான அசல் ஆவணம் அதன் சொந்த மொழியில் அதிகாரப்பூர்வ மூலமாகக் கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்காக, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கிறோம். இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்பட்ட எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கும் நாங்கள் பொறுப்பு ஏற்கமாட்டோம்.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->