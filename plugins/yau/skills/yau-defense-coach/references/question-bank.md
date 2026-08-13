# Defense question bank (by category + subject)

Generate a drill set from these. Categories apply to all subjects; specials are per-subject.
Grounded in ch.7's documented panel patterns.

## Universal categories
- **Motivation:** "Why this problem? Why does it matter? Who cares about the answer?"
- **Method choice:** "Why this approach and not {simpler / harder alternative}?"
- **Rigor:** "How do you know this isn't luck / overfitting / a confound?"
- **Mechanism:** "Why does it work? Explain, don't just describe."
- **Ownership:** "What part of this is genuinely yours? Could you do it without AI?"
- **Limitations:** "Where does this break? What would you do with more time?"
- **Citation:** "Summarize reference [X] in one sentence." (random spot-check)

## Subject specials
- **数学:** "Re-prove this lemma on the whiteboard now." / "Why is this hypothesis necessary?" /
  "What breaks if you drop assumption Y?"
- **物理:** "What are the boundary conditions?" / "Check the dimensions of this equation." /
  "What's the dominant error source in your measurement?"
- **化学:** "How did you confirm the product's identity (characterization)?" / "Why this synthesis
  route?" / (computational) "Why this functional/basis set?"
- **生物:** "Where did the data come from? Ethics approval?" / "Did you control for batch effect?"
  / "What's your independent validation set?"
- **计算机:** "How did you split train/val/test? Same distribution?" / "What's the cross-attention
  dimension and why?" / "Is the baseline comparison fair?" / "Is the gain 1% or 10%, and is that
  significant at your sample size?"
- **经济金融建模:** "What's your identification strategy?" / "Does your instrument satisfy the
  exclusion restriction?" / "Do parallel trends hold? Show a placebo test." / "Is this causal or
  correlational?"

## AI landmines
Pull from `/yau-ai-compliance` → `references/judge-qa-landmines.md` (10 questions). Always include
in the drill if the project used AI/ML.
