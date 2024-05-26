import pandas as pd
import matplotlib.pyplot as plt

# Словник з даними
students = [
    {"Name": "Student1", "Gender": "Male", "Height": 170},
    {"Name": "Student2", "Gender": "Female", "Height": 160},
    {"Name": "Student3", "Gender": "Male", "Height": 180},
    {"Name": "Student4", "Gender": "Female", "Height": 155},
    {"Name": "Student5", "Gender": "Male", "Height": 175},
    {"Name": "Student6", "Gender": "Female", "Height": 165},
    {"Name": "Student7", "Gender": "Male", "Height": 185},
    {"Name": "Student8", "Gender": "Female", "Height": 150},
    {"Name": "Student9", "Gender": "Male", "Height": 190},
    {"Name": "Student10", "Gender": "Female", "Height": 145}
]

# Перетворення словника на датафрейм
df = pd.DataFrame(students)

# Виведення датафрейму на екран
print(df)

# Агрегація та групування даних за статтю
grouped_df = df.groupby('Gender').agg({'Height': ['mean', 'min', 'max']})

# Виведення результату групування на екран
print(grouped_df)

# Функція для розбиття списку на два списки за вказаним значенням атрибуту
def split_list_by_attribute(lst, attribute, value):
    list_below_value = [item for item in lst if item[attribute] < value]
    list_above_value = [item for item in lst if item[attribute] >= value]
    return list_below_value, list_above_value

# Використання функції для розбиття списку students за зростом 165
list_below_165, list_above_165 = split_list_by_attribute(students, 'Height', 165)

# Друк списків на екран
print("Список учнів зі зростом менше 165:")
print(list_below_165)
print("\nСписок учнів зі зростом 165 і вище:")
print(list_above_165)

# Категорії зросту
height_ranges = ['145-160', '161-175', '176-190']
height_counts = [0, 0, 0]

# Підрахунок кількості учнів в кожній категорії
for student in students:
    if 145 <= student["Height"] <= 160:
        height_counts[0] += 1
    elif 161 <= student["Height"] <= 175:
        height_counts[1] += 1
    elif 176 <= student["Height"] <= 190:
        height_counts[2] += 1

# Кольори для кожної категорії
colors = ['gold', 'yellowgreen', 'lightcoral']

# Створення кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(height_counts, labels=height_ranges, colors=colors, autopct='%1.1f%%', startangle=140)

# Додавання легенди
plt.legend(height_ranges, loc="best")

# Відображення діаграми
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
