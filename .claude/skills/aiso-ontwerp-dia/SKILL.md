---
name: aiso-ontwerp-dia
description: Gebruik bij het schrijven of aanpassen van dia's voor een lesdag of training — elk deck dat een trainer presenteert — en zodra een dia meer draagt dan een luisteraar in één oogopslag opneemt. Triggers zijn "maak de dia's", "voeg een dia toe", "deze dia is te vol", "korter", "te veel tekst op het scherm", of een dia waarvan een deelnemer de tekst leest in plaats van luistert.
argument-hint: "pad-naar-deck.html [dianummers]"
---

# De dia draagt het bewijs, de trainer draagt het verhaal

## De kernregel

**Een deelnemer leest of luistert, nooit allebei.** Een zaal die zinnen op een dia ziet, leest ze — en
zolang ze lezen, horen ze de trainer niet. Dus draagt een dia alleen wat de stem niet kan
dragen: de ene zin die blijft hangen, een getal, een citaat, een naam, een structuur, een
tekening. Alles wat je kunt zéggen, zeg je — en het staat niet op het scherm. De volledige tekst
staat in de sprekersnotities, en dat is ook waar de deelnemer hem later terugvindt in de pdf.

Dit is de bewering-en-bewijsstructuur: de kop is de bewering, het lijf is het bewijs ervoor, en
het betoog is van de trainer.

## Wat een dia draagt

| Onderdeel | Regel |
|---|---|
| Kop (`h2`) | Eén zin die een deelnemer kan navertellen; hooguit twaalf woorden. Een label (*De casus*) markeert een blok; een inhoudsdia stelt iets. |
| Lijf | Hooguit 40 woorden lopende tekst. Fragmenten, geen volzinnen. Hooguit drie opsommingspunten van één regel. |
| Een zin, als het er een moet zijn | Hooguit 20 woorden — D1 voor geprojecteerde tekst, want de lezer krijgt één oogopslag. |
| Bewijs | Eén ding: een getal, een citaat, een naam, een tekening, een rij tegels. Nooit een alinea die het uitlegt. |
| Tekening (`svg`) | Aslabels en kernwoorden tellen anders dan lopende tekst: ze worden bekeken, niet gelezen. Het script houdt ze in een aparte kolom. |
| Detail | Naar de sprekersnotities, of naar het bronmateriaal van de lesdag. |
| Regie | Nooit op de dia. Wat de trainer moet dóen staat in de sprekersnotities (`div.notes`) of in het draaiboek, het script van de trainer per blok — zie „Geen regieaanwijzingen op een dia" hieronder. |

## Geen regieaanwijzingen op een dia

Wat de trainer moet dóen hoort in de sprekersnotities of in het draaiboek, niet op het scherm.
„Cluster hardop terwijl je leest", „sluiten doe je op de volgende dia", „laat eerst drie
antwoorden komen" — dat leest de zaal mee, en het maakt van een dia een spiekbriefje.

