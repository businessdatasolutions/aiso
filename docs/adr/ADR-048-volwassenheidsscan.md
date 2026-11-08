# ADR-048: Het blok van 10:00 wordt de volwassenheidsscan

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Het blok "Breed gebruikt, zelden volwassen" (dag 1, 10:00) heette tot ADR-044 "Wat AI nu kan en niet kan". ADR-044 gaf het een titel die de kernboodschap noemt, en liet de inhoud gelijk. Daardoor stond er nog van alles in wat bij de oude titel hoorde:

- de werkvorm "Mens tegen agent" (ADR-018);
- de vier faalwijzen van een agent;
- de grillige grens;
- gevoel is geen meting;
- de soorten AI;
- een brug naar 11:00 over taalmodellen die te lang vasthouden aan wat werkt.

Op de werkkaart van ADR-047 werd zichtbaar dat de deelnemer daar niet uit kon halen wat het blok vroeg. De trainer zag het meteen. "Mens tegen agent" en de faalwijzen horen bij de uitleg hoe een agent werkt, en die is al geparkeerd voor dag 2 (ADR-040). De andere punten komen in het blok niet aan bod.

Het blok heeft wel een sterke kern. De cijfers laten zien dat bijna elke organisatie AI gebruikt, maar dat weinig organisaties het opschalen. De maquette van een ziekenhuis laat het in één beeld zien: gemiddeld 18 AI-toepassingen, en één is opgeschaald. Wat ontbrak, is de stap naar de eigen organisatie.

## Besluit

- **Het blok bestaat uit de cijfers, de maquette en de volwassenheidsscan.**
  - 10:00–10:15: de cijfers en de maquette.
  - 10:15–10:30: de scan.
  - 10:30–10:40: het duo vergelijkt de profielen.
  - 10:40: werkregel 1.
- **De volwassenheidsscan** (`materiaal/volwassenheidsscan.html`, FR-40) meet de eigen organisatie op zes dimensies:
  - richting en eigenaarschap;
  - gebruik en schaal;
  - mensen en werk;
  - data en technologie;
  - governance en risico;
  - waarde meten en leren.
- **Hoe de deelnemer scoort.** Elke dimensie heeft vier niveaus die je kunt waarnemen. De deelnemer kiest het hoogste niveau waarvan alles klopt, met een voorbeeld uit de laatste drie maanden. Wie het niet weet, kiest "weet ik niet" en schrijft op wie het wel weet. De uitkomst is een profiel, geen totaalscore.
- **De dimensies komen uit de AI-wiki.** Ze zijn wat de modellen van MIT CISR, Cisco, BCG en McKinsey gemeen hebben. Gebruik en schaal volgt de trechter van de AI Monitor Ziekenhuizen 2026, dezelfde trechter als in de maquette. Het onderzoek staat in `~/Projects/ai-wiki/inspiration/2026-11-08-ai-volwassenheid-meten-scan-research-log.md`.
- **Het profiel komt terug** bij de doelen (dag 1, 11:40), het transformatieplan (dag 3, 9:45) en de roadmap (dag 3, 10:45). Die blokken noemen het in "Je gebruikt" en hebben een tegel naar de scan.
- **Wat uit het blok gaat, is niet weg.**
  - "Mens tegen agent", de faalwijzen, de grillige grens, gevoel is geen meting en de soorten AI staan in het draaiboek onder "Achtergrond en reserve voor de trainer".
  - De meting van Allen en McDonald (2026) staat al op de lespagina Vier vragen. De trainer noemt haar nu om 11:15, en de lastige vragen erover staan bij het blok van 11:00.

## Overwogen alternatieven

- **De oude punten houden, met een betere uitleg op de werkkaart.** Verworpen: ze komen in het blok niet aan bod. Een betere uitleg maakt ze niet passender.
- **Een bestaand volwassenheidsmodel uitleggen,** zoals dat van MIT CISR of BCG, of de dertien raamwerken uit de atlas van de trainer. Verworpen: een model uitleggen kost tijd en dient geen extra resultaat van S&N (KISS, deel 5.1). De scan neemt alleen wat de modellen gemeen hebben.
- **Eerst de eigen AI-toepassingen tellen,** in de zes fasen van de trechter. Verworpen: het telt één dimensie en laat de andere vijf liggen. Gebruik en schaal zit nu als dimensie in de scan.
- **De AI de scan laten invullen.** Verworpen: welke AI een organisatie heeft, is vaak interne informatie (NFR-01). En juist "weet ik niet" is een uitkomst.
- **Een totaalscore.** Verworpen: een gemiddelde verbergt waar het blijft steken, en daar gaat het in de doelen, het plan en de roadmap om.

## Gevolgen

- De scan is zelfrapportage van één persoon. De wiki laat zien dat bijna elk cijfer over volwassenheid dat ook is, en dat zelfrapportage te rooskleurig uitvalt. Daarom vraagt de scan om een voorbeeld bij elk niveau. De lespagina raadt aan een collega uit een ander deel van de organisatie hem ook te laten invullen.
- Veel deelnemers weten het bij een paar dimensies niet. Dat is een uitkomst, en het sluit aan op governance op dag 3: weet je het, of weet je wie het weet?
- Het profiel staat in de browser van de deelnemer. Op dag 3 werkt dat alleen op dezelfde laptop. Daarom is het ook te downloaden als tekstbestand.
- De scan is geen product naast het casusdeck (ADR-034): wat de deelnemer eruit haalt, gaat in de doelen, het transformatieplan en de roadmap.
- Het risico "Een voorbeeld uit een andere sector leidt af" krijgt een betere maatregel: na het ziekenhuis kijkt elke deelnemer meteen naar de eigen organisatie.
- Dag 1 bereidt de referentiewaarde van werkplaats 2 niet meer voor met "Mens tegen agent". FR-20 vraagt daar zelf om: eerst vijf tot tien gevallen zelf beoordelen, en pas daarna de AI.

## Raakt

- FR-26 en FR-40 (nieuw).
- In `DATA.days`:
  - het blok van 10:00 op dag 1;
  - "Je gebruikt", het materiaal, de werkkaart en de instructie van dag 1 om 11:40, en van dag 3 om 9:45 en 10:45.
- Verder in de LRD:
  - de terugvaloptie in deel 6 en een verlichting bij de pijnpunten;
  - de KISS-keuze over één patroon en die over één voorbeeldcasus;
  - de opleveringen van de trainer, fase 0 van de roadmap en een risico.
- `materiaal/volwassenheidsscan.html` (nieuw), `materiaal/draaiboek-bouwstenen.md` en `materiaal/voorbeeldcasus.md`.
- ADR-018: deels vervangen, voor de opening van het blok.
