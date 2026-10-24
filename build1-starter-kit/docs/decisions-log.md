# Decisions log — Briefs A and B

The rows below record the cleaning and counting decisions used in Briefs A and B, with their effects on the reported numbers. AI use is recorded in `ai-log.md`.

| # | Brief | Finding | Team decision | Rows / visits | Effect on the number | Reversible? | Owner |
|---|---|---|---|---:|---|---|---|
| A1 | A | 2,442 rows have `slot_at` exactly two days before `created_at`; 990 of the 1,030 affected booking IDs appear in collection records. | Leave these rows out of the clean count and show a sensitivity. | 2,442 rows | Growth is 5.01% with them excluded and 4.97% if counted as tests. | Yes | Team |
| A2 | A | Some rows have no valid `test_code`. | Do not treat them as confirmed tests; show a one-row-per-reject sensitivity. | 1,311 rows | 422 are in H1 2025 and 464 in H1 2026. Counting each as one test gives 5.01% growth; this is only a sensitivity. | Yes | Team |
| A3 | A / B | 21 Nova visits have no accepted test row: 15 in Chennai and 6 in Jaipur. | Keep them in the reject audit; they are absent from the clean booking table. | 21 visits | All have H1 2026 slot dates. Twenty were created in Q2 (14 Chennai, 6 Jaipur), affecting Q2 clean booking counts. | Yes | Team |
| A4 | A | The total city plan is 515,740; 2025 booked tests increased by 18% is 513,309. | Use booked tests for the plan comparison and label result rows as a check. | — | Booked tests grew 5.01%; result rows grew 6.09%. | Yes | Team |
| B1 | B | The system switch began in April 2026. | Compare Q2 2025 with Q2 2026 and show all six cities. | — | Chennai bookings fell 7.6%, Jaipur 10.7%; the four Legacy cities grew 2.1%. | Yes | Team |
| B2 | B | Nova records include superseded bookings. | Exclude the replaced records and keep the `rescheduled_from` links. | 970 Chennai; 494 Jaipur | Removing them makes the Q2 declines larger; raw Nova counts hide part of the fall. | Yes | Team |
