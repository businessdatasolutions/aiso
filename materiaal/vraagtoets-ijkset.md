# Vraagtoets: de ijkset voor de trainer

- **Status:** concept (ADR-039). Trainermateriaal: niet uitdelen.
- **Doel:** vóór dag 1 nagaan of de prompt van `vraagtoets.html` in Claude, ChatGPT en Gemini dezelfde uitkomst geeft als de trainer (FR-37).
- **Wanneer:** in fase 0, vóór 12 november. Opnieuw doen na elke wijziging van de prompt of de criteria.

Alle organisaties op deze pagina zijn verzonnen. Een gelijkenis met een echte organisatie is toeval.

## De norm, vooraf vastgelegd

- Per model geeft de AI bij **minstens acht van de negen vragen dezelfde uitkomst** als de trainer: operationeel, nog geen keuze of strategisch.
- Een uitkomst telt alleen als goed als de woorden die de AI aanhaalt, letterlijk in de vraag staan.
- Haalt een model de norm niet, dan scherpt de trainer de prompt aan en doet alle negen vragen opnieuw. Lukt het dan nog niet, dan vervalt de AI-stap voor dat model. De trainer zegt dat bij de start van de vraagtoets, en de deelnemer toetst samen met het duo.

## Zo voer je de ijking uit

1. Open `vraagtoets.html` en laat de definitie staan zoals de trainer die voorstelt. Laat "Wat de groep scherper maakte" leeg.
2. Vul in stap 3 de vraag in, kopieer de prompt en plak hem in een **nieuwe chat**, zonder eerdere berichten.
3. Noteer de scores en de uitkomst van de AI in de tabel hieronder. Noteer ook de naam en de versie van het model.
4. Doe dat voor alle negen vragen, in Claude, ChatGPT en Gemini. Gebruik ook een reserve-account op Gemini (NFR-03).

## De negen vragen

| # | Organisatie (verzonnen) | Vraag | Omgeving | Positie | Keuze | Uitkomst van de trainer |
|---|---|---|---|---|---|---|
| 1 | Voorbeeld BV, installateur | Hoe handelen we klachten sneller en beter af, en leren we ervan? | 0 | 0 | 0 | Operationeel |
| 2 | Voorbeeld BV, installateur | Hoe handelen we klachten sneller af dan de concurrent? | 1 | 0 | 0 | Operationeel (het twijfelgeval) |
| 3 | Bakkerij Voorbeeld, 30 winkels | Hoe voorspellen we met AI beter hoeveel brood elke winkel per dag nodig heeft? | 0 | 0 | 0 | Operationeel |
| 4 | Fietsenketen Voorbeeld, 12 winkels | Hoe blijven we met AI relevant voor onze klanten? | 1 | 2 | 0 | Nog geen keuze |
| 5 | Uitgeverij Voorbeeld, vakbladen | Hoe zetten we AI in om onze positie als marktleider te versterken? | 0 | 2 | 0 | Nog geen keuze |
| 6 | Fietsenketen Voorbeeld, afdeling Marketing | Wat wordt de rol van onze afdeling, nu AI zelf campagnes kan maken? | 2 | 1 | 0 | Nog geen keuze |
| 7 | Voorbeeld BV, installateur | Blijven we het eerste aanspreekpunt van de klant, nu installaties hun storingen zelf aan de fabrikant melden? Of worden we de vaste installateur van de fabrikanten? | 2 | 2 | 2 | Strategisch |
| 8 | Uitgeverij Voorbeeld, vakbladen | Vakmensen stellen hun vakvragen steeds vaker aan een AI-assistent. Blijven we een uitgever van bladen, of worden we de bron waar die assistenten hun kennis vandaan halen? | 2 | 2 | 2 | Strategisch |
| 9 | Vertaalbureau Voorbeeld | Nu AI een goede eerste vertaling maakt: verkopen we nog vertalingen? Of verkopen we de zekerheid dat een juridische tekst klopt, aan minder klanten tegen een hogere prijs? | 2 | 2 | 2 | Strategisch |

**Waarom deze negen.** Vraag 1 tot en met 3 zijn operationeel: ze gaan over hoe een bestaand proces loopt. Vraag 2 is het twijfelgeval uit de oefening. Vraag 4 tot en met 6 zijn de vragen die deelnemers vaak meenemen: ze klinken strategisch, maar niets valt af. Vraag 6 ligt op het niveau van een afdeling, daarom Positie 1. Vraag 7 tot en met 9 noemen een concrete verandering, en elk antwoord laat iets.

## Resultaat van de ijking

Datum: …

| # | Uitkomst van de trainer | Claude (model: …) | ChatGPT (model: …) | Gemini (model: …) |
|---|---|---|---|---|
| 1 | Operationeel | | | |
| 2 | Operationeel | | | |
| 3 | Operationeel | | | |
| 4 | Nog geen keuze | | | |
| 5 | Nog geen keuze | | | |
| 6 | Nog geen keuze | | | |
| 7 | Strategisch | | | |
| 8 | Strategisch | | | |
| 9 | Strategisch | | | |
| | **Gelijk (norm: 8 van 9)** | … | … | … |

**Besluit per model:** de AI-stap gaat door, of vervalt. Bij een aangescherpte prompt: wat er veranderde, en de datum van de tweede ronde.
