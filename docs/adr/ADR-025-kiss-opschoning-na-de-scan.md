# ADR-025: KISS-opschoning na de scan: minder dubbel, eerlijke KISS-keuzes, FR-12 in FR-18

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Na ADR-024 zocht een aparte agent naar verdere vereenvoudiging van de LRD. De KISS-criteria van `aiso-beoordeel-onderwijsontwerp` waren de meetlat. De scan deed tien voorstellen ([toetsrapport](../../onderzoek/2026-11-07-kiss-scan.md)). De trainer koos per voorstel. Van de programmawijzigingen voor de deelnemers is alleen de verhuizing van de kennisvormen overgenomen, omdat die bij voorstel 8 hoorde.

## Besluit

Overgenomen:

- **Acceptatiecriteria samengevoegd** (voorstel 3).
  - AC-03 gaat op in AC-02 (het werkplaatslog), AC-13 in AC-05 (de pitch) en AC-18 in AC-04 (de businesscase).
  - AC-04, AC-06, AC-07, AC-14 en AC-16 verwijzen naar "alle elementen uit" hun FR in plaats van die elementen over te typen.
  - NFR-04 gaat op in NFR-09.
- **Risico's samengevoegd: van 23 naar 15** (voorstel 4).
  - Vier risico's over toegang tot een sterk model worden er één, en drie over het thuiswerk ook.
  - De twee risico's over de boards worden er één.
  - "Te veel modellen" vervalt. Het herhaalde een KISS-keuze en had geen maatregel in een eis.
  - "De ontwikkeldoelen ontbreken" vervalt. Het staat al als open punt in deel 1 en in fase 0.
- **Niets twee keer typen** (voorstel 7).
  - De opbouw van het verslag staat alleen nog in FR-21. "Verwachting" ging daarbij van de lijst naar FR-21.
  - Het ritme van de werkplaats in 6.2 komt uit `DATA.rhythm`.
  - De opbouw van een ADR staat alleen nog in FR-18.
  - De kaart "Zelfstandigheid per fase" houdt het waarom; de regels staan in FR-15.
  - Deel 10 voor de deelnemer komt uit het veld `deliverable` op de AC's. Zo staat elk product bij het criterium dat het meet.
  - De takenlijst van de begeleider in 5.2 verwijst naar fase 0 en 2.
  - "Businesscase op één pagina" is gelijkgetrokken met FR-14: hooguit twee pagina's.
- **KISS-keuzes eerlijk** (voorstel 8).
  - De keuze over modellen telt nu al het gereedschap dat de lesdagen toevoegen.
  - De vier kennisvormen gaan van dag 1 (FR-26) naar de PRD in werkplaats 2 (FR-20), als naslag.
  - De twee keuzes over fouten in de online omgeving worden er één.
  - Drie keuzes die bewust de ingewikkelder optie kiezen, staan nu als "Spanningen" onder 5.1: twee boards, een interactief verslag, en de vorm van het experiment. Van 18 naar 14 paren.
- **FR-12 gaat op in FR-18** (voorstel 9). De gevolgen in de ADR van het boardmoment noemen de eerste volgende stap, en die gaat het actieplan in. De afsluitingen verwijzen naar FR-18. AC-12 meet de volgende stap.

## Overwogen alternatieven

Deze voorstellen zijn niet overgenomen:

- **De risicoklasse één keer bepalen** (voorstel 1).
- **De rondgang langs de decks schrappen** (voorstel 2).
- **Een vaste stoel voor de scepticus en een intake vóór dag 1** (voorstel 6).

  De trainer koos deze drie niet. Ze kunnen terugkomen bij de evaluatie in fase 4.
- **Het wijzigingslog van de deelnemers schrappen** (voorstel 5). Niet gekozen. Het zou een deel van ADR-015 terugdraaien.
- **De blueprint laten opgaan in PRD en buildplan** (voorstel 10). Niet gekozen. Het raakt ongeveer vijftien plekken en zou een eigen architectuurbesluit zijn.
- **Alle tien voorstellen tegelijk.** Verworpen: de trainer kiest per voorstel.

## Gevolgen

- **Tellingen:** FR 29 → 28, NFR 9 → 8, AC 19 → 16, risico's 23 → 15 en KISS-paren 18 → 14. De ID's AC-03, AC-13, AC-18, NFR-04 en FR-12 bestaan niet meer. De andere ID's houden hun nummer.
- **Minder volledig zonder JavaScript.** Deel 10 voor de deelnemer en de ritmelijst in 6.2 worden nu uit `DATA` opgebouwd. Zonder JavaScript zijn ze leeg, net als de andere tabellen.
- **Dag 1 vult gat 1 (data) dunner.** De kennisvormen komen pas in werkplaats 2, waar de PRD om die kennis vraagt. ADR-018 is daarom deels vervangen.
- **Het draaiboek is mee aangepast.** De kennisvormen en de uitleg van RAG, de kennisgraaf en de LLM-wiki staan nu bij werkplaats 2. De volgende stap na het governanceblok loopt via de ADR van het boardmoment.
- **De drie dubbelingen in het programma blijven bestaan:** de risicoklasse, de rondgang en het thuiswerk met de blueprint. Ze staan in het toetsrapport als kandidaten voor de evaluatie in fase 4.

## Raakt

Deel 5.1 (KISS-paren en spanningen), 5.2, 6.2, 6.3, 6.4, 10, 11, 12; FR-12 (vervalt), FR-18, FR-20, FR-21, FR-26; NFR-04 (vervalt), NFR-09; AC-02, AC-03 (vervalt), AC-04, AC-05, AC-06, AC-07, AC-12, AC-13 (vervalt), AC-14, AC-16, AC-17, AC-18 (vervalt), AC-19; programma dag 1 (10:00 en afsluiting), dag 2 (afsluiting), dag 3 (afsluiting); `DATA.rhythm`, `DATA.deliverables`; materiaal/draaiboek-bouwstenen.md; ADR-018.
