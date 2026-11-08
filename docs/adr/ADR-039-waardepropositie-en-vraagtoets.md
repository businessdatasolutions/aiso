# ADR-039: Waardepropositie en vraagtoets voor de strategische AI-vraag

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

In een tweede sessie werkte de gebruiker op 8 november aan de waardepropositie en nam vijf besluiten:
- **De lead** moet zeggen waaraan de deelnemer werkt en wat het oplevert. De eigen organisatie is alleen de context.
- **"Hoe handelen we klachten sneller af?"** is operationeel, en geen strategische vraag.
- **Een definitie en een meetinstrument.** De groep spreekt af wat een goede vraag op strategisch niveau is. Daar komen een definitie en een meetinstrument voor, eventueel met AI.
- **De AI als tweede beoordelaar.** Eerst scoren de deelnemer en het duo, dan de AI. De trainer ijkt de AI vóór dag 1.
- **Voorbeeld BV** krijgt vraag C, over de klantrelatie.

De gebruiker koos de toets na de omslag en vóór de doelen. In deze sessie werd dat 11:40.

Beide sessies schreven tegelijk in de LRD. De gebruiker besloot dat de sessie van versie 0.22 het werk samenvoegt.

## Besluit

- **Een nieuwe sectie in deel 1: "Waarvoor de deelnemer komt".** Ze bevat:
  - de definitie van een strategische AI-vraag;
  - de drie niveaus van de integrale opdracht, met Voorbeeld BV;
  - de waardepropositie en de klus waarvoor de deelnemer komt (job to be done);
  - pijnpunten en winst uit `DATA.value`, met bij elk pijnpunt de vraag die het raakt;
  - twee gebruikersverhalen;
  - een kaart die zegt dat dit een aanname is.

  De strategische vraag is vraag 1 in de taal van de eigen casus.
- **Een nieuwe lead.**
- **De vraagtoets (FR-36).** Drie criteria: Omgeving, Positie en Keuze, elk met een score van 0, 1 of 2. Er is geen totaalscore, wel een beslisregel. De groep oefent op drie vragen van Voorbeeld BV en scherpt de definitie aan. Dan scoren de deelnemer en het duo. In de lunch scoort de AI, via het supervisory board.
- **De ijking (FR-37).** Negen vragen, met de norm dat de AI er minstens acht goed beoordeelt, in Claude, ChatGPT en Gemini.
- **AC-23.**
- **FR-01** spreekt van een voorlopige vraag, die na de toets vastligt.
- **Dag 1.** "Waarom geen plan volstaat" duurt 11:00–11:40. Daarna volgt 11:40–12:15: eerst de vraagtoets, dan de doelen.
- **Materiaal:**
  - `materiaal/vraagtoets.html` en `materiaal/vraagtoets-ijkset.md`;
  - in `materiaal/boards.html` een veld en een prompt voor de strategische vraag;
  - in `materiaal/voorbeeldcasus.md` de nieuwe strategische vraag.
- **Bronnen:** Christensen e.a. (2016), Osterwalder e.a. (2014), Gillespie e.a. (2025), PwC (2026) en Porter (1996).
- **Bij het samenvoegen herschreven:** de regels over het ADR-register, de rondgang, het regelboek en het buildplan. De nummers van de toets en de ijking werden FR-36 en FR-37.

## Overwogen alternatieven

- **Een totaalscore, of een strategiemodel als lesstof** (Rumelt). Verworpen: een totaal verbergt welk criterium zwak is.
- **De AI als enige beoordelaar, of geen AI.** Verworpen: wie eerst het oordeel van de AI ziet, neemt het over. En zonder AI ziet de groep niet hoe je een AI ijkt.
- **Een definitie die de groep vanaf nul bouwt.** Verworpen: dat lukt niet in tien minuten.
- **De toets in de opening van 9:30.** Verworpen: hij komt dan vóór de omslag, en de opening is vol.
- **De toets in het blok van 30 minuten om 11:45.** Verworpen: dan houden de doelen 20 minuten over.

## Gevolgen

- **Het blok van 11:00 wordt 5 minuten korter.**
- **De trainer ijkt de prompt vóór dag 1** (fase 0).
- **Twee nieuwe risico's in deel 12:** de AI oordeelt anders dan deelnemer en duo, of de toets loopt uit.
- **Deel 1 wordt langer.** De pijnpunten en de winst komen uit `DATA`, dus de vier vragen en de eisen blijven op één plek.

## Raakt

Kop; deel 1, 2.3, 4, 5.1, 5.2, 6.2, 7, 8, 10, 11, 12, 13 en de bronnen; `DATA.value`; FR-01, FR-36 en FR-37; AC-23; `materiaal/vraagtoets.html`, `materiaal/vraagtoets-ijkset.md`, `materiaal/boards.html` en `materiaal/voorbeeldcasus.md`.
