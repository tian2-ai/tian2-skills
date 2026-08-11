# 分发改动记录

**源**：`ai-config/skills/mine/`（私有工作副本，持续变动）
**本仓库**：派生产物，由 `sync-from-source.py` 重新生成
**本次**：12 个 skill，7 处改动，涉及 4 个 skill

改动只涉及**可移植性**，不改变任何 skill 的方法论、判据或输出格式。
所有规则都写在 `sync-from-source.py` 里——**没有手工改动**。改不了的会让同步失败，而不是悄悄发布。

---

## 出处标注去本机路径（6 处）

「本文件提取自 X」式的溯源标注。**不是运行时依赖**——被引用的内容早已固化在各 skill 自己的 `references/` 里。换成来源名称后溯源保留，不再依赖任何人的目录布局。

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

### `isef-topic-finder` — `references/winner-patterns.md`

**改前**

```
Patterns mined from `/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output/` (PHYS021 deep-dives + project inventories) and from `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 4 (52k-project trends) and ch. 7 (2025 top-312 keyw
```

**改后**

```
Patterns mined from 「ISEF 获奖作品语料（ISEF-Scrape）」 (PHYS021 deep-dives + project inventories) and from `ISEF-Scrape/ISEF竞赛完全指南-完整版.md` ch. 4 (52k-project trends) and ch. 7 (2025 top-312 keyword analysis).
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

### `isef-topic-finder` — `references/category-map.md`

**改前**

```
**Source:** `/Volumes/Mac-Mini/workspaces/tian2-edu/Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md` (verified extract from official 2026 Rules Book PDF).
```

**改后**

```
**Source:** 「ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）」 (verified extract from official 2026 Rules Book PDF).
```

---

## 删除本机兜底路径（1 处）

路径解析链里那个只在作者机器上成立的候选。环境变量与 `~/` 约定保留，行为对有数据的人完全不变。

### `isef-topic-finder` — `scripts/search_isef_archive.py`

**改前**

```
"/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output",
```

**改后**

```
（已删除；保留 $ISEF_SCRAPE_ROOT 与 ~/ISEF-Scrape/output）
```

---

## 未随分发包发布的内容

| 项 | 原因 |
|---|---|
| `references/development-plan.md` | skill 的内部开发计划，使用者不需要，且含本机路径 |
| `validation/` | 回测数据与报告，属开发资产 |
| ISEF 获奖作品语料 | 抓取产物，体量大且非 skill 内容。设 `ISEF_SCRAPE_ROOT` 自备；缺失时 M4 维度自动停用并标注，不会静默降级 |
| ISEF 官方规则 PDF | 第三方版权材料，不再分发。`references/` 已含逐条提取的要点 |

## 怎么更新

```bash
python3 sync-from-source.py --check   # 先看上游有无增删
python3 sync-from-source.py           # 重新派生并刷新本文件
```

**不要直接改 `plugins/` 下的文件**——下次同步会被覆盖。改动请回到上游，或在 `sync-from-source.py` 里加规则。
