# Project statement · Briefs A and B

**Record status:** This statement was completed after the analysis. The repository contains no dated pre-analysis prediction. The hypothesis below is therefore labeled retrospective; it is not represented as the team's original prediction before opening the data.

## 1. Dr Menon's questions

The exact brief text is not stored in this repository. The following are paraphrases of the questions addressed:

- **Brief A:** Why did booked tests grow by about 5% in H1 when the plan called for 18% growth?
- **Brief B:** Did Q2 booking declines in Chennai and Jaipur reflect patient activity, a difference in booking counts around the Legacy-to-Nova change, or both?

## 2. The questions in our words

For Brief A, we compare H1 booked-test growth with the 18% plan and break total test growth into unique patients, visits per patient, and tests per visit. For Brief B, we compare Q2 2026 booking counts with Q2 2025 in Chennai and Jaipur, apply the superseded-reschedule rule consistently, and compare the city changes with the four cities that remained on Legacy.

The decision is whether to treat the A result as a growth gap, reconcile the booking counts in Chennai and Jaipur, and investigate city-specific patient declines if they remain after the count is reconciled.

## 3. A question the briefs do not resolve

Why did the number of patients fall in Chennai and Jaipur? The notebook measures patient counts and activity per patient, but it does not test causes such as patient acquisition, retention, service access, or local operations. Those questions would need follow-up with the city teams and additional evidence.

## 4. Translation into the method

| Brief language | Method used | What the measure means here |
|---|---|---|
| Explain the H1 growth result | Volume tree | Tests = unique patients × visits per patient × tests per visit. The component changes combine multiplicatively. |
| Compare actual growth with plan | Fair comparison | H1 2026 booked tests are compared with H1 2025 and the 18% plan. The plan total is 515,740; 2025 booked tests grown by 18% are 513,309, so booked tests are used as the headline measure. |
| Check two city declines around the system change | Same-quarter city comparison | Q2 2025 and Q2 2026 bookings are grouped by booking creation date. Chennai and Jaipur are compared with the four Legacy cities. Superseded reschedules are excluded consistently from adjusted counts. |

## 5. What does not transfer from Retail

| Retail framing | Diagnostics framing | What changes in the analysis |
|---|---|---|
| One sale is one order. | One booking is one visit, and a visit may contain several tests. | The notebook first aggregates test rows to bookings, then counts tests, visits, and patients separately. |
| A basket is the unit of customer demand. | Tests per visit and visits per patient are distinct measures. | We decompose total booked tests instead of treating a booking and a test as interchangeable. |
| A sale or conversion change explains the outcome. | Booking records may include replaced reschedules, while patient counts do not explain why a patient did not return. | The comparison checks superseded records and describes the patient-count change without claiming its cause. |

## 6. Prediction / working hypothesis

**Pre-analysis status:** No dated prediction written before data inspection was found in the repository. Do not backdate the statement below.

**Retrospective working hypothesis, recorded 2026-10-25:** The Q2 declines in Chennai and Jaipur are not explained solely by superseded Nova bookings. If the declines remain after excluding those records, and patient counts also decline relative to the four Legacy cities, the counts indicate a city-level patient-volume decline as well as a counting difference. This is a descriptive hypothesis, not a causal claim or a statistical significance test.

For Brief A, the analysis is a decomposition rather than a causal hypothesis: it identifies how changes in patients, visits per patient, and tests per visit combine to produce the observed H1 booked-test growth.

## 7. Requirements

### Functional

| # | Requirement | Evidence in this repository |
|---|---|---|
| F1 | Reproduce the H1 booked-test growth and compare it with the 18% plan. | `notebooks/01_briefs_A_B_analysis.ipynb`; `data/clean/brief_A_overall_summary.csv` |
| F2 | Show the denominator, period, and measure behind the headline. | H1 2025: 435,008 tests; H1 2026: 456,788 tests; growth: 5.01%. |
| F3 | Explain the H1 movement and show which cities contribute to the plan shortfall. | The notebook's volume tree and booking-based city-plan comparison. |
| F4 | Compare Q2 bookings in Chennai and Jaipur with the four Legacy cities using one superseded-reschedule rule. | Q2 city comparison and raw-to-adjusted count calculations in the notebook. |
| F5 | State limitations and data-quality sensitivity without claiming a cause. | Reject audit, sensitivity calculations, decisions log, and the Brief B findings. |

### Non-functional

| # | Requirement | Evidence / status |
|---|---|---|
| N1 | Run from a fresh environment without manual path edits. | Notebook uses a repository-relative `data/raw` path. Fresh-environment run and runtime still need to be recorded by a teammate. |
| N2 | Make the headline traceable to rows and rules. | Source-file fields, clean/reject outputs, and decisions log. |
| N3 | Record each material cleaning and counting decision and its effect. | `docs/decisions-log.md`; leave the finalized log unchanged. |

### Constraints

| # | Constraint |
|---|---|
| C1 | Use the released synthetic data pack and preserve the source files in `data/raw/`. |
| C2 | The course admin's updated guidance allows AI as a learning aid; team members must understand and be able to explain their work. Record assistant use accurately. |
| C3 | Scope is Briefs A and B. Brief E is out of scope. |

## 8. Scope

| In scope | Out of scope |
|---|---|
| H1 booked-test growth, its three-part volume decomposition, and city contributions to the H1 plan shortfall. | Brief E and an evaluation of the offer. |
| Q2 booking changes for Chennai and Jaipur, the four Legacy-city peer comparison, superseded reschedules, and patient/activity split. | A causal explanation for patient declines or a claim that the system migration caused them. |
| Documented sensitivity to specified rejected rows. | A financial cost estimate; no supporting rupee estimate is in the analysis. |

## 9. Done looks like

The project is ready to present when the A and B claims match the notebook's denominators and periods, the Q2 count rule is consistent across cities, each cleaning rule has a documented effect, and a teammate can run the notebook from a fresh kernel. The final slides and board-number workbook must use the same figures and caveats.

## 10. Who signs off

| Reader | What they should be able to check | What would undermine confidence |
|---|---|---|
| Dr Menon | The H1 result, Q2 city pattern, and the next decision. | A headline without a measure, comparison period, or caveat. |
| Finance controller | Counts, denominators, source data, and cleaning rules. | An unexplained difference between raw and adjusted counts. |
| Chennai and Jaipur city heads | Whether their dashboards use the same definition of a booking and replacement. | A claim that the data identifies why patient counts fell. |
