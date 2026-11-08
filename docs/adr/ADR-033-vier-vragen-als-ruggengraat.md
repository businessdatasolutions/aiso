# ADR-033: De vier vragen als ruggengraat van de lesdagen

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In versie 0.21 liepen zeven mechanismen naast elkaar:
- het casusdeck;
- de werkplaats;
- twee boards met vijf boardmomenten;
- een bouwstraat van vijf documenten;
- een ADR-register en een wijzigingslog;
- een werkplaatslog;
- een regelboek.

De deelnemer zag niet meer waar het om ging.

Op 8 november vroeg de gebruiker de LRD om te bouwen rond vier vragen. Elke leider heeft die in een tijd van snelle technologische verandering:
1. Richting: hoe bepaal ik een strategie als elk plan door de realiteit wordt ingehaald?
2. Transformeren: hoe verander ik de organisatie en houd ik de huidige business robuust?
3. Investeren: hoe investeer ik veilig in een onzekere toekomst?
4. Roadmap: hoe bouw ik een roadmap als na stap 1 onduidelijk is of stap 2 de beste is?

Het zijn wicked problems. Het patroon om ermee te werken is verkennen en benutten.

Dag 1 introduceert alle vier. Elke sessie komt op de vragen terug en vergelijkt ze met de antwoorden die ontstaan (Purpose en Mastery). Elke deelnemer doet dat voor de eigen casus (Autonomy). Later vroeg de gebruiker bij vraag 3 ook reële opties en het principe van de two-way door van Bezos op te nemen.

## Besluit

- **Vier vragen in `DATA.vragen`.** V1 tot en met V4 hebben elk een taak, de resultaten van S&N die ze raken, een methode, een vaardigheid en tools. Programmablokken en deckonderdelen verwijzen ernaar met `v`. De vier vragen ordenen SN1–7 en vervangen ze niet (ADR-024).
- **Eén verklaring:** wicked problems (Rittel & Webber, 1973).
- **Eén patroon:** verkennen en benutten (March, 1991), in drie talen:
  - de portfoliokaart (Osterwalder e.a., 2020);
  - de meerarmige bandiet en Bayesiaans optimaliseren (Shahriari e.a., 2016), met de simulator van de trainer als demo;
  - reële opties (Myers, 1977; McGrath, 1999) met de two-way door (Bezos, 2016).
- **Een ritueel (FR-33).** Elke lesdag opent en sluit met de vier vragen, op de vragenkaart: dia 1 van het casusdeck.
  - Op dag 1 om 9:30 schrijft de deelnemer een nulmeting, vóór alle uitleg.
  - In elke afsluiting herschrijft de deelnemer wat veranderde, met de reden.
  - Aan het eind van dag 3 wordt de kaart het concept van de Conclusie. De missie in één zin hoort bij het eindantwoord op vraag 1.
- **Verdieping per dag.** Dag 1 introduceert alle vier en verdiept vraag 1 (FR-34). Dag 2 verdiept vraag 3 (FR-35), dag 3 vraag 2 en 4.
- **Deel 2.** Kolb en COM-B gaan eruit als ontwerpkader. Wicked problems en verkennen en benutten komen naast Pink. COM-B blijft een model uit de online omgeving.
- **Nabespreken.** In de werkplaats twee vragen in plaats van drie (FR-05). Het werkplaatslog vervalt.

## Overwogen alternatieven

- **Elke dag een eigen thema, zoals in 0.21** (visie, businesscase, verandering). Verworpen: dan lijkt een vraag na die dag af.
- **De vier vragen als eigen leerdoelen naast SN1–7.** Verworpen: ADR-024 houdt één laag doelen aan.
- **Een eigen interactieve demo van de bandiet bouwen.** Verworpen: de bestaande simulator laat dezelfde afweging zien.
- **Kolb als kader houden.** Verworpen: de lus van verkennen en benutten dekt de cyclus van ervaren, en zo blijft er één kader minder over.

## Gevolgen

- **Eén logboek in plaats van drie.** De deelnemer ziet de eigen vooruitgang, van de nulmeting tot de Conclusie.
- **Elke afsluiting kost 30 minuten.** Het risico is een ritueel zonder inhoud; dat staat als nieuw risico in deel 12.
- **De vragenkaart moet op één dia passen,** met vier vragen en vier momenten.
- **Een andere toon.** De definities van FR-30 blijven, maar de omslag van 11:00 gaat nu over alle vier de vragen.

## Raakt

Kop; deel 1, 2, 3, 5, 6.1, 8, 9, 11, 12 en de bronnen; `DATA.vragen` en het veld `v`; FR-05, FR-26, FR-30, FR-31, FR-33, FR-34 en FR-35; AC-02, AC-20, AC-21 en AC-22; `materiaal/vier-vragen.html`, `materiaal/bo-demo/`, `materiaal/index.html` en `materiaal/voorbeeldcasus.md`. Vervangt deels ADR-002 (de drie vaste vragen en het werkplaatslog) en ADR-026 (de missie in één zin, zonder ADR).
