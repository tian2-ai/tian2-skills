# `score "topic"` flow — evaluate a topic the student already has

## Step 1 — Restate & classify
Restate the topic in one sentence and confirm the subject. If the subject is ambiguous (a
common silent failure), ask once or hand to `/yau-subject-navigator`.

## Step 2 — Pull grounding evidence
- Read `references/winning-patterns.md` + `references/judge-backgrounds.md` for the subject.
- Run `scripts/mine_winners.py "<topic keywords>"`. Record whether prior near-matches exist.
  If the archive is empty for these keywords, note it — it widens the range, it is not a green light.

## Step 3 — The originality gate (REQUIRED before scoring)
Ask the student, in one sentence: **"What is the one idea here that is yours — not from a paper,
a mentor, or an AI?"**
- If they give a crisp answer → proceed; this feeds O.
- If they can't → run the sharpening sub-dialog:
  - "What surprised you / annoyed you / seemed unexplained in what you read?"
  - "If a prior paper did X, what would you do differently and why?"
  - "What's the smallest new thing you could add on top of existing work?" (the doctrine's
    "加上一点儿原创性的想法")
  Cap O ≤ 5 until they produce a genuine answer. Do NOT invent one for them.

## Step 4 — The ownership gate
Ask: "Walk me through the hardest step — could you reproduce/derive it without notes, in English,
if a judge asked at the whiteboard?" Math especially: the panel re-derives lemmas live (ch.7).
If the method is beyond the student's reproduction, cap W ≤ 5 and name the defense risk.

## Step 5 — Score
Apply `references/scoring-rubric.md` with the caps. Compute the base, choose `h` by confidence,
emit the range.

## Step 6 — Diagnose + pivots
Identify the binding constraint (lowest weighted contributor). Give 2–3 concrete pivots that
each raise exactly that constraint — e.g. "to lift Originality, add a failure-mode analysis the
existing papers skip" or "to lift Feasibility, drop the wet-lab arm and validate computationally."

## Step 7 — Render (bilingual, depth-aware) + epilogue
Show the per-dimension scores, the range, the binding constraint, the pivots. Then the SKILL.md
epilogue. If score < ~50, append the discover/subject-navigator suggestion.
