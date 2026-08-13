---
name: conrad-market-finance
description: >
  Build the business case for a Conrad Challenge submission - Marketing Strategy (20%) plus
  Finances (10%), together 30% of the score and the half of the competition that science-minded
  teams systematically neglect. Covers customer segmentation and the buyer-versus-payer distinction,
  sourced market sizing, naming real competitors, go-to-market channel choice, unit economics
  (bill of materials to unit cost to price to margin), full cost-to-market budgeting, use-of-funds
  splits, and funding sources. Calibrated to the Conrad Chief Judge's documented leniency on
  Finances, where sound internal logic earns a 4 and unit profit with pricing strategy earns a 5.
  Use whenever a team is working on Innovation Brief questions 6 through 10, or asks about market
  size, TAM, customer segments, competitors, pricing, unit cost, business model, revenue, budget,
  fundraising, "how much should we charge", "商业模式", "市场分析", "成本估算"; or when a draft
  has no numbers in it.
argument-hint: [market|competition|gtm|unit-economics|funding|all] [path] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad Market & Finance

**Marketing Strategy 20% + Finances 10% = 30% of your score** — more than Practicality, more than
Storytelling. Teams from a science background lose most of it by default.

Two facts that should change how a team allocates its December:

1. **Finances is the cheapest scoring block in the competition.** Judges are explicitly told to be
   lenient. Sound internal logic earns 4/5. Most teams score 2.
2. **Marketing is decided by naming things.** Named competitors, named segments, named channels,
   sourced numbers. It is not a writing problem; it is a research problem.

**You do not write their answers.** You teach the frameworks, demand the numbers, and critique
what they produce.

---

## Marketing Strategy (20%) — Q6, Q7, Q8

Sub-criteria: Market Insight · Entry & Adoption · Ecosystem Awareness · Differentiation ·
Engagement Channels (website).

### Q6 Market (300 w)

Four things the question explicitly asks, and teams routinely answer two:

**1. Customers and segments.** Specific, not "everyone who cares about the environment."
Ocean Energy: yacht owners (primary) → shipbuilders (secondary) → charter companies (tertiary) →
defence (adjacent), **each with its own reason to buy.**

**2. What is important to them.** The purchase driver — cost, compliance, image, safety, time.
Different per segment.

**3. Size of the opportunity — with a source and a date.**
Nested sizing reads as sophisticated:
> "$216M smart diving devices within a $12.4B dive tourism industry" (DiveGuard, 2026 finalist)

Sources: industry association reports, government statistics, market-research press releases,
trade press, public company filings. Cite them. An unsourced market size is worth nothing;
a sourced one is worth a sub-criterion.

