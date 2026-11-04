# dashboard

Placeholder for Track C (Joey) — the Streamlit app.

Planned contents, per the Stage 3 instructions:

- `app.py` — layout: map first, region panel below, then car-info + cost calculator
- map built with streamlit-folium (or Plotly): one shape per region, colored by population, clickable
- on click: population count + preferred-mode bar chart for that region
- time/distance/CO₂e for walk/drive/bus, with a clear "no bus here" message when `bus_available` is false
- car-cost calculator (days/week, car MPG default 25, permit-type dropdown) + CO₂e number
- link out to EPA's Greenhouse Gas Equivalencies Calculator
- footer: assumptions, data sources, survey-vs-population legend

Data source: `data/cleaned/region_routing_table.csv` (built by Track B) plus `data/cleaned/survey_clean.csv` / `population_clean.csv` (Track A).
