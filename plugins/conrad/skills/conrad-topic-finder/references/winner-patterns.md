# Winner Patterns — What Actually Gets to Houston

Evidence base: `data/winners.jsonl` — 59 records across 2024, 2025, 2026 cycles.
The 2026 cycle is the deep sample: **35 records, 31 with full innovation descriptions**
(the complete Innovation Summit finalist roster). 2025 and 2024 are name-level only.

**Read the honest limitation first:** the strong claims below are drawn from one deep cohort
(2026). Treat them as well-grounded hypotheses about what the rubric rewards, cross-checked against
the rubric text and the Chief Judge's stated reasoning — not as multi-year statistics.

---

## 1. The one-sentence finding

> **Conrad finalists do not win with advanced technology. They win with a bounded problem,
> a named incumbent, a quantified delta, and a moat.**

Nearly every 2026 finalist description contains the same four moves. Most losing briefs
(see `02-judging-playbook.md`) contain none of them.

---

## 2. The finalist sentence template

Reverse-engineered from all 31 described 2026 finalists. It is startlingly consistent:

```
[Specific artifact] for [named, bounded user]
that [does X] via [named mechanism],
achieving [quantified delta] versus [named incumbent],
priced at [number], defended by [specific moat].
```

Worked examples, unmodified from the official finalist descriptions:

| Team | Artifact + user | Mechanism | Quantified delta | Incumbent named | Moat |
|---|---|---|---|---|---|
| **Vigil** | vital-sign monitor for *unmonitored hospital beds* | radar + thermal + motion | ICU-level at **<$100/bed** | ICU monitoring, consumable-based | no consumables |
| **Echo/Pulse** | speech headset for *7.5M Americans with speech disorders* | facial EMG + LLM | **$2,500** | AAC tablets **$10,500**, implants **$50–100k** | EMG-LLM pipeline |
| **Clarity** | microplastic detector for *households* | optical scattering + AI | **<$250** | lab equipment **$10,000+** | 40× price collapse + crowd dataset |
| **BeeGuard** | hive diagnostic for *10M beekeepers* | temporal multimodal AI | **94.7%** in **<1 s**, **zero hardware cost** | manual inspection | detects weeks before symptoms |
| **Aphelion** | attitude control for *small satellites* | spherical motor | **−20%** mass, **−61.8%** volume, **−71%** power | gimbaled mechanisms | proprietary control algorithms |
| **Root and Renew** | seeder for *480M smallholder farms* | no-till precision | **−62%** seed, **+52%** yield | ploughing | **$499**, 1–2 season payback |

**Notice what is absent:** none of these is a scientific discovery. Several use entirely
off-the-shelf components (Clarity: optical scattering; BeeGuard: a phone camera and microphone).

---

## 3. The seven repeatable winning archetypes

Each is a *strategy for generating a defensible innovation*, not a topic. These drive the
topic engine in `topic-engine/METHOD.md`.

### A. Price collapse
Take a capability that exists only at institutional cost and deliver it at consumer cost.
- **Clarity** — $10,000 lab → $250 consumer microplastic detection
- **Vigil** — ICU monitoring → <$100/bed
- **Echo/Pulse** — $50k–100k implant → $2,500 wearable

*Why it wins:* the delta is a single number, instantly checkable, and the incumbent is named
for you. Innovation scores on Ambition; Marketing scores on Differentiation.
*Requirement:* you must name the expensive incumbent and its real price.

### B. Zero-resource constraint
Deliver the function with one critical input removed — no power, no hardware, no water, no connectivity.
- **BlueFlow HydroSpines** — atmospheric water with **zero energy input**
- **ExFire Brick** — fire suppression with **no electricity, water, or intervention**
- **BeeGuard** — diagnosis at **zero hardware cost**
- **BeCure** — runs **offline on basic phones**
- **EcoClave** — **passive** countercurrent heat exchange, no controls

*Why it wins:* the constraint *is* the innovation, and it is self-evidently hard. Also scores
Impact Potential because it unlocks underserved geographies.
*Requirement:* name the input you removed and why competitors need it.

### C. Retrofit into installed base
Don't replace the expensive thing; clip onto it.
- **Kipos SubStation** — retrofit onto **aging subway cars**, 200+ metro systems
- **AeroLattice** — flap retrofit for **existing 737/A320 fleets**, 18,000+ aircraft
- **EcoClave** — external install on existing autoclaves, **workflow unchanged**

