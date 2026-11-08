---
type: toetsrapport
onderwerp: "De startpagina en de lespagina's, bekeken door een nieuwe trainer en een deelnemer"
datum: 2026-11-08
getoetst: materiaal/index.html, de lespagina's in materiaal/ en het programma in DATA.days
methode: scripts/meet-ux.py (Playwright in Chrome, op de site zoals bouw-pages.py hem bouwt)
besluit: ../docs/adr/ADR-046-startpagina-wijst-vragen-en-vindplaats-aan.md (ronde 1), ../docs/adr/ADR-047-werkkaart-en-trainersweergave.md (ronde 2)
---

# De startpagina, bekeken door een nieuwe trainer en een deelnemer

## Oordeel in het kort

Het begon met één zin. Op het scherm stond "Opening: je casus en de vier vragen", maar niets zei waar die vier vragen stonden. De vier chips lichtten op met een kort woord. De vraag zelf stond alleen in een tooltip, en die zie je op een beamer niet. Bij het blok stond geen verwijzing naar de geprinte vragenkaart.

Dat bleek geen los geval. De startpagina deed goed wat ze deed: de klok, de tijdlijn en de pauzes. Maar ze wees de stukken niet aan die een blok noemt, en ze zei niet hoe een blok loopt. We maten met 32 KPI's: kengetallen met een norm. In de nulmeting haalden 18 van de 32 de norm. Na acht verbeteringen halen ze alle 32 de norm.

In een tweede ronde bleek de looptekst die ronde 1 toevoegde, niet te helpen. Die tekst was geschreven voor de ontwerper. Een trainer die een blok voor het eerst geeft, las er niet in wat er gebeurt. Een deelnemer las er niet in wat hij moet doen. Ronde 2 maakt de startpagina eerst een pagina voor de deelnemer, met per blok een werkkaart van zeven vaste vragen. De trainer krijgt een eigen weergave achter `?rol=trainer`, strikt gescheiden van die van de deelnemer. Acht KPI's kregen een nieuwe definitie. In de nieuwe nulmeting haalden 25 van de 32 de norm, na de wijzigingen alle 32 ([ronde 2](#ronde-2-werkkaart-en-trainersweergave-adr-047)).

## Twee gebruikers

- **De trainer** geeft de lesdagen voor het eerst en heeft ze niet ontworpen. Hij heeft de startpagina, de lespagina's en het draaiboek. Hij moet per blok weten wat er gebeurt, en welk materiaal hij laat zien.
- **De deelnemer** zit in de zaal en kijkt naar de beamer of naar de eigen laptop. Zijn aandacht hoort bij de inhoud. Elke vraag als "waar staat dat?" of "wat betekent die code?" kost aandacht die niet naar leren gaat.

## De journeys

### Trainer

| Fase | Wat de trainer doet | Wat hij nodig heeft |
|---|---|---|
| T1 Voorbereiden | Leest in de week ervoor het programma door | Per blok wat er gebeurt, het draaiboek, verwijzingen die kloppen, links die werken |
| T2 Opstarten in de zaal | Zet tussen 8:45 en 9:30 de startpagina op de beamer | Het juiste blok vanzelf, snel een dag wisselen, de kern boven de vouw, geen fouten |
| T3 Een blok geven | Leest de vragen voor en laat materiaal zien | Elk genoemd stuk aangewezen, materiaal zonder scrollen, de vragen voluit, links die openen |
| T4 Overgang en afsluiten | Stuurt de groep de pauze in en sluit de dag af | Werkregel 1 met de AI-taak, het volgende blok, de stand na de lesdag |

### Deelnemer

| Fase | Wat de deelnemer doet | Wat hij nodig heeft |
|---|---|---|
| D1 Oriënteren | Kijkt waar de groep is | Wat hij maakt, het blok in beeld op een laptop, geen codes uit het ontwerp, een pagina die op een telefoon past |
| D2 Opdracht snappen | Leest wat het blok vraagt | Hoe het blok loopt, de vragen voluit, elke vraagcode met zijn naam, een pagina die zonder internet buiten de site werkt |
| D3 Materiaal vinden | Zoekt het stuk dat het blok noemt | Een vindplaats voor elk stuk, een bron bij eigen werk, tegels met een duidelijk label, een startpagina die blijft staan |
| D4 Terugkeren | Gaat van een lespagina terug naar de startpagina | Een link terug, bovenaan, die zegt waarheen en die op de goede dag landt |

