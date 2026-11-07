# ADR-003: De LRD als interactieve HTML-pagina in de huisstijl

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-04 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De eerste versie van de LRD was een Markdown-bestand. De trainer wil dat een LRD altijd een dynamisch HTML-document is, met schema's, diagrammen en animaties, in de huisstijl van Business Data Solutions.

## Besluit

De LRD is één HTML-bestand. Alle genummerde onderdelen staan in één databron (het object `DATA`), waaruit tabellen, diagrammen en tellingen worden opgebouwd. De huisstijl komt uit `brand-project/stylebook`. D3, Three.js en Motion laden vanaf een vaste CDN-versie. De Markdown-versie is vervangen. De skill `aiso-building-lrds` is hierop aangepast.

## Overwogen alternatieven

- **Markdown houden.** Geen interactie, en tellingen en verwijzingen moeten met de hand kloppen.
- **Markdown en HTML naast elkaar.** Twee versies lopen uit elkaar.

## Gevolgen

- De keten van leeruitkomst naar eis naar bewijs is zichtbaar en klikbaar.
- Tellingen en de dekkingscontrole rekenen zichzelf uit.
- Zonder internet tonen de diagrammen en tabellen niets; de tekst blijft leesbaar.
- Een wijziging vraagt het bewerken van de databron in JavaScript.

## Raakt

Het hele document; skill `aiso-building-lrds`.
