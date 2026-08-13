# Task 3 decision tree — intake → required approvals & uploads

Verbatim/derived from `Regeneron_STS_Application_Questions_2026.txt` (Task 3: Rules Wizard / Form
Uploads, Parts I–IX) and the Official Rules. Task 3 is a branching yes/no wizard inside the online
application; a student who worked with NONE of the regulated substrates will only answer a few
questions. This file maps the intake answers to the parts they activate and the approvals/uploads they
demand. **Do not invent additional approval bodies or paperwork beyond what the official wizard lists;
verify edge cases against the current Official Rules.**

> STS official framing (quote): "Research that involves humans or human-related data, vertebrate
> animals, or human or vertebrate animal tissue and cell lines, PHBAs, prescription drugs and
> supplements, controlled substances, and/or hazardous materials and activities must adhere to
> Regeneron STS rules. Researchers must obtain special permissions and approvals to work with these
> subjects."

Three global upload rules that apply across the regulated parts:
- All IRB/IACUC approval forms, risk assessments, wildlife permits, and other paperwork must be
  **properly signed and completed, including any checkboxes that must be marked**.
- Any **surveys and informed-consent documents uploaded must be BLANK** (templates — never completed
  or signed copies with participant data).
- **Exempt studies still upload documentation about the source of the tissue or data.**

---

## §1 — Intake questions (ask ONE at a time, in this order)

1. **Humans / human data?** — human participants or human-related data: surveys, interviews,
   behavioral tasks, biometric/physiological data, or data about identifiable people. (Yes/No/Not sure)
2. **Vertebrate animals?** — live vertebrate animals: mammals, birds, reptiles, amphibians, fish.
   (Yes/No/Not sure)
3. **Human or animal tissue / cell lines?** — human or vertebrate-animal tissue, blood, body fluids,
   or cell lines (primary or established, e.g. HeLa/HEK293). (Yes/No/Not sure)
4. **PHBAs (potentially hazardous biological agents)?** — microorganisms, rDNA, viruses, pathogens.
   (Yes/No/Not sure)
5. **Hazardous chemicals / devices / activities?** (Yes/No)
6. **Prescription drugs / supplements / controlled substances?** — incl. DEA-controlled. (Yes/No)
7. **Field work?** — sample collection or procedures in an outdoor/wild/natural setting. (Yes/No)
8. **Regulated Research Institution (RRI)?** — conducted, in full or in part, at or under the
   supervision of an RRI (university, hospital, government lab). (Yes/No/Not sure)
9. **AI / ML use?** — in the project, the Research Report, or the application, in any way (code
   generation, analysis, figures). (Yes/No)
10. **Payments?** — by you or on your behalf, for research, mentorship, programs, training, or
    essay/application/competition coaching, now or in the past. (Yes/No/Not sure)
11. **Conflict of interest?** — any real or perceived family/employer/mentor/donor connection.
    (Yes/No/Not sure)
12. **Larger project / continuation?** — conducted as part of a larger project or group, or a
    continuation of prior work. (Yes/No)

"Not sure" → treat as a trigger (resolve conservatively) and flag for the student to confirm with the
adult sponsor / SRC / IRB / RRI.

Questions 9–12 feed the disclosures handled in `disclosures-and-dq.md` (Task 4 Q6/Q15/Q18/Q20, Q24);
questions 1–8 drive the Task 3 substrate parts below.

---

## §2 — Trigger map: answer → Task 3 part → approvals/uploads

