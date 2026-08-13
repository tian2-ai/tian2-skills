# Judge Q&A landmines (AI-related) — finals 2023–2025

From 白皮书 ch.7 §评委追问的典型问题与应对（沙盘推演）. High-frequency AI questions at the
all-English finals. Each: don't-say / recommended direction / trap. Have the student draft
answers for the ones that apply.

1. **"Did you use ChatGPT to write the paper?"**
   - Don't: "No, never." (If the panel hears LLM cadence, you're judged dishonest.)
   - Do: admit grammar/expression polish; state design, lit review, discussion are yours; say you
     checked every AI edit.
   - Trap: calling "I had GPT fix the abstract" = "no AI" — small lie, big cost.

2. **"Why does your model give this result?"**
   - Don't: "The model learned it."
   - Do: explain via architecture (e.g. how attention captures long-range dependence), training
     data features, loss design; show attention/saliency maps if relevant.
   - Trap: treating the black box as an answer.

3. **"Could you do this research without AI?"**
   - Don't: "No" (self-deprecating) or "Totally" (sounds false).
   - Do: AI compressed time on implementation/lit-screening; the core idea — problem definition +
     method choice — is yours; without AI it'd be slower but the conclusion stands.
   - Trap: showing over-reliance.

4. **"Where did your training data come from? How were labels obtained?"**
   - Don't: "Downloaded from the internet."
   - Do: cite public datasets + license; describe self-collected protocol + size; annotation
     process (annotators, agreement) or weak-supervision rules; name data biases/limits.
   - Trap: ignoring data compliance/privacy/ethics (the top probe for human data).

5. **"What are your baselines, and why these?"**
   - Do: three layers — naive (random/linear), strong classic (XGBoost/SVM), recent SOTA. Explain
     each isolates a different reason your gain isn't luck/tuning.
   - Trap: one weak or unfair baseline (your big model vs their small one).

6. **"How do you verify the AI didn't make a mistake?"**
   - Do: internal (cross-validation, ablation), external (independent/hold-out set), mechanistic
     (attention/feature attribution matches domain sense).
   - Trap: reporting only training accuracy.

7. **"Would your method transfer to {related-but-different domain}?"**
   - Do: state the assumptions it relies on (distribution, sample size, feature type); honestly
     name the modifications a new domain would need.
   - Trap: claiming it works "for everything."

8. **"Summarize this paper you cited in one sentence."**
   - Do: 15-second problem/method/conclusion for every reference you listed.
   - Trap: citing papers (AI-selected) you never read — random spot-check exposes it.

9. **(Math) "Re-prove this lemma on the whiteboard."**
   - Do: walk up and derive it. No hesitation.
   - Trap: "the proof is long, I don't remember it all" = declaring it isn't yours.

10. **(Econ) "What's your causal-identification strategy? Does your instrument satisfy
    exclusion?"**
    - Do: name DID/IV/RDD/RCT; state key assumptions; give robustness checks (placebo, bandwidth
      sensitivity).
    - Trap: reading simple-regression correlation as causation — the top econ deduction.
