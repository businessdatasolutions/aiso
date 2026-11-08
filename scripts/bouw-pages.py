#!/usr/bin/env python3
"""Bouw de site voor GitHub Pages: de LRD en de lespagina's (ADR-045).

Gebruik:
    python3 scripts/bouw-pages.py _site
    python3 scripts/controleer-publicatie.py --site _site $(find _site -name '*.html')

Op de site komen alleen bestanden die in git staan:
- de LRD. Een link naar een bestand dat niet op de site staat, wordt gewone tekst;
  de link naar de cursuspagina gaat naar sn.nl/aiso;
- alle HTML-pagina's in materiaal/;
- de simulator in materiaal/bo-demo/, met de afbeeldingen en de licentie;
- een index.html die doorstuurt naar de startpagina materiaal/.

Niet op de site: background-docs/, temp/, onderzoek/, docs/, CHANGELOG.md en de
.md-bestanden in materiaal/ (trainermateriaal). De GitHub Action
.github/workflows/pages.yml draait dit script en daarna de lekcheck.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

REPO = Path(__file__).resolve().parent.parent
LRD = "LRD-AISO26009-lesdagen.html"
CURSUSPAGINA = "background-docs/AI%20Strategie%20en%20Organisatietransformatie.pdf"

# Een relatief pad naar een bestand, eventueel met #anker of ?vraag. Zo raakt de
# bewerking geen JavaScript zoals '<a href="' + x + '">' of `${esc(m.href)}`.
RELATIEF = re.compile(r"[A-Za-z0-9_./%-]+(?:[#?][^\"']*)?")
PROZALINK = re.compile(r'<a\s[^>]*?href="([^"]*)"[^>]*>(.*?)</a>', re.S)
DATALINK = re.compile(r"href: '([^']*)'")

# De weergave van het materiaal per blok in Deel 8: een leeg href wordt gewone tekst.
OUD = ': `<a href="${esc(m.href)}">${esc(m.label)}</a>`'
NIEUW = ': m.href ? `<a href="${esc(m.href)}">${esc(m.label)}</a>` : `<span>${esc(m.label)}</span>`'

DOORSTUREN = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>AISO26009 Lesdagen</title>
<link rel="icon" href="data:,">
<meta http-equiv="refresh" content="0; url=materiaal/">
</head>
<body style="font-family: system-ui, sans-serif; background: #faf7f0; color: #1a1a1a; margin: 2rem 1rem;">
<p><a href="materiaal/">Naar de startpagina van de lesdagen</a></p>
</body>
</html>
"""


def in_git(*paden: str) -> list[str]:
    uit = subprocess.run(["git", "ls-files", "--", *paden], cwd=REPO,
                         capture_output=True, text=True, check=True).stdout
    return sorted(regel for regel in uit.splitlines() if regel)


def te_publiceren() -> list[str]:
    """Repo-relatieve paden van alles wat op de site komt."""
    bo = [p for p in in_git("materiaal/bo-demo")
          if p.endswith((".html", ".png")) or p.endswith("/LICENSE")]
    paden = [LRD, *in_git("materiaal/*.html"), *bo]
    ontbreekt = [p for p in paden if not (REPO / p).is_file()]
    if ontbreekt:
        sys.exit(f"Niet gevonden of niet in git: {', '.join(ontbreekt)}")
    return paden


def staat_op_site(doel: str, op_site: set[str]) -> bool:
    """Waar of het doel van een link in de LRD (in de hoofdmap) op de site staat."""
    pad = unquote(re.split(r"[#?]", doel, maxsplit=1)[0])
    return pad == "" or pad in op_site or pad.rstrip("/") + "/index.html" in op_site


def lrd_voor_site(html: str, op_site: set[str]) -> str:
    html = html.replace(f'href="{CURSUSPAGINA}"', 'href="https://www.sn.nl/aiso"')

    def proza(m: re.Match) -> str:
        doel = m.group(1)
        if not RELATIEF.fullmatch(doel) or doel.startswith(("http", "#")) or staat_op_site(doel, op_site):
            return m.group(0)
        return f"<span>{m.group(2)}</span>"

    def data(m: re.Match) -> str:
        doel = m.group(1)
        if not RELATIEF.fullmatch(doel) or doel.startswith("http") or staat_op_site(doel, op_site):
            return m.group(0)
        return "href: ''"

    html = PROZALINK.sub(proza, html)
    html = DATALINK.sub(data, html)
    if OUD not in html:
        sys.exit("De weergave van het materiaal in de LRD is veranderd: pas OUD in bouw-pages.py aan.")
    return html.replace(OUD, NIEUW)


def bouw(uit: Path) -> None:
    paden = te_publiceren()
    if uit.exists():
        shutil.rmtree(uit)
    for pad in paden:
        doel = uit / pad
        doel.parent.mkdir(parents=True, exist_ok=True)
        if pad == LRD:
            doel.write_text(lrd_voor_site((REPO / pad).read_text(encoding="utf-8"), set(paden)),
                            encoding="utf-8")
        else:
            shutil.copyfile(REPO / pad, doel)
    (uit / "index.html").write_text(DOORSTUREN, encoding="utf-8")
    (uit / ".nojekyll").write_text("", encoding="utf-8")
    print(f"{uit}: {len(paden) + 1} bestanden")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Gebruik: python3 scripts/bouw-pages.py UITMAP")
    bouw(Path(sys.argv[1]))
