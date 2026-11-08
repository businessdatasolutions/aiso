# Bouwstenen voor het draaiboek

- **Status:** concept (ADR-018), bijgewerkt naar versie 0.22 van de LRD: de vier vragen (ADR-033 tot en met ADR-039). Dag 1 loopt gelijk met het programma in de LRD: dezelfde blokken, tijden, titels en volgorde. Dag 2 en 3 zijn nog niet bijgewerkt; dat volgt in fase 2. Dit zijn bouwstenen voor het draaiboek per lesdag (NFR-07), nog geen draaiboek.
- **Herkomst:** de sessie "AI en kwaliteitsmanagement in de zorg" van 10 november 2026, algemeen gemaakt met de voorbeeldcasus Voorbeeld BV (`materiaal/voorbeeldcasus.md`). Zie `onderzoek/2026-11-07-hergebruik-santeon-presentatie.md`.
- **Bronnen:** `background-docs/2026-11-07-volwassen-ai-blijft-zeldzaam.md` (het volwassenheidsrapport) en `background-docs/2026-11-06-kritiek-op-ai-inzet-query-trace.md` (de kritiektrace, met codes als [B2]). De literatuur staat in de LRD onder Bronnen.
- **Lespagina's van dag 1:** `materiaal/vier-vragen.html`, `materiaal/vraagtoets.html`, `materiaal/boards.html` en `materiaal/casusdeck.html`. De startpagina is `materiaal/index.html?dag=1`.
- **Regel:** kies per blok hooguit één of twee punten om echt te zeggen. De rest is reserve voor vragen.
- **Wijkt dit bestand af van de LRD, dan geldt de LRD.**

## Alle dagen · Werkregel 1 en de pauzes (FR-28)

**Herkomst.** Werkregel 1 komt uit de minor AI in Business van de trainer (ADR-023). Sinds versie 0.22 is het de enige werkregel van de training. Het regelboek met vier werkregels is vervallen (ADR-037). Werkregels voor het eigen team komen op dag 3 terug, in het transformatieplan, met werkregel 1 als voorbeeld (FR-24).

**De werkregel:** "Voordat je pauze neemt, zet je **altijd** AI aan het werk." Hoe je hem invoert, staat bij de opening van dag 1.

### Vóór en na elke pauze

- De startpagina toont werkregel 1 vijf minuten vóór elke pauze, en tijdens de pauze, met een idee voor een AI-taak die het blok erna voorbereidt. De taken staan in de LRD, bij de pauzes in het programma (veld `aiTask`). Zo staan ze op één plek. Hoort er een lespagina bij, zoals de prompt voor het paper in de lunch van dag 2, dan staat die in het veld `materials`, en toont de startpagina de link achter de taak.
- Zeg de werkregel hardop bij de eerste twee pauzes. Daarna doet de startpagina het.
- Na de pauze: "Wat heeft je AI gemaakt?" Eén voorbeeld is genoeg. Een taak die mislukte, is stof voor de eerste vraag van het nabespreken: waar ging het mis?
- Ook in de pauze werkt de AI alleen met openbare of verzonnen gegevens (NFR-01).

## Dag 1 · Vooraf (trainer)

- **Print de vragenkaart.** Dat is dia 1 van `materiaal/casusdeck.html`. Open het bestand, klik op **Download als PDF** en kies in het printvenster alleen pagina 1, liggend. Eén per deelnemer en twee reserve. De lege vakken hebben schrijflijnen.
- **Download de twee filmpjes**, zodat ze ook zonder internet werken. De links staan in de LRD, bij 9:30 en 11:00. De tutorial waar ze uit komen: https://businessdatasolutions.github.io/emergent-strategy-tutorial/ (ten Hove, 2026).
- **Zet de startpagina klaar, in twee vensters** (ADR-047).
  - Op de beamer de weergave voor de deelnemers: https://businessdatasolutions.github.io/aiso/materiaal/?dag=1. Per blok staat daar de werkkaart: wat de deelnemer nodig heeft, waar die op let, wat die moet weten en doet, waaraan die ziet dat het goed gaat, wanneer het klaar is, en waarvoor die jou vraagt.
  - Op je eigen scherm de trainersweergave: https://businessdatasolutions.github.io/aiso/materiaal/?dag=1&rol=trainer. Per blok staan daar wat je klaarzet, het verloop met tijden (de stap van nu licht op) en waar je op let. De gele band bovenaan linkt naar de weergave voor de deelnemers. Zet de trainersweergave nooit op de beamer: ze verraadt de werkvorm.
  - Zonder internet werkt de pagina via een lokale server, zoals `python3 -m http.server`, met `materiaal/index.html?dag=1` (en `&rol=trainer`). Om te oefenen zet `?tijd=HH:MM` de klok op een tijdstip.
- **Geef de deelnemers de lespagina's** vóór 11:00: `vier-vragen.html` met de map `bo-demo/`, `vraagtoets.html` en `boards.html`. Via de site (https://businessdatasolutions.github.io/aiso/), als bestanden of in de leeromgeving. Ze werken zonder server.
- **Gebruik de simulator uit `bo-demo/`.** In de online versie doet de schuif β bijna niets (`materiaal/bo-demo/LEESMIJ.md`). De simulator heeft wel internet nodig. De reserve zijn de drie schermafbeeldingen op de lespagina.
- **Zet het lege casusdeck op de openbare downloadpagina** (FR-02). Doorloop het één keer zelf met je AI: invullen, lokaal openen, PDF maken.
- **Ken de uitkomst van de ijking** van de vraagtoets (FR-37, `materiaal/vraagtoets-ijkset.md`). In welke AI-omgeving haalde de prompt de norm? Dat zeg je om 11:40.
- **Maak de duo's** (FR-08). Waar het kan, zijn dat de buddy's uit de leeromgeving.
- **Lees de ontwikkeldoelen** (FR-11). Noteer welke leerdoelen niet in het programma passen. Die bespreek je op dag 1 apart met de deelnemer, in een pauze.
- **Zet je eigen boards klaar** (stap 2 en 3 van `boards.html`). Je laat ze om 12:15 en 13:30 zien.

## Dag 1 · 9:30–10:00 · Opening: je casus en de vier vragen (FR-01, FR-11, FR-28, FR-30, FR-32, FR-33)

**Materiaal:** de geprinte vragenkaart en pennen, filmpje 1 (10 seconden), de startpagina. Die toont de vier vragen voluit, wijst de vragenkaart aan en zet de werkkaart van het blok in beeld. Het verloop met tijden staat in de trainersweergave (`&rol=trainer`).
**Uitkomst:** een casus met een voorlopige strategische AI-vraag, de duo's en de nulmeting op de vragenkaart. En de opdracht om de stukken van het bestuur te zoeken.

**De volgorde ligt vast.** Eerst de casus, dan de nulmeting, en pas daarna uitleg. Wie eerst uitleg krijgt, schrijft die uitleg op. Dan meet de nulmeting niets meer.

### 9:30–9:35 · Welkom en duo's (5 minuten)

1. Zeg in twee zinnen wat de training oplevert: "Je werkt drie dagen aan één casus uit je eigen organisatie. Vandaag gaat het om richting: waar gaat je organisatie heen nu AI de omgeving verandert?"
2. Kennismaking: iedereen noemt naam, rol en organisatie, in één zin.
3. Noem de duo's. Die blijven drie dagen hetzelfde (FR-08).
4. Deel de geprinte vragenkaart uit. Zeg: "Deze kaart blijft drie dagen op tafel liggen. Gooi hem niet weg."

### 9:35–9:40 · De casus vastleggen (5 minuten)

1. Zeg: "Vul bovenaan de kaart twee vakken in. Bij Casus je organisatie, of het deel waar je werkt. Bij Strategische AI-vraag de vraag over AI waar je organisatie mee worstelt, in één zin."
2. Zeg erbij: "Het is een voorlopige vraag. Om 11:40 toetsen we hem. Daarna ligt hij vast."
3. Zeg: "Schrijf alleen op wat openbaar mag. Wat op deze kaart staat, gaat vanmiddag je AI in" (NFR-01).
4. De deelnemers schrijven. Loop rond. Help alleen wie niets opschrijft: "Waar maakt je directie zich zorgen over, als het om AI gaat?"

### 9:40–9:50 · De vier vragen en de nulmeting (10 minuten)

1. Lees de vier vragen voor, van de kaart. Leg ze niet uit.
   - **V1 Richting:** Hoe bepaal ik een strategie als elk plan door de realiteit wordt ingehaald voordat het op papier staat?
   - **V2 Transformeren:** Hoe transformeer ik de organisatie onder snel veranderende omstandigheden en houd ik de huidige business robuust?
   - **V3 Investeren:** Hoe zorg ik dat mijn investeringen veilig zijn terwijl de toekomst onzeker is?
   - **V4 Roadmap:** Hoe bouw ik een roadmap met mijlpalen als na stap 1 onduidelijk is of stap 2 de beste volgende is?
2. Zeg: "Schrijf bij elke vraag in het vak Nulmeting wat je nu zou doen, in je eigen organisatie. Hooguit drie zinnen per vraag. Er is geen goed of fout antwoord, en niemand beoordeelt het. Vanmiddag lees je het terug."
3. De deelnemers schrijven acht minuten, alleen. Het duo praat nog niet.
4. Zeg: "Laat de vakken Mijn antwoord nu en Na dag 1 leeg. Die vul je om 16:00."

**Zeg niets over het onderwerp.** Geef geen voorbeeld, geen hint, en geen woord als "wendbaar" of "experimenteren". De nulmeting laat zien hoe de deelnemer nu denkt. Bij Voorbeeld BV lijkt een nulmeting op klassiek plannen: een vast doel, een plan, en daarna uitvoeren (`materiaal/voorbeeldcasus.md`). Dat voorbeeld zien de deelnemers pas om 11:32.

### 9:50–9:55 · Visie, missie en strategie (5 minuten, FR-30, ADR-030)

1. Toon het eerste filmpje (10 seconden): vandaag → een boog → de visie over vijf jaar, met de missie als stip.
2. Geef de drie definities:
   - **Visie:** hoe de wereld eruitziet in de toekomst. Een beeld van de veranderende omgeving waarin je organisatie zal opereren.
   - **Missie:** welke plek je ziet voor de organisatie in die toekomstige wereld. De rol en positie die je wilt innemen.
   - **Strategie:** welk pad je gaat volgen richting die nieuwe positie. De keuzes en stappen om van nu naar je gewenste plek te komen.

