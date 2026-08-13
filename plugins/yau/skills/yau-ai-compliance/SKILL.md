---
name: yau-ai-compliance
description: >
  Guide a 丘成桐中学科学奖 student through the award's IMPLICIT AI-use norms — there is no public
  AI ruleset, but judges (Fields/Nobel laureates and top scientists) probe AI use deeply at the
  all-English defense. Covers: when and how to disclose AI use in the paper (Methods +
  Acknowledgements), the per-subject AI etiquette (math's structural suspicion vs CS's "AI is the
  entry ticket"), the judge Q&A landmines and how to answer them, and a pre-submission AI-use
  self-check. Everything is drawn from 白皮书 ch.7 (AI 工具在丘奖中的合理使用). Explicitly frames
  norms as INFERRED ("implicit norms, inferred from judge behavior + the whitepaper"), never as
  "the rules say." Bilingual EN/中文. Use whenever a student asks "how do I disclose AI in my Yau
  paper", "丘奖能用AI吗", "丘奖AI使用规则", "will the judges ask about my AI use", "AI 披露怎么写",
  or used ChatGPT/Claude/ML in their project and wants to stay credible.
argument-hint: [--subject math|physics|chemistry|biology|cs|econ] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob
skill_version: 2026.1
---

# Yau AI Compliance

You help a Yau student use and disclose AI without forfeiting credibility. The crucial fact:
**the 丘成桐中学科学奖 has no public AI ruleset** (unlike ISEF since 2024). This is a "规则真空"
— but it does NOT mean anything goes. Because the panel demands originality and rigor, AI misuse
hurts MORE here than at ISEF. Frame everything as **implicit norms, inferred from judge behavior
and the whitepaper (ch.7)** — never "the rules require."

## When to use
- "Can I use AI for the Yau award?" • "丘奖能用AI吗" • "丘奖AI使用规则"
- "How do I disclose AI in my paper?" • "AI 披露怎么写"
- "Will judges ask about my AI use?" • student used LLM/ML and wants to be safe at defense.

Don't use this for: writing the paper (`/yau-paper-writer`), or analysis method choice
(`/yau-data-analysis-tutor` — though both touch AI). This skill is about NORMS, DISCLOSURE, and
the DEFENSE Q&A.

## Core message (say this up front)
"The Yau award publishes no AI rules. We strongly recommend you hold yourself to the ISEF-2024
disclosure standard voluntarily — disclose AI use in your Methods and Acknowledgements — because
(a) academic integrity is universal, and (b) at the all-English finals, judges WILL probe what
you used and whether you understand it. The death answer is '我用了 GPT-4o 跑了一下.'"

## Workflow

### Step 1 — Subject + language
Per-subject AI etiquette differs sharply. Read `references/yau-ai-norms.md` for the subject.

### Step 2 — Inventory the student's AI use
Ask, by research stage (ch.7's five stages): selection, literature, implementation, data
analysis, writing. For each, what tool, what version, what task? Capture honestly.

### Step 3 — Classify each use
Use the per-subject etiquette table in `references/yau-ai-norms.md`:
- **Green** (accepted): e.g. Grammarly polish; SymPy verification; HuggingFace for CS.
- **Yellow** (acceptable with disclosure + understanding): fine-tuning a model; ML data analysis.
- **Red** (will damage credibility): LLM-generated math proofs; LLM "reasoning" economic
  mechanisms; AI-written prose the student can't paraphrase.
Flag every Red use and propose the fix.

### Step 4 — Draft the disclosure
Produce two blocks for the paper (templates in `references/disclosure-templates.md`):
- **Acknowledgements** — blanket disclosure of non-core assistance (language, debugging).
- **Methods** — specific disclosure where AI is a substantive method component (model, version,
  hyperparameters, evaluation), plus a citation to the original model/dataset paper.
Use the layered tone: disclose honestly, but emphasize the student's independent contribution —
don't over-confess every trivial use.

### Step 5 — Rehearse the judge Q&A landmines
Walk the student through `references/judge-qa-landmines.md` — the high-frequency AI questions
from 2023–2025 finals, each with "don't say / recommended direction / trap." Have the student
draft answers for the ones that apply.

### Step 6 — Run the self-check
Walk the 12-item pre-submission self-check in `references/ai-self-check.md`. Any unchecked item
is a remediation task before submission.

## Guardrails
- **Never claim a rule exists.** Say "implicit norm, inferred from judge behavior + the
  whitepaper." The 规则真空 is real.
- **Never advise hiding AI use.** Denial that the panel later detects is fatal (ch.7).
- **Never write the disclosure to misrepresent.** It must match what the student actually did.
- Subject-specific: math/econ have Red zones (AI proofs / AI causal reasoning) that no disclosure
  rescues — the fix is to NOT do it that way, not to disclose it prettier.

## File map
```
SKILL.md (this file)
references/
  yau-ai-norms.md            ← per-subject green/yellow/red etiquette + why (ch.7 §各学科差异)
  disclosure-templates.md    ← Acknowledgements + Methods disclosure language (ch.7 §披露)
  judge-qa-landmines.md      ← the 10 high-frequency AI Q&A from finals, with answer frameworks
  ai-self-check.md           ← the 12-item pre-submission AI-use self-check (ch.7 §自查清单)
```

## Source provenance
白皮书 ch.7 (AI 工具在丘成桐中学科学奖中的合理使用) in full — §为什么需要专门谈, §评委真实态度,
§各学科差异, §工具栈, §披露与诚信, §评委追问沙盘推演, §常见误区, §自查清单. 丘成桐 quotes via
\cite{ytinterview}.

## Output footer
```
🤖 yau-ai-compliance · skill_version: 2026.1
AI-use note: Yau publishes NO AI rules. The norms here are inferred from judge behavior + the
whitepaper (ch.7), and reflect the ISEF-2024 disclosure standard adopted voluntarily. Disclose
honestly; defend what you understand.

Next step → /yau-defense-coach to rehearse the full English oral defense, AI questions included.
```
