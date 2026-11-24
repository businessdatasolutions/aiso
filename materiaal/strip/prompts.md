# Prompts voor de beelden van de strip

- **Status:** concept. De beelden komen uit een beeldgenerator, met de tekst erin. [strip.html](strip.html) toont ze; de tekst komt uit het [script](script.md).
- **Stijl:** de klare lijn van het referentiebeeld [beeld/referentie-figuren.jpg](beeld/referentie-figuren.jpg).
- **Taal:** de prompts zijn Engels, omdat beeldgeneratoren daar het best op reageren. De tekst in het beeld is Nederlands.
- **Alles is verzonnen.** Geen prompt beschrijft een deelnemer of een bestaande organisatie.

## Zo werk je

1. Open `strip.html?schets=1` en maak een schermafbeelding van de schets van het plaatje, zonder het casusdeck eronder.
2. Geef de generator drie dingen: het referentiebeeld voor de figuren, de schets voor de opstelling en de plek van de tekst, en de prompt.
3. De prompt bestaat uit het blok Stijl, het blok Figuren en de prompt van het plaatje. Daarin staat de tekst nog eens letterlijk, zodat de generator hem niet van de schets hoeft te lezen.
4. Bewaar het beeld in de map `beeld/` als `plaatje1.jpeg`, `plaatje2.jpeg` en zo verder. De pagina vervangt de schets dan door het beeld.
5. Plaatje 1, 2 en 12 spelen in dezelfde vergaderkamer, en plaatje 6 en 7 aan dezelfde tafel. Geef het eerste goedgekeurde beeld van die plek mee bij de andere.

## Controleer elk beeld

- De tekst is letter voor letter gelijk aan de tekst in de prompt. Let op lange woorden, op "AI" en op cijfers.
- Er staat geen andere tekst in het beeld.
- De geelgroene kleur staat alleen op de trui van Noor.
- Noor, het duo en de trainer lijken op het referentiebeeld: kapsel, bril, baard en trui.
- De eerste spreker staat links, en de ballon van de eerste spreker staat het hoogst.
- Het robotje heeft lichte ogen, geen turquoise.
- Het casusdeck staat er niet in. De pagina zet het onder het plaatje.

Staat er na twee pogingen nog een fout in de tekst, dan kan de pagina de tekst over een beeld zonder tekst leggen. Zet het nummer van dat plaatje dan in `TEKST_EROVER` in `strip.html`.

## Blok Stijl

```text
One comic panel in European ligne claire style (clear line): clean, uniform black outlines of constant width, flat colours without shading, gradients or hatching, precise but simple backgrounds. Muted natural palette: off-white walls, warm wood, soft grey, green plants, red-brown brick seen through tall industrial windows. The only bright colour is the yellow-green sweater of the main character. Calm daylight, friendly and professional tone. A thin black panel border with slightly rounded corners on a white page.

Follow the attached layout sketch for the composition, the position of the figures and the position of every text element. The sketch is a rough layout only: do not copy its drawing style.

Lettering: clean modern sans-serif, black, sentence case, well spaced. Speech balloons are white with a black outline and a pointed tail to the speaker. Thought balloons have a dashed outline and small bubbles. Narration captions are cream boxes with a thin black outline. Title captions are black boxes with white capital letters. Reproduce the Dutch texts below exactly, letter for letter, with the same punctuation. Do not translate, shorten or add any text. No other text, numbers or logos anywhere in the image.
```

## Blok Figuren

```text
Recurring characters, exactly as in the attached reference image:
- NOOR, the main character: a woman in her late thirties with a black chin-length bob, a yellow-green sweater and dark trousers. Nobody else wears yellow-green.
- THE PARTNER: a man with brown curly hair and round glasses, a cream sweater with thin horizontal stripes over a light blue collar, brown trousers.
- THE TRAINER: a man in his sixties with grey hair and a short grey beard, a black sweater over a dark green collar, grey trousers.
- THE BOARD MEMBERS: faceless dark grey silhouette figures in suits, without any facial features.
- THE ROBOT: a small friendly cream-coloured robot with a round head and a dark visor with two small white eyes. It appears only on computer screens, never in the room.
```

