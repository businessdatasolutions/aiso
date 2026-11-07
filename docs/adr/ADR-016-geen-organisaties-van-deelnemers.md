# ADR-016: Geen organisaties van deelnemers in documenten

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De LRD noemde bij twee deelnemers hun werkgever of eigen bedrijf, en bij één deelnemer het werkdomein dat naar de werkgever wijst. Een voornaam en een functie kunnen al een persoonsgegeven zijn als de naam weinig voorkomt. Komt daar een organisatie bij, dan is de persoon herkenbaar.

## Besluit

Documenten die we bouwen noemen nooit de werkgever, het eigen bedrijf of een herkenbaar werkdomein van een deelnemer. Dat geldt voor de LRD, ADR's, het wijzigingslog, rapporten, artifacts en logs in andere repositories. Deelnemers verschijnen hooguit met voornaam en een algemene rol. De ruwe inzendingen in `temp/` blijven ongewijzigd als invoer en worden nooit gepubliceerd. De regel staat in `CLAUDE.md` en in de skill `aiso-building-lrds`.

## Overwogen alternatieven

- **Organisaties laten staan.** Maakt deelnemers herkenbaar.
- **Ook voornamen vervangen door pseudoniemen.** Nog niet besloten.

## Gevolgen

- Deel 4 beschrijft de groep minder specifiek. Voor het ontwerp is de rol genoeg.
- Eerdere versies van het artifact (versie 1 en 2) bevatten de organisaties nog in de versiegeschiedenis van de pagina. Het artifact is privé.

## Raakt

Deel 4 (deelnemers en de opsomming over het hoog-risicodomein), een risico in deel 12, ADR-004, `CLAUDE.md`, skill `aiso-building-lrds`.
