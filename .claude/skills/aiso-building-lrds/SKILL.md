---
name: aiso-building-lrds
description: Use when creating or updating a Learner Requirement Document (LRD) — a formal pedagogical design document for a course, module, or workshop specifying learning outcomes, target audience, design criteria, functional requirements, weekly programme, assessment, deliverables, acceptance criteria, and risks. The LRD is always delivered as one interactive, animated HTML page (D3, Three.js, Motion) in the project's brand style, never as Markdown.
---

# Building LRDs

## Overview

An LRD (Learner Requirement Document) is a format for specifying a course, module, or workshop as a formal design document rather than a syllabus: learning outcomes tagged to a cognitive taxonomy, an explicit design-criteria/KISS section, functional and non-functional requirements for any mechanism the course runs (gates, tutoring systems, platforms), a weekly programme, assessment alignment, deliverables, numbered acceptance criteria, and a risks/mitigations table. If the project has prior LRDs (workshop-level or module-level), read them first — they define the house template; don't invent structure from memory.

## When to Use

- Asked to write, redesign, or extend a module/workshop/course spec for any programme, training or organisation that uses this LRD format
- Asked to formalize an existing syllabus/programme doc into learning outcomes + requirements + acceptance criteria
- Mid-document: a request changes the underlying mechanism's *architecture*, not just its wording — treat as a new design decision (see Process, step 6), not a direct edit

## Template Shape

