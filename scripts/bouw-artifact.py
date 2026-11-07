#!/usr/bin/env python3
"""Bouw de artifact-kopie van de LRD volgens CLAUDE.md ("Publishing as an artifact").

Gebruik:
    python3 scripts/bouw-artifact.py LRD-AISO26009-lesdagen.html /pad/naar/kopie.html

Staat er onaf werk in de werkmap, bouw dan uit de laatste commit:
    git show HEAD:LRD-AISO26009-lesdagen.html > /tmp/lrd.html
    python3 scripts/bouw-artifact.py /tmp/lrd.html /pad/naar/kopie.html

Draai daarna scripts/controleer-publicatie.py op de kopie (ADR-022).
"""
import re
import sys

LOKAAL = r"(?:background-docs/|temp/|onderzoek/|docs/|materiaal/|CHANGELOG\.md)"
CURSUSPAGINA = "background-docs/AI%20Strategie%20en%20Organisatietransformatie.pdf"


def bouw(src: str) -> str:
    head, rest = src.split("<body>", 1)
    body = rest.rsplit("</body>", 1)[0]
    title = re.search(r"<title>.*?</title>", head, re.S).group(0)
    early = re.search(r"<script>.*?</script>", head, re.S).group(0)
    style = re.search(r"<style>.*?</style>", head, re.S).group(0)

    # Sticky nav en voortgangsbalk onder de veilige zone, plus een band erboven.
    style = style.replace(".bds-nav { position: sticky; top: 0;",
                          ".bds-nav { position: sticky; top: env(safe-area-inset-top, 0px);")
    style = style.replace(".progress { position: fixed; top: 0;",
                          ".progress { position: fixed; top: env(safe-area-inset-top, 0px);")
    assert style.count("env(safe-area-inset-top, 0px)") == 2, "nav of progress niet gevonden"
    style = style.replace("</style>",
                          'body::before { content: ""; position: fixed; inset: 0 0 auto; '
                          "height: env(safe-area-inset-top, 0px); z-index: 150; "
                          "background: var(--bg-page); }\n</style>")

    # Cursuspagina naar de openbare pagina van S&N.
    body = body.replace(f'href="{CURSUSPAGINA}"', 'href="https://www.sn.nl/aiso"')

    # Links naar lokale mappen worden platte tekst.
    body = re.sub(r'<a href="' + LOKAAL + r'[^"]*"[^>]*>(.*?)</a>', r"<span>\1</span>", body, flags=re.S)

    # Materiaal per blok (DATA): lokale paden weg, en de weergave maakt er dan platte tekst van.
    body = re.sub(r"href: '" + LOKAAL + r"[^']*'", "href: ''", body)
    oud = ": `<a href=\"${esc(m.href)}\">${esc(m.label)}</a>`"
    if oud in body:
        body = body.replace(oud, ": `<span>${esc(m.label)}</span>`")

    return f"{title}\n{early}\n{style}\n{body.lstrip(chr(10))}"


if __name__ == "__main__":
    bron, uit = sys.argv[1], sys.argv[2]
    with open(bron, encoding="utf-8") as f:
        html = bouw(f.read())
    with open(uit, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{uit}: {len(html.encode())} bytes")