Wat wél op een dia mag: alles wat de deelnemer aangaat. Een opdracht aan de zaal („typ je
schatting in", „overleg met je buur"), een aankondiging van de trainer aan de zaal („ik tel af",
„ik laat de spreiding zien naast het echte cijfer"), en natuurlijk de inhoud zelf. Het verschil
is de geadresseerde: spreek je de zaal aan of jezelf.

## Twee toetsen

**De spookdeck-toets.** Lees alleen de koppen, van boven naar beneden. Vertellen ze samen het
verhaal van het blok of de lesdag, dan houdt het deck. Een kop die alleen een label is
(*Structuur*, *Mensen*) betekent dat de dia nog niet weet waarvoor hij er staat.

**De luistertoets.** Zeg per dia hardop wat je erover gaat vertellen. Alles wat je zojuist zei en
óók op de dia staat, is dubbel: haal het van de dia. Alles wat je nooit hardop zou zeggen — de
exacte formulering van een opdracht, een getal, een citaat, een tekening — is precies waarom de
dia bestaat.

## Werkwijze

1. **Schrijf eerst het spoor van de trainer.** Eén regel per dia: wat je zegt. In het deck is dat
   de sprekersnotitie, en in het draaiboek de regel bij het blok; die staat er meestal al.
2. **Bepaal per regel wat de luisteraar moet zíen** om je te kunnen volgen. Dat is de dia.
3. **Draai de teller.** Hij geeft per dia de woorden, de figuurtekst apart, de opsommingspunten,
   de langste zin en de koplengte, en markeert wat over de streep gaat; afsluitcode 1 betekent
   dat er iets over is.

   ```bash
   python3 .claude/skills/aiso-ontwerp-dia/scripts/diawoorden.py pad/naar/deck.html
   python3 .claude/skills/aiso-ontwerp-dia/scripts/diawoorden.py pad/naar/deck.html --zonder-figuur
   python3 .claude/skills/aiso-ontwerp-dia/scripts/diawoorden.py deck.html --max-woorden 40 --max-opsomming 3 --max-zin 20
   PYTHONDONTWRITEBYTECODE=1 python3 -m pytest .claude/skills/aiso-ontwerp-dia/scripts -q -p no:cacheprovider   # 5 tests
   ```

4. **Draai de prozacontrole** op dezelfde dia's, zodat losse kaartjes niet als één lange zin
   gelezen worden en de notities buiten schot blijven:

   ```bash
   python3 .claude/skills/aiso-schrap-ai-taal/scripts/aitaal.py pad/naar/deck.html \
           --negeer-html-klasse notes --blok-tag span --codes A1,D1
   ```

5. **Render en kijk.** Een dia die als een muur tekst leest, zie je op het scherm en niet in de
   broncode. Open het deck via een lokale server (`python3 -m http.server 8765`; Playwright
   blokkeert `file://`) en bekijk elke dia op projectieformaat, of maak er per dia een
   schermafdruk van.
6. **Wat je schrapt, verplaats je.** Draagt een geschrapte zin een feit dat nergens anders staat,
   dan gaat hij naar de sprekersnotities van diezelfde dia — niet terug naar het scherm, en niet
   weg.

## Wat de streep betekent

Gemeten op drie eerdere presentatiedecks (16 september 2026), zonder figuurtekst en zonder
notities:

| Deck | Dia's | Gemiddeld | Mediaan | Zwaarste | ≤ 40 woorden |
|---|---|---|---|---|---|
| A | 32 | 63 | 58 | 115 (dia 14) | 10 |
| B | 35 | 50 | 53 | 116 (dia 15) | 10 |
| C | 40 | 63 | 65 | 120 (dia 1) | 10 |

Veertig woorden is dus geen poortje dat een gewoon deck vandaag haalt, en zo moet je de uitvoer
ook niet lezen: **gebruik de teller als rangschikking, niet als stoplicht.** De zwaarste vijf
dia's van een deck zijn het werk; de dia van 45 woorden is het niet.

Let op het verschil met een beoordelingslat. Een lat waarop een deck beoordeeld wordt — zoals
gemiddeld 110 en maximaal 170 woorden per dia, met de figuurtekst gewoon meegeteld — is de
ondergrens; deze skill is de scherpere blik waarmee je het beter maakt. Een deck kan zo'n lat
ruim halen en hier alsnog twintig dia's oplichten — dat is geen tegenspraak, dat is het verschil
tussen voldoende en goed. De didactische beoordeling van een deck als geheel loopt via
`aiso-beoordeel-onderwijsontwerp`.

## Het deckcontract

De teller gaat uit van dit contract. Houd een deck van een lesdag eraan, of pas de teller aan.

- Een deck is één HTML-bestand, met één `<section class="slide">` per dia.
- Een dia heeft `data-part` en `data-title`, dan een `p.eyebrow`, dan de kop (`h2`, of `h1` op de
  titeldia), dan het lijf, en sluit af met `div.notes`.
- De teller laat notities, eyebrow en de kop zelf buiten de woordentelling, en houdt `svg`-tekst
  in een aparte kolom.
- Een dia invoegen verschuift alle dianummers erna — werk elke verwijzing naar een dianummer bij
  (draaiboek, sprekersnotities) en draai een eerdere beoordeling opnieuw.
- Een pptx of pdf die uit het deck gemaakt is, is een afgeleide; je bewerkt hem nooit met de hand.

## Waar dit vandaan komt, en waar het afwijkt

- **De assertion–evidence structure van Michael Alley** (Penn State): een kop die de boodschap van de
  dia uitspreekt, gedragen door visueel bewijs; opsommingen horen er niet. Wij houden
  opsommingen, hooguit drie en alleen als fragment, omdat een deck ook als pdf wordt nagelezen.
- **De `academic-pptx`-skill** (Gabberflast): actietitels als hele zin, ongeveer 40 woorden lijf
  per inhoudsdia, één inzicht per dia, en de spookdeck-toets — „de spreker draagt het betoog, de
  dia draagt het bewijs". De 40 woorden en die toets zijn overgenomen zoals ze zijn.
- **De `pptx`-skill van Anthropic**: elke dia heeft een visueel element, want „text-only slides are
  forgettable", en notities horen in het notitieveld, nooit in een tekstvak.
- **De projectskill `aiso-schrap-ai-taal`**: D1 op 20 woorden voor geprojecteerde tekst, en
  `--blok-tag` zodat een deck dia voor dia gemeten wordt.

Deze skill is de Nederlandse bewerking (16 sep 2026) van een Engelstalige `slide-deck`-skill,
met de teller op het deckcontract hierboven gezet.
