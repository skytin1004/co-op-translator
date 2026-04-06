# "மற்ற பாடங்கள்" பிரிவை புதுப்பிக்கவும் (Microsoft Beginners கிடைகள்)

இந்த வழிகாட்டி Co‑op Translator-ஐ பயன்படுத்தி "மற்ற பாடங்கள்" பிரிவை தானாக ஒத்திசைக்க எப்படி செய்வது மற்றும் அனைத்து கிடைகளுக்கும் உலகளாவிய வார்ப்புருவை எப்படி புதுப்பிப்பது என்பதை விளக்குகிறது.

- பொருந்தும்: Microsoft Beginners கிடைகள் மட்டும்
- செயல்படும்: Co‑op Translator CLI மற்றும் GitHub Actions உடன்
- வார்ப்புரு மூலக்கோப்பு: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## விரைவான தொடக்கம்: உங்கள் கிடையில் தானாக ஒத்திசைவை இயக்கு

உங்கள் README-இல் "மற்ற பாடங்கள்" பிரிவின் சுமையுள்ள பகுதிகளை கீழ்காணும் குறிமுறைகளால் சுற்றியறுத்தவும். Co‑op Translator இந்த குறிமுறைகளுக்கிடையிலான அனைத்தையும் ஒவ்வொரு இயக்கத்திலும் மாற்றி பதிப்பிக்கும்.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Co‑op Translator CLI (எ.கா., `translate -l "<language codes>"`) வாயிலாகவோ அல்லது GitHub Actions மூலம் இயங்கும் ஒவ்வொரு முறையும், இந்த குறிமுறைகளால் சுற்றப்பட்ட "மற்ற பாடங்கள்" பிரிவு தானாக புதுப்பிக்கப்படும்.

> [!NOTE]
> உங்களிடம் ஏற்கனவே பட்டியலே இருந்தால், அதையே அதே குறிமுறைகளால் சுற்றி வைக்கவும். அடுத்த இயக்கம் அதனை சமீபத்திய நிலை நோக்கி மாற்றும்.

---

## உலகளாவிய உள்ளடக்கத்தை எப்படி மாற்றுவது

எல்லா Beginners கிடைகளிலும் தோன்றும் முறைப்படுத்தப்பட்ட உள்ளடக்கத்தை நீங்கள் புதுப்பிக்க விரும்பினால்:

1. வார்ப்புருவை திருத்துங்கள்: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. உங்கள் மாற்றங்களை கொண்டு Co-op Translator கிடையில் pull request ஒன்றை திறக்கவும்
3. PR இணைக்கப்பட்ட பிறகு, Co‑op Translator பதிப்பு புதுப்பிக்கப்படும்
4. அடுத்த முறையும் Co‑op Translator (CLI அல்லது GitHub Action) குறிக்கோள் கிடையில் இயங்கும் போது, அது தானாக புதுப்பித்த பிரிவை ஒத்திசைக்கும்

இந்த முறையே அனைத்து Beginners கிடைகளிலும் "மற்ற பாடங்கள்" உள்ளடக்கத்திற்கான ஒரே உண்மையை உறுதிசெய்கிறது.


## கிடை அளவுகள்

பயனாளர்களுக்கு வழிகாட்ட உதவ பல மொழிகளில் மொழிபெயர்க்கப்படுவதால் கிடைகள் பெரியதாக மாறலாம். clone - sparse ஐ பயன்படுத்தி தேவையான மொழிகளை மட்டும் கிளோன் செய்யும் முறையைப் பயன்படுத்தும்படி வழிமுறைகள் வழங்கப்படுகின்றன, முழு கிடையைக் கிளோன் செய்ய வேண்டாம்.

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
**எச்சரிக்கை**:  
இந்தக் கோப்புப் பகுப்பாய்வு [Co-op Translator](https://github.com/Azure/co-op-translator) எனும் AI மொழிபெயர்ப்பு சேவையைக் கொண்டு மொழிபெயர்க்கப்பட்டுள்ளது. நாங்கள் துல்லியத்திற்காக முயன்றாலும், தானாக்கூடான மொழிபெயர்ப்புகளில் தவறுகள் அல்லது பிழைகள் இருக்க வாய்ப்பு உள்ளது என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் இருக்கும் அசல் ஆவணம் அதிகாரப்பூர்வ மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவலுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்தியதில் ஏற்பட்ட எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்காக நாங்கள் பொறுப்பேற்கவில்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->