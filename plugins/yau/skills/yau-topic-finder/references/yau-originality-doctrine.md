# The 丘成桐 Originality Doctrine — and what it does to your topic score

This is the philosophical spine of every Yau skill. It is distilled from 白皮书 ch.1 (理念)
and ch.7 (§为什么需要专门谈丘奖中的 AI 使用), which quote 丘成桐 directly.

## The three load-bearing quotes (verbatim from the whitepaper)

1. **"奥数是出个题目给你做，丘奖是自己出题目自己做。这是一个很重要的能力，做研究总是要自己找题目。"**
   — Olympiads hand you a problem; the Yau award asks you to *pose your own problem and solve it.*
   Finding your own question is itself the skill being judged.

2. **"在现有研究基础上，加上一点儿原创性的想法，就很好。"**
   — On top of existing research, *add one genuinely original idea* — that is already good.
   You do NOT need a field-changing breakthrough. You need one real idea that is yours.

3. **理念 (ch.1):** 创新思维 · 合作精神 · 开阔眼界 · 去标准化. The award was created to break the
   "流水线式" standardized-answer mindset. "打破标准答案的束缚" is explicit in the official intro.

## What this means operationally

- The unit of value is **the original idea**, not the dataset size, the model parameter count,
  or the equipment budget. ch.7 §常见误区 一: "用 AI 越多，论文越现代" is false — "一篇用
  logistic regression 解决真问题的论文，比一篇用 100 亿参数大模型炫技但不解决问题的论文要强得多."
- No percentage safe harbor exists for student contribution. Under the official 2026 AI rules, the student must complete the topic conception, research design, core arguments, experimental verification and academic expression. AI and mentors are auxiliary; a small insight does not license outsourcing the rest. The separate 10% plagiarism threshold is neither an AI-generation allowance nor a minimum ownership percentage.
- Teacher/mentor role is **辅助 (auxiliary)**, not directive. ch.1: students who ask the teacher
  for "课题、实现过程、甚至结果乃至论文" are "极其违背比赛初衷的."

## Scoring consequences (used by scoring-rubric.md)

| Signal | Effect on score |
|--------|-----------------|
| Student can state a one-sentence original idea that is theirs | O (originality) can reach 8–10 |
| Topic is a known method applied to a new-but-obvious dataset, no new idea | O capped ~5 |
| Topic copies a prior Yau winner's method in the same subject | O penalty (cargo-cult, guardrail §4) |
| Idea imported across subjects (e.g. a physics method into econ) | O credit — this is the "开阔眼界" the award prizes |
| Student cannot say what is theirs vs. the mentor's/AI's | W (ownership) capped ~5; surface defense risk |
| Idea is feasible for a strong HS student to *own and defend* | W high |
| "社会意义" present (a real-world problem) | S bonus — but never required; pure-math beauty also wins |

## The defense reality that enforces this

The finals are an **all-English oral defense before international scientists** (ch.1 评审流程;
ch.7 §为什么). Math judges routinely ask students to **rewrite a key proof step on the whiteboard**
(ch.7 §各学科 AI: "几乎所有数学奖金、银奖得主都能在白板上重现自己的关键引理"). A topic the
student cannot defend this way is a topic that cannot win — no matter how good it looks on paper.
This is why Ownership (W) is weighted nearly as high as Originality (O).
