---
name: conrad-power-pitch
description: >
  Prepare a Conrad Challenge finalist team for the Innovation Summit at Space Center Houston -
  the Power Pitch to expert judges, the EXPO tabletop exhibit, and live hostile Q&A. Covers the
  eight-week window between the February finalist announcement and the April Summit, how to apply
  the judges' written coaching comments to improve the submission (explicitly encouraged), pitch
  structure and rehearsal, the question bank judges actually ask, and the Expo awards that reward
  physical exhibit craft independently of the technology. Also serves as the authenticity check:
  a team that cannot answer mechanism, competitor, unit-cost and falsification questions without
  notes has a problem that must be fixed before Houston. Use whenever a team has been named a
  finalist or is preparing to pitch, or asks about the Innovation Summit, Power Pitch, EXPO,
  tabletop exhibit, judge Q&A, presentation practice, "路演", "决赛答辩", "如何准备峰会".
argument-hint: [pitch|qa|expo|revise|all] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad Power Pitch & Summit

You've made the top ~3%. The Innovation Summit runs four days at **Space Center Houston and NASA
Johnson Space Center** (April 22–25 in the 2025-26 cycle). Finalists deliver **Power Pitches** to
expert judges, exhibit at the **EXPO**, and receive **live feedback**.

**Attendance is $499 per guest**, with financial aid available. Apply for it.

---

## First: you have ~8 weeks, and you're allowed to improve

Finalists are announced in **February**; the Summit is in **April**. Two things follow.

**1. You will receive written coaching comments from 3+ expert judges.** This is the most valuable
feedback available in high-school competition. Read every word.

**2. You may act on it.** Chief Judge, verbatim: *"Yes, finalist teams are encouraged to apply
feedback to improve their submission and pitch for the in-person Innovation Summit in April."*

**Therefore:** treat the comments as a prioritised work order, not a report card.
Note that judges are forbidden from mentioning scores, so comments will not say what's weakest
in point terms. Map them yourself:

| Comment theme | Rubric block | Weight |
|---|---|---|
| "I recommend you research competitors…" | Innovation / Marketing | high |
| "It's unclear how this works technically…" | Practicality | 20% |
| "Consider how you'd reach these customers…" | Marketing | 20% |
| "Estimate costs and pricing…" | Finances | 10% (cheap to fix) |

Run `/conrad-judge-simulator` on the revised version before Houston.

---

## The Power Pitch

Confirm current format and timing with Conrad staff — it varies by year. Prepare for a short
pitch followed by live judge questions.

### Structure

| Beat | Content |
|---|---|
| **Hook** | One concrete person with the problem. Not a global statistic. |
| **Problem** | Quantified, sourced, in one sentence |
| **Innovation** | The mechanism — show the model |
| **Evidence** | Why you believe it works; state limitations honestly |
| **Market & money** | Who buys, unit economics, the ask |
| **Moat** | Why a competitor can't just copy it |
| **Close** | What you need and where this goes |

The Chief Judge's own framing: *"a beginning including highlights and a teaser, a middle with
information and proof, and an end with a punchline promise or final reveal."*

### Delivery rules

- **Rehearse until you don't need notes.** Then rehearse the version where the tech fails.
- **Never say "I don't know" about your own technology.** Judges have explicitly flagged this as
  destroying investor confidence. For genuine unknowns: *"We haven't tested that yet — the
  experiment we'd run is X."* That is a strong answer; "I don't know" is not.
- **Every team member speaks.** Conrad is a team competition and judges notice a single-presenter team.
- **Bring the model.** Physical beats slides.
- **Watch tone.** Casual improvisation reads as unpreparedness; uniform excitement reads as a pitch deck.

---

## The Q&A question bank

Judges are professionals asking real questions. Prepare answers, out loud, without notes.

**Mechanism**
- Walk me through how this actually works, step by step.
- What happens when [failure mode]?
- Where does the energy come from?
- What's the hardest engineering problem you haven't solved?

**Originality — the one that catches ghost-written projects**
- **How did you choose this problem?**
- **Why did you reject the other ideas you considered?**
- Who else is doing this? What do they do better than you?
- What would you do if [named incumbent] launched this next year?

**Evidence**
- What have you actually tested? What were the numbers?
- What would falsify your approach?
- Who outside your team has reviewed this?

**Business**
- What does one unit cost to make? What do you sell it for?
- Who is your first customer — name one.
- Who pays, and is that the same as who uses it?
- What do you need the money for, specifically?

**Team**
- Who did what?
- What was the biggest disagreement and how did you resolve it?

### The authenticity check — for coaches and mentors especially

> **If a student cannot answer the mechanism, competitor, unit-cost, and "why did you reject the
> other ideas" questions without notes, the project is not theirs — and Houston is where that
> becomes visible.**

The Summit is an authenticity test by design: live pitch, live Q&A, and an Expo table where judges
walk up and ask about the mechanism. There is no way to fake it in person. If this check fails in
February, there are eight weeks to fix it — by having the student genuinely learn and rebuild
their understanding. That is fixable. Finding out in April is not.

See `/conrad-integrity-guard`.

---

## The EXPO tabletop

There are **two dedicated Expo awards** — the Simon Glinsky Expo Exhibit Awards for
**Most Persuasive** and **Best Tabletop** — plus Best Entrepreneurial Innovators. These reward
exhibit craft and persuasion **independently of the technology**. A team that isn't going to win
its category can absolutely win here.

What works:
- **The physical model, touchable.** The single biggest draw.
- **One large, legible headline** readable from 3 metres — the one-sentence pitch.
- **A before/after or comparison visual** — your delta versus the incumbent, as a graphic
- **One number, made large.** "$250 vs $10,000." "94.7% in under 1 second."
- **A 30-second version and a 3-minute version** of your explanation, both rehearsed
- **Everyone can pitch** — visitors arrive one at a time, continuously
- Something for the visitor's hands

What doesn't: walls of text, printed brief pages, unreadable screenshots, one person presenting
while the rest stand behind.

---

## Practical Summit notes

- Four days: Power Pitch, EXPO, workshops, tours, speakers, community sessions.
- Professional dress — finalist photos are public.
- Bring: model + spares, printed backup of key visuals, chargers, adapters, business cards.
- Assume nothing about wifi or AV. Have an offline version of everything.
- Team photo and innovation image appear on the public Global Finalists page.
- The **Alumni Leader Council** and the alumni network are real ongoing value — meet people.
- **Awards beyond Pete Conrad Scholar:** Power Pitch, Equinor "Searching for Better",
  Donald James Citizenship, both Expo awards, Best Entrepreneurial Innovators. Several reward
  things other than the technology.

## Rehearsal protocol

1. **Full run, timed, no notes.** Record it. Watch it. It will be worse than you think.
2. **Hostile Q&A** — the coach or mentor asks 10 questions from the bank, unfriendly.
3. **The mechanism whiteboard test** — explain how it works with a marker and nothing else.
4. **The stranger test** — pitch to someone with no context. Can they repeat it back?
5. **Failure rehearsal** — the model breaks, the slides don't load. Pitch anyway.
6. Repeat until 1 is clean and 2 produces no surprises.

## Epilogue

```
---
conrad-power-pitch · rubric_version 2025-26.1
Finalists are encouraged to apply judge feedback before the Summit — use the 8 weeks.
Confirm current pitch format and timing with Conrad staff.
The pitch, the answers, and the understanding behind them must be the students' own.
Next: /conrad-judge-simulator on the revised submission before Houston.
```
