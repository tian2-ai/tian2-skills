---
name: conrad-integrity-guard
description: >
  Keep a Conrad Challenge team on the right side of the originality, coaching and AI-use rules,
  and maintain the contribution log that makes the team's required self-certification honest.
  Conrad teams self-certify they have not used AI for writing, programming or key innovation;
  coaches may guide but may not create any submitted element or exert excessive influence on the
  concept design; AI used for research must be cited like any other source in the references
  attachment. This skill draws those lines concretely, adjudicates grey cases such as proofreading
  and translation, and produces the per-team contribution log. Use whenever anyone asks what AI
  use is allowed, whether a coach or parent or paid tutor can help with something, "can we use
  ChatGPT for our brief", "is this plagiarism", "how do we cite AI", "what can a mentor do",
  "AI能用吗", "辅导老师能帮我们写吗"; or when setting up a mentoring program; or before any
  submission, as a final compliance check.
argument-hint: [rules|check|log|grey-case "situation"] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, Write, WebFetch, WebSearch, Skill
rubric_version: 2025-26.1
---

# Conrad Integrity Guard

Conrad's authorship rules are stricter than most competitions', and the commercial prep market
routinely operates over the line. This skill exists so a team, coach, or program can be confidently
compliant — and can prove it.

**Read `references/competition-facts.md` §8 for the verbatim rules.**

---

## The three rules

**R1 — Originality.**
> "The team's idea must be original work that has been developed by the team as a group."

**R2 — Coach limits.**
> Coaches "may guide the students but **may not create any of the submitted elements** or provide
> **excessive influence on the concept design**."

**R3 — AI.**
> Rules & Regulations: submissions "may not copy or use other materials — **including artificial
> intelligence (AI) tools** — without properly citing the source," with full scientific citation
> information.
>
> Chief Judge Q&A, more specific: "Student teams **self-certify** that they present original work
> with necessary attributions and **have not used AI for writing, programming, or key innovation**.
> AI must be used only for **partial, original submission writing**." AI used for research
> "should be footnoted as any other source"; judges see a **research attribution page (PDF)**.

---

## The three-way AI distinction — the thing to teach first

| Use | Status | Requirement |
|---|---|---|
| AI **inside your product** | ✅ **Encouraged** | You must explain **how it works**. "Our AI solves X" unexplained is not convincing and is scored down. |
| AI as a **research tool** | ✅ **Allowed** | **Must be cited** in the references PDF, with full citation info |
| AI **writing your brief, code, or key innovation** | ❌ **Prohibited** | You self-certify you did not |

12 of 31 finalists in the 2026 cohort build AI into the product. That is the permitted, rewarded
use. It is categorically different from letting AI write your brief.

---

## Two asymmetries that make non-compliance a bad bet

**1. Scrutiny scales with success.** Chief Judge: *"We examine this more so for teams that show
finalist potential."* A ghost-written brief that fails quietly costs nothing. One that reaches
Houston gets examined.

**2. The Summit is an authenticity test by design.** Power Pitch, live judge Q&A, and an Expo
table where judges walk up and ask about the mechanism. **A team can be coached to the finals and
destroyed at them.**

Space Center Houston may disqualify a team at any point, at sole discretion.

---

## What a coach, parent, or paid mentor may and may not do

| ✅ May do | ❌ May not do |
|---|---|
| Teach the rubric and its 25 sub-criteria | Write or rewrite any submitted text |
| Facilitate the topic-discovery process | Supply the topic, or a shortlist to choose from |
| Enforce gates and standards | Decide which candidate survives |
| Teach business concepts with worked non-Conrad examples | Build the team's financial model |
| Mock-judge and give judge-style comments | Fix the problems those comments identify |
| Introduce the team to a domain expert | Send the expert email on their behalf |
| Ask "what's your evidence for that?" relentlessly | Supply the evidence |
| Run pitch rehearsal and hostile Q&A | Write the pitch script |
| Point out a spelling error | Rewrite the paragraph containing it |
| Teach how to search patents | Run the searches and hand over results |

**The operating rule:**
> **The mentor owns the process and the standard. The student owns every artifact and every decision.**

---

## Grey cases, adjudicated

**"Can a coach proofread?"**
Line-level correction — spelling, a missing article, a broken link — is coaching. **Rewriting a
sentence for impact is creating a submitted element.** Test: *is the mentor typing words that will
appear in the submission?* If yes, stop. Better practice: mark the location and name the problem
("this sentence has two ideas in it"), let the student fix it.

