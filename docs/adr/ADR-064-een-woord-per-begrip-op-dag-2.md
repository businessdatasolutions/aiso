# ADR-064: Dag 2 gebruikt één woord per begrip, en de resten van ADR-063 zijn weg

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-22 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Op 22 november is dag 2 beoordeeld op PAMS en KISS. De beoordelaar keek als deelnemer en als trainer die het
programma niet ontwierp. De startpagina haalde alle 32 KPI's van de UX-test (ADR-046), maar de inhoud had twee soorten
ruis.

De eerste soort: resten van de volgorde van vóór ADR-063.

- Een lespagina liet de businesscase om 11:30 maken.
- De kansenkaart zei "dit doe je voordat je de businesscase onderzoekt".
- De pagina over de deur die terug kan, die om 13:30 op het scherm staat, beloofde dat de deelnemer op dag 2 alle
  kansen op de portfoliokaart zet.
- FR-06, FR-20, een KISS-keuze, een risico, de rolkaarten en het draaiboek noemden nog een eerste proef in de
  werkplaats, een voorstel uit de lunch of een voorzitter die besluit.
- Deel 2 van de LRD zette de keuze van de rem en de aanjager nog op dag 3.
- ADR-048 koppelde het profiel van de volwassenheidsscan aan het transformatieplan, toen één blok op dag 3. ADR-063
  splitste dat blok in 11:00 en 11:45, en het profiel ging naar beide mee. Om 11:00 zei niets wat de deelnemer ermee
  doet. Om 11:45 had de deelnemer twee beginpunten: de werkkaart noemde de sterkste rem én de laagste score in de
  scan, en de scan wees naar de laagste van drie dimensies.

De tweede soort: woorden die botsen, of die uit het ontwerp komen.

- "Benutten" is op dag 1 de huidige business, op de portfoliokaart. In het model van Warner en Wäger betekent het
  een nieuwe kans grijpen. ADR-056 hield "Kansen benutten" en liet de trainer het verschil hardop zeggen.
- In het paper heten dezelfde dingen "maat" en "criterium", terwijl het paper zelf "één term voor één begrip" vraagt.
  "Criteria" zijn op dag 2 ook de kwaliteitscriteria van het comité.
- Verder: "twee portfolio's", "scandimensie", "Per deelnemer" achter "Je maakt", "dal" naast "dip", "de laatste
  regel van het bestand", namen van bibliotheken en een schrijfnorm in tekst voor de deelnemer, en "(Ask)", dat pas
  op dag 3 aan bod komt.

## Besluit

- **Kansen grijpen.** Het tweede vermogen van Warner en Wäger heet "kansen grijpen" (*seizing*). Dat geldt voor de
  tekening, de lespagina, de voorbeeldcasus, de LRD en het draaiboek. "Benutten" betekent alleen nog de huidige
  business, zoals op de portfoliokaart.
- **Benutten en verkennen, geen "twee portfolio's".** Om 11:00 pakt de deelnemer de zin bij vraag 2 van dag 1 erbij:
  wat benut je, en wat verken je? Bij "Je gebruikt" heet die zin zo.
- **Maat in het paper.** Wat een experiment meet, heet overal "maat", met een norm en een referentiewaarde. Dat geldt
  voor de lespagina, de prompts, de werkkaart van 14:00, de werkplaatsopdracht, FR-20 en AC-15. "Criteria" zijn
  alleen nog de kwaliteitscriteria van het comité.
- **Dip.** Het verloop van kosten en baten heet "eerst een dip, dan de winst", zoals op dia 4 van het casusdeck.
- **De werkkaart spreekt de taal van de deelnemer.**
  - "Je maakt" begint niet meer met "Per deelnemer".
  - "Scandimensie" wordt "je laagste score in de volwassenheidsscan".
  - "Kijk of onderaan '— einde casusdeck —' staat."
  - De volgende stap gaat naar "het actieplan in de leeromgeving".
  - Op de lespagina Experimentpaper staan geen namen van bibliotheken en geen schrijfnorm meer; de prompts houden ze.
  - Eén alinea laat zien hoe het samenhangt: eerste prioriteit, probleemstelling, kleine inzet, experiment. Het
    invulveld vraagt de eerste prioriteit en de kleine inzet apart.
- **Twee bronnen, elk met een eigenaar.** Terwijl de AI het voorstel schrijft, zoekt het duo één bron uit de
  businesscase op in het origineel (FR-14). Bij het kiezen zoekt de deelnemer zelf één bron uit het voorstel op
  (FR-20, AC-14).
