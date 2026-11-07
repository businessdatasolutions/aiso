# ADR-024: De resultaten van S&N als enige doelen; geen leeruitkomsten en geen Bloom

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De LRD had twee lagen doelen. Bovenaan stonden de zeven resultaten die S&N op de webpagina van de training belooft (SN1–7). Daaronder stonden negen eigen leeruitkomsten (LU1–9), elk met een tag uit de taxonomie van Bloom. Elke eis en elk programmablok verwees naar leeruitkomsten, en de leeruitkomsten verwezen naar de resultaten.

De trainer wil de LRD meer volgens KISS bouwen. De resultaten van S&N staan in de overeenkomst van opdracht, en daarop wordt de training afgerekend. LU1–7 herhaalden die resultaten grotendeels in andere woorden. Alleen LU8 (de eigen besluiten beoordelen, met boards en ADR's) en LU9 (een experiment opzetten) voegden iets toe dat niet in de resultaten staat.

## Besluit

- **De zeven resultaten van S&N zijn de enige doelen van de lesdagen.** `DATA.lu` vervalt. Elke eis, elk programmablok, elke werkplaats en elke deelnemerskaart verwijst met `sn` rechtstreeks naar de resultaten.
- **De omzetting keert de bestaande koppeling om.** LU1, LU2 en LU6 vallen onder SN1, en LU2 ook onder SN2. LU3 en LU5 vallen onder SN3, LU4 onder SN4, en LU7 onder SN5, SN6 en SN7.
- **LU8 en LU9 hangen onder de resultaten.** Het experiment (LU9) is de eerste mijlpaal van de roadmap en valt onder SN3. De boards en het ADR-register (LU8) toetsen de visie, de businesscase en het buildplan. Een eis met LU8 houdt de resultaten van de andere leeruitkomsten in dezelfde lijst. Vier eisen dienen daardoor geen resultaat direct: FR-08 en FR-13 (feedback van andere deelnemers) en FR-11 en FR-12 (regie). Hetzelfde geldt voor de opening, de afsluitingen en de rondgang in het programma. Zo zijn ook de meeste NFR's al opgezet.
- **De taxonomie van Bloom vervalt helemaal.** Dat geldt voor kader 2.1, de matrix in deel 3, de assen in `DATA` en de bron (Anderson & Krathwohl, 2001). Deel 2 houdt drie kaders: Pink (2.1), Kolb (2.2) en COM-B (2.3).
- **Deel 3 heet "Doelen".** Het toont de rol en de tabel met de zeven resultaten. Bij elk resultaat staan de lesdagen, berekend uit de programmablokken.
- **De herleidbaarheid in deel 7 heeft drie kolommen**: resultaat van S&N, eis, acceptatiecriterium. De dekkingsregel controleert of elk resultaat minstens één eis en één acceptatiecriterium heeft.
- **De getypte verwijzingen tussen haakjes in de AC-teksten vervallen**, zoals "(LU4)". Ze herhaalden wat de keten in deel 7 al laat zien.

## Overwogen alternatieven

- **Het axioma van Bloom houden, zonder tags en matrix.** Dan bleef het argument staan dat de klassikale tijd naar toepassen, evalueren en creëren gaat. Verworpen: de trainer kiest voor de eenvoudigste vorm. Dat argument staat al grotendeels in kader 2.2: de werkplaats begint met doen.
- **Bloom-tags op de zeven resultaten.** Dan bleef de matrix bestaan, maar met tags op woorden die S&N heeft gekozen. Het niveau ligt dan al vast in de formulering, dus de matrix toont geen ontwerpkeuze meer.
- **LU8 en LU9 houden als twee eigen doelen van de trainer.** De bedoeling bleef dan expliciet, maar er bleven ook twee lagen doelen. Precies die laag wil dit besluit kwijt.
- **De mechanismen schrappen die geen resultaat van S&N dienen.** Dan gingen de boards, het ADR-register en het experiment eruit. Dat raakt het kernmechanisme in deel 6 en een groot deel van dag 2 en 3. Verworpen omdat ze middelen zijn voor SN2–4.

## Gevolgen

- De LRD heeft één laag doelen minder, en de koptekst telt "7 resultaten van S&N" in plaats van "9 leeruitkomsten".
- Er is geen expliciete toets van het cognitieve niveau meer. Dat het ontwerp op toepassen en creëren mikt, volgt nu uit de werkvormen (werkplaats, bouwstraat, boards) en niet uit een matrix.
- Wat LU8 beoogde, de eigen rol en de eigen besluiten beoordelen, staat niet meer als doel in de LRD. Het leeft voort in FR-17, FR-18, FR-25 en AC-12.
- Vier eisen en vijf programmablokken dienen geen resultaat direct. De KISS-scan die op dit besluit volgt, kijkt of ze nodig zijn.
- ADR-011 is deels vervangen: de resultaten blijven de basis, maar de koppeling via leeruitkomsten en de verbreding van LU7 vervallen. De inhoud van LU7 blijft bestaan in FR-24 en AC-16.
- De projectskill `aiso-building-lrds` beschrijft deel 3 nog als leeruitkomsten met Bloom-tags. Voor deze LRD gaat dit besluit voor.

## Raakt

Kop (telling, navigatie, inhoud), deel 1, deel 2 (kader 2.1 vervalt, 2.2–2.4 worden 2.1–2.3), deel 3, deel 4, deel 5.1 (een nieuwe KISS-keuze en de tekst van twee bestaande), deel 7 (diagram en dekkingsregel), deel 8 (detailpaneel en printtabel), deel 10, deel 11 (13 AC-teksten, AC-09), bronnen; FR-11, alle FR's en NFR's (`lu` wordt `sn`), `DATA.lu`, `bloomP`, `bloomK`; ADR-011.
