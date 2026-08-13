# Scoring rubric, anchors, and calibration — sts-evaluator

A faithful transcription of `rubric.json` (the 4-criterion Regeneron STS evaluation rubric) plus the
calibration bands and OTT mechanics this skill scores against. Score EACH criterion /5 in 0.5
increments, cite specific evidence from the student's own text for every score, then SUM to a
composite /20. The composite is a sum, not a max — a weakness on any one criterion caps the total.

System facts (from rubric.json `evaluation_system`):
- total_points = 20.0; four criteria, each max 5.0, weight 0.25 (equally weighted, 25% each)
- scoring_increments = 0.5; score_range = 1.0–5.0
- typical_composite_range = 9.0–12.0; top_15_percent_threshold = 16.0

Generic anchor ladder (applies to every criterion):
- 5.0 = exceptional / groundbreaking
- 4.0–4.5 = strong
- 3.0–3.5 = adequate
- 2.0–2.5 = limited
- 1.0–1.5 = weak

Criterion→input mapping (mirrors scoring_engine.py `_build_criterion_prompt`):
- C1 Entry Form ← transcript rigor + test scores + honors, Task 8 activities, recommendations (2a–c)
- C2 Scientific Merit ← the research report (Task 5) + Task 4 research description
- C3 Student Contribution ← the six Task 4 contribution boxes (a–f) + independence statement (Q20)
  + limitations (Q14); assess differentiation of student vs mentor work phase by phase
- C4 Overall Scientific Potential ← Task 7 essays + the holistic whole-student trajectory

---

## Criterion 1 — Entry Form (max 5.0, weight 0.25)
*Academic achievement, recommendations, activities/interests.*

### 1a. Academic Achievement
Focus: transcript quality (grades, course rigor); test scores (SAT/ACT/AP/IB) if provided; academic
honors; course selection showing challenge.
- 5.0 — Exceptional record: consistently high grades in rigorous courses, outstanding test scores.
- 4.0–4.5 — Strong: challenging coursework, solid test scores.
- 3.0–3.5 — Good standing, adequate rigor.
- 2.0–2.5 — Average performance, limited rigor.
- 1.0–1.5 — Below average.

### 1b. Recommendations
Focus: quality/depth of educator recs; specificity of examples; insight into character/work
ethic/potential; project advisor/mentor recs.
- 5.0 — Exceptional: specific, compelling evidence of ability and potential.
- 4.0–4.5 — Strong: good examples, positive assessments.
- 3.0–3.5 — Adequate: standard praise.
- 2.0–2.5 — Generic or lukewarm.
- 1.0–1.5 — Weak or concerning.

### 1c. Activities and Interests
Focus: breadth/depth of involvement; leadership and sustained commitment; science competitions/
awards; community engagement; passion beyond academics.
- 5.0 — Exceptional breadth/depth: significant leadership, sustained multi-year commitments,
  national-level achievements.
- 4.0–4.5 — Strong: leadership roles, notable achievements.
- 3.0–3.5 — Good participation, some commitment.
- 2.0–2.5 — Limited or shallow.
- 1.0–1.5 — Minimal engagement.

NOTE: recommendations are confidential — the student usually cannot show them. If absent, score 1a
and 1c on the evidence given and mark 1b "insufficient evidence", do not guess.

---

## Criterion 2 — Scientific Merit (max 5.0, weight 0.25)
*Scientific quality, methodology, and advancement of the project.*

### 2a. Scientific Validity
Focus: sound principles/methodology; advancement of field knowledge; significance of the question;
contribution to understanding; proper terminology/concepts.
- 5.0 — Groundbreaking: significant question, potential for major impact.
- 4.0–4.5 — Solid work advancing field knowledge with a clear contribution.
- 3.0–3.5 — Valid approach, modest contribution.
- 2.0–2.5 — Basic work, limited advancement.
- 1.0–1.5 — Flawed methodology or minimal value.

