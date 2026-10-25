# Kalpa Health: Growth and Booking Review

This project investigates two questions using Kalpa Health’s synthetic booking and reference data:

1. **Brief A — Growth:** Why did booked tests increase by **5.01%** in January–June 2026 when the plan called for **18%** growth?
2. **Brief B — Chennai and Jaipur:** Did the Q2 booking declines reflect lower patient activity, differences in how Legacy and Nova records were counted, or both?

The analysis finds that H1 booked tests rose from **435,008** to **456,788**, below plan. The growth decomposition is patients **+3.76%**, visits per patient **−0.97%**, and tests per visit **+2.19%**. In Q2, adjusted bookings fell **7.6% in Chennai** and **10.7% in Jaipur**, while the four Legacy cities combined grew **2.1%**. Removing superseded rescheduled bookings makes the Chennai and Jaipur declines larger; the data does not establish why their patient counts fell.

## Project details

| Item | Details |
|---|---|
| Project | Build 1 — Data to Insight in Kalpa Health |
| Briefs covered | A (growth) and B (two cities) |
| Data period | January 2025–June 2026; exact comparison periods are labeled in the notebook and slides |
| Repository | [Week 3 Build Week — Kalpa Health](https://github.com/pdt0208/Week_3_Build_Week_Kalpa_Heath_Project) |
| Team | Add the full group roster and each member’s owned work before final submission |

## Analysis approach

The analysis combines the booking exports, aligns the Legacy and Nova fields, standardizes dates and city labels, and records rows that do not meet the stated counting rules. It then:

- compares H1 booked tests with the plan and decomposes growth into patients, visits per patient, and tests per visit;
- compares Q2 2026 with Q2 2025 in Chennai and Jaipur and uses the four Legacy cities as a peer comparison;
- excludes superseded rescheduled bookings consistently in the Q2 comparison; and
- reports data-quality checks and sensitivity results alongside the headline findings.

The city comparison is descriptive. It shows that patient counts fell in Chennai and Jaipur, but it does not identify the cause of the decline or establish that the booking-system change caused it.

## Repository map

| Path | Contents |
|---|---|
| [`notebooks/01_briefs_A_B_analysis.ipynb`](notebooks/01_briefs_A_B_analysis.ipynb) | Main analysis notebook for Briefs A and B |
| [`data/raw/`](data/raw/) | Original synthetic data exports and reference files; see [`data/raw/README.md`](data/raw/README.md) and `MANIFEST.json` |
| [`data/clean/`](data/clean/) | Derived clean tables, summary CSVs, reject audit, and charts produced by the notebook |
| [`docs/approach-log.md`](docs/approach-log.md) | Approaches considered and choices made |
| [`docs/decisions-log.md`](docs/decisions-log.md) | Cleaning and counting decisions and their effects |
| [`docs/challenges-log.md`](docs/challenges-log.md) | Issues encountered, checks, and resolutions |
| [`docs/ai-log.md`](docs/ai-log.md) | Record of AI assistance used on the project |
| [`docs/board-hypotheses.md`](docs/board-hypotheses.md) | Post-analysis hypothesis review and CEO-facing response |
| [`slides/Kalpa_Health_Brief_A_B_Board_Edition.pptx`](slides/Kalpa_Health_Brief_A_B_Board_Edition.pptx) | CEO-facing board presentation with recommendations |
| [`docs/`](docs/) | Project notes, diagrams, and supporting documents |
| [`slides/`](slides/) | Presentation files and the board-number workbook |

## Run the analysis

Run the notebook from the repository root so its relative path to `data/raw/` resolves correctly.

1. Install Python and create an environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade pip
   python -m pip install jupyterlab ipykernel numpy pandas matplotlib
   ```

2. Start JupyterLab from the repository root:

   ```bash
   jupyter lab
   ```

3. Open `notebooks/01_briefs_A_B_analysis.ipynb` and run all cells from a fresh kernel.

The notebook reads from `data/raw/` and writes derived tables and charts to `data/clean/`. Running it again replaces those generated outputs. It does not change the original files in `data/raw/`.

## Data and interpretation notes

- The Kalpa Health records are synthetic and fictional, as described in [`data/raw/README.md`](data/raw/README.md).
- H1 refers to January–June. Q2 refers to April–June.
- Brief A uses **booked tests** for the plan comparison. Lab-result rows are a separate cross-check because they omit visits without a recorded result.
- Superseded reschedules are excluded from the adjusted Q2 booking comparison. Raw and adjusted counts are shown separately in the supporting presentation material.
- Rows with missing or invalid test codes and date anomalies are documented in the notebook and decision log; their effects are not silently folded into the headline.
