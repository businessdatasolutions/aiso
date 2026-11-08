# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

The design workspace for the three classroom days of **AISO26009 "AI Strategie en Organisatietransformatie"**, a training by Schouten & Nelissen (S&N) that Witek ten Hove delivers on 12 Nov, 26 Nov and 10 Dec 2026 in Zwolle. S&N owns the online learning environment; this repo only designs the classroom days (ADR-001). Everything is in Dutch. It is a git repository with the private remote `businessdatasolutions/aiso` (branch `main`). `.gitignore` keeps `temp/` (participant data) and the contract in `background-docs/` (rates) out of git: never stage or commit them, and never quote them into tracked files.

The central deliverable is a **Learner Requirement Document (LRD)**: [LRD-AISO26009-lesdagen.html](LRD-AISO26009-lesdagen.html). Around it:

- `docs/adr/`: one ADR per design decision, with an index in `README.md`. `CHANGELOG.md`: one entry per LRD version.
- `background-docs/`: source material. These are the S&N course page (saved as PDF), the contract (it includes rates) and an overview of the online environment.
- `temp/`: participants' submissions, which contain personal data.
- `onderzoek/`: reviews of the LRD, such as the test against the AI wiki.
- `materiaal/`: classroom material (ADR-021). `voorbeeldcasus.md` (the fictitious Voorbeeld BV) is the content source for the lesson pages `groeimodel.html`, `kennisvormen.html` and `kansenkaart.html`: change a text there, then copy it into the page by hand. `index.html` is the start page per lesdag (`?dag=1|2|3`); it reads the programme from `DATA` in the LRD (fetch + parse), so it only works via a local server. For rehearsal, `?tijd=HH:MM` sets the clock to that time of day. `draaiboek-bouwstenen.md` and `rolkaarten-kritiekpunten.md` are trainer material.
- `scripts/`: `controleer-publicatie.py` (the leak check before publishing, ADR-022) and `excalidraw-huisstijl.py` (redraws an `.excalidraw` file as a house-style SVG).
- `.claude/skills/aiso-*`: project copies of the user's education skills, made generic (no HAN references). The `aiso-` prefix stops them clashing with the personal skills of the same name in `~/.claude/skills`.

## Privacy of participants (ADR-016, ADR-017)

No document we build may name a participant's employer, own company or a work domain that points to it. That covers the LRD, ADRs, the changelog, reports, artifacts and logs in other repos such as the ai-wiki. A rare first name plus a function plus an organisation identifies a person. Participants appear only as pseudonyms (Deelnemer A–F) with a general role. The key is in `temp/pseudoniemen.md` and nowhere else. Don't link to individual submissions either, because their filenames contain names. The raw submissions in `temp/` are input only: never quote their organisation details and never publish them.

## How the LRD works

The LRD is one self-contained HTML page. The skill `aiso-building-lrds` defines its shape and process; follow it for every change.

- **One data source.** All numbered items live in the `const DATA = {...}` object inside the `<script type="module">`. That covers the S&N results `sn` (the only goals: there are no separate learning outcomes and no Bloom tags, ADR-024), requirements `fr` and `nfr`, acceptance criteria `ac`, the programme `days`, KISS choices `kiss`, the build pipeline `pipeline`, experiment types `experimentTypes`, board moments `boardMoments`, risks `risks`, phases `phases` and more. Tables, diagrams, chips and counts are all rendered from it.
- **Prose is static HTML.** This covers Parts 1–13, the didactic frameworks and the explanations.
- **To add or change an item, edit `DATA`.** Do not hand-edit rendered tables. Cross-references are ID arrays: `sn` on FR/NFR, workshops and participant cards, `measuredBy` on AC, `refs` on risks, `fr` and `sn` on programme blocks. At load time, any ID that doesn't resolve is logged as `LRD: verwijzingen zonder doel`.
- **Counts are computed.** The `<b data-count="…">` stat numbers are rewritten by JS. Their static values are only a no-JS fallback, but keep them in sync.
- **ID scheme.** `SN1–7` are the contractual S&N results and the only goals. `LU1–9` existed up to version 0.12; don't reintroduce them, even though the skill `aiso-building-lrds` describes learning outcomes. Then `FR-NN`, `NFR-NN` and `AC-NN`. Never renumber: add new IDs at the end. Anchors are the lowercase IDs (`#fr-15`).
- **Deliverables per participant** (Part 10) render from the `deliverable` field on AC items, so each product sits next to the criterion that measures it. The trainer list stays in `DATA.deliverables.trainer`.
- **Materials per block.** A programme block may have `materials: [{ label, href }]`. `href` is relative to the repo root or an absolute https URL. The detail panel in Part 8 and the start page `materiaal/index.html` both render it.
- **Input per block (ADR-032).** `input` names only the online assignments a block builds on (the column "Invoer uit de online omgeving" in Part 8). Work the participant made during or between the lesdagen goes in `uses`, with its source in brackets, such as "Top 3 stakeholders (dag 1)" or "(AI-taak van de lunch)". The start page shows `uses` as "Je gebruikt:".
- **Visuals.** D3, Three.js and Motion load as ES modules from pinned jsDelivr versions (`d3@7.9.0`, `three@0.160.0`, `motion@11.11.13`). Each loads via its own dynamic `import()`, so one failing CDN doesn't break the rest. Tables render without any library.
- **Brand.** The tokens and components are copied verbatim from `~/Projects/brand-project/stylebook/shared.css` (Business Data Solutions). The palette is chartreuse `#d4db3e` as the single signal accent, warm black, cream, and tier/edge cards. The page is deliberately light-only.