- **Thuiswerk heet overal thuiswerk.** De eerste proef en het zelf scoren van vijf tot tien gevallen staan overal als
  huiswerk: in FR-06, FR-20, de lespagina Experimentpaper, het draaiboek en het risico bij een vastgelopen experiment.
- **Een verdieping in werkplaats 2 (FR-07).** "Je bent klaar als" krijgt erbij: "Eerder klaar? Laat een tweede model
  hetzelfde voorstel schrijven, en vergelijk de ontwerpen."
- **Het duo vergelijkt de antwoorden alleen op dag 1.** FR-33 volgt nu FR-18.
- **Het profiel van de volwassenheidsscan hoort bij 11:45.** Om 11:00 vervallen de tegel en de regel bij "Je
  gebruikt". Om 11:45 is de sterkste rem het enige beginpunt, en het profiel de toets: één actie pakt de rem aan, en
  één de laagste score op mensen en werk, data en technologie of richting en eigenaarschap. Dat staat in FR-24, op de
  werkkaart, in het verloop van de trainer, in het draaiboek en in de tip van de scan.
- **Ook bijgewerkt.**
  - De KISS-keuze over de werkplaats noemt de tijden per dag.
  - De KISS-keuze "één verklaring en één patroon" telt de probleemformulering als gereedschap.
  - Deel 2 zet de rem en de aanjager op dag 2 om 11:00.
  - De rolkaarten eindigen met een slotvraag voor het comité, in plaats van een besluit van de voorzitter.
  - De kennisvormen zijn in het draaiboek reserve.
  - De kansenkaart en de pagina over de deur die terug kan noemen het huiswerk en de eerste prioriteit.

## Overwogen alternatieven

- **"Kansen benutten" houden, en de trainer het verschil laten uitleggen (ADR-056).** Verworpen: dan herstelt de
  trainer in de zaal een woord dat het ontwerp zelf laat botsen, en de deelnemer leest het verschil nergens. "Grijpen"
  is gewoon Nederlands en ligt dicht bij *seizing*.
- **"Dal" op dia 4 van het casusdeck.** Verworpen: de decks van de deelnemers zeggen sinds dag 1 al "dip". Een
  nieuw leeg deck moet ook naar de openbare downloadpagina, en verandert de decks van de deelnemers niet.
- **"Criterium" in plaats van "maat".** Verworpen: de hypotheses noemen al een maat, dia 4 heeft een uitkomstmaat, en
  op dezelfde dag zijn "criteria" de kwaliteitscriteria van het comité.
- **Een duo in de afsluiting van dag 2 en 3.** Verworpen: FR-18 laat het duo alleen op dag 1 meekiezen, en de
  afsluiting van dertig minuten heeft er geen tijd voor. De tabel van ADR-059 blijft bij elf blokken.
- **Het duo ook de bron uit het voorstel laten opzoeken.** Verworpen: terwijl de AI schrijft, is er nog geen
  voorstel, en twee bronnen in 35 minuten past niet.

## Gevolgen

- Van ADR-056 vervalt het punt "De kolom heet Kansen benutten". De rest van ADR-056 blijft gelden.
- Het programma van dag 2 houdt dezelfde blokken en tijden. Dit besluit gaat over woorden en verwijzingen.
- De werkkaart van werkplaats 3 (dag 3) heeft nog geen verdieping. "Je bent klaar als" zit daar al op 22 woorden.
- Drie punten uit de beoordeling vallen buiten dit besluit:
  - de volgorde in het blok van 13:30 en de AI-taak van 10:45;
  - de tijd voor de onderzoeksfunctie in werkplaats 2;
  - het draaiboek voor 9:30, 15:15 en 16:00.

## Raakt

- LRD: deel 2 ("Hoe je ermee werkt"), twee KISS-keuzes, FR-06, FR-14, FR-20, FR-24, FR-33, FR-35, AC-14, AC-15, de
  pijn bij gat 2, de opdracht van werkplaats 2 en het risico bij een vastgelopen experiment.
- `DATA.days`: dag 2 om 9:30, 9:40, 11:00, 11:45, 13:30, 14:00, 15:15 en 16:00, en dag 3 om 9:40, 15:15 en 16:00.
- `materiaal/experimentpaper.html`, `transformeren.html`, `vier-vragen.html`, `kansenkaart.html`,
  `probleemformulering.html`, `volwassenheidsscan.html`, `voorbeeldcasus.md`, `draaiboek-bouwstenen.md` en
  `rolkaarten-kritiekpunten.md`. In `CLAUDE.md` komt het profiel op dag 2 alleen nog om 11:45 terug.
