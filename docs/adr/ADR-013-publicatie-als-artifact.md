# ADR-013: Publicatie als artifact zonder lokale bijlagen

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-05 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De trainer wil de LRD als artifact publiceren. De pagina verwijst naar lokale bestanden, waaronder de overeenkomst met tarieven en de intakeantwoorden van deelnemers.

## Besluit

De LRD staat als privé artifact op https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7. Het HTML-bestand in de repo blijft de bron. Voor het artifact wordt een kopie gebouwd: zonder eigen html-, head- en body-tags, met links naar lokale bestanden als gewone tekst, de link naar de webpagina naar sn.nl/aiso, en ruimte voor de inkeping van telefoons. De pagina blijft bewust licht, omdat de huisstijl geen donker thema kent.

## Overwogen alternatieven

- **De bijlagen meepubliceren.** Tarieven en persoonsgegevens horen niet op een deelbare pagina.
- **Een donker thema toevoegen.** De huisstijl kent het niet.

## Gevolgen

- De pagina noemt deelnemers bij naam en functie; vóór delen eventueel een versie zonder namen maken (open).
- Na elke wijziging moet de artifactversie opnieuw worden gebouwd en gepubliceerd.

## Raakt

Publicatie; titel 'LRD AISO26009 Lesdagen'.
