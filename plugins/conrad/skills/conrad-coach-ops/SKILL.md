---
name: conrad-coach-ops
description: >
  Run a Conrad Challenge season as a teacher, mentor, parent-coach or program operator. Provides
  the eight-stage season plan with milestone gates mapped to the real calendar, team formation and
  role assignment guidance, the weekly meeting structure, the go/no-go decision framework for the
  $499 Innovation Stage fee, multi-team management, and the mentoring boundary that keeps a
  commercial or school program compliant. Built around the structural fact that most teams collapse
  in the ten-week gap between the October Lean Canvas deadline and the January Innovation Stage
  deadline, which spans winter holidays and exams. Use whenever a teacher, coach, mentor, parent or
  tutoring program asks how to run Conrad, how to structure a club or class around it, how to form
  teams, when to do what, how to manage multiple teams, whether a team should pay the entry fee,
  "如何带队", "康莱德辅导", "season plan", or wants a curriculum or meeting schedule.
argument-hint: [season-plan|teams|gates|meeting|go-no-go|multi-team] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad Coach Operations

For the adult running the season. Your job is **process and standards** — not artifacts.
See `/conrad-integrity-guard` for the boundary; it is not optional reading.

---

## The structural fact that should shape your whole plan

```
Aug 28 ─────── Oct 30 ──────────── Jan 8 ────── Feb ──────── Apr 22-25
   │              │                   │           │              │
 register     Lean Canvas        Innovation    finalists      Summit
  opens          due              Stage due    announced    Power Pitch
              [FREE]              [$499]                   [$499/guest]
              ~9 weeks           ~10 weeks
                                   ▲
                        winter holidays + exams
                        ← this is where teams die →
```

**Most programs front-load onto the Lean Canvas because it has the visible deadline, then lose
teams over the winter break.** The canvas is the easy part and it's free.

**Design against this:**
- Submit the Lean Canvas **early** (review is rolling — early submission buys runway).
- Make the October gate require an **evidence plan**, not just the canvas.
- Schedule real work in **November**, and set a hard checkpoint on the **last day before break**.
- Plan an explicit re-entry session in the first week of January — the deadline is Jan 8.

---

## Season plan with gates

| # | Stage | When | Skill | Gate — do not pass without |
|---|---|---|---|---|
| 1 | **Team charter** | Aug | this skill | 2–5 members, roles named, coach registered, calendar agreed by families |
| 2 | **Asset inventory + domain scan** | Sep | `/conrad-topic-finder` 0–1 | 5+ named team assets, 12 problem territories |
| 3 | **Topic decision** | Sep–Oct | `/conrad-topic-finder` 2–7 | Topic card complete, **all 4 kill gates passed**, falsification done |
| 4 | **Lean Canvas** | Oct (due Oct 30) | `/conrad-lean-canvas` | 12 answers in limits + **an evidence plan for November** |
| 5 | **Evidence build** | **Nov–Dec** | `/conrad-evidence-builder` | ≥3 ladder rungs; **expert email sent** |
| 6 | **Brief + business case** | Dec | `/conrad-innovation-brief`, `/conrad-market-finance`, `/conrad-ip-defensibility` | Mock-judged score **≥75** |
| 7 | **Video + website** | Dec–Jan (due Jan 8) | `/conrad-video-website` | Links open in incognito; video <5:00 and <800MB |
| 8 | **Summit prep** | Feb–Apr | `/conrad-power-pitch` | Survives hostile Q&A without notes |

Continuous: `/conrad-judge-simulator` at every gate · `/conrad-integrity-guard` log maintained.

**Gate discipline is the whole job.** A gate that can be passed by showing up is not a gate.

---

## Team formation

**Size 2–5.** Data point worth knowing: in the 2026 finalist cohort, **two-person teams were the
most common size (11 of 31)**, with five-person teams next (7 of 31). **Size does not predict
success.** Don't force big teams for coverage.

Members may be **removed** but **never added** after Activation Stage submission. **Recruit before
you submit** — this is a hard, irreversible constraint that surprises programs every year.

### Roles worth naming explicitly

Conrad needs an unusual mix, and Q2 is scored on roles and capability:

| Role | Owns | Warning sign |
|---|---|---|
| **Technical lead** | Mechanism, Q4, the model | Team has no one who can explain how it works |
| **Research lead** | Originality search, evidence ladder, references PDF | Nobody is searching |
| **Business lead** | Market, competition, unit economics, Q6–Q10 | Everyone is an engineer |
| **Communications lead** | Video, website, brand, pitch | Left to the last two weeks |
| **Project lead** | Calendar, gates, submission mechanics | Missed deadlines |

