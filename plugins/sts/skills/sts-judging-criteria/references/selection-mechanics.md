# STS Selection Mechanics — the pipeline, the OTT cut, and why scoring has variance

> Verified from 「STS On-The-Table 选拔机制分析（2024 届）」, which
> reconstructs the **463-row "On The Table" docket** from `On_The_Table_2025.xlsx` +
> `On_The_Table_Stats_2025.pdf` for the 2024/25 cycle. These figures are from **one cycle** and
> **carry real variance** — treat them as directional, not a formula that guarantees a result.
> Re-confirm downstream tier names/counts against the current official rules each year.

## The funnel: entries → On The Table → Scholars → Finalists

```
~2,471 entrants            (the full applicant pool, 2024/25 cycle — largest since 1967)
      │   internal selection (the mechanical cut below)
      ▼
   463 "On The Table" (OTT)   ≈ 19% of entries — an internal docket, NOT a public tier
      │
      ▼
  ~300 Scholars               (public tier; confirm per year)
      │
      ▼
   40 Finalists               (Finals Week in Washington, DC; confirm per year)
```

- **"On The Table" (OTT)** is the Society's **internal** shortlist/docket of 463 projects — the set
  pulled forward for closer review. It is not a publicly announced tier; the public tiers are the
  ~300 Scholars and the 40 Finalists.
- ~19% reaching OTT is the first and biggest filter. Everything downstream (Scholars, Finalists) is
  selected from within (and around) this pool plus the Society's full deliberation.

## The OTT cut is mechanical — a UNION of two lenses

A project is On The Table if it lands in **EITHER** top list:

> **OTT = (Top 400 by Z-score) ∪ (Top 350 by raw average score)**
> i.e. `rank_by_Z ≤ 400` **OR** `rank_by_raw ≤ 350` → On The Table.

Reconstructed group breakdown of the 463 (official counts in parentheses):

| Group | Definition | Count |
|---|---|---:|
| Top by **both** Z and raw | in both lists | 219 (220) |
| **Z-only** | Top 400 by Z, not top 350 raw | 127 |
| **raw-only** | Top 350 raw, not top 400 Z | 85 |
| Outliers / ties at sentinel | edge cases | 32 (31) |

The ±1 discrepancies are ties at the `9999` not-scored sentinel (see below). The rule reconstructs
the official counts within ±1.

### Cutoff thresholds (this cycle)
- **Raw score at rank 350 ≈ 16.375 / 20.** (Above this raw average → in via the raw lens.)
- **Z-score at rank 400 ≈ 0.74.** (Above this Z → in via the Z lens.)

### Raw-score distribution of the scored OTT tier
min **12.67** · median **16.75** · mean **16.68** · max **19.75** · sd **1.12**. The whole docket is
compressed into a ~3-point band (~15.2 at the 10th percentile to ~18.1 at the 90th), so **small
scoring differences move you dozens of ranks.**

## The key insight: the two lenses barely agree (r ≈ 0.18)

> **Correlation between rank-by-Z and rank-by-raw: r ≈ 0.18** (n = 463) — nearly independent.

A project can be #50 on one lens and #380 on the other. This is the single most important finding:
- A project's standing depends heavily on **which lens** and **which category/evaluator pool** it is
  measured against. Scoring carries **large contextual / panel variance**, not just "quality."
- The **Z-only group (127, ~27% of OTT)** got in purely because their Z was high — they scored well
  *relative to a harshly-graded category or evaluator panel*, even though their absolute raw score
  wasn't top-350. The **raw-only group (85)** is the reverse.
- The union is a **deliberate hedge**: if the Society used raw alone, 127 projects would be dropped;
  if Z alone, 85 would be dropped. Using both neutralizes evaluator severity and category difficulty.

**What this means for the student:** you cannot reverse-engineer a guaranteed-safe number. Two
near-identical-quality projects can land on opposite sides of the cut depending on category and
panel. Control what you can (the rubric inputs), and treat the outcome as probabilistic.

## Category normalization: the raw bar is NOT the same for everyone

Evaluators in different fields grade harder or softer, so raw score is **not comparable across
categories** — which is exactly why Z exists and why both lenses are used.

| Category | OTT n | Mean raw | Mean Z |
|---|---:|---:|---:|
| Chemistry | 21 | **17.67** | +0.87 |
| Physics | 24 | 17.43 | +0.90 |
| Biochemistry | 13 | 17.44 | +0.83 |
| Medicine & Health | 64 | 17.25 | +0.81 |
| … | | | |
| Social Sciences | 10 | 15.83 | +0.87 |
| **Behavioral Sciences** | 37 | **15.50** | **+1.15** |

Note the inversion: **Behavioral Sciences has the lowest raw mean (15.50) but the highest mean Z
(+1.15).** A 16.5 in a hard-graded category can be *more* selective than a 16.5 in a soft-graded
one. **You are scored relative to your category pool** — choosing a category (Task 4) does not change
your prize eligibility, only the expertise of who reads you and the pool you're normalized against.

## Integrity reality: a high score does not guarantee survival

- **23 of the 463 OTT rows carry a `9999` "not-scored" sentinel** — they ranked in by score but were
  **parked pending screening** (Team/Secondary HS involvement, iThenticate plagiarism, parent COI,
  AI-content concerns).
- **A high score does NOT guarantee surviving the integrity / eligibility screens**, which run
  *after* scoring. Disclose honestly (COI, payments, AI use), keep the project individual, and cite
  every image/figure — the screens can drop or park an otherwise top-scoring project. Compliance
  depth → `/sts-rules-wizard`.
- **Gender is near-even** on the table (~51% M / ~47% F), roughly tracking the entrant pool — not a
  visible selection lever.

## Calibration gradient (what separates score bands)

| Exemplar | Composite | Why |
|---|---:|---|
| High | **19.33** | Real, large dataset + applied ML + clear impact (e.g., crop-yield prediction from MODIS) |
| Mid | **~12.5** | Solid, incremental (e.g., improving a medical screen's predictive value) |
| Low | **~4.67–6** | Thin method, weak novelty |

The gradient is **ambition × rigor × demonstrated personal contribution × impact** — not topic
glamour. (For HOW to climb this gradient — the FLOOR × DIFFERENTIATORS model and the six moves — use
`/sts-top400-playbook`, not this skill.)

## Hard limits of these numbers

- Selection groups were reconstructed from the rule `rank_by_Z ≤ 400 ∪ rank_by_raw ≤ 350`; they
  match official counts within ±1 (sentinel ties).
- Category/school/geography stats are over all 463 rows; the correlation is over the 463 rank pairs.
- **Non-OTT projects have no numeric scores in this dataset**, so this is the *selected* tier's
  internal structure — not a full driver model over all ~2,471 entrants.
- All figures are **one cycle's** docket and **carry variance**. They do not predict an individual
  student's score or outcome, and cutoffs shift year to year.

## Source

- 「STS On-The-Table 选拔机制分析（2024 届）」 — OTT union rule,
  cutoffs, r≈0.18, distribution, category normalization, 9999 sentinel, gender, calibration gradient.
- 「STS On-The-Table 名次表（2025 届）」 +
  `On_The_Table_Stats_2025.pdf` — the underlying 463-row score data.
- 「STS 四维评分标准（rubric.json）」 — the 4-criterion scoring the ranks are built from.
