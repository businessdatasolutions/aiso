# ADR-049: Eén tegel per stuk, met de naam van wat erachter staat

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Bij het deckblok van dag 1 (15:15) stonden op de startpagina twee tegels die hetzelfde lege casusdeck openden. De ene ging naar de downloadpagina, de andere naar de kopie in deze repo. De tweede stond er omdat het blok de vragenkaart noemt. ADR-046 eist dan een tegel met "vragenkaart" in de naam, en `scripts/meet-ux.py` meet dat (D3-A). De meting keek of zo'n tegel er was, niet of er al een tegel naar hetzelfde bestand ging. De eerste tegel had het webadres in de naam, en dat liep buiten de tegel.

Bij het blok van 11:00 stonden de tegels "Vragenkaart" en "Vier vragen" naast elkaar. Ze lijken hetzelfde stuk. "Vier vragen" is echter de lespagina van het blok:

1. de vier vragen als taken van leiderschap;
2. weerbarstige vraagstukken;
3. verkennen en benutten;
4. de meerarmige bandiet met de simulator;
5. reële opties en de deur die terug kan;
6. per vraag, met de eigen casus.

Alleen stap 1 staat ook op de vragenkaart. Op dag 2 om 10:45 werkt het blok met stap 5 van dezelfde pagina, maar de tegel opende stap 1.

## Besluit

- **Een blok heeft per stuk één tegel.** Gaan twee tegels naar hetzelfde bestand, dan blijft er één over, met een naam die beide zegt. Bij het deckblok is dat "Leeg casusdeck om te downloaden (dia 1 is je vragenkaart)", naar de downloadpagina (FR-02).
- **Een tegel heet naar wat de deelnemer erachter vindt**, niet naar een begrip uit het ontwerp. Een webadres hoort niet in de naam.
- **De lespagina `vier-vragen.html` heet "Waarom geen plan volstaat"**, net als het blok en de kop van de pagina. Die naam staat op de tegel, op de werkkaart, in de instructie voor de trainer, in de LRD en in de titel van de pagina.
- **Gebruikt een blok één stap van een pagina, dan opent de tegel die stap** en heet hij naar die stap. Op dag 2 om 10:45 is dat "De deur die terug kan", naar `vier-vragen.html#stap-5`. De stappen op de pagina kregen daarvoor een id (`stap-1` tot en met `stap-6`), zodat de link ook zonder JavaScript op de goede stap landt.
- **Een lang woord in een tegel breekt af**, zodat de tekst binnen de tegel blijft.

## Overwogen alternatieven

- **De tegel "Vier vragen" weghalen, omdat de vragenkaart de vragen al heeft.** Verworpen: dan verliezen het blok van 11:00 en het blok van dag 2 om 10:45 hun lesstof. Alleen stap 1 overlapt met de vragenkaart.
- **Stap 1 van de lespagina weghalen.** Niet gekozen. De vragenkaart noemt de vier vragen. Stap 1 legt uit bij welke taak van leiderschap elke vraag hoort.
- **Het bestand hernoemen naar de nieuwe naam.** Verworpen: de deelnemer ziet de bestandsnaam niet. Het draaiboek, de LEESMIJ van de simulator en de voorbeeldcasus noemen het bestand, en de site linkt ernaar. Een nieuwe bestandsnaam breekt links zonder dat de deelnemer er iets aan heeft.
- **De tweede casusdeck-tegel houden en de meting losser maken.** Verworpen: het blok werkt met de vragenkaart, dus de eis klopt. Eén tegel met een naam die beide zegt, voldoet aan de eis en haalt de dubbele keuze weg.

## Gevolgen

- `meet-ux.py` haalt 32 van 32. Een dubbele tegel ziet hij nog steeds niet: de twee casusdeck-tegels gingen naar twee adressen met hetzelfde bestand. Bij een nieuwe tegel kijkt de ontwerper zelf of het stuk er al een heeft.
- Het draaiboek, de LEESMIJ en de voorbeeldcasus noemen de pagina bij haar bestandsnaam `vier-vragen.html`. Dat is materiaal voor de trainer, en de bestandsnaam is eenduidig.

## Raakt

- `materiaal/index.html` (de tegels) en `materiaal/vier-vragen.html` (de titel en de ids van de stappen).
- In `DATA.days`:
  - dag 1 om 11:00: de tegel, de werkkaart en de instructie;
  - dag 1 om 15:15: de tegel;
  - dag 1 om 16:00: de instructie;
  - dag 2 om 10:45: de tegel, de werkkaart en de instructie.
- Deel 6 (hoe je ermee werkt), de lijst met lesmateriaal, de opleveringen van de trainer, een risico en fase 0 van de roadmap.
- ADR-046: aangevuld, niet vervangen.
