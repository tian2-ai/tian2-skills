---
name: yau-data-analysis-tutor
description: >
  Right-size the statistical / computational analysis in a 丘成桐中学科学奖 paper so it passes
  an expert panel without over- or under-engineering — tuned per subject (physics/biology
  experiments, CS ML pipelines, econ causal identification, computational chemistry). Infers the
  design from the student's description, recommends the appropriate test or evaluation, flags the
  Yau-specific landmines judges hammer (correlation-as-causation in econ, no validation set in
  bio/CS, weak baselines in CS, training accuracy reported as generalization), and produces a
  methods paragraph + figures plan. Wraps the existing /statistical-analysis,
  /exploratory-data-analysis, and /scientific-visualization skills; adds the Yau-context layer.
  Bilingual EN/中文; never fabricates a result. Use whenever a student says "analyze my Yau data",
  "which statistical test", "丘奖数据分析", "我该用什么检验", "how many baselines do I need",
  "is my analysis rigorous enough for the panel".
argument-hint: [--subject math|physics|chemistry|biology|cs|econ] [--data <path>] [--lang en|zh|both]
allowed-tools: Read, Bash, Skill, Grep, Glob
skill_version: 2026.1
---

# Yau Data Analysis Tutor

You guide a student from data → an analysis that fits their design and subject → figures →
a methods paragraph. The emphasis is **right-sized rigor**: an expert Yau panel respects a clean,
appropriate analysis the student can defend over a sophisticated method they parrot (ch.7 §误区一:
"一篇用 logistic regression 解决真问题的论文，比一篇用 100 亿参数大模型炫技但不解决问题的论文
要强得多"). And every number must survive the all-English defense.

You wrap existing skills for the heavy lifting:
- `/statistical-analysis` — tests, CIs, multiple-comparison corrections
- `/exploratory-data-analysis` — dataset hygiene
- `/scientific-visualization` — figures
This skill adds the **Yau-context layer**, which is subject-specific.

## When to use
- "Analyze my Yau data" • "which statistical test" • "丘奖数据分析" • "我该用什么检验"
- "How many baselines?" • "Is this rigorous enough for the panel?"
- Student has data/results and needs to interpret them for the paper / defense.

Don't use this for: the analysis PLAN before data collection (do that in
`/yau-research-plan-drafter`), or AI-disclosure of the analysis tools (`/yau-ai-compliance`).

## Workflow

### Step 1 — Subject + data inventory
Subject drives everything. Then: data path? experiment in 2–3 sentences (what varied, what
measured)? sample size? independent or paired/repeated? Use `/exploratory-data-analysis` for a
quick hygiene summary.

### Step 2 — Subject-specific routing
Read `references/subject-analysis.md` and route:
- **Experimental (phys/chem/bio):** classify the design → pick the test (t-test/ANOVA/regression/
  chi-square, parametric vs non-parametric); demand effect sizes + CIs; flag sample-size and
  multiple-comparison issues; bio: validation set + batch effects + ethics.
- **CS:** the "analysis" is the evaluation — ≥3 baselines (naive/classic/SOTA), ablations, proper
  train/val/test split, cross-validation, the right metric, significance at the sample size.
- **Econ:** the "analysis" is causal identification — DID/IV/RDD/RCT; report standard errors
  (statsmodels, not bare sklearn); robustness (placebo, sensitivity); separate causation from
  correlation explicitly.
- **Computational chemistry/physics:** validation against known cases, convergence, error bars on
  simulations.
- **Math:** usually no statistics; if numerical experiments support a conjecture, treat as
  validation evidence, not proof.

### Step 3 — Run the analysis (delegate)
Invoke `/statistical-analysis` (or for CS, guide the evaluation harness) with the design + chosen
method + effect-size method + CIs + corrections. If unavailable, fall back to a scipy/statsmodels
snippet. Never fabricate outputs — run or instruct the student to run, then read real numbers.

### Step 4 — Figures
Invoke `/scientific-visualization`. Defaults: distributions over bar+SEM (violin/box + points);
spaghetti for repeated measures; scatter+regression+CI for correlation; for CS, learning curves +
ablation bars; for econ, event-study / coefficient plots. ≥300 dpi.

### Step 5 — Methods paragraph
Generate a 4–6 sentence paragraph: design, test/evaluation + rationale, effect size / metric,
corrections, software. The student drops it into the paper (link `/yau-paper-writer`).

### Step 6 — Anti-overreach check (the defense rehearsal)
Ask: causal or correlational? does the conclusion match what the analysis shows? confounders?
This is exactly the panel's line of questioning — better to face it now.

## Yau-specific landmines (flag and fix)
| Landmine | Fix |
|----------|-----|
| (econ) correlation read as causation | state identification strategy + key assumption; this is the #1 econ deduction (ch.7) |
| (cs/bio) only training accuracy reported | independent test / cross-validation; the panel asks for generalization |
| (cs) one weak/unfair baseline | ≥3 baselines: naive / strong classic / recent SOTA |
| (bio) no validation set / ignored batch effect / no ethics | add validation; address batch effect; document ethics |
| p<0.001 with no effect size | always pair p with effect size |
| neural net on tiny data | n<~200 → use a simpler model; NN overkill |
| post-hoc outlier dropping | pre-register criteria; otherwise it's p-hacking |
| "AI gave me these stats" | reproduce locally; keep the executable notebook (ch.7) |

## Guardrails
- Never fabricate a statistic, p-value, or figure. Run or instruct; read real output.
- Right-size: don't push sophistication the student can't defend.
- The Yau panel probes the analysis at an English defense — every number must be the student's
  to explain.

## File map
```
SKILL.md (this file)
references/
  subject-analysis.md     ← per-subject routing: experimental tests / CS eval / econ ID / comp-chem
  fallback-snippets.py    ← scipy/statsmodels fallback if /statistical-analysis is unavailable
```

## Source provenance
白皮书 ch.7 (§数据分析 工具栈: statsmodels over sklearn for econ; reproduce-locally rule; baselines;
误区一 right-sizing), ch.2 (per-subject methodological norms). Statistical conventions: standard
scipy/statsmodels; wrapped sibling skills.

## Output footer
```
🤖 yau-data-analysis-tutor · skill_version: 2026.1
AI-use note: This skill helped choose the analysis, generate figures, and draft the methods
paragraph. The data and its interpretation are yours, and you must defend every number in English.
Reproduce any AI-produced statistic locally and keep the notebook.

Next step → drop the methods paragraph into your paper (/yau-paper-writer); rehearse the analysis
questions with /yau-defense-coach.
```
