# ADR-047: Een werkkaart voor de deelnemer, een eigen weergave voor de trainer

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-046 zette per blok de looptekst uit de LRD op de startpagina, onder "Zo loopt dit blok". Die tekst is geschreven voor de ontwerper. Bij het blok "Breed gebruikt, zelden volwassen" staat er bijvoorbeeld: "Daarna: de grillige grens van wat AI goed kan; …". Een trainer die het blok voor het eerst geeft, leest daarin niet wat er gebeurt. Een deelnemer leest er niet in wat hij moet doen.

De startpagina is in de eerste plaats voor de deelnemer. Idealiter gaat al zijn cognitieve energie naar het leren. Hij hoort niet te zoeken waar iets staat of waar hij moet klikken, en ook geen ontwerptaal te ontcijferen. Per blok heeft hij antwoord nodig op zeven vragen:

1. Wat heb ik nodig?
2. Waar let ik vooral op?
3. Wat moet ik weten?
4. Wat doe ik?
5. Waaraan zie ik dat ik goed zit?
6. Wanneer ben ik klaar?
7. Waarvoor vraag ik de trainer?

De trainer heeft iets anders nodig: wat er klaar moet liggen, het verloop met tijden en waar hij op let. Een deel daarvan mag de zaal niet zien. "Geef vóór de nulmeting geen voorbeeld" of "laat niet zien wat een hoge β doet" verraadt op de beamer de werkvorm.

Een nieuwe meting met `scripts/meet-ux.py`, met de KPI's aangepast aan deze eisen, gaf 25 van 32 ([verslag](../../onderzoek/2026-11-08-ux-startpagina.md)). Onder de norm waren:

- de instructie voor de trainer per blok: 0 %;
- de instructie van het blok van nu in de kop: 0 %;
- de werkkaart, compleet, in beeld en kort: elk 0 %;
- ontwerp- en trainerstekst in de weergave voor de deelnemers: 253 stuks.

## Besluit

- **Elk blok krijgt een werkkaart voor de deelnemer** (`deelnemer` in `DATA.days`, NFR-11). Ze heeft zeven vaste onderdelen. Op de pagina heten ze: Je hebt nodig, Let vooral op, Je moet weten, Wat je doet, Je zit goed als, Je bent klaar als en Vraag de trainer.
- **De werkkaart staat in de kop**, in drie kolommen:
  - eerst wat je nodig hebt, waar je op let en wat je moet weten;
  - dan wat je doet;
  - dan of je goed zit, wanneer je klaar bent en waarvoor je de trainer vraagt.
- **Bij "Je hebt nodig" staat ook het eerdere werk** dat het blok gebruikt, met de bron (`uses`).
- **In de lijst is de werkkaart per blok uit te klappen.** Bij het blok van nu staat ze open. Op een smal scherm staat ze vóór de vier vragen.
- **De werkkaart is in de taal van de deelnemer:**
  - hooguit dertig woorden per onderdeel;
  - wat je doet in hooguit vijf stappen van twintig woorden;
  - geen codes uit het ontwerp.
- **Elk blok krijgt een instructie voor de trainer** (`trainer` in `DATA.days`, NFR-12): klaarzetten, het verloop met tijden, en let op. De eerste stap van het verloop begint op de begintijd van het blok.
- **De startpagina toont de instructie alleen met `?rol=trainer`:**
  - in de kop, met de stap van nu gemarkeerd, en bij elk blok in de lijst;
  - een gele band zegt dat de weergave niet op de beamer hoort, en linkt naar de weergave voor de deelnemers;
  - de voet linkt naar het draaiboek en de LRD.
