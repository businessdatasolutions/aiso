# ADR-057: Elke lesdag opent met het overzicht van de vier vragen over de drie dagen

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De vier vragen zijn de ruggengraat van de lesdagen (ADR-033). Elke dag opent en sluit ermee (FR-33). De startpagina
toont per blok welke vragen het dient (ADR-046). Maar nergens ziet de groep het geheel: welke vraag op welke dag de
hoofdvraag is, welke blokken eraan werken, en waar de groep nu staat.

De trainer verkende vijf richtingen voor de werkomgeving in ontwerpschetsen. Een ervan is de vragenkaart als tabel:
vraag × dag, met per cel de blokken, de hoofdvraag van elke dag gemarkeerd, een onderste rij voor de blokken die alle
vier de vragen dienen, en het blok van nu. De trainer wil dat beeld aan het begin van elke lesdag laten zien.

De schets had het programma als vaste kopie in de code. De LRD is de enige bron van het programma: een kopie loopt
bij de eerste wijziging van een tijd of titel uit de pas.

## Besluit

- **Het overzicht is een weergave van de startpagina**, met `?weergave=overzicht`. De pagina leest het programma al
  uit de LRD, kent de klok (ook `?tijd`) en de weergave voor de trainer, en heeft de blokken om naar te springen.
- **Het overzicht komt uit `DATA`.** De rijen zijn `DATA.vragen`, de kolommen `DATA.days`. Een blok staat in de rij
  van elke vraag in zijn `v`. Een blok voor alle vier de vragen staat één keer, in de onderste rij "Alle vier". De
  hoofdvraag van een dag komt uit `vragen[].dag`. Pauzes staan er niet in.
- **Het blok van nu licht op**, met het woord "Nu", op de dag in de kop. Die dag is ook in de tabel gemarkeerd.
- **Een klik op een blok opent dat blok** in het programma van zijn dag, met het materiaal. De klik blijft op de
  pagina, zodat `?tijd` en `?rol` blijven staan. Met een toets erbij opent de browser het blok in een nieuw tabblad.
- **Twee ingangen.** De tegel "Overzicht: vier vragen, drie dagen" is het eerste materiaal van de opening van elke
  dag, zodat de trainer haar om 9:30 in de kop vindt. En de pil "Overzicht" staat voor de dagen in de navigatie.
- **De trainer opent elke dag ermee**, in de eerste stap van het verloop: dag 1 bij het welkom, zonder de vragen uit
  te leggen; dag 2 met vraag 3 als hoofdvraag; dag 3 met vraag 2 en 4.
- **De opening van dag 2 dient alle vier de vragen**, net als de andere openingen. Ze begint met vijf minuten de
  vragenkaart (FR-33), maar haar `v` was alleen V3. In het overzicht stond ze daardoor bij vraag 3 en niet bij "Alle
  vier", en dan klopt "elke dag begint en eindigt bij alle vier" niet. Het investeringscomité blijft het werk voor
  vraag 3: het verloop zegt dat vraag 3 vandaag de hoofdvraag is.
- **Het overzicht past op de beamer** (1920 × 1080) zonder scrollen. Op een telefoon staat elke vraag als kaart, met
  de dagen eronder.
- Een nieuwe eis, NFR-13, en een zin in FR-33. De UX-test krijgt een werkingscontrole W3.

## Overwogen alternatieven

- **De schets overnemen als eigen lespagina, met het programma erin.** Verworpen: dan staat het programma twee keer,
  en de schets liep al achter (de titels en tijden van dag 2 en 3 waren ouder).
- **Een eigen lespagina die de LRD leest.** Verworpen: dan staat de code om `DATA` te lezen op drie plekken (de
  startpagina, de UX-test en de nieuwe pagina), en komt er een bestand bij in de bouw van de site.
- **Het overzicht in de kop van de opening, boven de werkkaart.** Verworpen: dan staan de band met de vragen, de
  tijdlijn en de werkkaart om 9:40 niet meer in beeld op de beamer (KPI T2-B en D2-V).
- **Het overzicht vanzelf tonen vóór 9:30.** Verworpen: de trainer bepaalt wat op de beamer staat. Een weergave die
  vanzelf wisselt, verrast in de zaal.
- **De opening van dag 2 bij vraag 3 laten, en de zin boven de tabel aanpassen.** Verworpen: dan wijkt dag 2 af van het
  ritme dat FR-33 vastlegt, en het overzicht zou dat ritme juist moeten laten zien.
- **De naam "vragenkaart" uit de schets.** Verworpen: de vragenkaart is de geprinte kaart op tafel, dia 1 van het
  casusdeck (FR-33). Twee dingen met één naam verwarren de deelnemer. Het heet daarom "overzicht".

## Gevolgen

- Het overzicht volgt elke wijziging van het programma vanzelf, ook van `v`. Een blok met een verkeerde `v` valt nu op.
- Om 9:30 tot 10:30 op dag 2 lichten op de startpagina alle vier de vragen op, ook tijdens de pitches. Vraag 3 staat
  in die tijd niet meer apart in beeld; de trainer noemt haar bij het overzicht.
- Op dag 1 toont het overzicht om 9:30 ook de titel van 11:00, "Waarom geen plan volstaat". Die stond al op de
  tijdlijn. Het verloop zegt: leg de vragen nog niet uit.
- De eerste stap van de opening wordt iets langer. Op dag 2 en 3 kost het overzicht één minuut van de vijf.
- Op een laptop van 1366 × 768 moet je scrollen. Dat is het eigen scherm van de trainer; op de beamer past het.

## Raakt

- FR-33 (een zin), NFR-13 (nieuw), deel 5 (KISS · Begeleider) en deel 10 (wat de trainer oplevert: de startpagina).
- `DATA.days`: de opening van dag 1, 2 en 3 (`detail`, `materials`, eerste stap van `trainer.verloop`), en van dag 2
  ook `v`.
- `materiaal/index.html` (de weergave), `scripts/meet-ux.py` (W3), `materiaal/draaiboek-bouwstenen.md` (dag 1, 9:30)
  en `CLAUDE.md`.
- ADR-033 en ADR-046: aangevuld, niet vervangen.