## De KPI's

Elke fase heeft vier KPI's, één per vraag. Die vier vragen sluiten elkaar uit en dekken samen het gebruik:

- **Aanwezig (A):** staat de informatie op de pagina?
- **Vindbaar (V):** is ze te vinden zonder hover, zonder scrollen, in zo weinig mogelijk handelingen?
- **Begrijpelijk (B):** is ze te lezen zonder voorkennis van het ontwerp?
- **Betrouwbaar (R):** werkt het, op elk scherm en zonder fouten?

De gemeten waarde is het kengetal. De norm is het stuurgetal: daarop sturen we. "Excellent" betekent dat de norm gehaald is. Twee metingen tellen voor beide gebruikers mee. Een stuk zonder vindplaats hindert de trainer en de deelnemer allebei (T3-A en D3-A). Dat geldt ook voor de vragen voluit in beeld (T3-B en D2-V).

`scripts/meet-ux.py` meet alles automatisch. Het script bouwt de site zoals GitHub Pages hem krijgt, serveert hem lokaal en zet met `?tijd=` de klok op elk blok van elke dag. Het meet op drie schermen: beamer (1920×1080), laptop (1366×768) en telefoon (390 px breed).

Dit is de tabel van ronde 1. Acht KPI's kregen in ronde 2 een nieuwe definitie: T1-A, T1-V, T1-B, T3-A, D1-B, D2-A, D2-V en D2-B. Die staan onder [ronde 2](#ronde-2-werkkaart-en-trainersweergave-adr-047).

