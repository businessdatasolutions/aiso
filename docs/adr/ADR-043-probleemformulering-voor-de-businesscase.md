# ADR-043: Eerst het probleem: probleemformulering vóór de businesscase

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De businesscase op dag 2 begon bij het knelpunt op de kansenkaart (FR-14, FR-27). Een knelpunt komt uit de pitch, en die gaat vaak al over een oplossing. Wie met AI begint, begint ook vaak bij de oplossing: "we willen een chatbot". Dan toetst de businesscase de oplossing en niet het probleem, en een route zonder AI blijft buiten beeld.

De trainer wil de probleemformulering een vaste plek geven in de businesscase. Daarvoor gebruikt hij de play "Problem framing" uit het Team Playbook van Atlassian, en het template dat erbij hoort. De play heeft drie stappen:

1. Zeg dat het doel is het probleem te begrijpen, niet op te lossen (2 minuten).
2. Verzamel ideeën in vier vakken: wie, wat, waar en waarom (10 minuten).
3. Schrijf één probleemstelling vanuit wie er last van heeft (10 minuten).

Vooraf stuurt de begeleider de gegevens die erbij horen.

De play en het template verschillen bij het vak Waarom. In de play gaat het over de impact: waarom is het de moeite waard om op te lossen, en wat gebeurt er als we niets doen? In het template gaat het over de oorzaak: waarom gebeurt dit, denken we? De probleemstelling in het template eindigt met "omdat …".

## Besluit

- **Plaats.** De probleemformulering opent het blok om 11:30 op dag 2, dat nu "Eerst het probleem, dan de businesscase" heet (FR-39). Het blok blijft een uur: 15 minuten probleemformulering, 20 minuten kansenkaart en 25 minuten businesscase.
- **De voorbereiding is werkregel 1.** De AI-taak van 10:30 wordt onderzoek naar het knelpunt langs de vier vragen, met de vragen van het comité erbij. Een oplossing zoekt de AI nog niet. Dat is de stap "stuur vooraf de gegevens" uit de play.
- **Het kader.** Vier vakken, zoals in het template:
  - **Wie** heeft last van het probleem, en hoe weten we dat?
  - **Wat** zijn de signalen?
  - **Waar en wanneer** speelt het, en wanneer niet?
  - **Waarom** gebeurt het, denken we, en wat als er niets verandert?

  Het vak Waarom neemt beide betekenissen mee: de oorzaak uit het template en de impact uit de play. Een businesscase heeft ze allebei nodig. De oorzaak wordt een van de twee aannames, de impact de waarde.
- **De probleemstelling.** Eén zin in vijf delen: wie, wat, waar en wanneer, omdat …, en "als er niets verandert, …". Ze noemt geen oplossing, en dus ook geen AI.
- **De toets van het duo.** Staat er een oplossing in? Is de zin geschreven vanuit wie er last van heeft? Heeft elke bewering een signaal?
- **De businesscase opent met de probleemstelling** (FR-14). Het "omdat" staat bij de twee aannames. AC-04 meet het.
- **Voorlopig.** De probleemstelling is een antwoord op een weerbarstig vraagstuk (deel 2.1). In de opening van dag 3 kijkt de deelnemer of ze na het experiment nog klopt.
- **Een nieuwe lespagina**, `materiaal/probleemformulering.html`:
  - het kader van Voorbeeld BV, met een eerste versie die een oplossing in vermomming was;
  - het lege kader, waarin de probleemstelling zich opbouwt met dezelfde strepen per deel;
  - de prompt voor het onderzoek van 10:30;
  - een prompt voor de businesscase met de elementen uit FR-14.

  De tekst van het voorbeeld staat in `materiaal/voorbeeldcasus.md`.

## Overwogen alternatieven

- **Een eigen blok van 30 minuten, zoals in de play.** Verworpen: dat gaat ten koste van de reële opties om 10:45 of van de werkplaats. De AI doet de voorbereiding al in de pauze, zodat 15 minuten volstaan voor de vakken en de zin.
- **De probleemformulering vóór de pitch, of als huiswerk na dag 1.** Verworpen: de pitch komt uit de online omgeving van S&N, en die valt buiten dit ontwerp (ADR-001). Nieuw huiswerk tussen dag 1 en 2 legt een tweede spoor naast de vier vragen.
- **De AI de vier vakken laten vullen.** Verworpen: het vullen is het denkwerk dat de deelnemer moet doen. De AI levert het materiaal, de deelnemer kiest wat erin komt.
- **Een andere techniek, zoals een visgraatdiagram of vijf keer waarom.** Verworpen: die zoeken vooral de oorzaak. Het kader van Atlassian vraagt ook wie er last van heeft en wanneer het niet speelt. Het levert in een kwartier één zin die de businesscase kan dragen.
- **Het vak Waarom alleen als oorzaak, zoals in het template.** Verworpen: dan mist de businesscase het gevolg van niets doen, en dat is de basis voor de waarde.
- **Het lege kader op papier, met briefjes zoals op een whiteboard.** Niet gekozen: de probleemstelling moet toch getypt in de prompt voor de businesscase. De lespagina toont het kader in dezelfde vorm als het template.

## Gevolgen

- **Een strak uur om 11:30.** Daarom krijgt de businesscase een prompt op de lespagina. Is de businesscase om 12:30 niet af, dan maakt de AI hem af in de lunch, vóór het voorstel. De trainer loopt het blok in fase 2 een keer door op tijd. Daarvoor is een nieuw risico opgenomen.
- **Een tweede nieuw risico:** de probleemstelling is een oplossing in vermomming. De regel, het voorbeeld en de toets van het duo vangen dat op.
- **De pauze van 10:30 krijgt een prompt** op de lespagina. De startpagina linkt ernaar.
- **Het casusdeck verandert niet.** Het vak "Probleem op de kansenkaart" op de dia Eerste prioriteit vraagt al welk probleem je aanpakt en waar het in de keten zit.
- **Testen vóór dag 2.** De prompts gaan in fase 2 langs Claude, ChatGPT en Gemini, samen met die van het experimentpaper.

## Raakt

Deel 6.5 (nieuwe kaart "Eerst het probleem"), 7, 8, 10, 11, 12 en 13, en de bronnen. FR-39 (nieuw); FR-14 en FR-27; AC-04; `DATA.value` (de pijn over de businesscase); het programma van dag 2 (10:30 en 11:30) en dag 3 (9:30); twee nieuwe risico's; fase 2; de opleverlijst voor de trainer. Ook: `materiaal/probleemformulering.html` (nieuw), `materiaal/voorbeeldcasus.md` en `materiaal/draaiboek-bouwstenen.md`.
