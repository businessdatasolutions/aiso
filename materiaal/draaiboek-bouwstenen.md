# Bouwstenen voor het draaiboek

- **Status:** concept (ADR-018). Dit zijn bouwstenen voor het draaiboek per lesdag (NFR-07), nog geen draaiboek.
- **Herkomst:** de sessie "AI en kwaliteitsmanagement in de zorg" van 10 november 2026, algemeen gemaakt met de voorbeeldcasus Voorbeeld BV (`materiaal/voorbeeldcasus.md`). Zie `onderzoek/2026-11-07-hergebruik-santeon-presentatie.md`.
- **Bronnen:** `background-docs/2026-11-07-volwassen-ai-blijft-zeldzaam.md` (het volwassenheidsrapport) en `background-docs/2026-11-06-kritiek-op-ai-inzet-query-trace.md` (de kritiektrace, met codes als [B2]). De literatuur staat in de LRD onder Bronnen.
- **Regel:** kies per blok hooguit één of twee punten om echt te zeggen. De rest is reserve voor vragen.

## Alle dagen · Het regelboek (FR-28, FR-29)

**Herkomst.** Het regelboek komt uit de minor AI in Business van de trainer (ADR-023). Daar groeide het per week. Hier groeit het per lesdag, tot vier werkregels.

### Opening dag 1: werkregel 1 (3 minuten)

1. Toon het lege regelboek met vier plekken, op een flap of dia. Alleen werkregel 1 is ingevuld.
2. Lees voor: "Voordat je pauze neemt, zet je **altijd** AI aan het werk."
3. Zeg waarom: een onderzoek met de onderzoeksfunctie van je AI duurt tien tot twintig minuten. Dat is precies een pauze. Wie de AI vóór de pauze een taak geeft, heeft na de pauze iets om mee verder te werken.
4. Doe het zelf voor bij de pauze van 10:45. Geef je eigen AI de taak van de startpagina, en laat na de pauze zien wat eruit kwam.

### Vóór en na elke pauze

- De startpagina toont werkregel 1 vijf minuten vóór elke pauze, met een idee voor een AI-taak die het blok erna voorbereidt. De taken staan in de LRD, bij de pauzes in het programma (veld `aiTask`). Zo staan ze op één plek.
- Zeg de werkregel hardop bij de eerste twee pauzes. Daarna doet de startpagina het.
- Na de pauze: "Wat heeft je AI gemaakt?" Eén voorbeeld is genoeg. Een taak die mislukte, is stof voor het nabespreken (vraag 2).
- Ook in de pauze werkt de AI alleen met openbare of verzonnen gegevens (NFR-01).

### Laatste vijf minuten van het nabespreken: een nieuwe werkregel

1. Bij de derde vaste vraag ("Wat vraagt dit van mijn organisatie?") schrijft elk duo één werkregel op: één korte zin over gedrag.
2. Elk duo leest de eigen werkregel voor, zonder discussie.
3. Iedereen heeft één stem, niet voor de werkregel van het eigen duo. De meeste stemmen winnen. Staken de stemmen, dan beslist de trainer.
4. Schrijf de werkregel in het regelboek en maak één woord vet. Zet de tekst na de lesdag in de LRD (`rules`). Dan staat hij ook in deel 6.2 en op de startpagina.

**Een goede werkregel** beschrijft een handeling, past in één zin, en is te zien in het werk. "Wees kritisch op AI" is te vaag: wat doe je dan? "Zoek elke bron op voordat je hem doorstuurt" is een werkregel.

**Reserve.** Komt de groep er niet uit, bied dan een werkregel uit het regelboek van de minor aan. Kies er een die past bij wat de groep die dag deed.

| Werkregel | Past bij |
|---|---|
| Doe iets **geks**. | Werkplaats 1: een board met een onverwacht lid |
| **Leren** gaat boven resultaat. | Werkplaats 2: ook een mislukt experiment levert iets op |
| Technologie is **niet** de drempel. | Werkplaats 3: weerstand gaat zelden over techniek |
| Maak het probleem van **een ander** nooit het jouwe. | Governance: wie is eigenaar? |
| Het is **nooit** af. | ADR's en wijzigingslog: elk besluit kan een nieuwe ADR krijgen |

### Afsluiting dag 3

Toon het regelboek met de vier werkregels van de groep: "De werkregels die we houden, dag na dag."

## Dag 1 · Wat AI nu kan en niet kan (FR-26)

