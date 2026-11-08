# ADR-040: De maquette van een ziekenhuis op dag 1; de opbouw van een agent geparkeerd

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Bij "Wat AI nu kan en niet kan" (dag 1, 10:00) stond een voorbeeld uit de zorg: de publieke pagina over de harness. Die laat zien hoe een agent technisch is opgebouwd. De trainer wil dat onderwerp bewaren voor later, mogelijk voor dag 2. Op die plek wil de trainer de maquette van een ziekenhuis uit de presentatie over AI in de zorg van 10 november 2026. ADR-018 nam die maquette niet over, omdat de cijfers alleen over ziekenhuizen gaan.

De maquette is een 3D-plaat van een ziekenhuis in twaalf stappen. Elke ruimte toont een cijfer uit de AI Monitor Ziekenhuizen 2026 van M&I/Partners (52 ziekenhuizen). Eén stap toont de kern van het blok: gemiddeld 18 AI-toepassingen per ziekenhuis, en één daarvan is opgeschaald. Dat is breed gebruik en zeldzame volwassen inzet in één beeld.

## Besluit

- **De maquette komt in de map `materiaal/`** als één bestand: `materiaal/ziekenhuis.html`. Het blok van 10:00 op dag 1 verwijst ernaar in plaats van naar de pagina over de harness.
- **Gekopieerd, met drie aanpassingen.** Three.js, D3 en motion komen van jsDelivr, in de versies van de LRD (three 0.160.0, d3 7.9.0, motion 11.11.13), en niet uit een build met Vite. Zonder die bibliotheken blijft de tekst per stap werken. De verwijzingen naar de sessie van 10 november zijn eruit: de bloknummers, "vandaag", de agenda van die sessie en de naam van de opdrachtgever. De vraag "Wie zit in de AI-board van jouw ziekenhuis?" wordt "… van jouw organisatie?", en de laatste stap vraagt hoe het in de eigen organisatie zit. Cijfers, paginanummers en de 3D-plaat zijn ongewijzigd.
- **Hoe een agent technisch is opgebouwd, is geparkeerd.** Het punt en de termen harness en contextvenster gaan van dag 1 naar "Achtergrond en reserve voor de trainer" in het draaiboek, met de notitie "mogelijk voor dag 2". De plek is nog niet gekozen; een kandidaat is werkplaats 2, als een experiment een agent test (FR-20). Die keuze krijgt een eigen ADR.
- **Bron.** De AI Monitor Ziekenhuizen 2026 komt in de bronnenlijst van de LRD.

## Overwogen alternatieven

- **Naar de publieke versie van de maquette linken.** Dan toont de les het programma van een andere sessie, met "vandaag" en een agenda die niet klopt. De trainer vroeg om een kopie.
- **De maquette algemeen maken met Voorbeeld BV.** Dat is veel werk, en de kracht zit in echte cijfers van 52 organisaties. Het blijft een voorbeeld uit de zorg, en de trainer zegt dat erbij.
- **De harness op dag 1 laten staan, naast de maquette.** Het blok duurt 45 minuten en heeft al zes punten. De trainer wil de techniek later.

## Gevolgen

- Het blok van 10:00 houdt zes punten: de maquette komt in de plaats van de opbouw van een agent. De cijfers en de maquette krijgen samen 15 minuten, de soorten AI 5.
- Een tweede bron uit een andere sector op dag 1. Het risico "Een voorbeeld uit een andere sector leidt af" blijft staan, met de maquette in de maatregel.
- De cijfers zijn van 2026 en gaan over ziekenhuizen. Elk cijfer dat de trainer noemt, zoekt de trainer eerst op in het pdf-bestand van de monitor (paginanummer staat bij elke stap).
- De kopie loopt los van het origineel. Een correctie in de presentatie over AI in de zorg komt er niet vanzelf in.
- Dag 2 heeft nog geen plek voor de opbouw van een agent. Zolang die er niet is, behandelt de training de harness niet.

## Raakt

Programma dag 1, blok 10:00 (deel 8), FR-26, NFR-08, opleverlijst voor de trainer (deel 10), risico "Een voorbeeld uit een andere sector leidt af" (deel 12), fase 0 (deel 13), bronnen, `materiaal/ziekenhuis.html`, `materiaal/draaiboek-bouwstenen.md`. Vervangt ADR-018 deels: de maquette is alsnog overgenomen.
