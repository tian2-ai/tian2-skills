# Yau paper norms — structure, abstract, English quality

Distilled from 白皮书 ch.1 (论文三要求) + ch.3 (写作方法/格式/摘要) + ch.7 (English signal,
AI-prose tells). Use to critique each section without rewriting it.

## The three paper requirements (ch.1)
1. **学术诚信 (integrity):** real data, independent work, honest citations.
2. **逻辑与完整性 (logic & completeness):** the paper presents the whole research process
   coherently — question → method → result → significance, no gaps.
3. **专业性 (professionalism):** correct format, complete structure, proper conventions. Weighs
   heavily in the 初赛.

## Format (ch.3, modeled on 清华学报)
- Numbered hierarchical headings: 1, 1.1, 1.1.1; then 1), 2); then a), b).
- Figures/tables/equations numbered in order of first reference (图1, 表2, 式(4), 定理5).
- The intro carries no section number/title.
- Title: concise; English title ≤ ~100 characters, first word not an article, lowercase except
  first letter + proper nouns.

## Abstract rules (ch.3)
- Four layers: **研究目的 / 研究方法 / 研究结果 / 研究结论.**
- Stands alone; one paragraph; complete in meaning.
- Concrete: scientific language + specific numbers. **No literary flourish.** No figures/tables/
  citations/complex formulas inside the abstract.
- The student must personally write: the abstract's last sentence (contribution), the intro's
  research-gap sentence, and the conclusion's "our contribution is…" (ch.7).

## Per-subject section emphasis
- **Math:** formal theorem statements; complete proofs; cite the results you build on.
- **Experimental (phys/chem/bio):** methods reproducible; controls/variables/sample size stated;
  ethics/data provenance addressed.
- **CS:** contributions list; datasets with provenance/license; ≥3 baselines; ablations;
  mechanism explanation (not "the model learned it").
- **Econ:** identification strategy + key assumption stated; robustness; causation ≠ correlation.

## English quality (ch.7)
- English quality is read by the panel as a proxy for overall rigor.
- Chinese-first workflow: draft Chinese → DeepL first pass → heavy self-revision → optional light
  polish. Never ship machine translation untouched.
- **AI-prose tells judges catch (§误区三):** over-symmetric sentence rhythm; vague superlatives
  ("significant", "novel", "remarkable" overused); transition stacking ("moreover",
  "furthermore"); avoidance of concrete numbers; unnaturally fluent literature review that the
  student can't paraphrase aloud.
- Safe polish instruction: "preserve my argument structure and terminology; fix only grammar and
  fluency, minimally."

## Citation honesty (ch.7)
Every reference must be one the student has read and can summarize (problem/method/conclusion) in
~15 seconds — judges spot-check by pulling a random citation. Never paste AI-generated citations.
Cite the original papers for any pretrained model/dataset/algorithm used (e.g. BERT → Devlin et
al. 2019).
