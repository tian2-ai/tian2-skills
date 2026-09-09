---
name: yau-ai-compliance
description: >
  Guide a 丘成桐中学科学奖 student through the award's OFFICIAL AI-use rules — on 2026-07-08 the
  organizers published《丘成桐中学科学奖 AI 使用规则》(https://www.yau-awards.com/show-86-59.html):
  an allowed list (润色/语法/代码调试/文献检索线索/结构梳理/图表草稿/数据分析辅助), a prohibited
  list (代写论文主体/虚假文献/伪造数据/未声明使用/上传涉密敏感或未授权数据), a mandatory Acknowledgements disclosure
  (工具名称及版本/环节及用途/时间及频率), chat-log submission for review (聊天记录备查), and consequences
  (取消资格并通报). Also covers judge-level practice beyond the letter of the rules: per-subject
  AI etiquette (math's structural suspicion vs CS's "AI is the entry ticket"), the judge Q&A
  landmines, disclosure drafting (Methods + Acknowledgements), and a pre-submission AI-use
  self-check — drawn from the official rules plus 白皮书 ch.7. Bilingual EN/中文. Use whenever a
  student asks "how do I disclose AI in my Yau
  paper", "丘奖能用AI吗", "丘奖AI使用规则", "will the judges ask about my AI use", "AI 披露怎么写",
  or used ChatGPT/Claude/ML in their project and wants to stay credible.
argument-hint: '[--subject math|physics|chemistry|biology|cs|econ] [--lang en|zh|both]'
allowed-tools: Read, Grep, Glob
skill_version: 2026.3
---

# Yau AI Compliance

## 2026-09-09 官方复核（先读）

使用前先读 `references/official-rules-2026-09-09.md`。该基线补齐导师事先许可、人工核验、敏感/未授权数据禁令、完整披露及“其他材料”上传要求；若下方旧摘要/白皮书示例有差异，以该基线和官方原文为准。AIGC检测目标与论文重复率10%规则不可混淆。


You help a Yau student use and disclose AI without forfeiting credibility. The crucial fact:
**since 2026-07-08 the 丘成桐中学科学奖 has an OFFICIAL published AI ruleset** —
《丘成桐中学科学奖 AI 使用规则》(https://www.yau-awards.com/show-86-59.html, verified
2026-09-09). The old "规则真空" framing is obsolete: cite the official rules directly. The
rules in brief:
- **允许 (allowed):** 语言润色 / 语法检查 / 代码调试 / 文献检索线索 / 结构梳理 / 图表草稿 /
  数据分析辅助。
- **前置许可：** 使用前获得指导教师许可；主体选题、研究设计、核心论证、实验验证和学术表达由学生本人完成。
- **人工核验：** 文献真实性、引文对应原意、公式/代码/实验结果正确性、版权与数据泄露风险。
- **禁止 (prohibited):** 代写论文主体 / 生成虚假文献 / 伪造数据 / 未声明的 AI 使用 / 上传涉密、敏感或未授权数据。
- **披露 (disclosure):** 致谢页写明每项使用的**工具名称及版本 / 具体使用环节及用途 / 使用时间及频率**。
- **留痕 (evidence):** 相关AI聊天记录**必须上传报名系统“其他材料”**，其他辅助材料如有一并提交；本地保存不等于已提交。
- **后果 (consequences):** 违规**取消资格并通报**。
Beyond the letter of the rules, the panel still demands originality and rigor — judge-level
etiquette (per-subject, from 白皮书 ch.7) tells you what survives the defense even when it is
technically "allowed."

## When to use
- "Can I use AI for the Yau award?" • "丘奖能用AI吗" • "丘奖AI使用规则"
- "How do I disclose AI in my paper?" • "AI 披露怎么写"
- "Will judges ask about my AI use?" • student used LLM/ML and wants to be safe at defense.

Don't use this for: writing the paper (`/yau-paper-writer`), or analysis method choice
(`/yau-data-analysis-tutor` — though both touch AI). This skill is about NORMS, DISCLOSURE, and
the DEFENSE Q&A.

## Core message (say this up front)
"The Yau award published official AI rules on 2026-07-08
(https://www.yau-awards.com/show-86-59.html). Disclosure is no longer voluntary: you MUST state
tool name and version, specific stage and purpose, dates/times and frequency on the Acknowledgements page, and your chat logs
with AI must be submitted for review — undeclared use is itself a violation and can mean
disqualification with notification. And beyond the rules, at the all-English finals judges WILL
probe what you used and whether you understand it. The death answer is '我用了 GPT-4o 跑了一下.'"

## Workflow

### Step 1 — Subject + language
Per-subject AI etiquette differs sharply. Read `references/yau-ai-norms.md` for the subject.

### Step 2 — Inventory the student's AI use
Ask, by research stage (ch.7's five stages): selection, literature, implementation, data
analysis, writing. For each, record tool/version, specific stage/purpose, dates/times and frequency; check prior teacher permission, manual verification and authorized data handling. Capture
honestly — these map directly onto the official disclosure's complete fields. Also ask whether chat logs still exist for each use: the official rules require chat-log
submission for review (聊天记录备查), so start retaining/exporting them NOW.

### Step 3 — Classify each use
First check against the OFFICIAL lists (show-86-59): anything on the prohibited list (代写论文
主体 / 虚假文献 / 伪造数据 / 未声明使用) requires fact-specific handling. An unsubmitted draft missing a disclosure needs truthful completion before submission; actual prohibited work must stop, be addressed by the student and truthfully documented; already-submitted inaccurate information requires prompt organizer consultation. Neither better wording nor redoing work guarantees that historical violations are erased. Then apply the per-subject etiquette table in
`references/yau-ai-norms.md` for judge-level credibility:
- **Green** (officially allowed + judge-accepted): e.g. Grammarly polish; SymPy verification;
  HuggingFace for CS.
- **Yellow** (allowed with disclosure + understanding): fine-tuning a model; ML data analysis.
- **Red** (rule violation and/or credibility-fatal): LLM-generated math proofs; LLM "reasoning"
  economic mechanisms; AI-written prose the student can't paraphrase.
Flag every Red use and propose the fix.

### Step 4 — Review student-completed disclosure
Use `references/disclosure-templates.md` as a factual worksheet. Ask the student to write their own draft and return missing-field questions and minimal corrections, not two ready-to-paste paragraphs:
- **Acknowledgements** — the OFFICIALLY REQUIRED disclosure: for each use state 工具名称及版本 /
  具体使用环节及用途 / 使用时间及频率 (the rules' complete fields).
- **Methods** — specific disclosure where AI is a substantive method component (model, version,
  hyperparameters, evaluation), plus a citation to the original model/dataset paper.
Use the layered tone: disclose honestly and completely (undeclared use is itself a violation),
emphasize the student's independent contribution, and make sure the disclosure matches the
retained chat logs (they can be checked against each other).

### Step 5 — Rehearse the judge Q&A landmines
Walk the student through `references/judge-qa-landmines.md` — the high-frequency AI questions
from 2023–2025 finals, each with "don't say / recommended direction / trap." Have the student
draft answers for the ones that apply.

### Step 6 — Run the self-check
Walk the 13-item pre-submission self-check in `references/ai-self-check.md` (includes chat-log
retention). Any unchecked item
is a remediation task before submission.

## Guardrails
- **Cite the official rules accurately.** The binding source is《丘成桐中学科学奖 AI 使用规则》
  (2026-07-08, https://www.yau-awards.com/show-86-59.html, verified 2026-09-09). Distinguish
  clearly between what the RULES require (allowed/prohibited lists, complete-field disclosure,
  chat-log submission, disqualification + notification) and judge-level ETIQUETTE beyond the
  rules (per-subject norms from ch.7) — never blur the two, and never invent requirements the
  rules don't state.
- **Never advise hiding AI use.** Undeclared use is now a rule violation on its own, and denial
  that the panel later detects is fatal (ch.7). Never help reconstruct or fabricate chat logs.
- **Never write the disclosure to misrepresent.** It must match what the student actually did.
- Subject-specific: math/econ have Red zones (AI proofs / AI causal reasoning) that no disclosure
  rescues — the fix is to NOT do it that way, not to disclose it prettier.

## File map
```
SKILL.md (this file)
references/
  yau-ai-norms.md            ← the 2026 official AI rules + per-subject green/yellow/red
                                etiquette (ch.7 §各学科差异)
  disclosure-templates.md    ← Acknowledgements + Methods disclosure language (official
                                complete-field requirement)
  judge-qa-landmines.md      ← the 10 high-frequency AI Q&A from finals, with answer frameworks
  ai-self-check.md           ← the 13-item pre-submission AI-use self-check (incl. chat-log
                                retention)
```

## Source provenance
Primary (binding):《丘成桐中学科学奖 AI 使用规则》, published 2026-07-08,
https://www.yau-awards.com/show-86-59.html — verified 2026-09-09.
Secondary (judge-level etiquette): 白皮书 ch.7 (AI 工具在丘成桐中学科学奖中的合理使用) in
full — §为什么需要专门谈, §评委真实态度,
§各学科差异, §工具栈, §披露与诚信, §评委追问沙盘推演, §常见误区, §自查清单. 丘成桐 quotes via
\cite{ytinterview}.

## Output footer
```
🤖 yau-ai-compliance · skill_version: 2026.3
AI-use note: Grounded in the OFFICIAL《丘成桐中学科学奖 AI 使用规则》(2026-07-08,
yau-awards.com/show-86-59.html, verified 2026-09-09): complete-field disclosure on the
Acknowledgements page + chat-log submission for review. Judge-level etiquette from 白皮书 ch.7
supplements — never replaces — the official rules. Disclose
honestly; defend what you understand.

Next step → /yau-defense-coach to rehearse the full English oral defense, AI questions included.
```

## 家族输出契约

本技能的书面交付物遵循家族统一契约：判定词 pass/revise/blocked、证据定位、tian2 三格式
渲染，以及"必须三件套 / 按需菜单"的分类——见
`../yau-submission-reviewer/references/deliverables-catalog.md`（本技能主责的按需交付件
也在该菜单中列明）。