| KPI | Fase | Meting | Norm | Nulmeting | Hermeting |
|---|---|---|---|---|---|
| T1-A | Voorbereiden | Blokken met een looptekst op de startpagina | 100 % | 0 % (0 van 19) | 100 % |
| T1-V | Voorbereiden | Klikken van de startpagina naar het draaiboek | 1 | niet bereikbaar | 1 |
| T1-B | Voorbereiden | Tijden in "Je gebruikt" die naar een bestaand blok wijzen | 100 % | 100 % (27 van 27) | 100 % |
| T1-R | Voorbereiden | Dode links en ankers op de site, ook in `DATA` | 0 | 0 | 0 |
| T2-A | Opstarten | Momenten waarop de kop het juiste blok toont | 100 % | 100 % (33 van 33) | 100 % |
| T2-V | Opstarten | Dag wisselen met één klik of één toets | ja | ja | ja |
| T2-B | Opstarten | Titel, vraagchips en tijdlijn boven de vouw op de beamer | ja | ja | ja |
| T2-R | Opstarten | Fouten in de console, op alle pagina's | 0 | 0 (zie onder) | 0 |
| T3-A | Blok geven | Genoemde stukken met een tegel bij het blok | 100 % | 31 % (5 van 16) | 100 % |
| T3-V | Blok geven | Blokken waarvan het materiaal zonder scrollen in beeld is (beamer) | 100 % | 21 % (3 van 14) | 100 % (17 van 17) |
| T3-B | Blok geven | Blokken waarvan de vragen voluit in beeld staan, zonder hover | 100 % | 48 % (10 van 21) | 100 % |
| T3-R | Blok geven | Materiaallinks die openen (intern 200, extern https) | 100 % | 100 % | 100 % |
| T4-A | Overgang | Pauzes met werkregel 1 en de AI-taak, 4 minuten vóór en tijdens | 100 % | 100 % | 100 % |
| T4-V | Overgang | Pauzes waarvan het materiaal in de band klikbaar is | 100 % | 100 % | 100 % |
| T4-B | Overgang | Blokken waarbij de kop het volgende blok noemt | 100 % | 100 % | 100 % |
| T4-R | Overgang | Dagen waarop de kop na 16:30 de volgende lesdag toont | 100 % | 100 % | 100 % |
| D1-A | Oriënteren | Blokken met "Je maakt" in de kop | 100 % | 100 % | 100 % |
| D1-V | Oriënteren | Blokken waarvan titel en materiaal zonder scrollen in beeld zijn (laptop) | 100 % | 38 % (8 van 21) | 100 % |
| D1-B | Oriënteren | Codes uit het ontwerp (FR-, SN, ADR-) in beeld | 0 | 1 | 0 |
| D1-R | Oriënteren | Pagina's die op een telefoon opzij schuiven | 0 | 1 | 0 |
| D2-A | Opdracht | Blokken waarvan de looptekst openstaat als het blok loopt | 100 % | 0 % | 100 % |
| D2-V | Opdracht | Vragen voluit in beeld, zonder hover (zelfde meting als T3-B) | 100 % | 48 % | 100 % |
| D2-B | Opdracht | Vraagcodes met hun naam, zoals "V3 Investeren" | 100 % | 92 % (12 van 13) | 100 % |
| D2-R | Opdracht | Bronnen buiten de site die de startpagina laadt | 0 | 0 | 0 |
| D3-A | Materiaal | Genoemde stukken met een tegel (zelfde meting als T3-A) | 100 % | 31 % | 100 % |
| D3-V | Materiaal | Stukken in "Je gebruikt" met een bron tussen haakjes | 100 % | 100 % (35 van 35) | 100 % |
| D3-B | Materiaal | Tegellabels die zeggen wat erachter zit | 100 % | 92 % (22 van 24) | 100 % |
| D3-R | Materiaal | Externe links die in een nieuw tabblad openen | 100 % | 100 % | 100 % |
| D4-A | Terugkeren | Lespagina's met een link terug | 100 % | 100 % (9 van 9) | 100 % |
| D4-V | Terugkeren | Lespagina's waar die link zonder scrollen in beeld is (laptop) | 100 % | 56 % (5 van 9) | 100 % |
| D4-B | Terugkeren | Links terug die zeggen waarheen | 100 % | 100 % | 100 % |
| D4-R | Terugkeren | Links terug die landen op een dag waarop de pagina gebruikt wordt | 100 % | 100 % | 100 % |

**Hoe "genoemd stuk" (T3-A) telt.** De vragenkaart en het casusdeck liggen drie dagen op tafel. Elk blok dat ze noemt, wijst ze aan. Dat geldt voor de titel, "Je gebruikt" en "Je maakt", en "de nulmeting" en "de vier vragen" tellen als de vragenkaart. Een ander stuk in "Je gebruikt", zoals "Businesscase (11:30)", is eigen werk. De bron tussen haakjes zegt waar het vandaan komt. Dat stuk telt alleen als de titel of "Je maakt" het noemt, want dan gaat het blok erover.

**De lespagina's bij D4.** Het casusdeck valt erbuiten. Dat is een bestand dat de deelnemer zelf invult, en een link terug hoort daar niet in.

## Waar het laag scoorde

1. **De vragen stonden niet voluit in beeld (T3-B, D2-V: 48 %).** De startpagina toonde een vraag voluit alleen als een blok precies één vraag had. Bij de opening en de afsluiting van elke dag, en bij "Waarom geen plan volstaat", zag je vier korte woorden. Daar draait het juist om alle vier.
2. **De vragenkaart werd nergens aangewezen (T3-A: 31 %).** Acht blokken noemen de vragenkaart, de nulmeting of de vier vragen. Bij geen van die blokken stond een tegel, en ook geen zin over de geprinte kaart.
3. **Hoe een blok loopt, stond alleen in de LRD (T1-A, D2-A: 0 %).** Een invaller moest naar deel 8 van de LRD om het verloop te lezen. Het draaiboek was vanaf de site niet te bereiken (T1-V).
4. **Het materiaal stond onder de vouw (T3-V: 21 %, D1-V: 38 %).** De kop toonde het blok van nu, maar niet het materiaal. Na 10:00 moest je scrollen om de tegel te vinden.
5. **Kleine slijtplekken:**
   - de code FR-37 op de vraagtoets (D1-B);
   - een menupad dat `boards.html` op een telefoon breder maakt dan het scherm (D1-R);
   - twee labels van één woord (D3-B);
   - vier lespagina's met de link terug alleen onderaan (D4-V);
   - "V3 · Hoe zorg ik …" zonder het woord Investeren (D2-B).

