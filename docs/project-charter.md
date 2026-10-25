# Project charter · Briefs A and B · Group details to confirm

**Record status:** Reconstructed after the analysis on 2026-10-25. This is not presented as a charter signed before work began. The repository does not record a public repository URL, confirmed member roster, or an original pre-analysis prediction; those fields are left for the team to supply.

| | |
|---|---|
| Project | Build 1 · Data to Insight in Kalpa Health · Briefs A and B |
| Sponsor named in the assignment materials | Dr Priya Menon, COO, Kalpa Health |
| Reviewers | Finance controller; city teams for Chennai and Jaipur |
| Group | Confirm group number and member names |
| Repository | Add the submitted repository URL, if applicable |
| Working period | Assignment project period; exact dates not recorded here |
| This record completed | 2026-10-25, after analysis |

## 1. The sponsor's questions

The exact sponsor wording is not saved in the repository. These are the questions as represented by the analysis:

- **Brief A:** Why did booked tests grow about 5% in H1 when the plan called for 18% growth?
- **Brief B:** Are the Q2 booking declines in Chennai and Jaipur real, a booking-count difference around the Legacy-to-Nova transition, or both?

## 2. The questions in our words

For A, reconcile the H1 booked-test result with the plan, decompose test growth into patients, visits per patient, and tests per visit, and show city contributions to the plan gap. For B, compare Q2 2026 with Q2 2025 across all six cities, apply the same rule for superseded rescheduled bookings, and compare Chennai and Jaipur with the four cities still on Legacy.

The decision is to treat the H1 result as below plan, reconcile the two city counts before interpreting them, and follow up on city-level patient losses without assigning a cause unsupported by this dataset.

## 3. Deliverables and acceptance checks

| Deliverable | Form | Acceptance check |
|---|---|---|
| A: growth explanation | Analysis, figures, and presentation | The 5.01% figure states the H1 periods, 435,008-test 2025 denominator, 456,788-test 2026 result, and 18% plan comparison; the volume tree and city shortfall contributions reconcile. |
| B: two-city comparison | Analysis, figures, and presentation | All six cities are shown for Q2 2025 vs Q2 2026; superseded records are treated consistently; a replacement trace and raw-to-adjusted comparison are available. |
| Reproducible analysis | `notebooks/01_briefs_A_B_analysis.ipynb` and data files | A teammate runs it from a fresh kernel using repository-relative paths and obtains the reported values. Fresh-run evidence still needs to be recorded. |
| Audit trail | Existing approach, decisions, and challenges logs | Each headline can be traced to a measure, denominator, period, and documented data rule. |
| Team explanation | Slides, board-number workbook, and individual write-ups | Slide claims match the notebook; each member writes and can explain their own contribution. |

## 4. Targets

| Target | Measure | Status in repository |
|---|---|---|
| Reconcile H1 growth | 2025 vs 2026 booked tests and +18% plan | Analysis reports +5.01%; verify in a fresh run. |
| Explain growth | Patients × visits per patient × tests per visit | Analysis reports +3.76% × −0.97% × +2.19%, approximately +5.01%. |
| Explain the two-city result | City changes vs Legacy peers, with replacement records reconciled | Analysis reports Chennai −7.6%, Jaipur −10.7%, and four Legacy cities +2.1%. |
| Keep the work auditable | Denominators, periods, row rules, and limitations stated | Logs and notebook are present; do not silently revise finalized logs. |
| Defend the work | Each member explains their own work and key numbers | Each member must complete their own write-up and preparation. |

## 5. Scope

| In scope | Out of scope |
|---|---|
| Brief A: H1 booked-test growth, plan gap, volume tree, and city contributions. | Brief E and the offer evaluation. |
| Brief B: Q2 city comparison, four Legacy peers, superseded reschedules, replacement tracing, and patient/activity split. | Causal claims about why patients fell or claims that Nova caused the decline. |
| Material reject-rule sensitivities and limitations. | A financial cost estimate not supported by the analysis. |

## 6. Roles and parts

The repository does not contain a verified roster or member-to-task mapping. Add each person's actual contribution here; do not infer or invent it.

| Member | Part owned | Notebook or deliverable | Also responsible for |
|---|---|---|---|
| To be confirmed by the team | To be supplied by the member | To be supplied by the member | Own write-up and ability to explain the work |

## 7. Risks and responses

| Risk | Response |
|---|---|
| Legacy and Nova count reschedules differently | Trace replacement links and show raw and adjusted Q2 counts. |
| A merge duplicates records | Keep the notebook's row-count checks and validate the final headline after a fresh run. |
| Rejected rows affect the headline | Show the documented sensitivity for the two-day date anomaly and rows without a valid test code. |
| Booking-count changes are mistaken for patient causes | Compare all six cities and describe patient-count change without a causal claim. |
| One member cannot explain the shared analysis | Each member reviews the notebook and writes their personal reflection in their own words. |

## 8. Assumptions and limits

| Assumption or limit | What could challenge it | Where to explain it |
|---|---|---|
| Released data is sufficient for the stated H1 and Q2 periods | Missing months or incomplete export coverage | Notebook checks and presentation caveat |
| A booking with a superseded-reschedule status was replaced | Broken or unmatched `rescheduled_from` link | Replacement trace and adjusted-count table |
| Lower patient counts describe the pattern but not its cause | Acquisition, retention, access, or operations data could show another explanation | Brief B caveat and proposed follow-up |
| No dated pre-analysis team prediction is in the repository | A contemporaneous team note could establish what was actually predicted | Add only if the team supplies that original record; never backdate a new one |

## 9. Decision rights

The team should confirm who made each original decision; this reconstructed charter does not assign individual ownership.

| Decision | Record available |
|---|---|
| Booking identity and cleaning rules | See finalized `docs/decisions-log.md` |
| Headline definitions and comparison periods | See notebook and finalized logs |
| Final slide and workbook freeze | Team to confirm |

## 10. Changes

This charter was reconstructed on 2026-10-25 to document the completed A/B scope. It does not claim the project was chartered or signed before the analysis. Future factual corrections should be dated and attributed by the team.
