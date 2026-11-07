# ADR-019: Ask → Assist → Automate in het buildplan, als derde nieuw model

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De KISS-keuze in deel 5.1 stond twee nieuwe modellen toe naast de vijf uit de online omgeving: de risicoklassen van de AI-verordening en een businesscase op één pagina. Gat 3 uit deel 1 (governance en de roadmap) had daarmee geen antwoord op de vraag hoeveel de AI zelf mag doen, en in welke volgorde. FR-16 vroeg wel "waar neemt een mens het besluit", maar gaf geen hulpmiddel. Het groeimodel van Beutler (OpenAI, 2026) beantwoordt die vraag per werkproces in drie niveaus: Ask, Assist en Automate. De hergebruiknotitie raadde aan: voeg je één model toe, kies dan dit.

## Besluit

Ask → Assist → Automate is het derde nieuwe model. Het staat op één plek: het buildplan. Elke fase krijgt een niveau van zelfstandigheid, met wie beslist (FR-15, AC-06). Het experiment draait op Ask. Automate geldt alleen voor duidelijke gevallen met een laag risico, en altijd met een harde grens: uitzonderingen en twijfel gaan naar een mens. De test gate voor gebruik krijgt een steekproef die eerst een mens beoordeelt, tegen afstempelen. Deel 6.4 heeft er een kader over, en `materiaal/groeimodel.html` toont het met de voorbeeldcasus.

## Overwogen alternatieven

- **Geen model, alleen de vraag "waar beslist een mens?".** Vaag: de vraag zegt niet hoe de rol van de mens per fase verandert.
- **Een volwassenheidsmodel voor de organisatie, zoals de vier fasen van MIT CISR.** Dat meet de hele organisatie, niet een use case. Het past niet in het buildplan.
- **De ladder voor AI-volwassenheid van de werknemer (L0–L5).** Die meet een persoon. Interessant voor de eigen rol (LU8), maar het lost gat 3 niet op.

## Gevolgen

- De KISS-keuze in 5.1 noemt drie toevoegingen. De zelftoets in 5.2 zegt "plus drie nieuwe". Het risico "Te veel modellen" verwijst naar drie modellen.
- FR-15 en AC-06 vragen per fase een niveau. FR-15 draagt ook bij aan LU6.
- Het model geeft een percentage AI-werk per niveau als beeld. Dat is geen meting, en de lespagina zegt dat.

## Raakt

Deel 5.1 (KISS), deel 5.2 (PAMS), deel 6.4 (kader "Zelfstandigheid per fase"), FR-15, AC-06, de bouwstraat (stap Buildplan), het blok "Van experiment naar buildplan" op dag 3, het risico "Te veel modellen", bronnen (IT Revolution, 2026), `materiaal/groeimodel.html`.
