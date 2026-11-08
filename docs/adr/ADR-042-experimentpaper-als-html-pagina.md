# ADR-042: Het experimentpaper als interactieve HTML-pagina, in zakelijk Nederlands volgens ASD-STE100

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Volgens ADR-041 schrijft de AI het experiment als wetenschappelijk paper. Over de vorm zei dat besluit niets. De deelnemer bewaarde het paper als document, bijvoorbeeld in Google Docs, in Word of als artifact.

De trainer wil twee dingen erbij:

1. **De vorm.** De AI stelt het paper op als een HTML-pagina die de lezer wil verkennen. Op die pagina staan schema's, diagrammen, grafieken, demo's en simulaties. De AI gebruikt daarvoor de beste bibliotheken: D3, Three.js, Remotion of Motion.
2. **De taal.** De AI schrijft volgens de normen van ASD-STE100, maar in zakelijk Nederlands.

ADR-009 koos al eens een interactieve pagina voor het experimentverslag. ADR-034 schrapte die pagina, omdat ze extra thuiswerk was. ADR-009 noemde ook twee risico's. Het bouwen kan een technisch project worden. En AI maakt een fout resultaat net zo overtuigend als een goed resultaat.

## Besluit

- **Eén HTML-pagina.** Het paper is één zelfstandig HTML-bestand, als artifact of in canvas. De deelnemer bewaart het met de datum in de naam, net als het casusdeck.
- **Drie tot vijf visualisaties.** Elke visualisatie legt iets uit wat tekst alleen slecht laat zien. De lespagina geeft per deel van het paper een voorbeeld:
  - een schema van de strategische vraag naar de hypotheses;
  - een kaart van de bronnen;
  - een vergelijking van de ontwerpen;
  - een demo van het besluit: bij welk resultaat ga je door, pas je aan of stop je;
  - een grafiek van de resultaten.
- **De bibliotheken.** D3, Three.js en Motion laden van jsDelivr, in dezelfde vaste versies als de LRD, elk met een eigen import(). Remotion alleen als de omgeving React draait en een korte video iets uitlegt.
- **Eerlijke visualisaties.** Elk getal in een visualisatie staat ook in de tekst, met bron of meting. Een verzonnen getal in een demo heet "illustratie". Een simulatie is een model en geen bewijs.
- **Altijd bruikbaar.** De tekst, de tabellen en de bronnen werken ook zonder bibliotheek. De pagina werkt lokaal, op een telefoon en als PDF. Onderaan staat "Einde paper", en de laatste regel is `<!-- einde paper -->`. Zo valt een afgekapt bestand op, net als bij het casusdeck.
- **De volgorde.** Eerst het onderzoek en de tekst, dan de pagina. Geeft de onderzoeksfunctie een gewoon rapport terug, dan vraagt de deelnemer met één zin om de HTML-pagina.
- **De schrijfstijl.** De AI schrijft in zakelijk Nederlands volgens de schrijfregels van ASD-STE100 (Issue 9). Het Engelse woordenboek van STE geldt niet. De regels gelden wel:
  - hooguit 25 woorden per beschrijvende zin, en 20 per instructie;
  - één onderwerp per zin en per alinea, en hooguit zes zinnen per alinea;
  - de bedrijvende vorm en een werkwoord voor een handeling;
  - één term per begrip, en samenstellingen van hooguit drie delen;
  - geen puntkomma en geen afkortingen als "bijv.".

  De prompts voor het voorstel en de uitwerking hebben de volledige regels. De prompt voor de keuze heeft een korte versie.
- **Werkplaats 2.** Het duo controleert ook één getal uit een visualisatie.

## Overwogen alternatieven

- **Eén diagram, zoals in ADR-009.** Verworpen: de trainer wil een pagina die de lezer wil verkennen. De deelnemer bouwt zelf niets, dus meer visualisaties kosten geen tijd van de deelnemer.
- **Geen grens aan het aantal visualisaties.** Verworpen: dan wordt de pagina een etalage. Drie tot vijf, die elk iets uitleggen.
- **Een document met losse afbeeldingen.** Verworpen: dan is er geen demo of simulatie, en de lezer kan niets zelf proberen.
- **STE in het Engels.** Verworpen: de deelnemers en hun boards werken in het Nederlands.
- **Geen schrijfregels.** Verworpen: een AI schrijft lange zinnen met naamwoordstijl. Met de regels van STE is de tekst snel te lezen, en kan hij maar op één manier begrepen worden.

## Gevolgen

- **De vorm kan de inhoud overstemmen.** Een mooie grafiek maakt een fout getal overtuigend. Daarvoor is er een nieuw risico in deel 12, met de maatregelen uit dit besluit.
- **De omgeving maakt verschil.** Claude, ChatGPT en Gemini tonen HTML elk op een eigen manier. Een onderzoeksfunctie geeft soms een rapport in plaats van een pagina. De trainer test de prompts in fase 2 in alle drie de omgevingen. De vraag is: werkt de pagina lokaal, op een telefoon en als PDF?
- **Langere prompts.** Het voorstel heeft nu regels voor de inhoud, de stijl en de vorm. Daarom vraagt de prompt eerst het onderzoek en de tekst, en pas daarna de pagina.
- **STE in het Nederlands.** STE is een norm voor het Engels. We nemen de regels over, en niet het woordenboek. Een deelnemer die het paper in het Engels nodig heeft, kan het woordenboek alsnog gebruiken.

## Raakt

FR-38, AC-14 (product), het programma van dag 2 (12:30), deel 6.5 (de kaart "Het experiment als paper"), deel 12 (één nieuw risico), fase 2 en de bronnen (ASD-STE100). Ook `materiaal/experimentpaper.html` (de drie prompts, de opbouw en de stappen) en `materiaal/draaiboek-bouwstenen.md`. Bouwt voort op ADR-041. Neemt het idee van ADR-009 weer op, nu met een AI die bouwt.
