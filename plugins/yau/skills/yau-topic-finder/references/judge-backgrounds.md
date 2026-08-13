# Per-subject judge backgrounds & AI etiquette

Distilled from 白皮书 ch.4 (评委背景分析) and ch.7 (各学科 AI 使用差异). These are REAL panel
members named in the whitepaper; do not invent others. Use this to set the right "what will the
panel care about" tone per subject, and to flag AI etiquette early.

## Why judge background matters for topic choice
ch.4: "这些评委的背景信息可以帮助大家更好的进行选题." The panel is dominated by working
scientists; their research tastes shape what reads as a serious vs. a naive topic.

## 数学 Mathematics
- **Panel character:** pure mathematicians. Named in ch.4: 朱毅 (applied/computational, intl.
  judge lead), 许洪伟 (differential geometry, Zhejiang), 叶俊 (stochastic processes / financial
  math), 吴康 (competition-math educator). The advisory committee includes 丘成桐, 李骏, 肖杰,
  朱熹平, 姚期智.
- **AI etiquette (ch.7):** *deep, structural suspicion.* AI is an aid, never a collaborator.
  OK: SymPy/Mathematica to check by-hand work; Lean/Coq/Isabelle to machine-verify key steps
  (the 2024 CS-gold LLM+formal-verification approach is the respected pattern); LLM for
  literature search. NOT OK: pasting an LLM-generated proof; asking an LLM to "think of" a
  problem. **Expect whiteboard re-derivation of your key lemma.**

## 物理 Physics
- **Panel character:** condensed-matter / statistical / computational physicists. Named: 徐少达
  (Siu-Tat Chui, condensed matter, intl. lead), 林熙 (low-T mesoscopic transport), 邢向军 (soft
  condensed matter), 吴镝 (magnetic nanomaterials), 郑波 (computational/statistical, finance &
  bio physics crossover), 阮东, 陈焱.
- **AI etiquette (ch.7):** reasonable in data analysis (PINNs, CNNs on experimental images, ML
  parameter inversion); be cautious in theoretical modeling. If your "physics model" is really
  "GPT listed equations," judges expose it via boundary conditions / dimensional analysis.
  Pure-AI physics rarely wins; AI as an experiment accelerator is a big plus.

## 化学 Chemistry
- **Panel character:** synthetic / materials / nano chemists. Named: 唐本忠 (AIE pioneer, intl.
  lead), 黄乃正 (natural-product synthesis), 唐智勇 (nano functional materials), 李艳梅 (chemical
  biology), 席振峰 (organometallic, CAS academician), 黎占亭, 王训, 王歆燕, 孙兴文.
- **AI etiquette (ch.7):** computational chemistry welcomes AI (DFT, MOF/COF design, ML scoring
  functions). For synthesis/materials prep, keep AI to literature + characterization; do not let
  it stand in for real experiments.

## 生物 Biology
- **Panel character:** cell biology / cell death / virology / genetics. Named: 袁钧瑛 (apoptosis
  & necroptosis pioneer, Harvard/CAS, intl. lead), 蔡亮 (cytoskeleton), 俞强 (tumor/inflammation
  signaling), 李文辉 (HBV receptor NTCP discoverer), 周敬流, 郗乔然, 杨继 (plant systematics).
- **AI etiquette (ch.7):** AI is near-standard (AI-guided drug design, single-cell, medical
  imaging). The panel knows the tools; they drill **data provenance, ethics approval, batch
  effect / confounding, independent validation.** Computation without wet-lab validation reads
  as "纸上谈兵."

## 计算机 Computer Science
- **Panel character:** computer graphics / vision / HPC / systems. Named: 查红彬 (CV/robotics,
  intl. lead), 傅红波 (interactive graphics/HCI), 胡事民 (graphics, Jittor framework author),
  过敏意 (parallel/HPC), 童若锋 (VR/CV/medical AI), 张松海 (non-photorealistic rendering).
  姚期智 (Turing laureate) on the advisory committee.
- **AI etiquette (ch.7):** "AI 就是这个学科本身." Using PyTorch/HuggingFace/fine-tuning is the
  entry ticket. The panel asks about *training details, not concepts* ("how did you split the
  data? same distribution? what's the cross-attention dimension and why?"). Edge = an
  independent contribution beyond the existing model ecosystem.

## 经济金融建模 Economic & Financial Modeling
- **Panel character:** macro-finance / econometrics / game theory economists. Named: 唐本忠
  (finance, Tsinghua SEM, intl. lead — note: distinct from the chemistry judge of the same
  romanization), 苗彬 (decision under uncertainty), 王城 (dynamic contracts/macro), 苏良军
  (nonparametric econometrics/ML), 翁翕 (game theory/info econ), 汤珂, 张顺明, 白重恩, 周亚虹.
- **AI etiquette (ch.7):** ML for prediction / NLP on financial text / RL trading is normal, and
  AI-as-research-object is a high-scoring pattern. **Danger zone:** asking an LLM to "reason"
  about economic mechanisms. The core is **causal identification** — judges ask for your
  instrument, exclusion restriction, parallel-trends assumption. LLMs cannot supply these.

## Universal pattern across all six panels (ch.7)
Judges default to assuming you used AI; they will not forgive your *not understanding* what you
used. The death answer is "我用了 GPT-4o 跑了一下." The winning posture is layered disclosure +
demonstrable ownership of the one original idea that is yours.
