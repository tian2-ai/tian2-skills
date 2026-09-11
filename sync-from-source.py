#!/usr/bin/env python3
"""Re-derive the distributable skills from the private working copy.

The working copy in ai-config is the source of truth and keeps changing (it
auto-commits). This repo is a derived artifact: run this after editing a skill
upstream, and it rebuilds the published copy by applying a fixed set of
transformations, then writes a before/after record of every one of them.

    python3 sync-from-source.py            # rebuild + write the changelog
    python3 sync-from-source.py --check    # report drift, change nothing

Two rules keep this honest:
  - Every transformation is declared here, not applied by hand. If a change is
    not expressible as a rule below, it belongs upstream instead.
  - Anything a rule cannot handle is reported, never silently shipped. The
    final scan fails the run if a machine-local path survives.
"""

from __future__ import annotations

import csv
import io
import json
import os
import re
import shutil
import subprocess
import sys

SOURCE = os.path.expanduser("~/ai-config/skills/mine")
HERE = os.path.dirname(os.path.abspath(__file__))

# Which upstream skills go into which plugin.
PLUGINS = {
    "isef": "isef-*",
    "yau": "yau-*",
    "sts": "sts-*",
    "conrad": "conrad-*",
    "humanizer": "edu-humanizer-zh",
}

# Files that exist upstream but must not ship: internal planning, scratch notes.
EXCLUDE_FILES = {"development-plan.md"}
EXCLUDE_DIRS = {"__pycache__", ".git", "validation", "evals"}

MACHINE_PREFIX = "/Volumes/Mac-Mini/workspaces/tian2-edu/"

# Provenance citations: keep the attribution, drop the path that only resolves
# on one machine. These are not runtime reads -- the cited content is already
# baked into each skill's own references/.
PATH_LABELS = {
    "Competitions/isef-research-playbook/05-analysis/compliance-form-decision-tree-2026-05-01.md":
        "ISEF 研究手册 · 合规表格决策树（2026-05-01 版）",
    "Competitions/isef-research-playbook/05-analysis/project-workflow-and-category-map-2026-05-01.md":
        "ISEF 研究手册 · 项目流程与类目图（2026-05-01 版）",
    "ISEF-Research-Topics/.omc/plans/2026-05-25-isef-topic-finder-skill.md":
        "isef-topic-finder 设计方案（2026-05-25 版）",
    "ISEF-Scrape/output/": "ISEF 获奖作品语料（ISEF-Scrape）",
    "ISEF-Scrape/output": "ISEF 获奖作品语料（ISEF-Scrape）",
    # STS：同为溯源标注，被引内容已固化在各 skill 的 references/ 里
    "STS/2024/STS_Top400_Winning_Criteria.md": "STS Top-400 获奖标准分析（2024 届，11 位 OTT 获奖者通读）",
    "STS/2024/OTT_Selection_Analysis.md": "STS On-The-Table 选拔机制分析（2024 届）",
    "STS/2024/On_The_Table_2025.xlsx": "STS On-The-Table 名次表（2025 届）",
    "STS/Regeneron_STS_Application_Questions_2026.txt": "Regeneron STS 申请问题全文（2026 届）",
    "STS/Regeneron_STS_Application_Questions.md": "Regeneron STS 申请问题全文",
    "STS/application_reference.md": "STS 申请参考",
    "STS/scoring_engine.py": "STS 评分引擎（本项目内部实现）",
    "STS/rubric.json": "STS 四维评分标准（rubric.json）",
    # 第三方版权材料：不再分发，改为指明官方来源
    "STS/Official-Rules.pdf": "Regeneron STS 官方规则（请自行从 societyforscience.org 取得）",
}

# Literal lines to drop: machine-specific fallbacks in resolution chains. The
# env var and the ~/ convention above them stay, so behaviour is unchanged for
# anyone who has the data; only the one dead candidate goes.
DROP_LINES = [
    '        "/Volumes/Mac-Mini/workspaces/tian2-edu/ISEF-Scrape/output",\n',
]


# The Yau winners archive ships with the skill, and it carries student, advisor
# and school names for 320 entries. Those names are individually public -- the
# award announces them -- but a redistributable compiled index of them is a
# different artifact from an announcement, and mine_winners.py never reads those
# columns: it prints year, keyword-hit count and paper title only. So they are
# stripped, which costs the skill nothing.
PII_CSV_COLUMNS = {"student", "advisor", "school"}
PII_MD_LINE = re.compile(r"^\s*-\s*(学校 / School|学生 / Students|指导老师 / Advisor):")


