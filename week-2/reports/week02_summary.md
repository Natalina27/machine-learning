# Итог недели 2

**Цель:** Python-база под ML — от типов и функций до Pandas / NumPy / Matplotlib.

**Задача / данные:** два мини-EDA на CSV — `data/perfumes.csv` и `data/titanic.csv` (день 7).

**Пайплайн:** загрузка → осмотр (`head` / `info` / `describe`) → чистка пропусков → `groupby` → графики → выводы.

**Ключевые находки:**

| Датасет | Находки |
|---------|---------|
| Perfumes | Floral — максимум продаж; Woody — выше средняя цена; Luxury — лучший рейтинг (~4.77); цены в основном premium |
| Titanic | ~38% выжили; класс и пол сильно связаны с выживаемостью; Age/Embarked заполнены, Cabin удалён; добавлен `FamilySize` |

**Вывод:** уверенно читать CSV, чистить пропуски, делать сводки и простые графики — база для интерпретации моделей.

Ноутбук: `week-2/notebooks/day7.ipynb`

---

# Week 2 summary

**Goal:** Python base for ML — types and functions through Pandas / NumPy / Matplotlib.

**Task / data:** two mini-EDAs on CSV — `data/perfumes.csv` and `data/titanic.csv` (day 7).

**Pipeline:** load → inspect (`head` / `info` / `describe`) → clean missing values → `groupby` → plots → conclusions.

**Key findings:**

| Dataset | Findings |
|---------|----------|
| Perfumes | Floral leads sales; Woody costlier on average; Luxury rated highest (~4.77); mostly premium prices |
| Titanic | ~38% survived; class and sex drive survival; Age/Embarked filled, Cabin dropped; added `FamilySize` |

**Takeaway:** read CSVs, clean gaps, summarize and plot — the base skill for interpreting models later.

Notebook: `week-2/notebooks/day7.ipynb`
