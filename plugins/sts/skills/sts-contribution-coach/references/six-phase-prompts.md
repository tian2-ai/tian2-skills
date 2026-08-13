# Six-phase elicitation prompts — STS Task 4 contribution boxes (Q13/14a–f)

Each of the six boxes is **≤200 words** and asks about ONE phase of the research. The boxes are the
primary evidence for the **Student Contribution** criterion (Independence, Initiative,
Originality/Creativity, Insight). The reviewer is reading for one thing across all six: *can I see the
student's independent core, clearly differentiated from the mentor/lab, phase by phase?*

Use this file as the question bank. Work ONE phase at a time, in order a→f. For every phase ask the
same three things, capture the student's answer verbatim first, then tighten.

## The universal per-phase pattern (ask these for every phase a–f)
1. **"In this phase, what did YOU personally do?"** — capture concrete actions, decisions, tools, files.
2. **"What did the mentor, lab, or anyone else provide or do for this phase?"** — equipment, code,
   protocols, datasets, funding, advice, hands-on help. This is not a confession; an honest, bounded
   mentor role makes the independent core *more* credible, not less.
3. **"Describe ONE specific step you took that your mentor did NOT — ideally something that went wrong
   and what you changed."** — the failure-and-fix story. This is the highest-scoring sentence in the
   box. Concrete process (Insight + Initiative) beats any generic claim.

If the student answers (3) with a generic line ("I troubleshooted the code"), push once: *which* error,
*which* decision, *what* did you change it to, *why*. If they still cannot answer, that is a finding —
record it; do not invent the step.

Anchor every box to a NUMBER where one exists ("cut runtime from 40 min to 90 s", "n grew from 12 to
180 samples"). Repeating a concrete figure is a strong Initiative/Originality signal.

---

## (a) Developing the purpose / research question
- What did YOU do to arrive at this purpose, hypothesis, or question?
- What did the mentor hand you — was the question assigned, suggested, or part of a larger grant?
- The decisive probe: **did you own or visibly extend the question?** Name the specific narrowing,
  variant, or new angle that is yours. "My mentor studies X broadly; I asked specifically whether X
  holds when Y, which the lab had not tested."
- Good: "I noticed the published method assumed a static field; I proposed testing the time-varying
  case, which became my purpose." Vague: "I was interested in this topic and wanted to learn more."
- If the question was fully assigned with no extension, say so honestly and look for where the student
  later made it their own (often surfaces in phases b–f). Do not manufacture ownership.

## (b) Designing the procedures / experimental or computational design
- What design decisions did YOU make (controls, variables, sample size, model choice, parameter grid,
  apparatus, pipeline architecture)?
- What did the mentor/lab provide (an existing protocol, a standard rig, a code template, a prior
  pipeline you adapted)?
- Probe: which design choice was a real fork where you picked one path and rejected another, and why?
- Good: "I added a negative control the standard protocol omitted, and switched from a linear to a log
  parameter grid after the linear sweep missed the regime of interest." Vague: "I designed the
  experiment following best practices."

## (c) Implementing the procedures / carrying out the work
- What did YOU physically or computationally build, run, code, assemble, or operate?
- What was done FOR you (technician ran the instrument, mentor wrote part of the code, a core facility
  processed samples)?
- Probe — this phase is where failure-and-fix stories live: what broke, and what did you do about it?
  ("Rewrote the integrator when it diverged; switched to a log grid; recalibrated the sensor after
  drift.")
- Good: "I wrote the 600-line simulation; when it diverged at high Reynolds number I rewrote the
  integrator with an implicit scheme, which stabilized it." Vague: "I implemented the methodology and
  collected results."
- Over-claim watch: do NOT claim sole credit for instrument runs a technician performed or code a
  mentor wrote. Bound it: "the mentor wrote the I/O wrapper; the solver core is mine."

## (d) Gathering / recording data
- What data-collection did YOU do, and how did you record/manage it (logs, scripts, instrument runs,
  field collection, database queries)?
- What was provided (a shared dataset, prior lab data, an automated logger someone else built, public
  archive access set up by the mentor)?
- Probe: a quality/integrity decision you made — discarding a corrupted run, adding a logging check,
  re-collecting after a calibration error, choosing inclusion criteria.
- Good: "I logged 180 runs; I caught a timestamp drift on day 3 and re-ran the affected 22 trials."
  Vague: "I gathered all the data needed for the study."
- For no-lab / computational / public-dataset projects (a valid top-tier path): be specific about
  *your* data handling — which archive (e.g., Chandra, MODIS), which query, which cleaning steps, which
  validation of the pipeline. The laptop is the instrument; show the rigor.

## (e) Analyzing data
- What analysis did YOU perform (which tests, models, code, statistical decisions, visualizations)?
- What did the mentor/lab provide (an analysis script template, a statistician's help, a shared
  toolchain)?
- Probe: an analysis decision and its justification — why this test, how you checked assumptions, how
  you handled an unexpected result, whether you cross-validated with a second independent method
  (a strong rigor signal).
- Good: "I ran the mixed-effects model myself, checked residual normality, and cross-validated the key
  effect with a permutation test that did not assume normality." Vague: "I analyzed the data and found
  significant results."
- Route deep analysis-rigor questions (which test is appropriate, error sources, cross-validation
  design) to `/sts-data-analysis-tutor`. This box reports *who did what*; that skill checks *whether the
  analysis is sound*.

## (f) Formulating the conclusions
- What conclusions did YOU draw, and how did you reason from the results to them?
- What interpretation came from the mentor or the broader lab discussion?
- Probe: where did you push back, revise, or temper a conclusion based on what the data actually showed
  — including any null or negative result you chose to report honestly (a rigorous null framed as
  shrinking the search space can win).
- Good: "The data did not support my original hypothesis; I concluded the effect is bounded above by X,
  which narrows where future work should look." Vague: "I concluded my hypothesis was correct and the
  results were important."
- Over-claim watch: do NOT inflate impact ("this will revolutionize…") ahead of the evidence; tie every
  conclusion to a specific result.

---

## Triage at the end of the six boxes
After a–f, scan for the shape of the contribution:
- **Strong:** independent core visible in most phases; at least one concrete failure-and-fix; the
  question owned or extended; mentor role bounded and consistent across boxes.
- **Thin phase:** a phase where the student cannot name anything they did beyond the mentor. Surface it
  honestly — sometimes the real independent work is in a neighboring phase and the student undersold it
  (under-claim); sometimes it is genuinely the mentor's, in which case the box should say so plainly.
- **Consistency check:** the same mentor role should appear the same way across all six boxes and the
  statement of independence (Q20). Contradictions read as either carelessness or over-claim.
- **Corroboration check:** every specific should be something the Project Recommendation writer (the
  person closest to the research) could independently confirm. If a claim could not be corroborated,
  it is either over-claimed or needs to be made confirmable.