*Why it wins:* market size is a fleet count you can look up, adoption friction is near zero,
and it neutralises the "who would rip out their equipment?" objection before it's asked.
*Requirement:* state the installed-base number and prove the retrofit changes nothing else.
EcoClave's "sterilization procedures unchanged" is doing enormous work — it kills a regulatory objection in four words.

### D. Workflow replacement
Attack the *process*, not the device. Collapse sample→transport→lab→report into in-situ.
- **MicroSeek Ideon** — on-site microplastic analysis replacing lab transport
- **BeCure** — behavioural analysis replacing physical hive inspection
- **Dravix** — ML screening **upstream of** physical fire testing

*Why it wins:* differentiation is structural rather than incremental, so Ambition Level scores high.
*Requirement:* diagram the old workflow and the new one, with time/cost per step.

### E. Data as the second moat
The device is the wedge; the accumulating dataset is the business.
- **SafeSat** — debris shield **plus monetizable in-situ debris measurement datasets**
- **Clarity** — detector **plus crowd-sourced contamination maps** for researchers and policymakers
- **Schoolace** — platform **plus student knowledge graphs**
- **Back Tracker** — patient exercise app **plus objective movement data for clinicians**

*Why it wins:* directly answers **IP Defensibility** without a patent. A dataset that grows with
adoption is a textbook moat and reads as commercially sophisticated.
*Requirement:* name who buys the data and why they can't collect it themselves.

### F. Razor / blade and recurring revenue
Put the defensible IP in the consumable or the service, not the hardware.
- **VORTA GEOOSE** — robots deploy **patent-pending SAP-encapsulated capsules** (IP is in the capsule)
- **Ocean Energy** (non-finalist, but strong on this) — units plus maintenance contracts plus licensing
- **OctoScope** — monitoring **service** with hardware
- **Dravix** — cloud **subscription**

*Why it wins:* Finances scores on Revenue Projections and Financial Viability. Recurring revenue
is the single easiest way to look like you understand business.

### G. Hyper-specific geography or failure mode
Refuse the generic problem. Solve one population's exact version of it.
- **Soaring Seeds** — safe water specifically for **western plateau pastoral nomadic households**,
  addressing **filter clogging, secondary contamination, and freeze damage** — and holds a **granted utility model patent**
- **ExFire** — fire suppression specifically for **overcrowded urban settlements**
- **Root and Renew** — seeders specifically for **Asian smallholders**, locally manufacturable
- **StomaLock** — ostomy care, an underserved niche, with **discreet** alerts as a design requirement

*Why it wins:* specificity defeats the originality search. "Water purifier" has 10,000 competitors;
"freeze-resistant backwashing purifier for high-altitude pastoralists" has approximately zero.
This is the highest-yield move available to a team with no lab and no budget.

---

## 4. Quantified findings from the 2026 cohort (n=31 described)

| Signal | Frequency | Interpretation |
|---|---|---|
| Names a specific incumbent, product, or competing technology | ~26/31 | Near-universal. Its absence is the strongest negative signal. |
| States at least one quantified performance delta | ~28/31 | Percentages, dB, litres/day, accuracy, seconds. |
| States a price or unit cost | ~18/31 | Not universal — but every price-collapse archetype has one. |
| States a sized market with a number | ~22/31 | Often nested ($216M device market inside $12.4B tourism). |
| Explicit IP claim (patent granted/pending) | 3/31 | **Rare.** Soaring Seeds (granted), VORTA and DeepTrust (pending). |
| Moat via data, price, retrofit, or specificity rather than patent | ~majority | **The dominant defensibility strategy.** |
| Uses AI/ML inside the product | ~12/31 | Fully permitted and common — see §6. |
| Team size 2 | 11/31 | **Two-person teams are the single most common size.** |
| Team size 5 | 7/31 | Also common. Size is not a predictor. |
| Cross-border team (2+ countries/states) | ~9/31 | Explicitly encouraged; not required. |

**Most important number here: only 3 of 31 finalists claimed a patent.**
Teams routinely believe Conrad requires patentable IP. It does not. The rubric's own wording
lists "first mover, contracts, ecosystem capture" alongside patents.

---

## 5. Category dynamics

| Category | 2026 finalists | Character |
|---|---:|---|
| Health & Nutrition | 8 | Largest and most crowded. Assistive/diagnostic devices dominate. |
| Energy & Environment | 7 | Equinor-sponsored. Broadest interpretation of "environment". |
| The Water Challenge | 6 | Special category — **best odds per entrant**, see below. |
| Aerospace & Aviation | 6 | Most technically demanding; space debris is a saturated sub-theme. |
| Cyber-Technology & Security | 6 | Loosest boundaries — absorbs AI, software, robotics, wearables. |

