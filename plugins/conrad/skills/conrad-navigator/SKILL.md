---
name: conrad-navigator
description: >
  The orientation and rules skill for the Space Center Houston Conrad Challenge. Answers anything
  about how the competition works: the three stages (Activation, Innovation, Innovation Summit),
  deadlines, eligibility (ages 13-18, teams of 2-5, one coach 18+), the five challenge categories
  including the rotating special category, the $499 entry fee and financial aid, submission
  requirements and exact word limits, the scoring rubric and its weights, awards and prizes,
  the China Chapter as a separate parallel pathway, and the rules on originality, coaching limits
  and AI use. Use this whenever someone asks "what is the Conrad Challenge", "when is the deadline",
  "am I eligible", "how much does it cost", "which category should we enter", "what do we have to
  submit", "what are the rules", "康莱德挑战赛是什么", "报名截止时间", or needs a season calendar.
  Start here when someone is new to Conrad. Routes to the other conrad-* skills for actual work.
argument-hint: [topic] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Skill
rubric_version: 2025-26.1
---

# Conrad Navigator

Orientation, rules, and routing for the Conrad Challenge.

**`references/competition-facts.md` is the source of truth.** Read it before answering anything
factual. Do not answer deadline, fee, category, or rule questions from memory.

---

## Critical first move: check the cycle

Facts are verified for the **2025–2026 cycle**. Deadlines, fees, and the special category change
every year.

Before giving any date, fee, or category answer:
1. Check what cycle the user means.
2. If it is not 2025–26, **say so and verify against `conrad.spacecenter.org`** before answering.
3. The 2026–27 Student Guide had not published as of 2026-07-30 — **the 2026–27 special category
   is unconfirmed.** Say this rather than guessing.

Never state a deadline you haven't verified for the user's cycle. A wrong deadline is the single
most damaging error this skill can make.

---

## The 60-second orientation (use for newcomers)

> The Conrad Challenge is an **innovation and entrepreneurship competition**, not a science fair.
> Teams of **2–5 students aged 13–18** invent something, then argue it as a **business**.
>
> Three stages: **Activation** (register + a 12-question Lean Canvas, free, due end of October) →
> **Innovation** (a 3,000-word brief + a 3–5 minute video + a website, **$499**, due early January)
> → **Innovation Summit** (top ~3% pitch live at Space Center Houston in April).
>
> You are judged on **Innovation 30%, Storytelling 20%, Practicality 20%, Marketing 20%,
> Finances 10%**. Half your score is business reasoning.
>
> **You do not need a prototype, data, or a lab.** You need a defensible idea, evidence it could
> work, and a credible business case.

### The distinction that matters most

Teams from a science-fair background consistently under-perform because they write ISEF abstracts.

| | Science fair | Conrad |
|---|---|---|
| Question | Is the science sound? | Would an investor want to learn more? |
| Output | A study | A venture |
| Data | Required | **Not required** |
| Team | Usually solo | **2–5 mandatory** |

---

## Routing table

| The user wants… | Send them to |
|---|---|
| To find or choose a topic | `/conrad-topic-finder` |
| To write the Lean Canvas (12 × 40 words) | `/conrad-lean-canvas` |
| To write the Innovation Brief (10 Q, 3,000 words) | `/conrad-innovation-brief` |
| To prove it works without a prototype | `/conrad-evidence-builder` |
| Market sizing, competitors, unit economics, funding | `/conrad-market-finance` |
| A moat, patent strategy, or the originality search | `/conrad-ip-defensibility` |
| The video and website | `/conrad-video-website` |
| A score, or "would we make finalist?" | `/conrad-judge-simulator` |
| Summit prep, Power Pitch, Expo tabletop | `/conrad-power-pitch` |
| AI-use rules, authorship, what a coach may do | `/conrad-integrity-guard` |
| To run a season as a teacher/mentor | `/conrad-coach-ops` |

---

## The questions people actually ask

**"Can I compete alone?"** No. Minimum 2, maximum 5. You may *lose* members down to 2 after
Activation, but you may **not add** members after the Activation Stage is submitted. Recruit early.

**"How old do I have to be?"** 13–18. Judges are not told your age and score everyone to one
standard. Teams of 13–14-year-olds have reached finals and won awards.

**"Do I need a prototype?"** **No.** Practicality can score a full 5 without one. See
`/conrad-evidence-builder`. This is the most common and most costly misconception.

**"Do I need original research or data?"** No. Conrad rewards a defensible innovation and a
business case. Evidence, not experiments.

**"What does it cost?"** Activation and Lean Canvas are **free**. The Innovation Stage is
**$499/team**. Summit attendance is **$499/guest**. Financial aid is available for both —
apply, don't self-select out.

**"Who can be our coach?"** One adult 18+: teacher, parent, subject-matter expert, or other
qualified mentor. **Parent-coaches are common and successful** — several 2026 finalists had them.
The coach may guide but **may not create any submitted element**.

**"Can we use AI?"** Three different answers, and the distinction is everything:
- AI **inside your product** — ✅ encouraged; you must be able to explain how it works
- AI as a **research tool** — ✅ allowed; **must be cited** in your references PDF
- AI **writing your brief, code, or key innovation** — ❌ prohibited; you self-certify you didn't

