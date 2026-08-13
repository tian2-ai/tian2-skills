# Per-subject AI etiquette (green / yellow / red)

Distilled from 白皮书 ch.7 §各学科 AI 使用差异. These are INFERRED norms (no public rule), based
on judge behavior + the whitepaper. Same AI strategy across subjects is a silent failure cause.

## Universal (all subjects, ch.7 §评委真实态度)
- Judges assume you used AI; they will not forgive your not UNDERSTANDING it.
- They ask training details, not concepts ("how did you split the data?" not "what is a
  transformer?").
- They want "why use it / why this way," and your one original idea AI couldn't supply.
- Death answer: "我用了 GPT-4o 跑了一下."

## 数学 Mathematics — AI is an aid, not a collaborator
- GREEN: SymPy/Mathematica to verify hand-derived formulas; Lean/Coq/Isabelle to machine-verify
  key steps; LLM for literature search.
- RED: pasting an LLM-generated proof into the paper; asking an LLM to "think of" a problem.
- Why: math judges are pure mathematicians with structural distrust of AI proofs; they re-derive
  your lemma on the whiteboard. No disclosure rescues an AI proof — just don't.

## 物理 Physics — fine in data analysis, careful in theory modeling
- GREEN: PINNs, CNNs on experimental images, ML parameter inversion, symbolic tools.
- YELLOW: AI in theoretical modeling — disclose + be ready for boundary-condition / dimensional /
  Hamiltonian questions.
- RED: "GPT listed the equations and I plugged in numbers."

## 化学 Chemistry — computational welcomes AI; experimental limits it
- GREEN (computational): DFT, MOF/COF design, MD with ML scoring functions.
- YELLOW: ML on characterization data.
- RED (experimental synthesis/materials): AI standing in for real lab work.

## 生物 Biology — AI near-standard; guard the data
- GREEN/YELLOW: AI-guided drug/vaccine design, single-cell, medical imaging — disclose specifics.
- The panel drills: data source? ethics approval? batch effect / confounding handled?
  independent validation set? The respected pattern is "AI screen + real wet-lab validation."
- RED: computational results with no validation ("纸上谈兵"); ignoring ethics for human data.

## 计算机 Computer Science — AI IS the subject
- GREEN: PyTorch/HuggingFace/fine-tuning/API calls — the entry ticket, not a flaw.
- The edge (what earns points): an independent contribution beyond the existing ecosystem — a new
  training paradigm, a new benchmark, a new explanation of model behavior, domain knowledge fused
  with a model.
- RED: treating the model as a black box you can't explain; one weak/unfair baseline.

## 经济金融建模 Economic & Financial Modeling — AI for data, never for causal reasoning
- GREEN: ML return prediction, NLP on financial text, RL trading strategies, AI-as-object.
- RED: asking an LLM to "reason" the economic mechanism. The core is causal identification —
  judges ask your instrument, exclusion restriction, parallel-trends. LLMs can't supply these.

## License caveat (ch.7 §误区四)
Open-source ≠ unconditional use. LLaMA has commercial limits; some HF models bar
medical/legal use; some datasets bar commercial use. Note licenses for any model/dataset you
rely on, especially if the work might be published/promoted later.
