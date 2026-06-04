# Machine Learning Journey

Hands-on ML notebooks — from fundamentals to production-ready pipelines.

## Prerequisites

- **Python 3.11+** (recommended: **3.12**)
- **Git** — clone and track progress
- **~1 hour/day** for one week (see PDF plans in `resources/`)
- **Internet** only if `data/*.csv` files are missing (see [Data](#data) below)
- **Editor:** [Cursor](https://cursor.com/) or VS Code with Jupyter support (or classic Jupyter in the browser)

**Stack** (`requirements.txt`, pinned): NumPy, Pandas, Matplotlib, scikit-learn, Jupyter, ipykernel.

## Goal

Two-week, notebook-first path:

1. **Week 1** — ML workflow: data → model → metrics → pipeline → mini project (Titanic).
2. **Week 2** — Python foundations for ML: types, control flow, collections, functions, files, NumPy, EDA.

No prior ML experience required for Week 1; Week 2 can be done before or after Week 1 depending on your Python level.

## Quick Start

```bash
cd machine-learning
python3.12 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name machine-learning --display-name "Python 3.12 (machine-learning)"
```

**Run notebooks in Cursor / VS Code:** open a `.ipynb` file → select kernel **Python 3.12 (machine-learning)** (project `.venv`).

**Or in the browser:**

```bash
jupyter notebook
```

Start here: `week-1/day-1-intro/day1.ipynb` (ML) or `week-2/day-1-variables/day1.ipynb` (Python base).

**Troubleshooting:** if you see *"requires the ipykernel package"* — pick kernel **Python 3.12 (machine-learning)**, not the system/Homebrew Python. Reload the window if the kernel list is outdated.

**Workspace settings:** `.vscode/settings.json` points the interpreter at `.venv` and keeps notebooks lean in Git (see [Notebooks and Git](#notebooks-and-git)).

## Notebooks and Git

Committed `.vscode/settings.json` includes:

| Setting | Effect |
|---------|--------|
| `notebook.transientOutputs` | Cell outputs are **not** written into `.ipynb` on save |
| `notebook.output.textLineLimit` | Caps long text output in the editor (100 lines) |
| `python.defaultInterpreterPath` | Uses project `.venv` |

**Optional — clear outputs in the editor on save:** add to your **user** keybindings (Cursor / VS Code → *Keyboard Shortcuts* → open `keybindings.json`):

```json
{
  "key": "cmd+s",
  "command": "runCommands",
  "args": {
    "commands": [
      "notebook.clearAllCellsOutputs",
      "workbench.action.files.save"
    ]
  },
  "when": "notebookEditorFocused && !notebookOutputFocused"
}
```

On **Cmd+S**, visible outputs disappear and the file stays small; re-run cells when you need output again. Keybindings stay local (not in the repo).

**Git + [nbstripout](https://github.com/kynan/nbstripout) (optional):** if `*.ipynb filter=nbstripout` is set (often in `~/.gitattributes`), then `git add .` runs each notebook through `nbstripout` before it lands in the index: **outputs are removed**, file size stays small. Without `--keep-id`, cell ids can reset to `"0"`, `"1"`, … and GitHub notebook preview may break. This repo expects **`--keep-id`** on the filter.

After **clone** (or on a new machine), configure the filter **in this repo** — settings live in `.git/config` and are **not** committed:

```bash
cd machine-learning   # repository root

git config filter.nbstripout.clean "/Library/Developer/CommandLineTools/usr/bin/python3 -m nbstripout --keep-id"
git config filter.nbstripout.smudge "cat"
git config diff.ipynb.textconv "/Library/Developer/CommandLineTools/usr/bin/python3 -m nbstripout -t --keep-id"
```

Use your `python3` path if different (`which python3`). Check: `git config --get-regexp 'filter\.nbstripout'`.

**What `git add .` does with this setup:** stages all changes; for `.ipynb` files, git stores the **stripped** version (no outputs, **ids kept**). Other files (`.py`, `README.md`, `data/*.csv`, …) are staged as-is. If the filter is missing, `git add` may still work but ids can be corrupted — run the commands above.

If you rely only on `notebook.transientOutputs` in the editor, you can skip nbstripout entirely and remove `filter=nbstripout` from your global `~/.gitattributes`.

## Data

CSV files in `data/` are **included in the repository** (clone and run offline). Only `data/*.zip` is gitignored. Start Jupyter from the **repository root** ([Quick Start](#quick-start)); week-2 days 5–7 pick `data/` or a notebook-relative path automatically.

| File | Used in |
|------|---------|
| `titanic.csv` | week-1 days 2–7; week-2 day 7 (assignments) |
| `california_housing.csv` | week-1 day 3 |
| `iris.csv` | practice / extras |
| `perfumes.csv` | week-2 day 7 (theory) |

Week-1 notebooks use `../../data/...` from each day folder.

If files are missing, from project root after `pip install -r requirements.txt`:

```bash
curl -o data/titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
python -c "import pandas as pd; from sklearn.datasets import load_iris, fetch_california_housing as f; i=load_iris(); pd.DataFrame(i.data, columns=i.feature_names).assign(target=i.target, species=i.target_names[i.target]).to_csv('data/iris.csv', index=False); f(as_frame=True).frame.to_csv('data/california_housing.csv', index=False)"
```

## Study Plans (`resources/`)

Weekly plans (PDF, Russian) — one file per week, aligned with notebook folders:

| Week | Plan | Notebooks |
|------|------|-----------|
| 1 | [ML from scratch](resources/План_на_неделю_ML_с_нуля_1.pdf) | `week-1/day-1-intro/` … `week-1/day-7-project/` |
| 2 | [Python base for ML (v2)](resources/План_Неделя_2_Python_база_под_ML_v2.pdf) | `week-2/day-1-variables/` … `week-2/day-7-pandas-eda/` |

## Repository Structure
- `week-1/day-1-intro/` — ML basics: terms and first mini dataset
- `week-1/day-2-pandas/` — data loading and cleaning
- `week-1/day-3-regression/` — Linear Regression, MAE/RMSE, baseline
- `week-1/day-4-classification/` — Logistic Regression, confusion matrix, F1
- `week-1/day-5-trees/` — Decision Tree, Random Forest, feature importances
- `week-1/day-6-pipeline/` — Pipeline, StandardScaler, cross-validation
- `week-1/day-7-project/` — final project: full ML pipeline on Titanic

**Week 2 — Python base for ML** (`dayN.ipynb` in each folder):

- `week-2/day-1-variables/` — variables, types, strings, errors
- `week-2/day-2-loops/` — conditions and loops
- `week-2/day-3-collections/` — lists, dicts, sets
- `week-2/day-4-functions/` — functions and clean code
- `week-2/day-5-files/` — files and modules
- `week-2/day-6-numpy/` — NumPy basics
- `week-2/day-7-pandas-eda/` — Pandas + Matplotlib EDA

- `data/` — CSV datasets (in repo; [setup](#data) if a file is missing)
- `resources/` — weekly study plans (see [Study Plans](#study-plans-resources))
- `LEARNING_LOG.md` — progress checklist

## Week 1 Results

Snapshot from completed notebooks (May 2026). Re-running cells may shift numbers slightly.

**Data & setup:** see [Data](#data). Split: `test_size=0.2`, `random_state=42`.

| Day | Notebook | Dataset | Key result |
|-----|----------|---------|------------|
| 1 | `day-1-intro/` | synthetic mini example | Classification vs regression, train/test split |
| 2 | `day-2-pandas/` | Titanic | Missing values, encoding |
| 3 | `day-3-regression/` | `data/california_housing.csv` | LinearRegression MAE **0.53** vs baseline **0.91** |
| 4 | `day-4-classification/` | Titanic (`Survived`) | LogisticRegression accuracy **0.80**, F1 **0.75** |
| 5 | `day-5-trees/` | Titanic | Random Forest accuracy **0.80**; top feature: **Fare** |
| 6 | `day-6-pipeline/` | Titanic | 5-fold CV mean accuracy **0.78** ± **0.02** |
| 7 | `day-7-project/` | Titanic | RF test accuracy **0.81**; LR more stable across CV (std **0.02**) |

## Week 2 Results

Python fundamentals for ML — **skills and exercises**, not model metrics. Notebooks are in Russian. Days 1–6 and day 7 theory run offline; **day 7 assignments** use local `data/titanic.csv` ([Data](#data)).

| Day | Notebook | Key outcome |
|-----|----------|-------------|
| 1 | `day-1-variables/` | `int` / `float` / `str` / `bool`, f-strings, `type()`; read **NameError**, **TypeError**, **IndexError**; type casting; palindrome check |
| 2 | `day-2-loops/` | `if` / `elif` / `else`; `and` / `or` / `not`; `for` over list, string, `range()`; `while`; **calculator**, char counter, **max + index** without `max()` |
| 3 | `day-3-collections/` | list / dict / set; `.get()`; `top_k()`; set ops `&` `\|` `-`; `copy()` vs `deepcopy()` |
| 4 | `day-4-functions/` | defaults, `try/except`; list/dict comprehension; `normalize()`; mini-pipeline filter → transform → aggregate |
| 5 | `day-5-files/` | `open` + UTF-8, `pathlib`; `utils.py` + import; text stats (lines, unique words, top-10) → `results.txt` |
| 6 | `day-6-numpy/` | `ndarray`, `shape`/`reshape`, boolean masks; `mean`/`std` by `axis`; broadcasting; BMI filter, `standardize()`; list vs NumPy speed |
| 7 | `day-7-pandas-eda/` | `read_csv`, `head`/`info`/`describe`, missing values, `groupby`; matplotlib `hist`/`bar`; theory on `perfumes.csv`; assignments EDA on **Titanic** (`data/titanic.csv`) |

Update this table when you finish a day (replace *planned* with your takeaways). Day-by-day checklist: [LEARNING_LOG.md](LEARNING_LOG.md).

## Progress

**Checklist (Week 1 & 2):** update [LEARNING_LOG.md](LEARNING_LOG.md) when you finish a day — one place for ✅ / todo, no duplicate tables here.

## License

[MIT License](LICENSE) — Copyright (c) 2026 Natalya Myunster.