### 2b. Scientific Setup
Focus: clear hypothesis/question; appropriate design; proper controls/variables; suitable
methodology; adequate sample size / statistical power.
- 5.0 — Exemplary design, sophisticated methodology, excellent controls.
- 4.0–4.5 — Well-designed, appropriate methods and controls.
- 3.0–3.5 — Adequate design, basic controls.
- 2.0–2.5 — Weak design, limited controls or inappropriate methods.
- 1.0–1.5 — Poor setup, fundamental flaws.

### 2c. Scientific Analysis
Focus: appropriate analysis techniques; recognition/discussion of error sources; valid
interpretation; logical conclusions supported by data; acknowledged limitations; future directions.
- 5.0 — Sophisticated analysis, excellent recognition of limitations, well-supported conclusions.
- 4.0–4.5 — Strong analysis, good interpretation, errors acknowledged.
- 3.0–3.5 — Adequate analysis, reasonable conclusions.
- 2.0–2.5 — Limited analysis or overreaching conclusions.
- 1.0–1.5 — Poor analysis or invalid conclusions.

---

## Criterion 3 — Student Contribution (max 5.0, weight 0.25)
*Independent work, initiative, originality, personal contribution.* THE criterion the six Task 4
contribution boxes drive.

### 3a. Student Independence
Focus: clear differentiation between student work and mentor contributions; the student's role in
EACH research phase; autonomy in execution; evidence of independent problem-solving.
- 5.0 — Exceptional: student drives the majority of the research process.
- 4.0–4.5 — Strong: clear student ownership of key components.
- 3.0–3.5 — Moderate: adequate student contribution.
- 2.0–2.5 — Limited: heavy mentor involvement.
- 1.0–1.5 — Minimal contribution or undifferentiated from mentor work.

(Mirrors scoring_engine.py's cross-reference "independence ratio" — the share of the work clearly
attributable to the student across the six phases. Reward an explicit mentor-role bound, e.g.
"my mentor provided lab access; I designed and ran every experiment".)

### 3b. Student Initiative
Focus: resourcefulness; seeking out opportunities/resources; proactive approach; performance
relative to available resources; self-directed learning.
- 5.0 — Exceptional resourcefulness, maximizing limited resources creatively.
- 4.0–4.5 — Strong, proactive problem-solving.
- 3.0–3.5 — Adequate, some self-direction.
- 2.0–2.5 — Limited, primarily reactive.
- 1.0–1.5 — Minimal initiative.

(Resource-context: an under-resourced student doing serious work with a laptop + public datasets can
score high here — judge achievement relative to opportunity.)

### 3c. Student Originality / Creativity
Focus: unique approaches/novel solutions; creative designs/procedures; innovative use of materials/
techniques; original problem formulation; novel applications of existing methods.
- 5.0 — Highly original: innovative approaches or novel discoveries.
- 4.0–4.5 — Creative, clear originality in methods or thinking.
- 3.0–3.5 — Some originality, modest creative elements.
- 2.0–2.5 — Limited; mostly standard approaches.
- 1.0–1.5 — Minimal creativity.

### 3d. Student Insight
Focus: learning from failures/setbacks; deep understanding of context; vision for future
directions; scientific integrity/honesty; reflection on process and outcomes.
- 5.0 — Exceptional: deep reflection, learns from failure, clear vision.
- 4.0–4.5 — Strong insight and understanding, good reflection.
- 3.0–3.5 — Adequate, basic understanding.
- 2.0–2.5 — Limited or superficial.
- 1.0–1.5 — Minimal insight or reflection.

---

## Criterion 4 — Overall Scientific Potential (max 5.0, weight 0.25)
*Holistic potential as a future STEM leader.*

