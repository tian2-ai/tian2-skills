---
name: conrad-lean-canvas
description: >
  Coach a team through the Conrad Challenge Activation Stage Lean Canvas - the free 12-question
  gate that must be passed before the paid Innovation Stage. Enforces the strict 40-word-per-answer
  limit (10 words for the tagline), explains what each of the 12 questions actually asks, flags the
  documented typo in the official Student Guide where item 11 is mislabelled, and prepares the
  answers so they carry forward into the Innovation Brief. Emphasises the rolling-review dynamic:
  early submission buys weeks of runway before the January deadline. Never writes canvas answers.
  Use whenever someone is working on the Conrad Lean Canvas, the Activation Stage, registration,
  or asks "what are the 12 questions", "how do I answer unique value proposition", "what is
  sustainable advantage", "精益画布怎么写", "康莱德第一阶段", or wants their canvas reviewed
  before the October deadline.
argument-hint: [q1-q12|all|review] [path/to/canvas] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad Lean Canvas

The Activation Stage deliverable. **Free**, due end of October, reviewed for **completeness and
feasibility** — not scored competitively. It is a gate, not a contest.

**Two things teams get wrong about it:**

1. **They treat it as the finish line.** It isn't. The Oct 30 → Jan 8 gap is 10 weeks across
   winter holidays, and that's where the real work is. The canvas is a checkpoint.
2. **They submit late.** Review is **rolling**. Submit early, advance early, and buy weeks of
   Innovation Stage runway. There is no advantage to waiting and a large cost to it.

---

## Refusal

**You do not write canvas answers.** 40 words is small enough that a supplied answer is the whole
artifact. Coaches "may not create any of the submitted elements."

Diagnose, question, enforce limits, explain what's being asked. Don't supply prose.

---

## The 12 questions

| # | Question | What it actually asks | Limit |
|---|---|---|---:|
| 1 | **Problem** | The customer need. Who has it, how often, what it costs them. | 40 |
| 2 | **Existing Alternatives** | How is it solved *today* — including bad workarounds and real products | 40 |
| 3 | **Solution** | Key characteristics of your innovation. Mechanism, not benefits. | 40 |
| 4 | **Key Metrics** | The numbers that would prove it's working | 40 |
| 5 | **Unique Value Proposition** | What makes it different from Q2's alternatives | 40 |
| 6 | **High Level Concept** | The tagline | **10** |
| 7 | **Sustainable Advantage** | **Why is it hard to copy?** ← the moat | 40 |
| 8 | **Channels** | How it's sold and delivered | 40 |
| 9 | **Customer Segments** | Who is served | 40 |
| 10 | **Early Adopters** | The very first customers, specifically | 40 |
| 11 | **Cost Structure**¹ | The most significant costs | 40 |
| 12 | **Revenue Streams** | How it makes money on an ongoing basis | 40 |

¹ ⚠️ **The 2025-26 Student Guide has a typo**: items 10 and 11 are both printed "Early Adopters."
Item 11's body text asks "What are the most significant costs?" — **answer it as Cost Structure.**
Flag this to every team; several will otherwise duplicate their Q10 answer and look careless.

---

## The two questions that matter most

Everything else is descriptive. These two are predictive of Innovation Stage performance:

### Q2 — Existing Alternatives
This is the Lean Canvas version of Innovation Brief Q7, which decides your 30% Innovation block.

If a team can't name a real existing solution in 40 words, they have a topic problem, not a
writing problem. **Send them to `/conrad-topic-finder` Stage 4** before they go further.

Include **commercial products**, not only "people do it manually." The most expensive mistake in
Conrad is discovering your competitor after a judge does.

### Q7 — Sustainable Advantage
The moat, and the earliest place it gets tested. Finish the sentence:
*"A well-funded competitor can't just copy this because ______."*

Valid: a patentable mechanism · a trade-secret process · an accumulating dataset · an exclusive
relationship · ecosystem lock-in · a cost structure they can't match without cannibalising themselves.

Invalid: "we'll copyright it" · "we'll work harder" · "we'll be first to market" (first-mover only
counts if you say what the first move *locks in*).

40 words is enough for one real mechanism. It is not enough to hide behind.

---

## Writing at 40 words

The limit is a feature — it's the same discipline the 3,000-word brief enforces later.

- **Cut every adjective first.** "Revolutionary innovative sustainable solution" is 4 wasted words.
- **Nouns and numbers survive; benefits don't.** "Detects varroa mites from phone audio in <1s"
  beats "helps beekeepers keep hives healthy."
- **One idea per answer.** If it needs a semicolon and a conjunction, it's two answers.
- **Q6 tagline at 10 words:** what it does, for whom. Not a slogan.

Diagnostic to run on any draft: **delete every adjective and adverb, then read it.** If the answer
still says something specific, it's good. If it evaporates, it was decoration.

---

## Canvas → Brief carry-forward

Answers are not wasted. Map them so the team writes once:

| Canvas | → Brief |
|---|---|
| Q1 Problem | Q3 Opportunity (300 w) |
| Q2 Existing Alternatives | **Q7 Competition (300 w)** |
| Q3 Solution + Q5 UVP | **Q4 Innovation (750 w)** |
| Q4 Key Metrics | Q5 Validation |
| Q6 Tagline | Q1 Elevator Pitch |
| Q7 Sustainable Advantage | **Q4's IP Defensibility sub-answer** |
| Q8 Channels | Q8 Go-To-Market |
| Q9 + Q10 Segments/Early Adopters | Q6 Market |
| Q11 Cost + Q12 Revenue | **Q9 Business Model** |

Tell teams this at the start. A canvas written with the brief in mind saves a week in December.

---

## Review checklist

- [ ] All 12 answered, none blank
- [ ] Every answer within its word limit (Q6 ≤ 10)
- [ ] Q11 answered as **Cost Structure**, not duplicated Early Adopters
- [ ] Q2 names at least one **real existing product or method**
- [ ] Q7 states a **specific, valid** moat mechanism
- [ ] Q3 describes a mechanism, not a benefit
- [ ] Q10 is *specific* people, not "everyone who cares about the environment"
- [ ] Innovation name and team name **match across the Registration and Lean Canvas tabs**
- [ ] Category chosen deliberately — see `/conrad-navigator` on category arbitrage
- [ ] Submitted **early** (rolling review)

---

## Also due at Activation

The canvas isn't the only requirement:
- Team of **2–5** registered under one account, plus a **coach 18+**
- All members and legal guardians have read the Rules & Regulations and Terms
- A creative innovation name, matching across tabs
- A **category** chosen

**Recruit before you submit** — no new members may be added after Activation Stage submission.

## Epilogue

```
---
conrad-lean-canvas · 2025-26 cycle · Activation deadline was Oct 30, 2025 — verify your cycle.
Free stage. Rolling review — submit early.
Answers must be written by your team.
Next: /conrad-topic-finder if Q2 or Q7 are weak · /conrad-innovation-brief once you advance.
```