**Zeg niets over wat er komt.** Noem het niet "klassiek" of "de oude theorie", en wijs niet vooruit naar 11:00. De deelnemers passen het model eerst toe op hun eigen organisatie. De omslag werkt pas als ze er zelf in zijn gestapt. Daarom heeft het materiaal op de startpagina neutrale namen.

### 9:55–10:00 · Werkregel 1 en de opdracht voor de pauze (5 minuten)

1. Toon werkregel 1 op een dia of de startpagina. Lees voor: "Voordat je pauze neemt, zet je **altijd** AI aan het werk."
2. Zeg waarom: een onderzoek met de onderzoeksfunctie van je AI duurt tien tot twintig minuten. Dat is precies een pauze. Wie de AI vóór de pauze een taak geeft, heeft na de pauze iets om mee verder te werken. De regel geldt vóór elke pauze, negen keer in drie dagen.
3. Geef de opdracht: "Zoek op wat het bestuur van jouw organisatie zegt over visie, missie en strategie." De AI zoekt de stukken in de pauze van 10:45. Het gaat alleen om openbare stukken: een jaarverslag, artikelen, interviews (FR-32, NFR-01).
4. Zeg: "Om 10:40 staat de taak op het scherm. Ik doe het dan voor."

**Leerdoelen (FR-11).** Een leerdoel dat niet in het programma past, bespreek je apart met de deelnemer, in de pauze van 10:45 of in de lunch. Niet in de groep.

### Lastige vragen

**"Wat bedoel je met strategie?"**
"Schrijf op wat jij eronder verstaat. Dat is precies wat de nulmeting meet. Over vijf minuten krijg je de definities."

**"Ik weet het antwoord nog niet."**
"Schrijf op wat je morgen zou doen als je directeur het je vroeg. Een half antwoord is ook een nulmeting."

**"Mijn casus is één afdeling. Mag dat?"**
Ja. Een casus mag een deel van een organisatie zijn (FR-01). De vraagtoets om 11:40 kijkt of de vraag strategisch is op het niveau van die afdeling.

**"Waarom op papier?"**
De kaart blijft drie dagen liggen, en je ziet je eerste antwoord terug zoals je het schreef. Om 15:15 neem je het letterlijk over in je casusdeck.

**"Mag ik de naam van mijn organisatie opschrijven?"**
Ja, op je eigen kaart. Zet er niets vertrouwelijks op: de tekst gaat vanmiddag je AI in (NFR-01).

## Dag 1 · 10:00–10:45 · Breed gebruikt, zelden volwassen (FR-26, FR-40, ADR-048)

**Materiaal:** het voorbeeld uit de zorg, de maquette van een ziekenhuis (`materiaal/ziekenhuis.html`); de lespagina Volwassenheidsscan (`materiaal/volwassenheidsscan.html`); de startpagina voor werkregel 1 om 10:40.
**Uitkomst:** het profiel van de eigen organisatie uit de volwassenheidsscan.

### 10:00–10:15 · Breed gebruikt, zelden volwassen (15 minuten)

- **Gebruik is breed, volwassen inzet is zeldzaam.** In enquêtes onder bestuurders gebruikt 78–88% AI. Volgens het CBS gebruikt 33% van de Nederlandse bedrijven met tien of meer werkzame personen AI (2025, voorlopig). Metingen met een strenge lat komen uit op 5 tot 13%: BCG 7,5% (2026), McKinsey 6% (2025 en 2026), Gartner 13% (2026). Noem bij elk cijfer wat er gemeten is en in welk jaar. Het getal beweegt mee met de lat. (Volwassenheidsrapport.)
- **Een voorbeeld: de maquette van een ziekenhuis** (`materiaal/ziekenhuis.html`, twaalf stappen). Zeg erbij dat het voorbeeld uit de zorg komt. De cijfers komen uit de AI Monitor Ziekenhuizen 2026 van M&I/Partners, met 52 ziekenhuizen. Laat in elk geval stap 3 zien: een ziekenhuis heeft gemiddeld 18 AI-toepassingen, en één daarvan is opgeschaald. Dat is breed gebruik en zeldzame volwassen inzet in één beeld. Stap 9 en 10 tonen een patroon: 's avonds maakt AI een eerste selectie, de volgende dag beslist de radioloog. Weinig tijd? Toon stap 1, 3, 9 en 10. Een klik op een ruimte springt naar de stap van die ruimte. Zoek elk cijfer dat je noemt eerst op in het origineel: `~/Projects/presentatie-santeon-10-11-2026/background-material/2026-03-ai-monitor-ziekenhuizen-2026-mxi.pdf`. Bij elke stap staat het paginanummer. Om 10:05 is er tijd voor stap 1, 3, 6, 9 en 10. Stap 6 laat zien dat begonnen nog niet gebruikt is: dat komt terug in de scan, bij gebruik en schaal.

### 10:15–10:30 · De volwassenheidsscan (15 minuten)

1. Zeg: "Bijna elke organisatie gebruikt AI, weinig organisaties schalen het op. Waar staat jouw organisatie? Open de lespagina Volwassenheidsscan."
2. Lees de regels van stap 1 voor. Kies per dimensie het hoogste niveau waarvan alles klopt. Schrijf er een voorbeeld uit de laatste drie maanden bij. Weet je het niet, schrijf dan op wie het wel weet.
3. Zeg: "Niveau 1 of 2 is normaal. Er is geen totaalscore."
4. De deelnemers vullen de scan alleen in, zonder AI, in ongeveer tien minuten. Loop rond. Vraag bij een niveau: "Waaraan zie je dat?" Is het antwoord een gevoel, dan is het niveau waarschijnlijk lager.

### 10:30–10:40 · Profielen vergelijken (10 minuten)

1. Het duo legt de twee profielen naast elkaar: welke dimensie is het laagst, en wat weten jullie niet?
2. Twee deelnemers noemen hun laagste dimensie, met het voorbeeld erbij. Geef geen oordeel over een profiel.
3. Zeg: "Je profiel komt terug. Om 11:40 bij je doelen, en op dag 3 bij je transformatieplan en je roadmap. Het staat in je browser. Download het ook, voor de zekerheid."

### 10:40–10:45 · Werkregel 1: de AI aan het werk (5 minuten)

1. De startpagina toont werkregel 1 met de AI-taak voor de pauze. Lees de taak voor.
2. Doe het voor met je eigen AI: zet de onderzoeksfunctie aan, plak de taak, vul de organisatie in en start.
3. De deelnemers doen hetzelfde. Kijk of bij iedereen de AI loopt voordat de pauze begint.
4. Werkt iemand met Voorbeeld BV, of vindt de AI niets openbaars? Dan zoekt de AI het jaarverslag van een organisatie uit dezelfde sector (FR-32).

### Nederlandse uitleg bij Engelse termen (NFR-08)

| Term | Uitleg |
|---|---|
| Frontiermodel | Een van de sterkste taalmodellen van dit moment, zoals de betaalde versies van Claude, ChatGPT of Gemini. |

### Lastige vragen

**"Wat telt als volwassen inzet?"**
Dat verschilt per bron, en daarom verschilt het getal. Noem bij elk cijfer wat er gemeten is en in welk jaar.

**"Ik weet het bij de meeste dimensies niet."**
Dan is dat je uitkomst. Kies "Weet ik niet" en schrijf op wie het wel weet. Wie AI wil opschalen, moet eerst weten wat er al draait. Op dag 3 komt die vraag terug bij governance: weet je het, of weet je wie het weet?

**"Mijn organisatie verschilt per afdeling."**
Vul de scan in voor je casus: het deel van de organisatie waar je strategische vraag over gaat. Verschilt het daarbinnen nog, kies dan het niveau dat voor het grootste deel geldt, en schrijf het verschil erbij.

**"Welk model is dit?"**
Geen bestaand model. De zes dimensies komen terug in de modellen van MIT CISR, Cisco, BCG en McKinsey; gebruik en schaal volgt de trechter van de AI Monitor Ziekenhuizen. De bronnen staan onderaan de lespagina, en het onderzoekslog staat in de AI-wiki (`inspiration/2026-11-08-ai-volwassenheid-meten-scan-research-log.md`). Bijna elk cijfer in die onderzoeken komt van één bestuurder die over de eigen organisatie oordeelt. Daarom vraagt de scan om een voorbeeld bij elk niveau.

## Dag 1 · 10:45–11:00 · Pauze

- **AI-taak:** de onderzoeksfunctie zoekt openbare stukken waarin het bestuur iets zegt over visie, missie en strategie, en over AI. Per stuk de link en een korte samenvatting. De volledige tekst staat op de startpagina en in de LRD.
- Gebruik de pauze voor een gesprek over een leerdoel dat niet past (FR-11), als dat nodig is.

## Dag 1 · 11:00–11:40 · Waarom geen plan volstaat (FR-34, FR-30, ADR-030)

**Materiaal:** filmpje 2 (25 seconden); `materiaal/vier-vragen.html`, stap 1 tot en met 6; de simulator `materiaal/bo-demo/bo-simulator-fast.html`, met de schermafbeeldingen als reserve.
**Uitkomst:** per vraag één zin over verkennen en benutten.
**Bouwt op:** de nulmeting (9:30).

### 11:00–11:03 · Na de pauze (3 minuten)

1. "Wat heeft je AI gevonden?" Eén voorbeeld is genoeg.
2. Zeg: "Vanochtend zagen jullie het model: één beeld van de toekomst, één stip, één route. Wie vond in de stukken van het eigen bestuur zo'n stip?" Laat er twee voorlezen.

### 11:03–11:08 · De omslag (5 minuten)

1. **Waarom dat bij AI vastloopt.** Een straalmotor is gecompliceerd: duizenden onderdelen, maar voorspelbaar. De oceaan is complex: een kleine verandering heeft onvoorspelbare gevolgen. AI hoort bij de oceaan. Wie één stip kiest en ernaartoe blijft lopen, loopt een groot risico dat het de verkeerde stip is.
2. **Het organische pad.** Toon het tweede filmpje (25 seconden): korte stappen naar de "ware toekomst". De missie verschijnt pas onderweg. Mintzberg noemt dit emergente strategie: strategie die ontstaat uit wat je doet (Mintzberg & Waters, 1985).
3. **De lus.** Keuzes → dynamiek → opties → inzichten. Zeg: "Elke afsluiting is één ronde van de lus. Vanmiddag om 16:00 doe je de eerste. Een eigen missie schrijven we vandaag niet; die zie je op dag 3. De missie van je bestuur is het startpunt."
4. **Aanhaken.** In de Eerste blik online lazen ze het advies van Reid Hoffman: herzie de AI-strategie elke week. Vraag wat ze daar toen van vonden.

### 11:08–11:15 · Weerbarstige vraagstukken (7 minuten, stap 1 en 2 van de lespagina)

