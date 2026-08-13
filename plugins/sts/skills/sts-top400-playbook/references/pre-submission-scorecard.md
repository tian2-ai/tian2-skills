# Pre-submission scorecard — the ~12 checks before you submit

A final self-diagnosis the student runs before submitting. Mark each line **PASS / AT-RISK / GAP**
and route any non-PASS to the named sibling. This is a strategic gut-check, NOT the formal rubric
scoring — for evidence-based per-criterion numbers and a composite/percentile estimate, run
`/sts-evaluator`. For how scoring and selection work, see `/sts-judging-criteria`.

The first four checks are the FLOOR (one per 25% criterion). The next five are the
DIFFERENTIATORS. The last three are RED-FLAG / compliance gates that can quietly cost points or
even disqualify. Grounded in rubric.json and the winner pattern analysis (see SKILL.md provenance).

## FLOOR — all four must be PASS (the composite is a sum; the weakest caps it)

1. **Entry Form floor.** Strong academic record relative to opportunity (transcript rigor, honors,
   and — if shared — test scores) AND at least one founded or sustained-leadership activity.
   → non-PASS: strengthen the activities/awards narrative; route via `/sts-application-navigator`.

2. **Scientific Merit floor.** The method is genuinely graduate-level (not a science-fair demo),
   executed at 4–5/5 sophistication, on a real question that produced RESULTS (a review or a plan
   without results is ineligible). → non-PASS: `/sts-data-analysis-tutor`, `/sts-research-report-coach`.

3. **Student Contribution floor.** The student did the core intellectual work AND a mentor can
   corroborate it specifically; the mentor's role is bounded and stated across the six Task 4
   contribution boxes. → non-PASS: `/sts-contribution-coach`, `/sts-mentor-finder`.

4. **Scientific Potential floor.** There is a one-sentence accessible layperson hook AND a
   distinctive, specific identity essay (not a template). → non-PASS: `/sts-essay-coach`.

## DIFFERENTIATORS — aim for at least 2–3 PASS (this is what moves 16.5 → 18+)

5. **Cross-validation.** Every key claim is checked by a second independent method.
   → `/sts-data-analysis-tutor`.

6. **Something NEW.** The project contributes a new term, method, or generalization — not just a
   tool run unchanged. → `/sts-research-report-coach`, `/sts-contribution-coach`.

7. **Honest null framed as progress.** Any null result is framed as shrinking the search space, not
   as failure. → `/sts-data-analysis-tutor`.

8. **External stamp.** There is (or is in progress) a publication / first-authorship / top fair /
   olympiad / preprint, disclosed in Task 6/16. → `/sts-application-navigator`.

9. **Owned/quantified.** The student visibly owned or extended the question, and the significance is
   quantified and repeated as a number in the abstract, the layperson summary, and the conclusions.
   → `/sts-contribution-coach`, `/sts-essay-coach`.

## RED-FLAG / COMPLIANCE GATES — any GAP here costs points or risks DQ

10. **Limitations are named.** The report and Task 4 state **2–4 honest limitations** — NOT
    "None / N/A" (the single most common avoidable mistake). Also: no confirmatory result dressed as
    discovery; no thin data behind a big claim; no overclaiming ("revolutionize") before results.
    → `/sts-data-analysis-tutor`, `/sts-contribution-coach`.

11. **Disclosures complete.** AI use (Q15), additional support (Q17), conflicts of interest (Q18),
    payments for research/coaching, and STEM-family disclosure (Task 1) are all answered honestly;
    the Task 10 Ethics Statement (report/responses NOT constructed with AI) can be signed truthfully.
    → `/sts-rules-wizard`.

12. **Format / eligibility clean.** Report ≤20 pages, ≤4MB, not a scanned-image PDF, filename
    `LASTNAME.FIRSTNAME.ZIPCODE`; **every image/chart/graph is cited (including your own)** — a
    missing citation can DISQUALIFY; the project is INDIVIDUAL (no other HS students); required
    approvals (IRB/IACUC/PHBA/etc.) are uploaded; recommendations + transcript are in.
    → `/sts-rules-wizard`, `/sts-research-report-coach`, `/sts-application-navigator`.

## How to read the result

- **Any FLOOR check is GAP** → you are not yet at the cutoff region; fix the floor before anything
  else. The composite is a sum, so a single weak criterion caps it.
- **All four FLOOR checks PASS but <2 DIFFERENTIATORS** → you are likely near the ~16.375 raw cutoff
  (rank ~350) with little margin; selection variance (rank-by-Z vs rank-by-raw correlate only
  r ≈ 0.18) means this is a coin-flip zone. Add differentiators to build margin.
- **All four FLOOR + 2–3 DIFFERENTIATORS + clean red-flag gates** → competitive for OTT. Still no
  guarantee: ~19% of entries reach the docket, 23 of 463 were parked pending integrity screens, and
  structural correlates (elite school, NY/CA, lab access) are real. Maximize the controllables.
- Then run `/sts-evaluator` for an evidence-based per-criterion score and a composite/percentile
  estimate before you submit.
