# BO-simulator (kopie)

Een simulator die laat zien hoe Bayesiaans optimaliseren de volgende test kiest. Het voorbeeld is de beste plek voor een distributiecentrum: de plek met de laagste transportkosten naar dertig klanten. Elke test is een dure haalbaarheidsstudie, dus je wilt er zo weinig mogelijk doen.

- **Gebruik:** de lespagina `materiaal/vier-vragen.html`, stap 4 (dag 1 om 11:00, FR-34). Op dag 3 komt hij terug bij vraag 4, de roadmap.
- **Bron:** <https://github.com/businessdatasolutions/bayesian-optimization>, commit `a6bd2ae0fae4045823eee4383aee705d75bc4139` van 2 september 2025.
- **Wat is gekopieerd:** alleen `bo-simulator-fast.html` en `LICENSE`, op 8 november 2026. `bo-simulator-fast.html` wijkt op drie punten af van het origineel: twee reparaties (het model, en de volgorde binnen een stap) en de huisstijl. Zie "Aanpassingen ten opzichte van het origineel". De openbare repo is niet gewijzigd.
- **Licentie:** MIT. Copyright (c) 2025 businessdatasolutions. De volledige tekst staat in `LICENSE`.

## Live versies

- De simulator, zonder de aanpassingen: <https://businessdatasolutions.github.io/bayesian-optimization/bo-simulator-fast.html>
- De Nederlandse dia's over Bayesiaans optimaliseren: <https://businessdatasolutions.github.io/bayesian-optimization/slides-nl.html>

Beide gaven op 8 november 2026 een HTTP 200.

## Internet nodig

De simulator laadt Three.js r128 van cdnjs.cloudflare.com en de camerabediening (OrbitControls) van cdn.jsdelivr.net. Zonder internet blijft "Loading 3D Scene..." in beeld staan. De reserve zijn de drie schermafbeeldingen hieronder. Ze staan ook op `vier-vragen.html`.

Bij elke keer laden staan de dertig klanten op een andere plek. Twee groepen zien dus nooit precies hetzelfde beeld.

## De bediening in het Nederlands

| In de simulator | Wat het doet |
|---|---|
| Initialize / Reset | Begin of begin opnieuw. De simulator doet twee tests op een willekeurige plek, als eerste aanwijzing. |
| Run One Step | Eén stap: de simulator test de plek van de rode bol. Daarna werkt het model zijn beeld bij en kiest het de volgende plek, een nieuwe rode bol. |
| Run Automatically | Stappen achter elkaar, tot "Max Auto Runs" (standaard 50). Klik op "Stop" om te stoppen. |
| Observation Noise | De meetfout: hoe onbetrouwbaar één test is. Bij 0 klopt elke test precies. |
| Exploration (Beta) | β: hoeveel de keuzeregel verkent. Laag: blijf bij wat goed lijkt. Hoog: test waar je het minst weet. |
| Graphics Quality, Max Auto Runs | Alleen het beeld en het aantal automatische stappen. De rekensom verandert niet. |
| Toggle True Cost | De echte kosten, als zwarte draadjes. Staat eerst uit, want in het echt ken je ze niet. |
| Toggle Belief | Wat het model denkt, als vlak. Bleek is onzeker, grijs is zekerder. Waar nog niet getest is, ligt het vlak op de gemiddelde kosten. |
| Toggle Decision | De keuzeregel, als rood vlak. De volgende test komt waar dit vlak het laagst is. |
| Iteration, Feasibility Studies | Het aantal stappen en het aantal tests. |
| Best Cost Found, Optimal Location | De laagste kosten tot nu toe, en op welke plek. |

Een weergaveknop die aan staat, is zwart. Bij het laden staat alleen Toggle Belief aan.

**De kleuren:** grijze staafjes zijn klanten. Zwarte bollen zijn plekken die al getest zijn. De gele bol met de zwarte rand is de beste plek tot nu toe. De rode bol is de volgende test. De gele en de rode bol staan altijd vooraan, ook als er een vlak voor ligt. De legenda rechtsonder noemt ook de drie vlakken.

