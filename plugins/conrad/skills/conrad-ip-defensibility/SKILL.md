---
name: conrad-ip-defensibility
description: >
  Harden the moat and pass the originality search for a Conrad Challenge innovation - the two
  sub-criteria (Verification and IP Defensibility) that decide the largest single block of the
  score, Innovation at 30%. Runs the same web, commercial-product, patent, and prior-Conrad-entry
  searches that judges are required to run, then converts findings into a defensible differentiation
  argument. Teaches the six real moat types (patent, trade secret, accumulating dataset, exclusive
  relationship, ecosystem lock-in, cost structure) and rejects the naive claims students commonly
  make. Only 3 of 31 recent finalists claimed a patent, so this is about defensibility, not
  patenting. Use whenever someone asks "is our idea original", "has this been done before",
  "should we patent this", "what is our competitive advantage", "how do we protect our innovation",
  "why is our innovation score low", "我们的创新点是什么", "查重"; or when a competitive analysis
  names no real incumbent.
argument-hint: [search|moat|audit] ["innovation description"] [--lang en|zh|both]
allowed-tools: Read, Grep, Glob, WebSearch, WebFetch, Write, Skill
rubric_version: 2025-26.1
---

# Conrad IP & Defensibility

Innovation is **30%** — double any other theme. Two of its five sub-criteria are the ones teams
consistently fail:

- **Verification** — "Has an online search confirmed its uniqueness and ruled out duplicates?"
- **IP Defensibility** — "Can the concept be protected (patent, trade secret, copyright,
  **first mover, contracts, ecosystem capture**) to secure its value?"

The Chief Judge's test, verbatim:

> **"If anyone can copy that application, it's not a strong innovation."**

And the worked example that reframes everything: a **new soda flavour scores 1/5**. The same
flavour, if it **reduces tooth decay**, scores **3–5** — "a worthy and protectable innovation, even
though it's a new application of an existing product."

> **Innovation is not measured by technological sophistication. It is measured by defensible
> differentiation.** SUNSYNC used more advanced hardware than the soda example and scored 2.

---

## Mode 1 — the originality search

Judges are **required** to "perform an online search to verify originality." Run it against
yourself first. This is the highest-value hour in the entire preparation.

### Four search moves — run all four

**1. Search the industry term, not the student phrasing.**
The most common reason a search comes back clean is wrong vocabulary.

| Student phrasing | Industry term |
|---|---|
| sun-following solar panel | single-axis solar tracker |
| pet toilet | automatic pet waste disposal system |
| road that makes electricity | piezoelectric energy harvesting pavement |
| smart beehive | precision apiculture / hive monitoring |

Ask: *what would a salesperson in this industry call it?* Then search that.
Find the term via: industry association sites, trade publications, patent classification codes,
the "related searches" of a first attempt.

**2. Search commercial products, not just papers.**
Amazon, Alibaba, Crunchbase, Product Hunt, trade press, industry directories.

> **This is the Puppy WC failure.** That team scored **1 on Innovation** because automatic
> self-cleaning flushing pet toilets are an existing consumer product category, and their brief
> positioned only against puppy pads and mats. A paper search would have come back clean.
> A product search would not.

**3. Search patents.** Google Patents, Espacenet, USPTO. Search the *mechanism*, not the name.
- A near-identical **granted** patent → kill or pivot.
- An **adjacent** patent → a gift. It proves the field is commercially real *and* hands you the
  claim language you should be using in Q4.
- Read the "cited by" and "similar documents" lists — this is the fastest map of a field.

**4. Search prior Conrad entries.** `../../knowledge-base/data/winners.jsonl` plus the published
finalist pages. A close match from a recent year is a strong negative — the judges have seen it.

### Interpreting the result

| Finding | Verdict | Action |
|---|---|---|
| Nothing similar at all | ⚠️ **Suspicious** | Almost always wrong search terms — or there's a reason nobody does it. Search harder before celebrating. |
| Similar exists, differs on a **named axis** | ✅ **Ideal** — the finalist position | Name it in Q7, defend the delta in Q4 |
| Differs only in degree | 🟡 Salvageable | Only if the degree is large and quantified (Clarity: 40× cheaper) |
| Identical product on the market | ❌ Kill or pivot | Find an unserved segment of that market |

