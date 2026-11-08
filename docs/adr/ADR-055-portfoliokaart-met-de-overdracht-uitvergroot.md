# ADR-055: De portfoliokaart volgt de bron en vergroot de overdracht uit

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Stap 3 van de lespagina "Waarom geen plan volstaat" (FR-34) toonde de portfoliokaart als twee losse panelen naast
elkaar, met vier initiatieven van Voorbeeld BV. De kaart van Strategyzer (Osterwalder e.a., 2020) zet de twee
portfolio's schuin tegen elkaar. Verkennen staat linksonder, benutten rechtsboven, en ze raken elkaar op één punt:
5, de overdracht. In de oude tekening liep de risico-as bij benutten bovendien andersom, van klein naar groot. Zo
sloten de twee portfolio's niet op elkaar aan.

De trainer wil twee dingen laten zien. Management maakt steeds een afweging tussen consolideren en innoveren. En de
kwaliteit van de overdracht is een succesfactor. In software heet de oplossing CI/CD en DevOps: kleine stappen,
vaak, getest en terug te draaien. Teams die zo opleveren, hebben ook minder mislukte wijzigingen (Forsgren e.a.,
2018).

## Besluit

- **De kaart volgt de bron.** Verkennen staat linksonder, benutten rechtsboven, en ze raken elkaar op 5. In beide
  portfolio's loopt de risico-as van veel naar weinig risico. Alle assen hebben hun naam, hun uitersten en hun
  werkwoord: ontwerpen en testen bij verkennen, versterken en beschermen bij benutten.
- **Punt 5 is uitvergroot**, in een kaart naast de portfoliokaart. De kop zegt: "De overdracht is de flessenhals."
  Daaronder staan twee banen. Bij "over de muur" gaat een innovatie aan het eind in één keer naar het huidige
  businessmodel. In de pijplijn van Voorbeeld BV gaat het van experiment via pilot naar opschalen, met voor elke stap
  een poort: een norm vooraf en een deur die terug kan.
- **Op de kaart staan geen initiatieven meer.** Voorbeeld BV staat in de pijplijn. De tabel met vier plekken in
  `voorbeeldcasus.md` vervalt.
- **De figuur past op één scherm.** Ze krijgt hooguit 46 % van de hoogte, net als de oude tekening. Een knop
  "Toon groot" toont alleen de figuur, schermvullend, voor een laptop of een kleine beamer.

## Overwogen alternatieven

- **De hele kaart met alle elf stations en de initiatieven erop ("de reis").** Verworpen: te druk voor vijf minuten.
  Punt 5 blijft een stip, en de kwaliteit van de overdracht zie je niet.
- **De kaart als kringloop, met een keuze voor management** (consolideren, allebei of innoveren). Benutten betaalt
  daarin verkennen, en verkennen vernieuwt benutten. Verworpen: de afweging staat al in de tekst boven de figuur
  (March, 1991) en komt terug in de bandiet van stap 4. De overdracht was het nieuwe inzicht.
- **"Proef" en "de lijn" als namen in de banen.** Verworpen: "innovatie" past bij de as innovatierisico, en "huidig
  businessmodel" bij de bron.

## Gevolgen

- De afweging consolideren of innoveren staat niet meer in de figuur zelf. De trainer zegt haar bij de tekst erboven.
- Twee details van de casus zijn nieuw: de pilot bij heel Klantcontact, en opschalen naar Planning en Service.
- De pijplijn bereidt stap 5 (de deur die terug kan) en dag 2 om 10:45 voor (FR-35). De trainer legt de deur hier
  nog niet uit.
- Een nieuwe bron: Forsgren, Humble en Kim (2018).

## Raakt

- Deel 2 (Hoe je ermee werkt), FR-34, `DATA.days`: dag 1 om 11:00 (trainer, verloop) en de bronnen.
- `materiaal/vier-vragen.html` (stap 3 en de bronnen), `materiaal/voorbeeldcasus.md` en
  `materiaal/draaiboek-bouwstenen.md`.
- ADR-033: aangevuld, niet vervangen. De portfoliokaart blijft het beeld bij verkennen en benutten.
