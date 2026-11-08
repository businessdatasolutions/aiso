# ADR-034: De bouwstraat vervalt; de onderdelen van het deck zijn de producten

| | |
|---|---|
| **Status** | Deels vervangen door [ADR-041](ADR-041-experiment-als-paper.md): het experiment krijgt weer een paper, en dat schrijft de AI |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De gebruiker zei op 8 november dat de vijf documenten van de bouwstraat dezelfde dingen zijn als de onderdelen van het deck. Het gaat om de businesscase, de PRD, het experimentverslag, de blueprint met het buildplan, en de ADR met het wijzigingslog.

De integrale opdracht van S&N vraagt negen onderdelen in hooguit tien dia's. In versie 0.21 stonden randvoorwaarden en risicoanalyse samen in één onderdeel, en had het experiment geen eigen plek in het deck.

## Besluit

- **Deel 6.4 vervalt,** met `DATA.pipeline` en `DATA.examples`.
- **Eisen eruit:**
  - FR-22 (de blueprint);
  - FR-23 (de vijf sjablonen);
  - FR-25 (het ADR-register en het wijzigingslog van de deelnemer);
  - AC-17.
- **FR-20** gaat alleen nog over het ontwerp van het experiment, zonder PRD en zonder de keuze uit de kennisvormen.
- **FR-21:** de uitkomst van het experiment komt op de dia Eerste prioriteit. Daar staan de vraag, de norm, de uitkomst en het besluit, met hooguit één grafiek. Er is geen apart interactief verslag meer.
- **FR-15:** het buildplan heet nu roadmap voor jaar 1. Elke gate krijgt een uitwijkroute.
- **Het deck telt tien dia's.** Eerst de vragenkaart, dan de negen onderdelen apart, zoals S&N ze noemt. Randvoorwaarden en risicoanalyse zijn weer twee dia's. De Conclusie is op dag 3 een concept.
- **Wat blijft:** het experiment, de experimenttypen, Ask, Assist en Automate, en de kansenkaart. Die staan in een nieuw deel 6.5.
- **Kennisvormen:** `kennisvormen.html` gaat uit het programma; het bestand blijft bestaan.
- **Bronnen eruit:** die van de AI-bedrijven, en Nygard en Lacan.

## Overwogen alternatieven

- **De documenten als bijlagen bij het deck houden.** Verworpen: dan staat hetzelfde werk weer op twee plekken.
- **Het interactieve verslag houden.** Verworpen: dat is extra thuiswerk, en het HTML-deck kan zelf een grafiek dragen.
- **De vragenkaart en de Conclusie samenvoegen om een dia te sparen.** Verworpen: de vragen horen drie dagen vooraan te staan.

## Gevolgen

- **Minder thuiswerk.** Tussen dag 2 en 3 blijft alleen het experiment over.
- **Minder oefening met hoe AI-bedrijven bouwen.** De deelnemers oefenen niet meer met de PRD en de blueprint. SN3 wordt gedragen door het experiment en de roadmap.
- **Vervangen ADR's:**
  - ADR-007 en ADR-009 zijn vervangen.
  - ADR-015 is vervangen: de vragenkaart neemt de plaats in van het ADR-register.
  - ADR-012 is deels vervangen: de PRD vervalt, maar het herontwerp van het werkproces blijft in de kansenkaart, de businesscase en de gates.

## Raakt

Deel 5.1, 6 (6.4 vervalt, 6.5 is nieuw), 7, 8, 9, 10, 11, 12 en de bronnen; `DATA.deck`, `moments`, `pipeline` en `examples`; FR-15, FR-20, FR-21, FR-22, FR-23 en FR-25; AC-01, AC-06, AC-14, AC-15 en AC-17. Vervangt ADR-007, ADR-009 en ADR-015, en deels ADR-012.
