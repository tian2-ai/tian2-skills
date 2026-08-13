# Example — `discover` mode, a CS-leaning student

**Invocation:** `/yau-topic-finder discover --subject cs --lang both`

**Profile intake:**
- Subject: 计算机 (Computer Science)
- Interests: large language models, how they fail, ancient-text/low-resource languages
- Background: Python, PyTorch basics, has fine-tuned a small model once
- Constraints: team of 2, no GPU cluster (Colab only), ~10 hrs/week until Sep
- Mentor: school CS teacher only

**Evidence (mine_winners.py "LLM oracle bone low-resource recognition" --subject cs):**
- [2024] Decoding the Past: Oracle Bone Character Recognition via ViT + GAN restoration (铜)
- [2024] LLM Mathematical Reasoning Grounded with Formal Verification (金)
CS panel (ch.4): graphics/vision/systems professors; AI is the entry ticket; edge = an
independent contribution beyond calling an API.

**Candidates (each with "what would be yours"):**

1. **Failure-mode taxonomy of LLMs on classical Chinese.** Build a small benchmark of where
   LLMs mistranslate 文言文 and *why*. Yours: the new evaluation benchmark + error analysis,
   not a new model. → fits "new benchmark/new explanation" edge. `[60,70]/100, conf: high`.
   Binding constraint: scope discipline (keep the benchmark small and clean).
2. **Cross-import: Poisson-fusion-style seam repair (from graphics) applied to GAN-restored
   oracle-bone glyphs.** Yours: the cross-subject method import. `[55,67]/100, conf: medium`
   (one near-match exists; the import angle is fresh). Constraint: GAN training on Colab is tight.
3. **A retrieval-augmented agent for citation honesty in student essays.** Yours: a verification
   loop. `[50,62]/100, conf: medium`. Constraint: originality competes with a crowded area.

**Recommendation:** Candidate 1 best matches the doctrine (a clearly student-owned benchmark +
analysis, feasible on Colab, defensible in English) and the CS panel's "go beyond the API" taste.

中文：候选一（古文 LLM 失败模式基准 + 误差分析）最契合丘奖理念——基准与分析是真正属于你们
自己的贡献，Colab 即可完成，英文答辩时能讲清楚。下一步用 /yau-research-plan-drafter 把它结构化。