1. Toon stap 1: de vier vragen. Zeg: "Dit zijn de vragen van vanochtend. Elke vraag hoort bij een taak van leiderschap."
2. Toon stap 2. Zeg: "Rittel en Webber (1973) noemen zulke vragen wicked problems: weerbarstige vraagstukken. Ze geven tien kenmerken. Vijf daarvan zie je terug in onze vier vragen."
3. Noem er minstens vier, elk met het voorbeeld van Voorbeeld BV op de pagina:
   - **Geen vaste formulering** (V1). Hoe je het probleem opschrijft, bepaalt al welke oplossing je ziet. Klachten sneller afhandelen of het aanspreekpunt van de klant blijven: elke formulering geeft een andere strategie.
   - **Elke poging telt** (V2). Je kunt niet oefenen op de echte organisatie. Ook als je stopt, is de situatie anders dan ervoor.
   - **Beter of slechter, niet goed of fout** (V3). Een investering is nooit gewoon veilig. Hooguit is de ene inzet veiliger dan de andere.
   - **Elk probleem is uniek** (V3). Wat elders werkte, is een idee. Het rendement dat een leverancier noemt, komt uit een andere organisatie.
   - **Geen stopregel** (V4). Je weet nooit wanneer je klaar bent. De roadmap is nooit af.
4. Zeg het gevolg: "Je lost ze niet één keer op. Je blijft eraan werken. Daarom komen de vier vragen elke dag terug, en leg je elk antwoord naast het vorige."

### 11:15–11:20 · Verkennen en benutten (5 minuten, stap 3 en het begin van stap 4)

1. **Twee manieren van werken** (March, 1991). Benutten is beter worden in wat je al doet: het rendement is zeker en komt snel. Verkennen is zoeken naar wat nieuw is: het rendement is onzeker en komt later. Organisaties schuiven vanzelf naar benutten, want dat betaalt sneller uit. Verandert de wereld, dan word je steeds beter in iets wat minder waard wordt.
2. Noem de meting uit stap 4 van de lespagina: "In een strategiesimulatie hielden taalmodellen vast aan de oude technologie. Ze benutten te veel" (Allen & McDonald, 2026).
3. **De portfoliokaart** (Osterwalder e.a., 2020). Toon de twee portfolio's van Voorbeeld BV naast elkaar: links wat het bedrijf verkent, rechts wat het benut. Wijs "AI sorteert mee in één team" aan, met de pijl: haalt het de norm, dan schuift het naar benutten.
4. **De meerarmige bandiet.** "Voor je staan tien gokautomaten. Elke automaat betaalt anders uit, maar hoeveel weet je niet. Trek je aan de arm die tot nu toe het meest gaf? Dat is benutten. Probeer je een andere? Dat is verkennen. Wie alleen benut, mist misschien de beste automaat."

### 11:20–11:30 · De simulator (10 minuten)

**Voordoen (3 minuten).**

1. Open de simulator uit `bo-demo/` op het scherm. Zeg wat hij zoekt: de beste plek voor een distributiecentrum, met de laagste transportkosten naar dertig klanten. "Elke test is een dure haalbaarheidsstudie. Je wilt er zo weinig mogelijk doen." Zeg erbij dat de knoppen Engels zijn.
2. Klik op **Initialize / Reset**. **Toggle Belief** staat al aan (een knop die aan staat, is zwart): "Dit denkt het model. Bleek is onzeker, grijs is zekerder." Zet **Toggle Decision** aan: "Dit is de regel. De volgende test komt waar het rode vlak het laagst is."
3. Klik twee keer op **Run One Step**. Wijs de rode bol aan: dat is de volgende test. De gele bol is de beste plek tot nu toe.
4. Zeg: "De schuif β (bèta) bepaalt hoeveel de regel verkent." Laat niet zien wat een hoge β doet. Dat ontdekken ze zelf.

**Zelf doen (5 minuten).** De deelnemers volgen stap 4 van de lespagina, alleen of met het duo:

1. Zet β op 0,5 en klik op Initialize / Reset.
2. Voorspel: komt de volgende test dicht bij de beste plek, of ver weg, waar het model het minst weet?
3. Klik vijf keer op Run One Step. Waar liggen de zwarte bollen?
4. Zet β op 10, klik op Initialize / Reset en weer vijf keer op Run One Step.

**Nabespreken (2 minuten).** Vraag: "Wat verschilde er?" Bij een lage β bleven de tests bij de beste plek. Bij een hoge β lagen ze verspreid over het veld. Zeg de kern: "Wat je over het onbekende aanneemt, bepaalt hoeveel je verkent." Vraag dan: "Bij welke van je vier vragen zit jij nu op een lage β?"

- **Blijft "Loading 3D Scene..." staan?** Dan is er geen internet. Toon de drie schermafbeeldingen onderaan stap 4.
- **Elk beeld is anders.** Bij elke keer laden staan de klanten op een andere plek. Het verschil tussen een lage en een hoge β is toch steeds te zien.

### 11:30–11:32 · De deur die terug kan (2 minuten, kort uit stap 5)

Zeg: "Bezos (2016) deelt besluiten in twee soorten in. De meeste besluiten zijn een deur die terug kan. In het Engels heet dat een two-way door. Bevalt het niet, dan loop je terug: besluit snel en klein. Een paar besluiten zijn een deur die niet terug kan, een one-way door. Besluit dan langzaam en met bewijs." De rest van stap 5 is voor dag 2.

### 11:32–11:40 · Eén zin per vraag (8 minuten, stap 6)

1. Toon stap 6 met het voorbeeld van Voorbeeld BV: per vraag wat verkennen is en wat benutten. Lees er één voor, bijvoorbeeld V2: "Benutten: Klantcontact, Planning en Service werken door en verbeteren wat werkt. Verkennen: één team werkt zes weken met een AI die meesorteert."
2. Zeg: "Schrijf per vraag één zin: wat is in jouw casus verkennen, en wat benutten? Bij V3 vraag je je ook af: kan deze deur terug?"
3. Zeg: "Schrijf de vier zinnen op de achterkant van je vragenkaart. De kaart zelf herschrijf je om 16:00."
4. In de laatste twee minuten lezen twee deelnemers één zin voor. Kies er één bij V3.

**Bron:** Allen, R. T., & McDonald, R. M. (2026). How well can AI do strategy? Empirical benchmarking using strategy simulations. *Strategy Science, 11*(1), 93–117. https://doi.org/10.1287/stsc.2025.0444

### Lastige vragen

**"Dus plannen heeft geen zin?"**
Plannen heeft zin. Een plan vasthouden terwijl de wereld verandert, heeft dat niet. Je plant de volgende stap, en bij elk doel zet je een signaal om het los te laten. Dat doe je om 11:50.

**"Ons bestuur wil een plan voor vijf jaar."**
Dat mag. Geef het een koers met beslispunten: wat doen we eerst, wat meten we, en wanneer kiezen we opnieuw? Op dag 3 bouw je die roadmap.

**"Is een weerbarstig vraagstuk gewoon een moeilijk probleem?"**
Een moeilijk probleem heeft een oplossing die je kunt controleren, zoals een rekensom. Bij een weerbarstig vraagstuk kan dat niet. Elke poging verandert het probleem, en een antwoord is alleen beter of slechter dan het vorige.

**"Is dit gewoon agile?"**
Het lijkt erop: korte stappen, meten, bijsturen. Agile gaat over hoe een team bouwt. De vier vragen gaan over waar de organisatie heen gaat en waarin ze investeert.

**"Wat is een goede β in het echt?"**
Daar is geen vaste waarde voor. Hoe sneller je omgeving verandert en hoe minder je weet, hoe meer je verkent. De vraag "bij welke vraag zit ik op een lage β?" helpt meer dan een getal.

**"Verkennen kost geld. Dat geeft ons bestuur niet."**
Verkennen kan klein: zes weken in één team, met een norm vooraf, zoals bij Voorbeeld BV. Dag 2 gaat hierover: een kleine inzet koopt het recht om door te gaan, zonder de plicht.

**"AI wordt toch elke maand beter?"**
De grens schuift, dat klopt. Daarom vertrouw je niet op wat vorig jaar gold, en meet je in je eigen experiment (dag 2). De meting van Allen en McDonald laat ook zien dat nieuwer niet altijd beter is. De modellen van eind 2025 scoorden in de simulatie lager dan eerdere modellen.


**"Lag dat niet aan de prompt?"**
Dat kan meespelen. De onderzoekers zagen een vast patroon, over meerdere modellen. En in je eigen werk geef je je AI ook geen perfecte prompt. Vraag de AI daarom expliciet om andere opties, en verken zelf.


**"Welke modellen waren het precies?"**
Dat staat in het artikel (bron hierboven). Noem geen modelnamen uit je hoofd.


**"Waarom scoren nieuwere modellen slechter?"**
Het artikel meet dat het zo is. Waarom, weten we nog niet zeker. Voor jou telt de les: een AI die strategisch adviseert, houdt vast aan wat al werkt. Verken dus zelf.

## Dag 1 · 11:40–12:15 · Vraag 1: van visie naar doelen (FR-36, FR-01, FR-30, FR-08, FR-10, ADR-039, ADR-052)

**Materiaal:** `materiaal/vraagtoets.html` op het scherm en bij elke deelnemer; de stukken van het bestuur uit de pauze van 10:45; de vragenkaart.
**Uitkomst:** een getoetste strategische vraag, en een concept van 2–4 strategische doelen, elk met een signaal om het los te laten.
**Bouwt op:** de voorlopige vraag (9:30), de stukken van het bestuur (10:45) en de zin bij V1 (11:32).

### 11:40–11:50 · De vraagtoets (10 minuten)

**Eerst (30 seconden).** Zeg de uitkomst van de ijking (FR-37): in welke AI-omgevingen haalde de prompt de norm? Haalde een omgeving de norm niet, dan toetst wie daarin werkt alleen met het duo.

1. **De definitie (2 minuten, stap 1).** Lees voor: "Een AI-vraag is strategisch als het antwoord bepaalt welke plek de organisatie inneemt nu AI haar omgeving verandert, en welk aantrekkelijk alternatief ze daarvoor bewust afwijst." Noem de drie criteria. Elk krijgt een score van 0, 1 of 2.
   - **Omgeving** (hoort bij de visie): welke verandering maakt de vraag nu dringend?
   - **Positie** (hoort bij de missie): gaat het antwoord over wat de organisatie aanbiedt, aan wie, of waarmee ze zich onderscheidt?
   - **Keuze** (hoort bij de strategie): wijst elk antwoord een aantrekkelijk alternatief bewust af? Een optie afwijzen die toch niemand wilde, telt niet.

   Zitten er deelnemers uit de publieke sector in de groep, noem dan ook de lezing die onder niveau 2 staat. Positie: welke rol de organisatie inneemt tegenover inwoners, ketenpartners en andere overheden. Keuze: het afgewezen alternatief gaat vaak over wie een taak, kanaal of rol uitvoert, de organisatie zelf of een ander. Een gemeente heeft geen concurrent; haar plek is de rol tegenover inwoners.

   Zeg: "Dit is mijn voorstel. Jullie mogen het scherper maken. Wat we afspreken, geldt drie dagen." Verandert de groep iets? Vul het dan in op het scherm. Iedereen neemt het over op de eigen pagina.
