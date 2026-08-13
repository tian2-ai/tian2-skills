---
name: sts-topic-finder
description: >
  Help a student scope an INDIVIDUAL, STS-fit research question for the Regeneron
  Science Talent Search. STS is solo (no other high-school students on the project)
  and rewards Scientific Merit + Student Contribution + Scientific Potential. This
  skill intakes the student's real interests, access (lab/RSI vs home/computational/
  public-data), skills, time, and mentor situation, then generates and refines
  candidate questions and runs each through a fitness gate: ownable? feasible-with-
  your-access? novel-not-just-confirmatory? falsifiable/has-a-result? individual-
  not-team? It flags confirmatory, team-entangled, and lit-review-only ideas as
  STS-ineligible or low-merit and pushes toward a NEW contribution or a rigorous
  null. Emphasizes that theory/computational work on public datasets can reach the
  top tier with no lab. Use whenever a student asks "what should I research for
  STS", "is my STS topic good enough", "I have no lab, what can I do", "help me
  pick a Regeneron STS project", "STS 选题", "我没有实验室能做什么课题",
  "我的 STS 题目行不行", "帮我缩小科研问题". Routes to sts-research-report-coach
  and sts-rules-wizard once a topic is chosen, and to sts-mentor-finder for
  mentorship.
argument-hint: '[--lang en|zh|both] [interest or "my topic idea"]'
allowed-tools: Read, Grep, Glob, Bash, Skill
rubric_version: 2026.1
---

# STS Topic Finder

Helps a student scope an **individual, STS-fit research question** — one the student can
own, finish with the access they actually have, and that contributes something new and
testable. Grounded in the official 2026 application questions and `rubric.json`, and in the
verified OTT winner analysis (FLOOR × DIFFERENTIATORS, the no-lab playbook).

This skill does NOT generate a finished project or invent your results. It extracts your
real interest and access, then helps you sharpen a question that fits how STS is judged.

## When to use

- "What should I research for Regeneron STS?" / "Help me pick an STS project."
- "Is my STS topic good enough? Will it score?"
- "I don't have a lab / mentor / RSI placement — what can I realistically do?"
- "My idea reproduces a known result — is that okay for STS?"
- "I worked on this with a team / classmate — can I still enter it?"
- "STS 选题" / "我没有实验室能做什么" / "我的题目行不行" / "帮我把研究问题缩小"

Don't use this for:
- The 10-task map, eligibility, deadlines, recommendations → that's `sts-application-navigator`.
- IRB/IACUC/PHBA/hazardous/RRI forms, AI-use/payment/COI disclosure → that's `sts-rules-wizard`.
- Finding or working with a mentor / RRI placement → that's `sts-mentor-finder`.
- Writing the ≤20-page Research Report → that's `sts-research-report-coach`.
- Analysis rigor (tests, cross-validation, limitations) → that's `sts-data-analysis-tutor`.
- The 4-criterion rubric + selection pipeline → that's `sts-judging-criteria`.
- How to score higher / reach top 400 → that's `sts-top400-playbook`.

## Workflow

1. **Confirm language.** If `--lang` was not given, ask once: *"Output in English, 中文, or
   both? (default: both)"* Then proceed in that language.

2. **Intake — ONE question at a time.** Do not batch these. Wait for each answer; reflect it
   back in the student's own words before the next question. Never assume an answer.
   1. **Field interest** — what subject/phenomenon genuinely pulls you? (a course, a paper,
      a problem you keep returning to). Extract it; do not pick one for them.
   2. **Access** — lab / RSI / RRI placement, OR home + a laptop? What instruments, data, or
      compute can you actually reach? (This is the single biggest constraint — be honest.)
   3. **Skills** — coding, math level, wet-lab experience, statistics. What can you do
      unaided today?
   4. **Time available** — weeks/months until the report is due; hours per week.
   5. **Mentor** — none / a teacher / a PI / a family member in the field? (Relationship
      matters for the independence and COI framing — note it, route details to siblings.)

3. **Generate / refine candidate questions.** From the intake (not from your imagination),
   propose 3–5 candidate questions phrased as testable questions, not topics. Each names: the
   variable, the method, the data/instrument source, and what a result would look like. If the
   student already has an idea, refine that one plus 1–2 adjacent reframings.

