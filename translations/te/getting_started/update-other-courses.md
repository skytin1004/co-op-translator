# "ఇతర కోర్సులు" విభాగాన్ని నవీకరించండి (Microsoft Beginners రిపోజిటరీలు)

ఈ గైడ్ Co‑op Translator ఉపయోగించి "ఇతర కోర్సులు" విభాగం ఆటో-సంక్రమణను ఎలా చేయాలో, మరియు అన్ని రిపోజిటరీలు కోసం గ్లోబల్ టెంప్లేట్ ఎలా అప్‌డేట్ చేయాలో వివరించిస్తుంది.

- వర్తించేది: Microsoft Beginners రిపోజిటరీలు మాత్రమే
- పని చేస్తుంది: Co‑op Translator CLI మరియు GitHub Actions తో
- టెంప్లేట్ మూలం: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## త్వరిత ప్రారంభం: మీ రిపోలో ఆటో-సింక్‌ను సక్రియం చేయండి

మీ READMEలో "ఇతర కోర్సులు" విభాగం చుట్టూ ఈ క్రింద సూచికలను చేర్చండి. Co‑op Translator ఈ సూచికల మధ్య ఉన్న అన్ని విషయాలను ప్రతి సారి రన్ సమయంలో మార్చి ఉంచుతుంది.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```
  
ప్రతి సారి Co‑op Translator CLI (ఉదా: `translate -l "<language codes>"`) లేదా GitHub Actions ద్వారా నడుస్తుంది — అది ఈ సూచికలతో చుట్టబడిన "ఇతర కోర్సులు" విభాగాన్ని ఆటోమాటిక్ గా నవీకరించుతుంది.

> [!NOTE]  
> మీ వద్ద ఇప్పటికే ఉన్న జాబితా ఉంటే, దానిని అదే సూచికలతో చుట్టండి. తదుపరి రన్‌లో అది తాజా ప్రమాణీకరించిన కారణాలతో మారుస్తుంది.

---

## గ్లోబల్ కంటెంట్‌ను ఎలా మార్చాలి

మీరు అన్ని Beginners రిపోజిటరీలు లలో కనిపించే ప్రమాణీకరించిన కంటెంట్‌ను అప్‌డేట్ చేయాలనుకుంటే:

1. టెంప్లేట్‌ను సవరించండి: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)  
2. మీ మార్పులతో Co-op Translator రిపోకు ఒక pull request తెరవండి  
3. PR మర్జ్ అయిన తర్వాత, Co‑op Translator వర్షన్ అప్‌డేట్ అవుతుంది  
4. తదుపరి సారి Co‑op Translator CLI లేదా GitHub Action ద్వారా లక్ష్య రిపోలో నడిచినప్పుడు, అది ఆటోమాటిక్ గా సవరిచిన విభాగాన్ని సింక్ చేస్తుంది

ఇది అన్ని Beginners రిపోజిటరీలలో "ఇతర కోర్సులు" కంటెంట్ కోసం ఒకే మూల సత్యాన్ని కల్పిస్తుంది.


## రిపో పరిమాణాలు  

భాషల అనువాదాల సంఖ్య కారణంగా రిపోల పరిమాణం పెద్దది కావచ్చు. దీని ద్వారా చివరి వినియోగదారులు clone - sparse ని ఉపయోగించి అవసరమైన భాషల్ని మాత్రమే క్లోన్ చేసుకోవడానికి, మొత్తం రిపోను క్లోన్ చేయకుండా మార్గనిర్దేశం అందించబడుతుంది.

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
**హక్కుమార్పిడి**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వం కోసం ప్రయత్నించినా, ఆటోమేటెడ్ అనువాదాలలో లోపాలు లేదా తప్పులు ఉండవచ్చు. మౌలిక పత్రాన్ని దాని స్థానిక భాషలోనే అధికారిక ఆధారం గా పరిగణించాలి. కీలక సమాచారం కోసం, వృత్తిగత మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం ఉపయోగంలో నుండి ఏదైనా తప్పు అర్థం చేసుకోవడం లేదా తప్పుగా అర్థం చేసుకోవడమైనా మేం బాధ్యులం కాము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->