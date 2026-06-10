# Machine Learning Journey

Personal ML learning repo — weekly notebooks, PDF plans, day-by-day progress in [LEARNING_LOG.md](LEARNING_LOG.md).

## Curriculum

Details in `resources/*.pdf` and notebooks.

| Week | Topic | Plan | Code | Status |
|------|-------|------|------|--------|
| 1 | ML from scratch → pipeline on Titanic | [PDF](resources/План_Неделя_1_ML_с_нуля_1.pdf) | `week-1/` | done |
| 2 | Python base for ML | [PDF](resources/План_Неделя_2_Python_база_под_ML_v2.pdf) | `week-2/` | done |
| 3 | Git + first scikit-learn models | [PDF](resources/План_Неделя_3_Git_и_первая_ML_модель.pdf) | `week-3/` | in progress |

## Quick Start

Python **3.12**, Git, Jupyter in [Cursor](https://cursor.com/) / VS Code. Stack: `requirements.txt`.

```bash
cd machine-learning
python3.12 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m ipykernel install --user --name machine-learning --display-name "Python 3.12 (machine-learning)"
```

Open `.ipynb` → kernel **Python 3.12 (machine-learning)**. Run from **repo root**.

*Troubleshooting:* *"requires ipykernel"* → pick **Python 3.12 (machine-learning)**, not system Python.

## Data

`data/*.csv` are in the repo (offline). Only `data/*.zip` is gitignored.

| File | Used in |
|------|---------|
| `titanic.csv` | week-1, week-2 day 7 |
| `california_housing.csv` | week-1 day 3 |
| `iris.csv` | extras |
| `perfumes.csv` | week-2 day 7 |

If missing after clone:

```bash
curl -o data/titanic.csv https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
python -c "import pandas as pd; from sklearn.datasets import load_iris, fetch_california_housing as f; i=load_iris(); pd.DataFrame(i.data, columns=i.feature_names).assign(target=i.target, species=i.target_names[i.target]).to_csv('data/iris.csv', index=False); f(as_frame=True).frame.to_csv('data/california_housing.csv', index=False)"
```

## Notebooks and Git

`.vscode/settings.json` — project `.venv`, outputs not saved into `.ipynb` on save.

If `*.ipynb filter=nbstripout` is enabled, configure **`--keep-id`** after clone (else GitHub preview breaks):

```bash
git config filter.nbstripout.clean "/Library/Developer/CommandLineTools/usr/bin/python3 -m nbstripout --keep-id"
git config filter.nbstripout.smudge "cat"
git config diff.ipynb.textconv "/Library/Developer/CommandLineTools/usr/bin/python3 -m nbstripout -t --keep-id"
```

Per-repo only (`.git/config`, not committed). Use your `python3` path if different.

## License

[MIT License](LICENSE) — Copyright (c) 2026 Natalya Myunster.
