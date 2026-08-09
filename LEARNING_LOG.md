# Learning Log

Progress checklist for this repo. Update here when you complete a day — [README](README.md) links here instead of duplicating status tables.

Study plans: [Week 1 PDF](resources/План_Неделя_1_ML_с_нуля_1.pdf) · [Week 2 PDF](resources/План_Неделя_2_Python_база_под_ML_v2.pdf) · [Week 3 PDF](resources/План_Неделя_3_Git_и_первая_ML_модель.pdf)

**Data:** `data/*.csv` — setup in [README → Data](README.md#data).

## Week 1 — ML from scratch

- [x] Day 1: ML basics — `week-1/notebooks/day1.ipynb`
- [x] Day 2: pandas basics — `week-1/notebooks/day2.ipynb`
- [x] Day 3: regression — `week-1/notebooks/day3.ipynb`
- [x] Day 4: classification and metrics — `week-1/notebooks/day4.ipynb`
- [x] Day 5: trees and random forest — `week-1/notebooks/day5.ipynb`
- [x] Day 6: leakage, overfitting, pipeline — `week-1/notebooks/day6.ipynb`
- [x] Day 7: mini project — `week-1/notebooks/day7.ipynb` — summary `week-1/reports/week01_summary.md`

## Week 2 — Python base for ML

- [x] Day 1: variables, types, strings, errors — `week-2/notebooks/day1.ipynb`
- [x] Day 2: conditions and loops — `week-2/notebooks/day2.ipynb`
- [x] Day 3: collections (list / dict / set) — `week-2/notebooks/day3.ipynb`
- [x] Day 4: functions and clean code — `week-2/notebooks/day4.ipynb`
- [x] Day 5: files and modules — `week-2/notebooks/day5.ipynb`
- [x] Day 6: NumPy basics — `week-2/notebooks/day6.ipynb`
- [x] Day 7: Pandas + Matplotlib EDA — `week-2/notebooks/day7.ipynb` — summary `week-2/reports/week02_summary.md`

## Week 3 — Git + first ML models

- [x] Day 1: Git setup — `week-3/notebooks/day01_git_setup.ipynb`
- [x] Day 2: problem setting — `week-3/notebooks/day02_problem_setting.ipynb` — Iris (`load_iris`), X/y split, train/test 80/20 (120/30), `stratify=y`
- [x] Day 3: EDA + baseline — `week-3/notebooks/day03_eda_baseline.ipynb`
- [x] Day 4: classification — `week-3/notebooks/day04_classification.ipynb` — LogisticRegression 0.97, DecisionTree 0.93 vs baseline 0.33
- [x] Day 5: regression — `week-3/notebooks/day05_regression.ipynb` — Diabetes: LinearRegression MAE 42.8 / R² 0.45 vs baseline MAE 64.0
- [x] Day 6: validation & CV — `week-3/notebooks/day06_validation_cv.ipynb` — Diabetes tree: best `max_depth=2` (CV R² ~0.33); `None` overfits (train 1.0 / CV −0.15)
- [x] Day 7: final project — `week-3/notebooks/day07_final_project.ipynb` — Diabetes: LinearRegression MAE 42.8 / R² 0.45 vs tree `max_depth=2` MAE 49.4 / R² 0.30 vs baseline MAE 64.0; summary `week-3/reports/week03_summary.md`
