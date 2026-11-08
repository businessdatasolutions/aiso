# ADR-046: De startpagina toont de vragen voluit en wijst elk stuk aan

| | |
|---|---|
| **Status** | Deels vervangen door [ADR-047](ADR-047-werkkaart-en-trainersweergave.md): de looptekst en de link naar het draaiboek wijken voor een werkkaart en een eigen weergave voor de trainer |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Op de startpagina staat om 9:30 "Opening: je casus en de vier vragen". De vier chips in de band lichten op, maar alleen met een kort woord: Richting, Transformeren, Investeren, Roadmap. De vraag zelf stond alleen in een tooltip, en die zie je op een beamer niet. Nergens stond dat de vragen op de geprinte vragenkaart staan.

We hebben de site bekeken met twee gebruikers in gedachten:

- een trainer die de lesdagen voor het eerst geeft en ze niet heeft ontworpen;
- een deelnemer die zijn aandacht nodig heeft voor de inhoud, niet om de site te leren kennen.

Per gebruiker zijn er vier fasen. Per fase meten we vier KPI's, kengetallen met een norm: is het er, is het te vinden, is het te begrijpen en werkt het. In de nulmeting haalden 18 van de 32 KPI's de norm ([verslag](../../onderzoek/2026-11-08-ux-startpagina.md)). Het laagst scoorden:

- de vragen voluit in beeld (48 %);
- een vindplaats voor elk stuk dat een blok noemt (31 %);
- de looptekst per blok (0 %);
- de weg naar het draaiboek (geen).

## Besluit

- **De vragen van het blok staan voluit in de kop.** Het gaat om alle vragen van het blok, niet alleen als het er één is. Eronder staat dat ze ook op de geprinte vragenkaart staan, dia 1 van het casusdeck. De chips in de band blijven.
- **Het materiaal van het blok van nu staat ook in de kop.** Wie de pagina opent, opent het materiaal met één klik, zonder te scrollen.
- **Elk stuk dat een blok noemt, staat als materiaal bij dat blok.** De vragenkaart staat bij elk blok dat de kaart, de nulmeting of de vier vragen noemt. De tegel linkt naar `materiaal/casusdeck.html`. Het deckblok van dag 2 krijgt de prompt voor de businesscase en het experimentpaper. Twee kale labels zeggen nu wat er achter zit.
- **Per blok staat de looptekst uit de LRD (`detail`), uit te klappen.** Bij het blok van nu staat hij open. Codes als (FR-21) haalt de startpagina eruit.
- **De voet linkt naar het draaiboek** in de openbare repo op GitHub. Het draaiboek zelf komt niet op de site (ADR-045).
- **Vier lespagina's krijgen bovenaan een link terug naar de startpagina.** Uit de vraagtoets gaat de code FR-37. Op een telefoon mag een lang menupad in `boards.html` afbreken.
- **`scripts/meet-ux.py` meet de 32 KPI's.** Met `--toets` is het de toets voor elke wijziging aan de startpagina, de lespagina's of het programma in `DATA`.

## Overwogen alternatieven

- **De vraag tonen bij een klik op de chip.** Verworpen: een deelnemer moet dan weten dat de chip klikbaar is. Op de beamer klikt bovendien alleen de trainer.
- **De tegel naar `vier-vragen.html` in de opening.** Verworpen: die pagina toont het voorbeeld van Voorbeeld BV, en dat zien de deelnemers pas om 11:32. De nulmeting gaat zonder hint.
- **Een aparte trainersweergave, zoals `?rol=trainer`, met de looptekst.** Verworpen: een invaller kent die parameter niet. Een dichte uitklap kost een deelnemer niets.
- **Het draaiboek op de site zetten.** Verworpen: trainersstukken horen niet op de site (ADR-045). Een link naar de openbare repo maakt niets openbaar wat het niet al was.

## Gevolgen

- De kop is hoger. Op een laptop (1366×768) staan het blok van nu, de vragen en het materiaal nog steeds boven de vouw. Dat meet KPI D1-V.
- Een deelnemer kan vóór de nulmeting de looptekst van een later blok openklappen. Hij staat dicht, en de nulmeting duurt acht minuten op papier. Dat risico nemen we.
- De tegel "Vragenkaart" opent het lege casusdeck. Dia 1 daarvan is de lege vragenkaart. Wie de geprinte kaart kwijt is, kan hem daar opnieuw printen.
- Deel 8 van de LRD toont het nieuwe materiaal ook in het detailpaneel.

## Raakt

- `materiaal/index.html` (de startpagina), NFR-09 en FR-33.
- Het materiaal in `DATA.days`:
  - dag 1: de opening, 11:00, het deckblok en de afsluiting;
  - dag 2: de opening, het deckblok en de afsluiting;
  - dag 3: de opening en de afsluiting.
- `materiaal/boards.html`, `experimentpaper.html`, `probleemformulering.html` en `vraagtoets.html`.
- `scripts/meet-ux.py`.
