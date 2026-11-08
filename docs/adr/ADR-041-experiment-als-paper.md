# ADR-041: Het experiment als wetenschappelijk paper, geschreven door de AI

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Tot versie 0.25 maakte de AI in de lunch van dag 2 een eerste ontwerp van het experiment. Dat noemde de vraag, de vorm, de norm en een referentiewaarde zonder AI. De uitkomst van het experiment kwam op de dia Eerste prioriteit, zonder apart verslag. Dat besloot ADR-034: een verslag was extra thuiswerk.

De trainer wil nu dat de AI het experiment opstelt als wetenschappelijk paper, en later ook de uitwerking. De trainer werkt zelf ook zo in eigen projecten. Eerst schrijft de AI een voorstel met vier delen:

1. de aanleiding, met de koppeling naar het strategische vraagstuk, en de vragen of toetsbare hypotheses;
2. een overzicht van wetenschappelijke literatuur, goede voorbeelden en standpunten van experts;
3. minstens drie ontwerpen voor het experiment, geïnspireerd door de bronnen uit deel 2;
4. een bronnenlijst en verwijzingen in de tekst volgens APA 7.

De goede voorbeelden komen van koplopers: directe concurrenten, of organisaties uit een heel andere sector. De AI zoekt ook in de AI-wiki van de trainer (https://businessdatasolutions.github.io/ai-wiki/). Uit dezelfde bronnen haalt de AI ideeën voor de opzet, de uitvoering en de verwerking van het experiment.

Eerder koos ADR-008 al een kort paper. ADR-009 maakte er een interactieve pagina van, en ADR-034 schrapte het verslag.

## Besluit

- **Het voorstel.** In de lunch van dag 2 schrijft de AI met de onderzoeksfunctie een voorstel in de vorm van een paper (FR-38). Het heeft vier delen:
  - **Aanleiding:** de strategische vraag, de eerste prioriteit, de onderzoeksvraag met hooguit drie deelvragen, en toetsbare hypotheses. Elke hypothese heeft een maat, een norm en een referentiewaarde zonder AI.
  - **Wat we al weten:** onderzoek, koplopers uit de eigen en uit een andere sector, en experts, met ook een kritisch standpunt.
  - **Minstens drie ontwerpen:** elk met de bron die het inspireerde, en een tabel die ze vergelijkt.
  - **Bronnen volgens APA 7:** alleen bronnen die de AI geopend heeft. De rest staat onder "Niet gecontroleerd".
- **Werkplaats 2 begint met het voorstel.** Het duo zoekt één bron op in het origineel. De deelnemer kiest een ontwerp of combineert er twee, en legt de normen vast in het paper, met de datum (FR-20).
- **De uitwerking.** Thuis schrijft de AI in hetzelfde paper de methode, de resultaten, de discussie en de conclusie met het besluit. De normen veranderen niet (FR-21, AC-15).
- **Het deck.** De dia Eerste prioriteit blijft de plek in het deck en vat het paper samen.
- **Een nieuwe lespagina,** `materiaal/experimentpaper.html`. Ze heeft drie prompts: het voorstel, de keuze vastleggen en de uitwerking. Er staat ook een voorbeeld van Voorbeeld BV op, met drie echte bronnen uit de AI-wiki. De tekst van het voorbeeld staat in `materiaal/voorbeeldcasus.md`.
- **De startpagina** toont het materiaal van een pauze als link achter de AI-taak. Dat geldt voor de rij van de pauze en voor de band van werkregel 1.
- **Woordkeus.** In de teksten voor deelnemers staat "koplopers" voor champions. Op de eerste plek staat "champions" er tussen haakjes achter.

## Overwogen alternatieven

- **Alleen de tekst van de AI-taak aanpassen, zonder lespagina.** Verworpen: de opdracht heeft vier delen, zoekplekken en regels voor bronnen. Dat past niet in één regel op de startpagina. Elke deelnemer zou de AI dan een andere opdracht geven.
- **Het paper door de deelnemer laten schrijven, zoals in ADR-008.** Verworpen: dat is het extra thuiswerk waarom ADR-034 het verslag schrapte. Nu schrijft de AI. De deelnemer kiest, controleert en beslist.
- **De uitkomst alleen op de dia, zoals in ADR-034.** Verworpen: een dia draagt geen onderzoeksvraag, geen verwant werk en geen bronnen. Dan is niet te zien waarop het ontwerp steunt.
- **Eén ontwerp in plaats van drie.** Verworpen: bij één ontwerp kiest de AI. Bij drie kiest de deelnemer, en ziet die wat elke vorm kost.

## Gevolgen

- **Een tweede stuk naast het deck.** De KISS-keuze "één product" krijgt die uitzondering, met de reden.
- **Lezen kost tijd in werkplaats 2.** Daarom leest de deelnemer alleen de hypotheses, de tabel met ontwerpen en één bron.
- **Verzonnen bronnen.** Een langer stuk met meer bronnen geeft meer kans op verzonnen bronnen. De prompt en het duo vangen dat op (risico "De AI verzint bronnen of citaten").
- **De onderzoeksfunctie.** De kwaliteit hangt ervan af, en niet elk account heeft die functie. Zonder werkt de prompt in een gewone chat, met minder bronnen.
- **De AI-wiki als bron.** De wiki is openbaar. Een AI die de site niet kan openen, zegt dat, en de deelnemer zoekt er dan zelf in.
- **Testen vóór dag 2.** De trainer test de prompts vóór 26 november in Claude, ChatGPT en Gemini (fase 2).
- **De dagen tussen dag 2 en 3.** Het thuiswerk groeit iets: de deelnemer levert de getallen en leest de uitwerking na.

## Raakt

Deel 1, 5.1 (KISS), 6.5, 7, 8, 10, 11, 12 en 13. FR-06, FR-20, FR-21 en FR-38 (nieuw); AC-14 en AC-15; `DATA.workshops` (dag 2); het programma van dag 2 (12:30, 13:30, 15:00 en 16:00) en dag 3 (9:30 en 10:30); `DATA.value`; de risico's "De AI verzint bronnen of citaten" en "Het experiment tussen dag 2 en 3 loopt vast"; fase 2; de opleverlijst voor de trainer. Ook: `materiaal/experimentpaper.html` (nieuw), `materiaal/index.html`, `materiaal/voorbeeldcasus.md` en `materiaal/draaiboek-bouwstenen.md`. Vervangt ADR-034 deels.
