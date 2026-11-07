# ADR-028: Experts in het advisory board, zelfgekozen strategen in het supervisory board

| | |
|---|---|
| **Status** | Deels vervangen door [ADR-030](ADR-030-klassiek-eerst-dan-de-omslag.md): de stukken van het bestuur zoekt de AI in de pauze van 10:45, niet om 12:15 |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-006 maakte het supervisory board tot drie tot vijf commissarissen. Elke commissaris had de rol van een echte belanghebbende, zoals een financieel directeur of een OR-lid, en toetste op geld, risico, mensen en regels. De AI-taak voor de lunch op dag 1 haalde die commissarissen uit de stakeholderanalyse. ADR-027 bouwde het startsjabloon (`materiaal/boards.html`) op die indeling. Het advisory board kreeg daar de ledenlijst van het virtuele board van de trainer, met denkers en helden door elkaar.

De trainer bedoelt de boards anders:

- **Advisory board:** mensen met heel veel expertise op één gebied, zoals sales, HR of productmanagement.
- **Supervisory board:** mensen die strategisch kunnen denken. De deelnemer kiest ze om inspiratie, als eigen helden. Bij de trainer zijn dat bijvoorbeeld Churchill, Gandhi, Patton, Springsteen en Obama. Zij helpen het verhaal naar de stakeholders scherp te krijgen.

## Besluit

- **Supervisory board: drie tot vijf strategen, zelf gekozen om inspiratie.**
  - Het board bespreekt visie, missie en strategie met de vaste definities uit FR-30 (ADR-026).
  - Het helpt het verhaal voor de stakeholders scherp te krijgen en komt tot een gezamenlijke conclusie en advies.
  - Minstens één lid is een tegenspreker: iemand die tegen de koers van de deelnemer in zou gaan.
  - Het sjabloon biedt twintig helden: dertien uit het virtuele board van de trainer, plus zeven vrouwen (v_MichelleObama, v_Parton, v_AOC, v_Brown, v_Merkel, v_Ardern en v_Thatcher). De deelnemer kan eigen helden toevoegen.
- **Advisory board: vijf tot zeven experts, elk met een eigen vakgebied.**
  - Elk lid toetst vanuit het eigen vak. Het board sluit af met een oordeel, voorwaarden en stopcriteria.
  - Minstens één lid is een harde scepticus.
  - Het sjabloon biedt vijftien experts. Zes komen uit het virtuele board van de trainer. Daarbij komen v_Buffett (financiën), v_Edmondson (HR en teams), v_Kotter (verandermanagement), v_Schneier (informatiebeveiliging en privacy), v_Kotler (marketing), v_FeiFeiLi (AI), v_McGrath (strategie bij onzekerheid), v_O'Neil (algoritmen en hun schade) en v_Schaake (techbeleid en regels). De deelnemer kan eigen experts toevoegen, bijvoorbeeld voor recht of inkoop.
- **Vrouwen in beide lijsten.** In het virtuele board van de trainer was v_Oprah de enige vrouw. Nu zijn het er acht van de twintig helden en vijf van de vijftien experts. Voorbeeld BV kiest in beide boards evenveel vrouwen als mannen, of meer vrouwen.
- **Nieuwe lunchtaak op dag 1 (FR-32).**
  - Vóór de lunch stelt de deelnemer het supervisory board samen.
  - Daarna zoekt de deelnemer openbare stukken waarin het bestuur van de eigen organisatie iets zegt over visie, missie en strategie: een jaarverslag, artikelen, interviews.
  - Het supervisory board bespreekt de stukken tijdens de lunch en komt tot een gezamenlijke conclusie en advies. Werkplaats 1 begint met dat advies.
- **Programma dag 1.**
  - Het blok Stakeholders gaat van 11:45–12:30 naar 11:45–12:15.
  - Van 12:15 tot 12:30 stellen de deelnemers het supervisory board samen en zoeken ze de stukken.
  - Werkplaats 1 bouwt alleen nog het advisory board. De AI-visie gaat daarna naar beide boards.
- **Boardmomenten.**
  - Het advisory board toetst de normen van het experiment (dag 2) en de test gates en de governance (dag 3).
  - Het supervisory board weegt elke keer of de koers klopt en hoe de deelnemer het vertelt.
  - De pitch thuis blijft bij het supervisory board (FR-19): daar gaat het om het verhaal.
- **Het startsjabloon is herschreven.** Het supervisory board is stap 2 en het advisory board stap 3, in de volgorde waarin de deelnemer ze bouwt. Wat iemand in de oude versie had ingevuld, neemt de pagina niet over.

## Overwogen alternatieven

- **De commissarissen houden, met de stakeholders als leden.** Verworpen. De trainer wil een board dat inspireert en strategisch meedenkt. Een board dat de stakeholders nadoet, overlapt met de stakeholderanalyse en met het investeringscomité van dag 2.
- **Helden in het advisory board, en de commissarissen in het supervisory board** (zoals in ADR-027). Verworpen. De trainer legt vakkennis bij het advisory board en strategisch denken bij het supervisory board.
- **Elk lid van het supervisory board apart laten adviseren**, zoals de regel "per commissaris één stem". Verworpen. De trainer wil een discussie met een gezamenlijke conclusie en advies.
- **Het supervisory board pas in werkplaats 1 bouwen, en de stakeholdertaak in de lunch houden.** Verworpen. Dan heeft de lunch geen taak die het board laat werken, en begint werkplaats 1 zonder advies.

## Gevolgen

- **Tellingen:** FR 30 → 31 (FR-32 nieuw), risico's 17 → 18. AC-12 meet ook het advies van het supervisory board over de stukken van het bestuur.
- **Minder tijd voor de stakeholders.** Het blok duurt 30 minuten in plaats van 45. Het supervisory board in 15 minuten kiezen en installeren is krap; wat uitloopt, gaat de lunch in.
- **Het toetsen op geld, risico, mensen en regels zit nu bij de experts.** Dat gebeurt alleen als de deelnemer de vakgebieden kiest die ertoe doen. De uitleg in het sjabloon noemt daarom recht en inkoop als voorbeelden van een eigen expert.
- **Alleen openbare stukken van het bestuur** (NFR-01). Wie niets vindt of met de voorbeeldcasus werkt, neemt het jaarverslag van een organisatie uit dezelfde sector. Dit is een nieuw risico in deel 12.
- **Een board van bewonderde mensen geeft snel gelijk.** Daarom is er een tegenspreker. De skill bevat ook een regel: de tegenspreker zegt het als het board te snel gelijk geeft.
- **Fase 0:** de trainer test het herschreven sjabloon opnieuw in de drie omgevingen.
- **ADR-006 en ADR-027 zijn deels vervangen.** De twee boards, de boardmomenten en de vorm als skill blijven. De samenstelling en de rol van beide boards veranderen.

## Raakt

Deel 5.1 (spanning "twee boards"), 6.3, 9, 10, 11, 12; FR-06, FR-17, FR-19, FR-32 (nieuw); AC-12; werkplaats 1 (opdracht); programma dag 1 (Stakeholders, nieuw blok om 12:15, lunch, werkplaats 1); `DATA.boardMoments`; risico's (twee aangepast, één nieuw); `materiaal/boards.html`; `materiaal/draaiboek-bouwstenen.md`; ADR-006; ADR-027.
