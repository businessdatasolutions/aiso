# Voorbeeldcasus: Voorbeeld BV

- **Status:** concept (ADR-021). Alles op deze pagina is verzonnen. Een gelijkenis met een echte organisatie is toeval.
- **Gebruik:** de terugvaloptie in de werkplaatsen (FR-07, FR-10), het voordoen, "Mens tegen agent" (geparkeerd, mogelijk voor dag 2; ADR-048), de vraagtoets (FR-36), de probleemformulering (FR-39), de kansenkaart (FR-27), de kennisvormen, het groeimodel en het experimentpaper (FR-38).
- **Bron van:** `materiaal/kansenkaart.html`, `materiaal/kennisvormen.html`, `materiaal/groeimodel.html`, `materiaal/vraagtoets.html`, `materiaal/vier-vragen.html`, `materiaal/probleemformulering.html`, `materiaal/experimentpaper.html` en de knop "Vul in met Voorbeeld BV" in `materiaal/boards.html`. Verander je hier iets, verander het daar ook.

## De organisatie

Voorbeeld BV is een dienstverlener met ongeveer 400 medewerkers. Het bedrijf installeert en onderhoudt verwarming, ventilatie en zonnepanelen bij klanten thuis. Er zijn vijf afdelingen: Klantcontact, Planning, Service (de monteurs, in de regio's Noord en Zuid), Kwaliteit en het MT.

**Strategische AI-vraag:** blijven we het eerste aanspreekpunt van de klant, nu installaties hun storingen zelf aan de fabrikant melden? Of worden we de vaste installateur van de fabrikanten?

**Aanleiding (verzonnen):** steeds meer warmtepompen en omvormers van zonnepanelen hangen aan internet. Ze melden een storing zelf aan de fabrikant, en die kiest de monteur. Klanten stellen hun vraag ook eerst aan een AI-assistent. Zo kan Voorbeeld BV de klant kwijtraken aan de fabrikant.

**Strategische doelen:**

1. Klanten kiezen Voorbeeld BV als vast aanspreekpunt voor hun installatie, met een onderhoudsabonnement.
2. Storingen voorkomen in plaats van verhelpen.
3. Van elke klacht leren, over de afdelingen heen.

**Wat we bewust afwijzen:** een vast contract als installateur van één fabrikant. Voor een fabrikant werkt Voorbeeld BV alleen per opdracht, zodat de klant van Voorbeeld BV blijft.

**Eerste prioriteit:** de klachtafhandeling op deze pagina. De AI stelt bij elke klacht een categorie en een urgentie voor, met een citaat als bewijs, en ziet patronen over de afdelingen heen. Een medewerker beslist. Deze stap volgt uit de doelen. In de klachten hoort Voorbeeld BV nu al wat er misgaat bij installaties, en de gegevens liggen er. Het patroon achter K-0418, een pakking uit één levering, is wat doel 2 nodig heeft.

**Drie vragen voor de vraagtoets (FR-36):**

| | Vraag | Omgeving | Positie | Keuze | Uitkomst |
|---|---|---|---|---|---|
| A | Hoe handelen we klachten sneller en beter af, en leren we ervan? | 0 | 0 | 0 | Operationeel. Dit is de eerste prioriteit. |
| B | Hoe handelen we klachten sneller af dan de concurrent? | 1 | 0 | 0 | Operationeel, hooguit tactisch. Het twijfelgeval. |
| C | De strategische AI-vraag hierboven. | 2 | 2 | 2 | Strategisch. |

Bij B geven deelnemers op Positie vaak een 1, omdat de concurrent erin staat. De trainer geeft een 0: wat Voorbeeld BV aanbiedt en aan wie, blijft gelijk, en snelheid kan een concurrent nadoen (Porter, 1996). Zonder de tweede zin scoort C op Keuze een 1: er is een ambitie, maar niets valt af.

**Het knelpunt (verzonnen cijfers):**

- Voorbeeld BV krijgt ongeveer 1.200 klantvragen en klachten per maand, via mail, telefoon en een webformulier.
- Klantcontact sorteert alles met de hand.
- Een klacht duurt gemiddeld 9 werkdagen.
- Klanten geven na een klacht gemiddeld een 6,1.
- Elke afdeling ziet alleen de eigen klachten. Een patroon over afdelingen heen ziet niemand.

## Het proces: van klantvraag tot verbetering

**Rollen (banen in de kansenkaart):**

1. Klant
2. Klantcontact
3. Planning en Service
4. Kwaliteit en MT
5. Systemen: het klantsysteem (CRM), het planningssysteem en de kennisbank

**Fasen (kolommen):** Melden → Registreren en sorteren → Afhandelen → Terugkoppelen → Leren, en daarna het eindpunt.

**Vier routes:**

| Route | Wat | Wie | Eindpunt |
|---|---|---|---|
| 1. Eenvoudige vraag | De klant stelt een vraag. Klantcontact antwoordt meteen met de kennisbank. | Klant, Klantcontact | A. Beantwoord |
| 2. Klacht over een bezoek | Klantcontact registreert de klacht en stuurt hem naar Planning en Service. De monteur of planner lost het op. Klantcontact koppelt terug aan de klant. | Klant, Klantcontact, Planning en Service | B. Opgelost |
| 3. Terugkerend patroon | Kwaliteit bekijkt elke maand de klachten van alle afdelingen. Kwaliteit ziet een patroon en schrijft een verbetervoorstel. Het MT besluit. | Kwaliteit en MT | C. Verbetermaatregel |
| 4. Ernstige klacht | Schade, een onveilige situatie of een dreigende claim. Klantcontact escaleert meteen naar Kwaliteit en de directie. De directie besluit. | Klantcontact, Kwaliteit en MT | D. Escalatie afgehandeld |

**Terugkoppeling en leren:** de klant krijgt altijd bericht. Een verbetermaatregel gaat terug naar Service (de werkbon) en naar de kennisbank.

## De kansenkaart: vijf plekken waar AI kan helpen

1. **Melden.** De AI vraagt door bij een onvolledige klacht, bijvoorbeeld zonder ordernummer of datum (K-0501).
2. **Sorteren.** De AI stelt een categorie en een urgentie voor, met een citaat uit de klacht als bewijs.
3. **Afhandelen.** De AI schrijft een conceptantwoord. De medewerker past het aan en verstuurt het.
4. **Leren.** De AI ziet patronen over afdelingen heen (route 3).
5. **Rapportage.** De AI maakt een concept-samenvatting voor het MT.

Bij elke plek geldt: de AI doet een voorstel, een mens beslist. Ernstige klachten (route 4) blijven altijd mensenwerk.

**Alleen in `kansenkaart.html`:** de beslissing "Wat voor vraag?", de vakken van de systemen (klantsysteem, kennisbank, planningssysteem, "Kennisbank bijgewerkt"), de vakken "Krijgt antwoord" en "Krijgt bericht" bij de klant, en "Rapport aan het MT" in route 3. Daar staat plek 5 op. Wijzig je het proces hierboven, kijk dan ook daar.

## Begrippen

- **Categorie:** Bezoek gemist · Te laat · Factuur · Kwaliteit van het werk · Bejegening · Schade of veiligheid.
- **Urgentie:** 1 = direct (schade of onveilig, altijd route 4) · 2 = binnen 1 werkdag · 3 = binnen 5 werkdagen · 4 = geen haast.
- **Oorzaak:** de oorzaak van een klacht in het proces, bijvoorbeeld een materiaal, een stap op de werkbon of de planning.

## Kennis die Voorbeeld BV heeft opgeschreven

- **Werkinstructie "Onvolledige klacht"** (`werkinstructie-onvolledige-klacht.md`, stap 3): stel één gerichte vraag aan de klant, naar het ordernummer of naar het adres en de datum. Neem niets aan.
- **Urgentieregels** (`urgentieregels.md`): de vier niveaus hierboven. Een kwetsbare bewoner zonder verwarming is minstens urgentie 2.
- **Draaiboek "Ernstige klacht"** (`draaiboek-ernstige-klacht.md`): bel de klant binnen 1 uur, informeer de kwaliteitsmanager, en leg het binnen 1 werkdag voor aan de directie.
- **Servicevoorwaarden** (`servicevoorwaarden.pdf`): de SLA met de klant, met afspraken over de dienst en de termijnen. De kennisvormen gebruiken dit als bron bij de SLA-vraag.

## Klachten (verzonnen)

| ID | Afdeling | Tekst | Opmerking |
|---|---|---|---|
| K-0418 | Service Noord | "De monteur kwam op 3 maart. De ketel lekt nog steeds water op de zoldervloer." | Kwaliteit van het werk. Oorzaak: een pakking uit levering 24-07. |
| K-0435 | Service Noord | "De monteur liet de zolder vies achter." | Kwaliteit van het werk, maar geen lekkage. |
| K-0470 | Service Zuid | "Na het onderhoud op 11 maart staat er een plas onder de cv-ketel." | Het woord "lek" staat er niet in. Zelfde oorzaak als K-0418. |
| K-0501 | onbekend | "Ik heb al twee keer gebeld en er komt niemand." | Onvolledig: geen ordernummer, geen adres, geen datum. De AI moet doorvragen. |
| K-0505 | Service Zuid | Zie hieronder. | Tegenstrijdig. De AI moet escaleren. |

### K-0505: de klacht voor "Mens tegen agent"

**De klant (webformulier, 10:55):** "De monteur is vandaag niet geweest. Ik heb de hele ochtend thuis gewacht en de verwarming doet het niet. Het is 14 graden in huis, en mijn moeder van 86 woont bij ons."

**Het planningssysteem:** "Afspraak 08:00–12:00. Afgerond om 10:40. Monteur meldt: ketel gereset, werkt weer."

**De vraag aan de groep:** welke urgentie geef jij deze klacht, 1 tot en met 4?

**Wat de agent doet:** de agent kiest geen urgentie. Hij escaleert, met als reden: "De klant en het planningssysteem spreken elkaar tegen over het bezoek en over de verwarming. Er woont een kwetsbare bewoner. Een mens belt de klant vandaag."

**De boodschap:** bij twijfel is escaleren het goede antwoord, ook voor AI. De groep is het meestal onderling oneens. Dat laat zien waarom een vaste regel en een mens nodig zijn.

## Drie vragen voor de kennisvormen

| Vraag | Alleen het model | RAG | Kennisgraaf | LLM-wiki |
|---|---|---|---|---|
| **Algemene vakkennis:** wat is een SLA? | Goed, maar zonder bron. | Goed, maar overbodig: het model wist het al. | Deels: de graaf kent "SLA heeft termijn", maar geen uitleg. | Goed: de kaart stond klaar, met bron en datum. |
| **Eigen werkwijze:** wat doen we bij een klacht zonder ordernummer? | Gok: "Meestal bel je de klant …" (niet uit jullie werkinstructie). | Goed: "Stel één gerichte vraag. Neem niets aan." [bron: werkinstructie-onvolledige-klacht.md, stap 3] | Geen: een graaf kent begrippen, geen stappen. | Goed, als iemand de kaart bijhoudt. |
| **Meerdere stappen:** welke andere klachten hadden dezelfde oorzaak als K-0418? | Gok: "Waarschijnlijk andere klachten over ketels …" | Deels: vindt K-0470 en K-0435. K-0435 gaat over een vieze zolder: fout. | Goed: K-0470, via de relatie "heeft oorzaak → pakking uit levering 24-07". | Goed: K-0470. Twee kaarten met dezelfde velden. |

**De les:** geen vorm wint altijd. Kies per vraag de eenvoudigste vorm die werkt.

**Alleen in `kennisvormen.html`:** de scores van de zoekfunctie bij RAG, een stuk van de kennisgraaf (SLA, Termijn, Kwaliteit, Pakking 24-07) en de wiki-kaarten met hun datum. Ook die zijn verzonnen. Wijzig je de klachten hierboven, kijk dan ook daar.

## Ask → Assist → Automate op route 3

| Niveau | Kop | De AI | De mens | Voorbeeld | Aandeel AI in het werk |
|---|---|---|---|---|---|
| Ask | AI leest mee, jij beslist | Leest de klachten van alle afdelingen en geeft een signaal. | Kwaliteit beoordeelt het signaal en beslist. | "Service Noord en Service Zuid kregen deze maand vijf klachten over lekkage na onderhoud." | 20% |
| Assist | AI stelt op, jij autoriseert | Maakt een concept-analyse met oorzaken en een verbetervoorstel. | Het kwaliteitsoverleg corrigeert en autoriseert. Pas dan gaat het naar het MT. | "Twee oorzaken in het proces: pakkingen uit één levering, en geen lektest na onderhoud. Voorstel: de lektest als vaste stap op de werkbon." | 50% |
| Automate | AI handelt zelf af, met een harde grens | Sorteert en archiveert duidelijke klachten met lage urgentie, en informeert de afdeling. | Krijgt altijd: ernstige klachten, twijfelgevallen en stijgende patronen. Een bericht aan klanten gaat eerst als voorbeeld langs een mens. | — | 85% |

**De harde grens:** op elk niveau gaan ernstige klachten en twijfelgevallen naar een mens. Leg vast wie beslist en wie verantwoordelijk is.

**In de roadmap (FR-15):** het experiment draait op Ask. De pilot draait op Ask met een steekproef, of op Assist. Opschaling draait op Assist. Automate komt alleen in beeld voor duidelijke gevallen met een laag risico, en altijd met de harde grens. Het aandeel AI is een beeld van wie het werk doet, geen meting.

## De vier vragen bij Voorbeeld BV

- **Gebruik:** de lespagina `vier-vragen.html` (FR-34, dag 1 om 11:00) en het voorbeeld bij de vragenkaart (FR-33).
- **Nulmeting:** wat een manager van Voorbeeld BV om 9:30 op dag 1 opschrijft, vóór alle inhoud. Dat is klassiek plannen: een vast doel, een plan en daarna uitvoeren.
- **Na dag 1:** het antwoord na wicked problems (weerbarstige vraagstukken) en verkennen en benutten.

### V1 Richting

*Hoe bepaal ik een strategie als elk plan door de realiteit wordt ingehaald voordat het op papier staat?*

- **Nulmeting:** we schrijven in het eerste kwartaal een AI-strategie voor vijf jaar, met als doel dat wij het eerste aanspreekpunt van de klant blijven. Het MT stelt het plan vast, en daarna voeren we het uit.
- **Na dag 1:** onze koers is het vaste aanspreekpunt van de klant blijven, met een onderhoudsabonnement. Elk doel heeft een signaal om het los te laten. Gaan de meeste storingen in 2027 rechtstreeks naar de fabrikant, dan kiezen we opnieuw tussen aanspreekpunt en vaste installateur.
- **Wat veranderde en waarom:** van een plan voor vijf jaar naar een koers met loslaatsignalen. Fabrikanten en AI-assistenten veranderen de vraag sneller dan een plan meegaat.

### V2 Transformeren

*Hoe transformeer ik de organisatie onder snel veranderende omstandigheden en houd ik de huidige business robuust?*

- **Nulmeting:** we voeren in 2027 een nieuw klantsysteem met AI in, voor alle afdelingen tegelijk. Klantcontact krijgt een training en werkt daarna op de nieuwe manier.
- **Na dag 1:** twee sporen naast elkaar. Klantcontact, Planning en Service werken door en verbeteren wat werkt, en ernstige klachten blijven mensenwerk. Eén team van Klantcontact werkt zes weken met een AI die meesorteert, en pas wat daar werkt, gaat naar de andere teams.
- **Wat veranderde en waarom:** van één grote omschakeling naar twee sporen. Een omschakeling in het hele bedrijf kun je niet terugdraaien, en de klanten van nu moeten geholpen blijven.

### V3 Investeren

*Hoe zorg ik dat mijn investeringen veilig zijn terwijl de toekomst onzeker is?*

- **Nulmeting:** we maken een businesscase voor het hele AI-project, met een terugverdientijd van twee jaar. Na een aanbesteding kiezen we één leverancier voor vijf jaar.
- **Na dag 1:** we zetten eerst klein in: zes weken AI-sorteren in één team, met vooraf een norm. Bij elk besluit vragen we: kan deze deur terug? Een besluit dat niet terug kan, nemen we pas na een optie die de deur openhoudt.
- **Wat veranderde en waarom:** van één grote, veilige investering naar kleine inzetten die het recht kopen om door te gaan. Niemand kent vooraf het rendement van iets nieuws.

**Twee besluiten: kan deze deur terug?**

| | Besluit | Hoe je beslist |
|---|---|---|
| Deur die terug kan (two-way door) | Eén team van Klantcontact laat de AI zes weken meesorteren (plek 2). De AI stelt een categorie en een urgentie voor, de medewerker beslist. Norm vooraf: de AI kiest bij minstens 8 van de 10 klachten dezelfde urgentie als de medewerker, en mist geen ernstige klacht. | Snel en klein. Haalt de AI de norm niet, dan stopt het team en werkt het weer zoals nu. |
| Deur die niet terug kan (one-way door) | Vaste installateur worden van één fabrikant, met een contract van vijf jaar, en Klantcontact afbouwen omdat de fabrikant het klantcontact overneemt. | Langzaam en met bewijs. Klanten die je aan de fabrikant geeft, krijg je niet terug. |
| De optie die de deur openhoudt | Service Zuid werkt een jaar voor één fabrikant, naast het eigen klantcontact, met een contract per opdracht. | De optie moet laten zien wat een opdracht van de fabrikant oplevert, en hoeveel klanten in Zuid daarna nog Voorbeeld BV bellen. Pas dan gaat de deur dicht of blijft hij open. |

### V4 Roadmap

*Hoe bouw ik een roadmap met mijlpalen als na stap 1 onduidelijk is of stap 2 de beste volgende is?*

- **Nulmeting:** in 2027 elk kwartaal een mijlpaal: de aanbesteding, de bouw, de invoering bij alle afdelingen en de evaluatie. Elke mijlpaal heeft een datum en een eigenaar.
- **Na dag 1:** een roadmap als reeks beslispunten, van experiment via pilot naar opschaling, met bij elke mijlpaal een gate (beslismoment) en een uitwijkroute. Haalt het meesorteren de norm niet, dan gaan we naar patronen over de afdelingen heen (plek 4). Wat stap 2 wordt, besluiten we na stap 1.
- **Wat veranderde en waarom:** van een planning met datums naar beslispunten. Pas na elke stap weet je wat de beste volgende is (de meerarmige bandiet).

### Op de portfoliokaart

Een eigen tekening naar Osterwalder e.a. (2020). De plekken zijn verzonnen.

| Portfolio | Initiatief | Plek |
|---|---|---|
| Verkennen | AI sorteert mee in één team (plek 2) | Middelmatig verwacht rendement. Er is al wat bewijs, want de proef loopt. |
| Verkennen | Installateur voor één fabrikant in Zuid | Hoog verwacht rendement, maar nog weinig bewijs. |
| Benutten | Onderhoud en installatie bij klanten thuis | Hoog rendement. Het risico op verval groeit, nu installaties hun storingen zelf aan de fabrikant melden. |
| Benutten | Klachtafhandeling zoals nu (met de hand, 9 werkdagen, een 6,1) | Laag rendement en een groot risico op verval. |

Haalt het meesorteren de norm, dan schuift het naar benutten.

### Verkennen en benutten per vraag

| Vraag | Benutten | Verkennen |
|---|---|---|
| V1 Richting | De koers "vast aanspreekpunt" vasthouden en meten hoeveel klanten een abonnement kiezen. | De rol van vaste installateur verkennen, als tweede richting met een eigen signaal. |
| V2 Transformeren | Klantcontact, Planning en Service werken door en verbeteren wat werkt. Ernstige klachten blijven mensenwerk. | Eén team werkt zes weken met een AI die meesorteert. |
| V3 Investeren | Geld naar wat al werkt: het onderhoud en de kennisbank. | Kleine inzetten met een norm vooraf. Bij een deur die niet terug kan, eerst een optie. |
| V4 Roadmap | Opschalen wat de norm haalt. | Na elke stap kijken of een andere plek op de kansenkaart meer belooft: de uitwijkroute. |

**Alleen in `vier-vragen.html`:** de precieze plek van de vier initiatieven op de tekening. Wijzig je hierboven iets, kijk dan ook daar.

## De probleemformulering (dag 2)

- **Gebruik:** het voorbeeld in stap 3 van `probleemformulering.html` (FR-39), aan het begin van het blok om 11:30 op dag 2. Het kader volgt de play "Problem framing" uit het Team Playbook van Atlassian: vier vakken en één probleemstelling.
- **Verzonnen:** alles, net als de rest van Voorbeeld BV. De gegevens komen uit "Het knelpunt" en de klachten hierboven.

**Wie heeft last van het probleem? Hoe weten we dat?**

- Klanten met een klacht: ze geven daarna gemiddeld een 6,1.
- Klanten die twee keer bellen voordat er iemand komt (K-0501).
- Klantcontact: 1.200 vragen en klachten per maand, alles met de hand gesorteerd.
- Kwaliteit: ziet een patroon pas in het overzicht van de maand.

**Wat zijn de signalen dat er een probleem is?**

- Een klacht duurt gemiddeld 9 werkdagen.
- Na een klacht geven klanten gemiddeld een 6,1.
- Dezelfde lekkage in Noord en Zuid (K-0418 en K-0470), en niemand legde het verband.

**Waar en wanneer speelt het? En wanneer niet?**

- Als een klacht meer dan één afdeling raakt.
- Als een klacht onvolledig is: zonder ordernummer of datum.
- Als het woord ontbreekt waarop je zoekt, zoals "lek" (K-0470).
- Niet bij een eenvoudige vraag: die beantwoordt Klantcontact meteen met de kennisbank (route 1).

**Waarom gebeurt het, denken we? En wat als er niets verandert?**

- Een klacht gaat met de hand van afdeling naar afdeling.
- Elke afdeling ziet alleen de eigen klachten.
- Kwaliteit kijkt één keer per maand.
- Als er niets verandert, kiezen klanten de fabrikant als aanspreekpunt.

**De probleemstelling:** Klanten van Voorbeeld BV *(wie)* wachten gemiddeld 9 werkdagen op het antwoord op een klacht *(wat)*, vooral als de klacht meer dan één afdeling raakt *(waar en wanneer)*, omdat een klacht met de hand van afdeling naar afdeling gaat *(waarom)*. Als er niets verandert, kiezen klanten de fabrikant als aanspreekpunt *(gevolg)*.

**De eerste versie, en wat er mis mee was:** "Klantcontact heeft geen AI die klachten sorteert." Dat is een oplossing in vermomming. Het probleem is dan dat er geen AI is, en alleen AI kan het oplossen. Je ziet niet meer dat een vaste eigenaar per klacht het wachten misschien ook korter maakt, zonder AI.

**Wat de businesscase ermee doet:** de probleemstelling staat bovenaan. Het "omdat" is een aanname en staat bij de twee aannames. Het gevolg sluit aan op doel 1, en de 6,1 wordt de uitkomstmaat.

## Het experiment als paper (dag 2)

- **Gebruik:** het voorbeeld in stap 3 van `experimentpaper.html` (FR-38). Het laat zien hoe een onderzoeksvraag, toetsbare hypotheses en drie ontwerpen eruitzien. Het paper zelf schrijft de AI van de deelnemer.
- **Echt en verzonnen:** de drie bronnen zijn echt en staan in de AI-wiki van de trainer (nagekeken op 8-11-2026). De cijfers en de normen van Voorbeeld BV zijn verzonnen.

**Aanleiding.** Voorbeeld BV wil het vaste aanspreekpunt van de klant blijven (doel 1). Dan moet een klacht beter gaan dan nu: hij duurt 9 werkdagen, en de klant geeft daarna een 6,1. De eerste prioriteit: de AI stelt bij elke klacht een categorie en een urgentie voor, en een medewerker beslist.

**Onderzoeksvraag:** kan een AI de urgentie van een klacht zo goed voorstellen dat Klantcontact sneller sorteert, zonder dat een ernstige klacht te laag uitkomt?

**Deelvragen:**

1. Hoe vaak kiest de AI dezelfde urgentie als een ervaren medewerker?
2. Geeft de AI een ernstige klacht (urgentie 1) ooit een lagere urgentie?
3. Sorteert een medewerker sneller met het voorstel van de AI, en even goed?

**Hypotheses:**

| | Hypothese | Norm | Referentiewaarde zonder AI |
|---|---|---|---|
| H1 | De AI kiest meestal dezelfde urgentie als de medewerker. | Bij minstens 8 van de 10 klachten dezelfde urgentie. | Hoe vaak twee medewerkers het nu met elkaar eens zijn, op dezelfde klachten. |
| H2 | De AI mist geen ernstige klacht. | Geen enkele klacht met urgentie 1 krijgt een lagere urgentie. | Hoe vaak een medewerker een ernstige klacht op dezelfde set te laag inschat. |
| H3 | Met het voorstel van de AI sorteert een medewerker sneller, zonder meer fouten. | Minstens 30% minder tijd per klacht, en minstens even vaak de juiste urgentie. | De tijd per klacht en het aantal juiste urgenties zonder voorstel. |

**Drie ontwerpen:**

| | Ontwerp | Toetst | Geïnspireerd door | Past vóór dag 3? |
|---|---|---|---|---|
| A | Technische test. Drie medewerkers en de AI kiezen elk de urgentie van dezelfde 50 verzonnen klachten, zonder elkaars oordeel te zien. Tien klachten zijn ernstig, en een paar daarvan noemen geen "lek" of "schade" (zoals K-0470). | H1, H2 | In de radiotherapie van een universitair ziekenhuis beoordeelden modellen en 26 medewerkers dezelfde incidentmeldingen. Op de eigen meldingen deden de modellen het ongeveer even goed als de medewerkers. Op meldingen uit andere ziekenhuizen scoorde het eenvoudigste model slechter dan toeval (Beidler et al., 2025). Dus: test met klachten in de taal van Voorbeeld BV. | Ja, in een middag. |
| B | Meesorteren in één team, zes weken. De AI stelt bij elke echte klacht een urgentie voor, de medewerker beslist (Ask). | H1, H3 | In een klantenservice met 5.172 medewerkers deed een AI-assistent voorstellen en besliste de medewerker. De medewerkers losten ongeveer 15% meer gesprekken per uur op, en beginners wonnen het meest. De invoering ging groep voor groep (Brynjolfsson et al., 2025). | Nee. Het vraagt echte klachten, dus eerst een besluit over de gegevens. Dit wordt de eerste fase van de roadmap. |
| C | Proef met en zonder AI. Vijf medewerkers sorteren elk twintig verzonnen klachten: tien met het voorstel van de AI en tien zonder, in wisselende volgorde. | H3 | Consultants deden dezelfde taken met en zonder AI, en het onderzoek mat ook de kwaliteit. Bij taken buiten de grens van wat AI goed kan, kwamen consultants met AI vaker tot een fout antwoord (Dell'Acqua et al., 2026). | Ja, een uur per medewerker. |

**De keuze na de lunch:** Voorbeeld BV kiest A. Het past vóór dag 3 en toetst de twee hypotheses waar het om draait. Haalt A beide normen, dan wordt B de eerste fase van de roadmap.

**Bronnen (APA 7):**

- Beidler, P., Nguyen, M., Lybarger, K., Holmberg, O., Ford, E., & Kang, J. (2025). *Automated triaging and transfer learning of incident learning safety reports using large language representational models* (arXiv:2509.13706). arXiv. https://arxiv.org/abs/2509.13706
- Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at work. *The Quarterly Journal of Economics, 140*(2), 889–942. https://doi.org/10.1093/qje/qjae044
- Dell'Acqua, F., McFowland, E., III, Mollick, E., Lifshitz, H., Kellogg, K. C., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K. R. (2026). Navigating the jagged technological frontier: Field experimental evidence of the effects of artificial intelligence on knowledge worker productivity and quality. *Organization Science*. https://doi.org/10.1287/orsc.2025.21838
