# Challenges log — Briefs A and B

These entries record issues found during the analysis, the checks we made, and the changes that followed.

| # | Phase | What we found | What we checked | Team decision and change | What we learned | Owner | Date |
|---|---|---|---|---|---|---|---|
| A1 | Growth | Booked tests grew 5.01%, while result rows grew 6.09%. | We compared both counts with the plan total. | We use booked tests for the plan comparison and keep result rows as a separate check. | Check how the plan was measured before choosing a headline. | Team | 2026-10-24 |
| A2 | Data quality | 2,442 rows put the slot date exactly two days before booking; 990 of 1,030 affected booking IDs also appear in collection records. | We checked the time gap and looked for those booking IDs in collection data. | We left them out of the clean count and recorded both results: 5.01% with the rows excluded and 4.97% if included. | Check unusual rejects against another source and show their effect on the headline. | Team | 2026-10-24 |
| B1 | Vendor change | Q1 did not line up with a system change that began in April. | We checked the system-change date and compared the same quarter across years. | We use Q2 year-on-year and include all six cities. | Choose the comparison period based on when the change occurred. | Team | 2026-10-24 |
| B2 | Booking counts | Nova kept records marked as replaced after rescheduling. | We followed the `rescheduled_from` links and compared raw and clean counts. | We exclude superseded records consistently and keep the replacement links for review. | Check replacement records before comparing vendor totals. | Team | 2026-10-24 |
