# data/raw

This folder holds the two source datasets **untouched** — exactly as distributed on Canvas, before any cleaning.

| File | Observational unit | Status |
|---|---|---|
| `simulated_commuter_survey_2020_26_messy.csv` | one respondent × one survey year | **missing — needs to be added** |
| `population_addresses_messy.csv` | one person (campus role + current/permanent address) | **missing — needs to be added** |

**Action needed:** these two files are referenced by `analysis/01_clean_data.qmd` (Step 2 — Load raw data) but were never committed to this repo. Whoever has the original Canvas download should add them here, untouched, so the analysis notebook can be re-rendered end to end. Do not edit, rename, or re-save these files through Excel/Sheets (that silently changes ZIP codes and other text-formatted columns) — add them exactly as downloaded.

Once added, `analysis/01_clean_data.qmd` already points at `../data/raw/<filename>` for both files.
