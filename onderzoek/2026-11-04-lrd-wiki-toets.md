---
type: toetsrapport
onderwerp: "LRD AISO26009 (lesdagen) getoetst aan de ai-wiki"
datum: 2026-11-04
getoetst_document: ../LRD-AISO26009-lesdagen.html
methode: iterative-wiki-query (ai-wiki), 4 niveaus
research_log: /Users/witoldtenhove/Projects/ai-wiki/inspiration/2026-11-04-lrd-aiso26009-wiki-toets-research-log.md
---

# LRD AISO26009 getoetst aan de ai-wiki

## Oordeel in het kort

De richting van de LRD klopt met wat de wiki het sterkst onderbouwt:

- werken aan de eigen casus, in een vaste groep, als traject;
- een experiment met een norm vooraf;
- fasen met test gates;
- een vaste plek om vast te leggen wat je leert.

Er zijn drie echte spanningen:

1. **De bouwstraat werkt van één use case naar één product.** Volgens de wiki zit de waarde in het herontwerp van het werkproces. Dat is de best onderbouwde uitspraak in de wiki: zeven of meer bronnen zijn het erover eens.
2. **Het buildplan toetst of een artefact werkt, maar niet of het in het werk terechtkomt.** Juist daar blijven pilots volgens de wiki hangen.
3. **Werkplaats 3 oefent iemand overtuigen.** De wiki behandelt weerstand als informatie over het plan.

Over de didactische kaders (Bloom, Pink, Kolb, COM-B), over 7S, ADKAR, Kotter en Mendelow, en over de AI-verordening zegt de wiki niets. Op die punten steunt de LRD op eigen bronnen.

## Vijf aanbevelingen, gerangschikt naar impact

| # | Aanbeveling | Raakt | Wiki-basis |
|---|---|---|---|
| 1 | **Zet herontwerp van het werkproces in de bouwstraat.** De businesscase en de PRD beschrijven de hele procesketen: waar schuift het knelpunt heen, en wat moet er in het omliggende werk veranderen? Vervang de voorbeeldnorm "−20%" door een norm die je alleen met herontwerp haalt. | FR-14, FR-20, sjablonen, `experimentTypes` | Bain/OpenAI (Dutt et al., 2026): procesherontwerp is *"the most challenging part … and also creates most of the value"*. Argenti (Goldman Sachs): *"3x more productive, not 20%"*. |
| 2 | **Geef elke gate in het buildplan ook een criterium voor integratie en gebruik, en noem een senior sponsor uit de business.** | FR-15, AC-06, LU5 | Allen/AWS over *"pilot purgatory"*. McKinsey: *"no single success story where senior business leaders weren't in the driver's seat"*. Beutler/OpenAI: *"business owns the outcomes"*. |
| 3 | **Vergelijk het experiment met de huidige werkwijze en meet een uitkomst.** Elke norm krijgt een referentiewaarde zonder AI. De businesscase noemt minstens één uitkomstmaat (omzet, kwaliteit of klant) naast tijd of fte, en laat een dal vóór de winst zien. | FR-20, FR-14, AC-15 | Dutt et al.: metrics *"that allow for comparisons with non-AI methods"*. BCG: herontwerp, niet alleen kostenbesparing. Brynjolfsson: de J-curve. |
| 4 | **Maak van werkplaats 3 een diagnose.** Welk signaal hoor je (verlies, onzekerheid, gebrek aan controle, of een fout in het plan), en welke aanpassing aan het plan volgt eruit? Plan dat de uitvoering betrokken wordt vóórdat de use case vastligt. | LU7, werkplaats 3, FR-24 | Carucci (HBR, 2026): weerstand is informatie. Hij waarschuwt voor *"rushing to resolution"* en *"faux-inclusion"*. Dutt: FabricationCo betrok de frontlijn en kwam tot 14 use cases. Let op: Carucci is een praktijkessay zonder data. |
| 5 | **Behandel de boards als hulpmiddel en benoem hun zwakke plekken.** Spreek over een board als hulpmiddel, niet als collega. Benoem bij het boardmoment op dag 3 dat AI zwak is in strategische keuzes voor de lange termijn. Zet een tweede model ook in voor de boards. | FR-17, FR-18, deel 6.3 | Kropp (BCG/HBR, RCT, N=1.261): AI als werknemer framen geeft −9 pp persoonlijke verantwoordelijkheid en −18% gevonden fouten. Allen & McDonald (2026): *"exploitation bias"*. Boussioux: antwoorden schuiven naar het gemiddelde. |

