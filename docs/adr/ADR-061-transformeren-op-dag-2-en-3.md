# ADR-061: Transformeren komt op dag 2 en dag 3 terug, met een presentatie voor het investeringscomité

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-13 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Na dag 1 kwam er feedback van de deelnemers: ze willen meer aandacht voor transformeren, vraag 2. In het programma
was vraag 2 alleen de hoofdvraag van dag 3, in één blok van 45 minuten om 9:45. Dag 2 ging over vraag 3, investeren.

Dag 2 opende al met een investeringscomité (FR-09): elke deelnemer hield de pitch uit de online omgeving, en het
comité stelde vragen vanuit rolkaarten van de trainer. Deel 9 zei daarbij dat de trainer de rolkaarten en de vragen
maakt, en de deelnemers niet.

## Besluit

- **Vraag 2 is hoofdvraag op dag 2 en op dag 3.** Dag 2 heet "Vraag 2 en 3: transformeren en veilig investeren". In
  `DATA.vragen` is `dag` bij vraag 2 een lijst: `[2, 3]`. Het overzicht van de vier vragen toont de hoofdvraag op
  beide dagen.
- **Een opdracht vóór dag 2 (FR-41).** Elke deelnemer bereidt thuis met AI een presentatie van vier minuten voor, voor
  het investeringscomité van de eigen organisatie. De andere deelnemers zijn dat comité. De presentatie heeft drie
  delen: het probleem en de gevraagde investering, wat er in de organisatie verandert en wat moet blijven werken, en
  het bewijs. Het tweede deel is vraag 2.
- **Vier kanalen als startpunt, en zelf verder zoeken.** De trainer geeft de YouTube-kanalen van McKinsey, Boston
  Consulting Group, Bain en Harvard Business Review. De deelnemer zoekt zelf tekst, data en video: minstens één van
  elk, waarvan minstens één bron van buiten de vier kanalen.
- **De deelnemers krijgen de skill `ontwerp-dia` mee.** Het is de skill waarmee de trainer zijn eigen dia's maakt,
  herschreven voor een spreker voor een comité: de dia draagt het bewijs, de spreker het verhaal. De lespagina biedt
  hem aan als zip en als tekst. De teller in Python en de verwijzingen naar het deck van de trainer zijn eruit; de AI
  telt zelf. De skill is een hulpmiddel en geen eis.
- **De deelnemers schrijven hun eigen kwaliteitscriteria.** Elke deelnemer bedenkt thuis waar die op wil letten en
  maakt daar drie toetsbare criteria van. Toetsbaar betekent: twee comitéleden komen los van elkaar tot hetzelfde
  oordeel. De criteria liggen op tafel vóór de eerste presentatie, en de eigen presentatie voldoet eraan.
- **Het blok van 9:30 op dag 2 wordt twee blokken.** Van 9:30 tot 9:40 de opening met de vier vragen en de criteria.
  Van 9:40 tot 10:30 het investeringscomité, bij vraag 2 en 3. Een presentatie duurt vier minuten, de vragen drie.
  De oordelen langs de criteria gaan op schrift naar de presentator.
- **Dag 3 bouwt erop voort.** Het blok van 9:45 begint bij de oordelen van het comité over wat de investering van de
  organisatie vraagt.
- **De opdracht staat op een lespagina**: `materiaal/presentatie-dag2.html`. De trainer stuurt de link.

## Overwogen alternatieven

- **Het model van Warner en Wäger naar dag 2 verplaatsen.** Verworpen: dag 2 heeft daar geen ruimte voor zonder de
  probleemformulering of de businesscase in te korten, en het transformatieplan van dag 3 begint bij dat model.
- **Een beoordelingsformulier van de trainer.** Verworpen: wie zelf criteria schrijft, moet eerst bepalen wat een goed
  voorstel is. Een formulier neemt dat denkwerk weg.
- **De rolkaarten laten vervallen.** Verworpen: de kritiekpunten op de rolkaarten hebben bronnen, en die blijven van
  de trainer. De criteria komen ernaast.
- **Feedback mondeling geven.** Verworpen: bij zes presentaties past dat niet in vijftig minuten.

## Gevolgen

- De regel uit deel 9 dat de deelnemers geen eigen vragen maken, geldt alleen nog voor de rolkaarten. De criteria
  zijn van de deelnemers. Twee dingen houden ze eerlijk: ze liggen vast vóór de eerste presentatie, en elke
  deelnemer toetst de eigen presentatie eraan.
- De vragen van het comité duren drie minuten in plaats van vijf.
- De deelnemers krijgen meer werk tussen dag 1 en 2, naast de online voorbereiding van S&N.
- De adviesbureaus achter de kanalen verkopen ook advies. De lespagina vraagt daarom bij elk filmpje: wat is gemeten,
  en wat is een mening?
- Het draaiboek van dag 2 is nog niet geschreven. Het volgt dit programma.

## Raakt

- `DATA.vragen` (V2), `DATA.days`: dag 2 om 9:30, 9:40, 10:45 en 11:30, dag 3 om 9:45.
- FR-09 (gewijzigd), FR-41 (nieuw), AC-05 (gewijzigd), AC-24 (nieuw), twee risico's, een KISS-keuze, de opleverlijst
  van de trainer, fase 2, deel 8 en deel 9.
- `materiaal/presentatie-dag2.html` (nieuw, met de skill `ontwerp-dia` voor deelnemers) en `materiaal/index.html` (de hoofdvraag in het overzicht).
