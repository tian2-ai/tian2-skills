# Compliance / red-flag checklist — sts-evaluator

Run this every evaluation (Step 5). Surface every hit, sorted into three tiers. Cite the specific
spot in the student's materials. Per rubric.json `evaluation_guidelines`: note rules concerns but
STILL score the application — flagging does not zero the content score, it warns the student about
integrity exposure. Sources: rubric.json `compliance_checks` + /tmp/STS_FACTS.md.

---

## TIER 1 — DQ-level (can disqualify; from rubric.json `prohibited_items` + STS_FACTS)
Surface these first and unmistakably. If you SEE evidence of one, say so directly; if you cannot
verify it from the materials given, say "cannot verify — confirm with /sts-rules-wizard".

- [ ] **Team project with other high-school students.** STS is INDIVIDUAL. Research conducted
      together with other HS students is ineligible. (Past team work must be DISCLOSED in Task 6 but
      cannot be the submitted project.) Tell: "we" throughout the report with no role split, a
      co-author who is a HS peer.
- [ ] **AI-generated essays or research report.** The Ethics Statement (Task 10) certifies the
      report and application responses were NOT constructed with AI tools (e.g., ChatGPT). See the
      AI-content tells in Tier 3.
- [ ] **Research report exceeds 20 pages** (excluding title, abstract, bibliography per the rubric).
      If you have the PDF text, count pages. Over 20 → flag.
- [ ] **Uncited figure / chart / graph — including the student's OWN.** Per the Citation Guide every
      image/chart/graph must be cited; a missing citation can DISQUALIFY. Scan the report for
      figures with no citation/source line.
- [ ] **Plagiarism / uncited content.** Passages without attribution; report-similarity flags. STS
      runs iThenticate; Q19 asks the student to pre-explain similarities.
- [ ] **Missing required approval.** IRB for human subjects; IACUC for vertebrate animals; risk
      assessments for hazardous materials; PHBA / controlled-substance documentation; wildlife
      permits. If the research clearly needed one and it is not mentioned → flag → /sts-rules-wizard.
- [ ] **Undisclosed conflict of interest or payment.** Task 1 / Task 4 (Q17, Q18) and the rules
      require disclosing family members in STEM, conflicts of interest, and ALL payments for
      research/coaching. A close-relative mentor or paid coaching that is not disclosed → flag.
- [ ] **Literature review or plan with no results.** Reviews or proposals without original results
      are INELIGIBLE for the research report.

Note for the student: a high content score does NOT guarantee survival — ~23 of 463 OTT projects
were parked with a "9999" not-scored sentinel pending exactly these integrity screens
(plagiarism/iThenticate, COI, AI, team/secondary). Integrity is screened independently of score.

---

## TIER 2 — Score-costing red flags (observed in real STS losers; from STS_Top400_Winning_Criteria)
These don't disqualify but cost points on the rubric. Name each one you see and tie it to the
criterion it drags down.

- [ ] **"Limitations: None / N/A."** The single biggest avoidable mistake. Drags Scientific Analysis
      (2c) and Student Insight (3d). Every real project has 2–4 honest limitations — always name
      them. → /sts-contribution-coach, /sts-data-analysis-tutor
- [ ] **Confirmatory results dressed as discovery.** Reproducing a known result while framing it as
      novel. Drags Scientific Validity (2a) and Originality (3c). A rigorous NULL result framed as
      "shrinking the search space" scores better than an over-sold confirmation.
- [ ] **Thin data vs big claims.** Sweeping conclusions on a small/underpowered sample. Drags
      Scientific Setup (2b) and Analysis (2c). → /sts-data-analysis-tutor
- [ ] **Close-relative or assigned mentor with no student extension.** If the question and method are
      entirely the mentor's / a lab's and the student did not visibly extend or own a piece, drags
      Independence (3a). Reward an explicit bound on the mentor's role.
- [ ] **Thin / generic recommendations.** Standard praise with no specific example drags
      Recommendations (1b). (Student usually cannot control or see these — note, don't over-penalize.)
- [ ] **Overclaiming impact** ("revolutionize", "will cure", "first ever") before results support
      it. Drags Scientific Validity (2a) and reads as immature in Scientific Potential (4b).
- [ ] **No accessible layperson hook.** If the layperson summary (Task 7.1) is impenetrable, drags
      Scientific Ability (4a, communication). → /sts-essay-coach
- [ ] **Indistinct identity essay.** A generic "I love science" Potential essay drags 4b. → /sts-essay-coach
- [ ] **No external validation.** No publication/first-authorship/top-fair/olympiad stamp is not a
      flag per se, but its presence is a strong differentiator; note its absence as a ceiling on 4b.

---

## TIER 3 — AI-content tells (flag, still score; from rubric.json `ai_detection`)
Look for these in the essays AND the report. Any hit → flag for the student to confirm the text is
genuinely their own voice (the Ethics Statement certifies no AI construction). Do not accuse;
report the signal and let the student verify.

- [ ] Generic, voice-less language; no personal stake or specific lived detail.
- [ ] Uniform sentence cadence / rhythm across long stretches.
- [ ] Style inconsistent with the rest of the application (a polished essay next to rougher prose).
- [ ] Hedge-stuffing and filler ("it is important to note", "plays a crucial role", "in today's
      world", "delve into") without concrete content.
- [ ] Over-smooth structure with no idiosyncrasy, no false starts, no specific names/dates/numbers
      that only the student would know.
- [ ] Lists of benefits/limitations that are plausible-generic rather than specific to THIS project.

Reminder: AI-content concern is an INTEGRITY issue, not merely a style critique. If flagged, the
student should rewrite in their own voice (route to the relevant coach) — this skill does not
produce replacement text the student would submit as their own.

---

## How to present the compliance section
```
COMPLIANCE / RED FLAGS
  DQ-level:   <hits, or "none found in provided materials" + what you could not verify>
  Costing:    <each Tier-2 hit → criterion it drags → sibling to fix it>
  AI tells:   <each Tier-3 signal, framed as "confirm this is your own voice">
```
Route DQ/forms/disclosure concerns to `/sts-rules-wizard`; route score-costing fixes to the named
coach; then route the overall improvement plan to `/sts-top400-playbook`.
