# Wijzigingslog — LRD AISO26009 Lesdagen

Elke versie van de [LRD](LRD-AISO26009-lesdagen.html), met de besluiten die erbij horen ([ADR's](docs/adr/README.md)). Nieuwste versie bovenaan. Het versienummer in de kop van de LRD is gelijk aan de bovenste regel hier.

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