### Werkvorm "Mens tegen agent" (5 minuten, aan het begin van het blok)

1. Toon klacht K-0505 uit de voorbeeldcasus. Lees de twee feiten voor: wat de klant schrijft en wat het planningssysteem zegt.
2. Vraag: "Welke urgentie geef jij deze klacht, 1 tot en met 4?" Laat iedereen tegelijk 1 tot 4 vingers opsteken.
3. Benoem wat je ziet. De groep is het meestal oneens.
4. Toon wat de agent doet. De agent escaleert de klacht en geeft geen urgentie. De reden: de klant en het systeem spreken elkaar tegen, en er woont een kwetsbare bewoner.
5. Zeg: "Bij twijfel is escaleren het goede antwoord, ook voor AI."
6. Zeg wat dit oplevert voor werkplaats 2: "Je eigen score is de referentiewaarde. Eerst scoor jij, daarna de AI" (FR-20).

**Live variant:** geef je eigen AI-model de klacht en de urgentieregels uit de voorbeeldcasus. Kijkt het model of het escaleert? Gokt het model een score, dan is dat zelf een les.

**Waarom eerst zelf:** wie eerst het AI-antwoord ziet, neemt het over. Wie eerst zelf scoort, ziet het verschil.

### Punten voor het blok

- **Gebruik is breed, volwassen inzet is zeldzaam.** In enquêtes onder bestuurders gebruikt 78–88% AI. Volgens het CBS gebruikt 33% van de Nederlandse bedrijven met tien of meer werkzame personen AI (2025, voorlopig). Metingen met een strenge lat komen uit op 5 tot 13%: BCG 7,5% (2026), McKinsey 6% (2025 en 2026), Gartner 13% (2026). Noem bij elk cijfer wat er gemeten is en in welk jaar. Het getal beweegt mee met de lat. (Volwassenheidsrapport.)
- **De grillige grens (jagged frontier).** Binnen de grens van wat AI goed kan, maakten consultants 12% meer taken af, werkten ze 25% sneller en was de kwaliteit 34% hoger. Buiten die grens scoorden ze 19 procentpunt slechter, en hun foute adviezen klonken juist overtuigender (Dell'Acqua e.a., 2026; [B2]).
- **Gevoel is geen meting.** Ervaren ontwikkelaars werkten in een gerandomiseerde studie met AI 19% trager. Zelf dachten ze dat ze 20% sneller waren (Becker e.a., 2025). Daarom meet je in het experiment, en vertrouw je niet op indruk.
- **Vier faalwijzen van een agent, en wat ze opvangt.**
  1. Een antwoord zonder grond → verankering: elke uitspraak heeft een citaat uit de bron.
  2. Een ontbrekend feit → doorvragen in plaats van invullen (K-0501).
  3. Tegenstrijdige feiten → escaleren naar een mens (K-0505).
  4. Het eigen huiswerk nakijken → een tweede, aparte controle.
- **Een agent is opgebouwd als een organisatie.** Toon als voorbeeld uit een andere sector de publieke pagina https://businessdatasolutions.github.io/santeon-presentatie/harness.html. Zeg erbij dat het voorbeeld uit een ziekenhuis komt. De kern: het taalmodel is de professional, de harness (de besturing rond het model) is het kwaliteitssysteem, het contextvenster is het dossier op tafel. Het model huur je, de harness bouw je zelf.

### Nederlandse uitleg bij Engelse termen (NFR-08)

| Term | Uitleg |
|---|---|
| Agent | Een systeem dat een taalmodel gebruikt om een taak in stappen uit te voeren, binnen vaste grenzen. |
| Harness | Alles rond het model: welke informatie het krijgt, welke hulpmiddelen het mag gebruiken, en wat er gebeurt bij een fout. |
| Contextvenster | Wat het model op dit moment leest. |
| Jagged frontier | De grillige grens tussen taken die AI goed kan en taken waarbij AI fouten maakt. |

## Dag 1 · Van visie naar doelen

### Tien minuten strategie (FR-30)

**Herkomst.** De tutorial "Van klassieke naar organische strategie" van de trainer (ten Hove, 2026): https://businessdatasolutions.github.io/emergent-strategy-tutorial/. Download de twee filmpjes vooraf, zodat ze ook zonder internet werken.

1. **Het klassieke pad.** Toon het eerste filmpje (10 seconden): vandaag → een boog → de visie over vijf jaar, met de missie als stip. Geef de drie definities:
   - **Visie:** hoe de wereld eruitziet in de toekomst. Een beeld van de veranderende omgeving waarin je organisatie zal opereren.
   - **Missie:** welke plek je ziet voor de organisatie in die toekomstige wereld. De rol en positie die je wilt innemen.
   - **Strategie:** welk pad je gaat volgen richting die nieuwe positie. De keuzes en stappen om van nu naar je gewenste plek te komen.
2. **Waarom dat bij AI vastloopt.** Een straalmotor is gecompliceerd: duizenden onderdelen, maar voorspelbaar. De oceaan is complex: een kleine verandering heeft onvoorspelbare gevolgen. AI hoort bij de oceaan; dat zagen de deelnemers om 10:00 aan de grillige grens. Wie één stip kiest en ernaartoe blijft lopen, loopt een groot risico dat het de verkeerde stip is.
3. **Het organische pad.** Toon het tweede filmpje (25 seconden): korte stappen naar de "ware toekomst". De missie verschijnt pas onderweg. Mintzberg noemt dit emergente strategie: strategie die ontstaat uit wat je doet (Mintzberg & Waters, 1985).
4. **De lus.** Keuzes → dynamiek → opties → inzichten. Zeg: "Elk boardmoment is één ronde. Een missie schrijven we vandaag niet; die zie je op dag 3."
5. **Aanhaken.** In de Eerste blik online lazen ze het advies van Reid Hoffman: herzie de AI-strategie elke week. Vraag wat ze daar toen van vonden.

- **Signaal om los te laten.** Vraag bij elk van de 2–4 doelen: "Wat zou er moeten gebeuren om dit doel los te laten?" Dat signaal staat bij het doel in het deck (AC-20).
- **Risicobereidheid.** Besturen bespreken hun risicobereidheid zelden. Die verschilt per persoon, en dat blijft onuitgesproken (Linda Hill, in Bloomberg Podcasts, 2026). Vraag in de duo's: "Hoeveel risico wil jullie directie nemen met AI, en wie heeft dat ooit hardop gezegd?" Het antwoord hoort in de visie, bij de rol van de mens (SN2).

## Dag 1 · Stakeholders

- Vraag bij elke stakeholder met weerstand: "Wat verliest deze persoon?" Op dag 3 komt dit terug in de vier vragen bij weerstand.

## Dag 2 · Investeringscomité (FR-09)

- Deel de rolkaarten uit. Elke rolkaart heeft twee kritiekpunten met bewijs en tegenbewijs: `materiaal/rolkaarten-kritiekpunten.md`.
- Zeg vooraf: "De cijfers op de kaart zijn vaak zelfrapportage of van leveranciers. Vraag dus ook: wat is er gemeten?"

## Dag 2 · Zo bouwen AI-bedrijven

- **De productiviteitsparadox.** Op taakniveau meten studies +14 tot +73%, op bedrijfsniveau ongeveer 0%. 90% van de bedrijven investeert, minder dan 40% ziet meetbare winst [D5]. Dit sluit aan op de J-curve: eerst een dal, dan de winst (Brynjolfsson e.a., 2021).

## Dag 2 · Businesscase met AI-onderzoek (FR-14, FR-27)

1. **Voordoen met de kansenkaart (10 minuten).** Toon `materiaal/kansenkaart.html`, stap 1 tot en met 8: het proces van Voorbeeld BV, de vier routes, en de vijf plekken waar AI kan helpen.
2. **Zelf doen (10 minuten).** Toon stap 9, "Jouw proces". Elke deelnemer tekent de eigen procesketen op papier: rollen als banen, fasen als kolommen, een cijfer waar AI kan helpen, en bij elk cijfer wie beslist. Daarna de vraag uit FR-14: waar schuift het knelpunt heen als AI het oplost?
3. **Bronkritiek, met een echt voorbeeld.** Het vaak geciteerde "95% van de organisaties haalt geen rendement uit AI" komt van MIT NANDA (2025). Het rust op ruim 300 openbare initiatieven, 52 interviews en een enquête onder 153 bezoekers van vier conferenties. Het rapport noemt de eigen cijfers "directionally accurate". Vraag: wat is er gemeten, bij wie en wanneer? Dezelfde vraag stelt het duo bij de bron die het in het origineel opzoekt (AC-04).

## Dag 2 · Werkplaats 2: PRD en experiment (FR-20)

- **Referentiewaarde.** Doen mensen de taak nu al? Laat de deelnemer dan eerst zelf vijf tot tien gevallen scoren of afhandelen. Pas daarna doet de AI hetzelfde. Zo ontstaat de referentiewaarde zonder AI (AC-15).
- **Kennisvorm (FR-20).** Welke kennis heeft de use case nodig, en wie houdt die bij? Toon `materiaal/kennisvormen.html`. De boodschap: geen vorm wint altijd. Kies per vraag de eenvoudigste vorm die werkt. De laatste stap van de pagina helpt de deelnemer kiezen. Uitleg bij de termen (NFR-08): bij **RAG** zoekt het systeem passende documenten en zet die bij de vraag; een **kennisgraaf** legt begrippen en hun relaties vooraf vast; een **LLM-wiki** bewaart kennis als kaarten met bron en datum, door mensen bijgehouden.
- **Experiment met een agent.** De vier faalwijzen van dag 1 zijn kant-en-klare evaluatiecriteria. Bijvoorbeeld: elke uitspraak heeft een citaat; bij een ontbrekend feit vraagt de agent door; bij tegenstrijdigheid escaleert hij.

## Dag 3 · Transformatieplan en draagvlak (FR-24)

### Vier vragen bij weerstand

Gebruik ze bij het onderdeel "per stakeholder één actie van weerstand naar draagvlak", en in het nabespreken van werkplaats 3.

1. Zie de weerstand als signaal, niet als probleem.
2. Vraag door: wat is de weerstand precies?
3. Zoek de oorzaak. Gaat het om verlies, om onzekerheid, om verlies van controle, of om een terechte zwakke plek in de verandering?
4. Los het niet meteen op.

**Drie valkuilen voor wie leiding geeft:** de weerstand persoonlijk maken, erover moraliseren, en te snel een oplossing willen. Bron: Carucci (2026). Breng dit als vier vragen, niet als nieuw model (KISS-keuze in deel 5.1 van de LRD).

### Cultuur: werkregels voor het eigen team

- Vraag: "Welke werkregel uit ons regelboek zou in jouw team werken? En welke werkregel heeft jouw team nodig die wij nog niet hebben?"
- Elke deelnemer schrijft één of twee werkregels bij cultuur in het 7S-plan (FR-24, AC-16). Een werkregel voor een team gaat over hoe het team met AI werkt: de gedeelde waarden en de stijl uit 7S.

### Vaardigheden en mensen

- **Wie leert het vak nog?** Doet de AI altijd het eerste werk, dan bouwen nieuwe medewerkers het vak minder goed op. Junior juristen maakten na ongeveer 90 dagen veel meer fouten toen de AI wegviel (tweedehands gemeld). Geen bron meet het verlies direct [B1]. Tegenmaatregel: nieuwe medewerkers doen de eerste gevallen zelf. Dit hoort in het 7S-onderdeel vaardigheden en mensen.

## Dag 3 · Van experiment naar buildplan (FR-15, FR-22)

- **Zelfstandigheid per fase.** Toon `materiaal/groeimodel.html`. Elke fase in het buildplan krijgt een niveau: Ask, Assist of Automate, met wie beslist. Het experiment draait op Ask. Automate komt alleen in beeld voor duidelijke gevallen met een laag risico, en altijd met een harde grens.
- **Afstempelen.** Na een reeks goede voorstellen wordt menselijke controle ongemerkt een stempel. Na ongeveer honderd goedkeuringen leest niemand ze meer [B3]. Tegenmaatregel in de test gate: laat een steekproef eerst door een mens scoren, en vergelijk pas daarna met de AI.
- **Geen eigenaar, geen agent.** Wie is verantwoordelijk voor het resultaat? Zonder eigenaar blijft het een demo. Dat is de senior sponsor uit FR-15.
- **Verspreiden of opleggen (Werner & Le-Brun, 2025).** Na een paar geslaagde experimenten is de reflex: "Hoe schalen we dit op?" Dat wordt meestal een opdracht van bovenaf om één werkwijze overal in te voeren. Dan verdwijnt het eigenaarschap, en wie niet aan het experiment meedeed, voert alleen nog uit. Octopusorganisaties laten een werkwijze die werkt zich verspreiden: een ander team neemt hem over en past hem aan. Vraag bij de fase opschaling: "Welk team neemt dit als eerste over, en waarom zou het dat willen?"
- **Regels voor wat de AI mag doen (blueprint).** Schrijf ze als aanleiding → controle → handhaving: "Als X gebeurt, controleer Y. Doe dan Z: ga door, pauzeer voor een mens, of stop" (Wang e.a., 2026).

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
4. Vraag: "Wie vraag je morgen?" Iedereen noemt een functie, nooit een naam. Die vraag kan de volgende stap worden: de deelnemer zet hem in de gevolgen van de ADR bij het boardmoment van 15:45 (FR-18), en van daaruit in het actieplan.
5. Daarna beantwoordt elke deelnemer de vijf vragen voor de eigen use case (AC-07).

### Hulpmiddelen bij vraag 4 en 5

- **Vuistregel voor toezicht (Böckeler, in InfoQ, 2026).** Toezicht = kans op een fout × impact van de fout × hoe moeilijk de fout te zien is. Een hoge score op de laatste factor betekent: de fout valt niet op. Hoe hoger de uitkomst, hoe dichter de mens bij het besluit staat.
- **Twee eisen aan elke uitkomst van AI.** Elke uitspraak is te herleiden naar de bron, met een citaat. Bij twijfel of tegenstrijdigheid escaleert het systeem; het gokt niet.
- **Onomkeerbaar en zichtbaar.** Mensen willen vooral een controle bij handelingen die onomkeerbaar én zichtbaar voor anderen zijn, zoals een bericht aan klanten (Pochampally e.a., 2026; kleine studie onder 20 studenten). Laat zo'n handeling eerst langs een mens gaan, ook op niveau Automate.
- **Wie pakt een escalatie op?** In een experiment werd een bedrijf geleid door AI-agenten. Op dag 19 waarschuwde de AI dat het bedrijf de verkeerde kant op ging. Niemand deed er iets mee. Leg dus vast wie een escalatie oppakt.
- **Vraag 5 en de OR.** Kijkt de AI naar prestaties of gedrag van medewerkers? Dan vraagt dat meestal instemming van de OR, en kan de toepassing in de AI-verordening onder hoog risico vallen (bijlage III, werkgelegenheid). Laat een jurist dit per use case toetsen.

## Dag 3 · Werkplaats 3: AI als scepticus

- Geef de AI de kritiektrace als bron voor de scepticus, of het deel dat bij de use case past. Vraag de scepticus om bewijs én tegenbewijs. Een scepticus zonder tegenbewijs is een tegenstander, geen toets.
- Nabespreken: welke van de vier soorten weerstand speelde de AI? Verlies, onzekerheid, verlies van controle, of een terechte zwakke plek?

## Dag 3 · Afsluiting: de missie (FR-31)

- Toon het tweede filmpje nog één keer (25 seconden): "Dit is het pad dat je in drie dagen liep."
- Laat iedereen de drie ADR's van de boardmomenten naast elkaar leggen. Vraag: "Welke plek zie je nu voor je organisatie in de wereld uit je visie?" Eén zin, met de ADR waaruit die volgt. De zin komt bovenaan het deckonderdeel Conclusie (AC-20).
- Zeg erbij: deze missie is de stand van nu. De volgende rondes van de lus kunnen hem nog veranderen.

## Achtergrond en reserve voor de trainer

- **De atlas met raamwerken** (Engelstalig): `~/Projects/presentatie-santeon-10-11-2026/background-material/2026-07-01-ai-maturity-frameworks-visuals.html`. Lokaal openen; de pagina laadt zijn bibliotheken uit een eigen map. Gebruik hem bij vragen, niet als lesstof (KISS-keuze in 5.1). De cijfers in sectie 0 zijn verouderd; gebruik het volwassenheidsrapport. De hergebruiknotitie (`onderzoek/2026-11-07-hergebruik-santeon-presentatie.md`, onderdeel 15) zegt per raamwerk bij welk blok het past. Twee kandidaten voor later: de 2×2 van Anand en Wu ("op welke taak richt je AI eerst?") bij de prioriteiten van de roadmap (SN3), en de ladder L0–L5 voor de eigen rol bij de boardmomenten (FR-18).
- **Het prototype van een agent, uit de zorg.** Een demo met doorvragen, controle, een tweede AI als beoordelaar en een terugval op trefwoorden. De publieke versie draait zonder live AI: https://businessdatasolutions.github.io/santeon-presentatie/demo.html. Een animatie zonder netwerk: https://businessdatasolutions.github.io/santeon-presentatie/vim-agent-animatie.html. Alleen als reserve bij vragen over FR-15 ("een artefact dat een tester kan proberen") of over een technische test (FR-21). Zeg erbij dat het voorbeeld uit een ziekenhuis komt.

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
