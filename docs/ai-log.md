# Assistant log · Brief <LETTER> · Group <N>

Every use of a coding or chat assistant, one line each. Allowed uses: explaining an error you already tried to read, explaining a concept you then rewrite in your own words, checking English in the write-up without changing meaning. Not allowed: generating analysis, notebooks, cells, charts, slides, write-ups or the video script; asking what the answer or approach should be; pasting Kalpa Health data in.

An empty log next to notebooks that read like a tutorial is a claim the panel will test. Twenty honest lines are fine.

> Note: the course admin's email "Updated Guidance on AI Use for the Project" removed the earlier restriction on using AI tools for analysis, notebooks and write-ups, provided every use is acknowledged and understood. Entries below follow that guidance.

| # | Date | Who | Tool | What we asked (one line) | What we did with the answer |
|---|---|---|---|---|---|
| 1 | 2026-10-24 | dhairya244 | Claude Code | Review the notebook against the handbook | Got a list of problems: notebook crashed on a fresh run, Brief A tree missing, reject rules drop real visits; fixed them ourselves over several rounds |
| 2 | 2026-10-24 | dhairya244 | Claude Code | Fix the hard-coded datapack path and the wrong plan table name | Assistant edited cell 2 (relative `DATA_ROOT`) and cell 17 (`plan_2026_H1`); we re-ran and checked the outputs |
| 3 | 2026-10-24 | dhairya244 | Claude Code | Suggest code for the Brief B Q2 comparison, counting split and city tree | Adapted the suggested cells into the notebook; checked numbers against outputs (Chennai −7.6%, Jaipur −10.7%, peers +2.1%) |
| 4 | 2026-10-24 | dhairya244 | Claude Code | Reorder notebook sections and remove duplicate cells | Assistant moved the plan comparison into Brief A (A4), removed duplicate cells, fixed headings; we re-ran the notebook from a fresh kernel |
