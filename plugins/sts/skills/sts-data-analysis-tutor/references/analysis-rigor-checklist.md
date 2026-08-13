# Analysis-Rigor Checklist (STS Scientific Analysis)

This is the embedded knowledge for `sts-data-analysis-tutor`. It covers (1) test selection by
design, (2) the assumptions to check and the fallback when they fail, (3) cross-validation /
benchmark patterns for the headline claim, and (4) the error/limitations inventory. Everything is
drawn from `rubric.json` (Scientific Analysis), the Task 4 contribution box (e) + Q14 limitations,
and the verified OTT winner analysis (`STS_Top400_Winning_Criteria.md`).

The teaching frame: rigor is NOT a flashier method. Rigor is choosing a test that is valid for
your data, checking that it actually is, confirming your headline number a second independent way,
and being honest about what could be wrong. The student RUNS everything below and must be able to
explain every step (Ethics Statement). This skill advises and critiques; it does not produce
numbers, p-values, figures, or run hidden analyses.

---

## 1. Test selection by design

Classify the design from the student's own description, then name the default test AND its
non-parametric / small-sample fallback. Always pair the test with an effect size + a 95% CI, not a
bare p-value.

| Design | Example | Default test | Fallback if assumptions fail | Effect size |
|---|---|---|---|---|
| One group vs a known/reference value | "is mean shift different from 0?" | one-sample t-test | Wilcoxon signed-rank | Cohen's d |
| Two independent groups | "treatment vs control, different units" | independent t-test | Mann-Whitney U | Cohen's d |
| Two paired measurements | "before vs after on the same unit" | paired t-test | Wilcoxon signed-rank | Cohen's d (paired) |
| 3+ independent groups | "3 concentrations, different samples" | one-way ANOVA + post-hoc (Tukey) | Kruskal-Wallis + Dunn | eta-squared / omega-squared |
| 3+ paired conditions | "same unit, 4 time points" | repeated-measures ANOVA | Friedman | eta-squared |
| Two continuous variables | "rate vs temperature" | linear regression / Pearson r | Spearman rho (monotonic, non-normal) | r-squared |
| Categorical x categorical | "success/fail by group" | chi-square | Fisher's exact (small/sparse cells) | Cramer's V |
| Model / method vs a baseline | "my method vs an established tool on N inputs" | paired comparison + CI on the difference | bootstrap CI | mean delta + CI |
| Time series / periodic signal | "is there a period in this signal?" | spectral method (e.g., DFT/FFT) | period-finding for uneven sampling (e.g., Lomb-Scargle) | power / SNR of peak |

If the design does not fit one row cleanly, ask 1-2 more questions before committing. Do not pick
a test the student cannot explain.

---

## 2. Assumption checks (the part that actually scores)

The Scientific Analysis criterion rewards a visible "checked -> found a problem -> switched"
trail. Have the student run the check and report back; never assume the assumption holds.

- Normality (t-tests, ANOVA, linear regression residuals): Shapiro-Wilk per group, or a Q-Q plot.
  If violated -> switch to the non-parametric fallback in the table above.
- Equal variance / homoscedasticity (independent t-test, ANOVA): Levene's or Brown-Forsythe test.
  If violated -> Welch's t-test / Welch ANOVA.
- Independence of observations: a design question, not a test. If observations are
  paired/clustered/repeated, a between-groups test is the wrong tool -> use the paired/RM row.
- Linearity & residual structure (regression): plot residuals vs fitted; check for curvature or
  heteroscedasticity. Consider a transform or a non-linear model if structure remains.
- Sample size / power: small n makes normality untestable and effect sizes unstable; prefer
  non-parametric tests and state the underpowering honestly.
- Multiple comparisons: running many tests inflates false positives. Correct with
  Benjamini-Hochberg (FDR, preferred) or Bonferroni (conservative); report that you did.

WORKED RIGOR EXAMPLE (real OTT winner): planned a one-way ANOVA, tested normality with
Shapiro-Wilk, FOUND IT VIOLATED, and SWITCHED to Kruskal-Wallis. The act of checking and
switching -- and saying so in the report -- is the signal, not the specific test.

---

## 3. Cross-validation / benchmark of the headline claim (STRONGEST rigor signal)

In the OTT data, the single thing that most separated 18+ winners from the 16.5 floor was
confirming every key claim with a second, independent method. Build one for the student's ONE
headline claim. They run both routes and report whether the two agree, and by how much.

Three patterns (verified from winners):

1. Two methods from different families converging on the same answer.
   - A periodicity found by a DFT/FFT also recovered by Lomb-Scargle (a different period-finding
     method robust to uneven sampling).
   - A transport/scattering result from a transfer-matrix method also obtained from a direct
     ODE solver.
   - Agreement across independent machinery is far stronger evidence than one method run twice.

