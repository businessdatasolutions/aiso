# ADR-069: Het overzicht van de vier vragen linkt naar de strip

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-24 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De strip "Het plan dat werd ingehaald" (ADR-068) was alleen bereikbaar via de link die de trainer vóór dag 1
verstuurt. Op de startpagina en in de LRD stond geen link. Een deelnemer die de mail mist, ziet de strip daardoor
nooit, en op een lesdag kan niemand hem terugvinden.

## Besluit

- **De link staat in de kop van het overzicht van de vier vragen** (`?weergave=overzicht`, ADR-057), als laatste zin
  van de inleiding: "Het verhaal achter de vier vragen lees je in de strip."
- **De strip verwijst onderaan terug naar het overzicht.**
- **De mail van de trainer blijft de hoofdroute** (FR-43). De link in het overzicht vangt de gemiste mail op.

## Overwogen alternatieven

- **Een regel boven het programma van dag 1.** Verworpen: wie de strip om 9:30 opent, leest het principe van
  plaatje 5 vlak voor de nulmeting van 10:00.
- **Een stille link in de voettekst van de startpagina.** Verworpen: vindbaar voor wie zoekt, maar los van de
  inhoud. Het overzicht vertelt hetzelfde verhaal als de strip: vier vragen over drie dagen.
- **Een extra rij onder de tabel.** Verworpen: het overzicht moet zonder scrollen op de beamer passen.

## Gevolgen

- **De link staat ook op het scherm bij de opening van dag 1**, een half uur voor de nulmeting. De trainer klikt
  hem daar niet aan. Een deelnemer die het overzicht op het eigen scherm opent, kan dat wel doen; voor die
  deelnemer geldt het gevolg uit ADR-068.
- De inleiding van het overzicht is één zin langer. De tabel past nog op de beamer (controle W3 van de UX-test).

## Raakt

- LRD: FR-43 (tekst aangevuld).
- `materiaal/index.html`: de inleiding van het overzicht.
- `materiaal/strip/index.html`: de voettekst.
