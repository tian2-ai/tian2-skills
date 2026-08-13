---
name: conrad-evidence-builder
description: >
  Build the Practicality case for a Conrad Challenge submission - the 20% of the score that asks
  "will it work?" - without requiring a prototype. Teaches the six-rung evidence ladder documented
  by the Conrad Chief Judge (component precedent, expert testimony, cited literature, graphic
  representation, prototype or demonstration, described future experiments), any combination of
  which can earn a full 5 out of 5. Also runs the mechanism audit that catches energy-balance and
  conservation errors, the single most common reason polished submissions stall around 75 points.
  Use whenever a team says "we can't afford a prototype", "how do we prove this works", "we have
  no lab", "what counts as validation", "how do I answer question 5", "怎么证明可行性",
  "没有原型怎么办"; or when a draft makes technical claims without support; or when a mentor needs
  to sanity-check the physics of a student project.
argument-hint: [ladder|audit|plan] [description or path] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad Evidence Builder

Practicality is **20%** of the score. Its sub-criteria: Feasibility · Realism · Proof of Concept ·
Evidence Base · Next Steps.

**The fact most teams don't know, and it's worth 20 points:**

> The Chief Judge, verbatim: *"Teams can attain **5 points for Practicality without a prototype**."*

The cited example: a jet-engine electrolyser hydrogen burner — impossible on a student budget —
scored **5 on Practicality and 4–5 on Innovation** with no prototype. It earned that through
component-technology explanation, credible drawings, technical explanation, cited expert testimony,
and exploratory talks with manufacturers.

Most teams write "we couldn't afford a prototype" and surrender the section. That is the mistake
this skill exists to prevent.

---

## The six-rung evidence ladder

Any combination establishes proof of concept. **Target ≥3 rungs.** Rungs 1–4 and 6 cost nothing.

| # | Rung | What it is | Cost | How to do it |
|---|---|---|---|---|
| 1 | **Component precedent** | Each sub-technology already works elsewhere | Free | Name a real deployed system using each component. Decompose your innovation into 3–5 blocks and cite one working precedent per block. |
| 2 | **Expert testimony** | A named credentialed person reviewed it | One email | See the template below. **Highest value per unit effort in the entire competition.** |
| 3 | **Cited literature** | Published research supports the mechanism | Free | Google Scholar, ScienceDirect. Cite inline *and* in the references PDF. |
| 4 | **Graphic representation** | Convincing CAD, schematic, cross-section, animation | Free–low | Use an attachment slot. Ocean Energy used a 3D model plus a rendered animation. |
| 5 | **Prototype or demonstration** | Partial or full physical build | $–$$$ | **Partial counts.** Build the one subsystem that carries the most doubt. |
| 6 | **Described future experiments** | A specific, credible test plan that *would* verify it | Free | Explicitly listed by the Chief Judge. Name the measurement, apparatus, and pass criterion. |

### Rung 2 — the email

The single highest-leverage action available. Two of the five briefs I judged would have gained
~15 points from one reply.

```
Subject: High school innovation project — one technical question

Dear Dr. ___,

I'm a high school student on a team competing in the Conrad Challenge, an innovation
competition run by Space Center Houston. We're designing [one sentence].

I found your work on [specific thing]. I have one question:
[the single question whose answer would most change your design]

Any brief reply would help us a great deal, and we'd cite you in our submission
with your permission.

Thank you,
[name], [school]
```

Rules: **the student sends it**, not the coach or mentor. One question, not five. Ask the question
whose answer could *change the design* — that's what makes it evidence rather than endorsement.
Ask permission to cite. Send to 3–5 people; expect 1–2 replies.

Targets: university faculty in the field, engineers at relevant companies, local practitioners
(clinicians, farmers, technicians), authors of papers you cited, industry association staff.

### Rung 5 — the partial prototype

You don't need the whole system. Build the subsystem that carries the **most doubt**.

Ocean Energy Dynamics built only the turbine + DC motor + Arduino, could not test with water,
**said so explicitly** — and that honesty read as competence.