**Everything you find is reusable** — it populates Q7 (Competition), Q4 (what's new), and the
references PDF. No search effort is wasted.

---

## Mode 2 — the moat

### The reality check

**Of 31 finalists in the 2026 cohort, only 3 claimed a patent** (one granted — Soaring Seeds'
utility model; two pending — VORTA, DeepTrust). The rubric itself lists **first mover, contracts,
ecosystem capture** alongside patents.

**You do not need a patent. You need a moat.**

### The six real moat types

| Type | The claim | Finalist example |
|---|---|---|
| **Patent** | A specific novel mechanism, with claim language | Soaring Seeds — granted utility model |
| **Trade secret** | A process that can't be reverse-engineered from the product | VORTA — SAP capsule chemistry |
| **Accumulating dataset** | Data that grows with adoption and can't be bought | Clarity — crowd-sourced contamination maps; SafeSat — in-situ debris data; Schoolace — student knowledge graphs |
| **Exclusive relationship** | A named partner, supplier, dataset, or institution | BeCure — validated with the Korean Beekeepers Association |
| **Ecosystem lock-in** | Switching cost once adopted | Retrofit + service contracts |
| **Cost structure** | A price the incumbent can't match without cannibalising itself | Vigil — <$100/bed **with no consumables**, attacking razor-blade economics |

**The cost-structure moat is under-used and powerful.** An incumbent earning recurring revenue on
consumables *structurally cannot* match a no-consumables competitor without destroying its own
business. Say that explicitly and a judge recognises real strategic thinking.

### The rejection list

| Claim | Why it fails |
|---|---|
| "We'll copyright our code so it can't be replicated" | Copyright protects expression, not function. Anyone can reimplement. **SUNSYNC wrote a version of this and it actively damaged their score** — it signals IP illiteracy to an engineer-judge. |
| "We used a unique programming method so our code can't be copied" | Not a thing. Obfuscation is not protection. |
| "We'll be first to market" | Only a moat if you say what the first move *locks in* — a contract, a dataset, a standard. |
| "Our team is more passionate" | Not a moat. |
| "We'll patent it" (no mechanism named) | A wish. Name the claim: what specific novel step would the claim cover? |
| "Our design is proprietary" | Asserted, not argued. Proprietary how? |

### The moat sentence

Every team must be able to complete this, out loud, without notes:

> **"A well-funded competitor can't just copy this because ______."**

If the ending is weak, the problem is the topic, not the writing — go back to
`/conrad-topic-finder` Stage 3, Gate 4.

Then the follow-up a Summit judge will actually ask: **"Why hasn't [obvious big company] done this?"**
Three valid answers: *they can't* (name the barrier — that's your moat); *they won't* (market too
small for them — that's your moat); *they have* (back to the search).

---

## Mode 3 — audit an existing draft

Screen Q4 and Q7 for:

- [ ] Q7 names **≥3 real incumbents**, including at least one **commercial product**
- [ ] Q7 states honestly what each does **better**
- [ ] Q4 states the delta on a **named axis**, not "our design is innovative"
- [ ] Q4's IP paragraph names a **real mechanism** from the six types
- [ ] No claim from the rejection list appears anywhere
- [ ] The originality search is documented in the references PDF
- [ ] The moat sentence completes convincingly

**Red flag:** a competitive analysis that only names weak alternatives. The judge picks the
comparison set, not you — and if a competitor exists and you didn't name it, the judge concludes
you either didn't look or you're hiding it. **Both are worse than the competitor.**

---

## On actually filing

Conrad **award winners receive patent support** as a prize, and teams **retain ownership of their IP**.

For the submission you do **not** need to have filed anything. Naming what *would* be claimed is
sufficient and is what most finalists do. If a team genuinely wants to file, a US provisional
patent is comparatively cheap and buys 12 months — but this is a family decision with real costs,
and it is out of scope here. Point them at a qualified attorney; do not give legal advice.

## Epilogue

```
---
conrad-ip-defensibility · rubric_version 2025-26.1
Innovation is 30% and Verification + IP Defensibility are two of its five sub-criteria.
The searches must be run by your team — Summit judges ask how you know you're original.
Not legal advice. Consult a qualified attorney before filing anything.
Next: /conrad-innovation-brief for Q4 and Q7 · /conrad-judge-simulator to test the score.
```
