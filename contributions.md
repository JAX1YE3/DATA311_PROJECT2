# Contributions

This file describes the project and each team member's contributions.

| Name     | Role                                                                                      |
|----------|-------------------------------------------------------------------------------------------|
| Katayoon | Project Manager                                                                           |
| Ryan     | Data cleaning, validation and geocoding                                                   |
| Justin   | Regions and routing                                                                       |
| Joey     | Tech Lead                                                                                 |

---

## Katayoon: Project Manager

- Led the project and wrote the project plan. The plan divided the work into four workstreams (data, routing, dashboard, and repository/privacy/testing), set the dependencies between them, and gave each one a self-check.
- Coordinated the hand-offs between team members: the cleaned data feeds the regions table, and the regions table feeds the dashboard.
- Set up and organized the GitHub repository.
- QA, usability and deployment

## Ryan: Data cleaning, validation and geocoding

- Built `analysis/01_clean_data.qmd`, which loads, checks and cleans the survey and population data.
- Standardized categorical fields such as `role`, `city` and `mode_primary`. This included fixing misspelled values like "studnet", "Arcatra" and "Eurika", merging duplicate categories, and removing joke entries.
- Documented the cleaning in the narrative: the observational unit of each table, data-validation action items, assumptions and data-dictionary notes.
- Produced `survey_clean.csv`, `population_clean.csv` and the change log, and rendered the analysis to HTML.

## Justin: Regions and routing

- Defined the regions (Arcata, Eureka, McKinleyville, Fortuna, Trinidad, Blue Lake and Other) and found a centroid for each.
- Found the nearest GTFS bus stop for each region and set a distance cutoff that decides whether a bus is available.
- Saved everything as one precomputed table for the dashboard to read, so the deployed app never calls the routing server live.

## Joey: Streamlit dashboard

- Designed and built the dashboard in `app.py`. The layout puts the map first, then the region panel, then car information and cost.
- Built the interactive region map, colored by population. Clicking a region updates the population count, the preferred-mode chart, and the walk/drive/bus time, distance and CO₂e. A region with no bus shows a "no bus here" message.
- Built the car-cost calculator. Inputs are days per week, MPG and permit type (Cal Poly Humboldt permit prices). It shows the cost next to a CO₂e estimate based on the EPA factor.