2. **Oefenen op Voorbeeld BV (3 minuten, stap 2).** Iedereen scoort vraag A, B en C eerst alleen. Vergelijk dan met handen: "Wie gaf B op Positie een 1?" Waar de groep verschilt, is de definitie nog niet scherp genoeg.
   - **A:** "Hoe handelen we klachten sneller en beter af, en leren we ervan?" Scores 0-0-0: operationeel. Dit is een goede eerste prioriteit.
   - **B:** "Hoe handelen we klachten sneller af dan de concurrent?" Scores 1-0-0. Het twijfelgeval. Deelnemers geven op Positie vaak een 1, omdat de concurrent erin staat. Jij geeft een 0: wat Voorbeeld BV aanbiedt en aan wie, blijft gelijk, en snelheid kan een concurrent nadoen (Porter, 1996).
   - **C:** de strategische vraag van Voorbeeld BV, over het aanspreekpunt of de vaste installateur. Scores 2-2-2. Zonder de tweede zin scoort Keuze een 1: er is een ambitie, maar niets valt af.
   - **D:** alleen voor wie bij een publieke organisatie werkt; bespreek hem niet plenair. De verzonnen gemeente Voorbeeldstad: blijft ze het eerste loket voor inwoners, of laat ze eenvoudige vragen over aan een landelijke voorziening? Scores 2-2-2. Vraagt iemand ernaar, zeg dan: de plek is hier de rol tegenover inwoners, en het afgewezen alternatief gaat over wie het loket voor eenvoudige vragen uitvoert.
3. **Je eigen vraag (3 minuten, stap 3).** Elke deelnemer scoort de eigen vraag, alleen.
4. **Het duo (2 minuten).** Het duo scoort de vraag zonder de scores van de ander te zien. Verschillen ze, dan praten ze erover. De deelnemer beslist.

**De uitkomst.** Lees hem voor van de pagina:

- **Positie 0: operationeel.** Bewaar de vraag als kandidaat voor je eerste prioriteit (dag 2). Zoek de vraag erboven: waarom moet dit beter, en wat wil je organisatie daarmee bereiken?
- **Positie 1 of 2, Keuze 0: nog geen keuze.** Herschrijf de vraag zo dat er iets afvalt.
- **Positie 1 of 2, Keuze 1 of 2: strategisch.** Positie 1 is strategisch op het niveau van een afdeling of keten.
- **Altijd:** onder de vraag moet een eerste prioriteit passen die je tussen dag 2 en 3 kunt testen. Past die er niet onder, kies dan een deel, zoals één markt of één klantgroep.

**Vastleggen.** De deelnemer schrijft de gekozen vraag op de vragenkaart. Daarbij komen de eigen scores en die van het duo, bijvoorbeeld "O2 P1 K2 · duo O2 P1 K1" (AC-23). De vraag gaat ook in stap 1 van `boards.html`. Daarna ligt hij vast (FR-01).

**Stap 4, de AI, komt in de lunch.** Zeg: "De AI scoort je vraag in de lunch, als tweede beoordelaar, via je supervisory board. Nu leunt dus niemand op het oordeel van de AI."

**Loopt het uit?** Bespreek bij het oefenen alleen vraag B.

### 11:50–12:15 · Van visie naar doelen (25 minuten, FR-30)

1. **Voordoen (3 minuten).** Toon de drie doelen van Voorbeeld BV (`materiaal/voorbeeldcasus.md`):
   1. Klanten kiezen Voorbeeld BV als vast aanspreekpunt voor hun installatie, met een onderhoudsabonnement.
   2. Storingen voorkomen in plaats van verhelpen.
   3. Van elke klacht leren, over de afdelingen heen.

   Geef het loslaatsignaal van doel 1: "Gaan de meeste storingen in 2027 rechtstreeks naar de fabrikant, dan kiezen we opnieuw tussen aanspreekpunt en vaste installateur." Vraag de groep: "Wat zou het signaal bij doel 2 zijn?"
2. **Zelf doen (12 minuten).** Elke deelnemer neemt de eigen AI-visie uit de online voorbereiding erbij, en de stukken van het bestuur uit de pauze (FR-10). Wie de voorbereiding niet deed, werkt met Voorbeeld BV. Zeg: "Koppel je visie aan 2–4 doelen van je organisatie. Schrijf bij elk doel: wat zou er moeten gebeuren om dit doel los te laten?" Dat signaal komt bij het doel in het deck (AC-20). Vond de AI geen stukken, neem dan het jaarverslag van een organisatie uit dezelfde sector (FR-32).
3. **Duo (7 minuten).** De duo's geven elkaar feedback in de vorm "Toen je … / Ik zou …" (FR-08). Daarna de vraag over risicobereidheid: "Hoeveel risico wil jullie directie nemen met AI, en wie heeft dat ooit hardop gezegd?" Besturen bespreken hun risicobereidheid zelden. Die verschilt per persoon, en dat blijft onuitgesproken (Linda Hill, in Bloomberg Podcasts, 2026). Het antwoord hoort in de visie, bij de rol van de mens (SN2).
4. **Afronden (3 minuten).** Zeg: "Een eigen missie schrijft vandaag niemand. Die wordt pas na drie dagen zichtbaar. Je doelen gaan in werkplaats 1 naar je boards, en om 15:15 in je deck."

**Een goed loslaatsignaal** is te zien of te meten, en noemt een grens of een datum. "Als het niet werkt" is te vaag. "Als de meeste storingen in 2027 rechtstreeks naar de fabrikant gaan" is een signaal.

### Lastige vragen

**"Mijn vraag is operationeel. Is dat erg?"**
Nee. Dan heb je je eerste prioriteit al. Zoek de vraag erboven: waarom moet dit beter, en wat wil je organisatie daarmee bereiken? Bij Voorbeeld BV werd vraag A de eerste prioriteit onder vraag C.

**"Ik werk op een afdeling. Over de positie van de organisatie beslis ik niet."**
Dan scoort je vraag op Positie een 1: strategisch op het niveau van je afdeling of keten. Dat telt. Kijk wel of er iets afvalt.

**"Waarom geen totaalscore?"**
Een totaal verbergt waar de vraag zwak is. Kijk naar het laagste criterium: daar wint je vraag het meest bij herschrijven.

**"Kan de AI dit niet sneller?"**
Sneller wel. Wie eerst het oordeel van de AI ziet, neemt het makkelijk over. Daarom scoor jij eerst, dan je duo, en in de lunch de AI. Waar jullie verschillen, beslis jij.

**"Ons bestuur heeft al doelen."**
Neem ze over. Nieuw is het loslaatsignaal bij elk doel.

**"Als het signaal komt, hebben we gefaald."**
Dan kies je opnieuw. Dat is de lus van 11:00: kiezen, kijken wat er gebeurt, nieuwe opties zien, leren. Een doel dat je op tijd loslaat, kost minder dan een doel dat je te lang vasthoudt.

## Dag 1 · 12:15–12:30 · Je supervisory board (FR-17, FR-32, ADR-028, ADR-030)

**Materiaal:** `materiaal/boards.html`, stap 1, 2, 4 en 5.
**Uitkomst:** de supervisory board als skill in de eigen AI-omgeving.

**Voordoen (3 minuten).** Open `materiaal/boards.html` op het scherm, bij stap 2.

1. Laat je eigen supervisory board zien, bijvoorbeeld v_Churchill, v_Gandhi, v_Patton, v_Springsteen en v_Obama. Zeg waarom je juist hen koos: ze inspireren je, en ze denken strategisch.
2. Wijs de tegenspreker aan: "Kies er minstens één die tegen je koers in zou gaan. Een board van alleen helden geeft je snel gelijk."
3. Zeg: "Deze helden helpen je om je koers scherp te krijgen, en je verhaal voor je bestuur en je collega's."

**Daarna (12 minuten).** Elke deelnemer kiest drie tot vijf strategen, downloadt `supervisory-board.zip` en zet hem in de eigen AI-omgeving (stap 4 en 5 van de pagina). De stukken van het bestuur liggen er al: de AI zocht ze in de pauze van 10:45.

- **Alleen openbare stukken** (NFR-01). Een intern strategiestuk gaat geen AI-tool in.
- Vond de AI niets, of werkt iemand met Voorbeeld BV? Dan neemt die het jaarverslag van een organisatie uit dezelfde sector.
- Lukt het installeren niet vóór 12:30? Laat het stuk dan door de AI samenvatten met de vraag uit de AI-taak, en installeer de board in werkplaats 1. De vraagtoets doet die deelnemer dan met de prompt uit stap 4 van `vraagtoets.html`.

**Om 12:25: werkregel 1.** De AI-taak voor de lunch staat op de startpagina en onder stap 2 van `boards.html`. De board bespreekt de stukken van het bestuur en komt tot een gezamenlijke conclusie en advies. Daarna scoort de board de strategische vraag met de vraagtoets. Zeg: "Geef je eigen scores niet mee. Dan leunt de board er niet op."

### Lastige vragen

**"Mag ik iemand kiezen die nog leeft?"**
Ja, als het een publiek persoon is. Het lid heet v_Naam: een denkperspectief, geïnspireerd op die persoon. Wat het in je AI zegt, is nooit een citaat (ADR-029).

**"Mijn AI-omgeving kent geen skills."**
Gebruik de terugvaloptie uit stap 5: een project met de tekst als instructie. Het werkt hetzelfde.

**"Waarom een tegenspreker? Ik wil juist inspiratie."**
Een board die je alleen gelijk geeft, leert je niets. Eén lid dat tegen je koers in gaat, laat zien waar je verhaal zwak is.

## Dag 1 · 12:30–13:30 · Lunch

- **AI-taak:** leg de stukken van het bestuur voor aan je supervisory board. De board bespreekt wat ze zeggen over visie, missie en strategie, en komt tot een gezamenlijke conclusie en advies. Daarna scoort de board je strategische vraag met de vraagtoets. Waar de board anders scoort dan jij en je duo, beslis jij. De volledige tekst staat op de startpagina en in de LRD.
- Gebruik de lunch voor een gesprek over een leerdoel dat niet past (FR-11), als dat nog open staat.

