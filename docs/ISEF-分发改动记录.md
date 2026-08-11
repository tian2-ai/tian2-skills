# ISEF 插件 · 分发改动记录

**源**：`ai-config/skills/mine/isef-*`（私有仓库，本机使用）
**目标**：本仓库 `plugins/isef/skills/`（公开分发）
**日期**：2026-08-11 · **改动 13 处**

所有改动只涉及**可移植性**，不改变任何 skill 的方法论、判据或输出格式。
源仓库保持原样不动——两边现在是有意分叉的，本文件就是分叉点的完整记录。

---

## 一、出处标注去本机路径

这些是「本文件内容提取自 X」式的溯源标注，**不是运行时依赖**——引用的内容早已固化在各 skill 自己的 `references/` 里。
把绝对路径换成来源名称后，溯源信息保留，但不再依赖任何人的目录布局。

共 11 处：

### `isef-abstract-optimizer` — `SKILL.md`

**改前**

```
Word count and one-page rule: `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` Stage 4, citing
```

**改后**

```
Word count and one-page rule: 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 Stage 4, citing
```

### `isef-compliance-walker` — `SKILL.md`

**改前**

```
You guide a student through ISEF's form/approval requirements grounded in the **2026 ISEF Rules Book** and **All-Forms.pdf**. You do not invent rules — every requirement you emit is traceable to a specific section in `re
```

**改后**

```
You guide a student through ISEF's form/approval requirements grounded in the **2026 ISEF Rules Book** and **All-Forms.pdf**. You do not invent rules — every requirement you emit is traceable to a specific section in `re
```

### `isef-poster-designer` — `SKILL.md`

**改前**

```
`/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md` §6.
```

**改后**

```
「ISEF 研究手册 · 合规表格决策树（2026-05-01 版）」 §6.
```

### `isef-research-plan-drafter` — `SKILL.md`

**改前**

```
Section structure extracted from `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` Stage 1, which cites
```

**改后**

```
Section structure extracted from 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 Stage 1, which cites
```

### `isef-topic-finder` — `SKILL.md`

**改前**

```
`/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Research-Topics/.omc/plans/2026-05-25-isef-topic-finder-skill.md`:
```

**改后**

```
「isef-topic-finder 设计方案（2026-05-25 版）」:
```

### `isef-abstract-optimizer` — `references/abstract-rules.md`

**改前**

```
- `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` Stage 4
```

**改后**

```
- 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 Stage 4
```

### `isef-poster-designer` — `references/display-rules.md`

**改前**

```
**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md` §6, citing ISEF 2026 DS-Rules.pdf.
```

**改后**

```
**Source:** 「ISEF 研究手册 · 合规表格决策树（2026-05-01 版）」 §6, citing ISEF 2026 DS-Rules.pdf.
```

### `isef-research-plan-drafter` — `references/plan-structure.md`

**改前**

```
**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` Stage 1, citing ISEF Book.pdf lines 230–267 verbatim.
```

**改后**

```
**Source:** 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 Stage 1, citing ISEF Book.pdf lines 230–267 verbatim.
```

### `isef-topic-finder` — `references/category-map.md`

**改前**

```
**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` (verified extract from official 2026 Rules Book PDF).
```

**改后**

```
**Source:** 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 (verified extract from official 2026 Rules Book PDF).
```

### `isef-topic-finder` — `references/compliance-quickref.md`

**改前**

```
**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md` (verified extract from 2026 Rules Book + All-Forms.pdf + DS-Rules.pdf + Gen
```

**改后**

```
**Source:** 「ISEF 研究手册 · 合规表格决策树（2026-05-01 版）」 (verified extract from 2026 Rules Book + All-Forms.pdf + DS-Rules.pdf + Generative-AI-Use-Table.pdf).
```

### `isef-topic-finder` — `references/winner-patterns.md`

**改前**

```
Patterns mined from `/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output/` (PHYS021 deep-dives + project inventories) and from `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 4 (52k-project trends) and ch. 7 (2025 top-312 keyw
```

**改后**

```
Patterns mined from 「ISEF 获奖作品语料（ISEF-Scrape）」 (PHYS021 deep-dives + project inventories) and from `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 4 (52k-project trends) and ch. 7 (2025 top-312 keyword analysis).
```

---

## 二、删除脚本里的本机兜底路径

脚本原本的候选链是「环境变量 → `~/ISEF-Scrape/output` → 某台机器的绝对路径」。最后一项对别人永远不成立，留着只会泄露目录结构，已删除。

共 1 处：

### `isef-topic-finder` — `scripts/search_isef_archive.py`

**改前**

```
候选路径含 "/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output"
```

**改后**

```
只保留 $ISEF_SCRAPE_ROOT 与 ~/ISEF-Scrape/output
```

---

## 三、新增：语料缺失时的显式护栏（**这是真缺陷，不只是可移植性**）

语料**不随 skill 分发**。原先语料缺失时脚本返回 `status: "unavailable"` 且 `m4_value: 0`，但 SKILL.md 从未要求检查 `status`。

后果：`m4_value: 0` 有两种含义——「查过了，没有相似前作」与「根本没查成」。在没有语料的机器上（也就是除作者外的所有人），后者会被当成前者，**一个未经查重的课题会看起来通过了查重**。已加护栏。

共 1 处：

### `isef-topic-finder` — `SKILL.md`

**改前**

```
SKILL.md 未提及 search_isef_archive 返回的 status 字段；语料缺失时 m4_value=0 会被当作真实的“无前作”信号计入评分
```

**改后**

```
新增告警块：使用 m4 前必须检查 status；unavailable 时不计入 M4、标注 missing_sources、下调置信度
```

---

## 未改动的部分

- 12 个 skill 的方法论、评分口径、输出格式**一字未改**
- `isef-topic-finder` 的 40 个文件中，只动了 2 个（1 处脚本兜底路径、1 处新增护栏）
- 其余 7 个 skill（affiliated-fair-navigator、data-analysis-tutor、interview-prep、judge、
  judging-panel-researcher、mentor-finder、prep-feedback）**完全未改**，原样复制

## 使用者需要自备的东西

| 依赖 | 说明 |
|---|---|
| ISEF 获奖作品语料 | 设 `ISEF_SCRAPE_ROOT` 或放在 `~/ISEF-Scrape/output`。**不提供**——语料是抓取产物，非本 skill 内容。缺失时 M4 维度自动停用并标注 |
| ISEF 官方规则与表格 PDF | 各 skill 的 `references/` 已含逐条提取的要点，但原始 PDF 请自行从 societyforscience.org 取得 |
