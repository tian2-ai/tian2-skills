# Task 5 Research Report — Format & Eligibility Rules (binary)

These are the mechanical rules for the uploaded Research Report. Most are **binary** — the report
passes or fails — and several are **disqualifying**. Check them FIRST, before any content review.
Source: official 2026 application questions, Official-Rules.pdf, and the STS Citation Guide.

## Eligibility gates (fail = INELIGIBLE)

- The report must describe **original research with results.** A **literature review only**, or a
  **research plan / proposal without results**, is **INELIGIBLE.** If the student has no data they
  have analyzed, the report is not ready — do not coach format on a non-report.
- The research must be the **student's own individual work** (STS is an individual competition; no
  other high-school students on the project). Honest mentor attribution belongs in Task 4
  (see `sts-contribution-coach`), but the report itself must reflect the student's work.

## Hard format rules (fail = fix before submission; several disqualifying)

| Rule | Requirement | Stakes |
|------|-------------|--------|
| **Page limit** | **<=20 pages**, EXCLUDING the title page, abstract, and bibliography (per the rubric). Body + figures + tables count. | A report over 20 pages is a listed compliance/DQ item. |
| **File size** | **<=4 MB** PDF. | Upload will be rejected / capped. Compress images, don't downsample data figures into illegibility. |
| **Filename** | Exactly **`LASTNAME.FIRSTNAME.ZIPCODE`** (e.g. `SMITH.JANE.10001.pdf`). | Required naming; wrong name is a flagged mechanical error. |
| **Not a scanned image** | Must be a **real text PDF** with selectable text — NOT photographed/scanned pages. | A scanned-image PDF is non-compliant. |
| **Every image/chart/graph cited** | EVERY figure, chart, graph, photo, and table must carry a citation **including the student's own figures** (cite per the STS Citation Guide). | **Missing or incorrect citation can DISQUALIFY the report.** This is the most common avoidable failure. |
| **No clickable links (except bibliography)** | Evaluators/judges **cannot click links** anywhere except the bibliography. The paper must stand alone. | Anything load-bearing hidden behind a URL/footnote-link is effectively invisible to the reader. |

## How to verify mechanically (if you have the PDF)

- **Page count:** `pdfinfo report.pdf | grep Pages` — then subtract title/abstract/biblio pages to
  get the counted total. Confirm with the student which pages are title/abstract/biblio.
- **File size:** `ls -l` / `du -h report.pdf` => must be <=4 MB.
- **Scanned vs text:** `pdffonts report.pdf` (embedded fonts => text PDF) and `pdftotext report.pdf -`
  (returns real text => not a scan). If `pdftotext` returns almost nothing but the page is full of
  content, it is likely a scanned image — FAIL.
- **Filename:** check the actual filename string against `LASTNAME.FIRSTNAME.ZIPCODE`.
- **Citations:** you cannot fully auto-verify; visually confirm each figure/table caption carries a
  citation, and explicitly remind the student that **their own figures need citations too.**

## The own-figure citation rule (call this out every time)

Students reliably cite figures they copied from papers but forget to cite figures **they made
themselves** (their own plots, photos of their apparatus, their own schematics). Per the STS
Citation Guide, those must be cited too (e.g. "Figure by the author"). An uncited own-figure is
the classic disqualification trap. Always check for it.

## What this reference does NOT cover

- Citation-style edge cases, the full Citation Guide, IRB/IACUC/PHBA approvals, AI-use disclosure,
  payment disclosure => route to `sts-rules-wizard`.
- The abstract wording and the layperson summary => route to `sts-essay-coach`.
