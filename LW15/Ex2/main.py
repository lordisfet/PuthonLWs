import pandas as pd
import matplotlib.pyplot as plt

# Читання даних з CSV файлу
df = pd.read_csv('DataBase.csv', parse_dates=['Date'])

# Встановлення колонки 'Date' як індексу датафрейму
df.set_index('Date', inplace=True)

# Додавання колонки 'Total' для підрахунку загальної кількості велосипедистів за день
df['Total'] = df.sum(axis=1)

# Групування даних за місяцями та підрахунок суми велосипедистів за кожен місяць
monthly_totals = df.resample('MS').sum()

# Визначення місяця з найбільшою кількістю велосипедистів
most_popular_month = monthly_totals['Total'].idxmax().month_name()

print(f"Найпопулярніший місяць серед велосипедистів у 2014 році: {most_popular_month}")

# Виведення графіка використання велодоріжок
plt.figure(figsize=(12, 6))
plt.plot(monthly_totals.index, monthly_totals['Total'], marker='o')
plt.title('Використання велодоріжок у 2014 році')
plt.xlabel('Місяць')
plt.ylabel('Кількість велосипедистів')
plt.grid(True)
plt.show()