| Part | Content |
|---|---|
| Header | Doc/Version/Date/Programme/Scope/Author/Related-docs table + one-line lead quote |
| 1 — Context & positioning | What this LRD is/isn't; links to source docs it builds on rather than repeats |
| 2 — Pedagogical quality system | 3–5 grounded frameworks (e.g. Bloom's taxonomy, motivation/flow theory, a durable-skills framework), each written as **Point** (1–2 sentences: what the source actually claims) → **Design axiom** (1–2 sentences: what that forces this LRD to do) — never a literature summary |
| 3 — Learning outcomes | Open with a short paragraph naming and defining the future role each outcome serves (not in Part 1 or 4 — here, right before the table it grounds). One table per role/module, 5–8 outcomes each — don't force a 1:1 mapping to weeks. Every outcome: *"A learner can \<Bloom verb(s)\>, so that \<value tied to their future role\>"* — tag with the Bloom cell, e.g. `[Apply / Procedural]` (process ∈ Remember/Understand/Apply/Analyze/Evaluate/Create; knowledge ∈ Factual/Conceptual/Procedural/Metacognitive), plus any secondary framework tag (e.g. durable skill) |
| 4 — Target audience & prior knowledge | Who enrols, what's assumed/not assumed, team structure |
| 5 — Design criteria | KISS stated as **constraints, not aspirations** — "X was considered and rejected because Y" |
| 6 — Core mechanism | Whatever's genuinely new about this LRD (a gate, a tutoring system, a pipeline) — specified in enough detail that Part 7 can turn it into requirements |
| 7 — Functional / non-functional requirements | `FR-01`, `FR-02`… / `NFR-01`… numbered, one behaviour per row |
| 8 — Weekly/session programme | Table, one row per week/block |
| 9 — Assessment alignment | How the Part 6 mechanism does/doesn't affect grades |
| 10 — Deliverables | Numbered list of what learners/teams produce |
| 11 — Acceptance criteria | `AC-01`… numbered, each with a "Measured by" column citing the FR that produces the evidence |
| 12 — Risks & mitigations | Table; each mitigation cites the FR/section that actually prevents the risk, not just asserts it away |
| 13 — Roadmap | Pilot-first sequencing, not a big-bang rollout |
| Appendix — Sources | Every framework/paper cited in Part 2, plus links to related docs |

Not every LRD needs all 13 — a single-session workshop LRD compresses to ~9 sections (context, learning outcomes, audience, design criteria, session flow as functional requirements, deliverables, acceptance criteria, sources). Scale the shape to what's being specified.

## Output Format — One Interactive HTML Page

An LRD is always delivered as **one self-contained `.html` file**: a delightful, dynamic page a designer, client or colleague trainer wants to explore. Never deliver a Markdown version next to it — two formats drift apart. If a Markdown LRD exists, the HTML replaces it.

### Single source of truth

Put every numbered item in **one JavaScript data object** at the top of the script: learning outcomes, FR/NFR, acceptance criteria, programme blocks, risks, roadmap phases, and the links between them (`lu`, `fr`, `measuredBy` arrays). Tables, diagrams and counts all render from that object.

- Counts ("16 functional requirements") are computed, never typed — this removes the *Losing counts* mistake at the root.
- Cross-references (AC → FR, FR → LU, risk → FR) are IDs in the data, rendered as clickable chips that scroll to and highlight the target.
- Prose (context, frameworks, explanations) stays as static HTML, so the argument reads without JavaScript.

### Visual vocabulary — which Part gets which visual

Every visual must **explain a structure in the design**, not decorate. If a visual doesn't answer a question the reader has, drop it.

| Part | Visual | Library | Question it answers |
|---|---|---|---|
| Header | One 3D or animated emblem of the core mechanism (e.g. the product that grows over the sessions), interactive per session | Three.js | "What is the big idea?" |
| 2 — Quality system | Point → axiom cards that reveal in sequence | Motion | "Which theory forces which choice?" |
| 3 — Learning outcomes | Bloom matrix (process × knowledge) with each outcome plotted; click shows the full outcome | D3 | "Is the cognitive level right, and where are the gaps?" |
| 5 — Design criteria | KISS as chosen-vs-rejected pairs | CSS (brand tier cards) | "What did we decide *not* to do?" |
| 6 — Core mechanism | Animated flow or growth diagram; rhythm of a recurring block as an arc/bar | D3 + Motion | "How does the mechanism work over time?" |
| 7 + 11 — Requirements & acceptance | Traceability graph LU → FR → AC; hover highlights the full chain | D3 | "Is every outcome built and measured?" |
| 8 — Programme | Per-session timeline, blocks proportional to duration, tabs per session, click for details | D3 or CSS grid | "What happens when, and why?" |
| 13 — Roadmap | Timeline with phases and a "today" marker | D3 | "Where are we now?" |

### Technical rules

- **Libraries** as ES modules from a pinned CDN version, e.g. `https://cdn.jsdelivr.net/npm/d3@7.9.0/+esm`, `https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js`, `https://cdn.jsdelivr.net/npm/motion@11.11.13/+esm`. Never an unpinned `@latest`.
- **Brand.** If the project names a styleguide or brand folder, copy its CSS tokens, components and logo verbatim (Process step 8) and follow its colour and voice rules. Without one, use a restrained neutral palette with a single accent colour.
- **Motion with restraint.** Reveal on scroll, stagger lists, animate a diagram once when it enters the viewport. No looping motion except one slow ambient element in the header. Honour `prefers-reduced-motion`: everything renders in its final state.
- **Feedback stays in view.** When hovering or clicking part of a visual changes something else (a detail panel, a highlight), the reader must see that change without scrolling. Put the panel beside the visual, or make it stick to the viewport while the visual is in view. Never put it below a visual taller than about half a screen.
- **Accessible.** Every diagram has a text alternative (`aria-label`, or a table that holds the same data); colour is never the only carrier of meaning; controls work by keyboard.
- **Print.** `@media print` hides navigation and animation, expands every tab and collapsed panel, and keeps tables intact.
- **Responsive.** Readable at phone width; diagrams scale with their container.

## Decision Records and Change Log

Every LRD project keeps two companion files next to the LRD. They are separate files in the repo, not sections of the LRD page.

- **`docs/adr/ADR-NNN-<slug>.md`, one per design decision**, plus an index `docs/adr/README.md`. Write an ADR whenever a decision changes the architecture (Process steps 2 and 6), whenever the user picks one option from a question, and whenever a review recommendation is accepted or deliberately not taken. Shape: Status (Accepted, or Superseded by ADR-NNN) · Date · Decided by · Context · Decision · Alternatives considered (with why each was rejected) · Consequences (including the costs) · Affects (LRD parts and IDs).
- **Never rewrite a superseded decision.** Add a new ADR and set the old one to "Superseded by ADR-NNN". A reversal within the same session still gets its own ADR: the history of why is the point.
- **`CHANGELOG.md`, one entry per version**, newest first: version, date, Added / Changed / Removed, each line citing its ADR. Every publish (for example an artifact URL) gets an entry. The version in the LRD header must equal the top entry.
- Write both in the language of the LRD.

## Process

1. **Explore before drafting.** Read every doc the new LRD builds on (module overviews, prior LRDs, pedagogical background material) for the house template and the facts already established. Don't restate what those docs already say — link to them.
2. **Clarify architecture before writing prose.** For genuine design decisions (which framework variant, what the core mechanism does, team structure, output format/language) ask one focused question at a time with concrete recommended options. Reserve this for decisions that ripple across multiple Parts — a wording tweak doesn't need a question.
3. **Ground every pedagogical claim in a real, verifiable source — never invent one.** Cite the specific framework from the project's background material and state the design axiom it implies. If no background material exists, use a well-established named framework you're confident is real (Bloom's taxonomy, Pink's *Drive*, Deci & Ryan's SDT) rather than fabricating a plausible-sounding citation — a fabricated source is worse than an explicit `[TBD — needs a real source]` placeholder. Match whatever citation style the project's other docs already use; default to `Author, Year. *Title*` if none exists.
4. **Write outcomes as user stories tied to a role, not a task.** *"A learner can \<verb\>, so that \<as a future role, they can...\>"* forces every outcome to earn its place. If the module trains a professional identity, define that role explicitly before writing outcomes against it.
5. **State KISS as rejections, not intentions.** "One mechanism, not two" only means something if you name the two-mechanism alternative that was rejected and why. Test the whole design against the front-loading rule: the teacher or trainer's work belongs in the design, not in the sessions. During contact time learners work autonomously with the programme; the teacher or trainer only facilitates and measures how well the design holds up. Every session that needs live explanation, steering or repair marks work the design has not yet done — name it in the design criteria.
6. **When a request changes architecture mid-document** (e.g. "these two roles should work as one team," "this AI shouldn't be learner-built"), stop and treat it like step 2: identify which Parts, cross-references, and numbered items ripple before editing anything, and ask if the ripple is genuinely ambiguous.
7. **After any structural edit, re-verify the whole document, not just the section touched:**
   - Grep for stale references to renumbered sections, renamed entities, and counts that no longer match (e.g. search for the old section number, or for "five" after a sixth item was added).
   - Run an opening/closing tag-balance check before and after.
   - Check the data object: every ID referenced in `lu`, `fr`, `measuredBy` or a risk mitigation must exist.
   - Open it in a browser at desktop and phone width, with no console errors, and once with reduced motion on.
8. **Reuse the house visual style verbatim** if a sibling document or a named styleguide exists — copy its CSS/brand system rather than inventing a new one.
9. **Record the decision and the change.** Before finishing any change to the LRD, add or supersede the ADR and add the changelog entry (see *Decision Records and Change Log*), and bump the version in the LRD header.
10. **Track multi-part rewrites with a todo list.** An architecture-level LRD redesign touches 8–10 sections at once; track each as its own step so nothing gets silently skipped.
11. **Don't commit or push unless asked.**

## Common Mistakes

- **Treating an architecture change as a text edit.** "Make each team do both roles" reads like a rewording but actually invalidates the gate table, the FR numbering, the risk table, and every learning outcome's wording. Ask before rewriting; then rewrite everything the change touches, not just the sentence quoted.
- **Silent renumbering drift.** Inserting a new subsection (e.g. a new §6.2) shifts every later cross-reference. Grep for the old numbers after any insert or reorder — don't trust memory.
- **Conflating "who builds it" with "who it grades."** If a mechanism assesses learners, the learners it assesses shouldn't also control its rubric or prompts — state ownership (module owners vs. learners) explicitly, both in the mechanism's own section and in every deliverables/roadmap reference to who builds it.
- **Losing counts after edits.** "Five learning outcomes" silently becomes wrong the moment a sixth is added elsewhere — grep for cardinal numbers near "outcomes," "requirements," etc. after any addition.
- **KISS bullets that don't reject anything.** "Keep it simple" as a bullet with no named alternative is decoration, not a constraint.
- **Decorative visuals.** A spinning 3D object or a chart that repeats a table adds load time, not understanding. Each visual must answer the question in the visual-vocabulary table.
- **Typing data twice.** Writing an FR in a table *and* in a diagram label guarantees drift. Render both from the data object.
- **Identifying participants.** Part 4 describes the audience, not people. Never name a learner's employer, own company or a work domain that points to it, in the LRD or in any companion document. A rare first name plus a function plus an organisation identifies a person. Refer to learners by pseudonym (Participant A, B …) with a general role. Keep the key only in the project's private input folder, and don't link to files whose names contain learners' names.
- **Deciding in the chat only.** A design choice that lives only in the conversation is lost the moment someone else opens the LRD. If it shaped the document, it gets an ADR.
- **Fabricating a citation when no background material exists.** Under pressure to fill out Part 2, it's tempting to invent a plausible-sounding author/year for a framework that doesn't exist. Don't — use a real, well-known framework instead, or mark the slot `[TBD — needs a real source]`.
