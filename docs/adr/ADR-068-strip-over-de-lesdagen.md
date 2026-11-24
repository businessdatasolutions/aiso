# ADR-068: Een strip legt vóór dag 1 uit hoe de lesdagen werken

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-24 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Een deelnemer die zich heeft ingeschreven, weet vóór dag 1 weinig van de lesdagen. De webpagina van S&N beschrijft
de training, en de online omgeving begint met de voorbereiding. Hoe de drie dagen in elkaar zitten, wat je meeneemt
en waarmee je naar huis gaat, staat alleen in de LRD en op de startpagina per lesdag. Die zijn geschreven voor het
moment zelf: per blok, met tijden.

## Besluit

- **Er komt een strip van twaalf plaatjes**, "Het plan dat werd ingehaald", op `materiaal/strip/`. De trainer stuurt
  de link vóór dag 1.
- **De volgorde is waarom, hoe, wat** (de Golden Circle van Sinek). Drie plaatjes laten een AI-plan zien dat wordt
  ingehaald. Vier plaatjes tonen de vier vragen en de werkwijze. Vier plaatjes tonen per lesdag wat de deelnemer
  doet, met het casusdeck als tien vakjes eronder. Het slot speelt in de kamer van het eerste plaatje.
- **De hoofdpersoon is verzonnen**: Noor, van Voorbeeld BV. Geen figuur is naar een deelnemer getekend, ook niet als
  mengvorm (ADR-016, ADR-017).
- **De beelden komen uit een beeldgenerator, met de tekst erin.** De trainer schreef het script en keurde het goed.
  Een schets per plaatje legt de opstelling en de plek van de tekst vast, en gaat met de prompt mee naar de generator.
  Elke tekst in een beeld is letter voor letter met het script vergeleken.
- **De praktische gegevens staan onder de strip, als gewone tekst**: wanneer, waar, wat je meeneemt en waarmee je
  naar huis gaat. Een volgende groep vraagt daardoor geen nieuw beeld.
- **Op de site komen alleen de leesversie en de lichte beelden** (1280 breed, samen 3 MB). Het script, de schetsen,
  de prompts en de werkversie staan in de repo. De originele beelden van 23 MB blijven buiten git.

## Overwogen alternatieven

- **De figuren tekenen als SVG in de huisstijl.** Gebouwd, en gehouden als schets. De tekeningen waren te stijf en te
  kaal: een beeldgenerator haalt een kwaliteit die met de hand geschreven SVG niet haalt.
- **De tekst als aparte laag over een beeld zonder tekst.** Gebouwd en nog beschikbaar per plaatje. Niet de
  standaard: de generator zette de tekst in alle twaalf beelden foutloos, en een ballon uit de generator past beter
  bij de tekening.
- **De volgorde van het programma: dag 1, dag 2, dag 3.** Verworpen: de lezer moet eerst het eigen probleem
  herkennen, en pas daarna het programma lezen.
- **Brede plaatjes.** Verworpen: op een telefoon wordt de tekst in een breed plaatje onleesbaar.

## Gevolgen

- **De nulmeting meet iets anders voor wie de strip las.** Plaatje 5 noemt het principe klein beginnen en opties
  openhouden. De nulmeting op dag 1 meet daarna of de deelnemer dat op de eigen organisatie toepast, en niet meer
  wat die zonder enige richting zou doen. De methoden achter de vier vragen staan niet in de strip.
- **Een wijziging in de tekst kost een nieuw beeld.** De wijziging begint in het script, daarna in de prompt, en het
  nieuwe beeld gaat opnieuw door de controle.
- **De strip gebruikt "raad van advies" voor de boards.** De lezer kent het woord "board" vóór dag 1 nog niet in
  deze betekenis en leert het op dag 1.
- **De strip is af op 24 november 2026, na dag 1 van deze groep.** Voor zijn doel komt hij bij deze groep te laat;
  hij is er voor een volgende groep. Het kader onder de strip noemt de data van deze groep.
- De strip is niet door een buitenstaander proefgelezen. Dat staat nog open in het bouwplan.

## Raakt

- LRD: FR-43 (nieuw) en `DATA.deliverables.trainer`.
- `materiaal/strip/` (nieuw): `index.html` (leesversie), `beeld/web/` (beelden), en als werkmateriaal `bouwplan.md`,
  `scenario.md`, `script.md`, `prompts.md`, `strip.html`, `figuren.js`, `figurenblad.html` en
  `karakterblad-gemini.html`.
- `scripts/bouw-pages.py`: de leesversie en de lichte beelden gaan mee naar de site.
- `.gitignore`: de originele beelden blijven buiten git.
