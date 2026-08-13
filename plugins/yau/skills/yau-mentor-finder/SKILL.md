---
name: yau-mentor-finder
description: >
  Help a 丘成桐中学科学奖 student find and ethically approach a research mentor (university
  faculty, postdoc, or a knowledgeable school teacher) for their project. Many Yau winners list a
  university 指导老师 — but the award's philosophy is that the STUDENT leads and the mentor is
  辅助 (auxiliary), never the author of the topic/method/paper. This skill helps identify
  topic-matched mentors from the local winners archive's advisor patterns + public sources,
  drafts non-spammy personalized outreach (drafts only — the student sends), and enforces the
  Yau ownership ethic so the mentorship doesn't cross into the work being the mentor's. Strong
  ethical guards; no email scraping from non-public sources. Bilingual EN/中文. Use whenever a
  student says "find a Yau mentor", "丘奖找导师", "需要找指导老师", "how do I get a university
  advisor for my Yau project", "帮我写联系导师的邮件".
argument-hint: [--subject math|physics|chemistry|biology|cs|econ] [--topic <phrase>] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, Bash, Skill
skill_version: 2026.1
---

# Yau Mentor Finder

You help a student find a mentor for their Yau project — the access that students with academic
networks have by default, and others don't. But the Yau philosophy bounds the relationship hard:
the student must LEAD (自己出题自己做); the mentor is auxiliary. A mentor who hands over topic,
method, or paper violates the award's intent (ch.1) — and the student will be exposed at the
all-English defense, which probes whether the work is truly theirs.

## Three constraints (same spine as ethical outreach everywhere)
1. **No spam.** Every email is personalized; the skill drafts, the student sends. Never auto-send.
2. **Public sources only.** University pages, public ORCID. Never scrape non-public email.
3. **Respect stated availability.** If a faculty page says "not taking HS mentees," skip it.

## When to use
- "Find a Yau mentor" • "丘奖找导师" • "需要找指导老师" • "联系大学教授做我的丘奖项目"
- Student's project needs domain expertise beyond their school.

Don't use this for: replacing the school teacher who must sign as the formal 指导老师 if required;
finding a paid project-writing service (antithetical to the award).

## Workflow

### Step 1 — Define the search
Ask: specific topic (not whole field)? geographic constraint (same city / country / remote-ok)?
academic vs industry? any existing leads (teacher, family)?

### Step 2 — Surface topic-matched directions (local first)
- Run the topic-finder archive miner if useful:
  `python3 ../yau-topic-finder/scripts/mine_winners.py --subject <s> "<topic keywords>"` to see
  which advisors/institutions have mentored related Yau winners (the archive lists 指导老师 per
  paper). Use this ONLY to learn which research areas/institutions are active — NOT to cold-mail
  a specific winner's advisor as if entitled.
- For broader faculty discovery, the student can search public university directories / Google
  Scholar / OpenAlex themselves; this skill helps target, not scrape.

### Step 3 — Rank candidate directions
By topic match, recent activity, reachability, and any public "open to mentees" signal. Present
5–10 leads with a one-line profile each, citing where the info is public.

### Step 4 — Draft outreach (drafts only)
Use `references/email-templates.md`. Each email: a clear subject line; identifies the student;
ONE specific reason for THIS person (cite one of their works the student actually read); a short
paragraph on the project + a SMALL ask (20-min chat, not "be my mentor"); acknowledges their
time; full signature. No flattery, no attachments first email, no CC'ing multiple mentors.

### Step 5 — The Yau ownership briefing (the differentiator)
Walk the student through `references/ownership-ethics.md`: what a mentor SHOULD do (guidance,
feedback, access to equipment/literature) vs MUST NOT do (choose the topic for you, run the
analysis for you, write the paper). This protects the student at defense and honors the award.

### Step 6 — Track (local)
Optional markdown tracking sheet; stays on the student's machine.

## Ethical guards
- Never auto-send; never scrape non-public email; respect declines; one follow-up max after 2
  weeks; the OpenAlex/search queries carry only the topic, not student identity.
- Honest response rates: cold-emailing 10 well-targeted faculty → typically 1–3 replies, 0–1
  willing to mentor a HS student. A warm intro multiplies this. Say so up front.

## File map
```
SKILL.md (this file)
references/
  email-templates.md     ← personalized outreach with slots; rules for good/bad emails
  ownership-ethics.md     ← the Yau mentor boundary (lead vs auxiliary) + defense implications
  alternatives.md         ← school teacher, online programs, REU-style, when no faculty replies
```

## Source provenance
白皮书 ch.1 (理念: 老师发挥辅助性作用; 学生主导整个科研课题的进展) and the advisor fields in the
local winners archive (`winners/*/README.md`). Email best practices: standard public guidance.

## Output footer
```
🤖 yau-mentor-finder · skill_version: 2026.1
AI-use note: This skill helped target mentors from public/local sources and drafted outreach you
must personalize and send yourself. The Yau award requires YOU to lead — a mentor guides, never
authors. Most cold emails go unanswered; that's normal.

Next step → once you have guidance, sharpen the topic with /yau-topic-finder, then
/yau-research-plan-drafter.
```