> **The SUNSYNC rule: if you built it, measure it.** SUNSYNC had a working solar rig and claimed
> "twice as much energy, up to 90%" without ever measuring. An unmeasured prototype is worth *less*
> than a well-reasoned design, because it proves you had access and chose not to look.

Measure one thing. Plot it. Attach the plot.

---

## The mechanism audit — run before anything else

Two of five judged briefs had excellent business writing and stalled at ~66–76 because of this.
It is the difference between a 76 and a 90.

**1. Energy balance.** Where does every joule come from? Follow it back to a source.
- ❌ P-Bump: piezoelectric speed bump "harvests" energy — but the energy comes from the **car's
  engine** via added rolling resistance, at ~25% ICE efficiency, then piezo conversion. It is a
  net energy *loss* device that taxes every driver. The brief never says so.

**2. Closed loops.** Does the output power the input?
- ❌ Ocean Energy: extracts wave energy from a **moving ship's own motion**, which adds drag,
  then uses the electricity to power "an innovative propulsion system." That is perpetual motion.
  A marine engineer sees it instantly.

**3. Mass balance.** Does material conservation hold? Where does the waste go?

**4. Order of magnitude.** Units check every number.
- ❌ P-Bump: 46,875 Pa (~0.05 MPa) on a PZT stack. PZT is driven at *tens* of MPa. The geometry
  defeats the amplification by three orders of magnitude — while the arithmetic looks rigorous.

**5. Scale-up.** Does the mechanism survive being 100× bigger or 1000× more numerous?

### When the audit finds a flaw: reframe, don't abandon

Almost always there is an honest constrained version that scores **higher** than the ambitious
impossible one:

| Flawed claim | Honest reframe |
|---|---|
| Speed bump generates free energy | Energy is drawn from vehicles; viable **only where the bump is already required** for traffic calming, where the marginal fuel cost is the accepted price of a safety feature |
| Ship harvests wave energy to propel itself | Parasitic harvesting for **hotel loads on a moored or drifting vessel**, where drag is irrelevant |
| Solar tracker generates 90% more | Measured X% gain under conditions Y, with the concentration/heat trade-off stated |

The reframe is more interesting, survives scrutiny, and demonstrates the engineering judgement
judges are actually looking for.

---

## Writing Q5 (Validation / Progress, 450 words)

Structure that scores:

1. **What you tested or verified** (~150 w) — the specific thing, the method, the result with numbers
2. **Which ladder rungs you occupy** (~150 w) — component precedents, expert names and what they said,
   citations, the model
3. **Honest limitations** (~50 w) — what you could *not* test and why. **This helps you.**
4. **Next steps** (~100 w) — the specific experiment that would resolve the remaining doubt,
   with apparatus and pass criterion. This is the **Next Steps** sub-criterion; it is scored.

**Never write:** "we couldn't build a prototype due to budget constraints" and stop.
**Instead:** "A full build requires a vacuum chamber we don't have access to. We therefore verified
[X] by [method], confirmed [Y] with Dr. [name] of [institution], and the remaining uncertainty is
[Z], which would be resolved by [specific test]."

---

## Scoring self-check

| Practicality score | What it takes |
|---|---|
| 1–2 | Unrealistic, unworkable, or little evidence and reasoning |
| 3–4 | Plans and evidence are reasonable, reasoning is sound |
| 4–5 | Convincing, well-thought-out evidence for an unfunded start-up: similar uses, interviews or articles, reasoned application or prototype, technology demonstration |

Then honestly: how many rungs do you occupy? Has a domain expert confirmed no mechanism flaw?
Does energy/mass balance hold? Did you measure anything you built?

## Epilogue

```
---
conrad-evidence-builder · rubric_version 2025-26.1
No prototype required — evidence is. Target ≥3 ladder rungs.
The expert email must be sent by a student. Evidence gathered must be your team's own work.
Next: /conrad-judge-simulator to test the Practicality score · /conrad-innovation-brief for Q5.
```
