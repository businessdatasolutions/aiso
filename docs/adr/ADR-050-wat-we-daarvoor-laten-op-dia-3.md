# ADR-050: Dia 3 krijgt een vak voor wat de organisatie daarvoor laat

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De vraagtoets (ADR-039) noemt een AI-vraag strategisch als het antwoord bepaalt welke plek de organisatie
inneemt, en wat ze daarvoor laat. Het criterium Keuze scoort pas een 2 als de organisatie iets laat.
In het casusdeck had dat laten geen plek. Dia 3 vraagt per doel om een loslaatsignaal, maar dat is iets
anders: een loslaatsignaal zegt wanneer je een doel opgeeft. Wat de organisatie laat, zegt welke keuze ze
maakt om het doel te halen.

In de proefrun van dag 1 (8 november 2026) vroegen de supervisory board (drie keer), de advisory board, de
AI die het deck invulde en het duo samen vijf keer om dit punt. De deelnemer had het wel in haar vraag en
in haar visie staan, maar niet op de dia. Dia 3 is wat ze aan haar directie laat zien.

## Besluit

- Dia 3 krijgt onder de doelkaarten een vak over de volle breedte: **Wat we daarvoor laten**. De plaatshouder
  vraagt wat de organisatie niet meer of niet doet om de doelen te halen, in hooguit twee zinnen.
- De instructie voor de AI bovenaan het deck zegt dat dit vak altijd blijft staan, ook als de doelkaarten
  3 en 4 weg mogen.
- De pauzetaak van 15:00 op dag 1 vraagt de AI om de tekst voor dia 3 te maken met wat de organisatie
  daarvoor laat.
- Voorbeeld BV laat het vaste contract als installateur van één fabrikant. Het werkt voor een fabrikant
  alleen per opdracht, zodat de klant van Voorbeeld BV blijft. Dat volgt uit vraag C van de vraagtoets en
  uit de optie die de deur openhoudt op de lespagina Waarom geen plan volstaat.

## Overwogen alternatieven

- **Op dia 2, Aanleiding.** Verworpen: dia 2 zegt waarom het nu speelt. De keuze hoort bij de doelen.
- **Een vijfde kaart naast de doelen.** Verworpen: met vier doelen is er geen ruimte, en laten is geen doel.
- **Alleen in de strategische vraag.** Verworpen: de vraag mag met "Of …" de keuze noemen, maar de dia's
  gaan naar de stakeholders. Daar moet de keuze zichtbaar zijn.
- **Op de vragenkaart.** Verworpen: de kaart is voor de vier vragen en hun groei, niet voor de doelen.

## Gevolgen

- De doelkaarten worden lager. Getest met drie doelen uit de proefrun en twee zinnen in het nieuwe vak:
  geen rode rand, en de PDF telt nog tien pagina's van 960 × 540.
- Het lege deck op de downloadpagina (`aiso-casusdeck`) moet dezelfde versie krijgen.
- Een deck dat vóór deze versie werd ingevuld, mist het vak. Op 8 november heeft nog geen deelnemer een deck.

## Raakt

- `materiaal/casusdeck.html`: dia 3 en regel 7 van de instructie voor de AI; ook de kopie op de downloadpagina.
- `DATA.deck`: de naam van dia 3.
- `DATA.days`, dag 1 om 15:00: de AI-taak.
- Deel 2 (waarvoor de deelnemer komt): het voorbeeld van Voorbeeld BV bij de doelen.
- `materiaal/voorbeeldcasus.md`: de doelen van Voorbeeld BV.
