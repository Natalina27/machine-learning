# Machine Learning Journey

Hands-on ML notebooks — from fundamentals to production-ready pipelines.

## Quick Start
```bash
pip install -r requirements.txt
jupyter notebook
```

Open `week-1/day-1-intro/day1.ipynb`.

## Goal
Learn machine learning from scratch in a practical, notebook-first format.

## Repository Structure
- `week-1/day-1-intro/` — ML basics: terms and first mini dataset
- `week-1/day-2-pandas/` — data loading and cleaning
- `week-1/day-3-regression/` — Linear Regression, MAE/RMSE, baseline
- `week-1/day-4-classification/` — Logistic Regression, confusion matrix, F1
- `week-1/day-5-trees/` — Decision Tree, Random Forest, feature importances
- `week-1/day-6-pipeline/` — Pipeline, StandardScaler, cross-validation
- `week-1/day-7-project/` — final project: full ML pipeline on Titanic
- `resources/` — study plans and reference materials

## Week 1 Results

| Day | Topic | Key Result |
|-----|-------|------------|
| 1 | What is ML | Classification vs Regression, train/test split |
| 2 | Pandas & cleaning | Missing values, encoding |
| 3 | Regression | LinearRegression MAE 0.53 vs Baseline 0.91 |
| 4 | Classification | LogisticRegression accuracy 0.80, F1 0.75 |
| 5 | Trees | Random Forest accuracy 0.80, top feature: Fare |
| 6 | Pipeline | cross-validation 0.78 ± 0.02 |
| 7 | Mini project | RF accuracy 0.81, LR more stable (std 0.02) |