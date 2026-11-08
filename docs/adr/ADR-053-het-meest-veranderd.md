# ADR-053: "Het meest veranderd" is wat je nu anders kiest of laat; het duo krijgt drie minuten

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In de afsluiting van elke lesdag gaat het antwoord dat het meest veranderde naar een board (FR-18, ADR-036). Op dag 1
kiest het duo dat antwoord, in de laatste twee minuten van het herschrijven (ADR-051).

In de tweede proefrun van dag 1 (8 november 2026) vroeg het duo of het om de inhoud of om de lengte ging (issue #4).
Ze kozen uiteindelijk goed. Wel hadden ze meer tijd nodig dan de twee minuten, en het blok kreeg voor de tijd "krap".

## Besluit

- **Wat "het meest veranderd" is.** Het antwoord waarin je nu iets anders kiest of laat dan bij de vorige stand. Een
  langer of preciezer antwoord telt niet als meer veranderd. Dat staat in FR-18, en op de werkkaart van alle drie de
  afsluitingen onder "aandacht".
- **Dag 1: het duo krijgt drie minuten.** Het herschrijven loopt van 16:03 tot 16:11, zoals eerst. Om 16:11 kiest het
  duo, en de board begint om 16:14 in plaats van 16:13.
- **Dag 2 en 3** krijgen alleen de omschrijving. Dat het duo kiest, geldt nog steeds alleen op dag 1 (ADR-051).

## Overwogen alternatieven

- **Het herschrijven een minuut korter maken.** Verworpen: in beide proefruns was het herschrijven van vier
  antwoorden al krap.
- **"Toen en nu" een minuut korter maken.** Verworpen: dat is het enige moment van de afsluiting waarop de groep
  samen iets hoort, met de vraag van de trainer erbij.
- **Alleen de omschrijving, zonder extra tijd.** Verworpen: ook met een duidelijke omschrijving vergelijkt het duo
  vier antwoorden per persoon. Dat lukt niet in twee minuten.

## Gevolgen

- De board heeft op dag 1 negen minuten in plaats van tien. Met de grens van 1200 woorden is dat krap: de deelnemer
  leest eerst de conclusie en het advies.
- Op de werkkaart van dag 2 verdwijnt "Een antwoord dat bleef staan, mag ook" onder "aandacht", door de grens van
  30 woorden. Onder "koers" staat nog steeds dat "niet veranderd" mag.

## Raakt

- FR-18.
- `DATA.days`, dag 1 om 16:00: de beschrijving van het blok, "aandacht" en het verloop om 16:03, 16:11 en 16:14.
- `DATA.days`, dag 2 en 3 om 16:00: "aandacht".
- ADR-051: aangevuld, niet vervangen.
