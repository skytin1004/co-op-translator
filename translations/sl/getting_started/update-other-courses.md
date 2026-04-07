# Posodobite odsek "Druge tečaje" (Microsoft Beginners repozitoriji)

Ta vodič pojasnjuje, kako narediti samodejno sinhronizacijo odseka "Druge tečaje" z uporabo Co-op Translator ter kako posodobiti globalno predlogo za vse repozitorije.

- Velja za: repozitorije Microsoft Beginners
- Deluje z: Co-op Translator CLI in GitHub Actions
- Vzorec predloge: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hiter začetek: Omogočite samodejno sinhronizacijo v vašem repozitoriju

Dodajte naslednje označevalce okoli odseka "Druge tečaje" v vašem README. Co-op Translator bo ob vsakem zagonu nadomestil vse med tema označevalcema.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Vsakič, ko se Co-op Translator zažene – prek CLI (npr. `translate -l "<jezikovni kodi>"`) ali GitHub Actions – samodejno posodobi odsek "Druge tečaje", ovit z tema označevalcema.

> [!NOTE]
> Če že imate obstoječi seznam, ga preprosto ovijte z istimi označevalci. Naslednji zagon bo seznam nadomestil z najnovejšo standardizirano vsebino.

---

## Kako spremeniti globalno vsebino

Če želite posodobiti standardizirano vsebino, ki se pojavlja v vseh Beginners repozitorijih:

1. Uredite predlogo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Odprite pull request v Co-op Translator repozitorij s svojimi spremembami
3. Ko je PR združen, bo različica Co-op Translatorja posodobljena
4. Naslednjič, ko se Co-op Translator zažene (CLI ali GitHub Action) v ciljnem repozitoriju, bo samodejno sinhroniziral posodobljeni odsek

To zagotavlja en sam vir resnice za vsebino "Druge tečaje" v vseh Beginners repozitorijih.

## Velikosti repozitorijev 

Repozitoriji lahko postanejo veliki zaradi števila prevedenih jezikov, da uporabnikom nudijo navodila o uporabi ukaza clone - sparse, s katerim klonirajo le potrebne jezike in ne celotnega repozitorija

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
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da samodejni prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v izvorni jezik se šteje za avtoritativni vir. Za kritične informacije je priporočljivo profesionalno človeško prevajanje. Za kakršnakoli nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->