**"English isn't our first language. Can we use translation tools?"**
The rules don't ban translation, but the safest and most defensible practice is: **the student
writes the substance in their strongest language, the student translates, and the translation tool
is disclosed in the references PDF.** Do not let a tool generate English prose from a rough idea —
that is AI writing, not translation. Note that judges score Polish & Consistency and are also told
to be fair across a global field; a slightly imperfect but clearly authentic submission is safer
than a fluent one you can't defend at the Summit.

**"Can we use AI to find sources?"**
Yes — this is explicitly allowed. **Cite it.** Full citation info: tool name, version/model, date,
and the prompt or query if meaningful. Then **read and verify the actual sources yourself** —
never cite a paper an AI mentioned but you haven't opened. That is how fabricated citations get
into student work, and a judge who checks one will find it.

**"Can we use AI to check our grammar?"**
A grammar checker on student-written text is comparable to a spellchecker. An AI that rewrites
paragraphs is not. If the output differs substantially from the input, it wrote it.

**"Can a parent who is an engineer help with the technical design?"**
They can teach, review, and ask questions — the same latitude as any coach. They may not design.
Test: could the student explain and defend the design choice, and say **why** they chose it over
the alternatives, at a Summit Q&A?

**"Can we pay a company to build our prototype?"**
Commercial fabrication services (3D printing, PCB manufacture) are ordinary supply-chain use —
real companies use them. **Paying someone to design or engineer it for you is not.** The line is
between buying manufacturing and buying design.

**"A tutoring company advertises '商业计划书撰写' (business plan writing). Is that allowed?"**
**No.** The Innovation Brief is a submitted element; R2 prohibits a coach creating it. This service
is openly advertised by major providers and is the clearest common violation in the market.
See `../../knowledge-base/04-mentoring-market.md`.

**"We used AI early on and stopped. What now?"**
If AI-generated text remains in the draft, rewrite those sections from scratch in the students'
own words — not by paraphrasing the AI output, but by re-answering the question. Log it. If AI was
used for research, cite it. The self-certification must be true at submission time.

---

## The contribution log

Cheap to maintain, and it is what a defensible program looks like. One per team, updated at each
working session. Store at `teams/<team>/CONTRIBUTION-LOG.md`.

```markdown
# Contribution Log — Team [name] — Season [YYYY-YY]

| Date | Session | Student-produced artifact | Author(s) | Mentor role | AI tools used | Cited in refs PDF? |
|------|---------|---------------------------|-----------|-------------|---------------|--------------------|
| | | | | (questions asked / standards enforced) | | |

## AI tools register
| Tool | Version | Purpose | Sessions | Citation string for references PDF |

## Pre-submission attestation
- [ ] Every submitted artifact has a named student author
- [ ] No mentor or AI wrote text appearing in the submission
- [ ] Every AI tool used in research appears in the references PDF with full citation info
- [ ] Every cited source has been opened and read by a team member
- [ ] The topic was chosen by the students and they can say why they rejected the alternatives
- [ ] Every member can explain the mechanism without notes
- [ ] Team has reviewed and signed this log

Signed: ______________________  Date: __________
```

**Rules for the log:** mentor contributions are recorded as *questions asked* and *standards
enforced* — never as text supplied. The team signs off before submission, which is also how they
earn the self-certification honestly rather than clicking through it.

---

## Pre-submission compliance check

Run this before every submission:

- [ ] All brief text written by team members
- [ ] Video script and website copy written by team members
- [ ] Topic chosen by the team; they can explain why they rejected alternatives
- [ ] References PDF complete, including **all AI tools used in research**
- [ ] Every cited source actually read by a team member — no fabricated citations
- [ ] Any AI *inside the product* is explained, not asserted
- [ ] Coach has created **no** submitted element
- [ ] Contribution log current and signed
- [ ] Every member can answer mechanism, competitor, unit-cost and "why this topic" questions
      without notes → run `/conrad-power-pitch` Q&A bank as the test

---

## When someone asks you to cross the line

Refuse plainly and offer the real alternative:

> "I can't write that — your team self-certifies no AI wrote your submission, and finalists get
> examined. What I can do is tell you exactly what's missing from what you wrote and what a judge
> will ask about it. That's more useful anyway, because you'll have to defend it live in Houston."

No lecture beyond that. Redirect to the useful thing.

## Epilogue

```
---
conrad-integrity-guard · rules verified 2026-07-30 from conrad.spacecenter.org
Rules can change — re-verify each season.
This is guidance, not legal advice. Conrad staff (info@conradchallenge.org) are the authority
on any specific case; when genuinely uncertain, ask them.
```