### Category arbitrage is real and observable
Three 2026 finalists competed outside the "natural" category for their technology:

- **BeCure** (bee-mite detection) → **Health & Nutrition**, not Energy & Environment
- **Robo Therapy** (medical tremor exoskeleton) → **Cyber-Technology**, not Health
- **Echo/Pulse** (speech restoration) → **Cyber-Technology**, not Health

And **The Bee Initiative** (BeeGuard) entered the *same underlying problem* — hive health —
under **Energy & Environment**, where it won Pete Conrad Scholar. Two teams, one problem,
two categories, both finalists.

**Interpretation:** you compete against the teams in your category, not against the field.
A health device in Cyber-Technology is unusual, memorable, and faces a different comparison set.
This is a legitimate, rules-compliant strategic lever. Choose the category where your project is
*surprising*, provided the fit is honest.

### The special category is systematically under-entered
The Water Challenge takes the same ~6 finalist slots as the standing categories, but is new each
year and has no accumulated body of "obvious" projects. **Highest expected value per entrant.**
Whatever the 2026–27 special category turns out to be, this logic should hold.

---

## 6. AI in winning projects — the permitted use

12 of 31 finalists build AI/ML into the product: BeeGuard, BeCure, DeepTrust, Dravix, OncoMap,
Echo/Pulse, MicroSeek, Clarity, Schoolace, Back Tracker, Robo Therapy, VisionBridge.

This is **explicitly allowed and rewarded**, and is categorically different from using AI to
write your brief (prohibited). See `01-competition-facts.md` §8.

But the Chief Judge's warning governs: *"it's not convincing for teams to write that AI will solve
a problem or create action unexplainedly."* Compare:

- ❌ "Our AI analyzes hive health." — asserted, scores low
- ✅ BeeGuard: **"temporal multimodal"** — computer vision + acoustic + behavioural tracking,
  **94.7% accuracy**, **<1 second**, detects **weeks before visible symptoms**, **zero hardware cost**

The second names the modalities, the architecture property, the metric, the latency, the lead
time, and the deployment cost. That is what an AI claim has to look like.

---

## 7. Coaches compound

Two observable signals that coaching quality persists across seasons:

- **Karin Sempf** — Teacher of the Year 2025 (Inno-Vanation Panama); coached **TermoPaint**,
  a 2026 Citizenship Award winner.
- **Aashna Saraf** — 2026 Excellence in Education Award, coaching **two** teams (ExFire, TagAlong),
  one of which reached the finalist roster.
- Several finalist coaches share surnames with team members (Kummer/Aphelion, Davay/AeroLattice,
  Gupta/Flux Orbit, Suravarjjala/Dravix, Polapally/Clarity) — **parent-coaches are common and successful.**

**Implication for a mentoring program:** the coach relationship is durable and the returns
accrue over multiple seasons. Build for the second year from the start.

---

## 8. Anti-patterns — what does *not* appear among finalists

Cross-referenced against the five judged briefs in `02-judging-playbook.md`:

| Anti-pattern | Why it fails |
|---|---|
| Generic sustainability framing without a specific user | Fails the originality search; Impact is unquantifiable |
| "We'll copyright our code so it can't be replicated" | Signals IP illiteracy (SUNSYNC). IP Defensibility is an explicit sub-criterion. |
| Competitive analysis only against weak alternatives | The judge picks the comparison set (Puppy WC) |
| Advanced-sounding technology with no differentiation argument | Sophistication ≠ innovation (SUNSYNC) |
| Impressive arithmetic that violates conservation of energy | The reliable ~75-point ceiling (P-Bump, Ocean Energy) |
| Prototype built but never measured | Proves access and non-curiosity (SUNSYNC) |
| Duplicated answers across questions | Reads as abandonment (Greencrete) |

---

## 9. How to use this file

- **Topic generation** → `topic-engine/METHOD.md` operationalises §3 (seven archetypes) and §5 (arbitrage).
- **Brief writing** → §2's template is the target sentence for Q1 and Q4.
- **Self-assessment** → §4's signal table is a checklist: how many do you hit?
- **Refresh** → after each Summit, append the new finalist roster to `data/winners.jsonl`
  (procedure in `01-competition-facts.md` §12) and re-run the frequency counts in §4.
