# Example — `score` mode, a too-imitative math topic

**Invocation:** `/yau-topic-finder score "Improving the GPY sieve method to get a better bound on prime gaps" --subject math --lang both`

**Student's stated original idea (originality gate):** "I'd tune the GPY sieve constants to push
the bound lower." → not a new idea; an incremental re-run. Gate caps O ≤ 5.

**Evidence (mine_winners.py "GPY sieve prime gaps" --subject math):**
- [2024] The Improvement and Popularization of GPY Sieve Method (优胜)
- [2024] On Chen's Theorem, Goldbach's Conjecture and Applications of Sieve Methods (铜)

Two recent same-subject winners already occupy this exact method. Same-subject cargo-cult →
−2 to O.

**Ownership gate:** student can state the GPY setup but cannot yet reproduce the key analytic
estimate without notes → W capped ~5; flagged as a whiteboard-defense risk (math judges
re-derive lemmas live, ch.7).

**Scores:** O=3, W=5, F=6 (analytic number theory at this depth is hard for HS), S=6, Fit=9.
base = 10·(0.32·3 + 0.26·5 + 0.18·6 + 0.14·6 + 0.10·9) = 10·(0.96+1.30+1.08+0.84+0.90) = 50.8.
Archive speaks clearly → confidence high, h=5.

**Output:** `[46, 56]/100, confidence: high.`
Binding constraint: **Originality** (the method is already a recent winner; you'd be the third).
Pivots that each lift exactly that constraint:
1. Pose a *new* sieve question the prior two skipped (e.g. behavior under a constraint they didn't
   consider) — that becomes your "一点儿原创性的想法."
2. Import the sieve toolkit into an adjacent combinatorial problem (cross-subject-style import,
   which the doctrine rewards).
3. If neither excites you, run `/yau-topic-finder discover --subject math`.

中文摘要：该选题在数学奖近两届已有两篇同方法获奖论文，属同学科套用，原创性受限；且解析估计的
关键引理你目前无法脱稿白板重现，答辩风险高。建议在该方法上提出一个前人未触及的新问题，作为
真正属于你自己的那"一点儿原创性"。
