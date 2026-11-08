# ADR-045: De LRD en de lespagina's als site op GitHub Pages

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-08 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De startpagina `materiaal/index.html` leest het programma uit de LRD. Daarom werkt ze alleen als een webserver de bestanden aanbiedt (ADR-021). In de zaal betekent dat: de laptop van de trainer draait Live Server of `python3 -m http.server`. Deelnemers kunnen de lespagina's niet zelf openen via een link.

De repo `businessdatasolutions/aiso` is sinds 7 november openbaar. De trainer houdt dat zo. Alles wat in git staat, is dus al te lezen. De overeenkomst met de tarieven en de map `temp/` staan niet in git (ADR-016, ADR-017). De lekcheck op alle tekstbestanden in git vond geen deelnemersgegevens.

## Besluit

De LRD en de lespagina's komen op GitHub Pages: https://businessdatasolutions.github.io/aiso/. Het adres zonder pad stuurt door naar de startpagina `materiaal/`.

- **Een gebouwde selectie, geen kopie van de repo.** `scripts/bouw-pages.py` zet de LRD en alle HTML-pagina's uit `materiaal/` in `_site/`. Ook de simulator uit `materiaal/bo-demo/` gaat mee, met de afbeeldingen en de licentie. Het script neemt alleen bestanden die in git staan.
- **Wat niet op de site staat, wordt gewone tekst.** Het script maakt in de LRD gewone tekst van elke link naar een bestand buiten de site. Dat geldt voor `background-docs/`, `temp/`, `onderzoek/`, `docs/`, `CHANGELOG.md` en de `.md`-bestanden in `materiaal/`. De link naar de cursuspagina gaat naar https://www.sn.nl/aiso. De regel geldt dus niet per map: een nieuw bestand voor de trainer valt er vanzelf onder.
- **Elke push naar `main` publiceert.** De GitHub Action `.github/workflows/pages.yml` bouwt de site en draait daarna `controleer-publicatie.py --site _site`. In die modus mogen links naar `materiaal/`, maar elke relatieve link moet naar een bestand op de site wijzen. Vindt de check iets, dan stopt de publicatie.
- **De namencontrole draait lokaal.** In de Action ontbreekt `temp/`, dus daar controleert het script geen voornamen en verboden woorden. Omdat de repo openbaar is, is de push zelf al het moment van publicatie. Daarom draait de volledige controle lokaal vóór de push, zoals nu al.

Het artifact uit ADR-013 blijft bestaan.

## Overwogen alternatieven

- **Pages direct uit `main`, zonder bouwstap.** Verworpen: dan staan de ADR's, het onderzoek, de achtergronddocumenten en CLAUDE.md ook op de site. De LRD zou bovendien dode links hebben, met de bestandsnaam van de overeenkomst erin.
- **Een aparte openbare repo, zoals `aiso-casusdeck` (ADR-035).** Verworpen: dan kopieert de trainer elke wijziging met de hand. Dat is nodig voor een privé repo, en deze repo is openbaar.
- **Alleen de lespagina's, zonder de LRD.** Verworpen: de startpagina haalt het programma uit de LRD, dus de LRD moet op de site staan.

## Gevolgen

- De startpagina werkt nu ook online: `…/aiso/materiaal/?dag=1`. Lokaal is nog steeds een server nodig.
- Een wijziging in de LRD of in `materiaal/` staat na de push binnen een paar minuten online. Een fout in de lekcheck houdt de vorige versie online.
- Het materiaal per blok in deel 8 toont een link zonder doel als gewone tekst. Dat gebeurt nu nog niet, want alle paden in `DATA` wijzen naar een pagina op de site.

## Raakt

Publicatie; `materiaal/index.html` (de startpagina); `materiaal/draaiboek-bouwstenen.md` (voorbereiding); `scripts/bouw-pages.py` en `scripts/controleer-publicatie.py`.
