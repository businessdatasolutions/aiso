# ADR-021: Lesmateriaal in één map, met de voorbeeldcasus Voorbeeld BV en een startpagina per lesdag

| | |
|---|---|
| **Status** | Aanvaard; de voorbeeldcasus zelf is een concept |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

NFR-04 vraagt alle materialen op één plek, en NFR-06 een timer die de groep kan zien. De voorbeeldcasus voor de terugvaloptie (FR-07) bestond nog niet: deel 6.2 noemde alleen "een fictieve middelgrote organisatie". De sessie over AI in de zorg had pagina's in dezelfde huisstijl, zoals een groeimodel, vier kennisvormen naast elkaar, een proces als swimlane en een startpagina met tijdlijn. Hun inhoud ging over incidentmeldingen in een ziekenhuis.

## Besluit

- **Eén map.** Alle lesmateriaal staat in `materiaal/` (NFR-09).
- **Eén voorbeeldcasus.** `materiaal/voorbeeldcasus.md` beschrijft Voorbeeld BV: een fictieve dienstverlener met ongeveer 400 medewerkers die klantvragen en klachten afhandelt. Het bestand bevat het proces met vier routes, de vijf plekken waar AI kan helpen, de klacht voor "Mens tegen agent" en de teksten voor de lespagina's. De naam is bewust een plaatshouder, zodat hij naar geen echte organisatie wijst (ADR-016).
- **Drie lespagina's,** algemeen gemaakt uit de zorgsessie: `groeimodel.html` (ADR-019), `kennisvormen.html` en `kansenkaart.html` (FR-27). Ze laden D3 en Motion van jsDelivr, met dezelfde versies als de LRD, en tonen hun inhoud ook als een bibliotheek niet laadt.
- **Een startpagina per lesdag,** `materiaal/index.html`. Die leest het programma uit `DATA` in de LRD, zodat het programma op één plek staat. Blokken krijgen een veld `materials` met de links naar hun materiaal; het detailpaneel in deel 8 toont die ook. De startpagina heeft een tijdlijn en een afteller per blok (NFR-06).
- De publieke pagina's van de zorgsessie gebruikt de trainer alleen ter illustratie op dag 1, met die herkomst erbij.

## Overwogen alternatieven

- **De zorgpagina's gebruiken zoals ze zijn.** Gratis, maar het gesprek gaat dan over ziekenhuizen.
- **Het programma in een apart databestand, voor de LRD en de startpagina.** Dan is de LRD niet meer één losse pagina, en werkt de publicatie als artifact anders (ADR-003, ADR-013).
- **Per pagina een eigen voorbeeld.** Elke pagina vraagt dan eigen uitleg, en ze verwijzen niet naar elkaar.

## Gevolgen

- De startpagina werkt alleen via een lokale server (Live Server of `python3 -m http.server`), niet via `file://`.
- Een wijziging in de voorbeeldcasus moet met de hand naar de drie lespagina's. Het bestand zegt dat bovenaan.
- `materiaal/` gaat niet mee met het artifact. Links ernaar worden platte tekst, net als de andere lokale mappen; de lekcheck meldt ze (ADR-022).
- Alle cijfers van Voorbeeld BV zijn verzonnen, en de pagina's zeggen dat.
- Twee nieuwe risico's: een voorbeeld uit een andere sector leidt af, en een lespagina laadt niet in de zaal.

## Raakt

Deel 5.2 (PAMS), deel 6.2 (terugvaloptie), deel 8 (detailpaneel, `materials`), NFR-09, FR-26, FR-27, de opleverlijst van de trainer (deel 10), risico's (deel 12), projectdocumenten, `materiaal/`.
