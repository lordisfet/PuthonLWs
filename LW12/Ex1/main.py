import json

# Створення початкових даних
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

# Збереження даних у JSON файл
with open('students.json', 'w') as f:
    json.dump(students, f)

# Виведення вмісту JSON файлу
with open('students.json', 'r') as f:
    students = json.load(f)
    print(students)

# Додавання нового запису
new_student = {"Name": "Student11", "Gender": "Male", "Height": 195}
students.append(new_student)
with open('students.json', 'w') as f:
    json.dump(students, f)

# Пошук даних за полем
name_to_search = "Student11"
for student in students:
    if student["Name"] == name_to_search:
        print(student)
        break

# Розв'язання завдання
male_height = sum(student["Height"] for student in students if student["Gender"] == "Male")
female_height = sum(student["Height"] for student in students if student["Gender"] == "Female")
result = male_height < female_height

# Запис результату в інший JSON файл
with open('result.json', 'w') as f:
    json.dump({"IsFemaleHeightGreater": result}, f)
