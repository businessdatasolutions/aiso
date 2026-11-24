# ADR-067: De opening van dag 2 vraagt wat ieder met AI deed, en toont het werk van de trainer

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-24 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Dag 2 opent om 9:30 met het overzicht van de vier vragen, de vragenkaart en de kwaliteitscriteria. In de opening
noemde de deelnemer "wat er sinds dag 1 gebeurde", maar de vraag naar het eigen gebruik van AI stond er niet in.
Werkregel 1 van dag 1 zegt dat je AI aan het werk zet voordat je pauze neemt. Tussen dag 1 en dag 2 liggen twee
weken: of de deelnemers die regel thuis volhielden, weet de trainer pas als hij het vraagt.

Op dag 1 stelde de trainer zich voor met zijn eigen werk (ADR-058). Voor dag 2 was er geen vervolg op.

## Besluit

- **De trainer vraagt om 9:32 wat ieder sinds dag 1 met AI deed**, één zin per persoon. Hij stelt de vraag zelf. Er
  is geen pagina bij, en niemand turft of noteert de antwoorden.
- **Daarna laat hij zijn eigen werk van die twee weken zien** op de nieuwe lespagina `materiaal/sinds-dag-1.html`:
  per project de commits per dag en één zin over wat het opleverde. De bron is git: de eigen commits zonder merges
  van 13 tot en met 24 november 2026.
- **De pagina noemt geen privéprojecten bij naam**, en geen klanten, leveranciers of deelnemers. Dat is dezelfde
  regel als bij Even voorstellen (ADR-058).
- **De vragenkaart krijgt twee minuten in plaats van vijf.** De opening blijft tien minuten.

## Overwogen alternatieven

- **Een pagina met de vraag en een turflijst voor de antwoorden van de groep.** Gebouwd en weer weggehaald: de
  trainer stelt de vraag liever zelf, en turven haalt de aandacht van het gesprek naar het scherm.
- **Eén blokje per commit in 3D, zoals de repos op dag 1.** Gebouwd en weer weggehaald: het beeld zegt hetzelfde als
  de figuur per project, en twee beelden passen niet in drie minuten.
- **De opening vijf minuten langer maken.** Verworpen: het investeringscomité begint om 9:40 en heeft de tijd tot
  10:45 nodig.

## Gevolgen

- De vragenkaart krijgt in de opening minder tijd. De kaart komt aan het eind van de dag terug.
- De cijfers op de pagina zijn een momentopname van 24 november. Werkt de trainer daarna nog door, dan past hij de
  lijst `PROJECTEN` en de vaste getallen in de pagina aan.
- De pagina is een lespagina en gaat mee naar de openbare site.

## Raakt

- LRD: `DATA.days`, dag 2, het blok van 9:30 (detail, materials, deelnemer, trainer).
- `materiaal/sinds-dag-1.html` (nieuw).
- `materiaal/index.html` rendert de materials; die code verandert niet.
