# ADR-022: Gereedschap: lekcheck vóór publicatie, schemascript en drie projectskills

| | |
|---|---|
| **Status** | Aanvaard |
| **Datum** | 2026-11-07 |
| **Besloten door** | Witek ten Hove (trainer en ontwerper) |
| **Document** | [LRD AISO26009 Lesdagen](../../LRD-AISO26009-lesdagen.html) |

## Context

De trainer publiceert de LRD als privé artifact (ADR-013). Deelnemersgegevens, het contract en lokale bestanden mogen daar nooit in (ADR-016, ADR-017). Tot nu toe stond de controle alleen als lijst in `CLAUDE.md`. De zorgsessie had een script dat de publieke build controleert op geheimen, en een script dat Excalidraw-schema's tekent in de huisstijl van Business Data Solutions. Ook had die repo drie skills die hier ontbraken: STE100, taalredactie voor publicatie, en het ontwerp van dia's.

## Besluit

- **Lekcheck.** Vóór elke publicatie draait `scripts/controleer-publicatie.py` op de kopie voor het artifact, zonder meldingen. Het script zoekt links naar lokale mappen, het contract, bedragen, lokale paden, echte voornamen en woorden uit `temp/verboden-woorden.txt`. De voornamen haalt het uit de bestandsnamen in `temp/`; de inhoud van die bestanden leest het niet. Het toont nooit een gevonden waarde. Met `--alleen-privacy` controleert het ook bestanden die in de repo blijven.
- **Schemascript.** `scripts/excalidraw-huisstijl.py` tekent een `.excalidraw`-bestand opnieuw als SVG met het systeemfont, rechte lijnen en het palet van het stijlboek.
- **Skills.** `aiso-ste100-writer`, `aiso-taalredactie-publicatie` en `aiso-ontwerp-dia` zijn kopieën zonder verwijzingen naar de HAN, zoals de andere `aiso-`skills. Het woordenboek van de STE100-skill komt uit de specificatie en is privé; het staat in `.gitignore`.

## Overwogen alternatieven

- **Alleen de lijst in `CLAUDE.md`.** Een lijst vergeet je onder tijdsdruk; een script niet.
- **Het controlescript in Node, zoals in de zorgsessie.** De andere scripts in deze repo zijn Python.
- **Het STE100-woordenboek in git zetten.** De specificatie staat verspreiding niet toe, ook niet in een privé-repo.

## Gevolgen

- Organisaties en achternamen controleert het script pas als de trainer `temp/verboden-woorden.txt` vult. Dat bestand gaat nooit mee in git.
- Bij een nieuwe kloon werkt `aiso-ste100-writer` pas als het woordenboek lokaal teruggezet is.
- `CLAUDE.md` noemt de lekcheck als stap vóór publicatie.

## Raakt

`scripts/`, `.claude/skills/`, `.gitignore`, `CLAUDE.md` (publiceren, commando's), ADR-013.
