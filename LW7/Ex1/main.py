def height_under_new_boy(boys_dict, new_boy_height, new_boy_name):
    for key, name in boys_dict.items():
        if new_boy_height > key:
            print(f"Зріст {boys_dict[key]} сягає {key} та менший за зріст \"новенького\"")

def find_next_boy(boys_dict, new_boy_height):

    for key in boys_dict.keys():
        if key > new_boy_height:
            taller_boys = key
    return taller_boys

def paste_new_boy(boys_dict,new_boy_height, new_boy_name):
    boys_dict[new_boy_height] = new_boy_name
    return sorted(boys_dict.items())

def find_closest_height(boys_dict, height):
    closest_height = min(boys_dict.keys(), key=lambda x: abs(x - height))
    return closest_height, boys_dict[closest_height]

def output_dict(boys_dict):
    print("Список всіх юнаків:")
    for key, value in boys_dict.items():
        print(f"{key}: \'{value}\',")

boys_dict = {
    187: 'Андрій',
    185: 'Сергій',
    184: 'Олег',
    183: 'Юрій',
    182: 'Микола',
    177: 'Дмитро',
    175: 'Іван',
    172: 'Олександр',
    170: 'Петро',
    169: 'Василь'
}

# Створюємо словник функцій
functions = {
    '1': output_dict,
    '2': find_next_boy,
    '3': find_closest_height,
    '4': height_under_new_boy
}

while True:
    print("\n1: Вивести список юнаків")
    print("2: Знайти юнака який вищий \"новенького\"")
    print("3: Знайти найближчий зріст")
    print("4: Вивести юнаків з меншим зростом")
    print("5: Вийти з програми")

    choice = input("\nВведіть номер опції, яку ви хочете використати: ")

    if choice == '5':
        break
    elif choice in functions:
        if choice == '1':
            output_dict(boys_dict)
        if choice == '2':
            new_boy_name = input("\nВведіть ім`я \"новенького\": ")
            new_boy_height = int(input("Введіть зріст новенького в сантиметрах: "))
            # boys_dict = functions[choice](boys_dict, new_boy_height, new_boy_name)
            print(f"Юнак який є найблище до \"новенького\" за стрістом має зріст: {functions[choice](boys_dict, new_boy_height)}")
        elif choice == '3':
            new_boy_height = int(input("Введіть зріст для порівняння: "))
            closest_height, closest_name = functions[choice](boys_dict, new_boy_height)
            print(f"Найближчий до введеного зросту є {closest_name} зі зростом {closest_height} см.")
        elif choice == '4':
            new_boy_name = input("\nВведіть ім`я \"новенького\": ")
            new_boy_height = int(input("Введіть зріст новенького в сантиметрах: "))
            functions[choice](boys_dict, new_boy_height, new_boy_name)
        else:
            functions[choice]
    else:
        print("Невірний вибір. Будь ласка, спробуйте ще раз.")