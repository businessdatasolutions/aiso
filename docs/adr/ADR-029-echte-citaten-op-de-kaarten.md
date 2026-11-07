# ADR-029: Echte citaten en een Wikipedia-link op de kaarten van het startsjabloon

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In het startsjabloon (`materiaal/boards.html`, ADR-027 en ADR-028) kiest de deelnemer leden voor twee boards uit 39 publieke personen. Op een kaart stonden alleen een blik en een typische vraag. De trainer wil dat deelnemers zien wie ze kiezen: een link naar Wikipedia, en uitspraken die laten zien waar de persoon voor staat.

De eerlijkheidsregels zeggen dat wat een board zegt, nooit een citaat van de echte persoon is. Online circuleren bovendien veel valse citaten, juist van mensen als Churchill, Gandhi en Boeddha.

## Besluit

- **Elke kaart krijgt "Wie is dit?":** twee echte citaten met hun bron, en een link naar Wikipedia (Nederlands als dat er is, anders Engels). Josh Woodward heeft geen Wikipedia-artikel. Daar staat zijn auteurspagina bij Google.
- **Alleen controleerbare citaten.** De bron is een boek, een toespraak, een interview of een eigen tekst. Het citaat moet woordelijk in die bron zijn teruggevonden, of in de sectie "Sourced" op Wikiquote staan met bronvermelding. Dat laatste geldt voor vier citaten: twee van Kahneman en twee van Thatcher. Citaatsites tellen niet. Verkeerd toegeschreven en omstreden citaten zijn weggelaten.
- **Geen link naar gescande of geüploade kopieën.** Bij Patton en bij één citaat van Springsteen staat alleen de bronvermelding. Bij Edmondson linkt de bron naar de DOI van het artikel, en bij Ng naar de bewaarde officiële pdf in de Wayback Machine.
- **De citaten staan alleen op de pagina, niet in de skills.** In de skill blijft de regel dat het board geen echte uitspraken nadoet. De typische vraag op de kaart heet "Vraagt: …" en staat niet tussen aanhalingstekens, zodat hij niet als citaat leest.

## Overwogen alternatieven

- **De citaten ook in de skill zetten**, zodat de AI het perspectief beter treft. Verworpen. De AI zou ze kunnen herhalen alsof het board ze uitspreekt, en dat botst met de eerlijkheidsregels.
- **Alleen een Wikipedia-link, geen citaten.** Verworpen. De trainer wil juist zien hoe iemand denkt, en daarvoor is een uitspraak sterker dan een biografie.
- **Citaten van citaatsites.** Verworpen. Juist daar staan de valse toeschrijvingen.

## Gevolgen

- **78 citaten voor 39 personen**, op 7 november 2026 gezocht en gecontroleerd door vier AI-onderzoekers tegelijk. Bij twijfel is een citaat weggelaten. Twee punten zijn daarna apart nagezocht: de zin van Karpathy op zijn blog, en het citaat van Ng in de pdf.
- **Links kunnen verlopen.** De trainer controleert ze in fase 2, net als de andere links.
- **Een nieuw lid in het sjabloon** krijgt pas een kaart met "Wie is dit?" als er volgens dezelfde regels citaten bij zijn gezocht. Eigen leden van deelnemers hebben geen "Wie is dit?".
- **De pagina is zwaarder,** maar de citaten zijn standaard ingeklapt.

## Raakt

Deel 6.3 (eerlijkheidsregels); `materiaal/boards.html` (kaarten, eerlijkheidsregels in stap 6).