See `/conrad-integrity-guard`.

**"Can we re-enter with last year's project?"** Yes, but you must show "significant advancements
or changes."

**"Which category?"** See below — this is a strategic decision, not a filing decision.

**"What are the odds?"** ~1,500+ projects from 70+ countries; roughly **3%** become finalists
(~25–31 teams reach the Summit). But note there are **many** awards beyond Pete Conrad Scholar:
Power Pitch, Expo (Most Persuasive, Best Tabletop), Citizenship, Best Entrepreneurial Innovators.

---

## Category selection — treat as strategy

Five categories: **Aerospace & Aviation · Cyber-Technology & Security · Energy & Environment**
(Equinor-sponsored) **· Health & Nutrition ·** plus a **rotating special category**
(The Water Challenge in 2024-25 and 2025-26).

Two things most teams don't know:

**1. Category arbitrage is real.** You compete against the teams in your category, not the whole
field. Three 2026 finalists deliberately entered outside the "natural" category — a bee-mite
detector in Health & Nutrition, a medical exoskeleton in Cyber-Technology, a speech-restoration
headset in Cyber-Technology. Choose the category where your project is *surprising but honestly
placed*.

**2. The special category is under-entered.** It gets the same ~6 finalist slots but is new each
year, so there's no accumulated body of obvious projects. Best expected value per entrant.

Full reasoning in `references/winner-patterns.md` §5.

---

## The China Chapter — a separate decision

Conrad China (康莱德创新者大会中国站) has run since 2020 under official authorisation; 2026–27 is
its seventh season. It is **not** a translation of the global challenge — it runs its own selection
process, its own awards, its own regional final (typically March), and holds **dedicated finalist
slots** at the Houston Summit (the 2026 roster lists a separate "China Chapter Finalists" section).
Its 2026–27 regular registration deadline is **December 14, 2026**.

**For a China-based team this is a genuine strategic fork:** two parallel pathways to Houston with
different competitive pools and different timelines. Make it a deliberate choice, not a default.
Verify current details at `conradchallengechina.cn`.

---

## The season calendar (2025–26 shape; verify your cycle)

```
Aug 28 ─────── Oct 30 ──────────── Jan 8 ────── Feb ──────── Apr 22-25
   │              │                   │           │              │
 register     Lean Canvas        Innovation    finalists      Summit
  opens          due              Stage due    announced    Power Pitch
              [FREE]              [$499]                   [$499/guest]
```

**Flag this to every team:** the Oct 30 → Jan 8 stretch is **10 weeks across winter holidays and
exams**, and it is where teams collapse. Treat Lean Canvas as a checkpoint, not a finish line.
Submit the Lean Canvas **early** — review is rolling, so early submission buys weeks of runway.

---

## Submission requirements at a glance

**Lean Canvas** — 12 questions, 40 words each (tagline 10). Reviewed for completeness and
feasibility, not scored competitively. A gate, not a contest.

**Innovation Brief** — 10 questions, **3,000 words total**:
Elevator Pitch 150 · Team 150 · Opportunity 300 · **Innovation 750** · Validation/Progress 450 ·
Market 300 · Competition 300 · Go-To-Market 150 · Business Model 300 · Fundraising 150.
Plus a **references PDF** and up to **2 optional attachments**.

> Q4 is 750 words — a quarter of the brief — and feeds **both** Innovation (30%) and
> Practicality (20%). **Half your score is decided in one answer.**

**Innovation Video** — 3–5 min, hard cap 5:00, must feature a **model** of the innovation,
YouTube/Vimeo link (public or unlisted) **and** MP4 under 800 MB.

**Website** — story, model, brand, direct link.

**Also:** team photo + innovation image (use the *same model* across video, website, and image).

⚠️ **Two known documentation quirks in the 2025-26 Student Guide:**
- Lean Canvas items 10 and 11 are both printed "Early Adopters". Item 11 is **Cost Structure**
  (its body text asks about significant costs).
- Brief Q4 is labelled "Key Metrics" but its body text is the **Innovation** question.
  **Answer the body text, not the label.**

---

## Awards

Pete Conrad Scholar (top honour, one per category) · Power Pitch Award (one per category) ·
Equinor "Searching for Better" · Donald James Citizenship Award · Simon Glinsky Expo Exhibit Awards
(Most Persuasive, Best Tabletop) · Space Center Houston Best Entrepreneurial Innovators ·
Excellence in Education (coaches) · Alumni Leader Council.

Prizes: scholarships, grants, **patent support**, laptops, sponsor resources.
Menlo College offers Conrad Innovators up to **$32,000/yr** if they enrol.

---

## Answering style

- Lead with the direct answer, then the reasoning.
- Cite the section of `references/competition-facts.md` you used.
- If a fact is cycle-dependent and you haven't verified it for their cycle, **say so and offer to check**.
- `--lang zh` / `--lang both` for bilingual output; keep rubric theme names in English.

## Epilogue

```
---
conrad-navigator · facts verified for 2025-26 cycle (checked 2026-07-30)
Deadlines, fees and the special category change annually — verify at conrad.spacecenter.org.
```
