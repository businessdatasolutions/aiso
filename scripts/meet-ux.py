#!/usr/bin/env python3
"""Meet de UX van de site met KPI's voor twee gebruikers: de trainer en de deelnemer.

De KPI's staan in onderzoek/2026-11-08-ux-startpagina.md: per gebruiker vier
fasen, per fase vier KPI's (aanwezig, vindbaar, begrijpelijk, betrouwbaar).
De deelnemer ziet de startpagina zonder parameter; de trainer opent haar met
?rol=trainer (ADR-047). Het script meet beide weergaven, en meet ook dat de
deelnemersweergave niets van de trainer bevat.

Na de KPI's volgen twee werkingscontroles, die ook meetellen bij --toets: elk
tabblad op een lespagina toont zijn paneel (W1), en beide boards downloaden als
zip met een geldige SKILL.md (W2). De KPI's meten waar iets staat; deze controles
meten of het werkt. Ze kwamen erbij na de proefrun van dag 1 op 8 november 2026,
waarin de advisory board niet te downloaden was terwijl alle KPI's groen waren.

Het script bouwt de site met bouw-pages.py in een tijdelijke map, serveert die lokaal
en meet met Playwright in de Chrome van deze computer. Het verandert niets in de repo.

Gebruik:
  python3 scripts/meet-ux.py                  # tabel met waarde, norm en oordeel
  python3 scripts/meet-ux.py --toets          # stopt met code 1 als een KPI de norm mist
  python3 scripts/meet-ux.py --json UIT.json  # de metingen ook als JSON
  python3 scripts/meet-ux.py --bron REF       # meet een eerdere versie, bijv. HEAD~1

Nodig: pip install playwright, en Google Chrome (channel 'chrome').
"""
import argparse
import functools
import http.server
import json
import re
import subprocess
import sys
import tempfile
import threading
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse

from playwright.sync_api import sync_playwright

REPO = Path(__file__).resolve().parent.parent
BEAMER = {'width': 1920, 'height': 1080}
LAPTOP = {'width': 1366, 'height': 768}
TELEFOON = {'width': 390, 'height': 844}
# Lespagina's waar een deelnemer heen gaat en weer terug moet. Het casusdeck is een
# bestand dat de deelnemer zelf invult; de simulator is een gerepareerde kopie (LEESMIJ).
GEEN_TERUG = {'index.html', 'casusdeck.html'}
INTERNE_CODE = re.compile(r'\b(?:FR|NFR|AC|ADR)-\d+|\bSN\d\b|\bLU\d\b')
# De werkkaart van de deelnemer: zeven vaste vragen per blok (ADR-047), met de koppen op de pagina.
WERK = [('nodig', 'Je hebt nodig'), ('aandacht', 'Let vooral op'), ('weten', 'Je moet weten'),
        ('doen', 'Wat je doet'), ('koers', 'Je zit goed als'), ('af', 'Je bent klaar als'),
        ('hulp', 'Vraag de trainer')]
# Woordnorm: een onderdeel leest op de beamer in twee of drie regels; een stap in één zin.
MAX_WOORDEN, MAX_STAPPEN, MAX_STAP = 30, 5, 20
TIJD = re.compile(r'^(\d{1,2}:\d{2})\b')

# Stukken die een blok kan noemen, met de plek waar ze te vinden zijn (ADR-046).
# Een blok dat het stuk noemt, heeft een tegel met een href die het derde deel bevat;
# bij de vragenkaart staat ook "vragenkaart" in het label.
STUKKEN = [
    ('vragenkaart', re.compile(r'vragenkaart|nulmeting|vier vragen|vier antwoorden', re.I), 'casusdeck', 'vragenkaart'),
    ('casusdeck', re.compile(r'casusdeck', re.I), 'casusdeck', None),
    ('boards', re.compile(r'\bboards?\b', re.I), 'boards', None),
    ('vraagtoets', re.compile(r'vraagtoets', re.I), 'vraagtoets', None),
    ('experimentpaper', re.compile(r'experimentpaper|experiment als paper', re.I), 'experimentpaper', None),
    ('businesscase', re.compile(r'businesscase|probleemstelling|probleemformulering', re.I), 'probleemformulering', None),
    ('kansenkaart', re.compile(r'kansenkaart', re.I), 'kansenkaart', None),
    ('volwassenheidsscan', re.compile(r'volwassenheidsscan', re.I), 'volwassenheidsscan', None),
]
# De vragenkaart en het casusdeck liggen drie dagen op tafel: elk blok dat ze noemt, wijst ze aan.
# De volwassenheidsscan staat in de browser van de deelnemer: wie hem later gebruikt, opent de pagina.
# Een ander stuk in "Je gebruikt" is eigen werk met een bron tussen haakjes; dat telt alleen
# in de titel of in "Je maakt", waar het blok over dat stuk gaat.
OVERAL = {'vragenkaart', 'casusdeck', 'volwassenheidsscan'}

JS_DATA = r"""async () => {
  const src = await (await fetch('../LRD-AISO26009-lesdagen.html')).text();
  const doc = new DOMParser().parseFromString(src, 'text/html');
  const s = doc.querySelector('script[type="module"]').textContent;
  const merk = 'const DATA = {', op = s.indexOf(merk), begin = op + merk.length - 1;
  let d = 0;
  for (let i = begin; i < s.length; i++) {
    const c = s[i], n = s[i + 1];
    if (c === "'" || c === '"' || c === '`') { for (i++; i < s.length && s[i] !== c; i++) if (s[i] === '\\') i++; }
    else if (c === '/' && n === '/') i = s.indexOf('\n', i);
    else if (c === '/' && n === '*') i = s.indexOf('*/', i + 2) + 1;
    else if (c === '{') d++;
    else if (c === '}' && --d === 0) {
      const D = new Function('return (' + s.slice(begin, i + 1) + ')')();
      return { days: D.days, vragen: D.vragen, rules: D.rules };
    }
  }
}"""

