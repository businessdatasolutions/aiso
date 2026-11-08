# ADR-052: De vraagtoets krijgt een lezing voor publieke organisaties en een oefenvraag van een gemeente

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In de tweede proefrun van dag 1 (8 november 2026) werkte de fictieve deelnemer als adviseur data en AI bij een
gemeente (issue #3). De vraagtoets van ADR-039 is geschreven voor een bedrijf:

- Positie 2 vraagt "waarmee de organisatie zich onderscheidt". Een gemeente heeft wettelijke taken en geen concurrent.
- Keuze 2 vraagt of "de organisatie iets laat". Bij een gemeente bepalen de wet en de raad mee wat ze laat.
- De drie oefenvragen en de negen vragen van de ijkset komen allemaal van een bedrijf.

Deelnemer en duo vonden met moeite toch een strategische vraag. Het blok van 11:40 kreeg voor helderheid een 3 van
5, het laagste van de dag. Een deelnemer uit de publieke sector zonder zo'n duo loopt hier vast.

## Besluit

- **Eén schaal, met een lezing voor publieke organisaties onder niveau 2.**
  - Positie 2: welke rol de organisatie inneemt tegenover inwoners, ketenpartners en andere overheden.
  - Keuze 2: een taak, een kanaal of een rol die ze aan anderen overlaat.
  - Omgeving 2 noemt naast klanten ook inwoners.

  De lezing staat in de tabel met criteria, in de prompt van de vraagtoets en in de skilltekst van de supervisory
  board. De uitleg bij de definitie zegt dat een publieke organisatie vaak geen concurrent heeft, en dat haar plek de rol
  tegenover inwoners en ketenpartners is.
- **Oefenvraag D, van de verzonnen gemeente Voorbeeldstad.** D is alleen voor wie bij een publieke organisatie
  werkt; de groep oefent plenair op A, B en C. D is na de maquette van het ziekenhuis (ADR-040) de tweede
  uitzondering op de ene voorbeeldcasus. De vraag komt uit de ijkset, niet uit `voorbeeldcasus.md`.
- **De ijkset krijgt twee vragen van een gemeente.** Vraag 10 klinkt strategisch, maar er valt niets af. Vraag 11
  is oefenvraag D. De norm wordt tien van de elf.

## Overwogen alternatieven

- **Een aparte vraagtoets voor de publieke sector.** Verworpen: twee toetsen in één groep zijn niet te vergelijken,
  en een duo komt soms uit twee sectoren.
- **De criteria algemener maken, zonder "zich onderscheidt".** Verworpen: voor een bedrijf is het onderscheid de
  kern (Porter, 1996). Algemenere woorden maken de toets voor hen vager.
- **Een vierde oefenvraag die iedereen scoort.** Verworpen: het oefenen duurt drie minuten. D kost dan tijd van
  deelnemers die er niets aan hebben.
- **Het de trainer laten zeggen.** Verworpen: de deelnemer en de AI lezen de pagina en de prompt. Wat de trainer
  zegt, staat daar niet in.

## Gevolgen

- De trainer ijkt de prompt opnieuw, nu op elf vragen (FR-37), in fase 0.
- De skilltekst van de supervisory board verandert. Een deelnemer die de zip al installeerde, downloadt hem opnieuw.
- Het oefenen blijft drie minuten.
- De lezing voor publieke organisaties kan de AI ruimer laten scoren bij een vage vraag. Vraag 10 van de ijkset
  toetst dat.

## Raakt

- FR-36 en FR-37; de lijst van de trainer in deel 10.
- `DATA.days`, dag 1 om 11:40: de beschrijving van het blok, stap 1 van de werkkaart en het verloop om 11:42.
- `materiaal/vraagtoets.html`, `materiaal/vraagtoets-ijkset.md`, `materiaal/boards.html` en
  `materiaal/draaiboek-bouwstenen.md`.
- ADR-039: aangevuld, niet vervangen.
