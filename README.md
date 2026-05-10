# Machine Learning Journey

Hands-on ML notebooks - from fundamentals to production-ready pipelines.

## Quick Start
```bash
python3 -m pip install pandas notebook
python3 -m notebook
```

Open `week-1/day-1-intro/day1.ipynb`.

## Goal
Learn machine learning from scratch in a practical, notebook-first format.

## Repository Structure
- `week-1/day-1-intro/` - ML basics: terms and first mini dataset.
- `week-1/day-2-pandas/` - data loading and cleaning.
- Progress log: [`LEARNING_LOG.md`](LEARNING_LOG.md)

## Day 1 Completed
- Defined what ML is and how it differs from rule-based `if/else` logic.
- Learned the difference between **Classification** and **Regression**.
- Understood why data is split into train/test.
- Created a mini dataset with `age`, `income`, `bought`.
- Marked features (`age`, `income`) and target (`bought`).

## Day 2 Completed
- Загрузили датасет Titanic (891 строка, 12 колонок)
- Нашли пропуски: Age (177), Cabin (687), Embarked (2)
- Age заполнили медианой, Embarked — самым частым значением, Cabin удалили
- Sex преобразовали в числа: male=0, female=1
- Только 38% пассажиров выжили

## Day 3 Completed

- Загрузили California Housing датасет (20,640 домов)
- Разделили данные: 80% train, 20% test
- Обучили LinearRegression
- MAE модели: 0.53 ($53,000) vs Baseline: 0.91 ($91,000)
- Модель в 2 раза точнее чем просто предсказывать среднее