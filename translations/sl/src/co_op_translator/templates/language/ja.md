---
title: Lokalizacija s pomočjo GitHub App
description: Lokalizirajte datoteke v svojem repozitoriju z uporabo Localizeflow in GitHub App.
---

# Lokalizacija s pomočjo GitHub App

Ta članek pojasnjuje, kako uporabljati [Localizeflow](https://localizeflow.com) GitHub App za lokalizacijo datotek v vaših repozitorijih.

## Prednosti uporabe GitHub App v primerjavi z [Co-op Translator](https://github.com/Azure/co-op-translator)

- **Celovita avtomatizacija**: GitHub App lahko samodejno zazna spremembe, zažene lokalizacijske delovne tokove in ustvari PR-je.
- **Enostavna konfiguracija**: Samodejno upravljanje konfiguracije brez dodatnih skript.
- **Boljša varnost**: Deluje z minimalnimi pravicami, ki jih zagotovi GitHub OAuth.

## Začnite uporabljati GitHub App

1. Namestite [Localizeflow GitHub App](https://github.com/apps/localizeflow) v vaš repozitorij.
2. Konfigurirajte datoteko `.localizeflow.yml` v korenu repozitorija.
3. Ko potrdite spremembe v izvorni veji, bo app sprožil avtomatizirani proces lokalizacije.
4. Preverite ustvarjeni PR za lokalizacijo in ga po potrebi združite.

## Pogosta vprašanja

- Kako uredim konfiguracijo v `.localizeflow.yml`?
- Ali lahko uporabim GitHub App skupaj s [Co-op Translator](https://github.com/Azure/co-op-translator)?
- Kako spremljati napredek lokalizacije?

Za več informacij obiščite [dokumentacijo Localizeflow](https://localizeflow.com/docs).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne odgovarjamo za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->