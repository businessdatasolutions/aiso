# Hergebruik uit de Santeon-presentatie

- **Datum:** 7 november 2026
- **Bekeken:** `~/Projects/presentatie-santeon-10-11-2026/`. Dat is het materiaal voor de sessie "AI en kwaliteitsmanagement in de zorg" op 10 november 2026. De sessie duurt 90 minuten en is plenair, voor ruim 60 kwaliteitsadviseurs van ziekenhuizen.
- **Vraag:** welke onderdelen kunnen we hergebruiken in de drie lesdagen van AISO26009, en waar passen ze?
- **Getoetst aan:** de LRD, versie 0.9 (leeruitkomsten, programma, eisen, KISS-keuzes en risico's).
- **Niet geopend:** de offerte, de pitchmail, de notities van 22 juni en `.env` in de Santeon-repo. Die zijn vertrouwelijk en horen niet in ons materiaal.
- **Stand:** het voorstel is overgenomen in versie 0.11 van de LRD (ADR-018 t/m ADR-022). Onderdeel 14 (prototype) blijft reserve en onderdeel 15 (atlas) achtergrond, zoals hieronder voorgesteld.

## Conclusie

Er is veel bruikbaar materiaal. Het past vooral op drie plekken. Dat zijn "Wat AI nu kan en niet kan" op dag 1 (LU1), het governanceblok op dag 3 (LU6) en de werkplaats "AI als scepticus" (LU7). De meeste waarde zit in bronnen en werkvormen. Drie springen eruit:

- een onderzoek naar AI-volwassenheid met cijfers tot en met 2026;
- een overzicht van 24 kritiekpunten op AI, met bewijs voor en tegen;
- de werkvorm "eerst zelf scoren, dan de AI".

De visualisaties volgen dezelfde huisstijl als de LRD en zijn dus snel over te zetten. Ze gaan wel over incidentmeldingen in een ziekenhuis, dus ze hebben een algemene casus nodig.

Eén grens bepaalt de selectie. De KISS-keuze in deel 5.1 van de LRD staat geen nieuwe modellen toe naast de vijf uit de online omgeving. Dat zijn Mendelow, Kotter, COM-B, ADKAR en McKinsey 7S. Er zijn twee uitzonderingen: de risicoklassen van de AI-verordening en de businesscase op één pagina. Een deel van het Santeon-materiaal is een model, zoals Ask → Assist → Automate en de raamwerken uit de atlas. Die onderdelen hebben hieronder het label "besluit nodig".

## Labels

| Label | Betekenis |
|---|---|
| **Overnemen** | Past zonder nieuw model en vraagt weinig werk. |
| **Aanpassen** | Past, maar de zorgcasus moet eruit of de code moet om. |
| **Besluit nodig** | Voegt een model toe. Dat botst met de KISS-keuze, dus eerst een ADR. |
| **Achtergrond** | Voor de trainer: draaiboek, voorbereide antwoorden, reserve. |
| **Niet** | Niet hergebruiken. |

## Overzicht

| # | Onderdeel | Waar in ons programma | Raakt | Label |
|---|---|---|---|---|
| 1 | Onderzoek "Volwassen AI blijft zeldzaam" | Dag 1, Wat AI nu kan en niet kan; dag 2, Businesscase met AI-onderzoek | SN1, LU1, LU4, AC-04 | Overnemen |
| 2 | Kritiek op AI-inzet: 24 punten met bewijs | Werkplaats 3; rolkaarten van het investeringscomité; scepticus in het advisory board | SN7, LU7, FR-09, FR-17 | Overnemen |
| 3 | Bronnen over betrouwbaarheid en toezicht | Dag 1; dag 3, governance en transformatieplan | LU1, LU2, LU6, LU7, FR-16, FR-24 | Overnemen |
| 4 | Vuistregel van Böckeler voor toezicht | Dag 3, governance, vraag 4 van FR-16 | LU6, FR-16 | Overnemen |
| 5 | Werkvorm "Mens tegen agent" | Dag 1, Wat AI nu kan; werkplaats 2, referentiewaarde | LU1, LU9, FR-20, AC-15 | Overnemen |
| 6 | "Veilig voor wie?" en de vraag "Weet je …?" | Dag 3, governance; afsluiting | LU6, FR-16, FR-12 | Aanpassen |
| 7 | Voorbereide antwoorden op lastige vragen | Draaiboek; governance; comité | NFR-07, NFR-01, FR-16 | Achtergrond |
| 8 | Facilitatie bij weerstand (Carucci) | Dag 3, transformatieplan en draagvlak; werkplaats 3 | SN7, LU7 | Aanpassen; besluit nodig voor het model |
| 9 | Vier kennisvormen naast elkaar (`harness.html`, deel 2) | Dag 1, wat AI vraagt van data; werkplaats 2, PRD | LU1, LU3, FR-20 | Aanpassen |
| 10 | Agent, computer en organisatie als één bouwplaat (`harness.html`, deel 1) | Dag 1 | LU1 | Aanpassen |
| 11 | Vier faalwijzen van een agent (`architectuur.html`) | Dag 1; werkplaats 2, evaluatiecriteria | LU1, LU9, FR-20 | Overnemen als lijst |
| 12 | Ask → Assist → Automate (`groeimodel.html`, `groeipad.html`) | Dag 3, buildplan en governance | SN3, LU5, LU6, FR-15, FR-16 | Besluit nodig |
| 13 | Kansenkaart als swimlane (`vim-swimlane.html`) | Dag 2, procesketen in de businesscase | LU3, LU4, FR-14, FR-20 | Aanpassen |
| 14 | Prototype en animatie van een triage-agent | Dag 1, demonstratie; voorbeeld bij technische test en artefact | LU1, LU9, FR-15 | Achtergrond; tonen zoals het is |
| 15 | Atlas met dertien raamwerken | Achtergrond voor de trainer | SN2 t/m SN7 | Achtergrond; besluit nodig per raamwerk |
| 16 | Startpagina met tijdlijn (`index.html`) | Elke lesdag op het scherm | NFR-04, NFR-06, NFR-07 | Aanpassen |
| 17 | Excalidraw naar SVG in de huisstijl | Alle schema's van de lesdagen | — | Overnemen |
| 18 | Lekcheck vóór publicatie | Publicatie van de LRD als artifact | ADR-013, ADR-016 | Aanpassen |
| 19 | Projectskills voor STE100, taalredactie en dia's | Dia's, handouts en draaiboek | NFR-07, NFR-08 | Aanpassen |
| 20 | Stemtool met QR-code (`meedoen.html`) | — | NFR-05 | Niet |
| 21 | Ziekenhuismaquette, AI Monitor Ziekenhuizen en VIM-bronnen | — | — | Niet |

De publieke versie van alle pagina's staat op https://businessdatasolutions.github.io/santeon-presentatie/. Die versie werkt zonder live AI. Wil je een pagina alleen tonen als voorbeeld uit een andere sector? Dan hoef je niets te bouwen.

## Toelichting

### Inhoud en bronnen

**1. Onderzoek "Volwassen AI blijft zeldzaam"** · Overnemen
`reports/Nieuwe onderzoeken naar AI volwassenheid.md`, met de notities in `research_notes/`.

- **Wat het is.** Een onderzoek van 7 november 2026 naar nieuwe metingen van AI-volwassenheid. Bijna elke organisatie gebruikt AI. In enquêtes onder bestuurders is dat 78–88%. Volgens het CBS gebruikt 33% van de Nederlandse bedrijven met tien of meer werkzame personen AI (2025, voorlopig). Weinig organisaties halen er op grote schaal waarde uit. Instrumenten met een strenge definitie komen uit op 5 tot 13%: BCG 7,5%, McKinsey 6%, Accenture 8%, PwC 12%, Gartner 13%. Een NBER-studie onder bijna 9.000 bestuurders meet 0,2% extra groei van de arbeidsproductiviteit per jaar. De conclusie: het getal beweegt mee met de lat.
- **Waar het past.** Dag 1, "Wat AI nu kan en niet kan" (LU1, SN1): realistische verwachtingen. Elk cijfer noemt zijn eigen definitie en jaartal. Dag 2, "Businesscase met AI-onderzoek" (LU4, AC-04): het rapport laat zien hoe je een cijfer naar de bron terugvolgt. Het vond drie fouten in de wiki. Ook het vaak geciteerde "95% haalt geen rendement" (MIT NANDA) rust op een enquête onder 153 bezoekers van vier conferenties. Dat past bij het risico "De AI verzint bronnen of citaten". Het past ook bij de eis dat het duo één bron in het origineel opzoekt.
- **Wat je aanpast.** De paragraaf over ziekenhuizen en de slotalinea over kwaliteitsadviseurs gaan eruit. De tabel met drie groepen (streng, midden, ruim) kan zo mee.

**2. Kritiek op AI-inzet** · Overnemen
`background-material/2026-11-06-kritiek-op-ai-inzet-query-trace.md`

- **Wat het is.** Een trace uit de ai-wiki met 24 kritiekpunten in vier groepen. Input: energie, trainingsdata, synthetische data, privacy. Gebruik: vaardigheden slijten, te veel vertrouwen, toezicht verwatert, verborgen gebruik, agents als collega's, inzet die averechts werkt. Output: hallucinaties, grillige betrouwbaarheid, onveilige code, benchmarks, ketens van agents, bias, misbruik. Effecten op maatschappij en economie: banen, instapbanen, AI-washing, de productiviteitsparadox, een bubbel, machtsconcentratie. Elk punt heeft bewijs voor, tegenbewijs en genoemde oplossingen. Onderaan staat wat de wiki niet dekt, en een factcheck van Nederlandse cijfers over datacenters.
- **Waar het past.**
  - Werkplaats 3, "AI als scepticus" (LU7, SN7). De scepticus krijgt argumenten met bronnen. De deelnemer oefent met het tegenbewijs.
  - De rolkaarten van het investeringscomité (FR-09). De financieel directeur krijgt de productiviteitsparadox en de "verificatietax" (bespaarde tijd min controletijd). De privacy- of securityfunctionaris krijgt privacy en verborgen gebruik: bij een verbod uploadt 67% gevoelige data, zonder beleid 33%. Het OR-lid krijgt slijtende vaardigheden, minder gevoelde verantwoordelijkheid en verdwijnende instapbanen. De eindgebruiker krijgt de inzet die averechts werkt: niet-afgestemde AI deed het slechter dan het oude systeem.
  - De harde scepticus in het advisory board (FR-17) kan de lijst als kennisbron krijgen.
  - Dag 2, "Zo bouwen AI-bedrijven": de productiviteitsparadox sluit aan op de J-curve van Brynjolfsson die de LRD al gebruikt.
- **Wat je aanpast.** Inhoudelijk niets. Neem de kanttekeningen van de trace mee: veel cijfers zijn zelfrapportage, komen van leveranciers of komen tweedehands binnen. Dat maakt de oefening juist sterker.

**3. Bronnen over betrouwbaarheid en toezicht** · Overnemen
De sessie-outline (blok 2 en de reserve) en `background-material/2026-07-01-hospital-quality-ai-presentation-query-trace.md`.

| Bron | Kern | Waar het past |
|---|---|---|
| Jagged frontier (Dell'Acqua, Lakhani e.a.) | Binnen de grens: +12% taken af, +25% sneller, +34% kwaliteit. Buiten de grens 19 procentpunt slechter, met overtuigender foute adviezen. | Dag 1 (LU1) |
| METR | Ervaren ontwikkelaars werkten met AI 19% trager, maar voelden zich 20% sneller. | Dag 1; het risico "Het experiment meet wat makkelijk te meten is" |
| Lakhani | AI "talks really well", ook bij een fout antwoord. Eerst zelf, dan de machine. Laat het model eerst tegen je in argumenteren. | Werkplaats 1, boards; het risico "Een deelnemer bouwt een board dat gelijk geeft" |
| Afstempelen (een team bij Y Combinator) | Na een reeks goede voorstellen wordt de controle ongemerkt een stempel. Tegenmaatregel: laat een steekproef eerst zelf scoren. | Dag 3, governance; de test gate voor gebruik (FR-15) |
| "Distributed de-skilling" (BCG, Goel) | Doet de AI altijd de eerste analyse, dan leren nieuwe medewerkers het vak minder goed. | Transformatieplan, onderdeel vaardigheden en mensen (FR-24) |
| Spijt over een uitbestede beslissing | Mensen willen vooral een controle bij handelingen die onomkeerbaar én zichtbaar voor anderen zijn. | Dag 3, governance: waar beslist een mens? |
| Citaat over verantwoordelijkheid | "Als het afdelingshoofd niet verantwoordelijk gehouden kan worden voor het resultaat, heb je een demo, geen agent." | Buildplan: senior sponsor (FR-15); het risico "De pilot blijft een demo" |
| AgentSpec (Wang) | Een regel heeft een aanleiding, een controle en een handhaving: "Als X gebeurt, controleer Y. Doe dan Z: pauzeer voor een mens, stop, of ga door." | Blueprint met genummerde regels (FR-22) |
| Hill (Harvard) | Besturen bespreken hun risicobereidheid zelden expliciet. Die moet er zijn vóórdat AI komt. | Dag 1, visie (LU2); het supervisory board |
| Bedrijf geleid door AI-agenten | Op dag 19 waarschuwde de AI dat het bedrijf de verkeerde kant op ging. Niemand deed iets met die waarschuwing. | Dag 3, governance: leg vast wie een escalatie oppakt |

Vervang bij overname de zorgvoorbeelden. Zoek elke bron op in het origineel voordat je hem gebruikt: een deel komt uit podcasts en wikipagina's. Neem ook de regel uit de outline over: kies per blok hooguit één nieuw punt om echt te zeggen.

**4. Vuistregel van Böckeler** · Overnemen

- **Wat het is.** De vuistregel: toezicht = kans op een fout × impact van de fout × hoe moeilijk de fout te zien is. Daarbij horen twee eisen aan elke uitkomst van AI. Ten eerste: elke uitspraak is te herleiden naar de brontekst, met een citaat. Ten tweede: bij twijfel of tegenstrijdigheid escaleert het systeem; het gokt niet.
- **Waar het past.** Vraag 4 van FR-16 ("waar een mens het besluit neemt") heeft nu geen hulpmiddel. De vuistregel geeft een route naar het antwoord. Hij helpt ook in werkplaats 3 bij de indeling in een risicoklasse.
- **Wat je aanpast.** In de outline heet de derde factor "detecteerbaarheid". Leg uit dat een hoge score betekent dat de fout moeilijk te zien is, zoals in een FMEA. Anders klopt de vermenigvuldiging niet. Breng het als hulpvraag binnen het governanceblok en niet als model; dan blijft de KISS-keuze overeind.

**5. Werkvorm "Mens tegen agent"** · Overnemen

- **Wat het is.** De zaal kreeg een melding met twee tegenstrijdige feiten en koos eerst zelf een score. De zaal was het onderling oneens. Daarna zag de zaal wat de agent deed: hij escaleerde de melding en noemde de tegenstrijdigheid als reden. Een score gaf hij niet. De boodschap: bij twijfel is escaleren het goede antwoord, ook voor AI.
- **Waar het past.** Dag 1, "Wat AI nu kan en niet kan". LU1 vraagt "aan de hand van eigen ervaring", en deze werkvorm levert die ervaring in vijf minuten. Werkplaats 2: hetzelfde patroon levert de referentiewaarde zonder AI die FR-20 en AC-15 eisen. De deelnemer scoort eerst zelf een paar gevallen en vergelijkt daarna met de AI.
- **Wat je aanpast.** Neem een casus buiten de zorg, bijvoorbeeld een klacht of een offerteaanvraag met twee tegenstrijdige feiten, uit de voorbeeldcasus. Bij 4 tot 12 deelnemers stemt de groep met de hand.

**6. "Veilig voor wie?" en de vraag "Weet je …?"** · Aanpassen

- **Wat het is.** De vraag "Is AI wel veilig?" werd drie vragen: veilig voor de gegevens, voor de patiënt en voor de melder. Elke vraag kreeg een toetssteen uit regels die de zaal al kende. Daarna kreeg elke vraag de vorm "Weet je …?". De antwoorden waren "Ja", "Nee, maar ik weet wie het weet" en "Nee, en ik weet niet wie het weet". De vraag met de meeste "weet niet wie" ging naar een gesprek met de buur. De vraag "Wie vraag je morgen?" (een functie, geen naam) leverde de eerste stap op.
- **Waar het past.** Het governanceblok (FR-16). De vertaling: gegevens wordt persoonsgegevens en DPIA. Patiënt wordt de klant of burger: risicoklasse en menselijk toezicht. Melder wordt de medewerker: richt de AI zich op het systeem of op personen? Die laatste vraag zit nu niet in FR-16. De kritiektrace noemt toezicht op werknemers door algoritmes als gat in de wiki, en het OR-lid in het comité stelt die vraag waarschijnlijk. Een vijfde governancevraag is een ontwerpbesluit (ADR). De vorm "Weet je …?" werkt zonder nieuw model. Hij maakt zichtbaar waar de organisatie het antwoord niet heeft, en levert de volgende stap voor FR-12.
- **Wat je aanpast.** Vervang de Wkkgz en KNMG "veilig melden" door de AVG, de AI-verordening en de eigen regels van de organisatie.

**7. Voorbereide antwoorden** · Achtergrond

- **Wat het is.** Acht lastige vragen met een kort antwoord. Zes vragen kun je algemeen maken:
  - Mag ik bedrijfsgegevens in ChatGPT plakken?
  - Helpt het als ik ze eerst anonimiseer?
  - Wie is verantwoordelijk als de AI een fout mist?
  - Kan een analyse door AI tegen een medewerker worden gebruikt?
  - Gaat AI ons werk overnemen? Het antwoord gebruikt loondata van Stanford en ADP tot september 2026.
  - Moeten we iets met de AI-verordening? Het antwoord noemt artikel 4 (AI-geletterdheid, van kracht sinds februari 2025).
- **Waar het past.** Het draaiboek (NFR-07), het governanceblok en het comité. "Mag ik dit plakken?" sluit aan op NFR-01.
- **Wat je aanpast.** Maak de antwoorden algemeen en haal de Wkkgz-artikelen eruit. De outline vraagt zelf om een juridische controle; die geldt hier ook.

**8. Facilitatie bij weerstand** · Aanpassen; besluit nodig voor het model

- **Wat het is.** Uit de outline: zie weerstand als signaal. Vraag door wat de weerstand precies is. Zoek de oorzaak: verlies, onzekerheid, verlies van controle, of een terechte zwakke plek. Los het niet meteen op. Dat volgt Carucci ("Resistance as data", atlas §11): drie valkuilen voor de leidinggevende (persoonlijk maken, moraliseren, haast met een oplossing) en vier soorten signaal.
- **Waar het past.** Dag 3, "Transformatieplan en draagvlak" (LU7, SN7), en werkplaats 3, waar de deelnemer een gesprek oefent. De vier signalen geven het nabespreken taal. Ook dag 1, "Stakeholders".
- **Besluit.** De vier vragen kunnen zonder besluit als facilitatietip in het draaiboek. Carucci als benoemd model naast ADKAR en COM-B valt onder de KISS-keuze. Dit is een grensgeval: beslis het bewust.

### Visualisaties

Alle pagina's volgen het stijlboek van Business Data Solutions, net als de LRD. Ze gebruiken warm zwart, crème en chartreuse als enige accent. Wat de AI doet, krijgt een eigen markering: zwart met chartreuse en het Bot-icoon. Elke pagina werkt met de pijltjes, de spatiebalk of een klikker, en `#stap-N` springt naar een stap.

**9. Vier kennisvormen naast elkaar** (`harness.html`, deel 2) · Aanpassen

- **Wat het is.** Vier manieren om kennis bij een taalmodel te krijgen, getest op drie vragen. Alleen het model (geen voorwerk), RAG (weinig voorwerk), een kennisgraaf (veel voorwerk) en een LLM-wiki (doorlopend voorwerk). De vragen: algemene vakkennis, de eigen werkwijze, en een vraag in meerdere stappen. Elke cel zegt "goed", "deels", "gok" of "geen", met een les erbij. De boodschap: geen vorm wint altijd; kies per vraag de eenvoudigste vorm die werkt.
- **Waar het past.** Dag 1: LU1 vraagt wat AI "vraagt van data", en dit maakt dat concreet. Werkplaats 2 (FR-20): bij de PRD bepalen welke kennis de use case nodig heeft. LU3 (beschikbaarheid en eigenaarschap van data): de kolom "voorwerk" is een kostenpost in de businesscase.
- **Wat je aanpast.** Vervang de drie VIM-vragen door vragen uit de voorbeeldcasus. De teksten staan in `KOLOMMEN` en `VRAGEN` in `src/harness.js`. Dit deel gebruikt D3 en motion.

**10. Agent, computer en organisatie als één bouwplaat** (`harness.html`, deel 1) · Aanpassen

- **Wat het is.** Eén printplaat met zes onderdelen en drie sets namen: computer, AI-agent, jouw ziekenhuis. De processor is het taalmodel is de professional. Het besturingssysteem is de harness is het kwaliteitssysteem. Het werkgeheugen is het contextvenster is het dossier op tafel. Daarbij komen de vijf taken van de harness, met hun tegenhanger in het werk. Uit de atlas (§10) komt de zin "het model huur je, de harness bezit je".
- **Waar het past.** Dag 1 (LU1): wat een agent is, met een tegenhanger in de eigen organisatie. De zin over huren en bezitten past in de businesscase: wat bouw je zelf, wat huur je?
- **Wat je aanpast.** De derde lens wordt "Jouw organisatie", met namen als werkafspraken en procedures, en het klantdossier. De teksten staan in `DELEN`, `LENZEN` en `TAKEN`. De Three.js-scène met de bot en de lopende figuur is veel code (`src/harness.js` en `src/harness-dragers.js`, samen bijna 60 kB). Heb je weinig tijd, toon dan de publieke versie zoals hij is.

**11. Vier faalwijzen van een agent** (`architectuur.html`, station AI-agent) · Overnemen als lijst

- **Wat het is.** Wat er mis kan gaan, en wat het opvangt. Een antwoord zonder grond: verankering met een citaat. Een ontbrekend feit: doorvragen. Tegenstrijdige feiten: escaleren. Het eigen huiswerk nakijken: een tweede AI toetst. Het station legt ook uit hoe een agent verschilt van een taalmodel. Een agent heeft vier onderdelen: context, skills, tools en een harness. Elk onderdeel heeft een tegenhanger in het werk. Het station Ontologie geeft een tweede voorbeeld van wat AI van data vraagt. Een zoekopdracht op het woord "val" vindt een melding zonder dat woord niet. Een zoekopdracht op het begrip vindt hem wel.
- **Waar het past.** Dag 1 (LU1). Werkplaats 2 (FR-20): de vier faalwijzen zijn kant-en-klare evaluatiecriteria voor een experiment met een agent, en voor de experimentvorm "technische test".
- **Wat je aanpast.** Neem de lijst over. De pagina zelf hoeft niet mee.

**12. Ask → Assist → Automate** (`groeimodel.html`, `groeipad.html`) · Besluit nodig

- **Wat het is.** Het groeimodel van Beutler (OpenAI, 2026). Bij Ask leest de AI mee en beslist de mens. Bij Assist stelt de AI op en autoriseert de mens. Bij Automate handelt de AI zelf af, met een harde grens. `groeimodel.html` toont dat als een trap, met een balk voor wie het werk doet (AI 20, 50 en 85%); het deel van de mens verdwijnt nooit. `groeipad.html` voegt ideeën toe die op elk proces passen. Een mens kijkt mee als de AI minder dan 90% zeker is. Een steekproef voorkomt afstempelen. Correcties worden data, zodat de AI scherper wordt. Bij Automate gaan alleen uitzonderingen naar een mens.
- **Waar het past.** Dag 3, "Van experiment naar buildplan" (FR-15, LU5). De fasen experiment, pilot en opschaling krijgen een tweede as: hoeveel zelfstandigheid krijgt de AI per fase? En het governanceblok (FR-16): "waar neemt een mens het besluit" krijgt per fase een antwoord. Het vult gat 3 uit deel 1 van de LRD: governance en de roadmap krijgen online elk maar één slide.
- **Besluit.** Dit is een nieuw model. De KISS-keuze laat er twee toe, en die plekken zijn bezet. Een derde vraagt een ADR die de KISS-keuze bijwerkt. Mijn advies: voeg je één model toe, kies dan dit. Het past direct op FR-15 en FR-16 en vraagt weinig uitleg.
- **Wat je aanpast.** `groeimodel.html` laadt geen bibliotheken en is het makkelijkst over te zetten. Alleen de teksten moeten algemeen worden (VIM, PRISMA, de PVC- of MIP-commissie). `groeipad.html` gebruikt Three.js en is sterk gebonden aan VIM. Neem daarvan het idee over, niet de pagina.

**13. Kansenkaart als swimlane** (`vim-swimlane.html`) · Aanpassen

- **Wat het is.** Het hele proces in banen per rol en kolommen per fase. De baan waarover je praat groeit en toont de volledige tekst; de andere banen krimpen. Een stip loopt de route. In de sessie volgde daarna de kansenkaart: vijf plekken in het proces waar AI kan helpen. Bij elke plek gold: "De AI doet een voorstel, de mens beslist." `vim-proces.html` toont dezelfde keten als stroom.
- **Waar het past.** Dag 2, "Businesscase met AI-onderzoek": "Eerst de procesketen in kaart: waar schuift het knelpunt heen?" (FR-14, LU3, LU4). En FR-20: het werkproces vóór en na. De werkvorm werkt ook op papier of een whiteboard.
- **Wat je aanpast.** De inhoud staat als data in `BANEN`, `VAKKEN`, `PIJLEN` en `BRONNEN` in `src/vim-swimlane.js`. Vul die met het proces van de voorbeeldcasus, en het is het voordoen. De pagina gebruikt D3 en motion.

**14. Prototype en animatie van een triage-agent** · Achtergrond; tonen zoals het is

- **Wat het is.** `vim-okf-simulatie.jsx` is een werkende demo van een keten: verzamelde meldingen, ontologie, een bundel met kennisbestanden, een triage-agent en een rapportage. De agent vraagt door bij een onvolledige melding, laat een tweede aanroep zijn antwoord controleren tegen het draaiboek, en een tweede AI beoordeelt de onderbouwing. Valt de AI weg, dan classificeert de demo op trefwoorden. Twee meldingen zijn met opzet fout: één is onvolledig, één is tegenstrijdig. `vim-agent-animatie.html` speelt vijf gevallen af, zonder netwerk en zonder bibliotheken. `background-material/psebench-features.md` laat zien hoe een wetenschappelijk artikel tot ontwerpkeuzes voor de agent leidde.
- **Waar het past.** Dag 1, als demonstratie van wat een agent nu kan (LU1). Als voorbeeld bij FR-15 ("een artefact dat een tester kan proberen") en bij de experimentvorm "technische test" (LU9). De notitie over PSEBench past bij "Zo bouwen AI-bedrijven" op dag 2: van onderzoek naar ontwerp.
- **Beperkingen.** De casus is de zorg. Live AI werkt alleen lokaal met een API-sleutel, of als artifact op claude.ai; de publieke versie toont alleen de terugval op trefwoorden. Werkplaats 2 heeft al een eigen voorbeeld (plattegronden uit foto's). Bouw dit dus niet om; houd het als reserve.

**15. Atlas met dertien raamwerken** · Achtergrond; besluit nodig per raamwerk
`background-material/2026-07-01-ai-maturity-frameworks-visuals.html`. Engelstalig, met een eigen stijl, en met cijfers in sectie 0 die verouderd zijn (zie onderdeel 1).

| § | Raamwerk | Vraag van het raamwerk | Waar het zou passen |
|---|---|---|---|
| 0 | Realitycheck: vijf metingen | Hoe zeldzaam is volwassen AI? | Verouderd; gebruik onderdeel 1 |
| 1 | Tin Man vs. Octopus (Werner, Le-Brun) | Kan de organisatie zich aanpassen? | 7S, onderdeel structuur (FR-24) |
| 2 | Cisco 5 Foundations | Zijn de randvoorwaarden er? | Deck, randvoorwaarden (dag 3) |
| 3 | MIT CISR, vier fasen | Waar staan we op de curve? | Roadmap (SN3); werk de cijfers bij (18% in fase 4, N=152) |
| 4 | Augmented Learners (Ransbotham, Kiron) | Leert de organisatie van AI? | Cultuur; LU8 |
| 5 | McKinsey Rewired | Wat is het transformatieplan? | Naast 7S (SN6) |
| 6 | Bouwen, samenstellen, samenwerken of kopen (Nishar, Nohria) | Wat maak je zelf, wat koop je? | Businesscase, de oplossing (FR-14) |
| 7 | Bain/OpenAI, vier stappen (Dutt e.a.) | Hoe kom je verder dan kleine winst? | Staat al in de LRD; de figuur past bij "Zo bouwen AI-bedrijven" |
| 8 | Anand en Wu, 2×2 | Op welke taak richt je AI eerst? | Kansen rangschikken (LU3) |
| 9 | Ask → Assist → Automate | Hoeveel zelfstandigheid krijgt de AI? | Zie onderdeel 12 |
| 10 | Agent harness | Wat moet er tussen model en gebruiker? | Zie onderdeel 10 |
| 11 | Weerstand als signaal (Carucci) | Wat zegt weerstand? | Zie onderdeel 8 |
| 12 | AI-volwassenheid van de werknemer, L0–L5 | Hoe ver is de persoon? | Dag 3, afsluiting: eigen rol (LU8) |

Gebruik de atlas als achtergrond voor de trainer, niet als handout. Dertien raamwerken botsen met het risico "Te veel modellen". Sectie 7 kan zonder besluit, want Dutt staat al in de LRD. Na Ask → Assist → Automate zijn Anand en Wu (§8) en de ladder L0–L5 (§12) de sterkste kandidaten. Elk van die twee is wel een nieuw model.

### Gereedschap en werkwijze

**16. Startpagina met tijdlijn** (`index.html`) · Aanpassen

- **Wat het is.** De startpagina is de presentatie zelf. Bovenaan staat een tijdlijn met één balk per blok, met de breedte naar het aantal minuten. Daaronder heeft elk blok een rij tegels: tegels met een link en tegels met een punt dat de spreker maakt. Blokken en tegels zijn te verslepen, en de klok rekent mee. Een markering toont waar je bent, met een speld in de tijdlijn. De volgorde blijft bewaard in de browser.
- **Waar het past.** Eén startpagina per lesdag op het scherm. Dat dekt NFR-04 (alle materialen op één plek), helpt bij NFR-06 (tijdblokken in beeld) en bij NFR-07 (een andere trainer ziet het programma). De tijden kunnen uit `DATA.days` in de LRD komen; dan blijft er één bron.
- **Wat je aanpast.** De controle van de AI-verbinding gaat eruit. Er komen tegels bij voor werkplaatsopdrachten, sjablonen en rolkaarten. NFR-06 vraagt een zichtbare timer, en die zit er nog niet in: voeg per blok een afteller toe.

**17. Excalidraw naar SVG in de huisstijl** (`scripts/excalidraw-huisstijl.py`) · Overnemen
Het script zet een `.excalidraw`-schema om in een SVG met het systeemfont, rechte lijnen en het palet van het stijlboek. Dat is dezelfde huisstijl als de LRD. Het `.excalidraw`-bestand blijft de bron. Het script kan zo mee, voor schema's van de bouwstraat, de boards of het werkproces vóór en na.

**18. Lekcheck vóór publicatie** (`scripts/controleer-build.mjs`) · Aanpassen

- **Wat het is.** De build stopt als de publieke versie een sleutel bevat, een proxypad, een waarde uit `.env` of de naam van een vertrouwelijk bestand. Het script toont nooit de gevonden waarde. Daarnaast gaan alleen pagina's uit een vaste lijst mee, nooit een glob.
- **Waar het past.** De publicatie van de LRD als artifact (ADR-013) en de privacyregel (ADR-016). Nu is dat een handmatige lijst in `CLAUDE.md`. Een kleine controle vóór elke publicatie kan drie dingen nagaan:
  - geen link naar `background-docs/`, `temp/`, `onderzoek/`, `docs/` of `CHANGELOG.md`;
  - geen bedrag uit het contract;
  - geen woord uit een lokale lijst met organisatienamen en achternamen. Die lijst blijft buiten het artifact.
- **Wat je aanpast.** Herschrijf het script voor één HTML-bestand. Dat is klein werk dat ADR-016 beter afdwingt.

**19. Projectskills** (`.claude/skills/` in de Santeon-repo) · Aanpassen
De Santeon-repo heeft drie skills die hier ontbreken: `ste100-writer`, `taalredactie-publicatie` en `ontwerp-dia`. Ze passen bij de dia's, handouts en het draaiboek van de lesdagen (NFR-07, NFR-08). `ontwerp-dia` is geschreven voor HAN-colleges. Volgens de werkwijze van deze repo wordt dat een algemene kopie met het voorvoegsel `aiso-`. `ste100-writer` staat ook al als algemene skill klaar.

**20. Stemtool met QR-code** (`meedoen.html`) · Niet
De stemtool is gemaakt voor 60 mensen in een theaterzaal. Hij hangt aan een dienst in een andere repo. Bij 4 tot 12 deelnemers (NFR-05) werkt handopsteken. Twee regels van de pagina zijn wel bruikbaar. Toon nooit een verzonnen uitslag, want voorbeeldstaven sturen de stemmers. Vraag naar een functie, nooit naar een naam.

**21. Ziekenhuismaquette, AI Monitor Ziekenhuizen en VIM-bronnen** · Niet
`ziekenhuis.html` en de cijfers van de AI Monitor Ziekenhuizen 2026 gaan over ziekenhuizen. Dat geldt ook voor de bronnen over incidentmeldingen in `background-material/` (NVZ, NIVEL, VMS, KNMG, Wkkgz, NEN 8009). Eén beeld uit de maquette is wel algemeen. 's Avonds maakt AI een eerste selectie van de röntgenbeelden; de volgende dag beslist de radioloog. Dat is een helder voorbeeld van Ask, en het kan als verhaal mee.

## Aandachtspunten bij overnemen

1. **Sector.** Alles gaat over een ziekenhuis. Maak het algemeen met de voorbeeldcasus, een fictieve middelgrote organisatie, die nog gebouwd moet worden. Een deel van dit materiaal kan die voorbeeldcasus vullen. Denk aan een proces als swimlane (13), een tegenstrijdig geval voor "Mens tegen agent" (5) en drie vragen voor de kennisvormen (9).
2. **KISS.** Bronnen, werkvormen en gereedschap passen zonder besluit. Een raamwerk dat deelnemers moeten leren, telt als model. Leg zo'n toevoeging vast in een ADR, en houd het bij één.
3. **Techniek.** De Santeon-pagina's laden three, d3 en motion uit npm, via Vite (three 0.187, motion 14, d3 7.9.2). De LRD laadt ze per `import()` van jsDelivr (three 0.160.0, motion 11.11.13, d3 7.9.0). Een pagina overzetten naar de LRD of naar een artifact betekent: de imports omzetten en opnieuw testen, want de versies verschillen. `groeimodel.html` en `vim-agent-animatie.html` laden geen bibliotheken en hebben dat probleem niet.
4. **Taal.** De Santeon-teksten volgen STE100 in het Nederlands en gebruiken de je-vorm, net als het stijlboek. De atlas is Engelstalig. Elke Engelse term krijgt bij overname een Nederlandse uitleg (NFR-08).
5. **Bronnen.** De meeste cijfers komen uit de ai-wiki, vaak tweedehands. Zoek elk cijfer dat in het programma komt eerst op in het origineel. Dat is dezelfde regel die we aan de deelnemers stellen.
6. **Privacy.** Geen enkel onderdeel bevat gegevens van onze deelnemers. Bij het aanpassen geldt ADR-016: geen voorbeelden die naar de organisatie van een deelnemer wijzen.
7. **Besluiten.** Elke overname in de LRD is een ontwerpbesluit. Dat betekent een ADR, een regel in het wijzigingslog en een nieuw versienummer.

## Voorstel voor de volgorde

**Vóór dag 1 (12 november), zonder bouwwerk**
- Onderdeel 1: de cijfers voor "Wat AI nu kan en niet kan".
- Onderdeel 3: jagged frontier, METR, Lakhani en Hill.
- Onderdeel 5: "Mens tegen agent" als opening van dat blok.
- Onderdeel 11: de vier faalwijzen als lijst.
- Onderdeel 9 of 10 zoals ze zijn, via de publieke versie, als voorbeeld uit een andere sector.

**Vóór dag 2 (26 november)**
- Onderdeel 2: de kritiekpunten op de rolkaarten van het comité.
- Onderdeel 1: het voorbeeld van bronkritiek bij de businesscase.
- Onderdeel 13: de swimlane met het proces van de voorbeeldcasus.
- Onderdeel 9: de kennisvormen met vragen uit de voorbeeldcasus, voor werkplaats 2.

**Vóór dag 3 (10 december)**
- Onderdeel 12: besluit over Ask → Assist → Automate; zo ja, `groeimodel.html` algemeen maken.
- Onderdelen 4 en 6: de vuistregel van Böckeler en "Weet je …?" in het governanceblok.
- Onderdeel 8: de vier vragen bij weerstand in het draaiboek.
- Onderdeel 2: de kritiektrace als bron voor werkplaats 3.

**Doorlopend**
- Onderdelen 17, 18 en 19: het schemascript, de lekcheck en de skills.
- Onderdeel 16: een startpagina per lesdag uit `DATA.days`.
- Onderdeel 7: de voorbereide antwoorden in het draaiboek.