| Intake "Yes" | Task 3 Part | Required approvals / uploads | Pre/Post | Body |
|---|---|---|---|---|
| Humans / human data (Q1) | **PART II — Human Research** | IRB review/approval; informed-consent / assent documents (uploaded BLANK); survey instruments (uploaded BLANK). Exempt studies still upload **source-of-data** documentation. | Pre-experimentation (approval before data collection) | IRB |
| Human/animal tissue or cell lines (Q3) | **PART III — Human Tissue and/or Cell Lines** | Tissue / cell-line **source documentation**; exempt studies still upload source-of-tissue docs. | Pre-experimentation / with application | IRB or institutional source authority |
| Any human-related project | **PART IV — Final Verification for Human-Related Projects** | Final attestations confirming the above uploads/approvals are complete and signed. | With application | n/a (student attests) |
| Vertebrate animals (Q2) | **PART V — Vertebrate Animal Research** | IACUC review/approval; risk assessment as applicable; signed approval paperwork. | Pre-experimentation | IACUC |
| PHBAs (Q4) | **PART VI — Research Involving PHBAs** | Biosafety review/approval appropriate to the agent; signed paperwork. | Pre-experimentation | Biosafety / institutional review |
| Hazardous materials/devices/activities (Q5) | **PART VII — Hazardous Materials & Activities** | Risk assessment; signed safety paperwork. | Pre-experimentation | Designated supervisor / institutional safety |
| Prescription / controlled substances (Q6) | **PART VIII — Prescription Drugs & Controlled Substances** | Documentation/authorization for the substances used. | Pre-experimentation | Institutional / licensed supervisor |
| Field work (Q7) | (overlays the relevant part) | **Wildlife permits** and field safety / risk paperwork as applicable. | Pre-experimentation | Permitting authority / supervisor |
| RRI = Yes (Q8) | **PART IX — Additional Paperwork & Information** | RRI institutional approval paperwork; affects independence attribution. | Pre-experimentation / with application | RRI |
| Larger project / continuation (Q12) | (overlays Task 4 narrative) | No extra Task 3 upload by itself, but drives the independence/attribution disclosures. | n/a | n/a |

Notes:
- A project can trigger several parts at once (e.g. human survey + AI analysis + RRI). Collect ALL
  that apply.
- Field work is not a standalone part; it adds wildlife-permit / field-safety requirements on top of
  whichever substrate part applies.
- For every triggered item, when you emit the checklist, state **why** (the trigger), **pre- vs
  post-experimentation**, and **which body** approves/issues it.

---

## §3 — Definitions / clarifications

- **IRB** (Institutional Review Board): reviews human-subjects research; approval is required
  **before** data collection for non-exempt human studies.
- **IACUC** (Institutional Animal Care and Use Committee): reviews vertebrate-animal research;
  approval required **before** experimentation.
- **PHBA** (potentially hazardous biological agent): microorganisms, rDNA, viruses, pathogens.
- **RRI** (Regulated Research Institution): a regulated entity (university, hospital, government lab)
  with its own oversight. STS asks (Part I, item G) whether the research was conducted, in full or in
  part, at/under an RRI. Conducting work at an RRI does NOT replace the STS disclosure obligations and
  can affect how independence is attributed (route the narrative to `/sts-mentor-finder` and
  `/sts-contribution-coach`).
- **Exempt study**: even when a study is exempt from full review, the student **still uploads
  documentation of the source of the tissue or data**.
- **BLANK documents**: uploaded surveys and informed-consent forms must be the unfilled template — not
  a completed/signed copy carrying participant information.

---

## §4 — Part I: Rules Overview & Timeline (A–G) — scaffold ONLY

STS asks seven timeline questions. The skill emits these as a blank scaffold; the student supplies the
**real** dates. Never invent or estimate a date.

- **A.** When did you start brainstorming your project? *(75 words max)*
- **B.** When did you request permissions/preapprovals (if needed) from an IRB/IACUC/high school, etc.?
  *(100 words max)*
- **C.** When did you begin collecting your data? If you collected different types/sets of data,
  describe each and give a start date for each type. *(100 words max)*
- **D.** When did you conclude data collection? If still ongoing, note that and give the cutoff used
  for the submitted Research Report. *(75 words max)*
- **E.** How did you get the data used in your research report — private? online? self-collected?
  Describe. *(125 words max)*
- **F.** What type of data was utilized? (survey responses, public database, collected via
  experimentation, etc.) *(100 words max)*
- **G.** Was this research conducted (in full or in part) at or under the supervision of a Regulated
  Research Institution? *(50 words max)*

Remaining Parts (II–IX) are reached by the wizard's branching logic and are listed in §2.

---

## Source provenance

- 「Regeneron STS 申请问题全文（2026 届）」 — Task 3
  Parts I–IX, the A–G timeline, the BLANK-documents and exempt-source-docs rules.
- 「Regeneron STS 官方规则（请自行从 societyforscience.org 取得）」 — Rules Wizard requirements and
  approval obligations.

Refresh from the official question set if STS revises Task 3 in a later cycle.
