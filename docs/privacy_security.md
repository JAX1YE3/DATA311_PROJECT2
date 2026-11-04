# Privacy & Security

## 1. Sensitive fields in the raw data

- **Exact street addresses** — `current_street`/`permanent_street` (and the derived `current_full_address`, `current_lat`/`current_lon` in `population_geocoded.csv`). These can pinpoint a specific residence.
- **Free-text fields** — `open_ended_no_car` and the `secondary_barrier` write-in text in the survey. Free text can contain names, landmarks, or other identifying detail that structured fields don't.
- **Small-n groups that could re-identify someone when role is crossed with location.** Checked directly against the cleaned data (`data/cleaned/population_geocoded.csv`), grouping by `current_city` × `role`:

  | current_city | role | n |
  |---|---|---|
  | (blank/unknown) | Faculty | 5 |
  | (blank/unknown) | Staff/Admin | 12 |
  | Fortuna | Faculty | 18 |
  | Trinidad | Faculty | 25 |
  | Trinidad | Staff/Admin | 29 |
  | Blue Lake | Staff/Admin | 32 |
  | Blue Lake | Faculty | 36 |
  | Fortuna | Staff/Admin | 53 |

  Any of these groups, shown on a per-region map alongside role, is small enough that someone who knows "the only faculty member who commutes from Trinidad" could identify that respondent. The same risk applies on the survey side: Staff/Admin (1,630 of 6,990 survey rows) and Faculty (1,481) are much smaller than Student (3,879), so a region with a small Staff/Admin or Faculty count is exactly where this shows up.
- **Respondent-level rows in general** — even without a name, a full row (address + role + commute pattern + free text) is enough detail to be identifying in a small community like this one.

## 2. What the public app will and will not show

- **Will show:** region-level aggregates only — the six regions already built in `data/cleaned/region_routing_table.csv` (Arcata, Eureka, McKinleyville, Fortuna, Trinidad, Blue Lake), each with population count, preferred-mode %, average CO₂e by mode, and the walk/drive/bus routing numbers.
- **Will not show:** raw address rows, lat/lon dots per respondent, or any other respondent-level map marker.
- **Minimum-n suppression:** regions (or role breakdowns within a region) under a minimum count are suppressed rather than displayed with a potentially misleading or re-identifying small number. Proposed minimum: **n ≥ 20** per displayed cell, based on the table above — this would suppress the Faculty/blank-city, Staff-Admin/blank-city, and Fortuna-Faculty cells specifically. Track C should treat this as the default and we can revisit the threshold together before deploy.
- Any role breakdown shown per region (e.g., "mostly students" vs. a specific headcount by role) should be rounded/bucketed rather than shown as an exact small integer.

## 3. What would be needed before replacing the simulated data with real data

This project currently uses **synthetic** survey and population data. Before any real Cal Poly Humboldt data could be substituted in:

- **Institutional/IRB or ITS approval** for collecting and analyzing commuter + address data tied to role.
- **A data-use agreement** with whatever office holds the real roster/address data, specifying purpose limitation (sustainability/commute planning only) and retention.
- **De-identification** before the data reaches this codebase: addresses generalized to region (not exact geocoded points) prior to export, free-text fields reviewed/redacted, and small-n suppression applied upstream, not left to the dashboard to enforce as the only safeguard.
- Signed consent language covering how survey responses will be aggregated and published (the `consent` column already in the survey data suggests this was anticipated — worth confirming what that field actually governs before relying on it as our consent record).