**4. Is the buyer different from the payer?** ← the question most teams skip entirely.
It is asked explicitly. Examples: hospital procurement buys, insurance pays, nurse uses.
Government buys, taxpayer pays, community uses (P-Bump's B2G model, correctly identified).
School district buys, teacher uses (VisionBridge named institutional buyers separately from
end users).

Naming this distinction is one sentence and it demonstrates real market understanding.

**5. Industry ecosystem.** Who else is in the value chain — suppliers, distributors, regulators,
integrators, standards bodies — and how you enter it.

### Q7 Competition (300 w) — the answer that also decides Innovation

Covered in depth in `/conrad-ip-defensibility`. The short version:

- **Name three real incumbents**, including at least one **commercial product**
- State honestly what each does **better** — stated disadvantages build credibility
- Then earn the differentiation on a **named axis**

> The judge picks the comparison set, not you.

### Q8 Go-To-Market (150 w)

150 words. Make three decisions, don't describe a philosophy:

1. **Who are the first 10 customers?** Named types, ideally named organisations.
2. **Which channel, and why?** Direct sales / distribution / licensing / strategic partnership /
   B2G contract. Pick one primary and justify it in one clause.
3. **What is the wedge?** The specific reason the first customer says yes now.

❌ "We will use social media marketing and raise awareness."
✅ "First customers are the 40 canal authorities already running manual inspection; we enter via
a paid pilot with one, priced below their current annual inspection contract."

---

## Finances (10%) — Q9, Q10

Sub-criteria: Cost Estimation · Revenue Projections (per unit **and** overall) · Funding Strategy ·
Budget Reasonableness · Financial Viability.

### The judge's own scale — quote this to teams

| Score | What earns it |
|---|---|
| 2–3 | Reasonable effort; financials that **add up to totals** and show expected expense categories |
| 4 | **Sound internal logic** — even if actual market costs weren't surveyed |
| 5 | Strong logic, **strong pricing strategy**, and **unit profit** or supporting research/comparison |

> "A terrific team and product should **not** be knocked out of final consideration solely due to
> financial projections — as long as they made an effort with some logic involved."

**Translation: 4/5 is available to any team that computes one unit's cost, one unit's price,
and shows the arithmetic.** This is a few hours of work for ~6–8 points.

### Q9 Business Model (300 w) — build the unit table

The question explicitly asks for "the pricing and costs to deliver **one product or service unit**."
Give a table. Judges are checking arithmetic.

```
UNIT ECONOMICS — one unit
  Bill of materials
    component A            $__
    component B            $__
    component C            $__
  Assembly / labour        $__
  Packaging & shipping     $__
  ─────────────────────────────
  Unit cost                $__
  Price                    $__
  Unit margin              $__   (__%)
```

Rules of thumb worth teaching:
- **Price ≈ 3× cost** for a physical product — the Chief Judge says this outright: "you need room
  between cost and selling price to pay for advertising, distribution or shipping, office, and
  research costs, so see if it's possible to set the price at 3 times the cost."
- If prototype cost and unit cost differ by 10×, **explain the gap.** SUNSYNC went $120 → $1,200
  with no bridge and lost points.
- **Recurring revenue is the single easiest way to look sophisticated**: subscription, consumable,
  maintenance contract, licensing. VORTA put the patent-pending IP in the *capsule*, not the robot —
  a razor/blade model, and a moat, in one decision.

### Q10 Fundraising (150 w)

**1. Full cost to market — not prototype cost.** The classic student error the Chief Judge names:
teams cost "immediate costs, such as organizing themselves or purchasing prototype materials,
and only a few teams investigate the actual costs of full development and deployment."

Include: R&D, tooling, certification/regulatory, initial inventory, marketing, working capital.

**2. Use of funds as a percentage split.** Ocean Energy: $10M → 20% R&D / 40% manufacturing and
materials / 20% pilots / 20% marketing. Instantly readable, instantly credible.

**3. Named plausible sources with a reason for the fit.**
Grants (SBIR/STTR, national innovation funds, foundation grants) · competition prizes ·
accelerators · angel investors · strategic corporate partners · crowdfunding · revenue-first
bootstrapping. Say **why each fits your stage** — that's the Funding Strategy sub-criterion.

### Order-of-magnitude sanity

Greencrete proposed **$5–10 thousand** to commercialise a new cement chemistry. Judges read
order-of-magnitude errors as not understanding the domain.

Rough anchors to sanity-check against: a consumer hardware product to market ≈ $250k–$2M;
a medical device with regulatory approval ≈ $2M–$50M+; a software product ≈ $50k–$500k;
an industrial system pilot ≈ $500k–$5M.

**Never inflate.** Judges are told not to award points for claimed business achievements at all,
and to raise inflated claims dispassionately: *"Do you mean these have already been achieved, and
if so, where and how did you fund the $3M required investment? I am uncertain."*
An inflated claim converts a neutral section into an active credibility problem.

---

## Review checklist

**Marketing**
- [ ] Segments named specifically, each with its own purchase driver
- [ ] Market size stated **with source and date**
- [ ] **Buyer vs payer** explicitly addressed
- [ ] Industry ecosystem described
- [ ] ≥3 real competitors named, including a commercial product
- [ ] What competitors do **better** stated honestly
- [ ] Differentiation on a named axis
- [ ] Go-to-market names first customers, a channel, and a wedge
- [ ] Website demonstrates value and engages customers (Engagement Channels)

**Finances**
- [ ] Unit cost table with a bill of materials
- [ ] Unit price and **unit margin** stated
- [ ] Price/cost ratio leaves room for operating costs
- [ ] Any prototype-to-unit cost gap explained
- [ ] Recurring revenue identified if any
- [ ] **Full** cost to market, not prototype cost
- [ ] Use of funds as a percentage split
- [ ] Funding sources named with fit rationale
- [ ] **All arithmetic actually adds up**
- [ ] No inflated or ambiguous achievement claims

## Epilogue

```
---
conrad-market-finance · rubric_version 2025-26.1
Marketing 20% + Finances 10% = 30%. Finances is scored leniently — 4/5 is reachable
with one unit-economics table. Numbers and sources must be researched by your team.
Next: /conrad-judge-simulator --theme marketing · /conrad-innovation-brief for Q6-Q10.
```
