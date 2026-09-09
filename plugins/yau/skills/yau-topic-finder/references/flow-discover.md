# `discover` flow — topics from a student profile

Goal: help the student explore literature and formulate their OWN candidate questions; evaluate only student-proposed concepts. Do not supply ready-made original topics.

## Step 1 — Profile intake (one bundled question, plain text)
Ask:
1. Which of the six subjects? (If unsure → hand to `/yau-subject-navigator` first.)
2. What specific topics/phenomena genuinely interest you? (the more specific the better)
3. What's your background? (relevant courses, prior projects, programming/lab skills)
4. Constraints: solo or team (1–3)? equipment/lab access? hours/week until the verified deadline for their region?
5. Do you have a university mentor or only a school teacher? (affects feasibility of lab-heavy work)

## Step 2 — Pull grounding evidence
- Read `references/winning-patterns.md` for the chosen subject.
- Run `scripts/mine_winners.py "<keywords from interests>"` to list real prior titles near the
  student's interest area. Use these to learn the texture — NOT to suggest copying.
- If `site/analysis/data/analysis.json` exists, read it for trend/school signals; if not, skip
  silently.

## Step 3 — Literature leads and questions, not AI-authored original topics
Present adjacent research areas and verifiable literature leads from the student's interests.
Ask the student to propose a concrete question, explain why it matters, and identify their own
idea. Do not invent the original hook or write “your contribution is X” for them. Teacher
permission and the official auxiliary-only boundary apply before exploration.

## Step 4 — Evaluate only student-proposed candidates
Once the student provides concrete conceptions, critique feasibility, originality, prior art
and ownership using the coaching rubric. Do not assign originality scores to AI-created ideas.
If no conception is provided, keep the status “student to formulate” and use questions.

## Step 5 — Render the student's ideas with feedback
Report student-provided candidate wording, traceable literature, questions, constraints and
coaching-score ranges if evaluable. The rubric is not an official admission/award prediction.
Keep missing contributions explicit instead of filling them with AI-generated content.

## Step 6 — Off-ramp / handoff
If every candidate scores low because the student's interest is saturated or out of reach,
say so honestly and suggest either a different angle or `/yau-subject-navigator`. Otherwise,
hand the chosen topic to `/yau-research-plan-drafter`.
