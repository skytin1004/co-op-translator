---
title: "Förstå Azure Digital Twins-användningsfall och arkitektur"
description: "Utforska olika användningsfall och arkitekturalternativ för Azure Digital Twins."
ms.assetid: 7af98e5d-1e3d-4d08-a5d2-3d38d079a91e
ms.service: azure-digitaltwins
ms.subservice: digitaltwins
ms.topic: conceptual
ms.tgt_pltfrm: na
ms.devlang: na
ms.author: pnp
ms.date: 09/06/2022
---

# Förstå Azure Digital Twins-användningsfall och arkitektur

Azure Digital Twins är en plattform som tillhandahåller en deklarativ spatial intelligent modell för att förstå relationer och tillstånd i komplexa miljöer. Med Azure Digital Twins kan du skapa omfattande modeller av fysiska miljöer och tillstånd över enheter, system och processer.

## Användningsfall

### Smarta byggnader

Använd Azure Digital Twins för att skapa omfattande digitala modeller av byggnader och fastigheter. Detta inkluderar:

- **Energihantering:** Optimera energi-användning genom att övervaka värme, ventilation och luftkonditionering (HVAC) system i realtid.
- **Tillgångsspårning:** Följ tillgångars plats och status inom byggnaden för förbättrad hantering och underhåll.
- **Aktivt utrymmesutnyttjande:** Analysera områdesanvändning och optimera platsutnyttjande för mötesrum och arbetsytor.
- **Säkerhet och åtkomstkontroll:** Integrera sensorer och system för att förstärka säkerhetsåtgärder och hantera åtkomsträttigheter.

### Industriell tillverkning

Azure Digital Twins kan modellera komplexa industriella miljöer för att förbättra produktionsprocesser och underhåll:

- **Prediktivt underhåll:** Övervaka maskiners tillstånd och förutse fel innan de inträffar, vilket minimerar driftstopp.
- **Processoptimering:** Simulera och optimera tillverkningsprocesser för bättre effektivitet och produktkvalitet.
- **Resurshantering:** Hantera maskiner, material och personal i realtid för att maximera produktiviteten.

### Smart stadsplanering

Använd digitala tvillingar för att förstå och planera urbana miljöer:

- **Trafik- och transportsimulering:** Analysera trafikflöden och förbättra kollektivtrafiksystem.
- **Miljöövervakning:** Övervaka luftkvalitet och ljudnivåer för att skapa hälsosammare stadsområden.
- **Energianvändning:** Optimera energidistribution och implementera hållbara lösningar för stadsinfrastruktur.

### Hälsovård och sjukhus

- **Patientflöde:** Modellera sjukhusets olika avdelningar och patienter för att förbättra flödet och minska väntetider.
- **Utrustningshantering:** Spåra medicinsk utrustning och resurser för att maximera tillgänglighet.
- **Miljökontroll:** Övervaka luftkvalitet, temperatur och andra faktorer för att upprätthålla säkerheten och hygien.

## Arkitekturalternativ och designmönster

Azure Digital Twins kan integreras med andra Azure-tjänster och lösningar för att bygga kraftfulla, anpassade digitala tvillingløsningar.

### Grundläggande arkitektur

- **Azure Digital Twins-tjänst:** Den primära tjänsten för modellering och hantering av digitala tvillingar.
- **IoT Hub:** Används för att ansluta och samla in data från fysiska enheter och sensorer.
- **Event Grid:** Distribuerar händelser i realtid från Digital Twins till olika konsumenter för vidare bearbetning.
- **Azure Functions och logikappar:** Hantera anpassad affärslogik och automatisering baserat på händelser och tillståndsförändringar.

### Dataflöde

1. Enheter skickar telemetridata till IoT Hub.
2. Telemetrin uppdaterar digitala tvillingars tillstånd via Azure Digital Twins API.
3. Händelser triggas när tillstånd ändras och vidarebefordras via Event Grid.
4. Azure Functions eller andra tjänster reagerar på händelser för att utföra affärslogik, notifieringar eller integrationer.

### Skalbarhet och säkerhet

- **Rollbaserad åtkomstkontroll (RBAC):** Säkerställ att endast auktoriserade användare och tjänster kan interagera med digitala tvillingar.
- **Dataisolering:** Använd Azure-resursgrupper och prenumerationer för att skydda data i olika miljöer.
- **Skalning:** Tjänsten är utformad för att hantera stor skala av enheter och hög genomströmning av telemetri.

## Sammanfattning

Azure Digital Twins ger en flexibel och kraftfull plattform för att skapa omfattande digitala modeller av fysiska miljöer och deras tillstånd. Genom att kombinera modellering, realtidsdata och integrerade Azure-tjänster kan organisationer skapa lösningar som effektiviserar verksamheter, optimerar resurser och utvecklar smarta, uppkopplade ekosystem.

Fortsätt utforska [Azure Digital Twins-dokumentationen](https://learn.microsoft.com/azure/digital-twins/) för att få en djupare förståelse och konkreta exempel på implementation.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->