# Is het element echt te zien: weergegeven, niet leeg en binnen het venster zonder scrollen?
JS_IN_BEELD = r"""el => {
  if (!el) return false;
  const r = el.getBoundingClientRect(), st = getComputedStyle(el);
  return r.width > 0 && r.height > 0 && st.visibility !== 'hidden' && r.top >= 0 && r.bottom <= innerHeight + 1;
}"""

# Het diepste element waarvan de weergegeven tekst de zin bevat; in beeld zonder scrollen?
JS_TEKST_IN_BEELD = r"""zin => {
  const kandidaten = [...document.querySelectorAll('body *')].filter(el => (el.innerText || '').includes(zin));
  const diepst = kandidaten.filter(el => ![...el.children].some(k => (k.innerText || '').includes(zin)));
  return diepst.some(el => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && r.top >= 0 && r.bottom <= innerHeight + 1;
  });
}"""

JS_LINK_IN_BEELD = "h => [...document.querySelectorAll('a[href]')].filter(a => a.href === h).some(" + JS_IN_BEELD + ")"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for k in ('id', 'name'):
            if a.get(k):
                self.ids.add(a[k])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])


def ids_van(pad):
    p = Links()
    p.feed(pad.read_text(encoding='utf-8', errors='replace'))
    return p


def hm(s):
    u, m = s.split(':')
    return int(u) * 60 + int(m)


def tijd(minuten):
    return f'{minuten // 60}:{minuten % 60:02d}'


def bouw(bron, doel):
    if bron:
        # Bouw een eerdere versie: zet de bestanden van die commit in een werkboom.
        boom = Path(tempfile.mkdtemp(prefix='ux-bron-'))
        arch = subprocess.run(['git', '-C', str(REPO), 'archive', bron], check=True, capture_output=True).stdout
        subprocess.run(['tar', '-x', '-C', str(boom)], input=arch, check=True)
        # bouw-pages.py vraagt git om de lijst met bestanden
        subprocess.run(['git', 'init', '-q', str(boom)], check=True)
        subprocess.run(['git', '-C', str(boom), 'add', '-A'], check=True)
        wortel = boom
    else:
        wortel = REPO
    subprocess.run([sys.executable, str(wortel / 'scripts' / 'bouw-pages.py'), str(doel)],
                   check=True, capture_output=True, cwd=wortel)