### 4a. Student's Scientific Ability
Focus: analytical/critical thinking; work habits/discipline; mastery of concepts/methods;
communication of scientific ideas; technical skills.
- 5.0 — Exceptional: advanced analytical skills, excellent work quality.
- 4.0–4.5 — Strong abilities, good analytical thinking.
- 3.0–3.5 — Adequate, solid fundamentals.
- 2.0–2.5 — Developing, room for growth.
- 1.0–1.5 — Limited.

### 4b. Student's Promise as a Scientist
Focus: long-term STEM dedication; future leadership potential; trajectory; passion/commitment;
likelihood of a research career; potential for breakthrough contributions.
- 5.0 — Exceptional: future STEM leader (Nobel / Fields Medal / MacArthur Fellow potential).
- 4.0–4.5 — Strong promise, clear trajectory toward significant contributions.
- 3.0–3.5 — Good promise, solid foundation for a STEM career.
- 2.0–2.5 — Moderate, uncertain long-term commitment.
- 1.0–1.5 — Limited promise.

(The accessible layperson hook + a distinctive identity essay are the two strongest signals here.)

---

## Cross-cutting evaluation guidance (from rubric.json `evaluation_guidelines`)
- Holistic review: evaluate the whole student and trajectory, not just the best research.
- Bias awareness: watch for bias from gender, race, SES, school resources, topic familiarity.
- AI detection: flag suspected AI-generated content (generic language, no personal voice,
  inconsistent style) — but still score the application.
- Rules violations: note team-project / prohibited-research / citation / ethics concerns — still
  score (the compliance pass is in `redflag-checklist.md`).
- Resource context: judge achievement relative to available resources.
- Evidence-based: EVERY score must cite specific evidence from the application. This is the rule
  the skill enforces hardest — no evidence, no points.

## Calibration bands (from rubric.json `evaluation_guidelines` + `training_examples`)
- Most applications fall in the **9–12** composite range.
- **Top ~15% threshold ≈ 16.0** (roughly 4+ per criterion) — about 300–400 of 2,000+ entries.
- Exemplars: **High 19.33** (exceptional across all criteria), **Mid ~12.5** (solid, adequate
  independence), **Low ~6.0** (weak in multiple criteria). rubric.json also notes a Low band as
  low as 4.67.

## OTT (On The Table) selection mechanics — for the likelihood read (from /tmp/STS_FACTS.md)
- OTT = the internal docket of **463 of 2,471 (~19%)** projects.
- Rule = **Top 400 by Z-score ∪ Top 350 by raw average score** — a UNION of two lenses.
  (Reconstructed: both 219; Z-only 127; raw-only 85; ~31–32 outliers.)
- Reference cutoffs: raw ≈ **16.375/20** at rank 350; Z ≈ **0.74** at rank 400.
- Scored-OTT raw distribution: min 12.67, median **16.75**, mean **16.68**, max 19.75, sd **1.12**.
- **Variance caveat (always state):** rank-by-raw and rank-by-Z correlate only **r ≈ 0.18** —
  nearly independent. Scoring carries large category/evaluator variance; the union exists to hedge
  it. Treat any estimate as a wide band.
- **Category normalization (always state):** the raw bar differs by field — hard-graded means
  Chemistry 17.67, Physics 17.43, Biochem 17.44; soft-graded Behavioral 15.50, Social 15.83 — yet
  Behavioral had the highest mean Z (+1.15). Z normalizes category/evaluator severity; a student is
  scored relative to their category pool. So translate a raw composite into "competitive in your
  category" rather than an absolute verdict.
- ~23 of 463 carried a "9999" not-scored sentinel = ranked in but parked pending integrity screens
  (plagiarism/iThenticate, COI, AI, team/secondary). A high score does NOT guarantee surviving the
  integrity screens — hence the mandatory compliance pass.
- Downstream public tiers (general knowledge, confirm per year): ~300 Scholars → 40 Finalists.

For the FULL pipeline explanation (no draft to score), route to `/sts-judging-criteria`. For the
action plan on raising a score, route to `/sts-top400-playbook`.