## Dag 1 · 13:30–15:00 · AI-werkplaats 1: bouw je boards (FR-04, FR-05, FR-06, FR-07, FR-17, FR-32, ADR-027, ADR-028)

**Ritme:** voordoen (15 minuten), zelf doen (50), nabespreken (25) (FR-04).
**Materiaal:** `materiaal/boards.html`, stap 3 tot en met 6.
**Uitkomst:** de advisory board als skill, en een aangescherpte visie met doelen.

### 13:30–13:45 · Voordoen (15 minuten)

**Zeg eerst (NFR-01):** "Voer geen vertrouwelijke gegevens van je organisatie in, ook niet in een eigen account. Werk met openbare informatie of verzonnen gegevens."

**Begin (5 minuten).** Elke deelnemer leest het advies van de supervisory board uit de lunch. Vraag twee deelnemers: "Wat zei je board over hoe jullie bestuur visie, missie en strategie beschrijft? Een vaste stip, of ruimte om te leren?" Vraag daarna: "Scoorde iemands board de strategische vraag anders dan de deelnemer en het duo? Wat deed je ermee?"

**Voordoen (10 minuten).** Open `materiaal/boards.html` op het scherm, bij stap 3.

1. Klik op "Vul in met Voorbeeld BV". Laat zien dat de controles groen worden.
2. Zeg: "Kies experts uit de vakgebieden die je casus nodig heeft. Mis je er een, zoals recht of inkoop, voeg dan je eigen expert toe."
3. Download `advisory-board.zip` en zet hem in je eigen omgeving, met de stappen uit stap 5 van de pagina.
4. Stel de testvraag uit stap 6 en lees één lid voor, met de zwakke plek die het vanuit het eigen vak noemt.
5. Zeg: "Jullie doen hetzelfde, met je eigen organisatie. Wat je invult, blijft in je browser. Schrijf alleen op wat openbaar mag."

### 13:45–14:35 · Zelf doen (50 minuten)

1. **De advisory board bouwen (13:45–14:10).** Elke deelnemer vult stap 3 in en downloadt `advisory-board.zip`. Daarna zet de deelnemer hem in de eigen AI (stap 5) en test hem met de testvraag uit stap 6.
2. **Vraag 1 voorleggen (14:10–14:35).** Elke deelnemer legt het antwoord op vraag 1 en de doelen voor aan beide boards. De zinnen staan in stap 6 van de pagina:
   - aan de advisory board: "Wat zijn de drie zwakste punten, en welke bronnen spreken mij tegen?" Controleer minstens één genoemde bron zelf.
   - aan de supervisory board: "Past mijn koers bij wat ons bestuur zegt over visie, missie en strategie?"

**Tijdens het bouwen.**

- Geef de pagina als bestand mee, of zet hem in de leeromgeving. Hij werkt zonder server en zonder internet.
- Geen skills in de eigen omgeving (vaak ChatGPT zonder werkruimteplan)? Dan geldt de terugvaloptie: een project met de tekst als instructie. Het werkt hetzelfde, alleen roep je de board dan op door in dat project te werken.
- Wie een Gem wil maken: niet doen. Bij persoonlijke accounts zijn Gems vanaf 17 november alleen-lezen, vóór dag 2.
- **Terugvaloptie (FR-07).** Wie geen bruikbare eigen casus heeft, werkt met Voorbeeld BV, via de knop "Vul in met Voorbeeld BV".
- **Verdieping.** Wie klaar is, doet dezelfde opdracht met een tweede model, bijvoorbeeld een reserve-account op Gemini, en brengt de verschillen in bij het nabespreken.

**In de laatste tien minuten van het zelf doen** kijk je bij iedereen naar de samenstelling (FR-17). Heeft de advisory board een harde scepticus, en de supervisory board een tegenspreker? De controles op de pagina laten het zien, maar wie de tekst daarna aanpast, kan ze er weer uit halen.

### 14:35–15:00 · Nabespreken (25 minuten, FR-05)

Twee vragen, in deze volgorde.

1. **"Wat deed de AI goed voor je casus, en waar ging het mis of moest je corrigeren?"** (15 minuten) Elke deelnemer noemt één concreet punt (AC-02). Een concreet punt zegt wat de AI zei of deed, zoals: "De advisory board noemde een bron die niet bestaat." Te vaag is: "Het was best goed." Vraag door: "Wat deed je toen?"
2. **"Wat verandert dit aan je antwoord op een van de vier vragen?"** (8 minuten) Eerst in het duo. Daarna zeggen twee deelnemers het in de groep. Zeg: "Schrijf het op de achterkant van je vragenkaart. Om 16:00 heb je het nodig."
3. **Werkregel 1 (2 minuten, om 14:55).** Start de AI-taak voor de pauze. De AI maakt uit de visie en de doelen een eerste tekst voor de dia's Aanleiding en Strategische doelen.

### Lastige vragen

**"Mijn advisory board is het overal mee eens."**
Kijk of de harde scepticus in de board zit (stap 3) en of de skill aan staat. Noem de board bij zijn naam, en vraag om de drie zwakste punten. Een board die alles goed vindt, toetst niet.

**"De AI noemt een bron die ik niet kan vinden."**
Dat is een concreet punt voor het nabespreken. Een bron die je niet kunt vinden, gebruik je niet. Vraag de AI om de link, en zoek zelf.

**"Mijn twee boards spreken elkaar tegen."**
Dat mag. De supervisory board kijkt naar de koers, de advisory board naar het vak. Jij beslist, en schrijft op waarom.

**"Is wat de board zegt een citaat van die persoon?"**
Nee. De leden heten v_Naam: het zijn denkperspectieven. Wat ze zeggen, is nooit een citaat en hoort niet in materiaal voor buiten. Echte citaten staan alleen op de kaarten van het startsjabloon, met bron.

## Dag 1 · 15:00–15:15 · Pauze

- **AI-taak:** de AI maakt uit de aangescherpte visie en de doelen een eerste tekst voor de dia's Aanleiding en Strategische doelen. Na de pauze gaat die in het casusdeck. De volledige tekst staat op de startpagina en in de LRD.
- Tip voor de deelnemers: vraag de AI om hooguit drie zinnen per vak. Dan past de tekst in het deck.

## Dag 1 · 15:15–16:00 · Deckblok: je casusdeck als HTML-bestand (FR-02, FR-03, FR-08, NFR-10, ADR-035)

**Materiaal:** het lege casusdeck op de downloadpagina (de bron is `materiaal/casusdeck.html`), de geprinte vragenkaart, de tekst van de AI uit de pauze.
**Uitkomst:** een casusdeck met dia 1 (de vragenkaart), dia 2 (Aanleiding) en dia 3 (Strategische doelen), als HTML-bestand en als PDF.

**Eigenaarschap.** De deelnemer is eigenaar van het deck en bepaalt de inhoud. Jij geeft feedback, maar schrijft niet mee (LRD, deel 6.2).

### 15:15–15:30 · Voordoen (15 minuten)

Doe het hele rondje één keer op het scherm, met Voorbeeld BV of je eigen casus. Zeg bij elke stap wat je doet.

1. **Downloaden.** Open het lege casusdeck op de downloadpagina en klik op **Download als HTML**. Het bestand krijgt vanzelf de datum van vandaag in de naam, zoals `casusdeck-2026-11-12.html`.
2. **De instructie voor de AI.** Zeg: "Bovenin het bestand staat een instructie voor je AI. Die hoef je niet te lezen. Je AI leest hem." Klik op **Toon de instructie voor je AI** en laat hem kort zien.
3. **Aan je AI geven.** Voeg het bestand toe in de chat. Geef je aantekeningen erbij: de tekst uit de pauze, je doelen met hun loslaatsignaal, en je nulmeting. Typ de zin die bovenaan het deck staat: "Vul dit casusdeck in volgens de instructie bovenaan het bestand. Geef het hele bestand terug."
4. **Het hele bestand terug.** De AI geeft het bestand terug als download of als één codeblok. Een download sla je op. Een codeblok kopieer je naar een teksteditor in platte tekst, zoals Kladblok of TextEdit (Opmaak > Maak platte tekst). Sla het op met `.html` aan het eind.
5. **Controleer de laatste regel.** Open het bestand in de browser. Onderaan moet "— einde casusdeck —" staan. Staat die er niet, dan is het bestand afgekapt. Vraag dan: "Geef het hele bestand terug, zonder iets weg te laten." Laat zien dat dit kan gebeuren, en hoe makkelijk het te herstellen is.
6. **Kijk de dia's na.** Een te volle dia krijgt op het scherm een rode rand. Maak de tekst dan korter. Maak de letter niet kleiner.
7. **PDF maken.** Klik op **Download als PDF** en kies in het printvenster **Opslaan als PDF**. Je krijgt tien dia's in 16:9, één per pagina.
8. **Bewaar elke versie.** Sla elke nieuwe versie op met de datum in de naam, en bewaar de vorige. Dan kun je terug als de AI iets kapotmaakt.

### 15:30–15:50 · Zelf doen (20 minuten)

1. Elke deelnemer downloadt het lege deck en vult dia 1 tot en met 3 met de eigen AI.
2. **Dia 1, de vragenkaart.** Neem de casus, de getoetste strategische vraag en de nulmeting **letterlijk** over van de geprinte kaart. Verbeter niets: de nulmeting verandert nooit meer. Laat Mijn antwoord nu en de regel Na dag 1 nog leeg. Die komen om 16:00.
3. **Dia 2, Aanleiding.** Wat het bestuur openbaar zegt over visie, missie en strategie, wat dat nu van AI vraagt, en de bronnen in APA 7.
4. **Dia 3, Strategische doelen.** Twee tot vier doelen, elk met een loslaatsignaal (AC-20).
5. Controleer de regel "einde casusdeck" en maak een PDF.

**Sneller overnemen.** Typ de nulmeting over in je aantekeningen. Of maak een foto van de kaart en laat de AI hem overtikken. Controleer dan of de AI letterlijk overnam.

### 15:50–16:00 · Feedback van het duo (10 minuten)

Het duo kijkt naar elkaars dia 1 tot en met 3 en geeft feedback in de vorm "Toen je … / Ik zou …" (FR-08). Drie dingen om naar te kijken:

- Staat de nulmeting er zoals hij op papier stond?
- Heeft elk doel een loslaatsignaal dat je kunt zien of meten?
- Heeft elke bron op dia 2 een link die werkt?

### Lastige vragen

