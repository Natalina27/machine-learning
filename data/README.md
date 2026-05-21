# Data folder

Local datasets for notebooks. Files here are **gitignored** (not pushed to GitHub).

## Files in this folder

| File | Used in course? | Notes |
|------|-----------------|-------|
| `titanic.csv` | **Yes** (week-1, days 2–7) | Replace with **full** file (891 rows). Current copy may be incomplete (~183 rows). |
| `iris.csv` | **No** | Not referenced in any notebook. Safe to delete or keep for extra practice. |

## Other data (not stored here)

| Dataset | Where loaded | TODO |
|---------|--------------|------|
| **California housing** | `week-1/day-3-regression/` via `fetch_california_housing()` | Optional: export once to `california_housing.csv` |
| **Day 1 mini example** | Built in code (`pd.DataFrame({...})`) | No file needed |

## After week-2 merge

1. Download full Titanic → overwrite `titanic.csv`
2. Switch week-1 notebooks from URL to `../../data/titanic.csv` (grep `TODO` in `week-1/`)
3. Review `iris.csv` — remove if unused
