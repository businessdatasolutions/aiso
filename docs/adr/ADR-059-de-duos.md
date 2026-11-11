# ADR-059: De duo's: functie, samenstelling en momenten op één plek

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-11 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De duo's staan in elf blokken van het programma, in FR-08 en in zes risico's. Nergens stond bij elkaar waarvoor het duo
dient, hoe het ontstaat en wat het op elk moment doet. Deel 4 had één alinea: drie vaste duo's, waar mogelijk de
buddy's uit de leeromgeving. Voor het geval dat er geen buddy's zijn, was er geen regel.

## Besluit

- **Functie.** Het duo is de eerste lezer van het werk van de ander. Het vergelijkt, het toetst vóórdat de AI dat doet,
  en het controleert wat de AI schreef. Het schrijft niet mee, en bij een verschil van mening beslist de deelnemer.
- **Samenstelling.** De trainer maakt de duo's vóór dag 1. Eerst de buddy's uit de leeromgeving. Zijn die er niet, dan
  twee deelnemers met een verschillende rol of sector: wie de organisatie niet kent, vraagt naar wat de ander
  vanzelfsprekend vindt. De duo's blijven drie dagen gelijk (FR-08). Bij een oneven aantal wordt één duo een trio.
- **Momenten.** Een blok waarin het duo samenwerkt, krijgt in `DATA.days` het veld `duo`: één of twee zinnen over wat
  het duo daar doet. Deel 4 toont die velden als tabel.

## Overwogen alternatieven

- **Een vaste tabel in de tekst van deel 4.** Verworpen: bij een wijziging van het programma loopt ze achter.
- **Duo's uit dezelfde sector.** Verworpen: wie de organisatie van de ander herkent, vraagt minder door.
- **Elke dag een ander duo.** Verworpen: het duo moet de vragenkaart en het deck van de ander over drie dagen volgen.

## Gevolgen

- Wie een blok wijzigt waarin het duo werkt, past ook het veld `duo` aan.
- De startpagina toont het veld niet. De werkkaart noemt het duo al in de stappen.

## Raakt

- Deel 4 (De duo's) en `DATA.days`: het veld `duo` in elf blokken.
- FR-08, FR-09 en `materiaal/draaiboek-bouwstenen.md` (voorbereiding).