- **Zonder de parameter maakt het script niets voor de trainer aan.** De pagina bevat dan geen instructie, geen ontwerptekst (`detail`) en geen link naar draaiboek of LRD, ook niet verborgen.
- **"Zo loopt dit blok" vervalt op de startpagina.** De looptekst blijft in deel 8 van de LRD. Het detailpaneel daar toont nu ook de werkkaart en de instructie.
- **KISS krijgt een keuze erbij** (deel 5.1): de pagina en het materiaal moeten het leren helpen en mogen niet afleiden. De skill `aiso-beoordeel-onderwijsontwerp` neemt dit op in KISS · Deelnemer en KISS · Begeleider.
- **`scripts/meet-ux.py` meet het.** Acht KPI's zijn aangepast:
  - T1-A, T1-V en T1-B: de instructie per blok en de tijden in het verloop;
  - T3-A: de instructie van het blok van nu in de kop;
  - D1-B: niets van de trainer of uit het ontwerp in de weergave voor de deelnemers;
  - D2-A, D2-V en D2-B: de werkkaart compleet, in beeld op de beamer, en kort.

## Overwogen alternatieven

- **De looptekst herschrijven in gewone taal.** Verworpen: één tekst voor twee lezers bedient er geen van beide. De deelnemer wil weten wat hij doet, de trainer hoe hij het blok leidt.
- **De instructie voor de trainer verbergen met CSS of in een dichte uitklap.** Verworpen: wie de beamer bedient of de pagina doorzoekt, ziet haar toch. Strikte scheiding betekent dat de tekst niet in de pagina staat.
- **Een aparte pagina voor de trainer.** Verworpen: dan zijn er twee pagina's met dezelfde tijdlijn en hetzelfde programma, en die lopen uit elkaar. Eén pagina met een parameter leest dezelfde `DATA`.
- **De instructie onthouden in de browser, zodat de trainer de parameter maar één keer typt.** Verworpen: staat de beamer op dezelfde laptop, dan staat de instructie ineens op het scherm van de zaal. De parameter staat in het adres, en dat is te zien.
- **De zeven vragen als één doorlopende tekst.** Verworpen: vaste koppen op een vaste plek leer je één keer. Daarna zoekt de deelnemer niet meer.

## Gevolgen

- **De instructies staan in de LRD, en die is openbaar** (ADR-045). Wie de LRD opent of de broncode leest, kan ze vinden. De scheiding houdt de instructies uit beeld voor de zaal, maar is geen beveiliging. Er staat niets vertrouwelijks in.
- **De trainer moet de parameter kennen.** Het draaiboek zegt het bij "Zet de startpagina klaar", en de LRD noemt hem in NFR-12. Een lespagina linkt terug naar de weergave voor de deelnemers. Met de terugknop van de browser blijft de trainer in de eigen weergave.
- **Het draaiboek en de instructie op de startpagina overlappen.** Het draaiboek blijft de volledige tekst, met de lastige vragen. De instructie is de samenvatting voor tijdens het blok. Wijkt het draaiboek af, dan geldt de LRD.
- **De instructies voor dag 2 en 3 zijn een eerste versie.** Het draaiboek van die dagen is nog niet bijgewerkt, en de tijden binnen een blok zijn nog niet in een proefronde getest. Dat staat in deel 5.2 als zwak punt.
- **De kop is hoger.** Op de beamer (1920×1080) passen de werkkaart, de vragen en de tijdlijn nog op één scherm. Op een laptop (1366×768) passen de titel, het materiaal en de werkkaart. Dat meten T2-B, D1-V en D2-V.
- **De simulator in `bo-demo/` kreeg een icoon.** Zonder icoon gaf hij bij de eerste keer laden een 404 in de console. Die fout leek eerder tijdelijk (T2-R).

## Raakt

- `materiaal/index.html` (de startpagina), NFR-09, NFR-11 en NFR-12, en de KISS-keuzes in deel 5.1 en 5.2.
- `deelnemer` en `trainer` bij elk blok in `DATA.days` dat geen pauze is (21 blokken).
- Het detailpaneel in deel 8 en de lijst met opleveringen van de trainer.
- `scripts/meet-ux.py`, `materiaal/draaiboek-bouwstenen.md`, `materiaal/bo-demo/` en de skill `aiso-beoordeel-onderwijsontwerp`.
- ADR-046: deels vervangen. Vervangen zijn de looptekst op de startpagina en de link naar het draaiboek in de voet voor iedereen.
