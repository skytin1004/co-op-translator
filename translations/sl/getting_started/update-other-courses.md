# Posodobitev razdelka "Drugi tečaji" (Microsoft Beginners repozitoriji)

Ta vodič pojasnjuje, kako omogočiti samodejno sinhronizacijo razdelka "Drugi tečaji" z uporabo Co-op Translatorja in kako posodobiti globalno predlogo za vse repozitorije.

- Velja za: samo repozitorije Microsoft Beginners
- Deluje z: Co-op Translator CLI in GitHub Actions
- Vir predloge: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)

---

## Hiter začetek: Omogočite samodejno sinhronizacijo v vašem repozitoriju

Dodajte naslednje označevalce okoli razdelka "Drugi tečaji" v vašem README. Co-op Translator bo ob vsakem zagonu nadomestil vse med tema označevalcema.

```markdown
<!-- CO-OP TRANSLATOR OTHER COURSES START -->
<!-- The content between START and END is auto-generated. Do not edit manually. -->
<!-- CO-OP TRANSLATOR OTHER COURSES END -->
```

Ob vsakem zagonu Co-op Translatorja—prek CLI (npr. `translate -l "<language codes>"`) ali GitHub Actions—samodejno posodobi razdelek "Drugi tečaji" ovit z tema označevalcema.

> [!NOTE]
> Če imate obstoječ seznam, ga samo zavijte z istimi označevalci. Naslednji zagon bo seznam nadomestil z najnovejšo standardizirano vsebino.

---

## Kako spremeniti globalno vsebino

Če želite posodobiti standardizirano vsebino, ki se pojavlja v vseh Beginners repozitorijih:

1. Uredite predlogo: [src/co_op_translator/templates/other_courses.md](../src/co_op_translator/templates/other_courses.md)
2. Odprite pull request v repozitorij Co-op Translator z vašimi spremembami
3. Po združitvi PR-ja bo verzija Co-op Translatorja posodobljena
4. Naslednjič, ko se Co-op Translator zažene (CLI ali GitHub Action) v ciljnem repozitoriju, bo samodejno sinhroniziral posodobljen razdelek

To zagotavlja en sam vir resnice za vsebino "Drugi tečaji" v vseh Beginners repozitorijih.

## Velikost repozitorijev

Repozitoriji lahko postanejo veliki zaradi števila prevedenih jezikov, da bi uporabnikom pomagali z navodili, kako uporabiti clone - sparse za kloniranje samo potrebnih jezikov in ne celotnega repozitorija.

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
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvor­nem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za kakršna koli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->