## Verbeteringen en hun toets

Elke verbetering heeft een toets: de KPI's die erbij horen, met de norm als grens. `python3 scripts/meet-ux.py --toets` draait alle toetsen en stopt met code 1 als er één mislukt.

| | Verbetering | Toets (KPI) |
|---|---|---|
| V1 | De kop toont de vragen van het blok voluit, met de zin "De vier vragen staan ook op je geprinte vragenkaart, dia 1 van het casusdeck." | T3-B, D2-V: elke vraagtekst staat in beeld zonder hover of scrollen, bij elk blok met vragen. D2-B: elke vraagcode met zijn naam. |
| V2 | De kop toont het materiaal van het blok van nu | T3-V en D1-V: een tegel van het blok staat zonder scrollen in beeld, op beamer en laptop |
| V3 | De vragenkaart staat als materiaal bij acht blokken. Het deckblok van dag 2 krijgt de prompt voor de businesscase en het experimentpaper, en twee labels zijn langer. | T3-A, D3-A: elk genoemd stuk heeft een tegel met de juiste link. D3-B: labels van twee woorden of meer, zonder bestandsnaam. |
| V4 | Per blok "Zo loopt dit blok", uit te klappen. Bij het blok van nu staat het open, en codes gaan eruit. | T1-A: elk blok met een looptekst. D2-A: die van het blok van nu staat open. D1-B: geen codes in beeld. |
| V5 | De voet linkt naar het draaiboek in de openbare repo | T1-V: één klik |
| V6 | Vier lespagina's met een link terug, bovenaan | D4-V: de link staat zonder scrollen in beeld |
| V7 | De code FR-37 weg uit de vraagtoets | D1-B: geen codes in beeld |
| V8 | Een menupad in `boards.html` breekt op een telefoon af | D1-R: geen pagina schuift opzij |

De kop werd hoger. Daarom bewaken T2-B en D1-V of de kern boven de vouw blijft, op de beamer en op een laptop. Dat lukt. Ook een blokgrens is met de echte klok getest: om 9:59 gaat de looptekst van de opening dicht en die van het volgende blok open.

**T2-R.** De eerste nulmeting vond één fout in de console: een 404, die het script toen zonder adres meldde. Het script noemt nu het adres erbij. Een tweede meting van dezelfde versie (`--bron HEAD`) vond geen fout. De 404 kwam dus niet uit de code en is ook niet opgelost: hij kwam één keer voor. Daarom staat T2-R in de nulmeting op 0, en haalden 18 KPI's de norm, niet 17. Komt de fout terug, dan noemt het script nu het adres.

## Ronde 2: werkkaart en trainersweergave (ADR-047)

### Aanleiding

Na ronde 1 stond bij elk blok "Zo loopt dit blok". Bij "Breed gebruikt, zelden volwassen" stond daar onder meer: "Daarna: de grillige grens van wat AI goed kan; …". Een trainer die het blok voor het eerst geeft, las daarin niet wat er ging gebeuren, en een deelnemer ook niet.

De startpagina is eerst voor de deelnemer. Idealiter gaat al zijn cognitieve energie naar het leren, en niet naar zoeken waar iets staat of waar hij moet klikken. Per blok heeft hij antwoord nodig op zeven vragen:

1. Wat heb ik nodig?
2. Waar let ik vooral op?
3. Wat moet ik weten?
4. Wat doe ik?
5. Waaraan zie ik dat ik goed zit?
6. Wanneer ben ik klaar?
7. Waarvoor vraag ik de trainer?

De trainer heeft iets anders nodig: wat er klaar moet liggen, het verloop met tijden en waar hij op let. Een deel daarvan mag de zaal niet zien, zoals "geef vóór de nulmeting geen voorbeeld".

