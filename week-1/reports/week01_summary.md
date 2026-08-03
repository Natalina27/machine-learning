# Итог недели 1

**Цель:** ML с нуля → рабочий пайплайн классификации на Titanic.

**Задача / данные:** предсказать `Survived` (0/1). `data/titanic.csv`, 891 × 12. Признаки: Pclass, Sex, Age, SibSp, Parch, Fare.

**Пайплайн:** чистка → train/test → baseline (most frequent) → LogisticRegression / DecisionTree / RandomForest (+ 5-fold CV).

**Метрики:** baseline — accuracy на test; модели — mean ± std accuracy по CV (как в day 7).

| Модель | Accuracy | F1 | Заметки |
|--------|----------|-----|---------|
| Baseline | 0.59 | — | самый частый класс (test) |
| Logistic Regression | 0.78 ± 0.02 | 0.71 | стабильнее по CV |
| Decision Tree | 0.78 ± 0.03 | 0.71 | |
| Random Forest | **0.81 ± 0.05** | **0.75** | лучшая mean accuracy |

**Вывод:** RF бьёт baseline (~+22 п.п. по mean CV). Топ-признаки RF: Fare (~0.30), Sex (~0.27), Age (~0.26). Дальше — feature engineering, тюнинг, бустинг.

Ноутбук: `week-1/notebooks/day7.ipynb`

---

# Week 1 summary

**Goal:** ML from scratch → working Titanic classification pipeline.

**Task / data:** predict `Survived` (`data/titanic.csv`, 891 × 12). Features: Pclass, Sex, Age, SibSp, Parch, Fare.

**Pipeline:** clean → split → baseline → LogisticRegression / DecisionTree / RandomForest (+ 5-fold CV).

**Metrics:** baseline = test accuracy; models = CV mean ± std (as in day 7).

| Model | Accuracy | F1 | Notes |
|-------|----------|-----|-------|
| Baseline | 0.59 | — | most frequent class (test) |
| Logistic Regression | 0.78 ± 0.02 | 0.71 | more stable CV |
| Decision Tree | 0.78 ± 0.03 | 0.71 | |
| Random Forest | **0.81 ± 0.05** | **0.75** | best mean accuracy |

**Takeaway:** RF beats baseline by ~22 pp (CV mean). Top RF features: Fare, Sex, Age. Next: feature engineering, tuning, boosting.

Notebook: `week-1/notebooks/day7.ipynb`
