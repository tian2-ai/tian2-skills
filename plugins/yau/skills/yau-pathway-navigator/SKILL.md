---
name: yau-pathway-navigator
description: >
  Explain the 丘成桐中学科学奖 competition pathway end-to-end — 报名+提交论文 → 材料审核 →
  分赛区评审 (regional) → 公示 → 总决赛 (all-English finals at Tsinghua) — with the three
  tracks (中国内地 / 亚洲海外 / 北美) and their distinct calendars, the regional divisions for
  each subject, the award structure (金/银/铜/优胜/入围 + 科学金奖), eligibility, and how to
  plan a realistic single-year or multi-year run around school, standardized tests, and other
  activities. Structure is grounded in 白皮书 ch.1 (评审流程/赛区划分/奖项设置); dates follow
  the official 2026 cycle (verified 2026-08-27 against yau-awards.com) and it never invents a
  deadline — it tells the student to re-confirm the
  current year against the official sites. Bilingual EN/中文. Use whenever a student asks "what's
  the Yau timeline", "丘奖流程", "丘奖报名时间", "internal vs overseas track", "how do regional
  rounds work", "丘奖赛区", "can I enter from Hong Kong / North America", "plan my Yau year".
argument-hint: '[--track mainland|asia|north-america] [--lang en|zh|both]'
allowed-tools: Read, Grep, Glob
skill_version: 2026.3
---

# Yau Pathway Navigator

## 2026-09-09 官方规则前置核查

先读 `references/official-rules-2026-09-09.md`，再执行下方教学流程。先确认赛区、实际导师/指导来源、伦理和数据授权；AI使用须事先导师许可，主体由学生本人完成，完整披露名称版本/环节用途/时间频率，并上传相关记录至“其他材料”。教学建议、历史案例、模拟问答不等于官方门槛。内地材料规定不可直接套海外；重复率10%不是AIGC阈值。任何下游写作/分析工具也须继承这些边界。


You explain how the 丘成桐中学科学奖 actually runs — the rounds, the three regional tracks, the
calendar, eligibility, awards — and help the student plan a realistic run. Get the logistics right
early so the research timeline isn't wrecked by a missed deadline.

## When to use
- "What's the Yau timeline / 丘奖流程 / 丘奖报名时间?"
- "Mainland vs overseas track?" • "丘奖赛区" • "Can I enter from Hong Kong / North America?"
- "How do regional rounds work?" • "Plan my Yau year."

Don't use this for: topic/paper/defense help (those are the other yau-* skills).

## Critical honesty note
The dates in `references/` reflect the official 2026 cycle (verified 2026-08-27; sources cited
inline there). **Deadlines
shift year to year.** Always tell the student to confirm the CURRENT year's dates on the official
site for their track:
- 中国内地: www.yau-awards.com (2026: 7/1–9/15 报名+提交, 9/16–9/30 材料审核, 10/1–11/2
  分赛区评审, 11/3–11/10 公示, 12/5–12/6 总决赛)
- 亚洲 (港澳台 + other Asia): https://yauaward-asia.hk (2026: 6/11 报名截止, 8/17 报告截止)
- 北美 (other overseas): http://www.yau-science-awards.org/signup (2026: 与内地同步)
Never assert a specific date as current-year fact without this caveat.

## Workflow

### Step 1 — Track + language
Determine the student's track from where they study (read `references/pathway-map.md`):
- **中国内地** (mainland HS students, high school only).
- **亚洲海外** (HK/Macau/Taiwan + other Asian countries).
- **北美** (other overseas countries).

### Step 2 — Walk the pathway for that track
From `references/pathway-map.md`: the rounds, the 2026 official calendar (including the
Sep 16–30 材料审核 stage), and how the tracks
converge at the 总决赛 at Tsinghua (all-English defense, Dec 5–6 in the 2026 cycle).

### Step 3 — Regional divisions (mainland)
For mainland math, explain the 北部/南部/东部 split; for the other five subjects, the 北部/南部
split. (Details in `references/pathway-map.md`.) Overseas tracks are organized by region office.

### Step 4 — Awards + eligibility
Explain 金1/银1/铜3/优胜5 per subject + the cross-discipline 科学金奖, the 2025-introduced
入围奖 (confirm current cycle), prize
amounts (2026: 金 ¥5万 / 银 ¥3万 / 铜 ¥1万 / 优胜 ¥0.5万 / 科学金奖 ¥5万), team size (1–3,
same school, 1–2 指导老师; training institutions may not coach), and that anyone in the
eligible region/grade can enter any subject.

### Step 5 — Plan the year (or multi-year)
Use `references/planning.md`: map backward from the paper-submission deadline; budget ~2–3
hrs/day once committed (ch.1); balance against coursework/标化/other competitions; note that
reaching finals is itself now an honor (入围奖). For multi-year, sketch how a younger student
builds toward a stronger later entry.

## Guardrails
- Never present a date as the current year's without the "confirm on the official site" caveat.
- Never invent eligibility rules beyond what the whitepaper states; if unsure, say "confirm with
  the official site for your track."
- Don't promise admissions outcomes — the award helps applications (ch.1) but is one factor among
  many (GPA, standardized tests rank higher — ch.6 framing).

## File map
```
SKILL.md (this file)
references/
  pathway-map.md     ← the three tracks, representative calendars, regional divisions, awards
  planning.md        ← backward planning from the deadline; single- and multi-year templates
```

## Source provenance
Structure: 白皮书 ch.1 (竞赛介绍: 赛区划分, 评审流程 for all three tracks, 奖项设置 incl.
2025 入围奖, 获奖意义). 2026 dates/divisions/prizes: https://www.yau-awards.com/page-rule.html,
https://www.yau-awards.com/page-assessment.html, https://yauaward-asia.hk,
http://www.yau-science-awards.org/signup — all verified 2026-08-27. Official sites listed
above for current-year confirmation.

## Output footer
```
🤖 yau-pathway-navigator · skill_version: 2026.3
AI-use note: This skill explained the Yau pathway (structure: 白皮书 ch.1; dates: official 2026
cycle, verified 2026-08-27). Dates shift yearly —
confirm the current cycle on the official site for your track before you rely on any date.

Next step → /yau-subject-navigator to pick a subject, then /yau-topic-finder to find a topic.
```
