# ADR-017: Pseudoniemen voor deelnemers

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-016 haalde de organisaties van deelnemers uit de documenten, maar liet voornamen met een rol staan. Een zeldzame voornaam met een functie kan zelf al een persoonsgegeven zijn. ADR-016 noemde pseudoniemen als alternatief dat nog niet besloten was.

## Besluit

Documenten die we bouwen noemen deelnemers met een pseudoniem: Deelnemer A t/m F, in de volgorde van de deelnemerslijst. De sleutel staat alleen in `temp/pseudoniemen.md`. Links naar inzendingen van afzonderlijke deelnemers verdwijnen, omdat de bestandsnaam de naam verraadt; de LRD verwijst naar de map `temp/` als geheel. Dit vult ADR-016 aan.

## Overwogen alternatieven

- **Voornamen met een algemene rol laten staan.** Bij een zeldzame naam herleidbaar.
- **Initialen.** Bij zes deelnemers bijna even herleidbaar als de naam.

## Gevolgen

- De LRD bevat geen namen en geen organisaties van deelnemers meer.
- Wie de LRD gebruikt, heeft `temp/pseudoniemen.md` nodig om een deelnemer te herkennen.
- Eerdere versies van het artifact bevatten de voornamen nog in de versiegeschiedenis.

## Raakt

Kop (gerelateerde documenten), deel 1 (open punten), deel 4 (deelnemers), bronnen, `temp/pseudoniemen.md`, `CLAUDE.md`, skill `aiso-building-lrds`.
