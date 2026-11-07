# ADR-027: De boards als skill, met een startsjabloon om in te vullen

| | |
|---|---|
| **Status** | Deels vervangen door [ADR-028](ADR-028-experts-en-strategen-in-de-boards.md): de leden van beide boards in het sjabloon, en de commissarissen |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

ADR-006 besloot tot twee boards per deelnemer, gebouwd met een startsjabloon van de trainer. FR-17 beschreef dat sjabloon als twee instructieteksten voor een ChatGPT-project, een Claude Project of een Gemini Gem. Elk van die drie vraagt een eigen werkwijze, en de tekst moet er met de hand in.

Sinds najaar 2026 lezen Claude, ChatGPT en Gemini hetzelfde open formaat voor skills. Een skill is een map met een bestand `SKILL.md`, met bovenin een naam en een beschrijving. Gecontroleerd op de helppagina's op 7 november 2026:

- **Claude:** skills op alle plannen, ook gratis, mits code-uitvoering aan staat. Uploaden als zip via Customize › Skills. Een beschrijving mag hooguit 200 tekens hebben.
- **ChatGPT:** uploaden via Skills › Create › Upload from your computer. ChatGPT controleert een skill eerst. De helppagina noemt alleen de werkruimteplannen (Business, Enterprise, Edu, Healthcare).
- **Gemini:** skills op elk persoonlijk Google-account vanaf 18 jaar, ook zonder abonnement, en op Workspace. Uploaden als `SKILL.md` of zip, alleen op het web en in de Mac-app. Google vervangt Gems: bij persoonlijke accounts zijn Gems vanaf 17 november 2026 alleen-lezen en op 17 december 2026 weg. Bij Workspace blijven ze tot ten minste maart 2027.

Een board dat op 12 november als Gem gebouwd wordt, werkt op dag 2 dus niet meer. Dat geldt ook voor de reserve-accounts van de trainer (NFR-03): dat zijn persoonlijke accounts.

## Besluit

- **Elk board is een skill:** `advisory-board` en `supervisory-board`, in het open formaat, met alleen `name` en `description` bovenin. Die werken in alle drie de omgevingen.
- **Het startsjabloon is een pagina,** `materiaal/boards.html`. De deelnemer vult de eigen organisatie, de leden en de commissarissen in. De pagina controleert de eisen uit FR-17 (aantallen, een harde scepticus per board) en maakt per board een zip met `<naam>/SKILL.md`. De tekst van de skills staat alleen op die pagina.
- **De pagina is één los bestand,** zonder server, bibliotheek of internet. Ze maakt de zip zelf en bewaart wat de deelnemer invult alleen in de eigen browser. Zo kan de trainer haar als bestand meegeven of in de leeromgeving zetten.
- **Per aanbieder een korte instructie,** met een terugvaloptie: de tekst als instructie van een project. De pagina noemt de datum van de laatste controle.
- **Beide skills sluiten af met drie regels voor de ADR** van het boardmoment (FR-18), en bevatten de eerlijkheidsregels uit deel 6.3.
- Commissarissen krijgen een rol of een verzonnen naam, nooit de naam van een echte collega.

## Overwogen alternatieven

- **Instructieteksten per aanbieder, zoals in FR-17.** Drie werkwijzen om uit te leggen, en de Gem-variant werkt na 17 november niet meer.
- **Eén skill met beide boards.** Eén upload minder, maar dan bepaalt de AI welk board spreekt. In één board wint de luidste stem (KISS-keuze in deel 5), en het verschil tussen verbreden en toetsen verdwijnt.
- **Twee Markdown-bestanden om zelf aan te vullen.** Dat scheelt een pagina. Een deelnemer moet dan zelf de map en de zip maken, en niets controleert de scepticus of de aantallen.
- **Een bibliotheek voor de zip, zoals JSZip van een CDN.** Minder eigen code, maar de pagina werkt dan niet zonder internet in de zaal.

## Gevolgen

- Werkplaats 1 kost geen extra tijd: invullen en uploaden vervangt het plakken van een instructietekst.
- Een deelnemer met ChatGPT zonder werkruimteplan ziet misschien geen Skills. Die gebruikt de terugvaloptie. Het board werkt dan hetzelfde, alleen in een vast project.
- Menu's en plannen veranderen vaak. In fase 0 laadt de trainer beide zips in alle drie de omgevingen en in een reserve-account. Twee nieuwe risico's in deel 12.
- De startpagina toont het sjabloon bij werkplaats 1, en "Zo gebruik je je boards" bij de drie boardmomenten (veld `materials`).
- Het advisory board neemt zijn ledenlijst en werkwijze over van het virtuele board van de trainer (skill `virtual-board`). Het supervisory board neemt de regel "per commissaris één stem" over uit het ontwerp van de Raad van Commissarissen (project `ai-consultant`).
- ADR-006 blijft staan: de twee boards en de boardmomenten veranderen niet, alleen de vorm van het sjabloon.

## Raakt

Deel 5 (KISS, twee boards), deel 6.3, FR-17, AC-12, werkplaats 1 (opdracht), het programma (werkplaats 1 en de boardmomenten, `materials`), de opleverlijst van de trainer, risico's (deel 12), fase 0, Bronnen, `materiaal/boards.html`, `materiaal/draaiboek-bouwstenen.md`.
