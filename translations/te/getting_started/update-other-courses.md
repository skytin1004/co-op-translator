# "ఇతర కోర్సులు" విభాగాన్ని నవీకరించండి (Microsoft Beginners repos)

ఈ గైడ్ Co-op Translator ఉపయోగించి "ఇతర కోర్సులు" విభాగాన్ని ఆటో‑సింక్ చేయడం ఎలా చేయాలో, మరియు అన్ని రిపోస్ కోసం గ్లోబల్ టెంప్లేట్‌ను ఎలా నవీకరించాలో వివరించును.

- వర్తిస్తుంది: Microsoft Beginners రిపోజిటరీలపై మాత్రమే
- పని చేయుటకు: Co-op Translator CLI మరియు GitHub Actions తో
- టెంప్లేట్ మూలం: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## త్వ‌రిత ప్రారంభం: మీ రిపోలో ఆటో‑సింక్ ఎనేబుల్ చేయండి

మీ README లో "ఇతర కోర్సులు" విభాగం చుట్టూ కింది మార్కర్లను జోడించండి. ప్రతి రన్ సమయంలో Co-op Translator ఈ మార్కర్ల మధ్య ఉన్న ప్రతీదాన్ని మార్చుతుంది.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

ప్రతి సారి Co-op Translator రన్ చెయ్యగానే—CLI ద్వారా (ఉదాహరణకు, `translate -l "<language codes>"`) లేదా GitHub Actions ద్వారా—ఈ మార్కర్లతో చుట్టబడిన "ఇతర కోర్సులు" విభాగాన్ని ఆటోమేటిక్‌గా నవీకరిస్తుంది.

> [!NOTE]
> మీ వద్ద ఇప్పటికే లిస్ట్ ఉన్నట్లయితే, దీన్ని ఆMARKర్లు తో కవర simply wrap చేయండి. తదుపరి రన్ తాజా ప్రమాణీకృత కంటెంట్ తో దానిని మార్చుతుంది.

---

## గ్లోబల్ కంటెంట్ మార్చడం ఎలా

మీరు అన్ని Beginners రిపోస్ లో కనిపించే ప్రమాణీకృత కంటెంట్‌ను నవీకరించాలనుకుంటే:

1. టెంప్లేట్‌ను ఎడిట్ చేయండి: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. మీ మార్పులతో Co-op Translator రిపోకు ఒక pull request తెరవండి
3. PR విలీనం అయ్యాక, Co-op Translator వెర్షన్ అప్డేట్ అవుతుంది
4. తదుపరి సారి Co-op Translator (CLI లేదా GitHub Action ద్వారా) టార్గెట్ రిపోలో రన్ అయినప్పుడు, అది ఆటోమేటిక్‌గా నవీకరించిన విభాగాన్ని సింక్ చేస్తుంది

ఇది అన్ని Beginners రిపోజిటరీలలో "ఇతర కోర్సులు" కంటెంట్‌కు ఒకే మూల సత్యాన్ని నిర్ధారిస్తుంది.


## రిపో పరిమాణాలు

వాడుకదారులకు మార్గదర్శకం ఇవ్వడంలో సహాయపడేందుకు అనువాద భాషల సంఖ్య పెరిగిన కారణంగా రిపో భారీగా మారవచ్చు. కావున, అవసరమైన భాషలకే క్లోన్ చేయడానికి clone - sparse ఎలా ఉపయోగించాలో గైడ్ చేయడం ఉంటుంది.

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
**పరామర్శ**:  
ఈ పాఠ్యాంశం [Co-op Translator](https://github.com/Azure/co-op-translator) అనే AI అనువాద సేవను ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, స్వయంచాలక అనువాదాల్లో లోపాలు లేదా తప్పుదోవలు ఉండవచ్చు. స్థానిక భాషలో ఉన్న మూల పత్రాన్ని అధికార పత్రంగా పరిశీలించాలి. అత్యవసరమైన సమాచారం కోసం, నైపుణ్యం కలిగిన మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం ఉపయోగించడంలో ఏవైనా అపార్థాలు లేదా తప్పుగా అర్థం చేసుకోవడంపై మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->