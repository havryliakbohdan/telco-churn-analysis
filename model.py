import pandas as pd

df = pd.read_csv('Telco-Customer-Churn.csv')
print(df.shape)
print(df.head())

# Прибираємо непотрібні колонки
df = df.drop(columns=['customerID', 'TotalCharges'])

# Перевіряємо що залишилось
print(df.columns.tolist())
print(df.shape)

# Перевіряємо пропущені значення в кожній колонці
print(df.isnull().sum())

# Перетворюємо текстові колонки у числа
df_encoded = pd.get_dummies(df, drop_first=True)

# Перевіряємо результат
print(df_encoded.shape)
print(df_encoded.columns.tolist())

from sklearn.model_selection import train_test_split

# Розділяємо на ознаки і ціль
X = df_encoded.drop(columns=['Churn_Yes'])
y = df_encoded['Churn_Yes']

# Ділимо на тренувальну і тестову вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f'Тренувальна вибірка: {X_train.shape}')
print(f'Тестова вибірка: {X_test.shape}')

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Створюємо і тренуємо модель
model = LogisticRegression(max_iter=1000, class_weight='balanced')
model.fit(X_train, y_train)

# Передбачаємо на тестових даних
y_pred = model.predict(X_test)

# Оцінюємо точність
print(f'Accuracy: {accuracy_score(y_test, y_pred):.2%}')
print(classification_report(y_test, y_pred))

import pandas as pd

# Важливість ознак
importance = pd.DataFrame({
    'feature': X.columns,
    'coefficient': model.coef_[0]
})

importance = importance.reindex(
    importance['coefficient'].abs().sort_values(ascending=False).index
)

print(importance.head(10))

# Передбачення для кожного клієнта
predictions = pd.DataFrame({
    'ймовірність_відтоку': model.predict_proba(X_test)[:, 1].round(2),
    'передбачення': y_pred,
    'реальність': y_test.values
})

predictions = predictions.sort_values('ймовірність_відтоку', ascending=False)
print(predictions.head(10))