### Wat er in de journeys verandert

| Fase | Wat de gebruiker nu ook nodig heeft |
|---|---|
| T1 Voorbereiden | Per blok een instructie in de eigen weergave: klaarzetten, het verloop met tijden, en let op |
| T3 Een blok geven | De instructie van het blok van nu in de kop van de eigen weergave, met de stap van nu gemarkeerd |
| D1 Oriënteren | Niets in beeld of in de pagina wat voor de trainer of voor het ontwerp is |
| D2 Opdracht snappen | De werkkaart: de zeven antwoorden, compleet, in beeld en kort |

### De aangepaste KPI's

Acht KPI's kregen een nieuwe definitie. De andere 24 bleven gelijk en haalden in beide metingen van ronde 2 de norm, op T2-R na (zie onder). Er meet ook geen KPI meer twee keer hetzelfde. D2-V was een kopie van T3-B en D3-A van T3-A. D3-A meet nu zelf, en de vraagcodes zonder naam (eerst D2-B) tellen mee in D1-B.

| KPI | Meting in ronde 2 | Norm | Nulmeting | Hermeting |
|---|---|---|---|---|
| T1-A | Blokken met een volledige instructie in de trainersweergave: klaarzetten, minstens twee stappen verloop, let op | 100 % | 0 % (0 van 21) | 100 % |
| T1-V | Klikken van de trainersweergave naar het draaiboek | 1 | 1 | 1 |
| T1-B | Tijden die kloppen: in "Je gebruikt", en in het verloop (de eerste stap op de begintijd, alle tijden in het blok, oplopend) | 100 % | 56 % (27 van 48) | 100 % (48 van 48) |
| T3-A | Blokken waarvan de eerste stap van de instructie zonder scrollen in de kop staat (trainersweergave, laptop) | 100 % | 0 % (0 van 21) | 100 % |
| D1-B | Ontwerp- of trainersinhoud in de weergave voor de deelnemers: codes in beeld, vraagcodes zonder naam, tekst van de trainer of uit `detail` in de pagina (ook verborgen), links naar draaiboek of LRD | 0 | 253 | 0 |
| D2-A | Blokken waarvan de kop alle zeven onderdelen van de werkkaart toont als het blok loopt | 100 % | 0 % (0 van 21) | 100 % |
| D2-V | Blokken waarvan de hele werkkaart zonder scrollen in beeld is (beamer) | 100 % | 0 % | 100 % |
| D2-B | Onderdelen binnen de norm: hooguit 30 woorden, wat je doet in hooguit 5 stappen van 20 woorden, geen codes | 100 % | 0 % (0 van 147) | 100 % (147 van 147) |

In de nulmeting haalde T1-V de norm al: de voet linkte toen voor iedereen naar het draaiboek. D1-B telt die link nu als lek. De woordnorm in D2-B komt uit het scherm: een onderdeel moet op de beamer in twee of drie regels passen, een stap in één zin.

### Verbeteringen en hun toets

| | Verbetering | Toets (KPI) |
|---|---|---|
| W1 | Elk blok krijgt een werkkaart (`deelnemer` in `DATA.days`). In de kop staat ze in drie kolommen: wat je nodig hebt, waar je op let en wat je moet weten; wat je doet; of je goed zit, wanneer je klaar bent en waarvoor je de trainer vraagt. In de lijst is ze uit te klappen. | D2-A, D2-V, D2-B |
| W2 | Elk blok krijgt een instructie voor de trainer (`trainer` in `DATA.days`). Die verschijnt alleen met `?rol=trainer`: in de kop met de stap van nu, en bij elk blok in de lijst. | T1-A, T1-B, T3-A |
| W3 | Strikte scheiding. Zonder de parameter maakt het script niets voor de trainer aan. De looptekst en de links naar draaiboek en LRD zijn weg uit de weergave voor de deelnemers. | D1-B |
| W4 | De voet van de trainersweergave linkt naar het draaiboek en de LRD, en een gele band linkt naar de weergave voor de deelnemers | T1-V |
| W5 | De simulator in `bo-demo/` krijgt een icoon | T2-R |