def serveer(map_):
    class Stil(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass
    h = functools.partial(Stil, directory=str(map_))
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv, f'http://127.0.0.1:{srv.server_address[1]}/'


def pct(goed, totaal):
    return round(100 * goed / totaal) if totaal else 100


class Meting:
    def __init__(self):
        self.kpi, self.fouten = {}, []

    def zet(self, id_, waarde, eenheid, norm_ok, toelichting=''):
        self.kpi[id_] = {'waarde': waarde, 'eenheid': eenheid, 'ok': bool(norm_ok), 'toelichting': toelichting}


def meet(site, base):
    M = Meting()
    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome')
        ctx = browser.new_context(viewport=BEAMER)
        pg = ctx.new_page()
        console = []
        pg.on('console', lambda m: console.append(m.text) if m.type == 'error' else None)
        pg.on('pageerror', lambda e: console.append(str(e)))
        # Een 404 meldt de console zonder adres; dit noemt het adres erbij.
        pg.on('response', lambda r: console.append(f'{r.status} {r.url}') if r.status >= 400 else None)

        def start(dag, t=None, viewport=None, rol=None):
            if viewport:
                pg.set_viewport_size(viewport)
            q = f'?dag={dag}' + (f'&tijd={t}' if t else '') + (f'&rol={rol}' if rol else '')
            pg.goto(base + 'materiaal/' + q)
            pg.wait_for_selector('#lijst:not([hidden])')
            pg.wait_for_timeout(120)

        start(1)
        D = pg.evaluate(JS_DATA)
        vragen = {q['id']: q for q in D['vragen']}
        dagen = D['days']
        lrd = urljoin(base, 'LRD-AISO26009-lesdagen.html')

        def mat_url(m):
            return urljoin(lrd, m['href']) if m.get('href') else None

        def trainerdelen(b):
            t = b.get('trainer') or {}
            delen = [t.get('klaarzetten') or '', *(t.get('verloop') or []), t.get('letop') or '']
            return t, [x for x in delen if x]

        # ---------------- T1 Voorbereiden ----------------
        # Per blok (geen pauze) staat in de trainersweergave wat de trainer klaarzet, het verloop
        # met tijden en waar de trainer op let. Elk deel moet in de rij van dat blok staan.
        rijen = compleet = 0
        onvolledig = []
        for d in dagen:
            start(d['n'], rol='trainer')
            for b in d['blocks']:
                if b['t'] == 'pauze':
                    continue
                rijen += 1
                t, delen = trainerdelen(b)
                ok = bool(t.get('klaarzetten') and len(t.get('verloop') or []) >= 2 and t.get('letop'))
                if ok:
                    ok = pg.evaluate("""([s, delen]) => { const r = [...document.querySelectorAll('.rij')]
                        .find(x => x.querySelector('.rij-titel')?.textContent === s);
                        const tr = r?.querySelector('.trainer');
                        return !!tr && delen.every(f => tr.textContent.includes(f.slice(0, 40))); }""", [b['title'], delen])
                compleet += bool(ok)
                if not ok:
                    onvolledig.append(f"dag {d['n']} {b['s']}")
        M.zet('T1-A', pct(compleet, rijen), '%', compleet == rijen, f'{compleet} van {rijen} blokken'
              + (f"; zonder: {', '.join(onvolledig[:6])}{' …' if len(onvolledig) > 6 else ''}" if onvolledig else ''))

        start(1, rol='trainer')
        n_draai = pg.locator('a[href*="draaiboek"]').count()
        M.zet('T1-V', 1 if n_draai else None, 'klik', n_draai > 0,
              'link in de trainersweergave' if n_draai else 'niet bereikbaar vanuit de trainersweergave')

        refs = goed = 0
        mis = []
        for d in dagen:
            starts = {b['s']: b for b in d['blocks']}
            for b in d['blocks']:
                for haak in re.findall(r'\(([^()]*)\)', b.get('uses') or ''):
                    for t in re.findall(r'\b\d{1,2}:\d{2}\b', haak):
                        dagref = re.search(r'dag (\d)', haak)
                        doel = next((x for x in dagen if x['n'] == int(dagref.group(1))), d) if dagref else d
                        refs += 1
                        ok = t in {x['s'] for x in doel['blocks']}
                        if ok and 'AI-taak' in haak:
                            ok = bool(next((x for x in doel['blocks'] if x['s'] == t), {}).get('aiTask'))
                        goed += ok
                        if not ok:
                            mis.append(f"dag {d['n']} {b['s']}: ({haak})")
                    if 'AI-taak van de lunch' in haak:
                        refs += 1
                        ok = any(x['t'] == 'pauze' and x['title'] == 'Lunch' and x.get('aiTask') for x in d['blocks'])
                        goed += ok
                        if not ok:
                            mis.append(f"dag {d['n']} {b['s']}: ({haak})")
        # Het verloop van de trainer: de eerste stap begint met het blok, elke tijd ligt in het blok
        # en de tijden lopen op.
        for d in dagen:
            for b in d['blocks']:
                verloop = (b.get('trainer') or {}).get('verloop') or []
                if b['t'] == 'pauze':
                    continue
                tijden = [hm(m.group(1)) for x in verloop if (m := TIJD.match(x))]
                refs += 1
                ok = (bool(tijden) and TIJD.match(verloop[0]) is not None and tijden[0] == hm(b['s'])
                      and all(hm(b['s']) <= x < hm(b['e']) for x in tijden)
                      and tijden == sorted(tijden) and len(set(tijden)) == len(tijden))
                goed += ok
                if not ok:
                    mis.append(f"dag {d['n']} {b['s']}: verloop")
        M.zet('T1-B', pct(goed, refs), '%', goed == refs, f'{goed} van {refs}' + (f"; mis: {'; '.join(mis[:6])}" if mis else ''))

        dood = []
        paginas = sorted(site.rglob('*.html'))
        cache = {}
        for pad in paginas:
            for href in ids_van(pad).links:
                u = urlparse(href)
                if u.scheme or href.startswith(('#', 'mailto:', 'data:', 'javascript:')):
                    continue
                doel = (pad.parent / u.path).resolve() if u.path else pad
                if doel.is_dir():
                    doel = doel / 'index.html'
                if not doel.exists():
                    dood.append(f'{pad.relative_to(site)} → {href}')
                elif u.fragment and doel.suffix == '.html':
                    ids = cache.setdefault(doel, ids_van(doel).ids)
                    if u.fragment not in ids:
                        dood.append(f'{pad.relative_to(site)} → {href}')
        for d in dagen:
            for b in d['blocks']:
                for m in b.get('materials') or []:
                    u = urlparse(mat_url(m) or '')
                    if not u.path or u.netloc != urlparse(base).netloc:
                        continue
                    doel = site / u.path.lstrip('/')
                    if doel.is_dir():
                        doel = doel / 'index.html'
                    if not doel.exists():
                        dood.append(f"DATA dag {d['n']} {b['s']} → {m['href']}")
                    elif u.fragment and u.fragment not in cache.setdefault(doel, ids_van(doel).ids):
                        dood.append(f"DATA dag {d['n']} {b['s']} → {m['href']}")
        M.zet('T1-R', len(dood), 'links', not dood, '; '.join(dood[:6]) or 'geen')

        # ---------------- T2 Opstarten ----------------
        blokken_ok = blokken_tot = 0
        verkeerd = []
        for d in dagen:
            eerste = min(d['blocks'], key=lambda b: hm(b['s']))
            start(d['n'], tijd(hm(eerste['s']) - 10))
            blokken_tot += 1
            ok = pg.text_content('#nu-label').startswith('Straks') and pg.text_content('#nu-titel') == eerste['title']
            blokken_ok += ok
        # Per blok: één bezoek op de beamer, één op de laptop.
        per_blok = []
        for vp_naam, vp in (('beamer', BEAMER), ('laptop', LAPTOP)):
            for d in dagen:
                for i, b in enumerate(d['blocks']):
                    start(d['n'], tijd(hm(b['s']) + 1), vp)
                    r = {'dag': d['n'], 'b': b, 'vp': vp_naam, 'laatste': i == len(d['blocks']) - 1}
                    r['label'] = pg.text_content('#nu-label')
                    r['titel'] = pg.text_content('#nu-titel')
                    r['titel_in_beeld'] = pg.evaluate(JS_IN_BEELD, pg.query_selector('#nu-titel'))
                    r['daarna'] = pg.evaluate("() => { const e = document.getElementById('nu-daarna'); return e && !e.hidden ? e.innerText : ''; }")
                    r['maakt'] = pg.evaluate("() => { const e = document.getElementById('nu-maakt'); return e && !e.hidden ? e.innerText : ''; }")
                    r['vragen_vol'] = all(pg.evaluate(JS_TEKST_IN_BEELD, vragen[v]['vraag']) for v in b.get('v') or [])
                    hrefs = [mat_url(m) for m in (b.get('materials') or []) if mat_url(m)]
                    r['heeft_mat'] = bool(hrefs) and b['t'] != 'pauze'
                    r['mat_in_beeld'] = any(pg.evaluate(JS_LINK_IN_BEELD, h) for h in hrefs) if r['heeft_mat'] else True
                    w = b.get('deelnemer') or {}
                    r['werk'] = pg.evaluate("""() => { const e = document.getElementById('nu-werk');
                        if (!e || e.hidden) return null;
                        const r = e.getBoundingClientRect();
                        return { tekst: e.textContent, top: r.top, bottom: r.bottom, h: innerHeight }; }""")
                    r['werk_compleet'] = bool(r['werk']) and all(
                        kop in r['werk']['tekst'] and all(x[:40] in r['werk']['tekst'] for x in (w[k] if isinstance(w.get(k), list) else [w.get(k) or '\x00']))
                        for k, kop in WERK)
                    r['werk_in_beeld'] = bool(r['werk']) and r['werk']['top'] >= 0 and r['werk']['bottom'] <= r['werk']['h'] + 1
                    if vp_naam == 'beamer':
                        # De pagina zoals de browser haar opbouwde, zonder de broncode van scripts:
                        # een sjabloon in het script is geen inhoud die de deelnemer krijgt.
                        r['html'] = pg.evaluate("""() => { const c = document.documentElement.cloneNode(true);
                            c.querySelectorAll('script').forEach(s => s.remove()); return c.outerHTML; }""")
                    per_blok.append(r)
        bm = [r for r in per_blok if r['vp'] == 'beamer']
        for r in bm:
            blokken_tot += 1
            ok = r['label'].startswith('Nu') and r['titel'] == r['b']['title']
            blokken_ok += ok
            if not ok:
                verkeerd.append(f"dag {r['dag']} {r['b']['s']}")
        M.zet('T2-A', pct(blokken_ok, blokken_tot), '%', blokken_ok == blokken_tot,
              f'{blokken_ok} van {blokken_tot} momenten' + (f"; fout: {', '.join(verkeerd)}" if verkeerd else ''))

        start(1, None, BEAMER)
        pg.click('.pil[data-dag="2"]')
        ok2 = pg.inner_text('#dagtitel').startswith('Dag 2')
        pg.keyboard.press('3')
        ok3 = pg.inner_text('#dagtitel').startswith('Dag 3')
        M.zet('T2-V', 'ja' if ok2 and ok3 else 'nee', '', ok2 and ok3, 'pil en cijfertoets')

        start(1, '9:40', BEAMER)
        kern = ['#nu-titel', '#vragen', '#spoor']
        boven = all(pg.evaluate(JS_IN_BEELD, pg.query_selector(s)) for s in kern)
        M.zet('T2-B', 'ja' if boven else 'nee', '', boven, 'nu-titel, vraagchips en tijdlijn op 1920×1080 om 9:40')

        console.clear()
        for d in dagen:
            start(d['n'])
        for pad in paginas:
            pg.goto(base + str(pad.relative_to(site)))
            pg.wait_for_timeout(250)
        M.zet('T2-R', len(console), 'fouten', not console, '; '.join(console[:3]) or 'geen')

        # ---------------- T3 Blok geven ----------------
        # De trainer heeft de eigen laptop open met ?rol=trainer. De instructie van het blok van nu
        # staat in de kop, en de eerste stap van het verloop is te lezen zonder te scrollen.
        tr_tot = tr_ok = 0
        tr_mis = []
        for d in dagen:
            for b in d['blocks']:
                if b['t'] == 'pauze':
                    continue
                tr_tot += 1
                start(d['n'], tijd(hm(b['s']) + 1), LAPTOP, rol='trainer')
                t, _ = trainerdelen(b)
                eerste = (t.get('verloop') or [''])[0][:40]
                ok = bool(eerste) and pg.evaluate("""f => { const e = document.getElementById('nu-trainer');
                    if (!e || e.hidden || !e.textContent.includes(f)) return false;
                    const li = [...e.querySelectorAll('li')].find(x => x.textContent.includes(f));
                    const r = (li || e).getBoundingClientRect();
                    return r.top >= 0 && r.bottom <= innerHeight + 1; }""", eerste)
                tr_ok += bool(ok)
                if not ok:
                    tr_mis.append(f"dag {d['n']} {b['s']}")
        M.zet('T3-A', pct(tr_ok, tr_tot), '%', tr_ok == tr_tot, f'{tr_ok} van {tr_tot} blokken, 1366×768'
              + (f"; niet: {', '.join(tr_mis[:6])}{' …' if len(tr_mis) > 6 else ''}" if tr_mis else ''))
        met_mat = [r for r in bm if r['heeft_mat']]
        ok = sum(r['mat_in_beeld'] for r in met_mat)
        M.zet('T3-V', pct(ok, len(met_mat)), '%', ok == len(met_mat), f'{ok} van {len(met_mat)} blokken met materiaal, 1920×1080')
        met_v = [r for r in bm if r['b'].get('v')]
        ok = sum(r['vragen_vol'] for r in met_v)
        M.zet('T3-B', pct(ok, len(met_v)), '%', ok == len(met_v), f'{ok} van {len(met_v)} blokken met vragen, 1920×1080')
        ext = intern_ok = intern_tot = 0
        for d in dagen:
            for b in d['blocks']:
                for m in b.get('materials') or []:
                    u = mat_url(m)
                    if not u:
                        continue
                    if urlparse(u).netloc == urlparse(base).netloc:
                        intern_tot += 1
                        resp = pg.request.get(u.split('#')[0])
                        intern_ok += resp.ok
                    else:
                        ext += 1
                        intern_tot += 1
                        intern_ok += u.startswith('https://')
        M.zet('T3-R', pct(intern_ok, intern_tot), '%', intern_ok == intern_tot, f'{intern_ok} van {intern_tot} materiaallinks (intern HTTP 200, extern https)')

        # ---------------- T4 Overgang en afsluiten ----------------
        pz_tot = pz_ok = pzm_tot = pzm_ok = 0
        onder_vouw = []
        for d in dagen:
            for b in d['blocks']:
                if b['t'] != 'pauze':
                    continue
                pz_tot += 1
                ok = True
                for t in (tijd(hm(b['s']) - 4), tijd(hm(b['s']) + 1)):
                    start(d['n'], t, BEAMER)
                    tekst = pg.evaluate("() => { const e = document.getElementById('regel'); return e && !e.hidden ? e.innerText : ''; }")
                    ok &= 'Werkregel 1' in tekst and (not b.get('aiTask') or b['aiTask'][:40] in tekst)
                # Vier minuten vóór de pauze zegt de werkkaart "start de AI-taak": dan moet die
                # taak ook op een laptop zonder scrollen in beeld staan, in de kop of in de band.
                if b.get('aiTask'):
                    start(d['n'], tijd(hm(b['s']) - 4), LAPTOP)
                    zien = pg.evaluate("""(k) => [...document.querySelectorAll('#nu-daarna, #regel')].some(e => {
                        if (e.hidden || !e.innerText.includes(k)) return false;
                        const r = e.getBoundingClientRect(); return r.top >= 0 && r.top < innerHeight; })""", b['aiTask'][:40])
                    ok &= zien
                    if not zien:
                        onder_vouw.append(f"dag {d['n']} {b['s']}")
                pz_ok += ok
                mats = [mat_url(m) for m in b.get('materials') or [] if mat_url(m)]
                if mats:
                    pzm_tot += 1
                    pzm_ok += all(pg.locator(f'#regel a[href="{h}"]').count() > 0 for h in mats)
        M.zet('T4-A', pct(pz_ok, pz_tot), '%', pz_ok == pz_tot,
              f'{pz_ok} van {pz_tot} pauzes, 4 min vóór en tijdens; de AI-taak 4 min vóór ook in beeld op 1366×768'
              + (f"; onder de vouw: {', '.join(onder_vouw)}" if onder_vouw else ''))
        M.zet('T4-V', pct(pzm_ok, pzm_tot), '%', pzm_ok == pzm_tot, f'{pzm_ok} van {pzm_tot} pauzes met materiaal')
        niet_laatste = [r for r in bm if not r['laatste']]
        ok = sum(r['daarna'].startswith('Daarna') for r in niet_laatste)
        M.zet('T4-B', pct(ok, len(niet_laatste)), '%', ok == len(niet_laatste), f'{ok} van {len(niet_laatste)} blokken')
        na_ok = 0
        for d in dagen:
            start(d['n'], '16:45', BEAMER)
            lab = pg.text_content('#nu-label')
            na_ok += lab in ('Volgende lesdag', 'Afgelopen')
        M.zet('T4-R', pct(na_ok, len(dagen)), '%', na_ok == len(dagen), 'kop na 16:30')

        # ---------------- D1 Oriënteren ----------------
        met_out = [r for r in bm if r['b']['t'] != 'pauze' and (r['b'].get('output') or '').strip() not in ('', '—')]
        ok = sum(r['b']['output'][:30] in r['maakt'] for r in met_out)
        M.zet('D1-A', pct(ok, len(met_out)), '%', ok == len(met_out), f'"Je maakt" in de kop: {ok} van {len(met_out)}')
        lp = [r for r in per_blok if r['vp'] == 'laptop' and r['b']['t'] != 'pauze']
        ok = sum(r['titel_in_beeld'] and r['mat_in_beeld'] for r in lp)
        M.zet('D1-V', pct(ok, len(lp)), '%', ok == len(lp), f'nu-titel en materiaal zonder scrollen op 1366×768: {ok} van {len(lp)}')
        # Wat niet voor de deelnemer is, staat niet in de deelnemersweergave: niet in beeld en ook
        # niet verborgen in de pagina (ADR-047). Telt codes uit het ontwerp, vraagcodes zonder naam,
        # tekst van de trainer of uit het ontwerp (detail), en links naar draaiboek of LRD.
        ruis = []
        pg.set_viewport_size(LAPTOP)
        for d in dagen:
            start(d['n'])
            ruis += [f"startpagina dag {d['n']}: {c}" for c in INTERNE_CODE.findall(pg.evaluate('() => document.body.innerText'))]
        for pad in paginas:
            if pad.name == 'LRD-AISO26009-lesdagen.html' or pad.parent == site and pad.name == 'index.html':
                continue  # de LRD is het ontwerp: daar horen de codes
            pg.goto(base + str(pad.relative_to(site)))
            pg.wait_for_timeout(150)
            ruis += [f'{pad.relative_to(site)}: {c}' for c in INTERNE_CODE.findall(pg.evaluate('() => document.body.innerText'))]
        for d in dagen:
            start(d['n'], tijd(hm(d['blocks'][0]['s']) + 1), BEAMER)
            tekst = pg.evaluate('() => document.body.innerText')
            for m in re.finditer(r'\bV([1-4])(?!\d)', tekst):
                rest = tekst[m.end():m.end() + 30].lstrip(' ·:–-\n\t')
                if not rest.startswith(vragen[f'V{m.group(1)}']['kort']):
                    ruis.append(f"dag {d['n']}: vraagcode zonder naam: {tekst[max(0, m.start() - 10):m.end() + 25]!r}")
        trainerstekst = set()
        for d in dagen:
            for b in d['blocks']:
                _, delen = trainerdelen(b)
                trainerstekst.update(x[:40] for x in delen)
                if b.get('detail'):
                    trainerstekst.add(b['detail'][:40])
        # Een zin die ook op de werkkaart of in een ander veld voor de deelnemer staat, is geen lek.
        voor_deelnemer = json.dumps([[b.get('deelnemer'), b.get('title'), b.get('output'), b.get('uses'), b.get('aiTask'),
                                      [m.get('label') for m in b.get('materials') or []]] for d in dagen for b in d['blocks']],
                                    ensure_ascii=False)
        trainerstekst = {f for f in trainerstekst if json.dumps(f, ensure_ascii=False)[1:-1] not in voor_deelnemer}
        for r in bm:
            html = r['html']
            for f in trainerstekst:
                if f in html:
                    ruis.append(f"dag {r['dag']} {r['b']['s']}: tekst voor de trainer of uit het ontwerp: {f[:24]!r}")
            for doel in ('draaiboek', 'LRD-AISO26009'):
                if re.search(r'href="[^"]*' + doel, html):
                    ruis.append(f"dag {r['dag']} {r['b']['s']}: link naar {doel}")
        ruis = list(dict.fromkeys(ruis))
        M.zet('D1-B', len(ruis), 'stuks', not ruis, '; '.join(ruis[:6]) + (' …' if len(ruis) > 6 else '') or 'geen')
        breed = []
        pg.set_viewport_size(TELEFOON)
        for d in dagen:
            start(d['n'], '9:40')
            if pg.evaluate('() => document.documentElement.scrollWidth > innerWidth + 1'):
                breed.append(f"startpagina dag {d['n']}")
        for pad in paginas:
            if pad.name == 'LRD-AISO26009-lesdagen.html':
                continue
            pg.goto(base + str(pad.relative_to(site)))
            pg.wait_for_timeout(200)
            if pg.evaluate('() => document.documentElement.scrollWidth > innerWidth + 1'):
                breed.append(str(pad.relative_to(site)))
        M.zet('D1-R', len(breed), 'pagina\'s', not breed, ', '.join(breed) or 'geen')

        # ---------------- D2 Opdracht snappen ----------------
        # De werkkaart: zeven vaste vragen bij elk blok, in de kop als het blok loopt (ADR-047).
        werkblokken = [r for r in bm if r['b']['t'] != 'pauze']
        ok = sum(r['werk_compleet'] for r in werkblokken)
        mis = [f"dag {r['dag']} {r['b']['s']}" for r in werkblokken if not r['werk_compleet']]
        M.zet('D2-A', pct(ok, len(werkblokken)), '%', ok == len(werkblokken), f'werkkaart met alle zeven onderdelen in de kop: {ok} van {len(werkblokken)}'
              + (f"; niet: {', '.join(mis[:6])}{' …' if len(mis) > 6 else ''}" if mis else ''))
        ok = sum(r['werk_in_beeld'] for r in werkblokken)
        mis = [f"dag {r['dag']} {r['b']['s']}" for r in werkblokken if not r['werk_in_beeld']]
        M.zet('D2-V', pct(ok, len(werkblokken)), '%', ok == len(werkblokken), f'hele werkkaart zonder scrollen, 1920×1080: {ok} van {len(werkblokken)}'
              + (f"; niet: {', '.join(mis[:6])}{' …' if len(mis) > 6 else ''}" if mis else ''))
        delen = binnen = 0
        lang = []
        for d in dagen:
            for b in d['blocks']:
                if b['t'] == 'pauze':
                    continue
                w = b.get('deelnemer') or {}
                for k, kop in WERK:
                    delen += 1
                    v = w.get(k)
                    if k == 'doen':
                        stappen = v if isinstance(v, list) else []
                        ok = 0 < len(stappen) <= MAX_STAPPEN and all(len(x.split()) <= MAX_STAP for x in stappen)
                    else:
                        ok = isinstance(v, str) and 0 < len(v.split()) <= MAX_WOORDEN
                    ok = ok and not INTERNE_CODE.search(json.dumps(v, ensure_ascii=False))
                    binnen += ok
                    if not ok:
                        lang.append(f"dag {d['n']} {b['s']} {k}")
        M.zet('D2-B', pct(binnen, delen), '%', binnen == delen,
              f'onderdelen binnen de norm ({MAX_WOORDEN} woorden, hooguit {MAX_STAPPEN} stappen van {MAX_STAP} woorden, geen codes): {binnen} van {delen}'
              + (f"; niet: {', '.join(lang[:6])}{' …' if len(lang) > 6 else ''}" if lang else ''))
        extern = []
        pg.on('request', lambda r: extern.append(r.url) if urlparse(r.url).netloc not in (urlparse(base).netloc, '') and not r.url.startswith('data:') else None)
        for d in dagen:
            start(d['n'], '9:40')
        M.zet('D2-R', len(set(extern)), 'bronnen', not extern, ', '.join(sorted(set(extern))[:3]) or 'geen: werkt op het netwerk van de zaal zonder CDN')

        # ---------------- D3 Materiaal vinden ----------------
        stukken_tot = stukken_ok = 0
        missen = []
        for d in dagen:
            for b in d['blocks']:
                if b['t'] == 'pauze':
                    continue
                alles = ' '.join([b['title'], b.get('uses') or '', b.get('output') or ''])
                kern = ' '.join([b['title'], b.get('output') or ''])
                mats = b.get('materials') or []
                for naam, rx, hrefdeel, labeldeel in STUKKEN:
                    if not rx.search(alles if naam in OVERAL else kern):
                        continue
                    stukken_tot += 1
                    ok = any(hrefdeel in (m.get('href') or '') and (not labeldeel or labeldeel in m['label'].lower()) for m in mats)
                    stukken_ok += ok
                    if not ok:
                        missen.append(f"dag {d['n']} {b['s']} {naam}")
        M.zet('D3-A', pct(stukken_ok, stukken_tot), '%', stukken_ok == stukken_tot,
              f'{stukken_ok} van {stukken_tot} genoemde stukken' + (f"; zonder vindplaats: {', '.join(missen)}" if missen else ''))
        items = bron = 0
        for d in dagen:
            for b in d['blocks']:
                u = b.get('uses') or ''
                delen, diepte, cur = [], 0, ''
                for c in u:
                    diepte += (c == '(') - (c == ')')
                    if c == ',' and diepte == 0:
                        delen.append(cur); cur = ''
                    else:
                        cur += c
                if cur.strip():
                    delen.append(cur)
                for x in delen:
                    items += 1
                    bron += '(' in x and ')' in x
        M.zet('D3-V', pct(bron, items), '%', bron == items, f'"Je gebruikt"-stukken met bron: {bron} van {items}')
        lab_tot = lab_ok = 0
        kaal = []
        for d in dagen:
            for b in d['blocks']:
                for m in b.get('materials') or []:
                    lab_tot += 1
                    ok = len((m.get('label') or '').split()) >= 2 and '.html' not in (m.get('label') or '')
                    lab_ok += ok
                    if not ok:
                        kaal.append(m.get('label') or m.get('href'))
        M.zet('D3-B', pct(lab_ok, lab_tot), '%', lab_ok == lab_tot, f'tegellabels die zeggen wat het is: {lab_ok} van {lab_tot}' + (f"; kaal: {', '.join(kaal)}" if kaal else ''))
        start(1, None, BEAMER)
        nieuw_tab_tot = nieuw_tab_ok = 0
        for d in dagen:
            start(d['n'])
            for a in pg.query_selector_all('a.tegel.is-extern, a.pauze-link'):
                href = a.get_attribute('href')
                if urlparse(href).netloc == urlparse(base).netloc:
                    continue
                nieuw_tab_tot += 1
                nieuw_tab_ok += a.get_attribute('target') == '_blank'
        M.zet('D3-R', pct(nieuw_tab_ok, nieuw_tab_tot), '%', nieuw_tab_ok == nieuw_tab_tot, 'externe links openen in een nieuw tabblad, de startpagina blijft staan')

        # ---------------- D4 Terugkeren ----------------
        les = [p_ for p_ in paginas if p_.parent.name == 'materiaal' and p_.name not in GEEN_TERUG]
        gebruikt_op = {}
        for d in dagen:
            for b in d['blocks']:
                for m in b.get('materials') or []:
                    if m.get('href', '').startswith('materiaal/'):
                        gebruikt_op.setdefault(m['href'].split('/')[1].split('#')[0], set()).add(d['n'])
        heeft = in_beeld = zegt = juiste_dag = 0
        zonder, laag = [], []
        pg.set_viewport_size(LAPTOP)
        for pad in les:
            pg.goto(base + str(pad.relative_to(site)))
            pg.wait_for_timeout(150)
            terug = [a for a in pg.query_selector_all('a[href]')
                     if urlparse(a.get_attribute('href')).path.rstrip('/') in ('./index.html', 'index.html', '.', './', '')
                     and not a.get_attribute('href').startswith('#')]
            if not terug:
                zonder.append(pad.name)
                continue
            heeft += 1
            zichtbaar = any(pg.evaluate(JS_IN_BEELD, a) for a in terug)
            in_beeld += zichtbaar
            if not zichtbaar:
                laag.append(pad.name)
            zegt += any(re.search(r'start|lesdag|programma|terug', a.inner_text(), re.I) for a in terug)
            dag_q = re.search(r'dag=(\d)', terug[0].get_attribute('href'))
            juiste_dag += (not dag_q) or int(dag_q.group(1)) in gebruikt_op.get(pad.name, {int(dag_q.group(1))})
        n = len(les)
        M.zet('D4-A', pct(heeft, n), '%', heeft == n, f'{heeft} van {n} lespagina\'s' + (f"; zonder: {', '.join(zonder)}" if zonder else ''))
        M.zet('D4-V', pct(in_beeld, n), '%', in_beeld == n, f'terug-link zonder scrollen in beeld (1366×768): {in_beeld} van {n}' + (f"; niet: {', '.join(laag)}" if laag else ''))
        M.zet('D4-B', pct(zegt, n), '%', zegt == n, f'link zegt waarheen: {zegt} van {n}')
        M.zet('D4-R', pct(juiste_dag, n), '%', juiste_dag == n, f'landt op een dag waarop de pagina gebruikt wordt: {juiste_dag} van {n}')

        # ---------------- Werking van de lespagina's ----------------
        # Geen UX-maat, maar: doet de pagina wat de deelnemer nodig heeft? Een paneel binnen een
        # verborgen paneel geeft geen consolefout en geen dode link; je ziet het pas als je klikt.
        tabs_tot = tabs_ok = 0
        leeg = []
        for pad in sorted(p_ for p_ in paginas if p_.parent.name == 'materiaal'):
            pg.goto(base + str(pad.relative_to(site)))
            pg.wait_for_timeout(150)
            for tab in pg.query_selector_all('[role=tab][aria-controls]'):
                if not tab.is_visible():
                    continue
                tabs_tot += 1
                tab.click()
                pg.wait_for_timeout(80)
                paneel = pg.query_selector('#' + tab.get_attribute('aria-controls'))
                if paneel and paneel.is_visible():
                    tabs_ok += 1
                else:
                    leeg.append(f'{pad.name} › {tab.inner_text().strip()}')
        M.zet('W1', pct(tabs_ok, tabs_tot), '%', tabs_ok == tabs_tot,
              f'tabbladen die hun paneel tonen: {tabs_ok} van {tabs_tot}' + (f"; leeg: {', '.join(leeg)}" if leeg else ''))

        zips_ok, zip_fout = 0, []
        pg.goto(base + 'materiaal/boards.html#downloaden')
        pg.wait_for_timeout(200)
        for wat, naam in (('sup', 'supervisory-board'), ('adv', 'advisory-board')):
            try:
                pg.click(f'#tab-{wat}')
                with pg.expect_download(timeout=4000) as dl:
                    pg.click(f'[data-zip="{wat}"]', timeout=2000)
                with zipfile.ZipFile(dl.value.path()) as z:
                    skill = z.read(f'{naam}/SKILL.md').decode('utf-8')
                if not re.match(rf'^---\nname: {naam}\n', skill):
                    raise ValueError('naam in SKILL.md klopt niet')
                zips_ok += 1
            except Exception as e:  # noqa: BLE001 — elke fout is hier een gemiste download
                zip_fout.append(f'{naam}: {type(e).__name__}')
        M.zet('W2', f'{zips_ok} van 2', '', zips_ok == 2,
              'beide boards downloaden als zip met een geldige SKILL.md' + (f"; mislukt: {', '.join(zip_fout)}" if zip_fout else ''))

        browser.close()
    return M


NAMEN = {
    'T1-A': 'Trainersinstructie per blok (?rol=trainer)', 'T1-V': 'Klikken naar het draaiboek (?rol=trainer)',
    'T1-B': 'Tijden in "Je gebruikt" en in het verloop kloppen', 'T1-R': 'Dode interne links en ankers',
    'T2-A': 'Kop toont het juiste blok', 'T2-V': 'Dag wisselen in één handeling',
    'T2-B': 'Kop, vragen en tijdlijn boven de vouw (beamer)', 'T2-R': 'Consolefouten',
    'T3-A': 'Instructie van het nu-blok in de kop (?rol=trainer, laptop)', 'T3-V': 'Materiaal van het nu-blok zonder scrollen (beamer)',
    'T3-B': 'Vragen van het blok voluit, zonder hover', 'T3-R': 'Materiaallinks openen',
    'T4-A': 'Werkregel 1 en AI-taak vóór en tijdens de pauze, ook in beeld op een laptop','T4-V': 'Materiaal van de AI-taak in de band',
    'T4-B': 'Kop noemt het volgende blok', 'T4-R': 'Kop na de lesdag',
    'D1-A': '"Je maakt" in de kop', 'D1-V': 'Nu-titel en materiaal zonder scrollen (laptop)',
    'D1-B': 'Ontwerp- en trainersinhoud in de deelnemersweergave', 'D1-R': 'Horizontaal scrollen op een telefoon',
    'D2-A': 'Werkkaart met zeven onderdelen in de kop', 'D2-V': 'Hele werkkaart zonder scrollen (beamer)',
    'D2-B': 'Werkkaart kort en zonder codes', 'D2-R': 'Externe bronnen op de startpagina',
    'D3-A': 'Vindplaats voor elk genoemd stuk', 'D3-V': '"Je gebruikt" met bron',
    'D3-B': 'Tegellabels zeggen wat het is', 'D3-R': 'Externe links in nieuw tabblad',
    'D4-A': 'Lespagina met link terug', 'D4-V': 'Terug-link zonder scrollen',
    'D4-B': 'Terug-link zegt waarheen', 'D4-R': 'Terug-link landt op de goede dag',
}
WERKING = {
    'W1': 'Elk tabblad op een lespagina toont zijn paneel',
    'W2': 'Downloads van de boards (supervisory en advisory)',
}
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--toets', action='store_true', help='stop met code 1 als een KPI de norm mist')
    ap.add_argument('--json', help='schrijf de metingen als JSON naar dit bestand')
    ap.add_argument('--bron', help='meet de site van deze git-versie (bijv. HEAD~1) in plaats van de werkmap')
    a = ap.parse_args()
    with tempfile.TemporaryDirectory(prefix='ux-site-') as tmp:
        site = Path(tmp) / 'site'
        bouw(a.bron, site)
        srv, base = serveer(site)
        try:
            M = meet(site, base)
        finally:
            srv.shutdown()
    print(f"| KPI | Naam | Waarde | Oordeel | Toelichting |\n|---|---|---|---|---|")
    for k in NAMEN:
        r = M.kpi[k]
        w = '–' if r['waarde'] is None else f"{r['waarde']} {r['eenheid']}".strip()
        print(f"| {k} | {NAMEN[k]} | {w} | {'excellent' if r['ok'] else 'onder de norm'} | {r['toelichting']} |")
    mis = [k for k in NAMEN if not M.kpi[k]['ok']]
    print(f"\n{len(NAMEN) - len(mis)} van {len(NAMEN)} KPI's halen de norm." + (f" Onder de norm: {', '.join(mis)}." if mis else ''))
    print(f"\n| Controle | Naam | Waarde | Oordeel | Toelichting |\n|---|---|---|---|---|")
    for k in WERKING:
        r = M.kpi[k]
        w = f"{r['waarde']} {r['eenheid']}".strip()
        print(f"| {k} | {WERKING[k]} | {w} | {'werkt' if r['ok'] else 'WERKT NIET'} | {r['toelichting']} |")
    stuk = [k for k in WERKING if not M.kpi[k]['ok']]
    print(f"\nWerking: {len(WERKING) - len(stuk)} van {len(WERKING)} controles in orde." + (f" Stuk: {', '.join(stuk)}." if stuk else ''))
    mis += stuk
    if a.json:
        Path(a.json).write_text(json.dumps(M.kpi, ensure_ascii=False, indent=2), encoding='utf-8')
    if a.toets and mis:
        sys.exit(1)


if __name__ == '__main__':
    main()
