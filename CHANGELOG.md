# Wijzigingslog — LRD AISO26009 Lesdagen

Elke versie van de [LRD](LRD-AISO26009-lesdagen.html), met de besluiten die erbij horen ([ADR's](docs/adr/README.md)). Nieuwste versie bovenaan. Het versienummer in de kop van de LRD is gelijk aan de bovenste regel hier.

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