## De twaalf plaatjes

### Plaatje 1: plaatje1.jpeg (3:4)

```text
Aspect ratio 3:4. A meeting room in a modern office. On the left, three faceless dark grey silhouette figures in suits sit at a long table. On the right, NOOR stands at the head of the table, proud and smiling, gesturing at a very thick bound report that lies on the table in front of her. Tall windows behind the table.

Texts in the image, exactly as written:
- Narration caption, top left: "Voorbeeld BV installeert en onderhoudt warmtepompen. Maandagochtend."
- Label on the cover of the report: "AI-plan"
- Speech balloon, NOOR: "Zes maanden werk. Hier staat hoe wij de komende drie jaar AI inzetten."
```

### Plaatje 2: plaatje2.jpeg (1:1)

```text
Aspect ratio 1:1. The same meeting room, closer. On the left, one faceless dark grey silhouette figure in a suit sits at the table in profile and looks up from the phone in its hand. On the right, NOOR stands behind the table, shocked, her hand still on the closed thick report.

Texts in the image, exactly as written:
- Speech balloon, board member, top left, read first: "Wacht even. Warmtepompen melden hun storing voortaan zelf aan de fabrikant. Die kiest de monteur."
- Speech balloon, NOOR, lower right: "Dan belt de klant ons niet meer. En daar gaat mijn hele plan van uit."
```

### Plaatje 3: plaatje3.jpeg (4:5)

```text
Aspect ratio 4:5. Evening in a kitchen at home, dark window, one warm lamp above the table. On the left, NOOR sits at the kitchen table in profile, facing right, worried and thoughtful. The thick report lies closed on the table next to her. On the right, an open laptop faces the viewer with a large white screen that shows a simple web page.

Texts in the image, exactly as written:
- Title caption, top left: "DIE AVOND"
- Thought balloon, NOOR: "Een nieuw plan is over een half jaar ook weer ingehaald."
- On the laptop screen, small heading: "Training AI-strategie, drie lesdagen"
- On the laptop screen, large bold text: "Hoe bepaal je een strategie als elk plan wordt ingehaald voordat het op papier staat?"
- On the laptop screen, black button: "Inschrijven"
- Speech balloon, NOOR, at the bottom: "Dat is mijn vraag."
```

### Plaatje 4: plaatje4.jpeg (4:5)

```text
Aspect ratio 4:5. Outdoors in thick fog, flat ground. In the centre a tall wooden signpost with four arrow-shaped signs, alternately pointing right and left, all pointing into the fog. On the left, NOOR stands at the foot of the signpost and looks up, puzzled. At the right edge, THE TRAINER stands in profile, facing her, relaxed.

Texts in the image, exactly as written:
- Narration caption, top left: "De training draait om vier vragen."
- On the four signs, from top to bottom: "Richting / Transformeren / Investeren / Roadmap"
- Speech balloon, NOOR, read first: "Ze wijzen allemaal de mist in."
- Speech balloon, THE TRAINER: "Klopt. Wat doe jij als je niet ver vooruit kunt kijken?"
```

### Plaatje 5: plaatje5.jpeg (4:5)

```text
Aspect ratio 4:5. A corridor in the same modern office as the other panels, in a converted brick building. A fully drawn and coloured scene: warm wooden floor, an off-white wall with a wooden skirting board, a ceiling with beams, at the far left a tall industrial window with red-brown brick outside, a large green plant in a pot, and a pendant lamp. Two doors are set in the wall, side by side.

On the left, a heavy closed steel vault door, dark blue-grey, with rivets, hinges and a large round wheel handle, and a small white sign on it. It looks massive and final.

On the right, an open doorway in a wooden frame with light wooden swinging saloon-style half doors. Through the doorway you see a glimpse of the bright office: a desk, a chair and a plant. NOOR steps through this doorway, full body, in profile, walking to the right, with a small confident smile. She is an adult woman in her late thirties, exactly as in the reference image, and of normal adult height: the doorway is clearly taller than she is.

The layout sketch shows only where the doors, NOOR and the texts go. Do not copy its empty white background or its flat drawing: draw this panel as richly as the reference image, with the same line, the same colours and the same level of detail. Draw nothing outside the panel border.

Texts in the image, exactly as written:
- Narration caption, top left: "Je begint klein."
- Sign on the vault door: "Geen weg terug"
- Speech balloon, NOOR: "Deze stap kan ik terugdraaien. Dus die zet ik nu."
- Narration caption, across the bottom: "Als de toekomst door onzekerheden wordt vertroebeld, kies voor leren en houd je opties open."
```

