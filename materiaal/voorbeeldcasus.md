# Voorbeeldcasus: Voorbeeld BV

- **Status:** concept (ADR-021). Alles op deze pagina is verzonnen. Een gelijkenis met een echte organisatie is toeval.
- **Gebruik:** de terugvaloptie in de werkplaatsen (FR-07, FR-10), het voordoen, "Mens tegen agent" (FR-26), de kansenkaart (FR-27), de kennisvormen en het groeimodel.
- **Bron van:** `materiaal/kansenkaart.html`, `materiaal/kennisvormen.html` en `materiaal/groeimodel.html`. Verander je hier iets, verander het daar ook.

## De organisatie

Voorbeeld BV is een dienstverlener met ongeveer 400 medewerkers. Het bedrijf installeert en onderhoudt verwarming, ventilatie en zonnepanelen bij klanten thuis. Er zijn vijf afdelingen: Klantcontact, Planning, Service (de monteurs, in de regio's Noord en Zuid), Kwaliteit en het MT.

**Strategische AI-vraag:** hoe zetten we AI in om klantvragen en klachten sneller en beter af te handelen, en om van klachten te leren?

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

**In het buildplan (FR-15):** het experiment draait op Ask. De pilot draait op Ask met een steekproef, of op Assist. Opschaling draait op Assist. Automate komt alleen in beeld voor duidelijke gevallen met een laag risico, en altijd met de harde grens. Het aandeel AI is een beeld van wie het werk doet, geen meting.
