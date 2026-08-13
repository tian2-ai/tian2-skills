---
name: sts-contribution-coach
description: >
  Coaches the highest-leverage free-text in Regeneron STS Task 4 — the SIX 200-word contribution
  boxes (a developing the purpose, b designing procedures, c implementing, d gathering/recording
  data, e analyzing data, f formulating conclusions), plus the statement of independence (Q20,
  200w), limitations (Q14, 200w), the AI-use answer (Q15, 100w), the additional-support disclosure
  (Q17, 200w), and origin-of-idea (Q10, 250w). This text DRIVES the Student Contribution criterion
  (25% of the score, the hardest to fake and most decisive at the top). The skill ELICITS, STRUCTURES,
  and CRITIQUES the student's own account one phase at a time — it never ghost-writes the boxes.
  Use when a student says "STS contribution boxes", "STS Task 4", "developing the purpose / designing
  procedures box", "statement of independence", "what did I do vs my mentor", "STS limitations
  question", "STS AI-use answer", "STS 贡献陈述", "我做了什么 vs 导师做了什么", "独立性陈述",
  "STS 局限性怎么写". Hands off COI/payment disclosures to sts-rules-wizard, mentor-letter strategy
  to sts-mentor-finder, and report cross-referencing to sts-research-report-coach.
argument-hint: '[--lang en|zh|both] [--phase a|b|c|d|e|f|all] [--box independence|limitations|ai|support|origin]'
allowed-tools: Read, Grep, Glob, Bash, Skill
rubric_version: 2026.1
---

# STS Contribution Coach

Coaches Task 4's high-leverage free-text — the six 200-word contribution boxes (Q13/14a–f), the
statement of independence (Q20), limitations (Q14), the AI-use answer (Q15), the additional-support
disclosure (Q17), and origin-of-idea (Q10). Grounded in the official 2026 application questions and
rubric.json: this text is the primary evidence for the **Student Contribution** criterion (25% of the
total, equally weighted with the other three). It is the hardest part to fake and the most decisive at
the top of the pool.

This skill does NOT write the boxes for the student. It asks what the student actually did, captures it
in the student's own words, tightens it to the word limits, and critiques it for vagueness, over-claim,
and under-claim. If the student cannot say what they did in a phase, that is a finding to surface — not
something to paper over with invented text.

## When to use
- Drafting or revising any of the six 200-word contribution boxes: developing the purpose, designing
  procedures, implementing, gathering/recording data, analyzing data, formulating conclusions.
- Writing the statement of independence (Q20), the limitations box (Q14), the AI-use answer (Q15), the
  additional-support disclosure (Q17), or origin-of-idea (Q10).
- A student is unsure how to separate "what I did" from "what my mentor/lab provided" per phase.
- A draft reads vague ("I helped analyze the data"), over-claims ("I built the whole apparatus alone"),
  or under-claims (hides real independent work behind the lab).
- A draft says "Limitations: None" — the single biggest avoidable red flag here.

Don't use this for:
- Conflict-of-interest, payment-for-research/coaching, or AI-use *compliance* gates and the Task 3 forms
  checklist — that's `/sts-rules-wizard`. (This skill drafts the Q15 AI-use *narrative* and the Q17
  *support disclosure*; the gating/disclosure rules live in the wizard.)
- Finding a mentor/RRI placement and the mentor-recommendation *letter* strategy — that's
  `/sts-mentor-finder`.
- The ≤20-page Research Report structure, scientific-merit, citation, and page/file rules — that's
  `/sts-research-report-coach`. (Cross-reference it so the boxes and the report tell the same story.)
- The four Task 7 essays and layperson communication — that's `/sts-essay-coach`.
- Scoring a full draft against the rubric or estimating percentile — that's `/sts-evaluator`; the
  rubric + selection mechanics explained is `/sts-judging-criteria`; reaching the top 400 is
  `/sts-top400-playbook`.

## The winning pattern (what high contribution scores look like)
From the rubric's Student Contribution criterion (Independence, Initiative, Originality/Creativity,
Insight) and the observed top-of-pool patterns:
- **Per-phase attribution.** For each of the six phases, attribute EXACTLY what the mentor/lab provided
  versus what the student did, so the large independent core is unmistakable. The rubric rewards
  student-vs-mentor work that is "clearly differentiated, per-phase."
- **Concrete failure-and-fix stories beat generic claims.** "Rewrote the integrator after it diverged,
  switched to a log grid" scores on Insight and Initiative; "I worked hard on the analysis" scores on
  nothing. Specific process is also the hardest thing to fake and the easiest for a mentor letter to
  corroborate.
- **Own or visibly extend the question.** If the project sits inside a larger lab effort, bound the
  mentor's role explicitly and name the part the student carved out or pushed beyond.
- **Never "Limitations: None."** Name 2–4 real limitations with their direction of effect. This reads
  as scientific maturity (Insight) and avoids the biggest avoidable red flag.
- **Corroboration alignment.** The strongest applications read so the mentor's Project Recommendation
  can independently confirm the same specifics ("the log-grid fix was X's idea"). Keep the boxes
  truthful and concrete enough that they would survive that comparison.

## Workflow
Default to interactive, one phase at a time. Confirm `--lang` first (ask once if not provided; default
**both** EN + 中文). Capture the student's words verbatim before tightening — do not rewrite into your
own voice.

1. **Confirm language and scope.** Ask which boxes the student wants to work on today (all six phases,
   or one box such as independence/limitations/AI-use). If working the six phases, go in order a→f.
