# Wijzigingslog — LRD AISO26009 Lesdagen

Elke versie van de [LRD](LRD-AISO26009-lesdagen.html), met de besluiten die erbij horen ([ADR's](docs/adr/README.md)). Nieuwste versie bovenaan. Het versienummer in de kop van de LRD is gelijk aan de bovenste regel hier.

## 0.26 — 2026-11-08

**Toegevoegd**
- FR-38: het experiment staat in een paper met de opbouw van een wetenschappelijk artikel, en dat schrijft de AI. In de lunch van dag 2 schrijft de AI het voorstel. Het heeft vier delen:
  - de aanleiding, met onderzoeksvraag en toetsbare hypotheses;
  - wat onderzoek, koplopers en experts zeggen, ook in de AI-wiki van de trainer;
  - minstens drie ontwerpen;
  - bronnen in APA 7.

  Na het experiment komt de uitwerking erbij (ADR-041).
- `materiaal/experimentpaper.html`: de lespagina met drie prompts (voorstel, keuze, uitwerking) en een voorbeeld van Voorbeeld BV met drie echte bronnen. De tekst van het voorbeeld staat in `materiaal/voorbeeldcasus.md` (ADR-041).
- Een kaart "Het experiment als paper" in deel 6.5, en de lespagina in de lijst met lesmateriaal en op de opleverlijst voor de trainer (ADR-041).

**Gewijzigd**
- De AI-taak van de lunch op dag 2 is het voorstel als paper, met de prompt als materiaal. Werkplaats 2 begint met dat voorstel: één bron in het origineel, een ontwerp kiezen en de normen vastleggen. De afsluiting van dag 2, de opening van dag 3 en de AI-taak van 10:30 op dag 3 noemen het paper (ADR-041).
- FR-06, FR-20, FR-21, AC-14 en AC-15 noemen het paper. AC-14 vraagt ook dat het duo één bron uit het paper opzocht (ADR-041).
- De KISS-keuze "één product" noemt de businesscase en het experimentpaper als de stukken achter de dia Eerste prioriteit. In het risico over een vastgelopen experiment staat niet meer "één dia, geen verslag". Het risico over verzonnen bronnen geldt ook voor het paper. Fase 2 test de prompts in drie AI-omgevingen (ADR-041).
- De startpagina toont het materiaal van een pauze als link achter de AI-taak, ook in de band van werkregel 1.
- ADR-034 is deels vervangen door ADR-041.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.25 — 2026-11-08

**Gewijzigd**
- De KISS-keuze voor één voorbeeldcasus noemt de maquette van een ziekenhuis als uitzondering, met de reden. Deel 5.2 zegt niet meer "alle lespagina's" (ADR-040).

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.24 — 2026-11-08

**Toegevoegd**
- `materiaal/ziekenhuis.html`: de maquette van een ziekenhuis uit de presentatie over AI in de zorg. Twaalf stappen tonen de cijfers van de AI Monitor Ziekenhuizen 2026. Het is één bestand met de bibliotheken van jsDelivr, en zonder de verwijzingen naar het programma van die sessie (ADR-040).
- De AI Monitor Ziekenhuizen 2026 (M&I/Partners) in de bronnen. Een punt over de maquette in het draaiboek, bij het blok van 10:00 (ADR-040).

**Gewijzigd**
- Dag 1, "Wat AI nu kan en niet kan": het materiaal is de maquette, niet meer de pagina over de harness. De opleverlijst, het risico over een voorbeeld uit een andere sector en fase 0 noemen de maquette (ADR-040).
- ADR-018 is deels vervangen door ADR-040.

**Verwijderd**
- Hoe een agent technisch is opgebouwd, met de termen harness en contextvenster, staat niet meer op dag 1. Het is geparkeerd in het draaiboek onder "Achtergrond en reserve", mogelijk voor dag 2 (ADR-040).

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.23 — 2026-11-08

**Gewijzigd**
- Overal "de board" in plaats van "het board", met "elke board" en "de board die …". De deelnemers komen uit het bedrijfsleven, en daar is "de board" gangbaar. Het geldt voor de LRD, `boards.html` (ook de skillteksten), het draaiboek, `vraagtoets.html`, ADR-036 en ADR-039. Oudere ADR's en changelogregels blijven zoals ze waren.
- De BO-simulator in `materiaal/bo-demo/` test bij Run One Step eerst de plek van de rode bol en werkt daarna het model bij. In het origineel liep het vlak een test achter. Een nieuwe beste plek lag dan onder het vlak, en de rode bol stond op de plek die net getest was. Twee schermafbeeldingen zijn opnieuw gemaakt, en `vier-vragen.html` volgt. De LRD verandert niet.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.22 — 2026-11-08

**Toegevoegd**
- De vier vragen als ruggengraat (`DATA.vragen`, V1–V4): richting, transformeren, investeren en roadmap. Elke vraag heeft een methode, een vaardigheid en tools. Programmablokken en deckonderdelen verwijzen ernaar met `v`. Deel 6.1 toont ze als kaarten (ADR-033).
- Deel 2: wicked problems (Rittel & Webber, 1973) en verkennen en benutten (March, 1991). Daarbij de portfoliokaart, de bandiet, Bayesiaans optimaliseren, reële opties en de two-way door (ADR-033).
- Het ritueel met de vragenkaart: elke dag openen en sluiten met de vier vragen. Op dag 1 om 9:30 is er een nulmeting (FR-33, AC-21, AC-22; ADR-033).
- Twee nieuwe blokken: "Waarom geen plan volstaat" op dag 1 (FR-34) en "Klein inzetten: de deur die terug kan" op dag 2 (FR-35; ADR-033, ADR-037).
- Het casusdeck als lokaal HTML-bestand met een PDF-knop: `materiaal/casusdeck.html`, met tien dia's en een openbare downloadpagina (FR-02, NFR-10; ADR-035). Een tweede knop bewaart het HTML-bestand met de datum in de naam, een derde toont de instructie voor de AI.
- `materiaal/vier-vragen.html` en `materiaal/bo-demo/`: de lespagina voor 11:00 en een kopie van de simulator, met een reparatie zodat de schuif β werkt (ADR-033). De simulator is in de huisstijl: paneel, legenda en 3D-scène, met nieuwe schermafbeeldingen. De tekst is Engels gebleven.
- Deel 1 krijgt "Waarvoor de deelnemer komt": de definitie van een strategische AI-vraag, de waardepropositie en de klus waarvoor de deelnemer komt. Ook pijnpunten en winst (`DATA.value`) en twee gebruikersverhalen. Daarbij een nieuwe lead (ADR-039).
- De vraagtoets om 11:40 op dag 1 en de ijking ervan, met `materiaal/vraagtoets.html` en `materiaal/vraagtoets-ijkset.md` (FR-36, FR-37, AC-23; ADR-039).
- Startpagina: een band met de vier vragen, waarin de vragen van het blok van nu oplichten (NFR-09; ADR-033).
- Vier risico's erbij: een ritueel zonder inhoud, een afgekapt casusdeck, een AI die anders oordeelt over de strategische vraag, en een vraagtoets die uitloopt. De KISS-lijst is opnieuw geschreven en telt 14 paren (ADR-033 tot en met ADR-039).

**Gewijzigd**
- Het programma: elke dag opent en sluit met de vier vragen. Dag 1 verdiept vraag 1, dag 2 vraag 3, en dag 3 vraag 2 en 4. Het deckblok duurt elke dag 45 minuten (ADR-033, ADR-036).
- Het deck telt tien dia's: de vragenkaart en de negen onderdelen van de integrale opdracht. Randvoorwaarden en risicoanalyse zijn weer apart, en de Conclusie is op dag 3 een concept (ADR-034).
- De board toetst in de afsluiting het antwoord dat het meest veranderde. `boards.html` vraagt geen ADR meer (FR-18; ADR-036).
- Het nabespreken heeft twee vragen (FR-05). Het comité verdeelt tien fiches over de pitches (FR-09). Het buildplan heet roadmap voor jaar 1 en heeft uitwijkroutes (FR-15). Het experiment komt op een dia (FR-21). FR-01 spreekt van een voorlopige strategische vraag (ADR-033, ADR-034, ADR-037, ADR-039).
- Herschreven: FR-02, 03, 06, 14, 17, 20, 24, 26, 28, 30, 31 en 32, en NFR-09. Ook AC-01, 02, 04, 05, 06, 12, 14 en 20. Verder de werkplaatsopdrachten, de trainerslijst, de risico's en fase 0 tot en met 2.

**Verwijderd**
- De bouwstraat: deel 6.4, `DATA.pipeline`, `DATA.examples`, FR-22, FR-23, FR-25 en AC-17, en de bronnen bij de AI-bedrijven, Nygard en Lacan (ADR-034).
- De boardmomenten: het bloktype `board`, `DATA.boardMoments` en FR-19 (ADR-036).
- Werkregels 2 tot en met 4 (FR-29, AC-19), de rondgang (FR-13, AC-08), het stakeholderblok op dag 1 en "Zo bouwen AI-bedrijven" (ADR-037).
- Kolb en COM-B als ontwerpkader in deel 2, het werkplaatslog en `kennisvormen.html` uit het programma (ADR-033, ADR-034).

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7. Het lege casusdeck staat openbaar op https://businessdatasolutions.github.io/aiso-casusdeck/ (repo `businessdatasolutions/aiso-casusdeck`, alleen het lege template; ADR-035).

## 0.21 — 2026-11-08

**Toegevoegd** (ADR-032)
- Een nieuw veld `uses` per programmablok: het eigen werk dat een blok gebruikt, uit een eerder blok, uit de AI-taak van een pauze of van thuis. Bij elk stuk staat waar het vandaan komt. Negentien blokken hebben het.
- Startpagina: de regel "Je gebruikt:" boven "Je maakt:", in de lijst en bij het blok van nu.
- Deel 8: het detailpaneel en de printtabel hebben een regel en een kolom "Eigen werk als invoer".

**Gewijzigd** (ADR-032)
- `input` bevat alleen nog werk uit de online omgeving, zoals de kolomnaam in deel 8 zegt. Het eigen werk uit dertien blokken staat nu in `uses`, waaronder de top 3 stakeholders uit ADR-030.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.20 — 2026-11-08

**Gewijzigd** (ADR-031)
- NFR-06: geen timer meer. Tijdblokken blijven veelvouden van 5 minuten, en de tijdlijn op de startpagina laat zien waar de dag staat.
- NFR-09: de startpagina toont het blok van nu bovenaan, een tijdlijn met een streep op de tijd van nu, en per blok het materiaal. Scrolt de trainer naar beneden, dan blijft alleen de tijdlijn staan. Werkregel 1 staat onder de tijdlijn.
- Deel 5, KISS · Begeleider: een startpagina met een tijdlijn en zonder afteller.
- Risico "Een boardmoment loopt uit": de maatregel steunt op één beslispunt per moment en de tijdlijn. Verwijst nu naar NFR-09 in plaats van NFR-06.
- Startpagina `materiaal/index.html`: de kop rolt mee met de pagina, de tijdlijn blijft boven in beeld staan. Een klik op een blok in de tijdlijn brengt dat blok in de lijst in beeld. Bij een nieuw blok scrolt de pagina alleen mee als de kop al uit beeld is.
- ADR-021 is deels vervangen door ADR-031.

**Verwijderd**
- Startpagina: de afteller, de standen "Volg de klok" en "Handmatig", de knoppen Pauze en Opnieuw, de klok rechtsboven en de opslag in de browser.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.19 — 2026-11-07

**Gewijzigd** (ADR-030)
- Dag 1, opening: na het vastleggen van de casus legt de trainer met het eerste filmpje uit wat visie, missie en strategie zijn, zonder vooruit te wijzen. De deelnemers krijgen de opdracht op te zoeken wat hun bestuur daarover zegt.
- Dag 1, pauze van 10:45: de AI zoekt openbare stukken van het bestuur over visie, missie, strategie en AI. De AI-taak over de sector vervalt.
- Dag 1, Van visie naar doelen: het blok begint met de omslag (tweede filmpje, gecompliceerd tegenover complex, de lus) en gebruikt de stukken van het bestuur bij de doelen.
- Dag 1, 12:15: alleen nog het supervisory board samenstellen. Het blok heet "Je supervisory board".
- FR-30 en FR-32 volgen de nieuwe volgorde. Het materiaal op de startpagina heeft neutrale namen ("Filmpje 1", "Filmpje 2", "Tutorial over strategie"), zodat de omslag niet vooraf te zien is.
- Startsjabloon: de lunchtaak verwijst naar de stukken uit de pauze. Bouwstenen voor het draaiboek: een nieuwe bouwsteen voor de opening, en "De omslag" om 11:00.
- De top 3 stakeholders van 11:45 staat nu als invoer bij het supervisory board (12:15), bij Transformatieplan en draagvlak (dag 3) en bij werkplaats 3. Het blok van 11:45 noemt die drie plekken in plaats van "later". In werkplaats 3 speelt de AI de stakeholder met de meeste weerstand uit de top 3, niet meer die uit de online opdracht. Het draaiboek laat de trainer zeggen dat iedereen de top 3 bewaart.
- ADR-026 en ADR-028 zijn deels vervangen door ADR-030.

**Toegevoegd**
- Startsjabloon: v_Drucker en v_Wennink bij de strategen van het supervisory board. Drucker staat er voor "Wat is ons bedrijf, wie is de klant?", Wennink (oud-topman van ASML) voor de lange termijn en het ecosysteem. Bij de experts van het advisory board staat v_Deming, voor kwaliteit en het systeem, als harde scepticus. Daar staat ook v_Damodaran, voor het verhaal van een bedrijf vertaald in getallen: zijn toets is of een verhaal mogelijk, aannemelijk en waarschijnlijk is. Twee van zijn citaten komen uit zijn talk bij Google ("The Value of Stories in Business", 2017), de derde uit zijn blog over AI. Alle vier met gecontroleerde citaten volgens ADR-029. Damodaran werkt die blogpost (augustus 2026) nog bij: lees dat citaat vóór dag 2 nog één keer na. Het sjabloon biedt nu drieëntwintig helden (zeven vrouwen) en negentien experts.

**Verwijderd**
- Startsjabloon: v_Ardern staat niet meer bij de strategen van het supervisory board, en haar citaten zijn weg. De lijst in ADR-028 noemt haar nog; die legt de keuze van toen vast.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.18 — 2026-11-07

**Gewijzigd** (ADR-028)
- Startsjabloon `materiaal/boards.html`: twee strategen erbij in het supervisory board. v_Godin staat er voor verhalen die zich verspreiden, v_Sinek voor het waarom en het oneindige spel. Dat is een blik in het board, geen lesstof (ADR-026). Het sjabloon biedt nu tweeëntwintig helden.
- Startsjabloon: twee experts erbij in het advisory board. v_Woodward (Josh Woodward, Google Labs) staat er voor innovatie met snelle prototypes, v_Karpathy voor hoe taalmodellen werken en hun grillige intelligentie. Het sjabloon biedt nu zeventien experts.

**Toegevoegd** (ADR-029)
- Startsjabloon: elke kaart heeft "Wie is dit?" met twee echte citaten, hun bron en een link naar Wikipedia. Dat zijn 78 gecontroleerde citaten voor 39 personen. De citaten staan alleen op de pagina, niet in de skills.
- Startsjabloon: de typische vraag heet "Vraagt: …" en staat niet meer tussen aanhalingstekens, zodat hij niet als citaat leest.
- 6.3: de eerlijkheidsregels noemen de echte citaten op de kaarten.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.17 — 2026-11-07

**Gewijzigd** (ADR-028)
- Het supervisory board bestaat uit drie tot vijf strategen die de deelnemer zelf kiest, om inspiratie, met minstens één tegenspreker. Het bespreekt visie, missie en strategie, helpt het verhaal voor de stakeholders scherp te krijgen en komt tot een gezamenlijke conclusie en advies. De commissarissen vervallen.
- Het advisory board bestaat uit vijf tot zeven experts, elk met een eigen vakgebied, met minstens één harde scepticus.
- `materiaal/boards.html` is herschreven. Het supervisory board is stap 2, met twintig helden (acht vrouwen) en eigen helden. Het advisory board is stap 3, met vijftien experts (vijf vrouwen) en eigen experts. De lunchtaak staat bij stap 2.
- Dag 1: Stakeholders duurt van 11:45 tot 12:15. De lunchtaak gaat over de stukken van het bestuur in plaats van over de stakeholders. Werkplaats 1 begint met het advies van het supervisory board en bouwt het advisory board.
- FR-06, FR-17 en FR-19, deel 6.3, deel 9, de spanning "twee boards", de opdracht van werkplaats 1, de boardmomenten en twee risico's volgen de nieuwe rollen.
- Bouwstenen voor het draaiboek: het nieuwe blok om 12:15 en werkplaats 1.
- ADR-006 en ADR-027 zijn deels vervangen door ADR-028.

**Toegevoegd** (ADR-028)
- FR-32: vóór de lunch op dag 1 stelt elke deelnemer het supervisory board samen. Daarna legt de deelnemer het openbare stukken van het eigen bestuur over visie, missie en strategie voor. Het board komt tot een gezamenlijke conclusie en advies. AC-12 meet dat advies.
- Programma dag 1, 12:15–12:30: "Je supervisory board en de stukken van je bestuur".
- Boardmomenten: de lunch op dag 1.
- Risico: het bestuur zegt openbaar weinig, of de stukken zijn vertrouwelijk.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7. Versie 0.16 is niet apart gepubliceerd.

## 0.16 — 2026-11-07

**Toegevoegd** (ADR-027)
- `materiaal/boards.html`: het startsjabloon voor de twee boards als skill. De deelnemer vult de organisatie, de leden en de commissarissen in, ziet of de eisen kloppen en downloadt elk board als zip. Met een korte instructie voor Claude, ChatGPT en Gemini, een terugvaloptie en een werkwijze voor het boardmoment.
- Materiaal op de startpagina: het sjabloon bij werkplaats 1, en "Zo gebruik je je boards" bij de drie boardmomenten.
- Risico's: geen skills in de eigen omgeving, en een menu dat verandert.
- Bronnen: de helppagina's over skills van Anthropic, OpenAI en Google.
- Bouwstenen voor het draaiboek: voordoen en begeleiden in werkplaats 1.

**Gewijzigd** (ADR-027)
- FR-17: twee skills in het open SKILL.md-formaat, met een harde scepticus in elk board, in plaats van instructieteksten voor een project of Gem.
- 6.3, de KISS-keuze over twee boards, AC-12, de opdracht van werkplaats 1 en de opleverlijst van de trainer volgen FR-17.
- Fase 0: beide zips testen in de drie omgevingen en in een reserve-account.

## 0.15 — 2026-11-07

**Toegevoegd** (ADR-026)
- FR-30: tien minuten strategie aan het begin van "Van visie naar doelen" op dag 1. Het blok geeft de drie vaste definities van visie, missie en strategie. Daarna volgen twee filmpjes uit de tutorial "Van klassieke naar organische strategie", gecompliceerd tegenover complex, en de lus keuzes → dynamiek → opties → inzichten. Bij elk doel staat een signaal om het los te laten.
- FR-31: in de afsluiting van dag 3 schrijft elke deelnemer de missie in één zin, uit de drie ADR's van de boardmomenten. De zin komt bovenaan het deckonderdeel Conclusie.
- AC-20 meet het signaal bij elk doel en de missie.
- Materiaal bij dag 1, 11:00: de twee filmpjes en de tutorial.
- Bronnen: Mintzberg en Waters (1985), Werner en Le-Brun (2025) en de tutorial (ten Hove, 2026).

**Gewijzigd** (ADR-026)
- De KISS-keuze over modellen noemt de bril en de kosten ervan: tien minuten.
- 6.3: elk boardmoment is één ronde van de lus.
- Dag 2, "Zo bouwen AI-bedrijven": de voorbeelden laten de lus in het groot zien.
- Dag 3, buildplan: bij de fase opschaling de vraag "verspreiden of opleggen?".
- Dag 3, afsluiting: heet nu "missie, eigen rol en volgende stap" en dient SN2.
- Bouwstenen voor het draaiboek: de tien minuten strategie, de vraag over verspreiden en de missie.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.14 — 2026-11-07

**Gewijzigd** (ADR-025, na de [KISS-scan](onderzoek/2026-11-07-kiss-scan.md))
- Acceptatiecriteria: AC-03 gaat op in AC-02, AC-13 in AC-05 en AC-18 in AC-04. AC-04, AC-06, AC-07, AC-14 en AC-16 verwijzen naar de elementen van hun FR.
- NFR-04 gaat op in NFR-09. FR-12 gaat op in FR-18: de ADR van het boardmoment noemt de volgende stap voor het actieplan, en AC-12 meet die.
- Risico's van 23 naar 15: toegang, thuiswerk en boards elk samengevoegd tot één risico.
- KISS-keuzes van 18 naar 14 paren. De keuze over modellen telt al het gereedschap. De keuzes over fouten online zijn er nu één. Drie keuzes staan apart als "Spanningen".
- De vier kennisvormen gaan van dag 1 (FR-26) naar de PRD in werkplaats 2 (FR-20). Dit staat ook zo in het materiaal per blok en in de draaiboek-bouwstenen.
- Deel 10 voor de deelnemer komt uit het veld `deliverable` op de AC's. Het ritme in 6.2 komt uit `DATA.rhythm`.
- FR-21 noemt de verwachting bij de vraagstelling. "Businesscase op één pagina" is "hooguit twee pagina's", zoals in FR-14.

**Toegevoegd**
- Toetsrapport van de KISS-scan in `onderzoek/`, met per voorstel de keuze van de trainer.

**Verwijderd**
- FR-12, NFR-04, AC-03, AC-13 en AC-18, acht risico's en vier KISS-paren.
- De getypte lijsten met de opbouw van het verslag (6.4) en het ritme (6.2). Ook de dubbele beschrijving van een ADR in 6.3 en 6.4, en de takenlijst van de begeleider in 5.2.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7. Versie 0.12 en 0.13 zijn niet apart gepubliceerd.

## 0.13 — 2026-11-07

**Gewijzigd** (ADR-024)
- Deel 3 heet "Doelen": de zeven resultaten van S&N zijn de enige doelen, met per resultaat de lesdagen, berekend uit het programma.
- Alle eisen, programmablokken, werkplaatsen en deelnemerskaarten verwijzen met `sn` rechtstreeks naar de resultaten van S&N.
- De herleidbaarheid in deel 7 heeft drie kolommen (S&N, eis, acceptatiecriterium). De dekkingsregel toetst per resultaat een eis en een acceptatiecriterium.
- Deel 2 heeft drie kaders: Pink (2.1), Kolb (2.2) en COM-B (2.3).
- De koptekst telt de resultaten van S&N. Deel 1, deel 4, FR-11, AC-09, de opleverlijst van de trainer en twee KISS-keuzes zijn aangepast.
- Hersteld na de KISS-scan: de verwijzing naar axioma 2.4 in het programma van dag 3 is 2.3, en ADR-024 telt vijf programmablokken zonder resultaat. De laatste verwijzingen naar leeruitkomsten in de draaiboek-bouwstenen zijn omgezet.

**Toegevoegd**
- Een KISS-keuze: één laag doelen, in plaats van eigen leeruitkomsten tussen de resultaten van S&N en de eisen.

**Verwijderd**
- De leeruitkomsten LU1–9 (`DATA.lu`).
- De taxonomie van Bloom: kader 2.1, de matrix in deel 3, `bloomP` en `bloomK`, en de bron Anderson & Krathwohl (2001).
- De getypte verwijzingen naar leeruitkomsten tussen haakjes in 13 AC-teksten.

## 0.12 — 2026-11-07

**Toegevoegd** (ADR-023)
- FR-28: werkregel 1 vanaf de opening van dag 1: "Voordat je pauze neemt, zet je altijd AI aan het werk." Elke pauze heeft een AI-taak (`aiTask`) die het blok erna voorbereidt.
- FR-29 en AC-19: in het nabespreken van elke werkplaats kiest de groep een nieuwe werkregel. Na dag 3 telt het regelboek vier werkregels.
- `DATA.rules` en de kaart "Het regelboek" in deel 6.2. De AI-taak staat bij elke pauze in het detailpaneel van deel 8.
- Een KISS-keuze: vier werkregels die de groep zelf schrijft, in plaats van zes regels bij de start.
- Twee risico's: werkregel 1 blijft een grap, en de groep komt niet tot een werkregel.
- Startpagina: werkregel 1 met de AI-taak in de laatste vijf minuten vóór en tijdens elke pauze. De lijst toont de taak bij elke pauze.
- Draaiboek-bouwstenen: het regelboek voor alle dagen, met reserveregels uit de minor, en werkregels voor het eigen team bij cultuur op dag 3.

**Gewijzigd**
- FR-24 en AC-16: bij cultuur in het transformatieplan staan één of twee werkregels voor het eigen team.
- NFR-09: de startpagina toont werkregel 1 vóór elke pauze.
- Axioma 2.3 en 2.4, de PAMS-tabel, het nabespreken in 6.2, zes programmablokken, de opleverlijsten en fase 0.

## 0.11 — 2026-11-07

**Toegevoegd** (ADR-018 t/m ADR-022, uit de [hergebruiknotitie](onderzoek/2026-11-07-hergebruik-santeon-presentatie.md))
- FR-26: "Mens tegen agent" en de nieuwe inhoud van "Wat AI nu kan en niet kan" op dag 1.
- FR-27 en AC-18: een kansenkaart van de eigen procesketen vóór het onderzoek voor de businesscase.
- NFR-09: een startpagina per lesdag met tijdlijn en afteller, en alle lesmateriaal in `materiaal/`.
- Lesmateriaal: de voorbeeldcasus Voorbeeld BV, de startpagina, drie lespagina's (groeimodel, kennisvormen, kansenkaart), kritiekpunten voor de rolkaarten en bouwstenen voor het draaiboek.
- Bronnen: het onderzoek naar AI-volwassenheid en de kritiektrace in `background-docs/`, en acht nieuwe bronnen in APA 7.
- KISS-keuzes: de atlas blijft achtergrond; één voorbeeldcasus. Twee risico's: een voorbeeld uit een andere sector leidt af, en een lespagina laadt niet.
- Kader "Zelfstandigheid per fase" in deel 6.4. Veld `materials` per blok in het programma, met links in het detailpaneel.
- Gereedschap: `scripts/controleer-publicatie.py` (lekcheck), `scripts/excalidraw-huisstijl.py` en de skills `aiso-ste100-writer`, `aiso-taalredactie-publicatie` en `aiso-ontwerp-dia`.

**Gewijzigd**
- KISS-keuze over modellen: drie toevoegingen, met Ask → Assist → Automate (ADR-019). Zelftoets 5.2 en het risico "Te veel modellen" aangepast.
- FR-15 en AC-06: per fase een niveau van zelfstandigheid en een steekproef in de gate voor gebruik.
- FR-16 en AC-07: vijf governancevragen, met de vorm "Weet je …?" en een vuistregel voor toezicht (ADR-020).
- FR-06, FR-09, FR-20, FR-22, FR-24: scepticus met bewijs en tegenbewijs, kritiekpunten op de rolkaarten, eerst zelf scoren, regels als aanleiding, controle en handhaving, en wie het vak nog leert.
- Programma: details van negen blokken, de opleverlijsten en de fasen 0 en 2.
- Lekcheck: vindt nu ook links die in JavaScript staan (`href:` in `DATA`), zoals het materiaal per blok. Nieuw: `scripts/bouw-artifact.py` bouwt de kopie voor het artifact.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7. De links naar `materiaal/` zijn daar platte tekst, ook in het detailpaneel van het programma.

## 0.10 — 2026-11-07

**Gewijzigd** (ADR-017)
- Deelnemers heten Deelnemer A t/m F; de sleutel staat alleen in `temp/pseudoniemen.md`.
- Links naar inzendingen van afzonderlijke deelnemers vervangen door één link naar de map `temp/`.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.9 — 2026-11-07

**Verwijderd** (ADR-016)
- Werkgever, eigen bedrijf en herkenbaar werkdomein van deelnemers in deel 4 en in een risico. Ook uit de context van ADR-004.

**Toegevoegd**
- Privacyregel voor deelnemers in `CLAUDE.md` en in de skill `aiso-building-lrds`.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.8 — 2026-11-05

**Toegevoegd** (ADR-014, ADR-015)
- ADR's in `docs/adr/` en dit wijzigingslog voor de LRD; versienummer in de kop.
- Deelnemers houden een ADR-register en een wijzigingslog bij hun stack bij (FR-25, AC-17); vijfde sjabloon: ADR met wijzigingslog; kader in deel 6.4; bronnen Nygard (2011) en Keep a Changelog.
- KISS-keuze: het boardlog is het ADR-register.

**Gewijzigd**
- Het boardlog is vervangen door ADR's: FR-18, AC-12, de stroom in deel 6.3, de boardmomenten in het programma, de opleverlijst en een risico.
- FR-23: vijf sjablonen in plaats van vier. LU8: besluiten vastleggen in ADR's.

**Gepubliceerd** op dezelfde link: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7.

## 0.7 — 2026-11-05

**Gepubliceerd** als privé artifact: https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7 (ADR-013). De kop van de pagina toonde toen nog versie 0.1.

**Gewijzigd** (ADR-012, na de toets aan de AI-wiki)
- LU4, FR-14, FR-20: herontwerp van het werkproces in businesscase en PRD; uitkomstmaat; verloop van kosten en baten.
- LU5, FR-15, AC-06: elke gate toetst werking, integratie en gebruik; senior sponsor uit de business.
- FR-20, AC-04, AC-15: elke norm heeft een referentiewaarde zonder AI; voorbeeldnormen aangepast.

**Toegevoegd**
- Risico 'pilot purgatory'. Bronnen Dutt et al. (2026) en Brynjolfsson et al. (2021). Link naar het toetsrapport.
- Titel 'LRD AISO26009 Lesdagen'.

## 0.6 — 2026-11-04

**Toegevoegd** (ADR-011)
- De zeven resultaten van S&N (SN1–SN7) met dekkingstabel en als eerste kolom in het herleidbaarheidsdiagram.
- FR-24 (transformatieplan met 7S), AC-16.

**Gewijzigd**
- LU7 verbreed tot transformatieplan en draagvlak; dag 3 begint met 'Transformatieplan en draagvlak'.
- 'Cursuspagina' heet nu 'webpagina van de training'.

**Verwijderd**
- Open punt en risico over ontbrekende leeruitkomsten van S&N.

## 0.5 — 2026-11-04

**Toegevoegd** (ADR-007, ADR-009, ADR-010)
- Deel 6.4 'De bouwstraat': businesscase, PRD, experiment, blueprint, buildplan; voorbeelden van AI-bedrijven; experimentvormen.
- LU9, FR-20 t/m FR-23, AC-14, AC-15, risico's over verzonnen bronnen, thuiswerk, meetbaarheid, technisch project en workshop-agenda.

**Gewijzigd**
- Werkplaats 2 wordt 'PRD en experiment'; FR-14, FR-15 en het roadmapblok op dag 3 ('Van experiment naar buildplan').
- Experimentverslag: eerst kort paper (ADR-008), daarna interactieve webpagina (ADR-009).
- Detailpanelen bij de Bloom-matrix en het herleidbaarheidsdiagram blijven in beeld.

## 0.4 — 2026-11-04

**Toegevoegd** (ADR-006)
- Deel 6.3 'De boards', FR-17 t/m FR-19, AC-12, AC-13, boardmomenten in het programma, drie risico's.

**Gewijzigd**
- Werkplaats 1 wordt 'Bouw je boards'; LU8 omvat het toetsen van eigen besluiten; deckblokken 45/45/30 minuten.

## 0.3 — 2026-11-04

**Gewijzigd** (ADR-004, ADR-005)
- AI-omgeving: eerst Gemini voor iedereen, daarna eigen frontieraccount met Gemini als reserve. NFR-01 t/m NFR-03, AC-10, KISS-keuze, twee risico's.

## 0.2 — 2026-11-04

**Gewijzigd** (ADR-003)
- De LRD is een interactieve HTML-pagina in de huisstijl van Business Data Solutions, met één databron, D3, Three.js en Motion. De Markdown-versie is vervangen.
- FR-03: duur van het deckblok op dag 3 gecorrigeerd.

## 0.1 — 2026-11-04

**Eerste concept** (ADR-001, ADR-002), als Markdown.
- Scope: de drie lesdagen. Kernmechanisme: eigen casus met casusdeck en AI-werkplaats.
- Leeruitkomsten LU1 t/m LU8, FR-01 t/m FR-16, NFR-01 t/m NFR-08, AC-01 t/m AC-11, programma, risico's en roadmap.
