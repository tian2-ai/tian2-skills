# Per-subject paper skeletons

Distilled from 白皮书 ch.3 (科研方法与论文写作) and the texture of winning papers per subject.
The Yau paper is judged first on the page (初赛) then defended; structure carries rigor.

## Math (proof paper)
1. **Problem statement** — the precise question you pose (自己出题). One clean sentence.
2. **Background & notation** — definitions, prior results you build on (cite honestly).
3. **Main results** — state your theorem(s)/proposition(s) formally up front.
4. **Proofs** — complete, step-by-step, all yours and reproducible on a whiteboard.
5. **Examples / special cases / numerics** — illustrate and sanity-check.
6. **Open questions** — what your result opens up (the RFW code from ch.3).
Rigor flags: every lemma must be the student's to defend; no AI-generated proof; cite the
prior results you stand on.

## Experimental (physics / chemistry / biology) — IMRaD
1. **Introduction & motivation** — why this phenomenon/question matters (社会意义 optional).
2. **Background / literature** — what's known, the GAP you target (ch.3 codes SPL/CPL/GAP/RAT).
3. **Methods** — apparatus, materials, controls, independent/dependent variables, sample sizes,
   procedure detailed enough to reproduce; **risk/ethics** for human/animal/hazard work.
4. **Results** — figures with error bars + appropriate statistics (see `/yau-data-analysis-tutor`).
5. **Discussion** — interpretation, mechanism, comparison to literature, confounders.
6. **Conclusion & future work.**
Rigor flags: controls explicit; sample size justified; ethics/data-provenance addressed
(biology panels drill this); no overreach beyond what the design supports.

## Theoretical / numerical (physics, applied math)
1. Problem & motivation → 2. Model & assumptions (state them!) → 3. Derivation / simulation →
4. Validation (limits, conservation laws, known cases) → 5. Limitations & scope → 6. Conclusion.
Rigor flags: dimensional analysis, boundary conditions, why this model not a simpler/harder one.

## Computer Science
1. **Problem & contributions** — what you do, stated as explicit contributions.
2. **Related work** — position against prior work honestly.
3. **Method / architecture** — precise enough to reimplement; design choices justified.
4. **Experiments** — datasets (provenance + license), **baselines (≥3: naive / strong classic /
   recent SOTA)**, ablations, metrics, cross-validation.
5. **Analysis** — mechanistic explanation of results (not "the model learned it"); failure modes.
6. **Limitations & future work.**
Rigor flags: train/val split & distribution; baselines fair; the one independent contribution
beyond calling an API named explicitly.

## Economic & Financial Modeling
1. **Research question** — a sharp causal question.
2. **Data** — source, sample, construction, summary stats.
3. **Identification strategy** — DID / IV / RDD / RCT / structural model; **state the key
   assumption** (exclusion restriction, parallel trends, etc.).
4. **Results** — main estimates with standard errors (statsmodels-style, not bare sklearn).
5. **Robustness** — placebo tests, bandwidth/spec sensitivity, alternative samples.
6. **Discussion** — causal interpretation; explicitly separate causation from correlation.
Rigor flags: the single most common deduction is reading correlation as causation — the
identification section is where the paper is won or lost.

## Format conventions (ch.3, 清华学报 example)
- Numbered hierarchical headings (1, 1.1, 1.1.1); figures/tables/equations numbered in citation
  order. Abstract: 研究目的/方法/结果/结论, concrete with data, no literary flourish.
- The Yau finals are in English; many students draft Chinese then translate — keep the English
  quality high (it signals overall rigor to the panel). See `/yau-paper-writer`.
