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

Met --site MAP controleert het script de site voor GitHub Pages (ADR-045),
gebouwd met scripts/bouw-pages.py. Links naar materiaal/ mogen dan, maar elke
relatieve link moet naar een bestand in MAP wijzen:

    python3 scripts/controleer-publicatie.py --site _site $(find _site -name '*.html')

In de GitHub Action ontbreekt temp/. Daar doet de namencontrole niets; draai
de controle daarom ook lokaal vóór de push.

Exitcode 0: niets gevonden. Exitcode 1: er is iets gevonden.
"""
import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
TEMP = REPO / "temp"

# Bestanden in temp/ die geen voornaam als naam hebben.
GEEN_NAAM = {"deelnemers", "pseudoniemen", "verboden-woorden"}

VERBODEN_MAPPEN = ("background-docs/", "temp/", "onderzoek/", "docs/", "materiaal/")
# Ook href: '…' in een JavaScript-object, zoals de links bij het materiaal in DATA.
LINK = re.compile(r"""\b(?:href|src)\s*[=:]\s*["'`]([^"'`]*)["'`]""", re.IGNORECASE)
BEDRAG = re.compile(r"€\s?\d|\b\d[\d.]*,\d{2}\s?(?:euro|EUR)\b|\bEUR\s?\d", re.IGNORECASE)
LOKAAL = re.compile(r"file://|/Users/[A-Za-z]")
# Voor --site: href= en src= in HTML, href: in JavaScript. Niet src: in DATA, dat is een bronvermelding.
SITELINK = re.compile(r"""\bhref\s*[=:]\s*["'`]([^"'`]*)["'`]|\bsrc\s*=\s*["'`]([^"'`]*)["'`]""",
                      re.IGNORECASE)
GEEN_BESTAND = re.compile(r"(?:[a-z][a-z0-9+.-]*:|#|\?|//)|.*\$\{", re.IGNORECASE)


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


def verboden_link(doel: str, mappen=VERBODEN_MAPPEN) -> str | None:
    pad = doel.strip()
    while pad.startswith(("./", "../")):
        pad = pad.split("/", 1)[1]
    if pad.startswith(mappen) or pad in mappen:
        return f"een link naar {pad.split('/')[0]}/"
    if pad.split("#")[0] == "CHANGELOG.md":
        return "een link naar CHANGELOG.md"
    if "overeenkomst" in pad.lower():
        return "een link naar het contract"
    return None


def buiten_site(bestand: Path, doel: str, site: Path) -> bool:
    """Waar als een relatieve link niet naar een bestand in de site wijst."""
    doel = doel.strip()
    if not doel or GEEN_BESTAND.match(doel):
        return False
    pad = unquote(re.split(r"[#?]", doel, maxsplit=1)[0])
    if not pad:
        return False
    # Een href in DATA geldt vanaf de LRD; de LRD staat in de hoofdmap van de site.
    doelpad = (bestand.parent / pad).resolve()
    if doelpad.is_dir():
        doelpad = doelpad / "index.html"
    return not (doelpad.is_relative_to(site) and doelpad.is_file())


def controleer(bestand: Path, alleen_privacy: bool, namen, woorden, site: Path | None = None) -> list[str]:
    meldingen = []
    naam_patronen = [patroon(n) for n in namen]
    woord_patronen = [patroon(w) for w in woorden]
    mappen = tuple(m for m in VERBODEN_MAPPEN if m != "materiaal/") if site else VERBODEN_MAPPEN
    for nr, regel in enumerate(bestand.read_text(encoding="utf-8").splitlines(), start=1):
        if not alleen_privacy:
            for doel in LINK.findall(regel):
                wat = verboden_link(doel, mappen)
                if wat:
                    meldingen.append(f"{bestand}:{nr}: {wat}")
            if site:
                for treffer in SITELINK.findall(regel):
                    if buiten_site(bestand.resolve(), treffer[0] or treffer[1], site):
                        meldingen.append(f"{bestand}:{nr}: een link naar iets dat niet op de site staat")
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
    parser.add_argument("--site", type=Path, metavar="MAP",
                        help="controleer de site voor GitHub Pages: elke relatieve link wijst naar een bestand in MAP")
    args = parser.parse_args()
    site = args.site.resolve() if args.site else None
    if site and not site.is_dir():
        print(f"Niet gevonden: {args.site}", file=sys.stderr)
        return 2

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
        meldingen += controleer(bestand, args.alleen_privacy, namen, woorden, site)

    for m in meldingen:
        print(m)
    if meldingen:
        print(f"\n{len(meldingen)} melding(en). Publiceer niet voordat ze opgelost zijn.")
        return 1
    print(f"Geen meldingen in {len(args.bestanden)} bestand(en).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
