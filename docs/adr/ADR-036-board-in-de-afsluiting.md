# ADR-036: Het board toetst in de afsluiting, zonder boardmoment en zonder ADR

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In versie 0.21 eindigde elk deckblok met een boardmoment van 15 minuten, met een ADR. Tussen dag 1 en dag 2 legde de deelnemer de pitch thuis voor aan het supervisory board (FR-19).

De gebruiker koos op 8 november om de twee boards te houden. Het aparte boardmoment en de ADR vervallen. Het board toetst in de afsluiting het antwoord dat die dag het meest veranderde.

## Besluit

- **Geen boardblokken meer.** Het bloktype `board` vervalt.
- **FR-18 herschreven.** In de afsluiting gaat het antwoord dat het meest veranderde naar het board dat erbij past. Bij vraag 1 en 2 is dat het supervisory board, bij vraag 3 en 4 het advisory board. Wat het board zegt en wat de deelnemer ermee doet, komt op de vragenkaart.
- **FR-19 en `DATA.boardMoments` vervallen.**
- **`materiaal/boards.html`:**
  - stap 6 heet "Je boards gebruiken";
  - de skills sluiten af met twee regels voor de vragenkaart, in plaats van drie regels voor een ADR.

## Overwogen alternatieven

- **Eén board.** Verworpen door de gebruiker: strategie en vakkennis lopen dan door elkaar.
- **Geen boards.** Verworpen door de gebruiker: SN1 verliest een oefening.
- **De boardmomenten houden.** Verworpen: ze deden hetzelfde als de afsluiting.

## Gevolgen

- **Elke dag 15 minuten vrij.** De afsluiting duurt 30 minuten, en het deckblok op dag 3 duurt 45 minuten.
- **De vergelijking van het AI-board met het comité op dag 2 vervalt** (FR-19).
- **Nog niets uitgedeeld.** Deelnemers hebben de skills nog niet gedownload, dus er is geen oude versie in omloop.

## Raakt

Deel 6.4, 8, 9, 11 en 12; FR-17, FR-18 en FR-19; AC-05 en AC-12; `materiaal/boards.html` en `materiaal/index.html`. Vervangt deels ADR-006.
