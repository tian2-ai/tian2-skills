#!/usr/bin/env python3
"""Fallback analysis snippets for yau-data-analysis-tutor.

Use ONLY if /statistical-analysis is unavailable. These are minimal, honest helpers — they run on
the student's REAL data and print real numbers. Never fabricate. Effect sizes + CIs included
because the Yau panel asks for them.

Each function is self-contained; import what you need or copy into a notebook the student keeps
(ch.7 requires a reproducible notebook for any reported statistic).
"""
from __future__ import annotations

import math


def cohens_d(a, b):
    """Cohen's d for two independent samples."""
    import numpy as np
    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    sp = math.sqrt(((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2))
    return (a.mean() - b.mean()) / sp if sp else float("nan")


def two_group(a, b, paired=False, parametric=True):
    """Two-group comparison with effect size. Returns a dict of real results."""
    from scipy import stats
    import numpy as np
    a, b = np.asarray(a, float), np.asarray(b, float)
    if parametric:
        if paired:
            t, p = stats.ttest_rel(a, b)
            test = "paired t-test"
        else:
            t, p = stats.ttest_ind(a, b)
            test = "independent t-test"
        stat = float(t)
    else:
        if paired:
            stat, p = stats.wilcoxon(a, b)
            test = "Wilcoxon signed-rank"
        else:
            stat, p = stats.mannwhitneyu(a, b)
            test = "Mann-Whitney U"
        stat = float(stat)
    return {"test": test, "statistic": stat, "p_value": float(p),
            "cohens_d": cohens_d(a, b), "n_a": len(a), "n_b": len(b)}


def anova(*groups):
    """One-way ANOVA + eta-squared. Pass each group as a sequence."""
    from scipy import stats
    import numpy as np
    groups = [np.asarray(g, float) for g in groups]
    f, p = stats.f_oneway(*groups)
    grand = np.concatenate(groups)
    ss_between = sum(len(g) * (g.mean() - grand.mean()) ** 2 for g in groups)
    ss_total = ((grand - grand.mean()) ** 2).sum()
    eta_sq = ss_between / ss_total if ss_total else float("nan")
    return {"test": "one-way ANOVA", "F": float(f), "p_value": float(p),
            "eta_squared": float(eta_sq), "k_groups": len(groups)}


def correlation(x, y, spearman=False):
    """Pearson (or Spearman) correlation with p-value."""
    from scipy import stats
    if spearman:
        r, p = stats.spearmanr(x, y)
        name = "Spearman"
    else:
        r, p = stats.pearsonr(x, y)
        name = "Pearson"
    return {"test": f"{name} correlation", "r": float(r), "p_value": float(p),
            "r_squared": float(r) ** 2}


def benjamini_hochberg(pvalues, alpha=0.05):
    """BH false-discovery-rate correction. Returns list of (p, significant)."""
    import numpy as np
    p = np.asarray(pvalues, float)
    order = p.argsort()
    ranked = p[order]
    m = len(p)
    thresh = (np.arange(1, m + 1) / m) * alpha
    passed = ranked <= thresh
    cutoff = np.where(passed)[0].max() if passed.any() else -1
    sig = np.zeros(m, bool)
    if cutoff >= 0:
        sig_idx = order[: cutoff + 1]
        sig[sig_idx] = True
    return list(zip(p.tolist(), sig.tolist()))


if __name__ == "__main__":
    # tiny smoke test on synthetic data (NOT real research data)
    demo_a = [5.1, 4.9, 5.3, 5.0, 4.8]
    demo_b = [6.0, 5.8, 6.2, 5.9, 6.1]
    print("two_group demo:", two_group(demo_a, demo_b))
    print("correlation demo:", correlation([1, 2, 3, 4], [2, 4, 6, 8]))