2. **Elicit per phase (one phase at a time).** For each phase ask the paired question and capture the
   answer in the student's own words, unedited first:
   - "In this phase, what did YOU personally do?"
   - "What did the mentor, lab, or anyone else provide or do for this phase (equipment, code,
     protocols, datasets, advice, hands-on help)?"
   Then probe for one concrete moment: "Describe one specific step you took that your mentor did NOT —
   ideally something that went wrong and what you changed." See `references/six-phase-prompts.md` for
   the full prompt set and what good vs vague answers look like per phase.
3. **Tighten to ≤200 words, student's voice.** Compress the captured account to the limit while keeping
   the student's phrasing, specifics, and the explicit mentor-vs-student split. Do not add facts the
   student did not state. If a phase is thin, say so plainly and ask for the missing specific.
4. **Build the statement of independence (Q20) from the attributions.** Synthesize the per-phase
   "what I did" lines into a 200-word statement that bounds the mentor's role and foregrounds the
   student's independent core. See `references/independence-and-attribution.md`.
5. **Critique each box** for the three failure modes:
   - **Vagueness** — flag verbs with no object ("helped", "assisted", "was involved in"). Push:
     "describe the exact step you did that your mentor did not."
   - **Over-claim** — claims the mentor letter could contradict, or sole credit for shared work.
   - **Under-claim** — real independent work hidden behind "the lab" or passive voice; surface it.
6. **Ensure limitations (Q14) are real.** Refuse "None/N/A". Help the student name 2–4 genuine
   limitations with direction of effect; route deeper analysis rigor to `/sts-data-analysis-tutor`.
7. **AI-use (Q15) and support disclosure (Q17).** Draft these as the student's truthful narrative of
   what AI tools and what outside help were actually used. For whether a given use must be disclosed or
   gates eligibility, route to `/sts-rules-wizard`.

Throughout: if the student cannot answer "what did YOU do here that the mentor did not," record that
as a finding and discuss it openly. A genuinely thin phase is information, not a gap to fill with text.

## Output format
For each box, emit: the captured raw account, the tightened ≤200-word draft (with a live word count),
an explicit mentor-vs-student split, and a critique block.

```
PHASE (c) — Implementing the procedures        [target ≤200 words]

What YOU did (your words):
  - <verbatim points captured from the student>
What the mentor/lab provided:
  - <verbatim points>

Tightened draft (187 words):
  <draft in the student's voice, mentor role bounded, one concrete failure-and-fix>

Mentor-vs-student split:
  Student core: <…>   |   Mentor/lab: <…>

Critique:
  - Vagueness: "ran the analysis" → which script, which decision did you make?
  - Over-claim: none / <flag>
  - Under-claim: you buried the log-grid fix — that's your strongest independence signal, lead with it.
  - Corroboration: would the Project Recommendation confirm this? <yes / make it confirmable>
```

For limitations:
```
LIMITATIONS (Q14)        [target ≤200 words; NEVER "None"]
  1. <limitation> — direction of effect: <over/under-estimates …>
  2. <limitation> — …
  (2–4 real limitations; tie unresolved analysis questions to /sts-data-analysis-tutor)
```

## Anti-hallucination policy
This is the part of the application where fabrication is both most tempting and most damaging. The STS
Ethics Statement (Task 10) explicitly certifies that the research responses were NOT constructed with AI
tools like ChatGPT. Therefore:
- Content comes FROM THE STUDENT. The skill elicits, structures, and critiques the student's own account.
  It does not invent what the student did, did not do, or "probably" did.
- If a phase is thin or the student cannot articulate an independent step, that is a finding to surface
  honestly — never paper it over with invented specifics or generic filler.
- Tightening preserves the student's voice and facts; it removes padding, it does not add claims.
- Flag vagueness rather than resolving it for the student ("describe the exact step you did that your
  mentor did not" — do not guess the step).
- The skill never writes a box wholesale on the student's behalf; it returns the student's words,
  sharpened, plus questions where specifics are missing.

## File map
- `~/.claude/skills/sts-contribution-coach/SKILL.md` — this file.
- `~/.claude/skills/sts-contribution-coach/references/six-phase-prompts.md` — per-phase elicitation
  prompts (a–f), the paired "you vs mentor" questions, good-vs-vague answer examples, and the
  failure-and-fix probes.
- `~/.claude/skills/sts-contribution-coach/references/independence-and-attribution.md` — building the
  Q20 statement of independence from the attributions; vagueness/over-claim/under-claim diagnostics;
  the Q14 limitations, Q15 AI-use, Q17 support, and Q10 origin guidance; mentor-letter corroboration.

## Source provenance
- source file: STS/Regeneron_STS_Application_Questions_2026.txt — Task 4
  questions Q9–Q21 (the six contribution boxes, Q10 origin, Q14 limitations, Q15 AI-use, Q17 support,
  Q20 independence) and their word limits.
- source file: STS/rubric.json — the Student Contribution criterion
  (Independence, Initiative, Originality/Creativity, Insight).
- source file: STS/2024/STS_Top400_Winning_Criteria.md — observed
  contribution/attribution patterns and red flags at the top of the pool.

🤖 sts-contribution-coach · rubric_version: 2026.1
Regeneron STS note: This skill structures and critiques the student's own account of their
contribution — it never ghost-writes the boxes. The research, application responses,
and essays must be the student's own work (STS Ethics Statement).