## Every change to the LRD

1. Edit `DATA` or the prose.
2. If the change is a design decision, add a new ADR in `docs/adr/` and add it to the index. A reversed decision gets a new ADR, and the old one is set to "Vervangen door ADR-NNN". Never rewrite an old decision.
3. Add a `CHANGELOG.md` entry and bump the version in three places: the eyebrow (`versie 0.8 (concept)`), the `<dt>Datum</dt>` row and the footer.
4. Verify (commands below).
5. If the published artifact should follow, republish it (see below).

Architecture-level changes ripple through many Parts. Before editing, list the affected Parts and IDs, and ask the user when the ripple is ambiguous.

## Commands

```bash
# Preview: VS Code Live Server is set to port 5501 (.vscode/settings.json), or:
python3 -m http.server 8765        # then open http://127.0.0.1:8765/LRD-AISO26009-lesdagen.html
                                   # (Playwright blocks file:// URLs)

# JS syntax check of the LRD module script
python3 -c "t=open('LRD-AISO26009-lesdagen.html').read(); open('/tmp/lrd.mjs','w').write(t.split('<script type=\"module\">')[1].split('</script>')[0])" && node --check /tmp/lrd.mjs

# Dutch text checks (run on the LRD, ADRs and any Dutch document before it goes out)
python3 .claude/skills/aiso-schrap-ai-taal/scripts/aitaal.py LRD-AISO26009-lesdagen.html --codes A1,A2,A3,A5,A7,A8
python3 .claude/skills/aiso-redigeer-nederlandse-tekst/scripts/tekstcheck.py CHANGELOG.md docs/adr --recursief

# Leak check: on the artifact copy before every publish (must report nothing),
# or with --alleen-privacy on files that stay in the repo. Never prints a found value.
python3 scripts/controleer-publicatie.py /path/to/artifact-copy.html
python3 scripts/controleer-publicatie.py --alleen-privacy LRD-AISO26009-lesdagen.html CHANGELOG.md docs/adr/*.md materiaal/*.md

# Diagram in the house style from an .excalidraw source
python3 scripts/excalidraw-huisstijl.py IN.excalidraw UIT.svg

# Tests for the AI-language checker (45 parametrised cases); a single test via -k
cd .claude/skills/aiso-schrap-ai-taal/scripts && PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q -p no:cacheprovider -k test_schone_tekst_blijft_stil
```

`tekstcheck.py` flags F4 ("kondigt 3 aan, maar er volgen N") as a false positive when a table follows a numbered list. Judge each hit; don't apply them blindly. In a browser check, confirm there are no console errors and that the coverage line under "Van resultaat van S&N naar eis en bewijs" reports full coverage.

## Publishing as an artifact

The LRD is published privately at https://claude.ai/artifact/P9qt4SHNze6mtWmEfnywP7 (ADR-013). The repo file stays the source. The artifact is a derived copy, built like this:

- Keep only the `<title>`, the early inline `<script>`, the `<style>` and the body content. The Artifact tool adds its own html/head/body skeleton.
- Make the sticky nav and the progress bar use `top: env(safe-area-inset-top, 0px)`, and add a `body::before` band.
- Point the course-page link to `https://www.sn.nl/aiso`.
- Turn every link into `background-docs/`, `temp/`, `onderzoek/`, `docs/`, `materiaal/` and `CHANGELOG.md` into plain text. The contract (rates) and participant data must never be published.
- `scripts/bouw-artifact.py SOURCE OUT` does the steps above, and also blanks the local `materials` hrefs in `DATA` so the detail panel shows plain text. If the working tree holds unfinished LRD work, build from `git show HEAD:LRD-AISO26009-lesdagen.html`.
- Run `scripts/controleer-publicatie.py` on the copy; publish only when it reports nothing. It finds real first names from the file names in `temp/`; organisations and surnames only if `temp/verboden-woorden.txt` is filled (one entry per line, never committed).

From a new session, publish to the existing URL with the `url` parameter after reading it first. Every publish gets a changelog line.

## Related outside this repo

- `~/Projects/brand-project/stylebook/` holds the brand source: tokens, logo and voice. Voice is plain Dutch with no anglicisms where a Dutch word exists.
- `~/Projects/ai-wiki/` is the user's LLM wiki. Research questions about the LRD go through its `iterative-wiki-query` skill, and its research logs are written in that repo's `inspiration/` folder.
