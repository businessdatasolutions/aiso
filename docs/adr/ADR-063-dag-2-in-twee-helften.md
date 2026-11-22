# ADR-063: Dag 2 in twee helften, dag 3 begint met presentaties, en het comité verdeelt geen budget

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-13 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-061 bracht transformeren naar dag 2, maar alleen in de presentatie voor het investeringscomité. De rest van de
ochtend ging over investeren, en het model van Warner en Wäger (ADR-056) stond op dag 3 om 9:45, in een blok van 45
minuten samen met het hele transformatieplan. De trainer wil op dag 2 de hele ochtend aan transformeren besteden en
de middag aan investeren, en het model daar introduceren.

Tussen dag 2 en dag 3 voeren de deelnemers het experiment uit en leggen het vast. Dag 3 opende daarmee in duo's, één
minuut per persoon. De trainer wil dat dag 3 net als dag 2 met presentaties begint.

Het comité verdeelde aan het eind tien fiches over de voorstellen (ADR-037). Naast de rolkaarten en de eigen criteria
was dat een derde ding in één blok. De trainer vindt dat te ingewikkeld.

## Besluit

- **De ochtend van dag 2 is voor transformeren.** Na de opening (9:30) en het investeringscomité (9:40) volgt om 11:00
  het model van Warner en Wäger, waar elke deelnemer de sterkste rem en de zwakste aanjager kiest. Om 11:45 volgt het
  transformatieplan met 7S: per onderdeel één actie, en werkregels voor het eigen team.
- **De middag van dag 2 is voor investeren.** In de lunch zoekt de AI materiaal over het knelpunt. Om 13:30 volgen
  klein inzetten en de probleemformulering, in een half uur. Werkplaats 2 duurt een uur, van 14:00 tot 15:00: de AI
  schrijft de businesscase en het voorstel voor het experiment, en de deelnemer kiest een ontwerp en legt de normen
  vast.
- **Huiswerk voor dag 3:** het experiment uitvoeren en vastleggen in het paper, de kansenkaart tekenen, en een
  presentatie van hooguit vijf minuten voorbereiden.
- **Dag 3 begint met presentaties (FR-42).** Na een opening van tien minuten presenteert elke deelnemer het
  experiment in hooguit vijf minuten, met vijf minuten vragen van de groep. De groep let op twee dingen: lag de norm
  vast vóór de uitkomst, en volgt het besluit uit norm en uitkomst? De roadmap schuift naar 11:00 en governance naar
  11:45, elk 45 minuten.
- **Het draagvlak blijft op dag 3.** De acties per stakeholder en de vier vragen bij weerstand gaan naar werkplaats 3,
  waar de AI de scepticus speelt. Ze steunen op de online voorbereiding van bijeenkomst 3.
- **Het comité verdeelt geen budget meer.** De fiches vervallen. Het comité stelt vragen vanuit de rolkaarten en
  toetst aan de eigen criteria.

## Overwogen alternatieven

- **De kansenkaart in de les houden.** Verworpen: de middag heeft daar geen ruimte voor. De lespagina doet het voor
  met Voorbeeld BV, dus het kan thuis.
- **Werkplaats 2 op anderhalf uur houden en het blok van 13:30 schrappen.** Verworpen: zonder probleemstelling toetst
  de businesscase een oplossing, en zonder reële opties mist het experiment zijn reden.
- **Het hele transformatieplan op dag 2, ook de stakeholders.** Verworpen: de top 3 stakeholders en de stof over
  weerstand komen uit de online voorbereiding van bijeenkomst 3, en die is op dag 2 nog niet gedaan.
- **De fiches houden, als keuze tussen verkennen en benutten.** Verworpen door de trainer: het maakt het blok te
  ingewikkeld.

## Gevolgen

- Investeren krijgt op dag 2 anderhalf uur in plaats van drie. De kansenkaart, de eerste proef en het zelf scoren
  van gevallen zijn huiswerk. Het zetten van alle kansen op de portfoliokaart vervalt; de deelnemer kijkt alleen naar
  het besluit bij de eerste prioriteit.
- Het huiswerk vóór dag 3 is zwaarder: experiment, paper, kansenkaart en presentatie. Daar is een risico voor
  toegevoegd.
- Werkplaats 2 wijkt af van het vaste ritme van anderhalf uur (FR-04).
- De roadmap krijgt op dag 3 vijf minuten minder en governance tien.
- Het comité kiest niet meer zelf tussen verkennen en benutten. Die keuze komt nog wel terug om 13:30, bij de deur
  die terug kan.
- ADR-056 blijft gelden voor het model; alleen de plek verschuift naar dag 2. Van ADR-062 vervalt het blok Klein
  inzetten om 11:00. Van ADR-037 vervalt punt 4, het budget van het comité. Van ADR-061 vervalt het comité als blok
  bij vraag 3: het hoort nu bij vraag 2.

## Raakt

- `DATA.days`: dag 2 vanaf 9:30, dag 3 tot en met de werkplaats. `DATA.vragen` (V2, V3), `DATA.workshops`.
- FR-04, FR-09, FR-14, FR-21, FR-24, FR-27, FR-35, FR-38 en FR-39 (gewijzigd), FR-42 (nieuw). AC-04, AC-05 en AC-16
  (gewijzigd), AC-25 (nieuw). Twee risico's, een KISS-keuze, de opleverlijst van de trainer, fase 2, deel 6 en deel 8.
- `materiaal/transformeren.html`, `probleemformulering.html`, `experimentpaper.html`, `presentatie-dag2.html`,
  `volwassenheidsscan.html`, `voorbeeldcasus.md` en `draaiboek-bouwstenen.md`.
