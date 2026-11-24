# ADR-066: Het lege casusdeck in elk deckblok, en een melding bij een leeg profiel

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-24 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

Op 24 november liep een gebruikerstest met vier gesimuleerde deelnemers op de lespagina's (rapport in
`onderzoek/ui-toets/2026-11-24-gebruikerstest/`). De deelnemers waren persona's, geen echte deelnemers; de
bevindingen zijn hypothesen. Twee bevindingen kwamen bij alle vier terug.

- **Het lege casusdeck was moeilijk te vinden.** De link stond alleen in het deckblok van dag 1, om 15:15. De
  deckblokken van dag 2 en dag 3 hadden geen link, terwijl een deelnemer die van laptop wisselt of het bestand kwijt
  is, het juist dan zoekt. De linktekst zei "dia 1 is je vragenkaart", maar op de downloadpagina staat de vragenkaart
  vóór "Dia 1 van 10".
- **Een leeg profiel in de volwassenheidsscan leek op verloren werk.** De antwoorden blijven in de browser waarin ze
  zijn ingevuld. In een andere browser staat het profiel op "nog niet ingevuld". De uitleg daarover stond onder de
  knoppen, niet bij het profiel. Het profiel komt terug op dag 1 om 11:40, dag 2 om 11:45 en dag 3 om 11:00.

## Besluit

- **Elk deckblok heeft het lege casusdeck als materiaal**, met dezelfde linktekst op dag 1, 2 en 3: "Leeg casusdeck
  om te downloaden (tien dia's, met je vragenkaart voorop)".
- **De volwassenheidsscan toont een melding boven een leeg profiel.** Zolang geen enkele dimensie is ingevuld, staat
  direct onder de kop "Je profiel" dat de antwoorden in de browser van het invullen staan, dat ze niet weg zijn, en wat
  de deelnemer dan doet: die laptop openen, of het tekstbestand gebruiken. De melding verdwijnt zodra er één dimensie
  is gekozen.

## Overwogen alternatieven

- **Een vaste link naar het casusdeck in de kop van elke dagpagina, naast Overzicht.** Verworpen: de kop heeft vier
  knoppen die het programma ordenen; een vijfde voor één bestand maakt hem drukker. De link in elk deckblok staat waar
  de deelnemer het deck gebruikt.
- **De antwoorden van de scan opslaan buiten de browser.** Verworpen: de pagina stuurt bewust niets weg (privacy van
  de deelnemer), en een account past niet bij lespagina's zonder installatie (NFR-02).
- **Het tekstbestand weer kunnen inladen.** Niet nu: het vraagt een uploadknop en een lezer voor het formaat. De
  melding wijst de weg; zelf overnemen kost een paar minuten.

## Gevolgen

- Op dag 2 en dag 3 vindt een deelnemer het lege deck in het blok waar hij het deck gebruikt.
- De bevindingen rusten op een simulatie. De trainer kan ze op dag 2 controleren: bij het deckblok en bij het profiel
  om 11:45 vragen wie het bestand of het profiel niet direct vond.
- De andere bevindingen uit het rapport (de vastgezette band tijdens pauzes, uitleg van termen als rem en 7S, de kop
  van het overzicht) zijn nog open.

## Raakt

- LRD: `DATA.days`, de deckblokken van dag 1, 2 en 3 (materials).
- `materiaal/volwassenheidsscan.html` (stap 3, Je profiel).
- `materiaal/index.html` rendert de materials; die code verandert niet.