### Plaatje 6: plaatje6.jpeg (4:5)

```text
Aspect ratio 4:5. A training room in the same modern office as the other panels: tall industrial windows with red-brown brick outside, green plants, wooden furniture. THE PARTNER (left) and NOOR (right) sit side by side behind a wooden table, facing the viewer. Each has one sheet of paper in front of them, with a few scribbled lines that are not readable. THE PARTNER leans over and points at the sheet of NOOR. NOOR writes on her sheet with a pen, concentrating.

NOOR and THE PARTNER are two adult colleagues of the same age, both in their late thirties. They are the same size: their shoulders are at the same height above the table and their heads are the same size. NOOR has the adult face and proportions of the reference image, not those of a child or a teenager. Her sweater has the same muted yellow-green as in the reference image.

The layout sketch shows only where the figures and the texts go. Do not copy its drawing style. Draw nothing outside the panel border.

Texts in the image, exactly as written:
- Narration caption, top: "Dat oefen je drie dagen op je eigen organisatie. Naast je zit je duo, met een eigen casus."
- Speech balloon, THE PARTNER, read first: "Ik werk bij een gemeente, dus leg eens uit: wat kost het jullie als dit mislukt?"
- Speech balloon, NOOR: "Zes weken van één team. Dat moet ik er wel bij zetten."
```

### Plaatje 7: plaatje7.jpeg (4:5)

```text
Aspect ratio 4:5. The same training room and the same table, now with nobody sitting at it. In the foreground two open laptops stand on the table, screens facing the viewer; each screen shows THE ROBOT, cheerful, above a horizontal progress bar that is two-thirds filled with yellow-green. In the background on the right, by a tall window, THE PARTNER and NOOR stand facing each other, each holding a white coffee cup, chatting and relaxed.

Texts in the image, exactly as written:
- Narration caption, top: "Het schrijfwerk doet de AI. De werkregel: voordat je pauze neemt, zet je de AI aan het werk."
- Speech balloon, THE PARTNER, read first: "Wat doet die van jou nu?"
- Speech balloon, NOOR: "Stukken van ons bestuur zoeken. Straks kijk ik of het klopt."
- Narration caption, across the bottom: "Zo werk je. En dit maak je ermee in drie dagen:"
```

### Plaatje 8: plaatje8.jpeg (2:3)

```text
Aspect ratio 2:3. One tall panel divided by a horizontal black line into an upper and a lower half. Upper half, morning in a training room: on the left NOOR sits at a table and writes with a pen; on the right a large close-up of the card she writes on, one sheet divided into four boxes numbered 1 to 4, the first two with a few scribbled lines. Lower half, afternoon: on the left NOOR stands in profile, facing right, a little taken aback; on the right an open laptop faces the viewer, and on its screen four small advisers sit around a round table, one of them leaning forward and speaking.

Texts in the image, exactly as written:
- Title caption, top left: "DAG 1: RICHTING"
- Narration caption, upper half: "'s Ochtends schrijf je bij elke vraag wat je nu zou doen."
- Narration caption, lower half: "'s Middags bouw je in je AI een raad van advies, die je keuzes toetst."
- Speech balloon, NOOR, lower half, read first: "Ons doel: de beste service van de regio."
- Speech balloon, the adviser on the screen: "Dit is nog geen strategische keuze. Welke alternatieven heb je en wijs je bewust af?"
```

### Plaatje 9: plaatje9.jpeg (4:5)