**"Mijn AI neemt geen HTML-bestand aan."**
Plak de inhoud van het bestand in de chat, of geef het bestand de extensie `.txt`. Vraag het antwoord terug als één codeblok, en sla dat op als `.html`.

**"De AI schrijft 'de rest blijft hetzelfde'."**
Dan is het bestand afgekapt. Vraag: "Geef het hele bestand terug, van `<!doctype html>` tot en met het commentaar EINDE CASUSDECK." Lukt het niet? Vraag het dan als bestand om te downloaden, in plaats van als codeblok.

**"De AI heeft mijn nulmeting mooier gemaakt."**
Zet hem terug zoals hij op papier staat. De nulmeting is een meting, en die verandert niet. Zeg het de AI: "Neem de nulmeting letterlijk over."

**"Kan ik PowerPoint gebruiken?"**
Je AI kan een HTML-bestand in één keer lezen en helemaal teruggeven. Je hebt geen account en geen hosting nodig, en de PDF is wat je bij S&N inlevert. Wil je andere kleuren of letters? Laat de AI dan alleen de waarden in `:root` aanpassen, bovenaan het stijlblok.

**"Telt het deck mee voor een cijfer?"**
Nee. In de lesdagen telt het deck nergens voor mee. Het is het concept van je integrale opdracht, die je online afmaakt en inlevert (LRD, deel 9).

## Dag 1 · 16:00–16:30 · Afsluiting: de vier vragen opnieuw (FR-18, FR-33, ADR-036)

**Materiaal:** de geprinte vragenkaart met op de achterkant de zinnen van 11:32 en het nabespreken; `materiaal/boards.html#gebruiken`.
**Uitkomst:** de vragenkaart na dag 1, en een volgende stap in het actieplan.

**Dit is het ritueel.** Het komt aan het eind van elke lesdag terug, in dezelfde volgorde. Zeg dat erbij. Er is geen boardmoment en geen ADR meer: de board toetst hier, en de uitkomst komt op de vragenkaart (ADR-036).

### 16:00–16:03 · Teruglezen (3 minuten)

Zeg: "Pak je vragenkaart. Lees je nulmeting van vanochtend, in stilte." Niemand praat.

### 16:03–16:13 · Herschrijven (10 minuten)

1. Zeg: "Herschrijf elk antwoord dat veranderde, in het vak Mijn antwoord nu. Hooguit drie zinnen. Zet bij Na dag 1 één regel: wat veranderde er, en waarom?"
2. Zeg: "Veranderde een antwoord niet? Laat het staan, en schrijf bij Na dag 1: niet veranderd."
3. Zeg: "Gebruik wat op de achterkant staat: je zinnen van 11:32 en je antwoord uit het nabespreken."
4. Loopt iemand vast, toon dan het voorbeeld van Voorbeeld BV bij V1 (stap 6 van `vier-vragen.html`): "Van een plan voor vijf jaar naar een koers met loslaatsignalen. Fabrikanten en AI-assistenten veranderen de vraag sneller dan een plan meegaat."
5. **Duo (de laatste 2 minuten).** "Leg je kaart naast die van je duo. Wat veranderde bij jou, en wat bij de ander?" (FR-33)

### 16:13–16:23 · De board toetst (10 minuten, FR-18)

1. Zeg: "Kies het antwoord dat vandaag het meest veranderde."
2. Zeg: "Gaat het om vraag 1 of 2, leg het dan voor aan je supervisory board. Gaat het om vraag 3 of 4, dan aan je advisory board."
3. Zeg: "Zet het in drie zinnen: wat was je antwoord, wat is het nu, en waarom veranderde het? Voeg je casusdeck van vandaag toe."
4. Beide boards sluiten af met twee regels voor de vragenkaart. Zeg: "Lees wat de board zegt, en beslis zelf. Zet in de regel Na dag 1 wat de board zei, wat jij ermee doet en je eerste volgende stap. Wijk je af van de board, schrijf dan op waarom."

Een oordeel van een board is een mening. Het besluit blijft bij de deelnemer.

### 16:23–16:28 · Toen en nu (5 minuten)

1. Vraag één deelnemer om één antwoord voor te lezen: eerst de nulmeting van 9:30, dan het antwoord van nu. Vraag om een vrijwilliger. Meldt niemand zich, vraag dan iemand bij wie je tijdens het schrijven een grote verandering zag. Vraag het eerst zachtjes, aan tafel.
2. Reageer met één vraag: "Wat zag je om 9:30 nog niet?" Geef geen cijfer en geen oordeel. Een antwoord is alleen beter of slechter dan het vorige.
3. Zeg: "Dit doen we elke dag. Op dag 3 leggen we alle antwoorden naast elkaar."

### 16:28–16:30 · De volgende stap (2 minuten)

1. Zeg: "Zet je eerste volgende stap in het actieplan in de leeromgeving" (FR-18).
2. Zeg: "Zet vóór dag 2 de nieuwe antwoorden en de regel Na dag 1 in dia 1 van je casusdeck. Dat gaat zoals om 15:15."
3. Zeg: "Neem de geprinte kaart mee naar dag 2. Dag 2 begint ermee. En doe de online voorbereiding, met je pitch voor het investeringscomité."

### Lastige vragen

**"Bij mij is niets veranderd."**
Dat mag. Schrijf "niet veranderd" en, als je wilt, waarom het standhield. Een antwoord dat een dag tegenspraak overleeft, zegt ook iets. Vraag wel: "Bij welke vraag zit je misschien op een lage β?"

**"De board is het niet met me eens."**
De board geeft een mening. Jij beslist. Wijk je af, schrijf dan op waarom. Dat vraagt de regel op de kaart.

**"Alles veranderde. Welke kies ik?"**
Kies het antwoord waar je het minst zeker over bent. Daar heb je het meest aan een tweede blik.

**"Wat is het actieplan?"**
Het actieplan staat in de online leeromgeving van S&N. Wat je daar zet, is je eerste stap na vandaag.

## Dag 2 · Eerst lezen

Nog niet bijgewerkt naar versie 0.22 (vier vragen). Volgt in fase 2; tot dan geldt het programma in de LRD.

## Dag 2 · Investeringscomité (FR-09)

- Deel de rolkaarten uit. Elke rolkaart heeft twee kritiekpunten met bewijs en tegenbewijs: `materiaal/rolkaarten-kritiekpunten.md`.
- Zeg vooraf: "De cijfers op de kaart zijn vaak zelfrapportage of van leveranciers. Vraag dus ook: wat is er gemeten?"

## Dag 2 · Zo bouwen AI-bedrijven

- **De productiviteitsparadox.** Op taakniveau meten studies +14 tot +73%, op bedrijfsniveau ongeveer 0%. 90% van de bedrijven investeert, minder dan 40% ziet meetbare winst [D5]. Dit sluit aan op de J-curve: eerst een dal, dan de winst (Brynjolfsson e.a., 2021).

## Dag 2 · 10:30–10:45 · Pauze: onderzoek langs vier vragen (FR-28, FR-39, ADR-043)

- **Om 10:25: werkregel 1.** Toon stap 2 van `materiaal/probleemformulering.html`; de startpagina linkt ernaar. Zeg: "Vul je knelpunt en de vragen van het comité in, en plak de prompt in een nieuwe chat met de onderzoeksfunctie aan. Je AI zoekt materiaal, nog geen oplossing. Om 11:30 heb je het nodig."
- **Dezelfde chat.** Zeg erbij: "Gebruik deze chat ook om 11:30 en om 12:05. Dan kent je AI het onderzoek al."

## Dag 2 · 11:30–12:30 · Eerst het probleem, dan de businesscase (FR-39, FR-27, FR-14, ADR-043)

### 11:30–11:32 · Het doel (2 minuten)

Zeg: "Een kwartier lossen we niets op. We leggen vast wat het probleem is, vanuit wie er last van heeft." Toon stap 3 van `materiaal/probleemformulering.html`, het kader van Voorbeeld BV. Wijs de strepen aan: elk deel van de zin komt uit een vak. Lees dan de eerste versie voor: "Klantcontact heeft geen AI die klachten sorteert." Vraag: wat is hier mis? Het is een oplossing in vermomming. Een vaste eigenaar per klacht zou het wachten misschien ook korter maken, zonder AI.

### 11:32–11:40 · Vier vakken (8 minuten)

Toon stap 4. Elke deelnemer vult de vier vakken op de lespagina, met het onderzoek van 10:30 ernaast: één signaal of vermoeden per regel. Loop rond en vraag bij een briefje: "Hoe weet je dat?" Weet de deelnemer het niet, dan is het een vermoeden. Dat mag, als het zo heet.

### 11:40–11:45 · Eén zin en het duo (5 minuten)

Elke deelnemer kiest per deel het briefje dat het zwaarst weegt. De zin bouwt zich op in het kader. Het duo leest de zin hardop en stelt de drie vragen uit stap 4: staat er een oplossing in, is de zin geschreven vanuit wie er last van heeft, en heeft elke bewering een signaal?

### 11:45–12:05 · De kansenkaart (20 minuten, FR-27)

1. **Voordoen (10 minuten).** Toon `materiaal/kansenkaart.html`, stap 1 tot en met 8: het proces van Voorbeeld BV, de vier routes, en de vijf plekken waar AI kan helpen. Leg de brug: "Het vak Wie wijst de banen aan waar de last valt, het vak Waar en wanneer de situaties waarin het speelt. Waar zit het probleem van Voorbeeld BV in de keten?" Let op: de banen zijn alle rollen in de keten. Planning en Service staat niet in het vak Wie, maar daar gaat de klacht met de hand naartoe.
2. **Zelf doen (10 minuten).** Toon stap 9, "Jouw proces". Elke deelnemer tekent de eigen procesketen op papier: rollen als banen, fasen als kolommen, een cijfer waar AI kan helpen, en bij elk cijfer wie beslist. Daarna de vraag uit FR-14: waar schuift het knelpunt heen als AI het oplost?

### 12:05–12:30 · De businesscase (25 minuten, FR-14)

1. **De prompt.** Toon stap 5 van `materiaal/probleemformulering.html`. Elke deelnemer beschrijft de kansenkaart in een paar zinnen (of voegt een foto toe), vult de eerste kleine inzet van 10:45 in, en plakt de prompt in de chat van 10:30. De AI schrijft; de probleemstelling staat bovenaan, en het "omdat" bij de aannames.
2. **Bronkritiek, met een echt voorbeeld.** Het vaak geciteerde "95% van de organisaties haalt geen rendement uit AI" komt van MIT NANDA (2025). Het rust op ruim 300 openbare initiatieven, 52 interviews en een enquête onder 153 bezoekers van vier conferenties. Het rapport noemt de eigen cijfers "directionally accurate". Vraag: wat is er gemeten, bij wie en wanneer? Dezelfde vraag stelt het duo bij de bron die het in het origineel opzoekt (AC-04).
3. **Niet af om 12:30?** Dan maakt de AI de businesscase in dezelfde chat af, vóór het voorstel van de lunch. Het duo zoekt de bron dan na de lunch op.

