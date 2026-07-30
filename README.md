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
| `iris.csv` | week-3 day 2 (also via `load_iris()`) |
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

## Week 3 — Iris classification (day 4)

Iris, `train_test_split(test_size=0.2, random_state=42, stratify=y)` — same split as day 2–3.

| Model | Accuracy | Notes |
|-------|----------|-------|
| Baseline (`most_frequent`) | 0.33 | always predicts one class |
| LogisticRegression | 0.97 | 1 error: versicolor → virginica |
| DecisionTreeClassifier | 0.93 | versicolor ↔ virginica confusion |

Notebook: `week-3/notebooks/day04_classification.ipynb`

## Week 3 — Diabetes regression (day 5)

`load_diabetes()`, `train_test_split(test_size=0.2, random_state=42)`. Lower MAE/RMSE is better; higher R² is better.

| Model | MAE | RMSE | R² | Notes |
|-------|-----|------|----|-------|
| Baseline (`DummyRegressor mean`) | 64.0 | 73.2 | −0.01 | always predicts train mean |
| LinearRegression | 42.8 | 53.9 | 0.45 | best model |
| DecisionTreeRegressor | 54.5 | 70.5 | 0.06 | unrestricted tree, weak on test |

Notebook: `week-3/notebooks/day05_regression.ipynb` · plot: `week-3/figures/05_y_true_vs_y_pred_linear_regression.png`

## Week 3 — Validation & CV (day 6)

Diabetes + `DecisionTreeRegressor`, sweep `max_depth = 1, 2, 3, 5, None`. Score = R² (higher is better).

| max_depth | train R² | test R² | CV mean ± std | Notes |
|-----------|----------|---------|---------------|-------|
| 1 | 0.30 | 0.13 | 0.17 ± 0.10 | underfitting |
| **2** | 0.45 | 0.30 | **0.33 ± 0.09** | best CV — chosen |
| 3 | 0.52 | 0.33 | 0.31 ± 0.08 | close second |
| 5 | 0.67 | 0.33 | 0.21 ± 0.09 | gap grows |
| None | 1.00 | 0.06 | −0.15 ± 0.08 | strong overfitting |

Why `max_depth=2`: highest 5-fold CV mean with a moderate train−test gap; unrestricted depth memorizes train.

Notebook: `week-3/notebooks/day06_validation_cv.ipynb` · plot: `week-3/figures/06_max_depth_vs_score.png`

## License

[MIT License](LICENSE) — Copyright (c) 2026 Natalya Myunster.