```text
Aspect ratio 4:5. A training room. On the left, four adults sit in a row behind a table, facing the viewer; one of them is THE PARTNER, the other three wear plain grey and cream clothes. Each has a folded name card on the table. On the right, NOOR stands and presents, calm. On the wall above her a white presentation screen with one line of text. A round wall clock in the upper left.

Texts in the image, exactly as written:
- Title caption, top left: "DAG 2: TRANSFORMEREN EN INVESTEREN"
- On the presentation screen: "Eerste prioriteit: de AI helpt klachten sorteren"
- On the four name cards, from left to right: "Financiën / Privacy / OR / Medewerker"
- Speech balloon, the person on the far left, read first: "Mooi verhaal. Hoe weet je dat het werkt?"
- Speech balloon, NOOR: "Dat weet ik nog niet. Ik ga het eerst klein meten."
- Narration caption, across the bottom: "Je presenteert wat je thuis hebt voorbereid. De groep speelt de mensen die bij jou beslissen. 's Middags maak je de businesscase."
```

### Plaatje 10: plaatje10.jpeg (1:1)

```text
Aspect ratio 1:1. Evening at home. On the left, NOOR sits behind a desk in profile, facing right, with a calm, decided look. On the right, an open laptop faces the viewer with a large white screen that shows a question and two horizontal bars; the lower bar is slightly shorter than the upper one. A desk lamp, a cup, a dark window.

Texts in the image, exactly as written:
- Narration caption, top: "Tussen dag 2 en dag 3 doe je thuis een klein experiment. De norm kies je vooraf."
- On the laptop screen, question: "Kiest de AI dezelfde urgentie als de medewerker?"
- On the laptop screen, above the upper bar: "Norm: 8 van de 10 klachten"
- On the laptop screen, above the lower bar: "Uitkomst: 7 van de 10"
- Speech balloon, NOOR: "Net onder de norm. Dan schalen we nog niet op. Ik kies de andere route."
```

### Plaatje 11: plaatje11.jpeg (2:3)

```text
Aspect ratio 2:3. One tall panel divided by a horizontal black line into an upper and a lower half. Upper half: a clean diagram of a railway line on an off-white wall, with three small station signs in a row; after each station a switch leads to a side track, and the first switch is set to the side track, drawn in a thicker line. Lower half, a training room: on the left an open laptop faces the viewer, and on its screen THE ROBOT looks worried; on the right NOOR stands in profile, facing left towards the laptop, with a kind and reassuring expression.

Texts in the image, exactly as written:
- Title caption, top left: "DAG 3: DE ROUTE EN HET DRAAGVLAK"
- Narration caption, upper half: "Je maakt een route voor het eerste jaar. Bij elke stap staat wat je doet als het tegenvalt."
- On the three station signs, from left to right: "Experiment / Pilot / Opschaling"
- Small note under the diagram: "De eerste wissel staat om."
- Narration caption, lower half: "Daarna oefen je het lastigste gesprek. De AI speelt je collega."
- Speech balloon, THE ROBOT on the screen, read first: "Ik ben nu verantwoordelijk voor het afhandelingsproces van klachten. Wat blijft er van mijn werk over als AI dit gaat automatiseren?"
- Speech balloon, NOOR: "Jij blijft beslissen. De AI doet alleen een voorstel."
```

### Plaatje 12: plaatje12.jpeg (3:4)

```text
Aspect ratio 3:4. The same meeting room and the same camera angle as the first panel. On the left, the faceless dark grey silhouette figures in suits sit at the table and lean forward with interest; one of them holds a phone. On the right, NOOR stands confident and smiling, and points with one arm to a wall screen in the upper right that shows a small railway diagram with three stations and switches. The thick report is gone.

Texts in the image, exactly as written:
- Title caption, top left: "VOORBEELD BV, EEN PAAR WEKEN LATER"
- On the three station signs on the wall screen: "Experiment / Pilot / Opschaling"
- Speech balloon, the board member with the phone, read first: "Wacht even. De fabrikant gaat nu ook onderhoud aanbieden."
- Speech balloon, NOOR: "Daarvoor is deze wissel. Vrijdag kiezen we welke kant we op gaan."
- Narration caption, across the bottom: "Het nieuws verandert weer. Je voorstel kan ertegen."
```
