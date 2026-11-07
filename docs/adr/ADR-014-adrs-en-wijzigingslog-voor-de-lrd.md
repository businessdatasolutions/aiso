# ADR-014: Besluiten en wijzigingen van de LRD in ADR's en een wijzigingslog

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-05 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In korte tijd zijn veel ontwerpbesluiten genomen, en een paar zijn teruggedraaid. De redenen stonden alleen in de chat. Ook de skill aiso-beoordeel-onderwijsontwerp vraagt om een besluitenregister als het project er een heeft.

## Besluit

Elk ontwerpbesluit krijgt een ADR in `docs/adr/`, met een register in `docs/adr/README.md`. Elke versie van de LRD krijgt een regel in `CHANGELOG.md`, en het versienummer in de kop van de LRD is gelijk aan de bovenste regel. Een besluit dat verandert, krijgt een nieuwe ADR; de oude krijgt de status 'Vervangen door'. De skill aiso-building-lrds doet dit voortaan standaard.

## Overwogen alternatieven

- **In de LRD zelf, als bijlagen.** Zichtbaar in het artifact, maar de trainer koos voor aparte bestanden.
- **Allebei.** Elk besluit op twee plekken.

## Gevolgen

- Het waarom van elk besluit is terug te vinden, ook als iemand anders de LRD opent.
- ADR's en log staan niet in het artifact; de LRD verwijst ernaar bij de projectdocumenten.
- Elke wijziging aan de LRD kost een ADR of logregel extra.

## Raakt

`docs/adr/`, `CHANGELOG.md`, versienummer in de kop, skill `aiso-building-lrds`.