def strip_csv_pii(text: str) -> tuple[str, int]:
    """Drop the name-bearing columns.

    Must go through the csv module, not str.split(","): at least one school
    field is a quoted value containing commas ("The International School,
    Bangalore, India"). Splitting naively shifts every later column on that row,
    so the wrong three get dropped and the names survive -- which is exactly the
    failure this function exists to prevent.
    """
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        return text, 0
    drop = {i for i, c in enumerate(rows[0]) if c.strip() in PII_CSV_COLUMNS}
    if not drop:
        return text, 0
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    for r in rows:
        w.writerow([c for i, c in enumerate(r) if i not in drop])
    return buf.getvalue(), len(drop)


def strip_md_pii(text: str) -> tuple[str, int]:
    kept, dropped = [], 0
    for ln in text.splitlines():
        if PII_MD_LINE.match(ln):
            dropped += 1
            continue
        kept.append(ln)
    return "\n".join(kept) + ("\n" if text.endswith("\n") else ""), dropped


def transform(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Return (new_text, [(kind, before_line, after_line)])."""
    out, notes = text, []
    for line in DROP_LINES:
        if line in out:
            notes.append(("删除本机兜底路径", line.strip(), "（已删除；保留 $ISEF_SCRAPE_ROOT 与 ~/ISEF-Scrape/output）"))
            out = out.replace(line, "")
    for rel, label in sorted(PATH_LABELS.items(), key=lambda kv: -len(kv[0])):
        full = MACHINE_PREFIX + rel
        if full in out:
            for ln in out.split("\n"):
                if full in ln:
                    after = ln.replace("`" + full + "`", f"「{label}」").replace(full, f"「{label}」")
                    notes.append(("出处标注去本机路径", ln.strip()[:220], after.strip()[:220]))
            out = out.replace("`" + full + "`", f"「{label}」").replace(full, f"「{label}」")
    return out, notes


def copy_skill(src: str, dst: str) -> list[tuple[str, str, str, str]]:
    """Copy one skill, transforming text files. Returns [(file, kind, before, after)]."""
    changes = []
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in files:
            if name in EXCLUDE_FILES or name.startswith("._") or name == ".DS_Store":
                continue
            s = os.path.join(root, name)
            rel = os.path.relpath(s, src)
            d = os.path.join(dst, rel)
            os.makedirs(os.path.dirname(d), exist_ok=True)
            if name.endswith((".md", ".py", ".sh", ".json", ".txt", ".csv")):
                text = open(s, encoding="utf-8", errors="ignore").read()
                new, notes = transform(text)
                if name.endswith(".csv"):
                    new, n = strip_csv_pii(new)
                    if n:
                        notes.append(("剥离个人信息", f"表头含 {n} 个姓名字段（student/advisor/school）",
                                      "已删除这些列；脚本只用 year/subject/medal/paper_title"))
                elif "winners" in root and name == "README.md":
                    new, n = strip_md_pii(new)
                    if n:
                        notes.append(("剥离个人信息", f"{n} 行「学校 / 学生 / 指导老师」条目",
                                      "已删除；论文标题、年份、奖级、学科保留"))
                with open(d, "w", encoding="utf-8") as fh:
                    fh.write(new)
                changes += [(rel, k, b, a) for k, b, a in notes]
            else:
                shutil.copyfile(s, d)
            os.chmod(d, 0o644)  # this volume writes new files as mode 000
    return changes


def main() -> int:
    check = "--check" in sys.argv
    if not os.path.isdir(SOURCE):
        print(f"source not found: {SOURCE}")
        return 1

    all_changes, counts = [], {}
    for plugin, pattern in PLUGINS.items():
        dst_root = os.path.join(HERE, "plugins", plugin, "skills")
        names = sorted(
            n for n in os.listdir(SOURCE)
            if not n.startswith("._")
            and re.fullmatch(pattern.replace("*", ".*"), n)
            and os.path.isdir(os.path.join(SOURCE, n))
        )
        if check:
            print(f"{plugin}: {len(names)} skills upstream")
            for n in names:
                d = os.path.join(dst_root, n)
                if not os.path.isdir(d):
                    print(f"  NEW upstream, not yet published: {n}")
            for n in sorted(os.listdir(dst_root)) if os.path.isdir(dst_root) else []:
                if not n.startswith("._") and n not in names:
                    print(f"  published but gone upstream: {n}")
            continue
        if os.path.isdir(dst_root):
            shutil.rmtree(dst_root)
        os.makedirs(dst_root, exist_ok=True)
        for n in names:
            for rel, kind, before, after in copy_skill(os.path.join(SOURCE, n), os.path.join(dst_root, n)):
                all_changes.append({"skill": n, "file": rel, "kind": kind, "before": before, "after": after})
        counts[plugin] = len(names)

    if check:
        return 0

    # Nothing machine-local may survive. The changelog is exempt: it quotes the
    # before-state on purpose.
    survivors = subprocess.run(
        ["grep", "-rlE", "/Users/tian|/Volumes/Mac-Mini", os.path.join(HERE, "plugins")],
        capture_output=True, text=True,
    ).stdout.strip()
    if survivors:
        print("FAILED -- machine-local paths survived, add a rule for these:")
        print(survivors)
        return 1

    write_changelog(all_changes, counts)
    print(f"rebuilt {sum(counts.values())} skills, {len(all_changes)} transformations")
    print("changelog -> docs/分发改动记录.md")
    return 0


def write_changelog(changes: list[dict], counts: dict) -> None:
    by_kind: dict[str, list[dict]] = {}
    for c in changes:
        by_kind.setdefault(c["kind"], []).append(c)

    touched = {c["skill"] for c in changes}
    L = [
        "# 分发改动记录", "",
        "**源**：`ai-config/skills/mine/`（私有工作副本，持续变动）",
        "**本仓库**：派生产物，由 `sync-from-source.py` 重新生成",
        f"**本次**：{sum(counts.values())} 个 skill，{len(changes)} 处改动，涉及 {len(touched)} 个 skill", "",
        "改动只涉及**可移植性**，不改变任何 skill 的方法论、判据或输出格式。",
        "所有规则都写在 `sync-from-source.py` 里——**没有手工改动**。改不了的会让同步失败，而不是悄悄发布。", "",
        "---", "",
    ]
    NOTES = {
        "出处标注去本机路径":
            "「本文件提取自 X」式的溯源标注。**不是运行时依赖**——被引用的内容早已固化在各 skill 自己的 "
            "`references/` 里。换成来源名称后溯源保留，不再依赖任何人的目录布局。",
        "删除本机兜底路径":
            "路径解析链里那个只在作者机器上成立的候选。环境变量与 `~/` 约定保留，行为对有数据的人完全不变。",
    }
    for kind, items in by_kind.items():
        L += [f"## {kind}（{len(items)} 处）", "", NOTES.get(kind, ""), ""]
        for c in items:
            L += [f"### `{c['skill']}` — `{c['file']}`", "", "**改前**", "", "```", c["before"], "```", "",
                  "**改后**", "", "```", c["after"], "```", ""]
        L += ["---", ""]

    L += [
        "## 未随分发包发布的内容", "",
        "| 项 | 原因 |", "|---|---|",
        "| `references/development-plan.md` | skill 的内部开发计划，使用者不需要，且含本机路径 |",
        "| `validation/` | 回测数据与报告，属开发资产 |",
        "| ISEF 获奖作品语料 | 抓取产物，体量大且非 skill 内容。设 `ISEF_SCRAPE_ROOT` 自备；缺失时 M4 维度自动停用并标注，不会静默降级 |",
        "| ISEF 官方规则 PDF | 第三方版权材料，不再分发。`references/` 已含逐条提取的要点 |", "",
        "## 怎么更新", "",
        "```bash", "python3 sync-from-source.py --check   # 先看上游有无增删",
        "python3 sync-from-source.py           # 重新派生并刷新本文件", "```", "",
        "**不要直接改 `plugins/` 下的文件**——下次同步会被覆盖。改动请回到上游，或在 `sync-from-source.py` 里加规则。", "",
    ]
    with open(os.path.join(HERE, "docs", "分发改动记录.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


if __name__ == "__main__":
    raise SystemExit(main())
