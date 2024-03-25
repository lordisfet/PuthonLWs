def height_under_new_boy(boys_dict, new_boy_height, new_boy_name):
    for key, name in boys_dict.items():
        if new_boy_height > key:
            print(f"Зріст {boys_dict[key]} сягає {key} а менший за зріст \"новенького\"")


boys_dict = {
    175: 'Василь',
    176: 'Петро',
    177: 'Олександр',
    178: 'Іван',
    179: 'Дмитро',
    180: 'Микола',
    182: 'Юрій',
    183: 'Олег',
    184: 'Сергій',
    185: 'Андрій'
}

new_boy_name = input("Введіть ім`я \"новенького\": ")
new_boy_height = int(input("Введіть зріст новенького в сантиметрах: "))
height_under_new_boy(boys_dict, new_boy_height,new_boy_name)

"""
for height, name in boys_dict:
    print(f"{height}: \'{name}\',")
"""