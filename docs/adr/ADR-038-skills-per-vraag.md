# ADR-038: Per vraag een vaardigheid, en een AI-skill waar die iets toevoegt

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De gebruiker beschreef het product van de training als "een algemene set aan methodes, skills en tools" voor vier taken van leiderschap. Op de vraag of skills vaardigheden of AI-skills zijn, koos de gebruiker allebei: per vraag een vaardigheid, en een AI-skill waar die iets toevoegt. Vóór dag 1 blijven de boards de enige AI-skill.

## Besluit

- **Per vraag drie velden.** Elke vraag in `DATA.vragen` noemt een methode, een vaardigheid en tools en skills. Deel 6.1 toont ze op een kaart per vraag.
- **AI-skills nu:** de twee boards. Het casusdeck heeft geen skill nodig, want de instructie voor de AI staat in het bestand zelf.
- **Besluit na dag 1.** In fase 2 (13–25 november) beslist de trainer welke vragen een eigen AI-skill krijgen. Kandidaten zijn de businesscase bij vraag 3 en de roadmap bij vraag 4.

## Overwogen alternatieven

- **Alleen vaardigheden.** Verworpen door de gebruiker.
- **Vóór dag 1 vier AI-skills bouwen.** Verworpen: er is geen tijd om ze in drie omgevingen te testen.

## Gevolgen

- **Fase 2 krijgt een besluit erbij.**
- **Elke nieuwe skill moet in Claude, ChatGPT en Gemini getest worden,** net als de boards (FR-17).

## Raakt

Deel 1, 6.1 en 13; `DATA.vragen` en `DATA.phases`.
