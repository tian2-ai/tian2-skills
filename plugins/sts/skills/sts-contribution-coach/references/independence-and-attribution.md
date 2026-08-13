# Independence & attribution — building Q20, plus Q14 / Q15 / Q17 / Q10

This file covers the non-phase boxes that share the same logic as the six contribution boxes: the
statement of independence (Q20, 200w), limitations (Q14, 200w), AI-use (Q15, 100w), additional-support
disclosure (Q17, 200w), and origin-of-idea (Q10, 250w). All of them are evidence for the **Student
Contribution** criterion or feed the integrity screens. None of them is ghost-written — the skill
structures and critiques the student's own words.

---

## Q20 — Statement of independence (≤200 words)
Built FROM the six per-phase attributions, not written fresh. After the student has answered "what I
did vs what the mentor/lab provided" for phases a–f, synthesize:

1. **Lead with the independent core.** One or two sentences naming the parts that are unambiguously the
   student's across the phases (e.g., "I conceived the time-varying variant, wrote the solver, ran all
   data collection, and did the analysis").
2. **Bound the mentor/lab role explicitly.** State plainly what they provided (lab access, an existing
   protocol, a code wrapper, weekly advice, funding). Bounding the role *increases* credibility — vague
   independence claims read as either naive or evasive.
3. **Differentiate per phase where it matters.** The rubric rewards student-vs-mentor work that is
   "clearly differentiated." If one phase was heavily mentor-led, say so and show where the student took
   over.
4. **Quantify if a number is honest and available.** "The simulation code is ~95% mine; the mentor
   contributed the I/O wrapper." Only use a figure the student can stand behind and the mentor letter
   would not contradict.

The statement must be CONSISTENT with all six boxes and with what the Project Recommendation writer
would say. Contradictions between Q20 and the phase boxes are a classic over-claim tell.

---

## Three failure modes — diagnose every box for these

### Vagueness (most common)
Verbs with no object or no agency: "helped", "assisted with", "was involved in", "participated in",
"worked on", "contributed to", "was responsible for", "supported the effort". Each hides who actually
did what.
- Fix prompt to the student: **"Describe the exact step you did that your mentor did not."** Do not
  guess the step — extract it. If they cannot name one for a phase, that is a finding.
- Replace passive/agentless phrasing with "I did X" / "the technician did Y".

### Over-claim
- Sole credit for shared or supervised work (instrument runs a technician performed, code a mentor
  wrote, a dataset the lab already had).
- Impact inflation ahead of evidence ("revolutionize", "first ever", "will cure") — a known red flag.
- Anything the Project Recommendation could contradict. The test: *would the person closest to the
  research confirm this exact sentence?* If not, it is over-claimed.
- Fix: bound it ("I built the solver core; the mentor wrote the I/O wrapper") and tie claims to results.

### Under-claim (costs points silently)
Strong students often bury their best work behind "the lab" or passive voice out of modesty, losing
Independence/Initiative credit they earned.
- Tells: real decisions and fixes described without "I"; the failure-and-fix story missing entirely;
  a genuinely owned question described as fully assigned.
- Fix: surface it. "You said the log-grid switch was your call after the linear sweep failed — that is
  your single strongest independence signal. Lead the box with it."

---

## Q14 — Limitations (≤200 words). NEVER "None."
"Limitations: None / N/A" is the single biggest avoidable red flag in this section. Naming real
limitations reads as scientific maturity and scores on Insight; pretending there are none reads as
naivety or evasion.
- Help the student name **2–4 genuine limitations**, each with its **direction of effect**: small sample
  size (widens CIs / limits generalization), single site or cell line, unmodeled confound, measurement
  noise, an assumption the model makes, short observation window, simulation not yet experimentally
  validated.
- For each, one clause on how it bounds the conclusion or what future work would address it.
- Tie limitations honestly to the conclusions (Q14f) — they should be the same limitations that tempered
  the conclusions, not a disconnected list.
- Route deeper rigor questions (which test, error sources, cross-validation, whether a limitation is
  fatal) to `/sts-data-analysis-tutor`. This box *states* limitations honestly; that skill *assesses*
  them.

## Q15 — AI-use answer (≤100 words)
Narrate truthfully what AI tools were used and for what — within the bounds STS allows. The Task 10
Ethics Statement certifies AI tools like ChatGPT were NOT used to construct the research report or
application responses; so this answer typically describes legitimate, disclosed uses (e.g., a coding
assistant for boilerplate during the research, literature-search aids) and explicitly NOT for writing
the report or these responses.
- Be specific and honest: tool, task, and what it was NOT used for.
- For whether a particular AI use is *permitted* or must be *disclosed/gated*, route to
  `/sts-rules-wizard`. This skill drafts the truthful narrative; the wizard owns the compliance rule.

## Q17 — Additional support disclosure (≤200 words)
The honest, complete account of outside help: lab access, equipment, funding, datasets, statistical
help, editing, programs, anyone who contributed. Under-disclosing here is an integrity risk; over-
disclosing costs nothing and aligns the application with the recommendation letters.
- Capture every form of support the student received; phrase it factually.
- This pairs with the COI (Q18) and payment disclosures, which are gated by `/sts-rules-wizard` — route
  the *disclosure-requirement* questions there; draft the *narrative* here.

## Q10 — Origin of idea (≤250 words)
Where the question came from and how the student made it theirs. This sets up the whole independence
story and feeds Originality/Creativity.
- What sparked it (a paper, a phenomenon, a course, a problem the student noticed) — in the student's
  own voice.
- The honest provenance: assigned, suggested, or self-generated — and then the specific move that made
  it the student's own (the narrowing, the variant, the new angle from box (a)).
- Consistent with Q9 (mentor relationship), Q12 (independence from a larger project), and the six boxes.

---

## Mentor-letter corroboration (the silent gate)
The Project Recommendation comes from the person closest to the research and is read alongside Task 4.
The strongest applications read so the recommendation can independently confirm the same specifics —
the same fix, the same owned question, the same bounded mentor role. Practical checks:
- For each strong claim, ask: *would my mentor describe it the same way?* If unsure, make it confirmable
  or soften it.
- Mentor-letter *strategy* (who should write, what to ask them to highlight) is `/sts-mentor-finder` —
  route there; do not coach the letter's content here.
- A high score does not survive an integrity screen if the boxes and the letter disagree, so consistency
  is not just style — it is risk management.

## Bilingual note
Coach in EN, 中文, or both per `--lang`. When working in 中文, still keep the student's own voice and the
same diagnostics (空泛 / 过度声称 / 低估自己), and keep the explicit "我做了什么 vs 导师/实验室提供了什么"
split in every box.