Tussen twee klikken gaat het vlak door alle tests, en is de rode bol de volgende test. Het laagste punt van het vlak ligt vaak één rasterhok naast de gele bol, en iets lager. Dat klopt: de gele bol is de beste meting, en daarnaast verwacht het model nog lagere kosten. Bij een lage β komt de volgende test daar.

De uitleg in de simulator zelf (tabblad "Tutorial") is Engels en gebruikt dezelfde kleuren.

## Schermafbeeldingen (reserve)

Gemaakt op 8 november 2026 met de aangepaste kopie in de huisstijl, in een venster van 1280 bij 760 pixels. Alle drie in dezelfde wereld: dezelfde klanten, dezelfde echte kosten en dezelfde twee eerste tests. Dat kan doordat `Math.random` een vaste beginwaarde kreeg (seed 7). De opnames zijn gemaakt in Chrome via Playwright.

- `start.png`: na Initialize / Reset met β = 0,5. Twee tests. Het vlak is bijna overal bleek: het model weet nog bijna niets. De rode bol ligt naast de gele.
- `stap-laag-beta.png`: vijf stappen met β = 0,5. De zwarte bollen liggen bij elkaar in één dal, met de gele bol onderaan. De rode bol ligt er vlak naast.
- `stap-hoog-beta.png`: vijf stappen met β = 10. De zwarte bollen liggen verspreid over het veld. De rode bol ligt ver van de gele, waar nog niet getest is.

De schermafbeeldingen zijn gemaakt na aanpassing 3 (zie hieronder). `start.png` bleef daarbij gelijk, want Initialize / Reset is niet veranderd.

## Aanpassingen ten opzichte van het origineel

### 1. Het model gaat uit van het gemiddelde

**Wat:** het model (een Gaussisch proces) gaat uit van het gemiddelde van de metingen in plaats van 0. Vóór het fitten trekt het het gemiddelde van de gemeten kosten af en deelt het door de standaardafwijking. Bij elke voorspelling telt het die er weer bij op. Het gaat om vier plekken in de klasse `SimpleGP`; elke plek heeft een commentaarregel `// AISO-reparatie: ...`.

**Waarom:** in het origineel rekent het model met 0 als beginwaarde, terwijl de kosten tussen ongeveer 16 en 64 liggen. Een plek die nog niet getest is, lijkt daardoor de goedkoopste. De keuzeregel koos dus bij elke β eerst nieuw terrein, en de schuif β deed bijna niets. Daar draait de oefening op `vier-vragen.html` juist om.

**Controle (8 november 2026):** gemeten is de afstand van elke nieuwe test tot de beste plek tot dan toe, over vijf stappen. Het veld is 50 bij 50.

| | β = 0,5 | β = 10 |
|---|---|---|
| Origineel, eigen narekening, 10 werelden | 35,8 | 37,2 |
| Aangepast, eigen narekening, 10 werelden | 3,5 | 10,2 |
| Aangepast, in de browser, 3 rondes | 2,6 tot 3,5 | 10,3 tot 12,2 |

Met de aanpassing blijft een lage β bij de beste plek, en waaiert een hoge β uit over onbekend terrein.

### 2. De huisstijl

**Wat:** het paneel, de legenda en de 3D-scène zijn in de huisstijl van Business Data Solutions, met dezelfde kleuren en letters als `vier-vragen.html`. De tekst is Engels gebleven. Elke plek heeft een commentaar `AISO-huisstijl`.