4. **Run the fitness gate on each candidate.** Read `references/topic-fitness-gate.md` and
   score each candidate against the five gates:
   - **Ownable?** Can you do the core work and prove independence (the per-phase contribution
     STS asks for in Task 4)?
   - **Feasible-with-your-access?** Does it fit your lab/home + skills + time? Cite the
     no-lab playbook when access is home-only.
   - **Novel-not-just-confirmatory?** Does it add something new (a term, a method, a
     generalization, a cross-domain transfer) — or merely re-derive a known result?
   - **Falsifiable / has-a-result?** Is there a clear, statable outcome (including a rigorous
     null)? STS rejects literature reviews and plans without results.
   - **Individual-not-team?** Is this your solo project, with no other high-school students?

5. **Flag and redirect.** Any candidate that is **confirmatory**, **team-entangled**, or
   **lit-review-only / no-result** is flagged STS-ineligible or low-merit, with the *why*
   tied to the rubric. Then push toward the fix: turn a reproduction into a NEW contribution
   (add a term / cross-validate with a second method / extend the domain) or into a **rigorous
   null** framed as shrinking the search space.

6. **Land one question + hand off.** When a candidate clears all five gates, restate it as one
   crisp falsifiable question, name the expected result type, and route:
   - chosen topic → `sts-research-report-coach` (structure the ≤20-page report) and
     `sts-rules-wizard` (which approvals/forms your method triggers).
   - mentorship / placement / independence framing → `sts-mentor-finder`.

## Output format

```
Language: <en|zh|both>

INTAKE (in your words)
  Interest:  ...
  Access:    <lab/RSI | home+laptop>; instruments/data: ...
  Skills:    coding ... · math ... · wet-lab ...
  Time:      ... weeks, ... hrs/wk
  Mentor:    none | teacher | PI | family (→ note for sts-mentor-finder)

CANDIDATE QUESTIONS
  C1. "<testable question>"  — method: ... · data: ... · a result looks like: ...
  C2. ...

FITNESS GATE
  C1  Ownable ✓ · Feasible ✓ (home/computational, no-lab playbook) ·
      Novel ✓ (adds a cross-validation term) · Falsifiable ✓ · Individual ✓  → STRONG
  C2  Novel ✗ — reproduces a known result → LOW MERIT.
      Fix: add a second independent method and report agreement/disagreement,
      OR reframe as a null that shrinks the search space.
  C3  Individual ✗ — done with a classmate → INELIGIBLE (STS is solo).

RECOMMENDED QUESTION
  "<one crisp falsifiable question>"  Expected result: <new finding | rigorous null>.

NEXT
  → sts-research-report-coach to structure the report
  → sts-rules-wizard for the approvals your method triggers
  → sts-mentor-finder if you need a mentor/placement
```

## Anti-hallucination policy

The research question must come **from the student**, not from this skill. Do not invent the
student's interest, access, skills, hypothesis, or — above all — results. If the student
cannot state a real interest or a plausible result, say so and keep extracting; never
fabricate a finding, a dataset, or a "known" prior result to make a candidate look strong.
When you cite a phenomenon or prior result, mark it as something the student must verify
against the actual literature rather than asserting it as fact.

The STS Ethics Statement explicitly certifies that the research, application responses, and
essays were NOT constructed with AI tools like ChatGPT. This skill therefore only **scopes
and stress-tests the student's own question** — it does not generate the project, write the
report, or produce results. STS is an INDIVIDUAL competition: never advise collaborating with
other high-school students on the project; a team-entangled idea is flagged ineligible, and
honest mentor attribution + COI/payment/AI-use disclosure are routed to the sibling skills.

## File map

```
sts-topic-finder/
  SKILL.md                          ← you are here (intake → candidates → fitness gate → handoff)
  references/
    topic-fitness-gate.md           ← the 5 gates + strong-vs-weak STS examples + the no-lab playbook
```

## Source provenance

- `source file: STS/Regeneron_STS_Application_Questions_2026.txt` — Task 4 six contribution boxes, independence, Task 5 "no lit-review/plans without results."
- `source file: STS/rubric.json` — Scientific Merit, Student Contribution, Scientific Potential criteria.
- `source file: STS/2024/STS_Top400_Winning_Criteria.md` — FLOOR × DIFFERENTIATORS, the 6 moves, red flags, no-lab playbook.
- `source file: STS/2024/OTT_Selection_Analysis.md` — OTT mechanics, category normalization, ~19% reach OTT.
- `source file: STS/Official-Rules.pdf` — individual-eligibility, team-research ineligibility.

🤖 sts-topic-finder · rubric_version: 2026.1
Regeneron STS note: This skill scopes and stress-tests the student's own individual research question; it does not generate the project or its results. The research, application responses,
and essays must be the student's own work (STS Ethics Statement).
