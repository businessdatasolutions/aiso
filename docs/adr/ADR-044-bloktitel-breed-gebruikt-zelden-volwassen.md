# ADR-044: Het blok van 10:00 op dag 1 heet "Breed gebruikt, zelden volwassen"

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Het blok van 10:00 op dag 1 heette "Wat AI nu kan en niet kan". Sinds ADR-018 en ADR-040 begint het blok met "Mens tegen agent". Daarna komen de cijfers over breed gebruik en zeldzame volwassen inzet, met de maquette van een ziekenhuis als voorbeeld. Dan volgen de grillige grens, vier faalwijzen van een agent en de soorten AI.

De oude titel beloofde een overzicht van wat AI kan. Het blok gaat over iets anders: bijna elke organisatie gebruikt AI, maar weinig organisaties halen er op grote schaal waarde uit. De maquette laat dat in één beeld zien: een ziekenhuis heeft gemiddeld 18 AI-toepassingen, en één daarvan is opgeschaald. De titel staat op de startpagina boven het blok, en de trainer vond dat hij niet meer paste.

## Besluit

Het blok heet **"Breed gebruikt, zelden volwassen"**. De titel noemt de kernboodschap. De andere delen van het blok laten zien waarom het zo gaat. Buiten de grillige grens is AI zelfverzekerd fout. Een agent faalt op vier manieren. En gevoel is geen meting.

De inhoud, de tijden en de uitkomst van het blok veranderen niet.

## Overwogen alternatieven

- **"De grillige grens van AI".** Verworpen: dat is één punt in het blok. De maquette en de cijfers gaan over iets anders.
- **"Mens tegen agent: wat AI kan".** Verworpen: de werkvorm duurt vijf minuten van de 45. Een titel die ermee begint, legt het gewicht verkeerd.
- **"Wat AI kan, en waar het misgaat".** Verworpen: dicht bij de oude titel. De kloof tussen gebruik en volwassen inzet staat er nog steeds niet in.

## Gevolgen

- De startpagina en deel 8 tonen de nieuwe titel, want ze lezen hem uit `DATA`.
- De titel verklapt niets van de omslag om 11:00 (FR-30): hij gaat over hoe organisaties AI inzetten, niet over strategie.
- Oude ADR's, onderzoeksnotities en regels in het wijzigingslog houden de oude titel. Ze beschrijven wat toen gold.

## Raakt

Deel 7 (FR-26) en deel 8 (dag 1, 10:00). Ook: `materiaal/draaiboek-bouwstenen.md` (kop van het blok) en de opmerkingen in `materiaal/ziekenhuis.html`.
