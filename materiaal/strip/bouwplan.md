# Bouwplan: de strip over de training

- **Wat:** een strip die uitlegt hoe de drie lesdagen werken.
- **Lezer:** een deelnemer die zich heeft ingeschreven en dag 1 nog voor zich heeft.
- **Volgorde van de boodschap:** de Golden Circle van Sinek: eerst waarom, dan hoe, dan wat.
- **Inhoud van de strip:** [scenario.md](scenario.md) (stap 1 tot en met 5), [script.md](script.md) (stap 6), [figurenblad.html](figurenblad.html) (stap 7), [index.html](index.html) (de leesversie van de strip), [strip.html](strip.html) (de werkversie met de schetsen) en [prompts.md](prompts.md) (de beelden). Dit bestand houdt alleen de stappen en de stand bij.

## Stappen

Stap 1 tot en met 6 zijn tekst en kosten weinig om te veranderen. Vanaf stap 7 kost elke wijziging tekenwerk. Ga daarom pas naar stap 7 als de tekst vaststaat.

| Stap | Wat | Klaar als | Stand |
|---|---|---|---|
| 1 | Opdracht: lezer, vorm en de drie gedachten | De drie gedachten staan in volgorde in het scenario | Klaar |
| 2 | Het waarom vaststellen | Witek heeft de zin goedgekeurd of herschreven | Goedgekeurd op 24-11-2026 |
| 3 | Inhoud kiezen per ring | Elk plaatje heeft één gedachte, 9 tot 12 in totaal | Klaar |
| 4 | Concept en verteller | Hoofdpersoon, bijfiguren en het terugkerende beeld staan vast | Klaar |
| 5 | Scèneoverzicht | Eén regel per plaatje, nog zonder tekst in ballonnen | Klaar |
| 6 | Script | Per plaatje: wat we zien, het bijschrift en de tekst, hooguit 25 woorden per ballon; tekst geredigeerd | Goedgekeurd op 24-11-2026 |
| 7 | Figuren en stijl | Elke figuur van voren en van opzij, met drie gezichtsuitdrukkingen; kleuren, lijn en letter vastgelegd | Klaar op 24-11-2026: klare lijn, naar het karakterblad uit Gemini |
| 8 | Schetsen | De hele strip klein en ruw, met de tekst erin; het plaatje van het waarom is het grootst | Klaar: de schetsen staan in [strip.html](strip.html) (`?schets=1`) en dienen als opstelling voor de beelden |
| 9 | Proeflezen | Iemand die de training niet kent vertelt de strip na: eerst het waarom, en weet wat hij meeneemt | Kan nu, met de strip in [strip.html](strip.html) |
| 10 | Beelden maken | Per plaatje een beeld uit de beeldgenerator in de map `beeld/`, met de tekst erin; elke tekst is letter voor letter met het script vergeleken | Klaar op 24-11-2026: twaalf beelden, de tekst klopt in alle twaalf. Lichte kopieën van 1280 breed staan in `beeld/web/` (samen 3 MB) |
| 11 | Controleren en plaatsen | Gelezen op een telefoon, tekst nagekeken, lekcontrole zonder melding | Geplaatst op 24-11-2026 als `materiaal/strip/` op de site (FR-43, ADR-068, LRD 0.54) |

## Open besluiten

| Besluit | Voorstel | Nodig vóór stap |
|---|---|---|
| Vorm | Eén kolom van plaatjes onder elkaar, 640 breed, gemaakt voor een telefoon. Geen brede plaatjes: die worden op een telefoon onleesbaar. Plaatje 8 en 11 hebben twee helften onder elkaar. Via afdrukken een PDF | 9 |
| Tekenwijze | Gekozen op 24-11-2026: de beelden komen uit een beeldgenerator, in de klare lijn van [beeld/referentie-figuren.jpg](beeld/referentie-figuren.jpg), met de tekst in het beeld. De schets uit `strip.html?schets=1` gaat mee als opstelling. De tekst staat ook in de beschrijving van elk beeld, voor schermlezers | 10 |
| Plek in het ontwerp | Besloten op 24-11-2026: de strip is lesmateriaal vóór dag 1, met FR-43 en ADR-068 | 11 |
| Data in de strip | De data staan alleen in het kader onder de strip, zodat een volgende groep één plek hoeft aan te passen | 6 |

## Regels die voor de strip gelden

- De hoofdpersoon en alle bijfiguren zijn verzonnen. Geen figuur lijkt op een deelnemer, ook niet als mengvorm (ADR-016, ADR-017).
- De casus in de strip is Voorbeeld BV uit [voorbeeldcasus.md](../voorbeeldcasus.md).
- De tekst gebruikt de woorden van de werkkaarten: geen codes, geen namen van methoden.
- De tekst in een beeld is letter voor letter de tekst uit het script. Een beeld met een fout gaat niet de strip in.
- Een wijziging in de tekst begint in het script en kost een nieuw beeld.
- De signaalkleur staat alleen op de trui van Noor en op de voortgang. De rest van het beeld heeft gedempte, natuurlijke kleuren.