### Lastige vragen

**"Mag de oplossing er echt niet in? Ik weet al wat we gaan doen."**
Schrijf die oplossing apart op, als kandidaat. Een probleemstelling met de oplossing erin kan alleen die oplossing goedkeuren. Zonder de oplossing kan de businesscase laten zien dat jouw oplossing de beste is, ook naast een route zonder AI.

**"Mijn probleem heeft meer dan één oorzaak."**
Kies voor de zin de oorzaak die je het eerst kunt toetsen. De andere blijven in het vak Waarom, en kunnen bij de aannames.

**"Wat is het verschil met de kansenkaart?"**
De probleemstelling zegt wat er misgaat, en voor wie. De kansenkaart zegt waar het in de keten zit, en waar AI kan helpen. Eerst het probleem, dan de plek.

## Dag 2 · Lunch: het voorstel als paper (FR-28, FR-38, ADR-041, ADR-042)

- **Om 12:25: werkregel 1.** Toon stap 2 van `materiaal/experimentpaper.html`; de startpagina linkt ernaar. Zeg: "Open de chat met je businesscase, zet de onderzoeksfunctie aan en plak de prompt. Na de lunch kies je een ontwerp."
- **Geen onderzoeksfunctie?** Dan werkt de prompt ook in een gewone chat. Het voorstel heeft dan minder bronnen, en de controle in werkplaats 2 weegt zwaarder.
- **De AI-wiki** is openbaar. Een AI die de site niet kan openen, zegt dat. De deelnemer zoekt er dan na de lunch zelf in.
- **Een HTML-pagina, geen rapport.** Het paper is één HTML-pagina met schema's, grafieken en een demo, in zakelijk Nederlands volgens de schrijfregels van ASD-STE100 (ADR-042). Een onderzoeksfunctie geeft soms eerst een gewoon rapport. Dan vraagt de deelnemer: "Maak van dit voorstel nu de HTML-pagina uit mijn eerste bericht." Na de lunch downloadt de deelnemer het bestand, met de datum in de naam.

## Dag 2 · Werkplaats 2: ontwerp je experiment (FR-20)

- **Voordoen met een eigen paper (FR-38).** Laat een paper uit een eigen project zien, zoals de test of een AI-model uit foto's van ruimtes plattegronden kan bouwen. Volg de opbouw: de vraag, de hypotheses, het verwante werk, de ontwerpen, en daarna de uitwerking. Wijs aan waar een hypothese een norm en een referentiewaarde kreeg.
- **Eerst één bron.** Het duo zoekt één bron uit het voorstel op in het origineel, met de vraag van 11:30: wat is er gemeten, bij wie en wanneer? Een bron onder "Niet gecontroleerd" telt niet. Laat niet het hele paper lezen: de hypotheses, de tabel met ontwerpen en één bron zijn genoeg.
- **De figuren.** Heeft elke figuur een nummer, een verwijzing in de tekst en een bijschrift met titel, uitleg en "Let op:"? Vraag een deelnemer de zin achter "Let op:" van één figuur voor te lezen: ziet het duo dat ook in de figuur?
- **Eén getal uit een figuur.** Staat het ook in de tekst, met een bron? Heet een verzonnen getal "illustratie"? Zeg: "Een mooie grafiek maakt een fout getal net zo overtuigend als een goed getal."
- **Dan kiezen.** Eén ontwerp, of twee samen. Past het niet vóór dag 3, dan kiest de deelnemer een kleiner ontwerp en zet het grote in de roadmap. Stap 4 van de lespagina geeft de prompt die de normen in het paper vastlegt, met de datum. Het voorbeeld van Voorbeeld BV staat in stap 3.
- **Referentiewaarde.** Doen mensen de taak nu al? Laat de deelnemer dan eerst zelf vijf tot tien gevallen scoren of afhandelen. Pas daarna doet de AI hetzelfde. Zo ontstaat de referentiewaarde zonder AI (AC-15).
- **Kennisvorm (FR-20).** Welke kennis heeft de use case nodig, en wie houdt die bij? Toon `materiaal/kennisvormen.html`. De boodschap: geen vorm wint altijd. Kies per vraag de eenvoudigste vorm die werkt. De laatste stap van de pagina helpt de deelnemer kiezen. Uitleg bij de termen (NFR-08): bij **RAG** zoekt het systeem passende documenten en zet die bij de vraag; een **kennisgraaf** legt begrippen en hun relaties vooraf vast; een **LLM-wiki** bewaart kennis als kaarten met bron en datum, door mensen bijgehouden.
- **Experiment met een agent.** De vier faalwijzen van een agent (zie "Achtergrond en reserve voor de trainer") zijn kant-en-klare evaluatiecriteria. Bijvoorbeeld: elke uitspraak heeft een citaat; bij een ontbrekend feit vraagt de agent door; bij tegenstrijdigheid escaleert hij.

## Dag 3 · Eerst lezen

Nog niet bijgewerkt naar versie 0.22 (vier vragen). Volgt in fase 2; tot dan geldt het programma in de LRD.

## Dag 3 · Transformatieplan en draagvlak (FR-24)

### Vier vragen bij weerstand

Gebruik ze bij "per stakeholder één actie van weerstand naar draagvlak", met de top 3 uit online voorbereiding 1, en in het nabespreken van werkplaats 3.

1. Zie de weerstand als signaal, niet als probleem.
2. Vraag door: wat is de weerstand precies?
3. Zoek de oorzaak. Gaat het om verlies, om onzekerheid, om verlies van controle, of om een terechte zwakke plek in de verandering?
4. Los het niet meteen op.

**Drie valkuilen voor wie leiding geeft:** de weerstand persoonlijk maken, erover moraliseren, en te snel een oplossing willen. Bron: Carucci (2026). Breng dit als vier vragen, niet als nieuw model (KISS-keuze in deel 5.1 van de LRD).

### Cultuur: werkregels voor het eigen team

- (vervallen in 0.22)
- Elke deelnemer schrijft één of twee werkregels bij cultuur in het 7S-plan (FR-24, AC-16). Een werkregel voor een team gaat over hoe het team met AI werkt: de gedeelde waarden en de stijl uit 7S.

### Vaardigheden en mensen

- **Wie leert het vak nog?** Doet de AI altijd het eerste werk, dan bouwen nieuwe medewerkers het vak minder goed op. Junior juristen maakten na ongeveer 90 dagen veel meer fouten toen de AI wegviel (tweedehands gemeld). Geen bron meet het verlies direct [B1]. Tegenmaatregel: nieuwe medewerkers doen de eerste gevallen zelf. Dit hoort in het 7S-onderdeel vaardigheden en mensen.

## Dag 3 · Van experiment naar roadmap (FR-15)

- **Zelfstandigheid per fase.** Toon `materiaal/groeimodel.html`. Elke fase in de roadmap krijgt een niveau: Ask, Assist of Automate, met wie beslist. Het experiment draait op Ask. Automate komt alleen in beeld voor duidelijke gevallen met een laag risico, en altijd met een harde grens.
- **Afstempelen.** Na een reeks goede voorstellen wordt menselijke controle ongemerkt een stempel. Na ongeveer honderd goedkeuringen leest niemand ze meer [B3]. Tegenmaatregel in de test gate: laat een steekproef eerst door een mens scoren, en vergelijk pas daarna met de AI.
- **Geen eigenaar, geen agent.** Wie is verantwoordelijk voor het resultaat? Zonder eigenaar blijft het een demo. Dat is de senior sponsor uit FR-15.
- **Verspreiden of opleggen (Werner & Le-Brun, 2025).** Na een paar geslaagde experimenten is de reflex: "Hoe schalen we dit op?" Dat wordt meestal een opdracht van bovenaf om één werkwijze overal in te voeren. Dan verdwijnt het eigenaarschap, en wie niet aan het experiment meedeed, voert alleen nog uit. Octopusorganisaties laten een werkwijze die werkt zich verspreiden: een ander team neemt hem over en past hem aan. Vraag bij de fase opschaling: "Welk team neemt dit als eerste over, en waarom zou het dat willen?"
- (vervallen in 0.22)

## Dag 3 · Governance (FR-16)

### Werkvorm "Veilig voor wie?"

1. Vraag: "Is jullie use case veilig?" Zeg: "Het eerlijke antwoord is een wedervraag: veilig voor wie, en waarvoor?"
2. Stel de vijf governancevragen uit FR-16 als "Weet je …?"-vraag. Iedereen kiest per vraag: **Ja** / **Nee, maar ik weet wie het weet** / **Nee, en ik weet niet wie het weet**. Laat met de hand stemmen. Toon nooit een verzonnen uitslag.
   1. Weet je in welke risicoklasse van de AI-verordening je use case valt?
   2. Weet je welke persoonsgegevens de AI ziet, wie ze nog meer kan lezen, en of je een DPIA nodig hebt?
   3. Weet je wie eigenaar is van het model en van de data?
   4. Weet je waar een mens het besluit neemt?
   5. Weet je of de AI naar het werkproces kijkt of naar personen?
3. Kies de vraag met de meeste "Nee, en ik weet niet wie het weet". Laat de duo's daar vijf minuten over praten: wie in jouw organisatie weet het antwoord?
4. Vraag: "Wie vraag je morgen?" Iedereen noemt een functie, nooit een naam. (vervallen in 0.22)
5. Daarna beantwoordt elke deelnemer de vijf vragen voor de eigen use case (AC-07).

### Hulpmiddelen bij vraag 4 en 5

- **Vuistregel voor toezicht (Böckeler, in InfoQ, 2026).** Toezicht = kans op een fout × impact van de fout × hoe moeilijk de fout te zien is. Een hoge score op de laatste factor betekent: de fout valt niet op. Hoe hoger de uitkomst, hoe dichter de mens bij het besluit staat.
- **Twee eisen aan elke uitkomst van AI.** Elke uitspraak is te herleiden naar de bron, met een citaat. Bij twijfel of tegenstrijdigheid escaleert het systeem; het gokt niet.
- **Onomkeerbaar en zichtbaar.** Mensen willen vooral een controle bij handelingen die onomkeerbaar én zichtbaar voor anderen zijn, zoals een bericht aan klanten (Pochampally e.a., 2026; kleine studie onder 20 studenten). Laat zo'n handeling eerst langs een mens gaan, ook op niveau Automate.
- **Wie pakt een escalatie op?** In een experiment werd een bedrijf geleid door AI-agenten. Op dag 19 waarschuwde de AI dat het bedrijf de verkeerde kant op ging. Niemand deed er iets mee. Leg dus vast wie een escalatie oppakt.
- **Vraag 5 en de OR.** Kijkt de AI naar prestaties of gedrag van medewerkers? Dan vraagt dat meestal instemming van de OR, en kan de toepassing in de AI-verordening onder hoog risico vallen (bijlage III, werkgelegenheid). Laat een jurist dit per use case toetsen.

