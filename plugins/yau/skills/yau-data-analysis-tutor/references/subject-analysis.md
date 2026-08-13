# Per-subject analysis routing

The "right" analysis depends entirely on the subject. Route here after the data inventory.

## Experimental (physics / chemistry / biology) — choose the test
| Design | Default test (parametric / non-param) |
|--------|----------------------------------------|
| One group vs known value | one-sample t-test / Wilcoxon |
| Two independent groups | independent t-test / Mann-Whitney |
| Two paired groups | paired t-test / Wilcoxon signed-rank |
| 3+ independent groups | one-way ANOVA + Tukey / Kruskal-Wallis |
| 3+ paired conditions | repeated-measures ANOVA / Friedman |
| Two continuous variables | linear regression / Pearson (or Spearman) |
| Categorical × categorical | chi-square / Fisher's exact (small n) |
Always: effect size (Cohen's d, η², r²) + 95% CI. Correct for multiple comparisons (Bonferroni
or Benjamini-Hochberg) if >5 tests. n<10/group → non-parametric, report exact p, be honest about
power. n>1000 → tiny effects significant; report effect size prominently.
**Biology specials:** independent validation set; address batch effect / confounders; ethics for
human/animal data — the panel always asks.

## Computer Science — the analysis IS the evaluation
- **Baselines:** ≥3 — naive (random/linear), strong classic (XGBoost/SVM), recent SOTA. Fair
  comparison (don't pit your big model against a tiny baseline).
- **Splits:** train/val/test stated; same distribution checked; cross-validation for small data.
- **Ablations:** isolate the contribution — show the gain comes from YOUR idea, not tuning.
- **Metric:** appropriate to the task (macro-F1 for imbalance, not raw accuracy); report
  significance at the sample size.
- **Mechanism:** explain WHY (attention maps, feature attribution), not "it learned it."

## Economic & Financial Modeling — the analysis IS causal identification
- **Strategy:** DID / IV / RDD / RCT / structural. State it explicitly.
- **Key assumption:** exclusion restriction (IV), parallel trends (DID), continuity (RDD) — state
  and test it.
- **Tools:** statsmodels / R (standard errors, robust diagnostics) over bare sklearn — the panel
  wants SEs, p-values, robustness, not just predictions.
- **Robustness:** placebo tests, bandwidth/spec sensitivity, alternative samples.
- **Causation ≠ correlation:** the single most common deduction (ch.7). Never present a simple
  regression's correlation as a causal effect.

## Computational chemistry / physics
- Validate simulations against known/limiting cases; show convergence; put error bars on computed
  quantities; state method parameters (functional/basis set, time step, etc.) for reproducibility.

## Mathematics
- Usually no statistics. If numerical experiments motivate a conjecture, frame them as
  *supporting evidence*, never as proof. The proof itself must be complete and the student's.
