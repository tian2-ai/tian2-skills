# Topic Fitness Gate — the 5 gates for an STS-fit research question

This is the source of truth for step 4 of the workflow. Run EVERY candidate question through
all five gates. The score is holistic, like the rubric: failing one gate is enough to make a
candidate ineligible or low-merit, so do not average them away. Tie every verdict to *why* it
matters for how STS is judged (Scientific Merit + Student Contribution + Scientific Potential,
each /5, summed to /20). Typical composite is 9–12; the top-15% / OTT bar is ≈ 16. ~19% of
entries reach the internal "On The Table" docket.

---

## Gate 1 — Ownable? (Student Contribution criterion)

**Pass:** the student can do the core work themselves and prove it per-phase. Task 4 forces six
200-word contribution boxes — (a) developing the purpose, (b) designing procedures, (c)
implementing, (d) gathering/recording data, (e) analyzing data, (f) formulating conclusions —
plus a statement of independence (Q20) and a question on independence from any larger project
(Q12, 150w). If you cannot honestly fill those boxes for THIS question, it is not ownable.

**Fail signals:**
- The interesting part was done by the mentor / the lab's existing pipeline and you only ran it.
- You can't articulate which design decisions were yours.
- The question is a slice of a PI's grant with no visible extension of your own.

**Fix:** narrow to the piece you genuinely drive, or extend the larger project with a question
the mentor was not already asking. Bound the mentor's role explicitly; winners' mentors
corroborate specifically ("≈98% is the student's own work").

---

## Gate 2 — Feasible with YOUR access? (Scientific Merit + Initiative)

**Pass:** the method fits your access (lab/RSI/RRI OR home+laptop), your skills (coding/math/
wet-lab), and your time. Initiative is judged *relative to available resources* — a rigorous
home project is not penalized for lacking a lab.

**Fail signals:**
- Needs an instrument, organism, cohort, or compute you cannot reach in the time you have.
- Wet-lab design but no lab and no remote/public substitute.
- Scope balloons past the hours/weeks the student actually has.

### THE NO-LAB PLAYBOOK (cite this whenever access is home-only)
Theory / computational topics where a laptop is the whole instrument can reach the TOP tier.
Two home-based winners and the 19.33-scoring exemplar prove it. The recipe:
- **Public datasets** as your "instrument" — e.g. Chandra (X-ray astronomy), MODIS (remote
  sensing), and other open archives in your field. (Confirm the dataset exists and is
  accessible; do not assert a dataset the student hasn't checked.)
- **A graduate-level method** done well — PDE/ODE modeling, DFT, Monte-Carlo, real inferential
  statistics, simulation. This clears the Scientific Merit floor without hardware.
- **Rigor as the differentiator** — validate your pipeline against a known case, test your
  assumptions, and report nulls honestly. Computational rigor substitutes for lab scale.

So "I have no lab" never fails Gate 2 by itself — it just routes the candidate toward
theory/computational/public-data framings.

---

## Gate 3 — Novel, not just confirmatory? (Scientific Merit + Originality)

**Pass:** the question adds something NEW the field did not already have — a new term/method/
generalization, a cross-domain transfer of an existing method, or a result that meaningfully
extends prior work. Differentiator #2 from the winner analysis: *contribute something new, not
just run an existing tool.*

**Fail signals (flag as LOW MERIT):**
- "Reproduces / confirms a known result" with nothing added — re-deriving textbook physics,
  re-running a standard tool on a standard dataset to get the standard answer.
- A confirmatory result dressed up as a discovery (an observed red flag that costs points).

**Fix — two routes:**
1. **Add a contribution:** introduce a new term/parameter into an existing model, cross-validate
   a claim with a *second independent method* (the single strongest rigor signal,
   Differentiator #1), or extend the method to a domain it hasn't been applied to.
2. **Reframe as a rigorous NULL:** a well-designed null result *wins* when framed as shrinking
   the search space (Differentiator #3). "X does not predict Y, and here is the bound" is a
   contribution; "X predicts Y, as expected" is not.

---

## Gate 4 — Falsifiable / has a result? (Scientific Setup + Analysis)

**Pass:** the question has a clear, statable hypothesis or goal and a definite outcome — a
measured effect, a model that fits or fails, a bound, or a clean null. The rubric rewards a
clear hypothesis/goals, design, controls, and acknowledged limitations.

**Fail signals (flag as INELIGIBLE):**
- A literature review or a research *plan* with no results — STS explicitly rejects these
  (Task 5 / report rules). "I will survey the field" is not a project.
- A question with no outcome that could come out the other way ("explore the relationship
  between..." with no testable prediction).

**Fix:** force a one-sentence falsifiable statement: *"If <X>, then I expect <measurable Y>;
the result will be <new finding | a bounded null>."* If the student can't write that sentence,
the question isn't ready — keep sharpening; don't fabricate a hypothesis for them. Always plan
to name 2–4 real limitations later; "Limitations: None/N/A" is the single biggest avoidable red
flag (route the detail to `sts-data-analysis-tutor` / `sts-contribution-coach`).

---

## Gate 5 — Individual, not team? (Eligibility — hard gate)

**Pass:** this is the student's solo project. STS is INDIVIDUAL: research conducted with **other
high-school students** is ineligible.

**Fail signals (flag as INELIGIBLE, not just low-merit):**
- Done jointly with a classmate / another HS student, even partially.
- A subset of a team project the student wants to "carve out" as theirs.

**Fix:** the student needs a question they can do alone. Past team work must still be *disclosed*
(Task 6 asks for it) but cannot be the entered project. Mentor/PI involvement is allowed and is
not a team violation — that is an independence/attribution question, routed to
`sts-mentor-finder` and `sts-rules-wizard` (COI/payment/AI-use disclosure).

---

## Strong vs. weak STS topics (drawn from the verified winner analysis)

| Candidate framing | Verdict | Why |
|---|---|---|
| "Re-derive the known X-ray luminosity of source S from Chandra data" | **WEAK** | Gate 3 fail — reproduces a known result, adds nothing. |
| "Apply method M (new to this domain) to Chandra data and cross-validate the key claim with an independent method" | **STRONG** | Gate 3 (new transfer) + Differentiator #1 (cross-validation). |
| "Does treatment T affect outcome O? (rigorous, ends in a clean null with a stated bound)" | **STRONG** | Gate 3/4 — a rigorous null that shrinks the search space. |
| "Survey the literature on topic Z" | **INELIGIBLE** | Gate 4 fail — lit review, no result. |
| "Our class's group project on Q, my part" | **INELIGIBLE** | Gate 5 fail — team with other HS students. |
| "Run standard tool U on dataset D to get the expected answer" | **WEAK** | Gate 3 fail — confirmatory; fix by adding a term or a second method. |
| "Build a PDE/Monte-Carlo model of phenomenon P on public data, validate the pipeline against a known case, report where it breaks" | **STRONG (no lab)** | Gates 1–4 + no-lab playbook; laptop is the whole instrument. |
| "Use my mentor's pipeline to produce a result the lab already expected" | **WEAK** | Gate 1 (ownership unclear) + Gate 3 (confirmatory). |

### The reusable upgrade pattern
A confirmatory or thin candidate becomes competitive by adding ONE of:
1. a second independent validation method (cross-validation — strongest signal),
2. a genuinely new term / method / generalization,
3. a reframing as a rigorous null that bounds the search space,
4. a quantified, repeated significance number ("76% less power", "100→10 keV"),
5. a clearly owned and bounded extension of the larger question.

Never apply more than one of these by inventing data or a result. The upgrade is a *direction
for the student's real work*, not a claim this skill manufactures.