**De tegenproef.** Een toets die niets vindt, kan ook blind zijn. Daarom zochten we dezelfde woorden in beide weergaven, om 10:05 op dag 1: "Klaarzetten", "Trainersweergave", "draaiboek", "LRD-AISO26009", "Zeg bij de maquette" en "K-0505". De weergave voor de deelnemers bevat ze geen van alle. De trainersweergave bevat ze allemaal.

**Twee meetfouten, onderweg rechtgezet.**

1. D1-B telde eerst de broncode van het script mee. Daar staat het sjabloon van de trainersweergave in, met een link naar de LRD. Dat is geen inhoud die de deelnemer krijgt. D1-B meet nu de pagina zoals de browser haar opbouwt, zonder `<script>`.
2. D1-B telde daarna een zin uit `detail` die ook als stap op de werkkaart staat: "Herschrijf elk antwoord dat veranderde …" (dag 2, 16:00). Een zin die de deelnemer hoort te lezen, is geen lek. D1-B slaat zulke zinnen nu over.

**T2-R, opgelost.** In de eerste hermeting kwam de 404 zonder adres terug. Nu is de oorzaak bekend. De simulator had geen icoon, dus vroeg Chrome bij de eerste keer laden `/favicon.ico` op. Daarna onthoudt Chrome dat het icoon ontbreekt. Daarom leek de fout in ronde 1 tijdelijk. De simulator heeft nu het icoon van de lespagina's, en `materiaal/bo-demo/LEESMIJ.md` noemt de aanpassing.

**De ruimte op de beamer is klein.** Om 10:05 eindigt de werkkaart op 939 van de 1080 pixels en de tijdlijn op 1059. Wordt een werkkaart langer, dan zakt de tijdlijn onder de vouw. T2-B en D2-V bewaken dat. De woordnorm van D2-B houdt de werkkaart kort.

## Wat de meting niet meet

- **De mens zelf.** De KPI's meten wat de pagina toont, niet wat een invaller ervan begrijpt. Laat vóór 12 november een collega die de lesdagen niet kent de startpagina gebruiken met `?tijd=9:35`, `?tijd=11:45` en `?tijd=15:20`: eerst als deelnemer, dan met `&rol=trainer`. Kijk of hij zonder hulp de vragenkaart, het materiaal, de werkkaart en het verloop vindt. Dat kost een kwartier.
- **De inhoud van de werkkaart en de instructie.** Het script meet of de onderdelen er zijn, kort zijn en geen codes hebben. Of ze kloppen en helpen, meet het niet. De instructies voor dag 2 en 3 zijn een eerste versie. Het draaiboek van die dagen is nog niet bijgewerkt, en de tijden binnen een blok zijn niet in een proefronde getest.
- **Scheiding is geen beveiliging.** De instructies voor de trainer staan in de LRD, en die is openbaar. Wie de LRD opent, kan ze lezen. De scheiding houdt ze uit beeld voor de zaal. Er staat niets vertrouwelijks in.
- **Leesbaarheid op afstand.** De tekst op de tijdlijn is 11 tot 12 pixels. Vanaf achterin de zaal is dat niet te lezen. Op die tijdlijn kijk je hoe laat het is; de titels staan ook in de kop.
- **Externe links.** Het script controleert of ze https zijn, niet of ze openen.
- **Een hint vóór de nulmeting.** Wie om 9:40 de werkkaart van een later blok openklapt, leest daar woorden als "verkennen en benutten". De uitklap staat dicht, en de nulmeting duurt acht minuten, alleen, op papier. Dat risico is klein en bewust genomen (ADR-046). De waarschuwingen voor de trainer, zoals "geef geen voorbeeld", staan sinds ronde 2 niet meer in de weergave voor de deelnemers.

## Opnieuw meten

```bash
python3 scripts/meet-ux.py --toets             # de werkmap, beide weergaven
python3 scripts/meet-ux.py --bron HEAD~1       # een eerdere versie, ter vergelijking
```
