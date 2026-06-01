# Telco Customer Churn Analysis

## Проблема
Телеком-компанія втрачає 24.75% клієнтів щороку. 
Завдання — знайти які фактори найбільше впливають на відтік і побудувати модель для передбачення ризикових клієнтів.

## Дані
- Джерело: [Telco Customer Churn — Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 7,043 клієнти · 21 ознака

## Інструменти
- SQL (MySQL) — exploratory analysis
- Power BI — візуалізація
- Python (pandas, scikit-learn) — ML модель

## Ключові висновки

| Фактор | Група ризику | Churn rate |
|--------|-------------|-----------|
| Тип контракту | Month-to-month | 41.8% |
| Метод оплати | Electronic check | 44.4% |
| Час користування | 0–12 місяців | 47.6% |

Клієнт максимального ризику: **новий + місячний контракт + electronic check + fiber optic**.

## Модель
Logistic Regression (scikit-learn) з `class_weight='balanced'` для роботи з дисбалансом класів.

| Метрика | Результат |
|---------|----------|
| Accuracy | 75.6% |
| Recall (churn) | 82% |
| Precision (churn) | 52% |

Recall пріоритизований над accuracy — для бізнесу важливіше не пропустити клієнта який піде.

## Рекомендації
1. Пропонувати знижку на річний контракт новим клієнтам в перші 3 місяці
2. Стимулювати перехід з electronic check на автоматичну оплату
3. Перевірити якість і ціну fiber optic тарифів — найвищий коефіцієнт відтоку

## Файли
- `model.py` — повний код очистки даних і моделі
- Power BI дашборд — скріншот нижче

## Дашборд
<img width="1371" height="774" alt="dashboard" src="https://github.com/user-attachments/assets/c894c892-c530-445c-b92a-3a4fa36c90e1" />