- Het stijlblok is vervangen. Geel is het enige accent: de open tab en de knop Initialize / Reset. De sectiekoppen staan in kleine grijze hoofdletters. De status staat op een cream kaart.
- Alle kleuren van de scène staan in `SCENE_COLORS`. Zwart is wat gemeten is: de tests en de draadjes van de echte kosten. Geel is de beste plek. Rood is de keuzeregel: het vlak en de bol die hij kiest. Grijs is context: de klanten. Het vlak van het model loopt van bleek (onzeker) naar warm grijs (zekerder).
- Het licht is zachter: 0,6 en 0,5 in plaats van 0,7 en 0,7. Anders wordt het bleke vlak wit.
- Het vlak van het model heeft wit als materiaalkleur. In het origineel vermenigvuldigde Three.js de kleur per hoekpunt met blauwgroen. Daardoor was het onzekere deel fel groen, terwijl de code geel opgaf.
- De beste plek is iets groter (straal 1,1 in plaats van 1) en heeft een zwarte rand. Hij staat altijd vooraan, net als de volgende test, en de volgende test staat weer vóór de beste plek. Zo blijft hij heel zichtbaar, ook als hij half in het vlak ligt.
- De weergaveknoppen tonen of hun laag aan staat (`aria-pressed`). Bij een andere Graphics Quality blijft een laag aan of uit. In het origineel sprong hij dan terug naar de beginstand.
- De legenda noemt ook de drie vlakken.
- De pagina heeft het icoon van de lespagina's. Zonder icoon vraagt de browser `/favicon.ico` op, en dat geeft een 404 in de console.
- In de Tutorial volgen de kleurwoorden de nieuwe kleuren. Twee zinnen zijn ook inhoudelijk hersteld. De kleur van het vlak toont de onzekerheid, niet de kosten. En de volgende test komt op het laagste punt van het keuzevlak, niet op een piek.

**Waarom:** de simulator hoort bij de lespagina's, en die zijn in de huisstijl. De huisstijl heeft maar twee echte kleuren, geel en warm zwart. Daarom heeft elke kleur één betekenis, en helpen vorm, grootte en de zwarte rand mee. De vier kleuren van de bollen zijn ook bij kleurenblindheid uit elkaar te houden. Het kleinste verschil is ΔE 10,8 (OKLab, deuteranopie), boven de grens van 8.

**Controle (8 november 2026):** de rekensom is niet veranderd. In de drie nieuwe schermafbeeldingen blijft een lage β bij de beste plek, en waaiert een hoge β uit. De console toont geen fouten. De 404 voor de ontbrekende favicon is sinds 8 november 2026 weg: de pagina heeft nu een icoon.

### 3. Eerst testen, dan het model bijwerken

**Wat:** `step()` test eerst de plek van de rode bol. Na 500 ms werkt het model zijn beeld bij en kiest het de volgende plek. Het origineel deed het andersom: eerst bijwerken en kiezen, en 500 ms later testen. De gekozen plek staat in `boState.nextPoint`. Een tweede klik binnen die 500 ms doet niets, zodat dezelfde plek niet twee keer getest wordt. Elke plek heeft een commentaar `AISO-reparatie`. De keuzeregel zelf is niet veranderd.

**Waarom:** in het origineel was het vlak tussen twee klikken het beeld van vóór de laatste test. De rode bol stond dan op de plek die net getest was. Een nieuwe beste plek lag daardoor onder het vlak, tot 2,5 kosteneenheden lager. Met de gele bol vooraan (aanpassing 2) zag je hem naast het vlak zweven. En "de rode bol is de volgende test" klopte alleen vlak na Initialize / Reset.

**Controle (8 november 2026):** in de browser, met β = 0,5 en een vaste beginwaarde, gemeten tussen twee klikken. Het gat is het verschil tussen het vlak en de gemeten kosten van de beste plek.

| Na stap | Gat, origineel | Gat, aangepast |
|---|---|---|
| 2 | 2,25 | 0,00 |
| 3 | 2,54 | 0,00 |
| 4 | 1,84 | 0,00 |
| 5 | 1,73 | 0,00 |

In het origineel stond de rode bol na elke stap op een geteste plek, na de aanpassing steeds op een nieuwe. Het aantal stappen en tests is gelijk gebleven. Na stap 1 bleef een gat van 0,77 over. Daar was de beste plek nog een van de twee willekeurige starttests, en die liggen niet op het raster. De meting nam het dichtstbijzijnde rasterpunt, dus het gat op het scherm is kleiner. Twee snelle klikken geven één test, en Run Automatically loopt door en stopt.

**Bij een nieuwe versie van het origineel:** kopieer opnieuw en breng de wijzigingen met `AISO-reparatie` en `AISO-huisstijl` weer aan. Kijk eerst of het origineel de reparaties zelf al heeft. Maak daarna de drie schermafbeeldingen opnieuw.
