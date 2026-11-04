# DATA 311 Project 2 — Commuter Access & Sustainability Dashboard

Team repository for DATA 311 Project 2: cleaning the synthetic commuter survey and campus population datasets, understanding the routing/transit data source, and building a dashboard that supports commute-mode decisions.

## Roster

| Name | Role |
|---|---|
| Katayoon | Project Manager |
| Joey | Tech Lead |
| Ryan | Domain Expert |
| Justin | QA |

Roles are held for the duration of Project 2 (Stages 1–5). Individual, stage-by-stage contributions are in [`contributions.md`](contributions.md).

## Repo structure

```
data/raw/        the two source CSVs, untouched — see data/raw/README.md
data/cleaned/    cleaning-notebook outputs — see data/cleaned/README.md
analysis/        the cleaning notebook — see analysis/README.md
dashboard/       the Streamlit app — see dashboard/README.md
outputs/figures/ exported chart images (empty until something is exported)
outputs/tables/  exported summary tables (empty until something is exported)
requirements.txt     Python dependencies for the notebook and dashboard
contributions.md     stage x role blurbs + individual evidence, all 5 stages
docs/privacy_security.md   sensitive fields, what the dashboard shows/doesn't, real-data prerequisites
```

## Privacy & security

See [`docs/privacy_security.md`](docs/privacy_security.md).
