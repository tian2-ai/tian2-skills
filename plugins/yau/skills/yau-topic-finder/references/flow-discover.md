# `discover` flow — topics from a student profile

Goal: turn the student's interests + constraints into 3–5 candidate topics, each scored as a
range. You are surfacing options for the student to OWN, not assigning them a project.

## Step 1 — Profile intake (one bundled question, plain text)
Ask:
1. Which of the six subjects? (If unsure → hand to `/yau-subject-navigator` first.)
2. What specific topics/phenomena genuinely interest you? (the more specific the better)
3. What's your background? (relevant courses, prior projects, programming/lab skills)
4. Constraints: solo or team (1–3)? equipment/lab access? hours/week until the Sep deadline?
5. Do you have a university mentor or only a school teacher? (affects feasibility of lab-heavy work)

## Step 2 — Pull grounding evidence
- Read `references/winning-patterns.md` for the chosen subject.
- Run `scripts/mine_winners.py "<keywords from interests>"` to list real prior titles near the
  student's interest area. Use these to learn the texture — NOT to suggest copying.
- If `site/analysis/data/analysis.json` exists, read it for trend/school signals; if not, skip
  silently.

## Step 3 — Generate candidates (anti-cargo-cult)
Produce 3–5 candidate framings. Each must:
- contain a hook for **one original idea the student could plausibly own** (the doctrine);
- be feasible under the stated constraints;
- NOT be a same-subject clone of an archived winner's method.
Favor: sharpening an under-explored angle; importing a method across subjects; a small but
real new question. For each candidate, write a one-sentence "what would be yours here."

## Step 4 — Score each candidate
Apply `references/scoring-rubric.md` to each. Emit each as a range with confidence and a one-line
binding-constraint note (what most limits this candidate, and the cheapest way to raise it).

## Step 5 — Render (depth-aware, bilingual)
- light: a ranked list of candidates with ranges + one-line rationale each.
- medium: + the per-candidate "what would be yours" + binding constraint.
- heavy: + the prior-art the candidate brushes against (from mine_winners) + a feasibility note
  tied to the student's stated constraints + which judges (ch.4) would care.

## Step 6 — Off-ramp / handoff
If every candidate scores low because the student's interest is saturated or out of reach,
say so honestly and suggest either a different angle or `/yau-subject-navigator`. Otherwise,
hand the chosen topic to `/yau-research-plan-drafter`.
