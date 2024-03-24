import math

def found_z(x):
    return math.exp(x) + math.sqrt(x)

def sum_figure(n):
    sum = 0
    while not (n == 0):
        sum += (n % 10)
        n = n//10
    return sum

print("Доступні дії:")
print("Введіть '1' для розрахунку значення рівнянння(z = e^x + √x)")
print("Введіть '2' для розрахунку суми цифр числа n\n")

act = 0

while act != 1 and act != 2:
    act = int(input("Виберіть дію: "))
    if (act == 1):
        print("Ви вибрали розрахунок значення рівнянння(z = e^x + √x)")
        x = int(input("Ведіть значення х: "))
        z = found_z(x)
        print(f"z = {z}")
    elif (act == 2):
        print("Ви вибрали розрахунок суми цифр числа n")
        n = int(input("Ведіть значення n: "))
        sum = sum_figure(n)
        print(f"sum = {sum}")
    else:
        print("Ви ввели число відмінне від 1 та 2!!!")
        print("Спробуйте ще раз)))\n")