2. Benchmark a new method against an analytic toy problem with a known closed-form answer.
   - A winner validated their solver on a simplified case with an exact solution and reported the
     error was < 0.1% before trusting it on the full problem. The known answer is the ground
     truth; the small error is the credential.

3. Validate a home-built pipeline against an established tool on a shared input and report the
   agreement (e.g., your reduction pipeline vs a standard package on the same dataset). This is
   the no-lab/computational student's equivalent of a calibration -- it shows the pipeline is
   correct independent of the result it later produces.

Interpreting the outcome:
- Agree -> strong corroboration; state the agreement and the tolerance.
- Disagree -> this is a genuine, scorable finding, NOT something to bury. Investigate why; the
  honest reporting of a discrepancy reads as integrity (the Insight sub-criterion), not weakness.

The deliverable from this skill is a PLAN: "here are two independent routes to your headline
number -- run both and report the agreement." It is never a fabricated agreement.

---

## 4. Error / limitations inventory (name 2-4 concrete; NEVER "None")

"Limitations: None / N/A" is the single biggest avoidable red flag in the OTT data. Every strong
project names 2-4 concrete limitations, each specific to the project and, where possible, paired
with how it bounds the conclusion or what a future direction would address. Pull from these real
categories:

- Measurement / instrument error + propagated uncertainty -- quote the instrument/numerical
  precision and propagate it to the final quantity (don't report more significant figures than the
  error supports).
- Sample size / statistical power -- small n, wide CIs, underpowered comparisons; say so.
- Confounders / uncontrolled variables -- what varied that you could not hold fixed, and which
  direction it could bias the result.
- Model / assumption scope -- where the approximation, idealization, or boundary condition breaks
  down; the regime outside which your conclusion does not hold.
- Generalizability -- the result is established only for the tested range/conditions/dataset; do
  not extrapolate beyond it.
- Data provenance / selection -- public-dataset coverage gaps, missing-data handling, selection
  effects (relevant for Chandra/MODIS-style archival work).

THE NULL RESULT IS A WINNING RESULT. A rigorous null -- "no correlation," "no detectable effect"
-- is a real contribution when framed as shrinking the search space: it tells the field where the
answer is NOT. An honest null beats a forced or p-hacked positive, and judges reward the honesty.
Report what you actually found; do not torture the data into significance.

Future directions: pair the limitations with 1-2 concrete next steps (a larger sample, a tighter
control, the regime to test next). This closes the Scientific Analysis criterion (limitations +
future directions) and feeds the contribution boxes.

---

## Common anti-patterns to flag and fix

| Anti-pattern | Fix |
|---|---|
| "Limitations: None / N/A" | Name 2-4 concrete, project-specific limitations. Biggest avoidable red flag. |
| Bare p-value, no effect size | Always pair p with an effect size + 95% CI. p alone says nothing about magnitude. |
| One method, claimed as proven | Add a second independent method (or analytic benchmark). Convergence is the credential. |
| p = 0.06 called "marginally significant" | At alpha = 0.05 it is non-significant. State it plainly. Don't reach. |
| Forced positive from a null | A rigorous null wins -- frame it as shrinking the search space. |
| Ran ANOVA without checking normality | Check (Shapiro-Wilk/Levene); switch to Kruskal-Wallis/Welch if violated. |
| Dropped outliers post-hoc to fit the story | Pre-state outlier criteria; post-hoc removal is p-hacking. |
| Pipeline never validated | Benchmark against an established tool / analytic case before trusting outputs. |
| More sig figs than the error supports | Propagate uncertainty; report the result to the precision the error allows. |

---

## Routing

- Results, figures, and error analysis INTO the <=20-page paper -> sts-research-report-coach.
- The statistics + the 200-word Q14 limitations answer in Task 4's contribution boxes ->
  sts-contribution-coach.
- The 4-criterion rubric + how Scientific Analysis fits the composite -> sts-judging-criteria.

## Source provenance

- 「STS 四维评分标准（rubric.json）」 -- Scientific Merit -> Scientific Analysis.
- 「Regeneron STS 申请问题全文（2026 届）」 -- Task 4 box (e) analyzing data; Q14 limitations (200w).
- 「STS Top-400 获奖标准分析（2024 届，11 位 OTT 获奖者通读）」 -- cross-validation as strongest signal; ANOVA->Kruskal-Wallis; DFT+Lomb-Scargle; transfer-matrix vs ODE; analytic toy benchmark <0.1%; pipeline validation; rigorous null wins; "Limitations: None" red flag.
- 「STS On-The-Table 选拔机制分析（2024 届）」 -- category/evaluator variance (r approx 0.18).
