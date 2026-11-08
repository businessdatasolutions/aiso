# ADR-023: Een regelboek met werkregels dat de groep zelf schrijft

| | |
|---|---|
| **Status** | Deels vervangen door [ADR-037](ADR-037-kiss-opschoning-vier-vragen.md): alleen werkregel 1 blijft |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In de minor AI in Business werkte de trainer met een regelboek: "De regels die we houden, week na week". Het had zes regels, zoals "Voordat je pauze neemt, zet je altijd AI aan het werk", "Leren gaat boven resultaat" en "Het is nooit af". De trainer wil dat deelnemers in deze training ook nadenken over nieuwe werkregels door AI. Drie of vier regels zijn genoeg. Regel 1 moet vanaf de start gelden.

De LRD had al twee haakjes. De derde vaste vraag van het nabespreken gaat over wat AI vraagt van de organisatie, "aan data, mensen en regels" (FR-05). Het 7S-plan op dag 3 heeft een onderdeel cultuur, met gedeelde waarden en stijl (FR-24).

## Besluit

- **Werkregel 1 vanaf de opening van dag 1** (FR-28): "Voordat je pauze neemt, zet je altijd AI aan het werk." Hij geldt vóór elke pauze, negen keer in drie dagen. Elke pauze heeft in `DATA` een AI-taak (`aiTask`) die het blok erna voorbereidt, zoals een onderzoek met bronnen of een eerste versie van een deckonderdeel. Na de pauze werkt de deelnemer verder met wat de AI maakte.
- **De startpagina toont werkregel 1** in de laatste vijf minuten vóór elke pauze en tijdens de pauze, met de AI-taak erbij (NFR-09). In de lijst staat de taak bij elke pauze.
- **Werkregel 2 tot en met 4 komen van de groep** (FR-29). In de laatste vijf minuten van het nabespreken stelt elk duo een werkregel voor, vanuit de derde vaste vraag, en de groep kiest er één. De trainer heeft de andere regels uit de minor als reserve.
- **Het regelboek staat in `DATA.rules`.** Deel 6.2 toont het met vier plekken. De trainer vult werkregel 2 tot en met 4 in na elke lesdag.
- **Naar het eigen team op dag 3.** Bij cultuur in het transformatieplan schrijft elke deelnemer één of twee werkregels voor het eigen team, met het regelboek als voorbeeld (FR-24, AC-16).

## Overwogen alternatieven

- **De trainer brengt elke lesdag een regel uit de minor in.** Voorspelbaar, maar de deelnemers bedenken dan zelf geen werkregel. Dat was juist het doel.
- **De groep schrijft alle werkregels in één ronde op dag 3.** Dan komt de werkregel los van de ervaring van die dag, en groeit het regelboek niet mee met de training.
- **Zes regels van de trainer bij de start.** Zoveel regels onthoudt niemand op de eerste ochtend (KISS-keuze in deel 5.1).
- **Alleen het regelboek van de groep, zonder vertaling naar het eigen team.** Dan blijft het een spelregel van de training en landt het niet in de integrale opdracht.
- **Alleen werkregel 1 op de startpagina, zonder AI-taak.** Eenvoudiger, maar zonder concrete taak blijft de regel een grap. Zie het risico in deel 12.
- **Niets op de startpagina; de trainer zegt de regel elke keer.** Dat kost negen keer aandacht van de trainer, en het werkt niet als een collega de lesdag geeft (NFR-07).

## Gevolgen

- Het nabespreken houdt 20 minuten over voor de drie vragen en het werkplaatslog. Het ritme van de werkplaats (FR-04) blijft 15, 50 en 25 minuten.
- Negen AI-taken moeten vóór de lesdagen getest worden: is elke taak binnen zijn pauze klaar (fase 0)?
- De startpagina leest `rules` en `aiTask` uit de LRD. Een LRD zonder die velden toont geen werkregel; de pagina werkt verder.
- Twee nieuwe risico's: werkregel 1 blijft een grap, en de groep komt in vijf minuten niet tot een werkregel.
- Het woord "regel" heeft in de LRD al de betekenis "regel in het werkplaatslog" (FR-05, AC-02). Het regelboek spreekt daarom steeds van "werkregel".

## Raakt

Deel 2 (axioma 2.3 en 2.4), deel 5.1 (KISS) en 5.2 (PAMS: Social, KISS voor de begeleider), deel 6.2 (nabespreken, kaart "Het regelboek"), deel 8 (opening dag 1, de drie werkplaatsen, transformatieplan en afsluiting dag 3, AI-taak bij elke pauze), FR-24, FR-28, FR-29, NFR-09, AC-16, AC-19, de opleverlijsten (deel 10), twee risico's (deel 12), fase 0 (deel 13), `materiaal/index.html`, `materiaal/draaiboek-bouwstenen.md`.
