# Scoring rubric — the math

> 2026-09-09规则优先：先核 `official-rules-2026-09-09.md` 的适用赛区、许可/数据安全、主体本人完成、伦理/机构签章、完整披露和提交要求。下方为学科教学/历史经验，并非新增官方硬门槛；数字评分、训练时长、基线数量、排期建议不代表官方规则。历史获奖医疗/药物题目不是本季许可，纯理论生物研究并不因没有湿实验自动不合格。


Five dimensions, each scored 0–10 by you (the model) from the evidence you gathered, then
weighted into a 0–100 total emitted as a **range with a confidence band**. Never a point score.

## Dimensions and weights

| Code | Dimension | Weight | Anchor for 0 | Anchor for 10 |
|------|-----------|--------|--------------|----------------|
| O | Originality | 0.32 | known method, known data, no new idea | one clearly student-owned idea per the doctrine |
| W | Ownership/defensibility | 0.26 | relies on a method the student can't reproduce | student can derive/defend it end-to-end in English |
| F | Feasibility | 0.18 | needs grad machinery or inaccessible equipment, won't finish | clean bounded scope, finishes before Sep deadline |
| S | Significance | 0.14 | answers nothing anyone asked | genuine question (pure or applied) worth answering |
| Fit | Subject fit | 0.10 | wrong subject panel for the idea | squarely in the chosen subject's norms (ch.4) |

`base = 10*(0.32·O + 0.26·W + 0.18·F + 0.14·S + 0.10·Fit)` → a number in [0,100].

## Caps (apply BEFORE weighting)
- Originality gate failed (student can't name their own idea): **O ≤ 5**.
- Ownership gate failed (can't reproduce/defend the method): **W ≤ 5**.
- Same-subject cargo-cult of a prior winner's method: subtract 2 from O (floor 0).
- Cross-subject import or sharpened under-explored angle: add 1 to O (cap 10).
- Applied-creativity claim with no validation plan ("纸上谈兵"): **S ≤ 6**.

## Turning the base into a range
Pick a half-width `h` from your evidence confidence:
- **high confidence** (archive + whitepaper both speak clearly to this topic): `h = 5`
- **medium** (one source speaks, the other is silent): `h = 9`
- **low** (`mine_winners.py` empty AND whitepaper silent on this niche): `h = 14`

Emit: `[max(0, base−h), min(100, base+h)] / 100, confidence: <band>`.

If confidence is low because sources were silent, SAY SO in plain language — silence is
information, not a reason to guess upward.

## What you must NEVER do
- Never print a single point score.
- Never predict a medal ("this is gold-level"). The panel decides on a defense you can't see.
- Never raise the score to be encouraging. If it's low, show the path up (pivot suggestions,
  or `/yau-subject-navigator`) instead of inflating.

## Worked micro-example
A CS topic = "fine-tune BERT for sentiment on a public dataset," student can't name an original
idea, can explain training but it's a standard pipeline:
O=4 (gate cap 5, then standard pipeline → 4), W=7, F=9, S=5, Fit=9.
base = 10·(0.32·4 + 0.26·7 + 0.18·9 + 0.14·5 + 0.10·9) = 10·(1.28+1.82+1.62+0.70+0.90) = 63.2.
Archive speaks clearly (many CS LLM/ML winners) → high confidence, h=5 →
**[58, 68]/100, confidence: high.** Then: the binding constraint is Originality — suggest a
pivot that adds one student-owned idea (a new evaluation angle, a failure-mode analysis).
