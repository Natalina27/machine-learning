# Итог недели 3

**Цель:** Git + первые модели scikit-learn; один читаемый мини-проект.

**Задача / данные:** регрессия Diabetes — предсказать прогрессию диабета за год по 10 признакам (`load_diabetes()`, 442 × 10, без пропусков). Split: `test_size=0.2`, `random_state=42`.

**Пайплайн:** EDA → train/test → baseline `DummyRegressor(mean)` → `LinearRegression` → `DecisionTreeRegressor(max_depth=2)` (лучший CV из day 6).

**Метрики на test:**

| Модель | MAE | RMSE | R² |
|--------|-----|------|-----|
| Baseline (mean) | 64.0 | 73.2 | −0.01 |
| LinearRegression | **42.8** | **53.9** | **0.45** |
| DecisionTree (`max_depth=2`) | 49.4 | 61.1 | 0.30 |

**Вывод:** LinearRegression заметно бьёт baseline (~21 по MAE). Ограниченное дерево лучше неограниченного из day 5, но слабее линейной на этом split. Ошибка всё ещё большая (~⅓ типичного `y`).

**За неделю:** Git, постановка задачи, Iris-классификация, метрики регрессии, CV / overfitting / `max_depth`.

**Дальше:** более сильные модели или признаки; проверять через CV.

Ноутбук: `week-3/notebooks/day07_final_project.ipynb`

---

# Week 3 summary

**Goal:** Git + first scikit-learn models; one readable mini-project.

**Task / data:** Diabetes regression — predict 1-year progression from 10 features (`load_diabetes()`, 442 × 10, no missing values). Split: `test_size=0.2`, `random_state=42`.

**Pipeline:** EDA → train/test → `DummyRegressor(mean)` baseline → `LinearRegression` → `DecisionTreeRegressor(max_depth=2)` (best CV from day 6).

**Test metrics:**

| Model | MAE | RMSE | R² |
|-------|-----|------|-----|
| Baseline (mean) | 64.0 | 73.2 | −0.01 |
| LinearRegression | **42.8** | **53.9** | **0.45** |
| DecisionTree (`max_depth=2`) | 49.4 | 61.1 | 0.30 |

**Takeaway:** LinearRegression clearly beats baseline (~21 MAE). Constrained tree beats the unrestricted day-5 tree but loses to linear on this split. Error still large (~⅓ of typical `y`).

**This week:** Git, problem framing, Iris classification, regression metrics, CV / overfitting / `max_depth`.

**Next:** stronger models or features; keep validating with CV.

Notebook: `week-3/notebooks/day07_final_project.ipynb`