## Dag 3 · Werkplaats 3: AI als scepticus

- De AI speelt de stakeholder met de meeste weerstand uit de top 3 van online voorbereiding 1.
- Geef de AI de kritiektrace als bron voor de scepticus, of het deel dat bij de use case past. Vraag de scepticus om bewijs én tegenbewijs. Een scepticus zonder tegenbewijs is een tegenstander, geen toets.
- Nabespreken: welke van de vier soorten weerstand speelde de AI? Verlies, onzekerheid, verlies van controle, of een terechte zwakke plek?

## Dag 3 · Afsluiting: de missie (FR-31)

- Toon het tweede filmpje nog één keer (25 seconden): "Dit is het pad dat je in drie dagen liep."
- (vervallen in 0.22)
- Zeg erbij: deze missie is de stand van nu. De volgende rondes van de lus kunnen hem nog veranderen.

## Achtergrond en reserve voor de trainer

- **De atlas met raamwerken** (Engelstalig): `~/Projects/presentatie-santeon-10-11-2026/background-material/2026-07-01-ai-maturity-frameworks-visuals.html`. Lokaal openen; de pagina laadt zijn bibliotheken uit een eigen map. Gebruik hem bij vragen, niet als lesstof (KISS-keuze in 5.1). De cijfers in sectie 0 zijn verouderd; gebruik het volwassenheidsrapport. De hergebruiknotitie (`onderzoek/2026-11-07-hergebruik-santeon-presentatie.md`, onderdeel 15) zegt per raamwerk bij welk blok het past. Twee kandidaten voor later: de 2×2 van Anand en Wu ("op welke taak richt je AI eerst?") bij de prioriteiten van de roadmap (SN3), en de ladder L0–L5 voor de eigen rol bij de afsluiting (FR-18).
- **Het prototype van een agent, uit de zorg.** Een demo met doorvragen, controle, een tweede AI als beoordelaar en een terugval op trefwoorden. De publieke versie draait zonder live AI: https://businessdatasolutions.github.io/santeon-presentatie/demo.html. Een animatie zonder netwerk: https://businessdatasolutions.github.io/santeon-presentatie/vim-agent-animatie.html. Alleen als reserve bij vragen over FR-15 ("een artefact dat een tester kan proberen") of over een technische test (FR-21). Zeg erbij dat het voorbeeld uit een ziekenhuis komt.
- **Hoe een agent technisch is opgebouwd: geparkeerd, mogelijk voor dag 2.** Tot versie 0.23 stond dit op dag 1 om 10:25 (ADR-040). Het voorbeeld uit de zorg is de publieke pagina over de harness: https://businessdatasolutions.github.io/santeon-presentatie/harness.html. Zeg erbij dat het voorbeeld uit een ziekenhuis komt. De kern: een agent is opgebouwd als een organisatie. Het taalmodel is de professional, de harness (de besturing rond het model) is het kwaliteitssysteem, het contextvenster is het dossier op tafel. Het model huur je, de harness bouw je zelf. De plek is nog niet gekozen. Een kandidaat is werkplaats 2, als een experiment een agent test (FR-20). Neem dan deze twee termen mee (NFR-08):

  | Term | Uitleg |
  |---|---|
  | Harness | Alles rond het model: welke informatie het krijgt, welke hulpmiddelen het mag gebruiken, en wat er gebeurt bij een fout. |
  | Contextvenster | Wat het model op dit moment leest. |

- **Werkvorm "Mens tegen agent": geparkeerd met de opbouw van een agent, mogelijk voor dag 2.** Tot versie 0.33 opende hij het blok van 10:00 op dag 1 (ADR-048). Hij hoort bij de uitleg hoe een agent werkt, niet bij breed gebruik en zeldzame opschaling. Een kandidaat is werkplaats 2, waar de eigen score de referentiewaarde is (FR-20). Materiaal: klacht K-0505 uit `materiaal/voorbeeldcasus.md`, op een dia of het scherm. Het verloop, vijf minuten:

  1. Toon klacht K-0505 uit de voorbeeldcasus. Lees de twee feiten voor: wat de klant schrijft en wat het planningssysteem zegt.
  2. Vraag: "Welke urgentie geef jij deze klacht, 1 tot en met 4?" Laat iedereen tegelijk 1 tot 4 vingers opsteken.
  3. Benoem wat je ziet. De groep is het meestal oneens.
  4. Toon wat de agent doet. De agent escaleert de klacht en geeft geen urgentie. De reden: de klant en het systeem spreken elkaar tegen, en er woont een kwetsbare bewoner.
  5. Zeg: "Bij twijfel is escaleren het goede antwoord, ook voor AI."
  6. Zeg wat dit oplevert voor werkplaats 2: "Je eigen score is de referentiewaarde. Eerst scoor jij, daarna de AI" (FR-20).

  **Live variant:** geef je eigen AI-model de klacht en de urgentieregels uit de voorbeeldcasus. Kijkt het model of het escaleert? Gokt het model een score, dan is dat zelf een les.

  **Waarom eerst zelf:** wie eerst het AI-antwoord ziet, neemt het over. Wie eerst zelf scoort, ziet het verschil.

- **Uit het blok van 10:00 op dag 1 gehaald, voor later (ADR-048).** Deze punten hoorden bij het blok toen het nog "Wat AI nu kan en niet kan" heette. Ze komen in het blok niet meer aan bod. Een plek is nog niet gekozen; de faalwijzen passen bij een experiment met een agent in werkplaats 2 (FR-20).

  - **Gevoel is geen meting.** Ervaren ontwikkelaars werkten in een gerandomiseerde studie met AI 19% trager. Zelf dachten ze dat ze 20% sneller waren (Becker e.a., 2025). Daarom meet je in het experiment, en vertrouw je niet op indruk.
  - **De grillige grens (jagged frontier).** Binnen de grens van wat AI goed kan, maakten consultants 12% meer taken af, werkten ze 25% sneller en was de kwaliteit 34% hoger. Buiten die grens scoorden ze 19 procentpunt slechter, en hun foute adviezen klonken juist overtuigender (Dell'Acqua e.a., 2026; [B2]).
  - **Vier faalwijzen van een agent, en wat ze opvangt.**
    1. Een antwoord zonder grond → verankering: elke uitspraak heeft een citaat uit de bron.
    2. Een ontbrekend feit → doorvragen in plaats van invullen (K-0501).
    3. Tegenstrijdige feiten → escaleren naar een mens (K-0505).
    4. Het eigen huiswerk nakijken → een tweede, aparte controle.
  - **Generatieve AI, agents, voorspellende modellen en data.** Generatieve AI maakt tekst, beeld of code. Een voorspellend model rekent uit wat er waarschijnlijk gebeurt, zoals welke installatie binnenkort een storing krijgt (doel 2 van Voorbeeld BV). Een agent voert met een taalmodel een taak in stappen uit, binnen vaste grenzen. Alle drie hangen af van data. Een voorspellend model heeft eigen gegevens nodig om van te leren.

  Nederlandse uitleg bij de termen (NFR-08):

  | Term | Uitleg |
  |---|---|
  | Agent | Een systeem dat een taalmodel gebruikt om een taak in stappen uit te voeren, binnen vaste grenzen. |
  | Jagged frontier | De grillige grens tussen taken die AI goed kan en taken waarbij AI fouten maakt. |

## Voorbereide antwoorden

**"Is AI wel veilig?"**
Het eerlijke antwoord is een wedervraag: veilig voor wie? Voor de gegevens, voor de klant die de uitkomst krijgt, of voor de medewerker? Elke vraag heeft een eigen antwoord. Dat zijn de vijf governancevragen.

**"Mag ik bedrijfsgegevens in ChatGPT plakken?"**
Niet met vertrouwelijke gegevens, tenzij je organisatie die omgeving daarvoor heeft goedgekeurd. Dan is er een verwerkersovereenkomst, zijn er afspraken over opslag, en traint de leverancier niet op je gegevens. In deze training werk je alleen met openbare of verzonnen gegevens (NFR-01). Weet je het niet? Vraag het je FG of informatiebeveiliger. Een verbod alleen helpt niet: bij een verbod uploadt 67% toch gevoelige data, zonder beleid 33% [A4].

**"En als ik het eerst anonimiseer?"**
Dat helpt. Vrije tekst is vaak toch te herleiden, via een afdeling, een datum of een bijzonderheid. Behandel tekst als persoonsgegevens, tenzij het tegendeel bewezen is.

**"Wie is verantwoordelijk als de AI een fout mist?"**
De organisatie, en daarbinnen de eigenaar van het proces. Verantwoordelijkheid gaat niet over naar een systeem. Daarom begint AI op Ask, en gaan ernstige gevallen en twijfel naar een mens. Het risico in de praktijk: verantwoordelijkheid schuift ongemerkt weg. In een experiment met 1.261 managers daalde de persoonlijke verantwoordelijkheid met 9 procentpunt, en werden 18% minder fouten opgemerkt [B5].

**"Kan een analyse door AI tegen een medewerker worden gebruikt?"**
Leg vooraf vast dat de AI naar het werkproces kijkt en niet naar personen (governancevraag 5). Kijkt de AI toch naar prestaties of gedrag, dan hoort de OR erbij, en kan de toepassing onder hoog risico vallen. Laat een jurist dat toetsen.

**"Gaat AI ons werk overnemen?"**
Over alle leeftijden is het verschil klein. Loondata van Stanford en ADP tot september 2026 tonen geen brede verdringing. Het werk voor starters van 22 tot 25 jaar in de beroepen met de meeste AI-blootstelling krimpt wel [D2]. Het risico in je eigen organisatie is eerder dat mensen het vak verleren. Laat nieuwe medewerkers daarom de eerste gevallen zelf doen.

**"Moeten we iets met de AI-verordening?"**
Ja. Artikel 4 (AI-geletterdheid) geldt sinds 2 februari 2025 voor elke organisatie die AI inzet. Of een toepassing onder strengere regels valt, hangt af van het gebruik. Dat is de risicoklasse, governancevraag 1.
