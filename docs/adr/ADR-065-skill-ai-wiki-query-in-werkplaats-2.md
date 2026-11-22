# ADR-065: De skill ai-wiki-query voor deelnemers, in werkplaats 2

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-22 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De trainer wil de deelnemers de skill `ai-wiki-query` aanbieden. Die beantwoordt een vraag alleen met de openbare
AI-wiki van de trainer, met bij elke bewering een URL van de wiki. De skill staat beschreven in een blueprint in de
repo van de wiki (`docs/2026-11-20-blueprint-ai-wiki-query-skill.md`).

Op dag 2 zit de wiki al in het programma. In werkplaats 2 schrijft de AI het voorstel voor het experiment, en deel 2
daarvan ("Wat we al weten") zoekt ook in de wiki (FR-38). De prompt zei de AI "bij de index" te beginnen. Volgens de
blueprint is die startpagina 1,4 MB, te groot om in één keer op te halen. Een AI die daar begint, krijgt een
afgekapte pagina.

De blueprint heeft twee routes. Route A gebruikt een Python-script dat de zoekindex van 11 MB downloadt en lokaal
doorzoekt. Daarvoor moet de AI een script met internettoegang mogen draaien. Route B haalt losse pagina's op, vanaf
de lijst met syntheses, de lijst met concepten of de sitemap. Deelnemers werken in Claude, ChatGPT of Gemini in de
browser, zonder installatie (NFR-02). Of een script daar het internet op mag, is niet zeker.

ADR-038 liet in fase 2 beslissen welke vragen een eigen AI-skill krijgen, en eiste dat elke nieuwe skill in Claude,
ChatGPT en Gemini getest wordt.

## Besluit

- **Vraag 3 krijgt de skill ai-wiki-query.** De deelnemer gebruikt hem in werkplaats 2, bij het deel "Wat we al
  weten" van het experimentpaper. De skill vervangt daar een regel in de prompt. Er komt geen stap bij in de werkplaats.
- **Installeren gebeurt thuis, vóór dag 2.** De lespagina Je presentatie voor het investeringscomité krijgt stap 7,
  "Je wiki-skill, voor werkplaats 2". Daar staat de skill als zip en als tekst, net als `ontwerp-dia` in stap 4. De
  deelnemer probeert hem één keer met een vaste testvraag. De opdrachttabel bovenaan noemt het.
- **Een versie voor deelnemers, alleen met route B.** Er is geen script. De skill beschrijft de wiki, de drie
  startpunten, de werkwijze (inkaderen, Engelse zoektermen, schiften met vaste redenen, gericht lezen, hoogstens één
  extra zoekronde) en de vorm van het antwoord: ankers [W1] met URL's, het kopje "Wat de wiki niet zegt", kennis van
  buiten de wiki apart, en een kort zoekspoor. Dit volgt de keuze bij `ontwerp-dia`: de versie voor deelnemers heeft
  geen script.
- **In een paper staat de oorspronkelijke bron.** Een wikipagina vat een bron samen. In de bronnenlijst volgens APA 7
  staat de bron die de wikipagina noemt; de URL van de wiki mag erbij, als vindplaats. Dit staat in de skill en in de
  prompt.
- **Zonder skill werkt de prompt ook.** Regel 4 van de prompt voor het voorstel zegt nu: gebruik de skill als die er
  is; anders zoek met Engelse termen en begin bij de syntheses, de concepten of de sitemap, niet bij de startpagina.
- **De trainer test de skill vóór 26 november** in Claude, ChatGPT en Gemini, ook met de onderzoeksfunctie aan.

## Overwogen alternatieven

- **Gebruiken om 11:00, bij Warner en Wäger.** De wiki heeft daar sterke pagina's over. Verworpen: het blok heeft
  geen ruimte voor iets nieuws.
- **Gebruiken in de AI-taak van de lunch.** Verworpen: dat onderzoek gaat over het eigen knelpunt, met bronnen van
  het open web. De wiki gaat over AI in het algemeen, en dat hoort bij "Wat we al weten".
- **Gebruiken voor de presentatie vóór dag 2.** Verworpen als doel: de opdracht vraagt dat de deelnemer zelf zoekt,
  en ze is al verstuurd. De skill staat wel op die lespagina, om hem te installeren.
- **Installeren in werkplaats 2.** Verworpen: installeren kostte op dag 1 bij de boards veel tijd, en werkplaats 2
  duurt een uur.
- **Route A, met het script uit de blueprint.** Verworpen voor deelnemers: in een browseromgeving is niet zeker dat
  een script het internet op mag. Route A blijft voor de trainer.

## Gevolgen

- Deelnemers krijgen een derde skill, naast de twee boards en `ontwerp-dia`. Installeren gaat zoals bij de boards.
- De opdracht vóór dag 2 is al verstuurd. De trainer stuurt de link naar stap 7 met een kort bericht na.
- Een onderzoeksfunctie (Deep Research, Research) gebruikt een geïnstalleerde skill misschien niet. Dan valt de AI
  terug op regel 4 van de prompt. De test vóór 26 november laat zien hoe het in elke omgeving gaat.
- Een bronpagina in de wiki noemt de titel en de auteurs van de bron, maar meestal geen DOI. De AI moet de
  oorspronkelijke bron dus zelf opzoeken voor de bronnenlijst.

## Raakt

- LRD: FR-38, FR-41, de tools bij vraag 3, de werkkaart en de trainersinstructie van werkplaats 2, de opleverlijst
  van de trainer en fase 2.
- `materiaal/presentatie-dag2.html` (stap 7, de opdrachttabel en het script voor de zips),
  `materiaal/experimentpaper.html` (stap 2 en de prompt voor het voorstel) en `materiaal/draaiboek-bouwstenen.md`.
- `CLAUDE.md`.
