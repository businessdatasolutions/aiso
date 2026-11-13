# ADR-062: De presentatie voor het comité heeft een tijdslimiet: vijf minuten presenteren, vijf minuten vragen

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-13 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-061 gaf elke presentatie voor het investeringscomité vier minuten, met drie minuten vragen. Zo pasten zes
presentaties in het blok van 9:40 tot 10:30. De trainer wil een vaste limiet van vijf minuten presenteren en vijf
minuten vragen. Zes presentaties duren dan een uur, en dat past niet in vijftig minuten.

## Besluit

- **Hooguit vijf minuten presenteren, daarna vijf minuten vragen.** Een timer in beeld bewaakt beide, en de trainer
  stopt wie over de tijd gaat.
- **Het comité loopt van 9:40 tot 10:45.** Zes presentaties duren tot 10:40. Daarna volgen de fiches en werkregel 1.
- **De pauze schuift naar 10:45, en het blok Klein inzetten naar 11:00.** Dat blok duurt 30 minuten in plaats van 45.
  Het begint direct bij de reële opties, het zelf doen duurt 12 minuten, en één deelnemer leest een kans voor.
- **Het blok van 11:30 blijft staan**, met de probleemformulering, de kansenkaart en de businesscase.
- **Bij zeven of acht presentaties**: vier minuten presenteren en drie minuten vragen.

## Overwogen alternatieven

- **Het kwartier bij het blok van 11:30 weghalen.** Verworpen: dat blok loopt al het risico uit te lopen, en het
  voorstel voor het experiment in de lunch steunt op de businesscase.
- **De opening van 9:30 laten vervallen.** Verworpen: elke lesdag opent met de vier vragen, en de criteria moeten op
  tafel liggen vóór de eerste presentatie.
- **De pauze inkorten.** Verworpen: in de pauze werkt de AI aan het onderzoek voor 11:30.

## Gevolgen

- Het blok Klein inzetten verliest een kwartier. De terugblik op wat de AI vond, vervalt daar; dat onderzoek komt om
  11:30 aan bod.
- Tijden in andere teksten schuiven mee: de AI-taak van 10:30 heet nu de AI-taak van 10:45, en het blok van 10:45
  het blok van 11:00.
- ADR-061 blijft gelden, behalve de duur van de presentatie en de vragen en de eindtijd van het comité.

## Raakt

- `DATA.days`: dag 2 om 9:40, 10:45, 11:00 en 11:30. FR-09, FR-41, FR-39, de opdracht van werkplaats 2, de
  opleverlijst van de trainer en één risico.
- `materiaal/presentatie-dag2.html`, `materiaal/probleemformulering.html` en `materiaal/experimentpaper.html`.
