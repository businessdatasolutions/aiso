# ADR-032: Eigen werk als invoer, apart van de online omgeving, en "Je gebruikt" op de startpagina

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Elk programmablok heeft in `DATA` een veld `input`. In de programmatabel van deel 8 heet die kolom "Invoer uit de online omgeving". Daar horen de online opdrachten bij, zoals de stakeholderanalyse of de COM-B-analyse. Dertien blokken zetten er ook werk in dat de deelnemer pas tijdens of tussen de lesdagen maakt. Voorbeelden zijn de stukken van het bestuur (AI-taak van 10:45), de top 3 stakeholders (ADR-030) en de businesscase.

De startpagina toont per blok alleen "Je maakt:". Wat een blok gebruikt, ziet de deelnemer daar niet. De trainer kreeg de vraag waar de top 3 stakeholders voor dient. Het antwoord stond alleen in het detailpaneel van de LRD en in het draaiboek.

## Besluit

- **Een eigen veld `uses`.** Daarin staat het eigen werk dat een blok gebruikt. Het komt uit een eerder blok, uit de AI-taak van een pauze of van thuis. Bij elk stuk staat waar het vandaan komt, zoals "(11:45)" of "(AI-taak van de lunch)".
- **`input` alleen voor de online omgeving.** Het eigen werk gaat uit `input`. Zo klopt de kolomnaam weer.
- **Ook blokken zonder invoer krijgen `uses`.** Dat zijn de deckblokken (de eerste versie uit de pauze), de afsluitingen (de ADR van het boardmoment) en de rondgang langs de decks.
- **De startpagina toont "Je gebruikt:"** boven "Je maakt:", in de lijst en bij het blok van nu.
- **De LRD toont beide.** Het detailpaneel en de printtabel van deel 8 hebben een regel en een kolom "Eigen werk als invoer".

## Overwogen alternatieven

- **`input` zelf op de startpagina tonen.** Verworpen. Dan blijft het werk van de online omgeving en dat van de lesdag door elkaar staan, en klopt de kolomnaam niet.
- **Niets op de startpagina; de trainer zegt het.** Verworpen. Het draaiboek laat de trainer om 11:45 zeggen waar de top 3 terugkomt (ADR-030). Dat geldt maar voor één blok. Andere ketens, zoals van de businesscase naar het boardmoment, zie je dan nog steeds niet.
- **Ook de online opdrachten op de startpagina tonen.** Niet gedaan. Dan krijgt bijna elk blok een extra regel, en de deelnemers kennen hun online opdrachten al. Het kan later, als de groep erom vraagt.

## Gevolgen

- **De deelnemer ziet de keten.** Bij elk blok staat wat er terugkomt. Een deelnemer die iets mist, ziet dat al vóór het blok begint.
- **Elk nieuw blok vraagt een keuze.** Komt de invoer uit de online omgeving, dan hoort ze in `input`, anders in `uses`. `CLAUDE.md` legt het verschil vast.
- **De startpagina wordt iets langer:** negentien blokken krijgen een regel erbij.
- **ADR-030 blijft gelden.** Daar staat de top 3 nog in `input`; dit besluit verplaatst haar naar `uses`.

## Raakt

Deel 8 (programma: detailpaneel en printtabel); `DATA.days[].blocks[].input` en het nieuwe veld `uses`, in negentien blokken over drie dagen; `materiaal/index.html` (regel "Je gebruikt:"); `CLAUDE.md`; ADR-030.
