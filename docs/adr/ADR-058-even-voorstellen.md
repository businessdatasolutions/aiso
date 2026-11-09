# ADR-058: De trainer stelt zich voor met zijn eigen werk

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-09 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De opening van dag 1 had een kennismaking "in één zin per persoon", maar de trainer stelde zich niet voor. De
deelnemers komen uit het bedrijfsleven en de publieke sector. Ze willen weten waarom deze trainer hen over AI-strategie
iets kan leren.

De trainer bouwt zelf: hij heeft 278 repos op GitHub, waarvan er 117 in 2025 en 2026 zijn aangemaakt (zonder forks), en
vier apps waar hij trots op is. Bonnenmonster staat in Google Play, Plinkie staat live, en Opgeruimd en Newmuzes zijn in
de maak. Daarmee doet hij voor wat de training leert: verkennen met kleine proeven, en overdragen wat werkt.

Er waren drie ontwerpen: één scherm met een tijdlijn ("De koers"), een werkplaats in 3D ("De werkplaats") en een
verhaal in drie stappen ("Ik doe wat jullie gaan doen"). De trainer koos het derde.

## Besluit

- **Een lespagina** `materiaal/voorstellen.html` met drie stappen:
  1. Een metrokaart (D3): handel, onderwijs, onderzoek en ondernemen zijn vier lijnen die samenkomen in "Deze training".
  2. Eén blokje per repo (Three.js), in kolommen per jaar: de sprong in 2025 en 2026, met echte aanmaakdatums.
  3. De vier apps op de portfoliokaart (D3), met T (ADR-055). Plinkie en Bonnenmonster reizen via T naar benutten.
- **Stap 1 en 2 om 9:30, stap 3 om 11:15.** In het blok van 9:30 geeft de trainer vóór de nulmeting geen voorbeeld en
  geen hint, en wijst hij niet vooruit naar 11:00. Stap 3 toont de portfoliokaart, en die hoort bij 11:15: daar is
  ze het tweede voorbeeld, na Voorbeeld BV. Stap 2 eindigt met de kennismaking: "En jij? Naam, rol en organisatie, in
  één zin."
- **Alleen openbare gegevens.** De bronnen zijn het openbare LinkedIn-profiel, de aanmaakdatums op GitHub en de repos
  van de apps. Er staan geen woonplaats, telefoon of privéprojecten in. Privérepos staan er zonder naam. Van de
  openbare repos krijgen er alleen twaalf een naam, omdat andere namen klanten, plaatsen of personen kunnen noemen.
- **Het logo van Plinkie** komt van plinkie.nl en is nagebouwd als SVG. Alle beelden en data staan in de pagina, want
  de site neemt uit `materiaal/` alleen HTML mee.

## Overwogen alternatieven

- **"De koers": één scherm met tijdlijn en 3D-kaarten.** Verworpen: snel, maar het minst sterk als verhaal.
- **"De werkplaats": vier werkbanken in 3D.** Verworpen: blijft hangen, maar de loopbaan is één regel, en het vraagt
  het meest van de beamer.
- **Alle drie de stappen om 9:30.** Verworpen: de portfoliokaart vóór de nulmeting kan de antwoorden kleuren.

De drie prototypes staan buiten de repo, in `~/Projects/aiso-voorstellen-ontwerpen/`.

## Gevolgen

- Het welkom duurt zeven minuten in plaats van vijf. De casus begint om 9:37 en de nulmeting om 9:42, met haar volle
  tien minuten. Filmpje 1 en werkregel 1 krijgen elk vier minuten in plaats van vijf.
- Om 11:15 komt er een tweede voorbeeld bij de portfoliokaart, in hetzelfde blok van vijf minuten.
- De cijfers zijn een momentopname van 9 november 2026. Bijwerken betekent: de pagina opnieuw maken met nieuwe data.

## Raakt

- `DATA.days`: dag 1 om 9:30 (detail, materiaal, verloop en letop) en om 11:00 (materiaal en verloop).
- `materiaal/voorstellen.html` (nieuw) en `materiaal/draaiboek-bouwstenen.md`.
- ADR-055: deze pagina gebruikt de portfoliokaart met T opnieuw.