Kleiner punt: draai het blok "Wat AI nu kan en niet kan" op dag 1 om. Laat deelnemers de grens eerst zelf tegenkomen en geef daarna pas uitleg. Uitleg vooraf kan averechts werken. In het experiment van Dell'Acqua deed de groep met GPT plus uitleg het slechter dan de groep met alleen GPT, op taken buiten de grens van wat AI kan.

## Bevindingen per onderdeel

Oordelen: **sluit aan**, **spanning**, **ontbreekt** (de wiki noemt iets wat de LRD mist), **wiki zwijgt**.

| Onderdeel | Oordeel | Wat de wiki zegt | Wiki-pagina |
|---|---|---|---|
| Eigen casus, vaste groep, traject (6.1) | Sluit aan | Programma's die *"run in cohorts, and are part of a journey"* werken beter dan zelfstudie (Sadun & Wood, 2025) | sources/2025-11-24-sadun-wood-… |
| Werkplaatslog en boardlog | Sluit aan | Kiron & Schrage: *"decision journals … evaluation logs"*. Ransbotham et al.: met feedbacklussen 6× zo vaak substantiële baten | concepts/micro-productivity-trap |
| Frontiermodel, geen gratis versie (NFR-02) | Sluit aan | Mollick: de *"$20 decision"* | sources/2026-06-16-mollick-…, syntheses/ai-worker-maturity-levels |
| Vraag "waar ging het mis?" (AC-03) | Sluit aan | *"Evaluation, not generation, is the binding constraint"* | syntheses/ai-worker-maturity-levels |
| Uitleg "wat AI kan" vóór de werkplaats | Spanning | *Familiarity training can backfire*. Buiten de grens van wat AI kan −19 pp correct | concepts/jagged-frontier |
| Zelfrapportage in het werkplaatslog | Ontbreekt | METR: 19% trager, maar 20% sneller gevoeld. Zelfbeoordeling losgekoppeld van prestatie (Dell'Acqua, 2026) | syntheses/ai-worker-maturity-levels, sources/2026-06-12-dellacqua-… |
| AI-boards beoordelen plannen (FR-19) | Sluit aan | LLM's maken en beoordelen businessplannen op menselijk niveau (Csaszar et al., 2024) | sources/2024-12-01-csaszar-… |
| Harde scepticus in het board | Sluit aan | *"the AI is a sycophant — tell it to act like a critic"* (Mollick) | sources/2026-06-16-mollick-… |
| Personificatie (v_Naam, commissarissen) | Spanning (extrapolatie) | Kropp: werknemer-framing −9 pp verantwoordelijkheid, +44% escalaties, −18% gevonden fouten | sources/2026-05-06-kropp-… |
| Boardmoment over het buildplan | Spanning | Frontiermodellen uit eind 2025 slechter dan MBA-studenten bij keuzes met uitgestelde feedback | concepts/jagged-frontier |
| 5–7 perspectieven in één model | Spanning | Antwoorden schuiven *"toward the statistical mean"* (Boussioux, Haghighi) | concepts/jagged-frontier, concepts/responsible-ai |
| Experiment met normen vooraf (AC-15) | Sluit aan | Sadun: *"You want to have hypothesis … measurement"*. *"AI makes vague specs more costly"* | concepts/spec-driven-development |
| Absolute normen, vergelijking tussen modellen | Ontbreekt | Vergelijk met de werkwijze zonder AI (Dutt) | sources/2026-05-02-dutt-chatterji-… |
| Interactief verslag gebouwd met AI | Spanning | AI maakt foute antwoorden overtuigender: *"subjective coherence"* | concepts/jagged-frontier |
| Vijf documenten op een rij, design docs | Spanning | Anthropic: *"design docs out, prototypes in"*. Werken met specs alleen bewezen in software (confidence 0.75) | sources/2026-05-08-running-an-ai-native-…, concepts/spec-driven-development |
| "Begin met het eenvoudigste" | Sluit aan | *"Find the simplest solution possible"* | sources/2024-12-19-anthropic-building-effective-agents |
| Businesscase voor één use case (FR-14) | **Spanning, grootste impact** | Procesherontwerp maakt de waarde (7 bronnen, confidence 0.95) | syntheses/organizational-frameworks-…, concepts/micro-productivity-trap |
| "Waarde" niet ingevuld | Ontbreekt | Uitkomstmaten. Alleen naar kosten kijken is *"a little lazy"* (Brynjolfsson) | concepts/micro-productivity-trap |
| Terugverdientijd | Ontbreekt | J-curve. *Rewired*: 1–2 jaar, maar met selectie-effect | syntheses/organizational-frameworks-… |
| Rangschikken op waarde en haalbaarheid (LU3) | Sluit aan, gat | "Readiness for change" ontbreekt als criterium (Lowe's) | sources/2026-05-02-dutt-chatterji-… |
| Fasen met gates (FR-15) | Sluit aan | Pilot als fase die je snel doorloopt. Lowe's ging naar 1.700+ winkels | syntheses/organizational-frameworks-… |
| Gate toetst alleen het artefact | Spanning | *"Pilot purgatory"*. De diagnose is beter onderbouwd dan de cijfers (95% / 56% / ~30%) | concepts/micro-productivity-trap |
| Eigenaar per fase, rol los van positie | Spanning | Senior leaders aan het roer. *"business owns the outcomes"* | syntheses/organizational-frameworks-… |
| Buildplan als roadmap voor jaar 1 | Spanning (klein) | Anthropic: *"no more 6-month roadmaps"* | sources/2026-05-08-running-an-ai-native-… |
| 7S, ADKAR, Mendelow, Kotter | Wiki zwijgt | Kotter alleen genoemd, niet uitgewerkt | — |
| Tijdsverdeling mens tegenover techniek | Spanning | 70/20/10 mensen/processen/techniek (Hines-Pierce). Dit is een advies, geen meting | concepts/micro-productivity-trap |
| AI benoemen in rollen | Ontbreekt | Werknemer-framing geeft +13% onzekerheid over de eigen beroepsidentiteit. *"make accountability explicit"* | sources/2026-05-06-kropp-… |
| Vaardigheden | Ontbreekt | Toegang tot AI-tools en training staan in een verhouding van 3:1. *"Imagination gap"*: training leert het werk niet anders inrichten | concepts/micro-productivity-trap |
| Weerstand omzetten (werkplaats 3) | Spanning | Weerstand is informatie. *"Be willing to adapt the plan"* | sources/2026-05-07-carucci-… |
| Wanneer stakeholders betrokken worden | Ontbreekt | *"Faux-inclusion"*. Betrek de frontlijn vroeg | sources/2026-05-07-carucci-…, sources/2026-05-02-dutt-chatterji-… |
| AI-verordening, risicoklassen | Wiki zwijgt | Alleen in bijzinnen genoemd | — |
| Vier governancevragen (FR-16) | Sluit aan | IMDA: controlepunten waar een mens goedkeurt | concepts/responsible-ai |
| Risicobereidheid | Ontbreekt | Hill: besturen spreken hun risicobereidheid zelden uit, en beslisrechten zijn vaak niet expliciet | concepts/responsible-ai |
| Bloom, Pink/PAMS, Kolb, COM-B | Wiki zwijgt | — | — |
| Maken "met de AI" | Spanning | AI-shortcuts geven het gevoel dat je leert (Mollick). Laat deelnemers hypothese, norm en besluit eerst zelf formuleren | sources/2026-06-16-mollick-… |
| Vaste duo's | Sluit aan, met nuance | Een team met AI heeft ~3× zoveel kans op een top-10%-oplossing, maar dat gold voor teams aan hetzelfde probleem | sources/2026-06-12-dellacqua-… |
| Ervaren doelgroep | Sluit aan | Ervaring helpt om AI-output te beoordelen (Mollick, BCG) | sources/2026-06-16-mollick-… |

## Waar de wiki zwijgt

Op deze punten steunt de LRD op eigen bronnen:

- de didactische kaders (deel 2);
- 7S, ADKAR, Kotter en Mendelow;
- de AI-verordening;
- de voorbeelden van AI-bedrijven: Kohavi, model cards, de Responsible Scaling Policy en OpenAI Evals;
- het risico dat AI bronnen verzint.

Het research log zet deze punten in `wiki/log.md` als kandidaten om later bronnen voor te verzamelen.

## Methode en controle

- **Werkwijze:** de iteratieve wiki-query in vier niveaus (skill `iterative-wiki-query`), uitgevoerd door een agent.
  - Niveau 1: 4 pagina's van 3 types.
  - Niveau 2: 4 pagina's.
  - Niveau 3: 3 pagina's plus gerichte sectielezingen.
  - Gezocht met qmd, zoals CLAUDE.md §Search voorschrijft.
- **Steekproef:** zeven claims zijn daarna letterlijk in de wiki gecontroleerd en klopten alle zeven: procesherontwerp, familiarity backfire, de cijfers van Kropp, faux-inclusion, design docs bij Anthropic, de vergelijking met de werkwijze zonder AI (Dutt), en Argenti's 3×.
- **Wijzigingen in de wiki:** alleen `accessed_at` op zes concept- en synthesepagina's, een log-entry en het research log. Er is niets aangepast in `raw/` of in de inhoud van pagina's.
- **Volledige vraagketen en bronnenmatrix:** zie het research log.
