# Wijzigingslog — LRD AISO26009 Lesdagen

Elke versie van de [LRD](LRD-AISO26009-lesdagen.html), met de besluiten die erbij horen ([ADR's](docs/adr/README.md)). Nieuwste versie bovenaan. Het versienummer in de kop van de LRD is gelijk aan de bovenste regel hier.

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