Roles can double up on a 2-person team, but **someone must own the business half**. The most
common structural failure in school programs is an all-engineering team that scores 2 on
Marketing and Finances — 30% of the score.

### Cross-school and cross-border teams
Explicitly allowed and common among finalists (~9 of 31 in 2026 spanned states or countries).
If you're recruiting, you can look outside your school.

---

## Weekly meeting structure (60–90 min)

```
 5 min   Gate status — where are we against the calendar, honestly
10 min   Blockers — what's stuck, who's stuck, what unblocks it
40 min   The work — one focused activity, students working, you circulating
10 min   Standards check — you ask the hard question of the week
 5 min   Commitments — who does what by when, written down
```

**The hard question of the week** rotates and is the highest-value five minutes:
- Who else is doing this? What do they do better?
- Where does the energy come from?
- What does one unit cost?
- Who pays, and is that who uses it?
- Why can't a well-funded competitor copy this?
- What would prove you wrong?
- What have you actually measured?

Ask them the same way a judge would: expecting a specific answer, and waiting through the silence.

---

## The go/no-go decision on $499

Between Lean Canvas approval and the January deadline, every team faces a real financial decision.
Have it explicitly, with families, in **early November** — not in the last week.

**Go if:** the topic passed all four kill gates · at least one evidence rung is already secured ·
the team is still meeting · they can name a real competitor · someone owns the business half.

**No-go / defer a year if:** the topic failed falsification and hasn't been replaced ·
the team is down to one active member · nobody can explain the mechanism ·
there is no plan for the video and website.

**Say this to families plainly:** Activation and Lean Canvas are free. A team that gets a genuine
Lean Canvas done and *decides not to pay* has still had a real educational experience and lost
nothing. **Financial aid is available on both the $499 entry and the $499 Summit fee** — help
families apply rather than letting them self-select out.

For a first-year team, "reach the Innovation Stage and collect three expert judges' written
coaching comments" is an excellent goal. Those comments are the best input a second-year team
can have — and the winner data shows coaching compounds across seasons.

---

## Multi-team programs

- **One folder per team** (`teams/<name>/`), identical structure — see `architecture/SOLUTION.md`.
- **Run gates as cohort reviews**, not one-on-ones. Teams learn more from each other's
  mock judging than from yours, and it costs you a fraction of the time.
- **Deliberately spread categories** across teams — including the **special category**, which is
  under-entered and has the best odds per entrant.
- **Cross-team mock judging**: teams judge each other with `/conrad-judge-simulator`. This teaches
  the rubric faster than any lecture, and it is completely compliant.
- **Maintain a contribution log per team** from day one.

---

## Coaching standards — what makes teams good

**Do:**
- Ask questions instead of giving answers. Wait through the silence.
- Enforce gates even when it's uncomfortable, especially at the topic stage.
- Insist on measurement over assertion.
- Make them contact a real expert — the single highest-value action in the season.
- Run hostile mock Q&A early, in November, not April.
- Teach the rubric explicitly. Students who know the 25 sub-criteria write to them.

**Don't:**
- Write anything that will be submitted. Ever. (`/conrad-integrity-guard`)
- Supply the topic or a shortlist.
- Let an all-engineering team ignore the business half.
- Let the video and website slip to the last week — they're worth ~a quarter of the score.
- Let a team submit without one adult with **domain expertise** reviewing the mechanism.
  Two of the five briefs I judged lost ~15 points to flaws a single expert email would have caught.

---

## First-year program checklist

- [ ] Read `references/competition-facts.md` and `references/judging-playbook.md` end to end
- [ ] Verify this cycle's dates, fees, and special category at `conrad.spacecenter.org`
- [ ] Decide global chapter vs **China Chapter** if applicable — different pool and timeline
- [ ] Recruit and register teams before the Activation deadline
- [ ] Set calendar with families, flagging the winter-break risk explicitly
- [ ] Schedule the November go/no-go conversation
- [ ] Identify domain experts your teams can email
- [ ] Set up team folders and contribution logs
- [ ] Plan cross-team mock judging sessions
- [ ] Check financial aid eligibility for any family who needs it

## Epilogue

```
---
conrad-coach-ops · rubric_version 2025-26.1 · calendar shape from the 2025-26 cycle
Verify your cycle's dates before planning. Coaches may guide but may not create
any submitted element — see /conrad-integrity-guard.
Teaching materials: ../../curriculum/
```
