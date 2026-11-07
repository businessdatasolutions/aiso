#!/usr/bin/env python3
"""Controle vóór publicatie: staat er iets in de pagina dat niet openbaar mag?

De LRD gaat als privé artifact naar claude.ai (ADR-013). Deelnemersgegevens,
het contract en lokale bestanden horen daar nooit in (ADR-016, ADR-017).
Dit script zoekt naar:

- links (href, src, ook href: in JavaScript) naar background-docs/, temp/, onderzoek/, docs/,
  materiaal/ of CHANGELOG.md;
- een link naar het contract, of een bedrag in euro's;
- lokale paden (/Users/, file://);
- echte voornamen van deelnemers. Die haalt het script uit de bestandsnamen
  in temp/ (bijvoorbeeld temp/<voornaam>.md). De inhoud van die bestanden
  leest het niet;
- woorden uit temp/verboden-woorden.txt, als dat bestand er is: één woord of
  woordgroep per regel, # voor commentaar. Zet daar organisaties en
  achternamen in. Het bestand staat in temp/ en gaat dus nooit mee in git.

Het script toont nooit een gevonden waarde, alleen wat het is en op welke regel.

Gebruik:
    python3 scripts/controleer-publicatie.py ARTIFACT.html
    python3 scripts/controleer-publicatie.py --alleen-privacy LRD-AISO26009-lesdagen.html docs/adr/*.md

Met --alleen-privacy slaat het script de controle op links en lokale paden
over. Dan kun je ook de LRD in de repo, ADR's en het wijzigingslog
controleren; die mogen wel naar lokale bestanden linken.

Exitcode 0: niets gevonden. Exitcode 1: er is iets gevonden.
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TEMP = REPO / "temp"

# Bestanden in temp/ die geen voornaam als naam hebben.
GEEN_NAAM = {"deelnemers", "pseudoniemen", "verboden-woorden"}

VERBODEN_MAPPEN = ("background-docs/", "temp/", "onderzoek/", "docs/", "materiaal/")
# Ook href: '…' in een JavaScript-object, zoals de links bij het materiaal in DATA.
LINK = re.compile(r"""\b(?:href|src)\s*[=:]\s*["'`]([^"'`]*)["'`]""", re.IGNORECASE)
BEDRAG = re.compile(r"€\s?\d|\b\d[\d.]*,\d{2}\s?(?:euro|EUR)\b|\bEUR\s?\d", re.IGNORECASE)
LOKAAL = re.compile(r"file://|/Users/[A-Za-z]")


def voornamen_uit_temp() -> list[str]:
    """Voornamen uit de bestandsnamen in temp/, zoals temp/<naam>-opdracht-1.md."""
    if not TEMP.is_dir():
        return []
    namen = set()
    for pad in TEMP.iterdir():
        if pad.is_file() and pad.suffix == ".md":
            naam = pad.stem.split("-")[0].lower()
            if naam and naam not in GEEN_NAAM and len(naam) >= 3:
                namen.add(naam)
    return sorted(namen)


def verboden_woorden() -> list[str]:
    bestand = TEMP / "verboden-woorden.txt"
    if not bestand.is_file():
        return []
    woorden = []
    for regel in bestand.read_text(encoding="utf-8").splitlines():
        regel = regel.split("#", 1)[0].strip()
        if len(regel) >= 3:
            woorden.append(regel.lower())
    return woorden


def patroon(woord: str) -> re.Pattern:
    return re.compile(r"(?<![\w-])" + re.escape(woord) + r"(?![\w-])", re.IGNORECASE)


def verboden_link(doel: str) -> str | None:
    pad = doel.strip()
    while pad.startswith(("./", "../")):
        pad = pad.split("/", 1)[1]
    if pad.startswith(VERBODEN_MAPPEN) or pad in VERBODEN_MAPPEN:
        return f"een link naar {pad.split('/')[0]}/"
    if pad.split("#")[0] == "CHANGELOG.md":
        return "een link naar CHANGELOG.md"
    if "overeenkomst" in pad.lower():
        return "een link naar het contract"
    return None


def controleer(bestand: Path, alleen_privacy: bool, namen, woorden) -> list[str]:
    meldingen = []
    naam_patronen = [patroon(n) for n in namen]
    woord_patronen = [patroon(w) for w in woorden]
    for nr, regel in enumerate(bestand.read_text(encoding="utf-8").splitlines(), start=1):
        if not alleen_privacy:
            for doel in LINK.findall(regel):
                wat = verboden_link(doel)
                if wat:
                    meldingen.append(f"{bestand}:{nr}: {wat}")
            if LOKAAL.search(regel):
                meldingen.append(f"{bestand}:{nr}: een lokaal pad")
        if BEDRAG.search(regel):
            meldingen.append(f"{bestand}:{nr}: een bedrag in euro's")
        if any(p.search(regel) for p in naam_patronen):
            meldingen.append(f"{bestand}:{nr}: een echte voornaam van een deelnemer")
        if any(p.search(regel) for p in woord_patronen):
            meldingen.append(f"{bestand}:{nr}: een woord uit temp/verboden-woorden.txt")
    return meldingen


def main() -> int:
    parser = argparse.ArgumentParser(description="Controle vóór publicatie van de LRD.")
    parser.add_argument("bestanden", nargs="+", type=Path)
    parser.add_argument("--alleen-privacy", action="store_true",
                        help="sla de linkcontrole over (voor bestanden die in de repo blijven)")
    args = parser.parse_args()

    namen, woorden = voornamen_uit_temp(), verboden_woorden()
    if not namen:
        print("Let op: geen voornamen gevonden in temp/. De namencontrole doet niets.", file=sys.stderr)
    if not woorden:
        print("Let op: temp/verboden-woorden.txt ontbreekt of is leeg. "
              "Organisaties en achternamen worden niet gecontroleerd.", file=sys.stderr)

    meldingen = []
    for bestand in args.bestanden:
        if not bestand.is_file():
            print(f"Niet gevonden: {bestand}", file=sys.stderr)
            return 2
        meldingen += controleer(bestand, args.alleen_privacy, namen, woorden)

    for m in meldingen:
        print(m)
    if meldingen:
        print(f"\n{len(meldingen)} melding(en). Publiceer niet voordat ze opgelost zijn.")
        return 1
    print(f"Geen meldingen in {len(args.bestanden)} bestand(en).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
